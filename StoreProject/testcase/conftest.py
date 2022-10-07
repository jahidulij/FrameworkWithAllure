import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture
def setup1(browser):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("Launching Chrome browser")

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching Firefox browser")

    elif browser.lower() == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("Launching Edge browser")

    else:
        print("Browser not supported")

    return driver

# It will get the value from command line
def pytest_addoption(parser):
    parser.addoption("--browser")

# This will return the browser value to the setup1 method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Pytest html report
def pytest_configure(config):
    config._metadata["Project Name"] = "NOP Commerce"
    config._metadata["Module Name"] = "Customer"
    config._metadata["Tester"] = "Jahid"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
