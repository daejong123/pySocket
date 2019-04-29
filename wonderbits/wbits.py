
import socketio
import time
import json
from .wbSerial import WBSerial
import threading

class Wonderbits(object):
    
    # 供返回类的函数使用
    _result = None
    # 初始化标志
    _init_flag = False
    # 存储事件注册的key，value
    _event_call_back_dict = {}
    # link-socket通信的串口
    _wbSerial = None
    # pysocket通信的串口
    _local_serial = False

    def __init__(self):
        try:
            # 优先采用link方式通信
            self._sio = socketio.Client()
            self._sio.connect('http://localhost:8082')
        except Exception as e:
            self._local_serial = True
            if not Wonderbits._init_flag:
                print(e, 'wonderbits初始化本地连接！')
                # link方式通信失败时 采用本地串口通信
                Wonderbits._wbSerial = WBSerial()
                Wonderbits._wbSerial.event_data_cb = self._event_data_from_local_py_serial
                Wonderbits._wbSerial.reporter_data_cb = self._reporter_data_from_local_py_serial
                    
        # 采用link方式通信时，注册事件以及受到数据的回调
        if not Wonderbits._init_flag:
            print('wonderbits初始化')
            @self._sio.on('connect')
            def on_connect():
                print('connection established')

            @self._sio.on('mfe-data')
            def on_message(data):
                print('{}'.format(data))
                pass

            @self._sio.on('event')
            def on_event(data):
                self._parse_event_data_and_notify(data)

        Wonderbits._init_flag = True

    # 本地串口通信的事件通知
    def _event_data_from_local_py_serial(self, data):
        self._parse_event_data_and_notify(data)
    
    # 本地串口通信的返回类函数的返回值
    def _reporter_data_from_local_py_serial(self, key, value):
        Wonderbits._result = self._format_str_to_bool_int_float(value)

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
        if self._local_serial:
            self._wbSerial.write_command(cmd)
        else:
            self._sio.emit('mfe-message', cmd)
        Wonderbits._event_call_back_dict['{}.{}'.format(module_name, source)] = cb

    # 设置类
    def set_command(self, command):
        if self._local_serial:
            self._wbSerial.write_command(command)
        else:
            self._sio.emit("mfe-message", command)
        time.sleep(.04)

    # 获取类
    def get_command(self, command):
        if self._local_serial:
            self._wbSerial.write_command(command)
            Wonderbits._result = None
        else:
            self._sio.emit('mfe-reporter', command)
            Wonderbits._result = None
            @self._sio.on(command)
            def on_data(data):
                Wonderbits._result = self._format_str_to_bool_int_float(data)
        self._set_time_out(3)

    # 给sdk中带返回值函数使用---自定义sleep(采用超时机制)
    def _set_time_out(self, loop_forever_time=0.1, time_interval=0.001,  break_property='_result',  break_value=None):
        count = loop_forever_time // time_interval
        while count > 0:
            if break_property != "" and Wonderbits.__dict__[break_property] != break_value:
                break
            time.sleep(time_interval)
            count = count - 1

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
