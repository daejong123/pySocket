from .wbits import Wonderbits



class Hall(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def register_magnetic(self, cb):
        self._register_event('hall{}'.format(self.index), 'magnetic', cb)
    
    def get_magnetic(self):
        """该函数用于获取霍尔检测的磁场强度值 """
        command = 'hall{}.get_magnetic()'.format(self.index)
        self._get_command(command)
        return self._result
    
    def calibrate(self):
        """校准霍尔传感器零点,使用该函数时，霍尔模块指示灯会在校准执行过程中变为黄色，校准完成后回复原有颜色。,校准过程中保证没有磁性物体靠近模块，否则会导致校准后的零点不准确。 """
        command = 'hall{}.calibrate()'.format(self.index)
        self._set_command(command)
    