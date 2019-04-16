from .wonderbits import Wonderbits


class Led(Wonderbits):
    def __init__(self, index=1):
        Wonderbits.__init__(self)
        self.index = index

    def set_rgb(self, r, g, b):
        command = 'led{}.set_rgb({},{},{})'.format(self.index, r, g, b)
        self.set_command(command)

    def set_brightness(self, brightness):
        command = 'led{}.set_brightness({})'.format(self.index, brightness)
        self.set_command(command)

    def fade_to_rgb(self, r, g, b, total, step=50, key=False):
        command = 'led{}.fade_to_rgb({},{},{},{},{},{})'.format(
            self.index, r, g, b, total, step, key)
        self.set_command(command)
