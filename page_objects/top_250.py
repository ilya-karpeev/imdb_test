# coding: UTF-8

from selenium.webdriver.support.select import Select


class SortType:
    RANKING = 'Ranking'
    IMDB_RATING = 'IMDb Rating'
    RELEASE_DATE = 'Release Date'
    NUMBER_OF_RATINGS = 'Number of Ratings'
    YOUR_RATING = 'Your Rating'


class SortOrder:
    ASCENDING = 'ascending'
    DESCENDING = 'descending'


class Top250Page:
    path = '/chart/top'

    def __init__(self, driver):
        '''
        :param selenium.webdriver.remote.webdriver.WebDriver driver: WebDriver instance
        '''
        self._driver = driver


    def get_top_table(self):
        '''
        :return: top 250 table
        :rtype: selenium.webdriver.remote.webelement.WebElement
        '''
        table = self._driver.find_element_by_xpath('/html'
                                                   '/body'
                                                   '/div[@id="wrapper"]'
                                                   '/div[@id="root" and @class="redesign"]'
                                                   '/div[@id="pagecontent"]'
                                                   '/div[@id="content-2-wide" and @class="redesign"]'
                                                   '/div[@id="main"]'
                                                   '/div[@class="seen-collection" and @data-collectionid="top-250"]')
        return table


    def get_top_table_rows(self):
        '''
        :return: List of top 250 table rows
        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        '''
        table = self.get_top_table()
        table_rows = table.find_elements_by_xpath('./div[@class="article"]'
                                                  '/div[@class="lister"]'
                                                  '/table[@class="chart"]'
                                                  '/tbody'
                                                  '/tr[td[@class="titleColumn"]/a[@title]]')
        return table_rows


    def get_sorting_control(self):
        '''
        :return: list sorting control with sorting type dropdown and sort order span on it
        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        '''
        table = self.get_top_table()
        sorting = table.find_element_by_xpath('./div[@class="article"]'
                                              '/div[@class="lister"]'
                                              '/div[@class="header"]'
                                              '/div[@class="nav"]'
                                              '/div[@class="controls float-right lister-activated"]')
        return sorting


    def get_sort_by_select(self):
        '''
        :return: sorting type dropdown list
        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        '''
        sorting = self.get_sorting_control()
        sort_by_select = Select(sorting.find_element_by_xpath('./select[@class="lister-sort-by" and @name="sort"]'))
        return sort_by_select


    def get_sort_order_span(self):
        '''
        :return: sort order span
        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        '''
        sorting = self.get_sorting_control()
        sort_order_span = sorting.find_element_by_xpath('./span[starts-with(@class, "global-sprite lister-sort-reverse")]')
        return sort_order_span


    def set_sort_order(self, sort_order):
        sort_order_span = self.get_sort_order_span()

        if sort_order not in sort_order_span.get_attribute('class'):
            sort_order_span.click()

        return self


    def set_sort_type(self, sort_type):
        sort_by_select = self.get_sort_by_select()
        sort_by_select.select_by_visible_text(sort_type)
        return self


    def set_sort(self, sort_type, sort_order):
        # first sort type then sort order, cause sort order is reset when sort type is changed
        return self.set_sort_type(sort_type).set_sort_order(sort_order)


    def get_genre_panel(self):
        genre_panel = self._driver.find_element_by_xpath('/html'
                                                         '/body'
                                                         '/div[@id="wrapper"]'
                                                         '/div[@id="root" and @class="redesign"]'
                                                         '/div[@id="pagecontent"]'
                                                         '/div[@id="content-2-wide" and @class="redesign"]'
                                                         '/div[@id="sidebar"]'
                                                         '/div[@class="aux-content-widget-2 links subnav" and h3="Top Movies by Genre"]')
        return genre_panel


    def get_genre_link(self, genre_name):
        genre_panel = self.get_genre_panel()
        genre_link = genre_panel.find_element_by_xpath('./ul/li/a[contains(., "{genre}")]'.format(genre=genre_name))
        return genre_link


    def navigate_genre(self, genre_name):
        self.get_genre_link(genre_name).click()
