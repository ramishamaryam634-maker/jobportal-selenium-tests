from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_signup_form(driver):
    driver.get("http://13.48.6.111:3000/auth/register")

    wait = WebDriverWait(driver, 10)

    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='name'], input#name")))
    email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email'], input#email")))
    password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password'], input#password")))

    name.send_keys("Test User")
    email.send_keys("test@test.com")
    password.send_keys("123456")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))).click()