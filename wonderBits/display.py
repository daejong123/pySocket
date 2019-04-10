from .wonderbits import Wonderbits

class Display(Wonderbits):
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    
    def register_button(self, cb):
        self.register_event('display{}'.format(self.index), 'button', cb)
    
    def get_button_state(self):
        msg = 'display{}.get_button_state()'.format(self.index)
        self.sio.emit('mfe-reporter', msg)
        self.r = '0'

        @self.sio.on(msg)
        def on_data(data):
            self.r = data

        self.setTimeOut()
        return self.r
    
    def print(self, row, column, text, size = 2):
        self.sio.emit("mfe-message", 'display{}.print({},{},\'{}\',{})'.format(self.index,row,column,text,size))
    
    def draw_dot(self, x, y, pageNum, saved = 0, writeColor = 1):
        self.sio.emit("mfe-message", 'display{}.draw_dot({},{},{},{},{})'.format(self.index,x,y,pageNum,saved,writeColor))
    
    def draw_line(self, headX, headY, tailX, tailY, pageNum, saved = 0, writeColor = 1):
        self.sio.emit("mfe-message", 'display{}.draw_line({},{},{},{},{},{},{})'.format(self.index,headX,headY,tailX,tailY,pageNum,saved,writeColor))
    
    def turn_to_page(self, page):
        self.sio.emit("mfe-message", 'display{}.turn_to_page({})'.format(self.index,page))
    
    def clear_page(self, page = 1):
        self.sio.emit("mfe-message", 'display{}.clear_page({})'.format(self.index,page))
    
    def clear_all_pages(self):
        self.sio.emit("mfe-message", 'display{}.clear_all_pages()'.format(self.index))
    
    def enable_page_turning(self):
        self.sio.emit("mfe-message", 'display{}.enable_page_turning()'.format(self.index))
    
    def disable_page_turning(self):
        self.sio.emit("mfe-message", 'display{}.disable_page_turning()'.format(self.index))
    
    def set_direction_regular(self):
        self.sio.emit("mfe-message", 'display{}.set_direction_regular()'.format(self.index))
    
    def set_direction_reverse(self):
        self.sio.emit("mfe-message", 'display{}.set_direction_reverse()'.format(self.index))
    
    def hide_scrollbar(self):
        self.sio.emit("mfe-message", 'display{}.hide_scrollbar()'.format(self.index))
    
    def show_scrollbar(self):
        self.sio.emit("mfe-message", 'display{}.show_scrollbar()'.format(self.index))
    
    def set_coordinate(self, row, column):
        self.sio.emit("mfe-message", 'display{}.set_coordinate({},{})'.format(self.index,row,column))
    
    def disable_auto_refresh(self):
        self.sio.emit("mfe-message", 'display{}.disable_auto_refresh()'.format(self.index))
    
    def enable_auto_refresh(self):
        self.sio.emit("mfe-message", 'display{}.enable_auto_refresh()'.format(self.index))
    
    def refresh(self):
        self.sio.emit("mfe-message", 'display{}.refresh()'.format(self.index))
    