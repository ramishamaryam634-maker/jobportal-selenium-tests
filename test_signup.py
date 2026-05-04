from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_signup_page(driver):
    driver.get("http://13.48.6.111:3000/signup")
    assert "signup" in driver.current_url.lower()


def test_signup_form(driver):
    driver.get("http://13.48.6.111:3000/signup")

    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    name.send_keys("Test User")

    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email.send_keys("test@test.com")

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password.send_keys("123456")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    )
    button.click()