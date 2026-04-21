import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


driver = "chrome"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="select browers"
    )

@pytest.fixture(scope="function")
def browserinstance(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "firefox":
        driver = webdriver.firefox()

    elif browser_name == "chrome":
        chrome_opt = webdriver.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False  # To disable password leak detection warnings
        }
        chrome_opt.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=chrome_opt)

    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    driver.get("https://automationintesting.online/")
    yield driver

    driver.close()

'''
@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
'''