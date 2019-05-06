from .wbits import Wonderbits



class Driver(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def set_motor_a(self, speed, time = 10):
        """设置电机A转动 """
        command = 'driver{}.set_motor_a({},{})'.format(self.index,speed,time)
        self._set_command(command)
    
    def stop_motor_a(self):
        """设置电机A停止转动 """
        command = 'driver{}.stop_motor_a()'.format(self.index)
        self._set_command(command)
    
    def set_motor_b(self, speed, time = 10):
        """设置电机B转动 """
        command = 'driver{}.set_motor_b({},{})'.format(self.index,speed,time)
        self._set_command(command)
    
    def stop_motor_b(self):
        """设置电机B停止转动 """
        command = 'driver{}.stop_motor_b()'.format(self.index)
        self._set_command(command)
    
    def set_servo1(self, angle):
        """设置舵机1转动到指定角度,使用此函数后舵机1将拥有维持角度的扭矩，施加外力改变舵机1的角度会很困难 """
        command = 'driver{}.set_servo1({})'.format(self.index,angle)
        self._set_command(command)
    
    def shut_servo1(self):
        """关闭舵机1,使用此函数后舵机1将失去维持角度的扭矩，施加外力可以轻松改变舵机1的角度 """
        command = 'driver{}.shut_servo1()'.format(self.index)
        self._set_command(command)
    
    def set_servo2(self, angle):
        """设置舵机2转动到指定角度,使用此函数后舵机2将拥有维持角度的扭矩，施加外力改变舵机2的角度会很困难 """
        command = 'driver{}.set_servo2({})'.format(self.index,angle)
        self._set_command(command)
    
    def shut_servo2(self):
        """关闭舵机2,使用此函数后舵机2将失去维持角度的扭矩，施加外力可以轻松改变舵机2的角度 """
        command = 'driver{}.shut_servo2()'.format(self.index)
        self._set_command(command)
    