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
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['appPackage'] = 'com.tencent.tgaapp'
        desired_caps['appActivity'] = '.launch.LaunchActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        time.sleep(2)
        global driver
        self.driver.find_element_by_id('com.tencent.tgaapp:id/test').click()

    def testswipe(self):
        #self.driver.find_element_by_id('com.tencent.tgaapp:id/test').click()
        el1 = self.driver.find_element_by_name('全部')
        el2 = self.driver.find_element_by_name('更多')
        self.driver.swipe(100,400,100,100,500)
        time.sleep(2)
        #self.driver.quit()

    def testscreen(self):

        time.sleep(2)
        self.driver.get_screenshot_as_file(r'E:\zhuanxiang\info\pictures\首页.png')
        self.driver.find_element_by_name('资讯').click()
        time.sleep(5)
        print(self.driver.current_activity)
    def testsendkey(self):
        self.driver.find_element_by_name('全部').click()
        self.driver.find_element_by_id('com.tencent.tgaapp:id/mRIvGameVideoBgLeft').click()
        time.sleep(2)
        self.inputel = self.driver.find_element_by_id('com.tencent.tgaapp:id/editText01')
        self.inputel.send_keys('主播真帅')
        time.sleep(2)
        self.driver.get_screenshot_as_file(r'E:\zhuanxiang\info\pictures\发送.png')
        self.driver.find_element_by_name('发送').click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Qtlp)
    unittest.TextTestRunner(verbosity=2).run(suite)