from wonderbits import Display, Control, Led
import time
import random

# 初始化模块
d1 = Display()
c1 = Control()
l1 = Led()


d1.show_console()

# 显示模块显示内容
d1.print(2, 1, 'value:')

# 计数变量
content = 1

for i in range(50):
    # 获取控制模块开关sw4的值
    sw4 = c1.get_sw4()
    # 在显示屏上显示sw4的值
    d1.print(2, 7, sw4)
    # 设置彩灯rbg随机颜色
    l1.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 显示模块显示计数值 
    d1.print(1, 1, content)
    # 将计数变量 递增1
    content += 1
