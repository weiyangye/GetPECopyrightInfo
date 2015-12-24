# *.* coding=utf-8
__time__ = '2015.12.14'
__author__ = 'weiyangye@hotmail.com'
# C:\Python27\python.exe
import os
import sys
import pefile
import glob
import struct

# to fix
'''
UnicodeEncodeError: 'gb2312' codec can't encode character u'\xa9' in position 9: illegal multibyte sequence
url:http://wangye.org/blog/archives/629/
'''
reload(sys)
sys.setdefaultencoding('utf-8')

pefiledir = r"D:\Program Files\WizNote\*.dll" # PE dir , you can select pe file dir path.

class GetPERightInfo():
    def __init__(self):
        self.filelist = []
        self.info_file = open('pefile_info.txt','a')

    def enumerate_pefile(self):  # enumerate_pefile and add to filelist
        # print os.listdir(pefiledir)
        # print glob.glob(pefiledir)
        for file in glob.glob(pefiledir):
            # print file
            if self.isPeFile(file):
                self.filelist.append(file)
            # print self.filelist
        return self.filelist

    def getpeinfo(self,pefile_list):
        pe_list = pefile_list
        for peFile in pe_list:
            print "PEFile_Path: " + peFile
            print "PE INFO: "
            self.info_file.write("PEFile_Path: " + peFile + '\n')
            self.info_file.write("PE INFO: \n")
            mype = pefile.PE(peFile)
            # mype = pefile.PE(pefilepath)
            # print pe # parse_version_information('MajorLinkerVersion')
            if hasattr(mype, 'VS_VERSIONINFO'):
                if hasattr(mype, 'FileInfo'):
                    for entry in mype.FileInfo:
                        if hasattr(entry, 'StringTable'):
                            for st in entry.StringTable:
                                for k, v in st.entries.items():
                                    #print k + ": " + v
                                    print k + ": " + v
                                    self.info_file.write(k + ": " + v + '\n')
        self.info_file.close()



    def isPeFile(self,filepath):
        str_file = filepath
        file = open(str_file,'r')
        dosSign = hex(struct.unpack("h",file.read(2))[0])
        # print dosSign
        if dosSign == '0x5a4d':
            file.seek(0x3c)
            data_fNew = hex(struct.unpack('l', file.read(4))[0])
            # print data_fNew
            file.seek(int(data_fNew,16))
            # print int(data_fNew,16)
            peSign = hex(struct.unpack("h",file.read(2))[0])
            # print peSign
            if peSign == '0x4550':
                return True
            else:
                return False
        else:
            return False


if __name__=='__main__':
    print 'main_funciton'
    ger = GetPERightInfo() # 初始化 类的实例
    pe_l = ger.enumerate_pefile() # get pefile list
    ger.getpeinfo(pe_l)  # use pefile list to parse pefile and get Copyright info


