#!/usr/bin/env python
import os
import sys
import logging
import pkg_resources

import click

from logging.config import fileConfig

from .config import commands as config_group

config_path = os.path.dirname(os.path.realpath(__file__))
fileConfig(os.path.join(config_path, 'logging_config.ini'),
           disable_existing_loggers=False)
logger = logging.getLogger()
logger.info("Starting `ga4gh-testbed`")


@click.group()
@click.option('--quiet', 'verbosity', flag_value='quiet',
              help=("Only display printed outputs in the console - "
                    "i.e., no log messages."))
@click.option('--debug', 'verbosity', flag_value='debug',
              help="Include all debug log messages in the console.")
def main(verbosity):
    """
    Command line interface for the `wfinterop` library.
    """
    if verbosity == 'quiet':
        logger.setLevel(logging.ERROR)
    elif verbosity == 'debug':
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

main.add_command(config_group.config)


if __name__ == '__main__':
    main()
