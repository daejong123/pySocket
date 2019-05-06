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
from wonderbits import Display, Control, Led
import time
import random

# 初始化模块
d1 = Display()
c1 = Control()
l1 = Led()

# 隐藏控制台输出 （默认方式为关闭， 任一个豌豆拼模块的实例调用 hide_console() 方法）
# c1.hide_console()

# 开启控制台输出 (任一个豌豆拼模块的实例，如c1.show_console())
d1.show_console()

# 显示模块显示内容
d1.print(2, 1, 'value:')

# 计数变量
content = 1

for i in range(10):
    # 获取控制模块开关sw4的值
    sw4 = c1.get_sw4()
    # 在显示屏上显示sw4的值
    d1.print(2, 7, sw4)
    # 设置彩灯rgb随机颜色
    l1.set_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 显示模块显示计数值 
    d1.print(1, 1, content)
    # 将计数变量 递增1
    content += 1

```

### 运行py文件
```python
运行环境：需要python -V 为3版本
运行：
python demo.py
```
