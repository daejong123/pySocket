from .wbits import Wonderbits



class LightBelt(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def set_leds_rgb(self, start, end, r, g, b):
        """设置灯带上某一段灯的颜色 """
        command = 'lightBelt{}.set_leds_rgb({},{},{},{},{})'.format(self.index,start,end,r,g,b)
        self._set_command(command)
    
    def set_single_led_rgb(self, num, r, g, b):
        """设置灯带上某个灯的颜色 """
        command = 'lightBelt{}.set_single_led_rgb({},{},{},{})'.format(self.index,num,r,g,b)
        self._set_command(command)
    