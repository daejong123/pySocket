
from wonderBits import Display, Led, Control
from wonderBits import Display
import random
import time

display1 = Display(1)
display2 = Display(2)
control1 = Control(1)
control2 = Control(2)
led = Led(1)

time.sleep(8)

display1.print(1, 1, 'hello')
display2.print(1, 1, "world")
state = display1.get_button_state()
print('收到显示模块按钮状态 {}'.format(state))

m1 = control1.get_m1_value()
print('收到获取m1的值为 {}'.format(m1))


@control1.event.sw1_pressed()
def whenSw1Pressed(data):
    if data:
        led.set_rgb(0, 0, 255)
        display2.set_direction_regular()
        sw4 = control1.get_sw4()
        print('我收到sw4状态{}'.format(sw4))
        print("_______________________")

@control2.event.sw2_pressed()
def whenSw2Pressed(data):
    if data:
        led.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        display2.set_direction_reverse()
        isAtOne = control1.is_sw3_at_1()
        print('我收到sw在1位置: {}'.format(isAtOne))
        print("************************")

@display2.register_button
def whenDisplayButton(data):
    print("显示模块被拨动{}".format(data))
    led.fade_to_rgb(30, 30, 30, 1000)

# python3 setup.py sdist bdist_wheel
# twine upload dist/*
