# 基于jinja2模板，生成项目模板

import os
import json
import fnmatch
import logging
import shutil
from pathlib import Path
from binaryornot.check import is_binary
from jinja2 import FileSystemLoader, Environment
from jinja2.exceptions import UndefinedError
from mysnippet.util.tool import work_in, ContextImportRepo2Path, make_sure_path_exists
from mysnippet.util.hjinja2 import StrictEnvironment
from mysnippet.util.hclick import prompt_for_config


logger = logging.getLogger(__name__)


def apply_overwrites_to_context(context: dict, overwrite_context: dict):
    for variable, overwrite in overwrite_context.items():
        if variable not in context:
            continue
        context_value = context[variable]
        if isinstance(context_value, list):
            if overwrite in context_value:
                context_value.remove(overwrite)
                context_value.insert(0, overwrite)
            else:
                raise ValueError(
                    f"{overwrite} provided for choice variable {variable}, "
                    f"but the choices are {context_value}."
                )
        elif isinstance(context_value, dict) and isinstance(overwrite, dict):
            apply_overwrites_to_context(context_value, overwrite)
            context[variable] = context_value
        else:
            context[variable] = overwrite


def is_copy_only_path(path, context):
    try:
        for dont_render in context['mysnippet']['_copy_without_render']:
            if fnmatch.fnmatch(path, dont_render):
                return True
    except KeyError:
        return False
    return False


def generate_dir(dirname: str, context: dict, output_dir: "os.PathLike[str]", environment: Environment):
    name_tmpl = environment.from_string(dirname)
    rendered_dirname = name_tmpl.render(**context)
    dir_to_create = Path(output_dir, rendered_dirname)
    if dir_to_create.exists():
        msg = f'Error: "{dir_to_create}" directory already exists'
        raise Exception(msg)
    else:
        make_sure_path_exists(dir_to_create)
    return dir_to_create


def generate_file(project_dir: "os.PathLike[str]", infile, context: dict, env: Environment):
    logger.info('Processing file %s', infile)
    outfile = os.path.join(project_dir, env.from_string(infile).render(**context))
    file_name_is_empty = os.path.isdir(outfile)
    if file_name_is_empty:
        logger.debug('The resulting file name is empty: %s', outfile)
        return
    if os.path.exists(outfile):
        raise Exception()

    logger.debug('Created file at %s', outfile)

    # Just copy over binary files. Don't render.
    logger.debug("Check %s to see if it's a binary", infile)
    if is_binary(infile):
        logger.debug('Copying binary %s to %s without rendering', infile, outfile)
        shutil.copyfile(infile, outfile)
    else:
        # Force fwd slashes on Windows for get_template
        # This is a by-design Jinja issue
        infile_fwd_slashes = infile.replace(os.path.sep, '/')
        # Render the file
        tmpl = env.get_template(infile_fwd_slashes)
        rendered_file = tmpl.render(**context)

        # Detect original file newline to output the rendered file
        # note: newline='' ensures newlines are not converted
        with open(infile, encoding='utf-8', newline='') as rd:
            rd.readline()  # Read the first line to load 'newlines' value
            # Use `_new_lines` overwrite from context, if configured.
            newline = rd.newlines
            if context['mysnippet'].get('_new_lines', False):
                newline = context['mysnippet']['_new_lines']
                logger.debug('Overwriting end line character with %s', newline)
        logger.debug('Writing contents to file %s', outfile)
        with open(outfile, 'w', encoding='utf-8', newline=newline) as fh:
            fh.write(rendered_file)

    shutil.copymode(infile, outfile)


class Project:
    def __init__(
            self,
            config: dict,
            template: str,
            template_dir: "os.PathLike[str]",
            output_dir: str,
            project_name: str=None,
            extra_context: dict = None):

        # 判断模板路径是否存在；判断是否存在mysnippet.json配置文件
        if not os.path.exists(template_dir) or not os.path.exists(os.path.join(template_dir, "mysnippet.json")):
            raise Exception(f"please check template {template_dir}")

        self.import_patch = ContextImportRepo2Path(template_dir)    # 创建上下文管理器，将项目模板放到sys.path
        self.template = template
        self.template_dir = template_dir
        self.config = config
        self.output_dir = output_dir
        self.extra_context = extra_context
        if project_name:
            self.prompt_config_default = dict(project_name=project_name)
        else:
            self.prompt_config_default = None

    def generate(self):
        # 处理上下文
        self.generate_context()

        # 生成文件夹和文件
        with self.import_patch:
            return self.generate_project()

    def generate_context(self):
        def _generate_context(context_file: str, default_context: dict = None, extra_context: dict = None):
            context = dict()
            with open(context_file, encoding='utf-8') as file_handle:
                obj = json.load(file_handle, object_pairs_hook=dict)
            file_name = os.path.split(context_file)[1]
            context[file_name.split('.')[0]] = obj    # context['mysnippet']

            if default_context:
                apply_overwrites_to_context(obj, default_context)
            if extra_context:
                apply_overwrites_to_context(obj, extra_context)

            logger.info('Context generated is %s', context)
            return context

        context_file = os.path.join(self.template_dir, 'mysnippet.json')
        logger.info('context_file is %s', context_file)
        context = _generate_context(
            context_file=context_file,
            default_context=self.config['default_context'],
            extra_context=self.extra_context,
        )

        with self.import_patch:
            context['mysnippet'] = prompt_for_config(context, self.prompt_config_default)

        context['mysnippet']['_mysnippet_template_dir'] = self.config['template_dir']
        context['mysnippet']['_template'] = self.template
        context['mysnippet']['_template_dir'] = self.template_dir
        context['mysnippet']['_output_dir'] = self.output_dir
        self.context = context

        # Create project from local context and project template.

    def generate_project(self):
        envvars = self.context.get('mysnippet', {}).get('_jinja2_env_vars', {})
        env = StrictEnvironment(context=self.context, keep_trailing_newline=True, **envvars)

        template_dir = Path(self.template_dir, "{{mysnippet.project_slug}}")
        logger.info('Generating project from %s...', template_dir)
        unrendered_dir = os.path.split(template_dir)[1]
        project_dir = generate_dir(unrendered_dir, self.context, self.output_dir, env)
        project_dir = os.path.abspath(project_dir)
        logger.info('Project directory is %s', project_dir)

        # with work_in(template_dir):
        #     run_hook('pre_gen_project', project_dir, context)

        with work_in(template_dir):
            env.loader = FileSystemLoader(['.', '../templates'])

            for root, dirs, files in os.walk('.'):
                copy_dirs = []
                render_dirs = []

                for d in dirs:
                    d_ = os.path.normpath(os.path.join(root, d))
                    if is_copy_only_path(d_, self.context):
                        copy_dirs.append(d)
                    else:
                        render_dirs.append(d)

                # 只复制文件夹，不渲染
                for copy_dir in copy_dirs:
                    indir = os.path.normpath(os.path.join(root, copy_dir))
                    outdir = os.path.normpath(os.path.join(project_dir, indir))
                    outdir = env.from_string(outdir).render(**self.context)
                    logger.info('Copying dir %s to %s without rendering', indir, outdir)
                    if os.path.isdir(outdir):
                        shutil.rmtree(outdir)
                    shutil.copytree(indir, outdir)

                # 需要渲染的文件夹
                # We mutate ``dirs``, because we only want to go through these dirs recursively
                dirs[:] = render_dirs
                for d in dirs:
                    unrendered_dir = os.path.join(project_dir, root, d)
                    generate_dir(unrendered_dir, self.context, self.output_dir, env)

                # 处理文件
                for f in files:
                    infile = os.path.normpath(os.path.join(root, f))
                    if is_copy_only_path(infile, self.context):
                        # 不需要渲染的文件
                        outfile_rendered = env.from_string(infile).render(**self.context)
                        outfile = os.path.join(project_dir, outfile_rendered)
                        logger.info('Copying file %s to %s without rendering', infile, outfile)
                        shutil.copyfile(infile, outfile)
                        shutil.copymode(infile, outfile)
                        continue

                    # 需要渲染的文件
                    try:
                        generate_file(project_dir, infile, self.context, env)
                    except UndefinedError as err:
                        msg = f"Unable to create file '{infile}'"
                        raise Exception(msg, err, self.context) from err

        # with work_in(template_dir):
        #     run_hook('post_gen_project', project_dir, context)

        return project_dir

