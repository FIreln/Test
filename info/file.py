import os
import time
class File:


    package = 'com.tencent.tgaapp'
    pid = '20320'
    #打开文件
    def OpenFile(self):
            self.file = open(r'E:\ez_test\zhuanxiang\info\sysinfoo','a+',encoding='utf-8')
    #关闭文件
    def CloseFile(self):
        self.file.close()
    #写入文件
    def Write(self,num1,num2):
        self.OpenFile()
        self.file.writelines('内存：'+num1+' K  '+'CPU：'+num2+'\n')
        self.CloseFile()
