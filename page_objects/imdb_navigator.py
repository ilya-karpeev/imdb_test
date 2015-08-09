# coding: UTF-8
from page_objects.base_imdb_page import action_log


class IMDbNavigator:
    def __init__(self, host, driver):
        self._host = host
        self._driver = driver


    @action_log('Navigating to {1} page')
    def navigate(self, path):
        self._driver.get('http://{host}{path}'.format(host=self._host, path=path))


    def navigate_page(self, page):
        self.navigate(page.path)
        return page(self._driver)
