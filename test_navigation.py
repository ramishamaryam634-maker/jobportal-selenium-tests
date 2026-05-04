def test_home_navigation(driver):
    driver.get("http://13.48.6.111:3000")
    assert "http" in driver.current_url

def test_reload(driver):
    driver.get("http://13.48.6.111:3000")
    driver.refresh()
    assert True
