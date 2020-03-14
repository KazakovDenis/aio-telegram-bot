import pytest


@pytest.fixture(autouse=True, scope='session')
def config():
    """Creates an instance of an object"""
    config = object
    return config


def setup_module():
    pass


def teardown_module():
    pass
