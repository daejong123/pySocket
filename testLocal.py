
from wonderbits import Display, Led, Control, LightBelt, Signal
import random
import time

display1 = Display()
led = Led()
control1 = Control()
# lightBelt = LightBelt()
signal = Signal()


time.sleep(3)
# lightBelt.set_leds_rgb(1, 10, 255, 0, 0)
signal.set_rgb(255, 255, 0)


@control1.event.sw1_pressed()
def whenSw1Pressed(data):
    if data:
        sw4 = control1.get_sw4()
        display1.print(1, 1, sw4)
        print('我收到sw4状态{}'.format(sw4))

@control1.event.sw2_pressed()
def whenSw2Pressed(data):
    if data:
        isAtOne = control1.is_sw3_at_1()
        display1.print(1, 1, isAtOne)
        print('我收到sw在1位置{}'.format(isAtOne))

# content = 1
# while True:
#     display1.print(1, 1, content)
#     content = content + 1
#     led.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# 获取类
#     sw4 = control1.get_sw4()
#     print('我收到sw4状态{}'.format(sw4))
#     isAtOne = control1.is_sw3_at_1()
#     print('我收到sw在1位置: {}'.format(isAtOne))

'''
def __init__(self, index=1):
        Wonderbits.__init__(self)
        self.index = index
        self.event = Control._Event(self)

    class _Event():
        def __init__(self, this):
            self.this = this

        def sw1_pressed(self):
            def wrapper(cb):
                self.this._register_event(
                    'control{}'.format(self.this.index), 'sw1', cb)
            return wrapper

        def sw2_pressed(self):
            def wrapper(cb):
                self.this._register_event(
                    'control{}'.format(self.this.index), 'sw2', cb)
            return wrapper

'''