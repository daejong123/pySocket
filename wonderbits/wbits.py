
import time
import json
from .wbSerial import WBSerial
import threading
import os

class Wonderbits(object):
    '''
    单例模式
    该类是所有豌豆拼的父类，
    '''
    
    # 供返回类的函数使用
    _result = None
    # 供命令完成返回标志
    _command = None
    # 该类初始化标志
    _init_flag = False
    # 存储事件注册的key，value
    _event_call_back_dict = {}
    # link-socket通信的串口
    _wbSerial = None

    def __init__(self):
        if not Wonderbits._init_flag:
            print('wonderbits初始化！')
            try:
                Wonderbits._wbSerial = WBSerial()
                Wonderbits._wbSerial.event_data_cb = self._event_data_from_local_py_serial
                Wonderbits._wbSerial.reporter_data_cb = self._reporter_data_from_local_py_serial
                Wonderbits._wbSerial.command_finish_cb = self._command_data_from_local_py_serial
                Wonderbits._init_flag = True
            except Exception as e:
                print('wonderbits初始化失败!', e)
    
    # 隐藏控制台输出
    def hide_console(self):
        Wonderbits._wbSerial._is_show_console = False
                    
    # 开启控制台输出
    def show_console(self):
        Wonderbits._wbSerial._is_show_console = True

    # 本地串口通信的事件通知
    def _event_data_from_local_py_serial(self, data):
        self._parse_event_data_and_notify(data)
    
    # 本地串口通信的返回类函数命令完成的通知
    def _reporter_data_from_local_py_serial(self, value):
        Wonderbits._result = self._format_str_to_bool_int_float(value)

    # 本地串口通信的设置类命令完成的通知
    def _command_data_from_local_py_serial(self, key):
        Wonderbits._command = key.strip()

    # 解析数据，并且通知调用者 
    def _parse_event_data_and_notify(self, data):
        try:
            obj = json.loads(data)
            if obj['type'] == 'event':
                key = '{}.{}'.format(obj['module'], obj['source'])
                if Wonderbits._event_call_back_dict[key]:
                    return_value = self._format_str_to_bool_int_float(obj['value'])
                    # { "module": obj['module'], "source": obj['source'], "value":obj['value'] }
                    Wonderbits._event_call_back_dict[key](return_value)
        except:
            pass

    # 事件注册类
    def register_event(self, module_name, source, cb):
        cmd = '{}.register.{}()'.format(module_name, source)
        self._wbSerial.write_command(cmd)
        Wonderbits._event_call_back_dict['{}.{}'.format(module_name, source)] = cb

    # 设置类
    def set_command(self, command):
        self._wbSerial.write_command(command)
        Wonderbits._command = None
        self._set_command_time_out(3, command)

    # 获取类
    def get_command(self, command):
        self._wbSerial.write_command(command)
        Wonderbits._result = None
        self._set_time_out(3)

    # 供设置类命令 使用
    # 给sdk中带返回值函数使用---自定义sleep(采用超时机制)
    def _set_command_time_out(self, loop_forever_time=0.1, break_value = None):
        try:
            time_interval = 0.001
            count = loop_forever_time // time_interval
            while count > 0:
                if Wonderbits._command == break_value:
                    break
                time.sleep(time_interval)
                count = count - 1
        except KeyboardInterrupt as e:
            print('exit-wb')
            os._exit(0)
        
    # 供获取类命令 使用
    # 给sdk中带返回值函数使用---自定义sleep(采用超时机制)
    def _set_time_out(self, loop_forever_time=0.1, break_value=None):
        try:
            time_interval = 0.001
            count = loop_forever_time // time_interval
            while count > 0:
                if Wonderbits._result != break_value:
                    break
                time.sleep(time_interval)
                count = count - 1
        except KeyboardInterrupt as e:
            print('exit-wb')
            os._exit(0)

    # 工具函数：将字符串转成bool int float
    def _format_str_to_bool_int_float(self, data):
        return_value = data
        try:
            if data.startswith('\'') and data.endswith('\''):
                return_value = data
            elif data == 'True':
                return_value = True
            elif data == 'False':
                return_value = False
            elif data.find(".") != -1:
                return_value = float(return_value)
            elif data.find(".") == -1:
                return_value = int(return_value)
            return return_value
        except Exception as e:
            pass
