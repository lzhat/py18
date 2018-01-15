import chardet
from chardet.universaldetector import UniversalDetector
import urllib.request


# # 1.测试网页内容编码
# # 获取网页内容
# data1 = urllib.request.urlopen('http://www.baidu.com').read()
#
# # 用chardet对内容解析
# chardit1 = chardet.detect(data1)
# print(chardit1)     # {'language': '', 'confidence': 0.99, 'encoding': 'utf-8'}


#  2.测试字符
# some_str1 = '你好'
# # print(some_str1.encode('utf-8'))  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
# result1 = chardet.detect(some_str1.encode('utf-8'))
# result2 = chardet.detect(some_str1.encode('GBK'))
# print(result1)  # {'encoding': 'utf-8', 'language': '', 'confidence': 0.7525}
# print(result2)  # {'encoding': 'TIS-620', 'confidence': 0.3598212120361634, 'language': 'Thai'}


# 3.检测文件
# 3.1 通过前5 行来判断文件编码
f_temp = open('测试文件.txt', 'rb')  # 测试文件.txt是一个WIN7系统下GB2312编码的文本文档
f_content = f_temp.read(5)  # 测试文件.txt 信息如下>>	文件编码语言：Russian	文件编码：KOI8-R	结果可信度：0.7679697235616183
enc = chardet.detect(f_content)
f_temp.close()
result = '测试文件.txt' + " 信息如下>>\n\t"+"文件编码语言：" + enc['language']+"\n\t文件编码："+enc['encoding']+"\n\t结果可信度："+ str(enc['confidence'])
print(result)
# 测试文件.txt 信息如下>>	文件编码语言：Russian	文件编码：KOI8-R	结果可信度：0.7679697235616183

# 3.2 读取全文来判断文件编码
f_temp = open('测试文件.txt', 'rb')  # 测试文件.txt是一个WIN7系统下GB2312编码的文本文档
f_content = f_temp.read()
enc = chardet.detect(f_content)
f_temp.close()
result = '测试文件.txt' + " 信息如下>>\n\t"+"文件编码语言：" + enc['language']+"\n\t文件编码："+enc['encoding']+"\n\t结果可信度："+ str(enc['confidence'])
print(result)
# 测试文件.txt 信息如下>>	文件编码语言：Chinese	文件编码：GB2312	结果可信度：0.99


# 3.3 高级应用，当用于检测的文档特别大时，可以chardet的子模块chardet.universaldetector。
# 这个模块允许我们分多次（逐行读取或者自行断行读取）检测文本的编码格式，当达到一定的阈值时便可以提前退出检测。
# 这样做可以有效地节省资源，提高程序效率，同时保证检测结果的准确性。

detector = UniversalDetector()  # 初始化一个UniversalDetector对象
detector.reset()  # 清除上次的检测结果
f = open('测试文件.txt', 'rb')  # 测试文件.txt是一个WIN7系统下GB2312编码的文本文档

for line in f:
    detector.feed(line)  # 逐行载入UniversalDetector对象中进行识别
    if detector.done:  # done为一个布尔值，默认为False，达到阈值时变为True
        break

detector.close()  # 调用该函数做最后的数据整合
f.close()
print(detector.result)
# {'language': 'Chinese', 'encoding': 'GB2312', 'confidence': 0.99}


