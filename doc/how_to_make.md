简介
--------

云巴智能小屋是利用云巴实时消息服务构建智能家居的一个小案例，小屋安装了一个自动门，三个灯，一个温湿度传感器，一个门磁，一个小音箱。一个树莓派2开发板通过GPIO与这些小器件连接，控制他们并获取他们的状态（参考[元器件列表][1]）。通过云巴实时消息服务，我们就可以远程实时控制小屋的各种设备了。观看[云巴智能小屋视频][2]了解更多。

系统安装
--------

安装Raspian，请参考[官方安装文档][3]。
第三方依赖请参考[setup_env.sh][4]，也可以直接运行这个脚本来安装。我们使用[raspberry-gpio-python][5]来进行GPIO操作，但Raspian系统自带了这个库不需要再安装。

集成云巴服务
--------

我们使用[云巴Socket.io API][6]，使用非常简单，只需少量代码就可以使用云巴服务了。参考[messenger.py][7]。

木屋模型
--------

参考包装内自带的图纸即可完成安装，需要胶水粘贴的地方，可以用包装内自带的白胶。也可以用[元器件列表][1]中的环氧树脂强力AB胶，AB胶需要在粘贴处混合A管和B管的胶水。需要注意的是白胶和AB胶水都需要一段时间才能变干牢固，牢固之前需要固定。

LED灯
--------

我们用3个LED分别模拟客厅灯（living），卧室灯（bedroom），廊灯（porch），每个灯需要串联一个10欧姆的限流电阻，灯的负极接树莓派2开发板的GND，正极分别接GPIO4，GPIO17，GPIO27，当然也可以接其他GPIO（参考[树莓派2引脚编号][8]），这样的话你需要修改[config.py][9]中如下部分，**注意：LED灯的正负极不能接反，否则可能会烧掉LED。**
```python
LED_LIVING = 4
LED_BEDROOM = 17
LED_PORCH = 27
```

我们使用python库[raspberry-gpio-python][10]来控制灯。具体使用请参考其文档，以及小屋的灯控制代码[led.py][11]。

自动门
--------

首先把门和小合页通过AB胶合牢固，然后再把合页的另一边粘在门框上，使门可以活动，正如你在视频中看到的那样，我们使用步进电机的转动来开关门，步进电机通过一个小曲柄与门连接。

对于电路，步进电机首先与其驱动板连接，驱动板的正负分别接树莓派2开发板的5V和GND，驱动板的IN1~IN4引脚分别接树莓派2开发板的GPIO26，GPIO19，GPIO13，GPIO6，当然也可以接其他GPIO（参考[树莓派2引脚编号][8]），这样的话你需要修改[config.py][9]中如下部分：
```python
STEP_MOTOR_IN1 = 26
STEP_MOTOR_IN2 = 19
STEP_MOTOR_IN3 = 13
STEP_MOTOR_IN4 = 6
```

同LED灯一样，也是使用python库[raspberry-gpio-python][10]来控制步进电机。参考控制步进电机的代码[stepper_motor.py][12]。

门磁
--------

门磁主要用来知道门的开关状态，由一个磁控开关和一个小磁铁组成（参考[元器件列表][1]），我们把磁控开关装在门框上，小磁铁装在门上，当磁铁靠近磁控开关时，开关接通，其输出端（DO）输出低电平，通过读取其输出端电平就可以知道门的开关状态。

磁控开关的VCC和地分别接树莓派2开发板的5V和GND，DO接GPIO10，当然也可以接其他GPIO并修改[config.py][9]中如下部分：
```python
MAGNET_SWITCH = 10
```

同LED灯一样，也是使用python库[raspberry-gpio-python][10]来读取磁控开关状态。参考读取磁控开关状态的代码[stepper_motor.py][13]。

温湿度传感器
--------

温湿度传感器用于获取小屋内的温湿度，使用的是DHT22数字温湿度传感器（参考[元器件列表][1]）。

连接方式参考[adafruit][14]，简单的说就是：我们面对有很多孔的一面，那么从左边算起，第一个引脚为VCC，接树莓派2开发板的3.3V，第二个为数据引脚，接树莓派2开发板的GPIO22，当然也可以接其他GPIO并修改[config.py][9]中如下部分，第三引脚悬空，第四引脚接树莓派2开发板GND。
```python
DHT22_GPIO_NUM = 22
```

使用Adafruit提供的python库[Adafruit_Python_DHT][15]来读取温湿度，我们在[setup_env.sh][4]中已经安装了这个库，具体使用代码参考[dht.py][16]。

音乐播放
------

在树莓派2开发板的A/V接口上接一个小音箱（参考[元器件列表][1]）来实现音乐播放。通过调用并控制[mplayer][17]来播放音乐，参考代码[player.py][18]。


[1]: https://github.com/yunbademo/yunba-smarthome/blob/master/doc/purchase_list.md
[2]: http://www.tudou.com/programs/view/BYpGTDNi72E/
[3]: https://www.raspberrypi.org/documentation/installation/installing-images/README.md
[4]: https://github.com/yunbademo/yunba-smarthome/blob/master/setup_env.sh
[5]: http://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
[6]: http://yunba.io/docs2/socket.io_API/
[7]: https://github.com/yunbademo/yunba-smarthome/blob/master/messenger.py
[8]: https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/
[9]: https://github.com/yunbademo/yunba-smarthome/blob/master/config.py
[10]: http://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/
[11]: https://github.com/yunbademo/yunba-smarthome/blob/master/led.py
[12]: https://github.com/yunbademo/yunba-smarthome/blob/master/stepper_motor.py
[13]: https://github.com/yunbademo/yunba-smarthome/blob/master/magnet_sw.py
[14]: https://www.adafruit.com/products/385
[15]: https://github.com/adafruit/Adafruit_Python_DHT
[16]: https://github.com/yunbademo/yunba-smarthome/blob/master/dht.py
[17]: http://www.mplayerhq.hu/
[18]: https://github.com/yunbademo/yunba-smarthome/blob/master/player.py
