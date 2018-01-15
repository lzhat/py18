__author__ = 'lzh'

import chardet

# def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
#  known special case of open
#  Open file and return a stream.  Raise IOError upon failure.
#  Character Meaning
#    --------- ---------------------------------------------------------------
#    'r'       open for reading (default)
#    'w'       open for writing, truncating the file first
#    'x'       create a new file and open it for writing
#    'a'       open for writing, appending to the end of the file if it exists
#    'b'       binary mode
#    't'       text mode (default)
#    '+'       open a disk file for updating (reading and writing)
#    'U'       universal newline mode (deprecated)
#    --------- ---------------------------------------------------------------


# 打开文件，获得文件句柄，
f_temp = open('测试文件.txt', mode='r')

f = open('1.txt', 'r', encoding='utf-8')


print(f.encoding)
# 读取文件内容
# data = f_temp.read()
#
# f_temp.close()
# print(data)


# f_write = open('测试文件2.txt', mode='w', encoding='GBK')
# # for line in data:
# #     f_write(line)
# f_write.write(data)
# f_write.close()
