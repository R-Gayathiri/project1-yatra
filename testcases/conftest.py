import pytest as pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.yatra.com/")
    request.cls.driver = driver
    # request.cls.wait = wait
    driver.maximize_window()
    yield
    driver.close()
