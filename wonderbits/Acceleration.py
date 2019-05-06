from .wbits import Wonderbits



class Acceleration(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def register_x_acceleration(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'x_acceleration', cb)
    
    def register_y_acceleration(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'y_acceleration', cb)
    
    def register_z_acceleration(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'z_acceleration', cb)
    
    def register_acceleration(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'acceleration', cb)
    
    def register_x_angular_velocity(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'x_angular_velocity', cb)
    
    def register_y_angular_velocity(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'y_angular_velocity', cb)
    
    def register_z_angular_velocity(self, cb):
        self._register_event('acceleration{}'.format(self.index), 'z_angular_velocity', cb)
    
    def get_x_acceleration(self):
        """该函数用于获取加速度传感器检测的x轴加速度值，单位,m/s2 """
        command = 'acceleration{}.get_x_acceleration()'.format(self.index)
        self._get_command(command)
        return self._result
    
    def get_y_acceleration(self):
        """该函数用于获取加速度传感器检测的y轴加速度值，单位,m/s2 """
        command = 'acceleration{}.get_y_acceleration()'.format(self.index)
        self._get_command(command)
        return self._result
    
    def get_z_acceleration(self):
        """该函数用于获取加速度传感器检测的z轴加速度值，单位,m/s2 """
        command = 'acceleration{}.get_z_acceleration()'.format(self.index)
        self._get_command(command)
        return self._result
    
    def get_acceleration(self):
        """该函数用于获取加速度传感器检测的x、y、z三轴合加速度值，单位,m/s2 """
        command = 'acceleration{}.get_acceleration()'.format(self.index)
        self._get_command(command)
        return self._result
    
    def get_x_angular_velocity(self):
        """该函数用于获取加速度传感器检测的x轴角速度值，单位,°/s """
        command = 'acceleration{}.get_x_angular_velocity()'.format(self.index)
        self._get_command(command)
        return self._result
    
    def get_y_angular_velocity(self):
        """该函数用于获取加速度传感器检测的y轴角速度值，单位,°/s """
        command = 'acceleration{}.get_y_angular_velocity()'.format(self.index)
        self._get_command(command)
        return self._result
    
    def get_z_angular_velocity(self):
        """该函数用于获取加速度传感器检测的z轴角速度值，单位,°/s """
        command = 'acceleration{}.get_z_angular_velocity()'.format(self.index)
        self._get_command(command)
        return self._result
    
    def calibrate(self):
        """校准加速度传感器零点,使用该函数时，加速度模块指示灯会在校准执行过程中变为黄色，校准完成后回复原有颜色。,校准过程中需要保证加速度模块且保持静止不动，有汉字的一面朝上。 """
        command = 'acceleration{}.calibrate()'.format(self.index)
        self._set_command(command)
    