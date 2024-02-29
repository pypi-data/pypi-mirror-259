import json
import os
import click
import logging
from mysnippet.util.tool import configure_logger
from mysnippet.util.hclick import click_prompt_choice
from mysnippet.project import Project


logger = logging.getLogger(__name__)


_app_config_filename = os.path.join(os.path.expanduser("~"), ".mysnippet.conf.json")
if os.path.exists(_app_config_filename):
    APP_CONFIG = json.load(open(_app_config_filename))
else:
    APP_CONFIG = {"default_context": {}}


@click.command()
@click.option("-l", "--language",type=str, default=None, help="编程语言")
@click.option("-t", "--template",type=str, default=None, help="模板名称")
@click.option("-o", "--output",type=str, default=None, help="输出目录")
@click.option("-n", "--name", type=str, default=None, help="项目名称，指定后创建项目时候项目名外参数将用默认值")
def project(language, template, output, name):
    configure_logger(stream_level='INFO')

    def filter(_l):
        return [v for v in _l if v[0] not in ('.', '_') and v != 'clip']

    # language
    if language is None:
        language = click_prompt_choice("language", filter(os.listdir(APP_CONFIG['template_dir'])))
    path = os.path.join(APP_CONFIG['template_dir'], language)

    # type
    # if stype is None:
    #    stype = click_prompt_choice("type", _filter_template_name(os.listdir(_path)))
    path = os.path.join(path, "project")

    # template
    if template is None:
        template = click_prompt_choice("template", filter(os.listdir(path)))
    path = os.path.join(path, template)


    # check path
    if not os.path.exists(path):
        raise Exception(f"failed with param language={language}, template={template}")

    if output is not None and not os.path.exists(output):
        raise Exception(f"output={output} not exists")

    obj = Project(APP_CONFIG, template, path, output if output else os.path.abspath(""), project_name=name)
    print(obj.generate())
