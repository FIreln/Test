from info import createinfo
from appium import webdriver
import unittest
import time

class Qtlp(unittest.TestCase):
    info = createinfo.CreatInfo()
    def setUp(self):
        desired_caps = {}
        desired_caps['deviceName'] = 'cb2be5b'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['browserName'] = ''
        desired_caps['appPackage'] = 'com.tencent.tgaapp'
        desired_caps['appActivity'] = '.launch.LaunchActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        time.sleep(2)
        global driver

    def testlaingping(self):
        self.driver.find_element_by_id('com.tencent.tgaapp:id/test').click()
        for i  in range(30):
            self.driver.find_element_by_name('鹅掌TV').click()
            self.info.run()
            time.sleep(10)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Qtlp)
    unittest.TextTestRunner(verbosity=2).run(suite)