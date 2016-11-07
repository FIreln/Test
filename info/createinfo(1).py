import os

from zhuanxiang.info import file


class CreatInfo:

    file = file.File()

    #获得内存
    def GetMem(self):
        self.TOTAL = 'TOTAL'
        self.Objects = 'Objects'
        self.mem = os.popen('adb shell dumpsys meminfo com.tencent.tgaapp').read()
        #print(self.mem)
        self.num1 = self.mem.find(self.TOTAL)
        #print(self.num1)
        self.num2 = self.mem.find(self.Objects)
        #print(self.num2)
        self.memused = self.mem[self.num1:self.num2].split()[4]
        #print(self.memused)
        return self.memused

    #获得CPU
    def GetCpuinfo(self):
        self.cpu_end = file.File.package
        #self.cpu_start = file.File.pid
        self.cpu = os.popen('adb shell top -m 10 -n 1').read()
        self.cpu_num1 = self.cpu.find(self.cpu_end)
        #self.cpu_num2 = self.cpu.find(self.cpu_start)
        self.cpuinfo_tga = self.cpu[(self.cpu_num1-48):self.cpu_num1:].split()[2]
        #print(self.cpuinfo_tga)
        #self.cpuinfo_xg = self.cpu[(self.cpu_num2-10):self.cpu_num2:].split()[0]
        return self.cpuinfo_tga


    def run(self,path):
        ci = CreatInfo()
        fl = file.File()
        fl.Write(ci.GetMem(),ci.GetCpuinfo(),path)
        print(ci.GetMem(),ci.GetCpuinfo())
