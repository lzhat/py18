################################################################
# 微信跳一跳，半自动程序。
# 知识点：
# 1: os.system()
#     def system(*args, **kwargs): # real signature unknown
#         """ Execute the command in a subshell. """
#         pass
# 2. coor.pop()
#    列表中的值使用后就丢弃的话，建议使用pop()方法
# 3.手机截图命令：adb shell screencap -p [图片路径]
# 4.手机截图保存：adb pull [图片路径]
# 5.模拟滑动事件：adb shell input touchscreen swipe x1 y1 x2 y2 time


# 准备工作：
#     adb驱动
#     Andore手机
#     手机打开开发者模式
#     打开手机的调试模式
#     手机与电脑相连
#################################################################

import os
import numpy
import matplotlib.pyplot as plt
import PIL
from matplotlib.animation import FuncAnimation
import time

need_update = True


# 获取截图
def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png')  # 截取手机屏幕
    os.system('adb pull /sdcard/screen.png')  # 把手机上的截图拿到电脑上
    return numpy.array(PIL.Image.open('screen.png'))  # 打开当前文件下的图片


# 执行跳的操作
def jump_to_next(point1, point2):
    x1, y1 = point1
    x2, y2 = point2  # 把两次点击的坐标取出来
    #  计算弦的长度
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    os.system('adb shell input swipe 300 400 300 400 {}'.format(int((distance * 1.35))))  # 按下的坐标，抬起的坐标，按压的时间
    global need_update
    need_update = True
    # time.sleep(1)


# 绑定鼠标的单击事件
def on_click(event, coor=[]):
    # 参数event是点击的位置
    x, y = event.xdata, event.ydata  # 刚刚点击的坐标
    coor.append((x, y))  # 把一次点击的坐标添加到列表
    if len(coor) == 2:  # 通过坐标的数量，判断当前是否点击了两次
        # jump_to_next(coor[0],coor[1])
        # coor=[]
        # 用列表的pop代替上面的方法
        jump_to_next(coor.pop(), coor.pop())


# 更新图片
def update_screen(frames):
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image())
        need_update = False
    return axes_image,


figure = plt.figure()  # 创建一张空白图片
axes_image = plt.imshow(get_screen_image(), animated=True)  # 把截图画到刚才的空白图片对象里面
figure.canvas.mpl_connect('button_press_event', on_click)  # 绑定鼠标事件
ani = FuncAnimation(figure, update_screen, interval=300, blit=True)
plt.show()  # 显示
