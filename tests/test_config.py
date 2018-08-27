import logging
import pytest
import yaml
import textwrap

from synorchestrator.config import queue_config
from synorchestrator.config import trs_config
from synorchestrator.config import wes_config
from synorchestrator.config import add_queue
from synorchestrator.config import add_toolregistry
from synorchestrator.config import add_workflowservice
from synorchestrator.config import set_yaml
from synorchestrator.config import show

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def mock_orchestratorconfig(tmpdir):
    # a mocked config file for a the orchestrator app
    logger.info("[setup] mock orchestrator config file, create local file")

    mock_config_text = """
    queues:
      wf1: {}
      wf2: {}

    toolregistries:
      trs1: {}
      trs2: {}

    workflowservices:
      wes1: {}
      wes2: {}
    """
    mock_config_file = tmpdir.join('config.yaml')
    logger.debug("writing config file: {}".format(str(mock_config_file)))
    mock_config_file.write(textwrap.dedent(mock_config_text))

    yield mock_config_file

    logger.info("[teardown] mock orchestrator config file, remove file")


def test_queue_config(mock_orchestratorconfig, monkeypatch):
    # GIVEN an orchestrator config file exists
    monkeypatch.setattr('synorchestrator.config.config_path', 
                        str(mock_orchestratorconfig))

    # WHEN the configuration data in the file is loaded
    test_config = queue_config()

    # THEN the returned object is correctly parsed from the YAML stream
    assert(
        test_config == {
            'wf1': {},
            'wf2': {}
        }
    )


def test_trs_config(mock_orchestratorconfig, monkeypatch):
    # GIVEN an orchestrator config file exists
    monkeypatch.setattr('synorchestrator.config.config_path', 
                        str(mock_orchestratorconfig))
    
    # WHEN the configuration data in the file is loaded
    test_config = trs_config()

    # THEN the returned object is correctly parsed from the YAML stream
    assert(
        test_config == {
            'trs1': {},
            'trs2': {}
        }
    )


def test_wes_config(mock_orchestratorconfig, monkeypatch):
    # GIVEN an orchestrator config file exists
    monkeypatch.setattr('synorchestrator.config.config_path', 
                        str(mock_orchestratorconfig))
    
    # WHEN the configuration data in the file is loaded
    test_config = wes_config()

    # THEN the returned object is correctly parsed from the YAML stream
    assert(
        test_config == {
            'wes1': {},
            'wes2': {}
        }
    )


def test_add_queue(mock_orchestratorconfig, monkeypatch):
    # GIVEN an orchestrator config file exists
    monkeypatch.setattr('synorchestrator.config.config_path', 
                        str(mock_orchestratorconfig))
    
    # WHEN an evaluation queue is added to the configuration of the
    # workflow orchestrator app
    add_queue(
        wf_id='mock_wf',
        version_id='develop',
        wf_type=''
    )

    mock_config = {'workflow_id': 'mock_wf',
                   'version_id': 'develop',
                   'workflow_type': '',
                   'trs_id': 'dockstore',
                   'wes_default': 'local',
                   'wes_opts': ['local']}

    # THEN the evaluation queue config should be stored in the config file
    with open(str(mock_orchestratorconfig), 'r') as f:
        test_config = yaml.load(f)['queues']

    assert('mock_wf__develop' in test_config)
    assert(test_config['mock_wf__develop'] == mock_config)


def test_add_toolregistry(mock_orchestratorconfig, monkeypatch):
    # GIVEN an orchestrator config file exists
    monkeypatch.setattr('synorchestrator.config.config_path', 
                        str(mock_orchestratorconfig))

    # WHEN a TRS endpoint is added to the configuration of the
    # workflow orchestrator app
    add_toolregistry(
        service='mock_trs',
        auth='',
        auth_type='',
        host='',
        proto=''
    )

    mock_config = {'auth': '',
                   'auth_type': '',
                   'host': '',
                   'proto': ''}

    # THEN the TRS config should be stored in the config file
    with open(str(mock_orchestratorconfig), 'r') as f:
        test_config = yaml.load(f)['toolregistries']

    assert('mock_trs' in test_config)
    assert(test_config['mock_trs'] == mock_config)


def test_add_workflowservice(mock_orchestratorconfig, monkeypatch):
    # GIVEN an orchestrator config file exists
    monkeypatch.setattr('synorchestrator.config.config_path', 
                        str(mock_orchestratorconfig))
    
    # WHEN a WES endpoint is added to the configuration of the
    # workflow orchestrator app
    add_workflowservice(
        service='mock_wes',
        auth='',
        auth_type='',
        host='',
        proto=''
    )

    mock_config = {'auth': '',
                   'auth_type': '',
                   'host': '',
                   'proto': ''}

    # THEN the WES config should be stored in the config file
    with open(str(mock_orchestratorconfig), 'r') as f:
        test_config = yaml.load(f)['workflowservices']

    assert('mock_wes' in test_config)
    assert(test_config['mock_wes'] == mock_config)


def test_set_yaml(mock_orchestratorconfig, monkeypatch):
    # GIVEN an orchestrator config file exists
    monkeypatch.setattr('synorchestrator.config.config_path', 
                        str(mock_orchestratorconfig))
    
    # WHEN the config is set for a given section and service
    set_yaml(
        section='mock_section',
        service='mock_service',
        var2add={}
    )

    # THEN the config should be stored under the correct section and service
    with open(str(mock_orchestratorconfig), 'r') as f:
        test_config = yaml.load(f)

    assert('mock_section' in test_config)
    assert('mock_service' in test_config['mock_section'])
    assert(test_config['mock_section']['mock_service'] == {})
