import time
from zhuanxiang.info import createinfo
from zhuanxiang.changjing import setUp
import unittest
class ShouYe(unittest.TestCase):
    info = createinfo.CreatInfo()
    su = setUp.SetUp()
    driver = su.setup()
    def testchangetab(self):
        for i in range(2):
            for i in range(4):
                self.driver.find_element_by_name('资讯').click()
                time.sleep(1)
                self.driver.find_element_by_name('主页').click()
                time.sleep(1)
            self.info.run(r'E:\ez_test\zhuanxiang\info\tab切换')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
