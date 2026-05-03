from selenium.webdriver.common.by import By

def test_login_page_load(driver):
    driver.get("http://13.48.6.111:3000/login")
    assert "login" in driver.current_url.lower()


def test_invalid_login(driver):
    driver.get("http://13.48.6.111:3000/login")

    driver.find_element(By.NAME, "email").send_keys("wrong@test.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button").click()