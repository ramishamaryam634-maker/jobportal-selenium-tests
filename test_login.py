from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login(driver):
    driver.get("http://13.48.6.111:3000/auth/login")

    wait = WebDriverWait(driver, 10)

    email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email'], input#email")))
    password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password'], input#password")))

    email.send_keys("wrong@test.com")
    password.send_keys("wrongpass")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))).click()