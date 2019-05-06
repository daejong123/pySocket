from .wbits import Wonderbits



class Display(Wonderbits):
    '''
    显示模块
    '''
    def __init__(self, index = 1):
        Wonderbits.__init__(self)
        self.index = index

    def register_button(self, cb):
        self._register_event('display{}'.format(self.index), 'button', cb)
    
    def print(self, row, column, text, size = 2):
        """固定位置显示 """
        text = str(text).replace('"', '\\"')
        command = 'display{}.print({},{},"{}",{})'.format(self.index,row,column,text,size)
        self._set_command(command)
    
    def draw_dot(self, x, y, page, save = 0, color = 1):
        """画点 """
        command = 'display{}.draw_dot({},{},{},{},{})'.format(self.index,x,y,page,save,color)
        self._set_command(command)
    
    def draw_line(self, head_x, head_y, tail_x, tail_y, page, save = 0, color = 1):
        """画线 """
        command = 'display{}.draw_line({},{},{},{},{},{},{})'.format(self.index,head_x,head_y,tail_x,tail_y,page,save,color)
        self._set_command(command)
    
    def turn_to_page(self, page):
        """转到某页 """
        command = 'display{}.turn_to_page({})'.format(self.index,page)
        self._set_command(command)
    
    def clear_page(self, page):
        """清除某页 """
        command = 'display{}.clear_page({})'.format(self.index,page)
        self._set_command(command)
    
    def clear_all_pages(self):
        """清除全部8页屏幕的内容 """
        command = 'display{}.clear_all_pages()'.format(self.index)
        self._set_command(command)
    
    def get_button_state(self):
        """该函数用于获取翻页按钮状态 """
        command = 'display{}.get_button_state()'.format(self.index)
        self._get_command(command)
        return self._result
    
    def disable_page_turning(self):
        """禁止翻页按键功能,在开启翻页按键功能的情况下使用该函数可以禁止翻页按键功能，禁止翻页按键功能后将不能通过翻页按键来切换不同页码的显示内容，只能使用turn_to_page函数来切换页码,系统默认开启翻页按键功能 """
        command = 'display{}.disable_page_turning()'.format(self.index)
        self._set_command(command)
    
    def enable_page_turning(self):
        """开启翻页按键功能,在禁止翻页按键功能的情况下使用该函数可以开启翻页按键功能,系统默认开启翻页按键功能 """
        command = 'display{}.enable_page_turning()'.format(self.index)
        self._set_command(command)
    
    def set_direction_reverse(self):
        """设置显示方向为翻转显示方向，使用该函数后显示内容将会进行180°翻转 """
        command = 'display{}.set_direction_reverse()'.format(self.index)
        self._set_command(command)
    
    def set_direction_regular(self):
        """设置显示方向为系统默认显示方向 """
        command = 'display{}.set_direction_regular()'.format(self.index)
        self._set_command(command)
    
    def hide_scrollbar(self):
        """隐藏页码滚动指示条，使用该函数后将不会再显示内容界面看到页码滚动指示条,系统默认显示页码滚动指示条 """
        command = 'display{}.hide_scrollbar()'.format(self.index)
        self._set_command(command)
    
    def show_scrollbar(self):
        """显示页码滚动指示条,系统默认显示页码滚动指示条 """
        command = 'display{}.show_scrollbar()'.format(self.index)
        self._set_command(command)
    
    def disable_auto_refresh(self):
        """禁止自动刷新显示功能,在禁止自动刷新显示功能后只能靠手动刷新显示界面实现更新显示内容,系统默认开启自动刷新显示功能 """
        command = 'display{}.disable_auto_refresh()'.format(self.index)
        self._set_command(command)
    
    def enable_auto_refresh(self):
        """开启自动刷新显示功能,在开启自动刷新显示功能后系统将智能识别当前显示内容是否需要更新，如果需要则会更新显示内容,系统默认开启自动刷新显示功能 """
        command = 'display{}.enable_auto_refresh()'.format(self.index)
        self._set_command(command)
    
    def refresh(self):
        """更新显示内容,在禁止自动刷新显示功能后只能靠该函数来实现手动刷新显示界面实现更新显示内容,系统默认开启自动刷新显示功能 """
        command = 'display{}.refresh()'.format(self.index)
        self._set_command(command)
    