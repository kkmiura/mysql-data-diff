import click
from mysql_data_diff.version import __version__

@click.command(no_args_is_help=True)
@click.option("--version", is_flag=True, help="Print version info and exit")
def main(**kw) -> None:
    if kw["version"]:
        print(f"v{__version__}")
    pass

if __name__ == "__main__":
    main()