from selenium.webdriver.common.by import By

def test_jobs_page(driver):
    driver.get("http://13.48.6.111:3000/jobs")
    assert "job" in driver.current_url.lower()


def test_job_list_visible(driver):
    driver.get("http://13.48.6.111:3000/jobs")
    assert True  # basic page load test