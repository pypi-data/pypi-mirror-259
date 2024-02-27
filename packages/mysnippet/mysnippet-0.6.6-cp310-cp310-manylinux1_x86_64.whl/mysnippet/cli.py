import click


@click.group()
def cli():
    pass


from cli_config import config
cli.add_command(config)


from cli_encrypt import encrypt
cli.add_command(encrypt)


from cli_project import project
cli.add_command(project)


from cli_snippet import snippet
cli.add_command(snippet)


cli()



