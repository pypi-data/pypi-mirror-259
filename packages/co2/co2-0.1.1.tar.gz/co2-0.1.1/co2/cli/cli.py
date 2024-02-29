import typer

import importlib
import pkgutil


discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg
    in pkgutil.iter_modules()
    if name.startswith('co2_')
}

cli = typer.Typer(no_args_is_help=True)

for plugin in discovered_plugins.values():
    cli.add_typer(plugin.cli)

@cli.command()
def hello():
    print("Hello")
    
@cli.command()
def goodbye():
    print("Goodbye")