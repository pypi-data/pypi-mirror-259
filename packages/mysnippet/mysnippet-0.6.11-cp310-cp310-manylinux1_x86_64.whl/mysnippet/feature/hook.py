import errno
import logging
import os
import subprocess
import sys
import tempfile

from mysnippet.util.tool import make_executable
from mysnippet.util.hjinja2 import StrictEnvironment

logger = logging.getLogger(__name__)

_HOOKS = [
    'pre_gen_project',
    'post_gen_project',
]
EXIT_SUCCESS = 0


def valid_hook(hook_file, hook_name):
    filename = os.path.basename(hook_file)
    basename = os.path.splitext(filename)[0]

    matching_hook = basename == hook_name
    supported_hook = basename in _HOOKS
    backup_file = filename.endswith('~')

    return matching_hook and supported_hook and not backup_file


def find_hook(hook_name, hooks_dir='../hook'):
    if not os.path.isdir(hooks_dir):
        return None
    scripts = []
    for hook_file in os.listdir(hooks_dir):
        if valid_hook(hook_file, hook_name):
            scripts.append(os.path.abspath(os.path.join(hooks_dir, hook_file)))
    if len(scripts) == 0:
        return None
    return scripts


def run_script(script_path, cwd='.'):
    run_thru_shell = sys.platform.startswith('win')
    if script_path.endswith('.py'):
        script_command = [sys.executable, script_path]
    else:
        script_command = [script_path]

    make_executable(script_path)
    try:
        proc = subprocess.Popen(script_command, shell=run_thru_shell, cwd=cwd)  # nosec
        exit_status = proc.wait()
        if exit_status != EXIT_SUCCESS:
            raise Exception(
                f'Hook script failed (exit status: {exit_status})'
            )
    except OSError as err:
        if err.errno == errno.ENOEXEC:
            raise Exception(
                'Hook script failed, might be an empty file or missing a shebang'
            ) from err
        raise Exception(f'Hook script failed (error: {err})') from err


def run_script_with_context(script_path, cwd, context):
    _, extension = os.path.splitext(script_path)

    with open(script_path, encoding='utf-8') as file:
        contents = file.read()

    with tempfile.NamedTemporaryFile(delete=False, mode='wb', suffix=extension) as temp:
        env = StrictEnvironment(context=context, keep_trailing_newline=True)
        template = env.from_string(contents)
        output = template.render(**context)
        temp.write(output.encode('utf-8'))

    run_script(temp.name, cwd)


def run_hook(hook_name, project_dir, context):
    scripts = find_hook(hook_name)
    if not scripts:
        logger.debug('No %s hook found', hook_name)
        return
    logger.debug('Running hook %s', hook_name)
    for script in scripts:
        run_script_with_context(script, project_dir, context)
