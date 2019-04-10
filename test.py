from wonderBits import Display, Led, Control
import random

display1 = Display(1)
display2 = Display(2)
control1 = Control(1)
led = Led(1)

# 设置值
display1.print(1, 1, "hello")
display2.print(1, 1, "world")


# 发送获取值
state = display1.get_button_state()
print('收到状态 {}'.format(state))

m1 = control1.get_m1_value()
print('收到获取 {}'.format(m1))


# 注册sw1被按下事件
@control1.register_sw1
def whenSw1Pressed(data):
    if data:
        led.set_rgb(0, 0, 255)
        display2.set_direction_regular()

# 注册sw2被按下事件
@control1.register_sw2
def whenSw2Pressed(data):
    if data:
        led.set_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        display2.set_direction_reverse()
        isAtOne = control1.is_sw3_at_1()
        print('sw在1位置: {}'.format(isAtOne))
        control1.set_m1_m2_sensitivity(40)
        sw4 = control1.get_sw4()
        print('sw4状态{}'.format(sw4))


@display2.register_button
def whenDisplayButton(data):
    print("显示模块被拨动{}".format(data))
    led.fade_to_rgb(30, 30, 30, 1000)

# python3 setup.py sdist bdist_wheel
# twine upload dist/* 
