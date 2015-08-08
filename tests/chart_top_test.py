# coding: UTF-8

def test_initial(driver, config):
    driver.get('http://{host}{path}'.format(host=config['host'],
                                            path=config['paths']['top']))
    assert "IMDb Top 250" in driver.title
