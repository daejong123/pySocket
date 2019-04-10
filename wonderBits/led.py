from .wonderbits import Wonderbits

class Led(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def set_rgb(self, r, g, b):
        self.sio.emit("mfe-message", 'led{}.set_rgb({},{},{})'.format(self.index,r,g,b))
    
    def set_brightness(self, brightness):
        self.sio.emit("mfe-message", 'led{}.set_brightness({})'.format(self.index,brightness))
    
    def fade_to_rgb(self, r, g, b, total, step = 50, key = False):
        self.sio.emit("mfe-message", 'led{}.fade_to_rgb({},{},{},{},{},{})'.format(self.index,r,g,b,total,step,key))
    