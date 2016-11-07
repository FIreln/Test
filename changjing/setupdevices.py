import os
import time
from appium import webdriver
from zhuanxiang.info import createinfo
import unittest

class Test(unittest.TestCase):
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

    def testLogin(self):
        self.driver.find_element_by_id('com.tencent.tgaapp:id/test').click()
        self.driver.find_element_by_name('全部').click()
        print('*******************************************')
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.tgaapp:id/mRIvGameVideoBgLeft').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.tencent.tgaapp:id/send_gitf').click()
        time.sleep(0.2)
        self.driver.find_element_by_id('com.tencent.tgaapp:id/mBtnLogin').click()
        time.sleep(2)
        self.driver.find_element_by_name('登录').click()
        time.sleep(2)
        self.driver.press_keycode('4')
        time.sleep(1)
        self.driver.press_keycode('4')
        time.sleep(1)
        self.driver.find_element_by_name('设置').click()
        self.driver.find_element_by_name('退出').click()
        self.driver.find_element_by_name('确定').click()
        time.sleep(2)
        self.driver.find_element_by_name('用户登录').click()
        time.sleep(2)
        self.driver.find_element_by_name('登录').click()
        time.sleep(2)
        self.driver.find_element_by_name('首页').click()

    def testMySubscribe(self):
            try:
                self.driver.find_element_by_name('设置').click()
                self.driver.find_element_by_name('我的订阅').click()
                self.driver.find_element_by_name('还没有订阅主播！').is_displayed()
            except:
                self.driver.find_element_by_id('com.tencent.tgaapp:id/my_fellow_list').click()
                time.sleep(2)
            else:
                self.driver.find_element_by_name('全部').click()
                time.sleep(1)
                self.driver.find_element_by_id('com.tencent.tgaapp:id/mRIvGameVideoBgLeft').click()
                time.sleep(0.5)
                self.driver.find_element_by_name('主播').click()
                self.driver.find_element_by_id('com.tencent.tgaapp:id/fellow_btn').click()
                self.driver.press_keycode('4')
                self.driver.find_element_by_name('设置').click()
                self.driver.find_element_by_name('我的订阅').click()
                self.driver.find_element_by_id('com.tencent.tgaapp:id/my_fellow_list').click()
                time.sleep(2)

    def testQuit(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)



