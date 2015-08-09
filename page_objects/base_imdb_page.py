# coding: UTF-8
from selenium.webdriver.remote.webdriver import WebDriver


class BaseIMDbPage:
    def __init__(self, driver_or_page):
        '''
        :param selenium.webdriver.remote.webdriver.WebDriver driver: WebDriver instance
        '''
        if isinstance(driver_or_page, WebDriver):
            self._driver = driver_or_page
        elif isinstance(driver_or_page, BaseIMDbPage):
            self._driver = driver_or_page._driver


    def find_links_subnav_by_header(self, header):
        '''
        Searches for subnavigation panels on the sidebar by header
        :param str header: subnavigation panel header
        '''
        subnav = self._driver.find_element_by_xpath('//div[@id="sidebar"]'
                                                    '/div[@class="aux-content-widget-2 links subnav" and h3="{header}"]'.format(header=header))
        return subnav
