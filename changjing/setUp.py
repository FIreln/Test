from appium import webdriver
import time
class SetUp:

    def setup(self):
        desired_caps = {}
        desired_caps['deviceName'] = 'cb2be5b'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['browserName'] = ''
        desired_caps['appPackage'] = 'com.tencent.tgaapp'
        desired_caps['appActivity'] = '.launch.LaunchActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        #self.sellsion_id = self.driver.session_id()
        time.sleep(2)
        return self.driver