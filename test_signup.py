from selenium.webdriver.common.by import By

def test_signup_page(driver):
    driver.get("http://13.48.6.111:3000/signup")
    assert "signup" in driver.current_url.lower()


def test_signup_form(driver):
    driver.get("http://13.48.6.111:3000/signup")

    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("test@test.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button").click()