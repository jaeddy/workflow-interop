import click

from . import run_job


@click.group()
def run():
    """
    Retrieve and run workflows.
    """
    pass


@run.command('single')
def orchestrate_submission():
    """
    Run a workflow job in a single environment.
    """
    pass


@run.command('multi')
def orchestrate_queue():
    """
    Run all workflow jobs in a queue in a single environment.
    """
    pass


