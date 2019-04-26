
from wonderbits import Display, Led, Control
import random
import time

display1 = Display()
led = Led()
control1 = Control()
control2 = Control(2)

time.sleep(8)

@control1.event.sw1_pressed()
def whenSw1Pressed(data):
    if data:
        sw4 = control1.get_sw4()
        print('我收到sw4状态{}'.format(sw4))
        print("----------------------")

@control2.event.sw2_pressed()
def whenSw2Pressed(data):
    if data:
        isAtOne = control1.is_sw3_at_1()
        print('我收到sw在1位置{}'.format(isAtOne))
        print("************************")

content = 1
while True:
    display1.print(1, 1, content)
    content = content + 1
    led.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# 获取类
#     sw4 = control1.get_sw4()
#     print('我收到sw4状态{}'.format(sw4))
#     isAtOne = control1.is_sw3_at_1()
#     print('我收到sw在1位置: {}'.format(isAtOne))


