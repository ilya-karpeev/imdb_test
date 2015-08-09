# coding: UTF-8

from page_objects.top_250 import Top250Page


class IMDbNavigator:
    def __init__(self, host, driver):
        self._host = host
        self._driver = driver


    def navigate_top_250_page(self):
        self._driver.get('http://{host}{path}'.format(host=self._host, path=Top250Page.path))
        return Top250Page(self._driver)
