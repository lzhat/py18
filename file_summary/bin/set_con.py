import os
import sys


# __file__获取当前程序的相对路径
# abspath 获取当前程序的绝对路径
# os.path.dirname(Path)获取当前程序的父目录的绝对路径
file_path = os.path.abspath(__file__)
super_path = os.path.dirname(file_path)
super_super_path = os.path.dirname(super_path)
# print(file_path)
# print(super_path)
# print(super_super_path)

# 将目标路径添加到系统环境变量中
sys.path.append(super_super_path)

from conf import conf_file

print(conf_file.loggin())



# 调用同级的
