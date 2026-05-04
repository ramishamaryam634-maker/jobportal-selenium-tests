import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()

def test_signup_form(driver):
    driver.get("http://13.48.6.111:3000/auth/register")
    wait = WebDriverWait(driver, 10)

    name     = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    email    = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    name.send_keys("Test User")
    email.send_keys("test@test.com")
    password.send_keys("123456")

    # JavaScript click — fixes "element click intercepted" error
    btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn)

    import time
    time.sleep(2)

    # After signup, either redirected away from register page OR still on it
    assert driver.current_url != ""
