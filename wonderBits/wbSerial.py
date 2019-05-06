import serial
import serial.tools.list_ports
import time
import threading
import os

class WBSerial(object):
    '''
    主要负责串口通信： 连接，收发串口数据，处理串口数据
    '''

    # 初始化标志
    _init_flag = False

    def __init__(self):
        # 初始化一些必要参数，出错时会重置这些参数
        self._initProperty()
        # 连接成功的回调函数
        self._connected_cb = None
        
        # 事件数据的回调函数
        self.event_data_cb = None
        # 带返回值数据命令的回调
        self.reporter_data_cb = None
        
        # 设置类命令的回调函数
        self._command_finish = None
        self.command_finish_cb = None

        # 是否开启控制台输出串口数据日志
        self._is_show_console = False

        # 开启一个子线程进行轮询串口
        # 若发现有我们的板子，就会尝试连接下
        # 如果板子有多块，第一块连不上的情况下会自动连接第二块，依次类推，直到连上我们的板子位置
        if not WBSerial._init_flag:
            threading.Thread(target=self._create_try_connect_py_serial_thread, args=('_create_try_connect_py_serial_thread',)).start()

        WBSerial._init_flag = True
    
    # 初始化该类的一些属性
    def _initProperty(self):
        self._ser = None
        self._canUsedPort = []
        self._initIndex = 0
        self._canUseCount = 0
        self._canSend = False
    
    # 发送命令给串口
    def write_command(self, command):
        try:
            cmd = '{}\r\n'.format(command).encode('gbk')
            while not self._canSend:
                time.sleep(.001)
            if self._canSend:
                self._ser.write(cmd)
        except KeyboardInterrupt as e:
            print('exit-wb')
            os._exit(0)

    # 处理串口数据
    def _handle_serial_data(self, r_str = ''):
        if r_str:
            if self._is_show_console:
                print(r_str, end="")
        else:
            return
        receive_str = r_str.strip()
        if receive_str.find('Type "help()" for more') != -1:
            self._canSend = True
            if self._connected_cb:
                self._connected_cb()
            return
        if receive_str.startswith("{") and receive_str.endswith('}'):
            # 返回事件数据
            if self.event_data_cb:
                threading.Thread(target=self._create_return_event_data_thread, args=('_create_return_event_data_thread',receive_str)).start()
                return
        
        if not receive_str.endswith(")") and receive_str.find('>>>') == -1:
            if self.reporter_data_cb:
                threading.Thread(target=self._create_return_serial_data_thread, args=('_create_return_serial_data_thread', receive_str)).start()

    # 创建一个子线程进行 事件通知回调
    def _create_return_event_data_thread(self,name, result):
        self.event_data_cb(result)

    # 创建一个子线程进行 获取值完毕回调
    def _create_return_serial_data_thread(self,name, value):
        self.reporter_data_cb(value)

    # 创建一个子线程进行 命令执行完毕回调
    def _create_return_command_finished_thread(self,name, key):
        self.command_finish_cb(key)

    # 创建一个子线程进行 监听串口数据(轮询)
    def _create_listen_serial_port_data_event_thread(self, name):
        _buffer = ''
        try:
            while True:
                oneByte = self._ser.read(1)
                _buffer += oneByte.decode("gbk")
                if oneByte == b"\n":
                    self._handle_serial_data(_buffer)
                    self._command_finish = _buffer
                    _buffer = ''
                if oneByte == b">" and _buffer[-3:] == '>>>':
                    self._handle_serial_data(_buffer)
                    _buffer = ''
                    if self._command_finish and self.command_finish_cb:
                        threading.Thread(target=self._create_return_command_finished_thread, args=('_create_return_command_finished_thread',self._command_finish)).start()
                        self._command_finish = None
                
        except KeyboardInterrupt as e:
            print('exit-wb')
            os._exit(0)

        except OSError as e:
            print('设备未配置')
            self._initProperty()

        except Exception as e:
            print("串口异常：{}".format(e))
            self._initProperty()

    # 初始化连接本地串口，获取串口信息
    def _initConnect(self):
        if self._ser != None:
            return
        self._initProperty()
        port_list = list(serial.tools.list_ports.comports())
        for i in range(len(port_list)):
            port = port_list[i]
            if port.pid == 29987 or port.pid == 60000:
                self._canUsedPort.append(port)
                # print(port.device, port.pid, port.vid, port.hwid)
                self._canUseCount = len(self._canUsedPort)

    # 根据指定端口，连接本地串口
    def _connect_serial(self, index=0):
        try:
            portx = self._canUsedPort[index].device
            bps = 115200
            timex = 1
            self._ser = serial.Serial(portx, bps, timeout=timex)
            cmd = '{}\r\n'.format("reset()").encode('gbk')
            self._ser.write(cmd)
        
            # 监听串口返回的数据
            threading.Thread(target=self._create_listen_serial_port_data_event_thread, args=('_create_listen_serial_port_data_event_thread',)).start()
            
        except serial.serialutil.SerialException as e:
            print("串口异常{}".format(e))
            if self._initIndex < self._canUseCount - 1:
                self._connect_serial(self._initIndex)
            else:
                self._initProperty()

        except Exception as e:
            print("通用异常：{}".format(e))
            self._initProperty()

    # 监听串口变化， 初始化或者连接
    def _create_try_connect_py_serial_thread(self, thread_name):
        try:
            while True:
                self._initConnect()
                if not self._canUseCount:
                    print('无可用串口')
                else:
                    if self._ser == None and self._canUseCount != 0:
                        self._connect_serial()
                time.sleep(.5)
        except KeyboardInterrupt as e:
            print('exit-wb')
            os._exit(0)