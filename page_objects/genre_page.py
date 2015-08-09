# coding: UTF-8

from page_objects.base_imdb_page import BaseIMDbPage, action_log


class TopTable:
    '''
    Represents table
    '''

    def __init__(self, element):
        self._table = element


    @action_log('Searching for top table rows')
    def get_rows(self):
        '''
        :return: list of table rows
        :rtype: list of selenium.webdriver.remote.webelement.WebElement
        '''
        table_rows = self._table.find_elements_by_xpath('./tbody'
                                                        '/tr[@class="even detailed" or @class="odd detailed" and td[@class="title"]/a]')
        return table_rows


class GenrePage(BaseIMDbPage):
    '''
    Represents any "Most Popular" page
    '''
    path = '/chart/top'


    @action_log('Searching for top table')
    def get_top_table(self):
        '''
        :return: top table
        :rtype: TopTable
        '''
        top_movies_table = self._driver.find_element_by_xpath('//div[@id="main"]'
                                                              '/div[@class="article"]'
                                                              '/table[@class="results"]')
        return TopTable(top_movies_table)


class WesternPage(GenrePage):
    path = '/genre/western'
