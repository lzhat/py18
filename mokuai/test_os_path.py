import os

path = 'D:\PycharmProjects\py18\mokuai\py.txt'

# os.path.abspath(path)
# """ Return the absolute version of a path."""
# 返回path规范化的绝对路径, 将相对路径转换为绝对路径
print(os.path.abspath(path))

# os.path.split(path)
# """Split a pathname.
#    Return tuple (head, tail) where tail is everything after the final slash.
#    Either part may be empty."""
#    将path分割成目录和文件名二元组返回。
# os 拆分路径，返回一个tuple，第一个元素是文件所在路径，第二个元素是对应文件名。
print(os.path.split(path))

# os.path.dirname(path)
# """Returns the directory component of a pathname"""
# 返回path的目录。其实就是os.path.split(path)的第一个元素。
print(os.path.dirname(path))

# os.path.basename(path)
# """Returns the final component of a pathname"""
# 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素。
# 只获取某路径对应的文件名。
print(os.path.basename(path))

# os.path.commonprefix(list)
# "Given a list of pathnames, returns the longest common leading component"
# 返回list中，所有path共有的最长的路径。
# 在一组路径中，找到一个共同的前缀，
print(os.path.commonprefix(['/home/td','/home/td/ff','/home/td/fff']))

# os.path.exists(path)
# """Test whether a path exists.  Returns False for broken symbolic links"""
# 如果path存在，返回True；如果path不存在，返回False。
print(os.path.exists(path))

# os.path.isabs(path)
# """Test whether a path is absolute"""
# 如果path是绝对路径，返回True。
print(os.path.isabs(path))

# os.path.isfile(path)
# """Test whether a path is a regular file"""
# 如果path是一个存在的文件，返回True, 否则返回False.
print(os.path.isfile(path))

# os.path.isdir(path)
# 如果path是一个存在的目录，则返回True。否则返回False。
print(os.path.isdir(path))

# os.path.join(path1[, path2[, ...]])
# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略。
# 使用os.path.join 组合一些零散的字符串，生成一个安全的路径表示
print(os.path.join('c:\\', 'csv', 'test.csv'))

# os.path.normcase(path)
# """Normalize case of pathname. Makes all characters lowercase and all slashes into backslashes."""
# 在Linux和Mac平台上，该函数会原样返回path，在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为饭斜杠。
print(os.path.normcase(path))


# os.path.normpath(path)
# """Normalize path, eliminating double slashes, etc."""
# 规范化路径。 处理不规则路径字符串，将其转化为正常的路径
print(os.path.normpath('c://windows\\System32\\../Temp/'))

# os.path.splitdrive(path)
print(os.path.splitdrive(path))

# os.path.splitext(path)
# 将路径、文件名、扩展名分开，并以一个tuple 的形式返回
print(os.path.splitext(path))


# os.path.getsize(path)
# 返回path的文件的大小（字节）
print(os.path.getsize(path))

