import functools
import json

import click
from jinja2 import Environment
from mysnippet.util.hjinja2 import StrictEnvironment


def click_prompt_choice(var_name, options):
    if not isinstance(options, list):
        raise TypeError
    if not options:
        raise ValueError
    choice_map = dict((f'{i}', value) for i, value in enumerate(options, 1))
    choices = choice_map.keys()
    default = '1'
    choice_lines = ['\t{} - {}'.format(*c) for c in choice_map.items()]
    prompt = '\n'.join(
        (
            f"Select {var_name}:",
            "\n".join(choice_lines),
            f"Choose from {', '.join(choices)}",
        )
    )
    user_choice = click.prompt(
        prompt, type=click.Choice(choices), default=default, show_choices=False
    )
    return choice_map[user_choice]


def read_user_dict(var_name, default_value):
    def process_json(user_value, default_value=None):
        if user_value == 'default':
            return default_value
        try:
            user_dict = json.loads(user_value, object_pairs_hook=dict)
        except Exception as error:
            raise click.UsageError('Unable to decode to JSON.') from error
        if not isinstance(user_dict, dict):
            raise click.UsageError('Requires JSON dict.')
        return user_dict

    if not isinstance(default_value, dict):
        raise TypeError
    user_value = click.prompt(
        var_name,
        default='default',
        type=click.STRING,
        value_proc=functools.partial(process_json, default_value=default_value),
    )
    if click.__version__.startswith("7.") and user_value == 'default':
        return default_value
    return user_value


def prompt_for_config(context, default: dict = None):
    if default:
        # 便于脚本自动生成项目，指定project_name，其他都用默认
        assert 'project_name' in default

    def _render_variable(env: Environment, raw, mysnippet_dict: dict):
        if raw is None or isinstance(raw, bool):
            return raw
        elif isinstance(raw, dict):
            return {
                _render_variable(env, k, mysnippet_dict): _render_variable(env, v, mysnippet_dict)
                for k, v in raw.items()
            }
        elif isinstance(raw, list):
            return [_render_variable(env, v, mysnippet_dict) for v in raw]
        elif not isinstance(raw, str):
            raw = str(raw)
        template = env.from_string(raw)
        return template.render(mysnippet=mysnippet_dict)

    mysnippet_dict = dict()
    env = StrictEnvironment(context=context)
    for key, raw in context['mysnippet'].items():
        if key.startswith('_') and not key.startswith('__'):
            mysnippet_dict[key] = raw
            continue
        elif key.startswith('__'):
            mysnippet_dict[key] = _render_variable(env, raw, mysnippet_dict)
            continue

        if isinstance(raw, list):
            val = click_prompt_choice(key, [_render_variable(env, _v, mysnippet_dict) for _v in raw])
            mysnippet_dict[key] = val
        elif isinstance(raw, bool):
            mysnippet_dict[key] = click.prompt(key, default=raw, type=click.BOOL)
        elif not isinstance(raw, dict):
            val = _render_variable(env, raw, mysnippet_dict)
            if default:
                if key == 'project_name':
                    mysnippet_dict[key] = default['project_name']
                else:
                    mysnippet_dict[key] = val
            else:
                mysnippet_dict[key] = click.prompt(key, default=val)

    # TODO 对dict再处理？
    for key, raw in context['mysnippet'].items():
        if key.startswith('_') and not key.startswith('__'):
            continue
        if isinstance(raw, dict):
            val = _render_variable(env, raw, mysnippet_dict)
            if not key.startswith('__'):
                val = read_user_dict(key, val)
            mysnippet_dict[key] = val

    return mysnippet_dict
