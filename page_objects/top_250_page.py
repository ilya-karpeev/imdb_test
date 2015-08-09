# coding: UTF-8

from selenium.webdriver.support.select import Select
from page_objects.base_imdb_page import BaseIMDbPage, action_log


class SortType:
    RANKING = 'Ranking'
    IMDB_RATING = 'IMDb Rating'
    RELEASE_DATE = 'Release Date'
    NUMBER_OF_RATINGS = 'Number of Ratings'
    YOUR_RATING = 'Your Rating'


class SortOrder:
    ASCENDING = 'ascending'
    DESCENDING = 'descending'


class Top250Table:
    '''
    Represents "Top 250" table
    '''
    def __init__(self, element):
        self._table = element


    @action_log('Searching for "Top 250" table rows')
    def get_rows(self):
        '''
        :return: list of table rows
        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        '''
        table_rows = self._table.find_elements_by_xpath('./div[@class="article"]'
                                                        '/div[@class="lister"]'
                                                        '/table[@class="chart"]'
                                                        '/tbody'
                                                        '/tr[td[@class="titleColumn"]/a[@title]]')
        return table_rows


    @action_log('Searching for sorting control on "Top 250" table')
    def get_sorting_control(self):
        '''
        :return: list sorting control with sorting type dropdown and sort order span on it
        :rtype: selenium.webdriver.remote.webelement.WebElement
        '''
        sorting = self._table.find_element_by_xpath('./div[@class="article"]'
                                                    '/div[@class="lister"]'
                                                    '/div[@class="header"]'
                                                    '/div[@class="nav"]'
                                                    '/div[@class="controls float-right lister-activated"]')
        return sorting


    @action_log('Searching for "sort by" control on "Top 250" table')
    def get_sort_by_select(self):
        '''
        :return: sorting type dropdown list
        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        '''
        sorting = self.get_sorting_control()
        sort_by_select = Select(sorting.find_element_by_xpath('./select[@class="lister-sort-by" and @name="sort"]'))
        return sort_by_select


    @action_log('Searching for "sort order" control on "Top 250" table')
    def get_sort_order_span(self):
        '''
        :return: sort order span
        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        '''
        sorting = self.get_sorting_control()
        sort_order_span = sorting.find_element_by_xpath('./span[starts-with(@class, "global-sprite lister-sort-reverse")]')
        return sort_order_span


    @action_log('Choosing {1} sort order on "Top 250" table')
    def set_sort_order(self, sort_order):
        '''
        Chooses specified sorting order by clicking sort order span.
        If sort order already as sort_order then does nothing.
        :param str sort_order: orting order. could be ascending or descending
        '''
        sort_order_span = self.get_sort_order_span()

        if sort_order not in sort_order_span.get_attribute('class'):
            sort_order_span.click()

        return self


    @action_log('Selecting {1} sort type on "Top 250" table')
    def set_sort_type(self, sort_type):
        '''
        Chooses specified sorting type by selecting item from sort type dropdown
        :param str sort_type: sorting type
        '''
        sort_by_select = self.get_sort_by_select()
        sort_by_select.select_by_visible_text(sort_type)
        return self


    def set_sort(self, sort_type, sort_order):
        '''
        Chooses specified sorting type and sort order
        :param str sort_type: sorting type
        :param str sort_order: orting order. could be ascending or descending
        '''
        # first sort type then sort order, cause sort order is reset when sort type is changed
        return self.set_sort_type(sort_type).set_sort_order(sort_order)


class GenreNames:
    '''
    Names of genres
    '''
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    ANIMATION = 'Animation'
    BIOGRAPHY = 'Biography'
    COMEDY = 'Comedy'
    CRIME = 'Crime'
    DOCUMENTARY = 'Documentary'
    DRAMA = 'Drama'
    FAMILY = 'Family'
    FANTASY = 'Fantasy'
    FILM_NOIR = 'Film-Noir'
    HISTORY = 'History'
    HORROR = 'Horror'
    MUSIC = 'Music'
    MUSICAL = 'Musical'
    MYSTERY = 'Mystery'
    ROMANCE = 'Romance'
    SCI_FI = 'Sci-Fi'
    SHORT = 'Short'
    SPORT = 'Sport'
    THRILLER = 'Thriller'
    WAR = 'War'
    WESTERN = 'Western'


class GenreLinksPanel:
    '''
    Represents "Top Movies by Genre" sidebar panel
    '''
    header = 'Top Movies by Genre'

    def __init__(self, element):
        self._panel = element


    @action_log('Searching for "{1}" genre link on "Top Movies by Genre" sidebar panel')
    def get_genre_link(self, genre_name):
        '''
        :param genre_name: name of the genre
        :return: genre link
        :rtype: WebElement
        '''
        genre_link = self._panel.find_element_by_xpath('./ul/li/a[contains(., "{genre}")]'.format(genre=genre_name))
        return genre_link


    @action_log('Clicking on "{1}" genre link on "Top Movies by Genre" sidebar panel')
    def navigate_genre(self, genre_name):
        '''
        Clicks on specified genre link
        :param genre_name: name of the genre
        '''
        self.get_genre_link(genre_name).click()


class Top250Page(BaseIMDbPage):
    '''
    Represents www.imdb.com/chart/top page
    '''
    path = '/chart/top'


    @action_log('Searching for "Top 250" table on "Top 250" page')
    def get_top_table(self):
        '''
        :return: top 250 table
        :rtype: Top250Table
        '''
        table = self._driver.find_element_by_xpath('//div[@id="main"]'
                                                   '/div[@class="seen-collection" and @data-collectionid="top-250"]')
        return Top250Table(table)


    @action_log('Searching for "Top Movies by Genre" panel on the sidebar of "Top 250" page')
    def get_genre_panel(self):
        '''
        :return: sidebar genre panel
        :rtype: GenreLinksPanel
        '''
        genre_panel = self.find_links_subnav_by_header(GenreLinksPanel.header)
        return GenreLinksPanel(genre_panel)
