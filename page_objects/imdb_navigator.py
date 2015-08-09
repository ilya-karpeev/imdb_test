# coding: UTF-8

class IMDbNavigator:
    def __init__(self, host, driver):
        self._host = host
        self._driver = driver


    def navigate(self, path):
        self._driver.get('http://{host}{path}'.format(host=self._host, path=path))


    def navigate_page(self, page):
        self.navigate(page.path)
        return page(self._driver)
