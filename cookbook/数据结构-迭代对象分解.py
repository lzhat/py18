# 对于固定长度可迭代的对象(字符串、文件、迭代器及生成器)，进行分解操作
s1 = 'Hello'
a, b, c, d, e = s1
print(a, b, c, d, e)  # H e l l o

data1 = ['ACEM', 50, (2012, 12, 21)]
_, shares, _ = data1
print(shares)  # 50

p1 = (4, 5)
x, y = p1
print(x)  # 4

# 对于任意长度可迭代的对象(字符串、file_summary、迭代器及生成器)，进行分解操作
record1 = ('Dave', 'dave@example.com', '133', '137')
name, email, *phone_number = record1
print(phone_number)  # ['133', '137']

head, *tail, end = [1, 10, 7, 4, 5, 9]
print(tail)  # [10, 7, 4, 5]

