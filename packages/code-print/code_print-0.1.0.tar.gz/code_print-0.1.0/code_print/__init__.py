import click

from .libs.click_order import CustomOrderGroup
from .libs.print_dir import print_file_info


@click.command(
    cls=CustomOrderGroup,
    order=[],
)
def code_print():
    click.echo("code print is print all code in directory")


@code_print.command("print_dir", help="Print Files in Specific Directory")
@click.argument("dirpath")
@click.option(
    "--ext", "-e", "exts", help="출력하려는 확장자", multiple=True, required=True
)
def run_print_dir(dirpath, exts):
    """
    run_print_dir 디렉토리내에서 지정한 확장자에 대해서만 출력

    _extended_summary_

    :param dirpath: 출력하려는 디렉토리
    :type dirpath: str
    :param ext: 출력하려는 확장자
    :type ext: str
    """
    exts = list(exts)
    click.echo(f"==>dirpath: {dirpath}, ext:{exts}")
    print_file_info(dirpath, exts=exts)
