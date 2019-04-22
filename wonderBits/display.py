from .wbits import Wonderbits


class Display(Wonderbits):
    def __init__(self, index=1):
        Wonderbits.__init__(self)
        self.index = index

    def register_button(self, cb):
        self.register_event('display{}'.format(self.index), 'button', cb)

    def get_button_state(self):
        command = 'display{}.get_button_state()'.format(self.index)
        self.get_command(command)
        return self.r

    def print(self, row, column, text, size=2):
        command = 'display{}.print({},{},\"{}\",{})'.format(
            self.index, row, column, text, size)
        self.set_command(command)

    def draw_dot(self, x, y, pageNum, saved=0, writeColor=1):
        command = 'display{}.draw_dot({},{},{},{},{})'.format(
            self.index, x, y, pageNum, saved, writeColor)
        self.set_command(command)

    def draw_line(self, headX, headY, tailX, tailY, pageNum, saved=0, writeColor=1):
        command = 'display{}.draw_line({},{},{},{},{},{},{})'.format(
            self.index, headX, headY, tailX, tailY, pageNum, saved, writeColor)
        self.set_command(command)

    def turn_to_page(self, page):
        command = 'display{}.turn_to_page({})'.format(self.index, page)
        self.set_command(command)

    def clear_page(self, page=1):
        command = 'display{}.clear_page({})'.format(self.index, page)
        self.set_command(command)

    def clear_all_pages(self):
        command = 'display{}.clear_all_pages()'.format(self.index)
        self.set_command(command)

    def enable_page_turning(self):
        command = 'display{}.enable_page_turning()'.format(self.index)
        self.set_command(command)

    def disable_page_turning(self):
        command = 'display{}.disable_page_turning()'.format(self.index)
        self.set_command(command)

    def set_direction_regular(self):
        command = 'display{}.set_direction_regular()'.format(self.index)
        self.set_command(command)

    def set_direction_reverse(self):
        command = 'display{}.set_direction_reverse()'.format(self.index)
        self.set_command(command)

    def hide_scrollbar(self):
        command = 'display{}.hide_scrollbar()'.format(self.index)
        self.set_command(command)

    def show_scrollbar(self):
        command = 'display{}.show_scrollbar()'.format(self.index)
        self.set_command(command)

    def set_coordinate(self, row, column):
        command = 'display{}.set_coordinate({},{})'.format(
            self.index, row, column)
        self.set_command(command)

    def disable_auto_refresh(self):
        command = 'display{}.disable_auto_refresh()'.format(self.index)
        self.set_command(command)

    def enable_auto_refresh(self):
        command = 'display{}.enable_auto_refresh()'.format(self.index)
        self.set_command(command)

    def refresh(self):
        command = 'display{}.refresh()'.format(self.index)
        self.set_command(command)
