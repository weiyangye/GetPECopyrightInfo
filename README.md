# GetPECopyrightInfo
获取PE文件的版权信息
# 主要目的
需要获取PE文件的详细信息，用以归类或者其他操作
# 产生的信息如下：
```
C:\Python27\python.exe D:/Working_Data/Project_Reasrch/GetPECopyrightInfo/ParserPE.py
main_funciton
['c:\\Windows\\twain_32.dll']
PEFile_Path: c:\Windows\twain_32.dll
PE INFO: 
InternalName: DSM
FileVersion: 1,7,1,3
CompanyName: Twain Working Group
ProductName: Twain_32 Source Manager
ProductVersion: 1,7,1,0
FileDescription: Twain_32 Source Manager (Image Acquisition Interface)
OriginalFilename: Twain_32.dll
Process finished with exit code 0
```
# 更新日志
## 2015.12.25
解决 UnicodeEncodeError: 'gb2312' codec can't encode character u'\xa9' in position 9: illegal multibyte sequence
\br
参考链接:
[解决Python2.7的UnicodeEncodeError: ‘ascii’ codec can’t encode异常错误](http://wangye.org/blog/archives/629/)

# 注意事项
## 1. 在windows 7 中文32位下，需使用如下方式执行才能得到正确结果
```
C:\Users\Admin\Desktop\GetPECopyrightInfo>ParserPE.py >11.txt
```
猜测原因是由于操作系统字符集造成的问题