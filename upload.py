
@control1.event.sw1_pressed()
def asdf1():
    led1.set_rgb(100, 0, 0)


@control1.event.sw1_released()
def asdf2():
    led1.set_rgb(0, 0, 0)
