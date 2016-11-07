import os
from appium import webdriver
import time
import unittest
class Launch():

    '''def setup(self):

        desired_caps = {}
        desired_caps['devicceName'] = ''
        desired_caps['platformName'] = 'Android'
        desired_caps['PlatformVersion'] = '4.3'
        desired_caps['appPackage'] = 'com.tencent.tgaapp'
        desired_caps['appActivity'] = '.launch.LaunchActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        global driver
        time.sleep(2)'''
    def testlaunchtime(self):
        self.log = os.popen("adb logcat>E:/log.txt ")
        self.file = open(r'E:/log.txt ','r',encoding='brief')
        print(self.file.read().find('Displayed '))
        #os.popen('adb find .launch.LaunchActivity /E:\zhuanxiang\Launch Time\f1 >/E:\zhuanxiang\LaunchTime\lastlog')
        #self.log = open(r'E:\zhuanxiang\Launch Time\lastlog','r')
if __name__ == '__main__':
    la =Launch()
    la.testlaunchtime()
