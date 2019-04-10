from .wonderbits import Wonderbits

class RfCommunication(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def register_button(self, cb):
        self.register_event('rfcommunication{}'.format(self.index), 'button', cb)
    
    def register_msg_received(self, cb):
        self.register_event('rfcommunication{}'.format(self.index), 'msg_received', cb)
    
    def get_msg(self):
        msg = 'rfcommunication{}.get_msg()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def clear_msg(self):
        self.sio.emit("mfe-message", 'rfcommunication{}.clear_msg()'.format(self.index))
    
    def get_unread_msg_count(self):
        msg = 'rfcommunication{}.get_unread_msg_count()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def read(self):
        msg = 'rfcommunication{}.read()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def send(self):
        self.sio.emit("mfe-message", 'rfcommunication{}.send()'.format(self.index))
    
    def init(self, name):
        self.sio.emit("mfe-message", 'rfcommunication{}.init({})'.format(self.index,name))
    
    def is_button_pressed(self):
        msg = 'rfcommunication{}.is_button_pressed()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    