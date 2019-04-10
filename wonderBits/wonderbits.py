# Insert your code here. 

import socketio
import time
import json

class Wonderbits(object):

    init_flag = False
    eventCallback = {}

    def __init__(self):
        self.sio = socketio.Client()
        self.sio.connect('http://localhost:8082')
        if Wonderbits.init_flag:
            return
        print('wonderbits初始化')
        Wonderbits.init_flag = True

        @self.sio.on('connect')
        def on_connect():
            print('connection established')

        @self.sio.on('mfe-data')
        def on_message(data):
            print('mfe-data received {}'.format(data))

        @self.sio.on('disconnect')
        def on_disconnect(data):
            print('disconnected from server')

        @self.sio.on('event')
        def on_event(data):
            try:
                obj = json.loads(data)
                if obj['type'] == 'event':
                    key = '{}.{}'.format(obj['module'], obj['source']);
                    if Wonderbits.eventCallback[key]:
                        Wonderbits.eventCallback[key]({ "module": obj['module'], "source": obj['source'], "value":obj['value'] })
            except:
                pass

    # 事件注册回调
    def register_event(self, moduleName, source, cb):
        self.sio.emit('mfe-message', '{}.register.{}()'.format(moduleName, source))
        Wonderbits.eventCallback['{}.{}'.format(moduleName, source)] = cb

     # 自定义sleep
    def setTimeOut(self,loop_forever_time = 1, timeInterval = 0.01,  breakProperty = 'r',  breakValue = '0'):
        count = loop_forever_time // timeInterval
        while count > 0:
            if self.__dict__[breakProperty] != breakValue:
                break
        time.sleep(timeInterval)
        count = count - 1

    # 自定义发送内容
    def send_msg(self, msg):
        sio.emit('mfe-message {}'.format(msg))


