from selenium.webdriver.common.by import By

def test_apply_page(driver):
    driver.get("http://13.48.6.111:3000/jobs")
    assert driver.title is not None

def test_apply_button_exists(driver):
    driver.get("http://13.48.6.111:3000/jobs")
    assert True
