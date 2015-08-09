# coding: UTF-8

import pytest
from page_objects.genre_page import GenrePage
from page_objects.top_250 import SortType, SortOrder, GenreNames, Top250Page


@pytest.fixture(scope='function')
def top_250_page(navigator):
    return navigator.navigate_page(Top250Page)


def test_initial(navigator, driver):
    navigator.navigate_page(Top250Page)
    assert "IMDb Top 250" in driver.title


def test_top_250(top_250_page):
    '''
    The Top 250 page returns at least 1 movie in the list
    '''
    table_rows = top_250_page.get_top_table().get_rows()
    assert len(table_rows) > 0


@pytest.mark.parametrize('sort_type', [
    SortType.RANKING,
    SortType.IMDB_RATING,
    SortType.RELEASE_DATE,
    SortType.NUMBER_OF_RATINGS,
    SortType.YOUR_RATING
])
@pytest.mark.parametrize('sort_order', [
    SortOrder.ASCENDING,
    SortOrder.DESCENDING,
])
def test_top_250_sorting(sort_type, sort_order, top_250_page, driver):
    '''
    The Top 250 page returns at least 1 movie in the list for all sorting options
    '''
    top_250_page.get_top_table().set_sort(sort_type, sort_order)
    table_rows = top_250_page.get_top_table().get_rows()
    assert len(table_rows) > 0


@pytest.mark.parametrize('genre_name', [
    GenreNames.WESTERN,
])
def test_navigate_genre_top(top_250_page, driver, genre_name):
    '''
    The page returns at least 1 movie in the list after navigating to some genre
    '''
    top_250_page.get_genre_panel().navigate_genre(genre_name)
    genre_page = GenrePage(driver)
    table_rows = genre_page.get_top_table().get_rows()
    assert len(table_rows) > 0
