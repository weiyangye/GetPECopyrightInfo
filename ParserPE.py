# *.* coding=utf-8
__time__ = '2015.12.14'
__author__ = 'weiyangye@hotmail.com'

import os
import sys
import pefile
import glob
import struct
pefiledir = r"d:\Working_Data\Vunl_Work\Crack_WPS_ProSuite\Code\*.dll"

class GetPERightInfo():
    def __init__(self):
        self.filelist = []

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
            mype = pefile.PE(peFile)
            # mype = pefile.PE(pefilepath)
            # print pe # parse_version_information('MajorLinkerVersion')
            if hasattr(mype, 'VS_VERSIONINFO'):
                if hasattr(mype, 'FileInfo'):
                    for entry in mype.FileInfo:
                        if hasattr(entry, 'StringTable'):
                            for st in entry.StringTable:
                                for k, v in st.entries.items():
                                    print k + ": " + v
            print '\n'


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
    ger = GetPERightInfo()
    pe_l = ger.enumerate_pefile()
    print pe_l
    ger.getpeinfo(pe_l)
