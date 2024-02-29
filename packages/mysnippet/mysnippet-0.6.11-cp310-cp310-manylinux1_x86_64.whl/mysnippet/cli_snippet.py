import json
import os
import shutil

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
def snippet(language, template):
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
    path = os.path.join(path, "snippet")

    if not os.path.exists(path):
        print("不存在该语言的snippet")
        return

    if len(os.listdir(path)) == 0:
        print("该语言snippet为空")
        return

    # template
    if template is None:
        template = click_prompt_choice("template", filter(os.listdir(path)))
    path = os.path.join(path, template)

    if not os.path.exists(path):
        print("不存在该语言的该模板")
        return

    for file in os.listdir(path):
        if os.path.exists(file):
            raise Exception(f"{file} exists, please check")
        else:
            print("copy file", file)
            shutil.copy(os.path.join(path, file), os.path.abspath(""))
