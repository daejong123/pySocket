import serial
import serial.tools.list_ports
import time
import threading

class WBSerial(object):

    # 初始化标志
    _init_flag = False

    def __init__(self):
        self._initProperty()
        self._connected_cb = None
        self._wait_to_send_msg_list = []
        
        self.event_data_cb = None
        self.reporter_data_cb = None
        # 开启一个子线程进行轮询串口
        # 若发现有我们的板子，就会尝试连接下
        # 如果板子有多块，第一块连不上的情况下会自动连接第二块，依次类推，直到连上我们的板子位置
        if not WBSerial._init_flag:
            threading.Thread(target=self._create_try_connect_py_serial_thread, args=('_create_try_connect_py_serial_thread',)).start()

        WBSerial._init_flag = True
    
    # 初始化属性
    def _initProperty(self):
        self._ser = None
        self._canUsedPort = []
        self._initIndex = 0
        self._canUseCount = 0
        self._canSend = False
    
    # 发送队列中的指令
    def _send_cmd_from_quene(self):
        for i in range(len(self._wait_to_send_msg_list)):
            self._ser.write(self._wait_to_send_msg_list[i])
        self._wait_to_send_msg_list = []

    def write_command(self, command):
        cmd = '{}\r\n'.format(command).encode('gbk')
        if self._canSend:
            # print('发送命令', command)
            self._ser.write(cmd)
        else:
            self._wait_to_send_msg_list.append(cmd)

    # 创建一个子线程进行 事件通知回调
    def _create_return_event_data_thread(self,name, result):
        self.event_data_cb(result)

    # 创建一个子线程进行 返回值回调
    def _create_return_serial_data_thread(self,name, key, value):
        self.reporter_data_cb(key, value)

    # 创建一个子线程进行 监听串口数据(轮询)
    def _create_listen_serial_port_data_event_thread(self, name):
        receive_key = None
        receive_val = None
        receive_str = ""
        try:
            while True:
                time.sleep(.005)
                receive_str = self._ser.readline().decode("gbk")
                if receive_str:
                    print("{}".format(receive_str), end="")
                    pass
                else:
                    continue
                if receive_str.find('Type "help()" for more') != -1:
                    self._canSend = True
                    self._send_cmd_from_quene()
                    if self._connected_cb:
                        self._connected_cb()
                    continue

                if not self._canSend:
                    continue

                if receive_str.startswith(">>> {") or receive_str.startswith("{"):
                    result = receive_str;
                    if receive_str.startswith(">>> {"):
                        length = len(">>>")
                        result = receive_str[length:]
                    # 返回事件数据
                    if self.event_data_cb:
                        threading.Thread(target=self._create_return_event_data_thread, args=('_create_return_event_data_thread',result)).start()
                    continue

                    
                if receive_str.startswith(">>>"):
                    receive_key = receive_str[3:].strip()
                    if not receive_key:
                        receive_key = None
                else:
                    receive_val = receive_str.strip()
                    if receive_key and receive_val:
                        if self.reporter_data_cb:
                            threading.Thread(target=self._create_return_serial_data_thread, args=('_create_return_serial_data_thread',receive_key, receive_val)).start()
                        receive_key = None
                        receive_val = None
                    # 当收到不是以>>>开头的内容时，会检查此时的key是否为None，若为None，则把该条>>>开头的数据作为 key，而不是作为 value。
                    if receive_key == None and receive_val:
                        if receive_val.endswith("()") != -1:
                            receive_key = receive_val
                            
        except OSError as e:
            print('设备未配置')
            self._initProperty()

        except Exception as e:
            print("ser通用异常：{}".format(e))
            self._initProperty()

    # 初始化连接本地串口
    def _initConnect(self):
        if self._ser != None:
            return
        self._initProperty()
        port_list = list(serial.tools.list_ports.comports())
        for i in range(len(port_list)):
            port = port_list[i]
            if port.pid == 29987 or port.pid == 60000:
                self._canUsedPort.append(port)
                print(port.device, port.pid, port.vid, port.hwid)
                self._canUseCount = len(self._canUsedPort)

    # 连接本地串口
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

    # 创建一个子线程
    def _create_try_connect_py_serial_thread(self, thread_name):
        while True:
            self._initConnect()
            if not self._canUseCount:
                print('无可用串口')
            else:
                if self._ser == None and self._canUseCount != 0:
                    self._connect_serial()
            time.sleep(.5)
