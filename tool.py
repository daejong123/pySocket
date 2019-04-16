from wonderBits import Display
import os
import time

display1 = Display(1)

sep = os.sep
directory = os.path.dirname(os.path.realpath(__file__))
readfileName = 'upload.py'
writeFileName = 'runLoop.py'

essentialImport = 'from sysCfg import * \n'

with open('{}{}{}'.format(directory, sep, readfileName), 'r') as f:
    lines = f.readlines();
    print(lines)
    display1._send_msg('with open(\'runLoop.py\', \'wb\') as w:')
    display1._send_msg('w.write(\'from sysCfg import * \\n\')')
    display1._send_msg('for i in range(len(lines)):')
    display1._send_msg('w.write(lines[i])')

#     with open('{}{}{}'.format(directory, sep, writeFileName), 'wb') as w:
#         w.write(essentialImport)
#         for i in range(len(lines)):
#             w.write(lines[i])
