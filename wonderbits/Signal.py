from .wbits import Wonderbits



class Signal(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def set_rgb(self, r, g, b):
        """设置LED灯颜色 """
        command = 'signal{}.set_rgb({},{},{})'.format(self.index,r,g,b)
        self._set_command(command)
    
    def set_buzzer(self, frequency):
        """设置蜂鸣器声音频率，单位,Hz,设置频率为0表示关闭蜂鸣器 """
        command = 'signal{}.set_buzzer({})'.format(self.index,frequency)
        self._set_command(command)
    
    def set_vibration(self, strength):
        """设置震动马达的震动幅度,这里的振动幅度没有单位，值越大表示震动幅度越大，参数为0则停止震动 """
        command = 'signal{}.set_vibration({})'.format(self.index,strength)
        self._set_command(command)
    
    def play_a_note(self, frequency, time):
        """设置蜂鸣器以一个固定频率发声并保持一段时间后关闭蜂鸣器 """
        command = 'signal{}.play_a_note({},{})'.format(self.index,frequency,time)
        self._set_command(command)
    