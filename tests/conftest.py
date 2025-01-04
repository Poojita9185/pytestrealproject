import pytest
from selenium import webdriver

from Utilities import Readconfigurations


@pytest.fixture(scope='class')
def launch_browser(request):
    driver = webdriver.Chrome()
    #URL = Readconfigurations.ReadConfigs('basic info','url')
    driver.maximize_window()
    request.cls.driver = driver



