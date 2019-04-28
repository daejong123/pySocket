import serial
import serial.tools.list_ports
import time
import threading

class WBSerial(object):

    init_flag = False
    def __init__(self):
        self._initProperty()
        self._connectedCb = None
        self._waitToSendMsg = []
        self.eventDataCb = None
        self.reporterDataCb = None
        # 开启一个子线程进行轮询串口
        # 若发现有我们的板子，就会尝试连接下
        # 如果板子有多块，第一块连不上的情况下会自动连接第二块，依次类推，直到连上我们的板子位置
        if not WBSerial.init_flag:
            threading.Thread(target=self._start, args=('detechSerailThread',)).start()

        WBSerial.init_flag = True
    
    def _initProperty(self):
        self._ser = None
        self._canUsedPort = []
        self._initIndex = 0
        self._canUseCount = 0
        self._canSend = False
    
    def _sendCmdFromQuene(self):
        for i in range(len(self._waitToSendMsg)):
            self._ser.write(self._waitToSendMsg[i])
        self._waitToSendMsg = []

    def connectedCallBack(self, cb):
        self._connectedCb= cb

    def writeCommand(self, command):
        cmd = '{}\r\n'.format(command).encode('gbk')
        if self._canSend:
            # print('发送命令', command)
            self._ser.write(cmd)
        else:
            self._waitToSendMsg.append(cmd)

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

    def createThreadEvent(self,name, result):
        self.eventDataCb(result)

    def createThreadData(self,name, key, value):
        self.reporterDataCb(key, value)

    def _doListenPort(self, name):
        receiveKey = None
        receiveVal = None
        try:
            while True:
                time.sleep(.005)
                receiveStr = self._ser.readline().decode("gbk")
                if receiveStr:
                    print("收到{}".format(receiveStr), end="")
                    pass
                else:
                    continue
                if receiveStr.find('Type "help()" for more') != -1:
                    self._canSend = True
                    self._sendCmdFromQuene()
                    if self._connectedCb:
                        self._connectedCb()
                    continue
                    
                if not self._canSend:
                    continue

                if receiveStr.startswith(">>> {") or receiveStr.startswith("{"):
                    result = receiveStr;
                    if receiveStr.startswith(">>> {"):
                        length = len(">>>")
                        result = receiveStr[length:]
                    # 返回事件数据
                    if self.eventDataCb:
                        threading.Thread(target=self.createThreadEvent, args=('createThreadEvent',result)).start()
                    continue

                    
                if receiveStr.startswith(">>>"):
                    receiveKey = receiveStr[3:].strip()
                    if not receiveKey:
                        receiveKey = None
                else:
                    receiveVal = receiveStr.strip()
                    if receiveKey and receiveVal:
                        if self.reporterDataCb:
                            threading.Thread(target=self.createThreadData, args=('createThreadData',receiveKey, receiveVal)).start()
                        receiveKey = None
                        receiveVal = None
                    # 当收到不是以>>>开头的内容时，会检查此时的key是否为None，若为None，则把该条>>>开头的数据作为 key，而不是作为 value。
                    if receiveKey == None:
                        receiveKey = receiveVal
                            
        except OSError as e:
            print('设备未配置')
            self._initProperty()

        except Exception as e:
            print("ser通用异常：{}".format(e))
            self._initProperty()

    def _connectSerial(self, index=0):
        if self._ser != None or self._canUseCount == 0:
            return
        try:
            portx = self._canUsedPort[index].device
            bps = 115200
            timex = 1
            self._ser = serial.Serial(portx, bps, timeout=timex)
            cmd = '{}\r\n'.format("reset()").encode('gbk')
            self._ser.write(cmd)
            # 监听串口返回的数据
            threading.Thread(target=self._doListenPort, args=('_doListenPort',)).start()
            
        except serial.serialutil.SerialException as e:
            print("串口异常{}".format(e))
            if self._initIndex < self._canUseCount - 1:
                self._connectSerial(self._initIndex)
            else:
                self._initProperty()

        except Exception as e:
            print("通用异常：{}".format(e))
            self._initProperty()


    def _start(self, threadName):
        while True:
            self._initConnect()
            if not self._canUseCount:
                print('无可用串口')
            else:
                self._connectSerial()
            time.sleep(.5)