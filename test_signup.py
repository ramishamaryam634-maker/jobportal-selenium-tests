def test_signup_form(driver):
    driver.get("http://13.48.6.111:3000/auth/register")

    wait = WebDriverWait(driver, 10)

    name = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    name.send_keys("Test User")
    email.send_keys("test@test.com")
    password.send_keys("123456")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()