import click

from . import show


@click.group()
def config():
    """
    Manage app configuration.
    """
    pass


@config.command('show')
def show_config():
    """
    Show current testbed/orchestrator configuration.
    """
    show()


@config.command('add-queue')
@click.option('--data')
def add_queue(data):
    """
    Add a workflow queue.
    """
    pass


@config.command('add-trs')
@click.option('--data')
def add_trs(data):
    """
    Add a Tool Registry Service endpoint.
    """
    pass


@config.command('add-wes')
@click.option('--data')
def add_wes(data):
    """
    Add a Workflow Execution Service endpoint.
    """
    pass

