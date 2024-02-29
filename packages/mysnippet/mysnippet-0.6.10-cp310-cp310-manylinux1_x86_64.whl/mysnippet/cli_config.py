import os
import click
import json

@click.command()
def config():
    # 配置模板文件夹路径

    config_filename = os.path.join(os.path.expanduser("~"), ".mysnippet.conf.json")
    app_config = json.load(open(config_filename)) if os.path.exists(config_filename) else {"default_context": {}}

    # 判断当前配置位置
    default_dir = os.path.join(os.path.expanduser('~'), ".mysnippet-template")
    if "template_dir" in app_config and os.path.exists(app_config['template_dir']):
        default_dir = app_config['template_dir']

    # 输入位置
    p = click.prompt("template_dir", default=default_dir)
    if os.path.exists(p):
        app_config['template_dir'] = os.path.abspath(p)
        print(app_config)
        with open(config_filename, "w") as outfile:
            json.dump(app_config, outfile, indent=2, sort_keys=True)
    else:
        raise Exception(f"dir '{p}' not exists, please check")

