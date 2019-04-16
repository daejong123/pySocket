from .wonderbits import Wonderbits


class RfCommunication(Wonderbits):
    def __init__(self, index=1):
        Wonderbits.__init__(self)
        self.index = index

    def register_button(self, cb):
        self.register_event(
            'rfcommunication{}'.format(self.index), 'button', cb)

    def register_msg_received(self, cb):
        self.register_event('rfcommunication{}'.format(
            self.index), 'msg_received', cb)

    def get_msg(self):
        command = 'rfcommunication{}.get_msg()'.format(self.index)
        self.get_command(command)
        return self.r

    def clear_msg(self):
        command = 'rfcommunication{}.clear_msg()'.format(self.index)
        self.set_command(command)

    def get_unread_msg_count(self):
        command = 'rfcommunication{}.get_unread_msg_count()'.format(self.index)
        self.get_command(command)
        return self.r

    def read(self):
        command = 'rfcommunication{}.read()'.format(self.index)
        self.get_command(command)
        return self.r

    def send(self):
        command = 'rfcommunication{}.send()'.format(self.index)
        self.set_command(command)

    def init(self, name):
        command = 'rfcommunication{}.init({})'.format(self.index, name)
        self.set_command(command)

    def is_button_pressed(self):
        command = 'rfcommunication{}.is_button_pressed()'.format(self.index)
        self.get_command(command)
        return self.r
