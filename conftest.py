# coding: UTF-8

import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.imdb_navigator import IMDbNavigator


def pytest_addoption(parser):
    parser.addoption("--cfg", action="store", help="path to configuration file")


def load_yaml(configuration_file_path):
    # yaml package needed only in case if configuration file is in yaml format
    import yaml

    try:
        cfg_file = open(configuration_file_path, 'r')
    except BaseException as e:
        raise ConfigurationException('Can not open configuration file', e)

    try:
        parsed_configuration = yaml.load(cfg_file)
    except BaseException as e:
        raise ConfigurationException('A problem occured while parsing configuration file', e)
    finally:
        cfg_file.close()

    return parsed_configuration


@pytest.fixture(scope='module')
def config(request):
    '''Returns content of configuration file.
       Now supports only yaml format'''
    configuration_file_path = request.config.getoption("--cfg")

    if configuration_file_path == None:
        parsed_configuration = {}
    else:
        configuration_file_name, configuration_file_type = os.path.splitext(configuration_file_path)

        if configuration_file_type == 'yaml':
            parsed_configuration = load_yaml(configuration_file_path)
        else:
            raise RuntimeError('Unknown configuration file format: {}\n'
                               'Only yaml is possible now'.format(configuration_file_type))

    return parsed_configuration


@pytest.fixture(scope='module')
def driver(request, config):
    '''returns WebDriver instance depending on configuration'''
    webdriver_config = config.get('webdriver', {})
    webdriver_mode = webdriver_config.get('mode', 'local')
    if webdriver_mode == 'remote':
        desired_capabilities = webdriver_config.get('remote', {}).get('desired_capabilities', DesiredCapabilities.FIREFOX)

        if isinstance(desired_capabilities, str):
            desired_capabilities = getattr(DesiredCapabilities, desired_capabilities)

        try:
            driver_host = config['webdriver']['remote']['host']
            driver_port = config['webdriver']['remote']['port']
            webdriver_url = 'http://{host}:{port}/wd/hub'.format(host=driver_host, port=driver_port)
            driver = webdriver.Remote(command_executor=webdriver_url, desired_capabilities=desired_capabilities)
        except Exception as e:
            raise WebDriverStartException('A problem occured while trying to initialize Remote WebDriver instance.\n'
                                          'Host: {host}\n'
                                          'Port: {port}\n'
                                          'desired_capabilities: {dc}'.format(host=driver_host, port=driver_port, dc=desired_capabilities), e)

    elif webdriver_mode == 'local':
        # TODO allow a better choice of drivers
        driver = webdriver.Firefox()

    def fin():
        driver.close()

    request.addfinalizer(fin)
    return driver


@pytest.fixture(scope='module')
def navigator(config, driver):
    '''returns WebDriver instance depending on configuration'''
    return IMDbNavigator(config.get('host', 'www.imdb.com'), driver)


class ConfigurationException(Exception):
    '''Exception to report problems with configuration file'''


class WebDriverStartException(Exception):
    '''Exception to report problems with WebDriver initialization'''
