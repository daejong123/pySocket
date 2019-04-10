from .wonderbits import Wonderbits

class Control(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def register_sw3(self, cb):
        self.register_event('control{}'.format(self.index), 'sw3', cb)
    
    def register_sw1(self, cb):
        self.register_event('control{}'.format(self.index), 'sw1', cb)
    
    def register_sw2(self, cb):
        self.register_event('control{}'.format(self.index), 'sw2', cb)
    
    def register_m1(self, cb):
        self.register_event('control{}'.format(self.index), 'm1', cb)
    
    def register_m2(self, cb):
        self.register_event('control{}'.format(self.index), 'm2', cb)
    
    def register_sw4(self, cb):
        self.register_event('control{}'.format(self.index), 'sw4', cb)
    
    def register_m1_value(self, cb):
        self.register_event('control{}'.format(self.index), 'm1_value', cb)
    
    def register_m2_value(self, cb):
        self.register_event('control{}'.format(self.index), 'm2_value', cb)
    
    def is_sw1_pressed(self):
        msg = 'control{}.is_sw1_pressed()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def is_sw2_pressed(self):
        msg = 'control{}.is_sw2_pressed()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def is_m1_connected(self):
        msg = 'control{}.is_m1_connected()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def is_m2_connected(self):
        msg = 'control{}.is_m2_connected()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def is_sw3_at_1(self):
        msg = 'control{}.is_sw3_at_1()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def get_sw4(self):
        msg = 'control{}.get_sw4()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def set_m1_m2_sensitivity(self, limit):
        self.sio.emit("mfe-message", 'control{}.set_m1_m2_sensitivity({})'.format(self.index,limit))
    
    def get_m1_value(self):
        msg = 'control{}.get_m1_value()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def get_m2_value(self):
        msg = 'control{}.get_m2_value()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    