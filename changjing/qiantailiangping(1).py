from info import createinfo
from changjing import setUp
import unittest
import time

class Qtlp(unittest.TestCase):
    info = createinfo.CreatInfo()
    su = setUp.SetUp()
    driver = su.setup()
    #前台亮屏待机
    def testqtlp(self):
        self.driver.find_element_by_id('com.tencent.tgaapp:id/test').click()
        for i  in range(2):
            self.driver.find_element_by_name('鹅掌TV').click()
            self.info.run(path = r'E:\zhuanxiang\info\前台亮屏待机')
            time.sleep(10)
        self.driver.quit()
    #前台锁屏待机
    def testqtdj(self):
        self.driver.find_element_by_id('com.tencent.tgaapp:id/test').click()
        time.sleep(5)
        self.driver.press_keycode('26')
        for i in range(2):
            self.info.run(path = r'E:\zhuanxiang\info\前台锁屏待机')
            time.sleep(5)
        self.driver.quit()
    '''#后台待机
    def testhtdj(self):
        self.driver.find_element_by_id('com.tencent.tgaapp:id/test').click()
        time.sleep(5)
        self.driver.press_keycode('3')
        for i in range(2):
            self.info.run(r'E:\ez_test\zhuanxiang\info\后台待机')
        self.driver.quit()'''
    def run_jinrtai(self):
        qt = Qtlp()
        qt.testqtlp()
        qt.testqtdj()
        #qt.testhtdj()

if __name__ == '__main__':
    qt = Qtlp()
    qt.run_jinrtai()
    #suite = unittest.TestLoader().loadTestsFromTestCase(Qtlp)
    #unittest.TextTestRunner(verbosity=2).run(suite)