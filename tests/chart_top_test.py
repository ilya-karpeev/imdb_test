# coding: UTF-8

import pytest
from page_objects.top_250 import SortType, SortOrder


@pytest.fixture(scope='function')
def top_250_page(navigator):
    return navigator.navigate_top_250_page()


def test_initial(navigator, driver):
    navigator.navigate_top_250_page()
    assert "IMDb Top 250" in driver.title


def test_top_250(top_250_page):
    '''
    The Top 250 page returns at least 1 movie in the list
    '''
    table_rows = top_250_page.get_top_table_rows()
    assert len(table_rows) > 1


@pytest.mark.parametrize('sort_type', [
    SortType.RANKING,
    SortType.IMDB_RATING,
    SortType.RELEASE_DATE,
    SortType.NUMBER_OF_RATINGS,
    SortType.YOUR_RATING])
@pytest.mark.parametrize('sort_order', [
    SortOrder.ASCENDING,
    SortOrder.DESCENDING,
])
def test_top_250_sorting(sort_type, sort_order, top_250_page):
    '''
    The Top 250 page returns at least 1 movie in the list for all sorting options
    '''
    top_250_page.set_sort(sort_type, sort_order)
    table_rows = top_250_page.get_top_table_rows()
    assert len(table_rows) > 1


@pytest.mark.parametrize('genre_name', [
    'Western',
])
def test_navigate_genre_top(top_250_page, driver, genre_name):
    '''
    The page returns at least 1 movie in the list after navigating to some genre
    '''
    top_250_page.navigate_genre(genre_name)
    top_movies_table = driver.find_element_by_xpath('/html'
                                                    '/body'
                                                    '/div[@id="wrapper"]'
                                                    '/div[@id="root"]'
                                                    '/div[@id="pagecontent"]'
                                                    '/div[@id="content-2-wide"]'
                                                    '/div[@id="main"]'
                                                    '/div[@class="article"]'
                                                    '/table[@class="results"]')
    top_movies_table_body = top_movies_table.find_element_by_xpath('./tbody')
    table_rows = top_movies_table_body.find_elements_by_xpath('./tr[@class="even detailed" or @class="odd detailed" and td[@class="title"]/a]')
    assert len(table_rows) > 1
