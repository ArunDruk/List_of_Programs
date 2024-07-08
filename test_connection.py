from selenium.webdriver.support.ui import WebDriverWait
import pytest
import logging
from appium_python_server.appium import AppiumServer
from appium_ps import webdriver
import time
import json
from reading_config_file import config_data

identify_obj1={'first_tile':'Testing Group'}
logger=logging.getLogger(__name__)

@pytest.fixture(scope='class')
def set_up(request):
    global config_data
    logger.info(f"config_data = {config_data}")

    appium_options = config_data['options']['capabilities']

    desired_capabilities = appium_options[0]['desiredCapabilities']
    server_options = appium_options
    server_config = server_options[0]['appiumServer']
    logger.info(f"Starting Appium Server {server_config['host']}:{server_config['port']}")
    try:
        appium_server = AppiumServer([__file__,
                                                          '--address', server_config['host'],
                                                          '--port', str(server_config['port']),
                                                          '--log-level', server_config.get('logLevel', 'info'),
                                                          '--log-timestamp'])
        appium_server.start()
        logger.info("Appium server is running...")
        appium_drivers={}
        # config_name = appium_options[0]['name'] if 'name' in appium_options else str(server_config['port'])
        appium_driver = webdriver.Remote(f"http://{server_config['host']}:{server_config['port']}/wd/hub",
                                                     desired_capabilities,
                                                     keep_alive=True)
        # appium_drivers[config_name] = appium_driver
        # request.cls.driver = list(appium_drivers.values())[0] if len(appium_drivers) == 1 else appium_drivers
        logger.info(f'driver object= {appium_driver}')
        request.cls.driver=appium_driver
        yield #request.cls.driver
    except Exception as e:
        logger.info(f'Exception during starting server'+str(e))

    # request.config.appium_client = list(appium_drivers.values())[0] if len(appium_drivers) == 1 else appium_drivers
    #
    # request.cls.driver = request.config.appium_client

    finally:
        logger.info("Stopping Appium server...")
        request.cls.driver.quit()
        appium_server.stop()
    # for name, driver in appium_drivers.items():
    #     logger.info('Stopped appium %s', name)
    # webdriver.quit()



@pytest.mark.usefixtures("set_up")
class Test_tc50:
    def test_tc50(self):
        app_port = {"862_context": "WEBVIEW_862"}
        links = {"home": "pscloudsubs:browse?page=home"}
        # self.driver=skynete_connections
        self.driver.ds.ps()
        time.sleep(2)
        self.driver.switch_to.context(app_port.get("862_context"))
        self.driver.get(links.get("home"))
        time.sleep(3)
        logger.info('Apollo Application Started')
        self.driver.ds.right()
        time.sleep(3)
        self.driver.ds.right()
        time.sleep(3)
        logger.info('Closing Apollo Application')

        self.driver.ds.ps()
