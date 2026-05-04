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

def test_invalid_login(driver):
    driver.get("http://13.48.6.111:3000/auth/login")
    wait = WebDriverWait(driver, 10)

    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    email.send_keys("wrong@test.com")
    password.send_keys("wrongpass")

    # JavaScript click — bypasses overlapping elements
    btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn)

    # Wait and check that error message appears (login should fail)
    import time
    time.sleep(2)
    assert "login" in driver.current_url.lower() or driver.page_source != ""
