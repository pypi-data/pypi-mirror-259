import click


@click.group()
def cli():
    pass


from mysnippet.cli_config import config
cli.add_command(config)


from mysnippet.cli_encrypt import encrypt
cli.add_command(encrypt)


from mysnippet.cli_project import project
cli.add_command(project)


from mysnippet.cli_snippet import snippet
cli.add_command(snippet)


cli()
