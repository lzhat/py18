import sys
# 1. 调用同级目录下的test3

from test_path.path1 import test3
from test_path.path1.path3 import test5

test3.loggin()
print(test5.loggin())

print(sys.path)

# import os, sys
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0,parentdir)

# 建议用sys.path.insert(0,parentdir) 而不是用sys.path.append(parentdir)。
# 因为是遍历搜索路径的，所以如果在其它路径里也有个同名的module，会import错。
# 用sys.path.insert(0,parentdir)可以确保先搜索这个路径。
'''
在实际项目中，经常要对程序目录进行规范化存储，这就必然涉及到不同目录间模块的调用。
python中，import module会去sys.path搜索，sys.path是个列表，并且我们可以动态修改。
要import某个目录的module，我们sys.path.insert(0,somedir)来加入搜索路径，就可以import了。
既然这样，要import上一级目录的module,可以sys.path.insert(0,parentdir)。
不过这种写绝对路径的方式，如果文件放到其它地方，就不行了。 
所以用动态方法来获取上一级目录。
'''
