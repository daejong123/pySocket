## python-sdk

**[豌豆拼api文档链接](http://doc.wonderbits.cn/)**

> 主要服务于豌豆拼硬件产品
>
> 需要搭配豌豆拼硬件模块使用
>
> **Powered by MFEducation**

1. 包含各个模块的api
    * 显示模块
    * 控制模块
    * 彩灯模块
    * 射频通信模块
    * 等等

2. sdk中包含串口通信功能
    * 插上硬件模块可以直接通信


### 简单示例
> 创建一个py文件 demo.py

```python
# 导入需要的模块
from wonderbits import Display, Led, Control
import random
import time

# 创建必要的模块对象
display1 = Display()
led = Led()
control1 = Control()

# 豌豆拼硬件复位等待时间，后期会优化
time.sleep(8)

# 定义一个全局变量
content = 1
while True:
    # 在显示模块上第一行第一列显示变量content
    display1.print(1, 1, content)
    content = content + 1
    # 设置彩灯模块颜色， 颜色随机
    led.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # 获取控制模块sw4开关状态值
    sw4 = control1.get_sw4()
    print('我收到sw4状态{}'.format(sw4))
    # 获取开关sw3的位置
    isAtOne = control1.is_sw3_at_1()
    print('我收到sw在1位置{}'.format(isAtOne))
```

### 运行py文件
```python
运行环境：需要python -V 为3版本
运行：
python demo.py
```
