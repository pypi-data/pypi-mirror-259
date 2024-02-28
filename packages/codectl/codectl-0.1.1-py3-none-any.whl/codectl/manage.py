"""A command-line tool for generating code based on templates."""

from pathlib import Path
import json
from typing import Union, Optional
import click
from codectl import compiler, settings
from codectl import utils


@click.group()
def cli():
    """
    Base command group for the CLI application.
    """
    pass


@cli.command()
@click.option("--set", is_flag=True, help="Set configuration options.")
@click.option("--show", is_flag=True, help="Show current configuration.")
@click.option(
    "--template-dir",
    type=click.Path(exists=True, file_okay=False),
    help="Specify a template directory.",
)
def config(set: bool, show: bool, **kwargs: dict):
    """Manage application configuration settings.

    Allows setting new configuration options or displaying the current configuration.
    """
    user_config = utils.get_user_config()

    if set:
        for key, value in kwargs.items():
            if value is not None:
                user_config[key] = value
        settings.CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        settings.CONFIG_PATH.write_text(json.dumps(user_config))
        if not show:
            click.secho("Done.", fg="green")

    if show:
        click.secho(json.dumps(user_config, indent=2), fg="green")


@cli.command()
@click.argument("scope")
@click.option("--rename", help="")
@click.option(
    "--template-dir",
    type=click.Path(exists=True, file_okay=False),
    help="Specify the template directory.",
)
@click.option(
    "--data",
    "-d",
    multiple=True,
    type=str,
    help="Additional data for templates in key=value format.",
)
def new(
    scope: str,
    template_dir: str | Path,
    rename: str | None,
    data: tuple,
):
    """Create new items based on templates and scope.

    Generates files or projects from templates located in a specified directory and scope.
    """
    user_config = utils.get_user_config()

    if not template_dir:
        user_template_dir = user_config.get("template_dir")
        template_dir = (
            Path(user_template_dir) if user_template_dir else settings.TEMPLATE_DIR
        )
    else:
        template_dir = Path(template_dir)

    template_dir.mkdir(parents=True, exist_ok=True)

    scope_path = template_dir / scope
    if not scope_path.exists():
        click.secho(
            f"Scope `{scope}` does not exist in the template directory.", fg="red"
        )
        return

    extra_data = dict((item.split('=') for item in data))
    compiler.process_directory(scope_path, rename, extra_data)
    click.secho("Done.", fg="green")


if __name__ == "__main__":
    cli()

"""debug cases
python codectl/manage.py config --help
python codectl/manage.py config --set
python codectl/manage.py config --show
python codectl/manage.py config --set --template-dir ~/workspace/code/codectl/templates --show

python codectl/manage.py new --help
python codectl/manage.py new codectl/manage.py new api --data service_name=v1 --rename v1-api
$cwd=${workspaceFolder}/out; python ../codectl/manage.py new api --template-dir ~/workspace/code/codectl/templates --data service_name=v1
$cwd=${workspaceFolder}/out; python ../codectl/manage.py new api --template-dir ~/workspace/code/codectl/templates --data service_name=v1 --rename v1
$cwd=${workspaceFolder}/out; python ../codectl/manage.py new rpc --template-dir ~/workspace/code/codectl/templates --data service_name=authz --rename authz
python codectl/manage.py new api --template-dir ~/.codectl/templates
"""
