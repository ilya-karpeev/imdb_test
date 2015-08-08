# coding: UTF-8

import pytest
from selenium.webdriver.support.select import Select


@pytest.fixture(scope='function')
def top_250_page(driver, config):
    driver.get('http://{host}{path}'.format(host=config['host'],
                                            path=config['paths']['top']))
    return driver


def test_initial(driver, config):
    driver.get('http://{host}{path}'.format(host=config['host'],
                                            path=config['paths']['top']))
    assert "IMDb Top 250" in driver.title


def test_top_250(top_250_page):
    '''
    The Top 250 page returns at least 1 movie in the list
    '''
    top250_table = top_250_page.find_element_by_xpath('/html'
                                                      '/body'
                                                      '/div[@id="wrapper"]'
                                                      '/div[@id="root" and @class="redesign"]'
                                                      '/div[@id="pagecontent"]'
                                                      '/div[@id="content-2-wide" and @class="redesign"]'
                                                      '/div[@id="main"]'
                                                      '/div[@class="seen-collection" and @data-collectionid="top-250"]'
                                                      '/div[@class="article"]'
                                                      '/div[@class="lister"]'
                                                      '/table[@class="chart"]'
    )
    top250_table_body = top250_table.find_element_by_xpath('./tbody')
    table_rows = top250_table_body.find_elements_by_xpath('./tr[td[@class="titleColumn"]/a[@title]]')
    assert len(table_rows) > 1


@pytest.mark.parametrize('sort_type', [
    'Ranking',
    'IMDb Rating',
    'Release Date',
    'Number of Ratings',
    'Your Rating',
])
@pytest.mark.parametrize('sort_order', [
    'ascending',
    'descending'
])
def test_top_250_sorting(sort_type, sort_order, top_250_page):
    '''
    The Top 250 page returns at least 1 movie in the list for all sorting options
    '''
    sorting = top_250_page.find_element_by_xpath('/html'
                                                 '/body'
                                                 '/div[@id="wrapper"]'
                                                 '/div[@id="root" and @class="redesign"]'
                                                 '/div[@id="pagecontent"]'
                                                 '/div[@id="content-2-wide" and @class="redesign"]'
                                                 '/div[@id="main"]'
                                                 '/div[@class="seen-collection" and @data-collectionid="top-250"]'
                                                 '/div[@class="article"]'
                                                 '/div[@class="lister"]'
                                                 '/div[@class="header"]'
                                                 '/div[@class="nav"]'
                                                 '/div[@class="controls float-right lister-activated"]')

    sort_by_select = Select(sorting.find_element_by_xpath('./select[@class="lister-sort-by" and @name="sort"]'))
    sort_order_span = sorting.find_element_by_xpath('./span[starts-with(@class, "global-sprite lister-sort-reverse")]')

    if sort_order not in sort_order_span.get_attribute('class'):
        sort_order_span.click()

    sort_by_select.select_by_visible_text(sort_type)

    top250_table = top_250_page.find_element_by_xpath('/html'
                                                      '/body'
                                                      '/div[@id="wrapper"]'
                                                      '/div[@id="root" and @class="redesign"]'
                                                      '/div[@id="pagecontent"]'
                                                      '/div[@id="content-2-wide" and @class="redesign"]'
                                                      '/div[@id="main"]'
                                                      '/div[@class="seen-collection" and @data-collectionid="top-250"]'
                                                      '/div[@class="article"]'
                                                      '/div[@class="lister"]'
                                                      '/table[@class="chart"]'
    )
    # WebElement
    top250_table_body = top250_table.find_element_by_xpath('./tbody')
    table_rows = top250_table_body.find_elements_by_xpath('./tr[td[@class="titleColumn"]/a[@title]]')
    assert len(table_rows) == 250


def test_top_250_western_genre(top_250_page, driver):
    '''
    The page returns at least 1 movie in the list after navigating to the Western genre
    '''
    genre_panel = top_250_page.find_element_by_xpath('/html'
                                                     '/body'
                                                     '/div[@id="wrapper"]'
                                                     '/div[@id="root" and @class="redesign"]'
                                                     '/div[@id="pagecontent"]'
                                                     '/div[@id="content-2-wide" and @class="redesign"]'
                                                     '/div[@id="sidebar"]'
                                                     '/div[@class="aux-content-widget-2 links subnav" and h3="Top Movies by Genre"]')
    genre_links = genre_panel.find_elements_by_xpath('./ul/li/a')
    genre_links[-1].click()
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
    assert len(table_rows) == 25
