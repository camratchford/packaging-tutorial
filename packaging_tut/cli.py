import os
import logging
from pathlib import Path

import click
from packaging_tut.config import config
from packaging_tut.__main__ import main

logger = logging.getLogger("__name__")

base_dir = Path(__file__).resolve().parent
cwd = Path(os.getcwd())


@click.command()
@click.option(
    "--config-file",
    envvar="CONF",
    type=str,
    default=f"{cwd}/config.yml",
    help="The location of the yaml configuration file",
    show_default=True,
)
def run(config_file):
    config.configure_from_file(config_file)
    main(config)
