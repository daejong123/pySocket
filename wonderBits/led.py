from .wbits import Wonderbits



class Led(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def set_rgb(self, r, g, b):
        """设置彩灯颜色 """
        command = 'led{}.set_rgb({},{},{})'.format(self.index,r,g,b)
        self._set_command(command)
    
    def fade_to_rgb(self, r, g, b, total, step = 50, key = False):
        """设置彩灯由当前颜色渐变到目标颜色 """
        command = 'led{}.fade_to_rgb({},{},{},{},{},{})'.format(self.index,r,g,b,total,step,key)
        self._set_command(command)
    