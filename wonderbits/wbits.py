
import socketio
import time
import json
from .wbSerial import WBSerial
import threading

class Wonderbits(object):
    
    r = None
    init_flag = False
    eventCallback = {}
    wbSerial = None
    localSerial = False

    def __init__(self):
        self.sio = socketio.Client()
        try:
            self.sio.connect('http://localhost:8082')
        except Exception as e:
            self.localSerial = True
            if not Wonderbits.init_flag:
                print(e, '采用本地连接！')
                Wonderbits.wbSerial = WBSerial()
                Wonderbits.wbSerial.eventDataCb = self.eventDataFromLocalPySerial
                Wonderbits.wbSerial.reporterDataCb = self.reporterDataFromLocalPySerial
                    
        if not Wonderbits.init_flag:
            print('wonderbits初始化')

            @self.sio.on('connect')
            def on_connect():
                print('connection established')

            @self.sio.on('mfe-data')
            def on_message(data):
                print('串口收到 {}'.format(data))
                pass

            @self.sio.on('event')
            def on_event(data):
                self.parseEventDataAnddoNoti(data)

        Wonderbits.init_flag = True

    def eventDataFromLocalPySerial(self, data):
        self.parseEventDataAnddoNoti(data)
    
    def reporterDataFromLocalPySerial(self, key, value):
        Wonderbits.r = self._formatStr(value)

    # 事件注册
    def register_event(self, moduleName, source, cb):
        cmd = '{}.register.{}()'.format(moduleName, source)
        if self.localSerial:
            self.wbSerial.writeCommand(cmd)
        else:
            self.sio.emit('mfe-message', cmd)
        Wonderbits.eventCallback['{}.{}'.format(moduleName, source)] = cb

    # 设置类
    def set_command(self, command):
        if self.localSerial:
            self.wbSerial.writeCommand(command)
        else:
            self.sio.emit("mfe-message", command)
        time.sleep(.04)

    # 获取类
    def get_command(self, command):
        if self.localSerial:
            self.wbSerial.writeCommand(command)
            Wonderbits.r = None
        else:
            self.sio.emit('mfe-reporter', command)
            Wonderbits.r = None
            @self.sio.on(command)
            def on_data(data):
                Wonderbits.r = self._formatStr(data)
        self._setTimeOut(3)

    def parseEventDataAnddoNoti(self, data):
        try:
            obj = json.loads(data)
            if obj['type'] == 'event':
                key = '{}.{}'.format(obj['module'], obj['source'])
                if Wonderbits.eventCallback[key]:
                    returnValue = self._formatStr(obj['value'])
                    # { "module": obj['module'], "source": obj['source'], "value":obj['value'] }
                    Wonderbits.eventCallback[key](returnValue)
        except:
            pass

     # 自定义sleep
    def _setTimeOut(self, loop_forever_time=0.1, timeInterval=0.001,  breakProperty='r',  breakValue=None):
        count = loop_forever_time // timeInterval
        while count > 0:
            if breakProperty != "" and Wonderbits.__dict__[breakProperty] != breakValue:
                break
            time.sleep(timeInterval)
            count = count - 1

    # 自定义发送内容
    def _send_msg(self, msg):
        self.sio.emit('mfe-message', '{}'.format(msg))

    # 将字符串转成bool int float
    def _formatStr(self, data):
        returnValue = data
        try:
            if data.startswith('\'') and data.endswith('\''):
                returnValue = data
            elif data == 'True':
                returnValue = True
            elif data == 'False':
                returnValue = False
            elif data.find(".") != -1:
                returnValue = float(returnValue)
            elif data.find(".") == -1:
                returnValue = int(returnValue)
            return returnValue
        except Exception as e:
            pass
