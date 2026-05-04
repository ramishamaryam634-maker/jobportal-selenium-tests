def test_homepage_load(driver):
    driver.get("http://13.48.6.111:3000")
    assert driver.title is not None

def test_home_url(driver):
    driver.get("http://13.48.6.111:3000")
    assert "http" in driver.current_url
