import click
import pathlib
import rich


from . import aci_convert
from . import stl_split

@click.group()
def cli():
    pass

@cli.command()
@click.option('-t', '--template', default=None, help='Jinja2 template file to use for the conversion. If not provided, the default template will be used.')
@click.option('-o', '--output-anyscript', default=None, help='Output file name. If not provided, the input file name will be used with the extension changed to .any.')
@click.argument('input-aci', nargs=1, type=click.Path(exists=True))
def aci(input_aci, output_anyscript, template):
    """Convert ACI file data to AnyScript file."""
    if output_anyscript is None:
        output_anyscript = pathlib.Path(input_aci).with_suffix('.any')
    aci_convert.main(input_aci, output_anyscript, template)

@cli.command()
@click.argument('files', nargs=-1)
def stl(files):
    """Split composite STL files into separate files."""
    for fn in files:
        stl_split.splitfile(fn)


if __name__ == "__main__":
    cli()