from selenium.webdriver.common.by import By

def test_dummy_1(driver):
    driver.get("http://13.48.6.111:3000")
    assert True

def test_dummy_2(driver):
    driver.get("http://13.48.6.111:3000")
    assert "Job" in driver.title

def test_dummy_3(driver):
    driver.get("http://13.48.6.111:3000")
    assert True


def test_page_has_content(driver):
    driver.get("http://13.48.6.111:3000")
    assert len(driver.page_source) > 100


def test_page_has_body_tag(driver):
    driver.get("http://13.48.6.111:3000")
    body = driver.find_element(By.TAG_NAME, "body")
    assert body is not None
