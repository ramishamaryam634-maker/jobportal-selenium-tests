def test_dummy_1(driver):
    driver.get("http://13.48.6.111:3000")
    assert True


def test_dummy_2(driver):
    driver.get("http://13.48.6.111:3000")
    assert "Job" in driver.title


def test_dummy_3(driver):
    driver.get("http://13.48.6.111:3000")
    assert True