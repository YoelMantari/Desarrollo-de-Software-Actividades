import json
import pytest
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'network_config.json')

@ pytest.fixture(scope="module")
def conf():
    return json.load(open(CONFIG_FILE))

def test_schema_keys(conf):
    assert isinstance(conf, dict)
    assert 'resources' in conf
    for res in conf['resources']:
        assert 'type' in res and 'name' in res
