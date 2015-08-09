# coding: UTF-8

import logging
from selenium.webdriver.remote.webdriver import WebDriver

logger = logging.getLogger(name=__name__)


def action_log(action_description):
    '''
    Decorator which allows to write action sequense to the log
    :param str action_description: description of the action
    '''

    def wrapper(action):
        def action_with_logging(*args, **kwargs):
            res = action(*args, **kwargs)
            formatted_action_description = action_description.format(*args, **kwargs)
            logger.log(logging.DEBUG, formatted_action_description)
            return res

        return action_with_logging

    return wrapper


class BaseIMDbPage:
    def __init__(self, driver_or_page):
        '''
        :param selenium.webdriver.remote.webdriver.WebDriver driver: WebDriver instance
        '''
        if isinstance(driver_or_page, WebDriver):
            self._driver = driver_or_page
        elif isinstance(driver_or_page, BaseIMDbPage):
            self._driver = driver_or_page._driver


    @action_log('Searching "{1}" subnavigation panel on sidebar')
    def find_links_subnav_by_header(self, header):
        '''
        Searches for subnavigation panels on the sidebar by header
        :param str header: subnavigation panel header
        '''
        subnav = self._driver.find_element_by_xpath('//div[@id="sidebar"]'
                                                    '/div[@class="aux-content-widget-2 links subnav" and h3="{header}"]'.format(header=header))
        return subnav
