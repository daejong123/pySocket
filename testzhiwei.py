from wonderbits import Display, Control, Hall, Pulse
import time
import math

d1 = Display()
c1 = Control()
# s1 = Signal()
p1 = Pulse()
h1 = Hall()
# #
time.sleep(3)
# #
# content = 1
# for i in range(100):
#     d1.print(1, 1, content)
#     content += 1

# d1.turn_to_page(3)
# time.sleep(2)
# d1.turn_to_page(2)
# s1.play_a_note(600, 2000)
# h1.calibrate()
value = p1.get_heart_rate()
d1.print(1, 1, c1.is_sw1_pressed())