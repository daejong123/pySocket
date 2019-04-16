from wonderBits import Display,Led,Control

import time

l1 = Led()

c1 = Control()

d1 = Display(1)



time.sleep(10)

# l1.set_rgb(100,0,0)
# time.sleep(1)

# l1.set_rgb(0,100,0)
# time.sleep(1)

# l1.set_rgb(0,0,100)
# time.sleep(1)

# d1.set_direction_reverse()

d1.print(1,1,'hello Init...')


while True:
    pos = c1.get_sw4()
    d1.print(1,1, pos)