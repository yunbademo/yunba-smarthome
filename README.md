这里简单介绍怎样让[云巴智能小屋][1]运行起来，doc目录下有以下详细文档：
[制作过程][2]
[元器件列表][3]
[消息格式][4]

运行
--------

下载代码并进入代码目录：
```bash
git clone git@github.com:yunbademo/yunba-smarthome.git
cd yunba-smarthome
```

然后安装第三方依赖库：
```bash
sudo chmod a+x setup_env.sh
sudo ./setup_env.sh
```
你需要在[云巴Portal][5]注册，并创建一个应用，这是免费的。然后修改配置文件config.py中的以下部分为你自己的参数：
```python
APPKEY = '563c4afef085fc471efdf803'
TOPIC = 'smart_home_topic'
ALIAS = 'pi_house'
CUSTOMID = 'pi_house'
```
其中**APPKEY**为你在[云巴Portal][5]上所建应用的AppKey；**TOPIC**为上报消息的topic，可以按自己需求定义；**ALIAS**为云巴小屋的别名，控制消息会像这个别名发送，可以按自己需求定义；**CUSTOMID**为用户ID，可以按自己需求定义（参考[云巴Socket.io API][6]）。

输入以下命令就可以完成运行了：
```bash
sudo python main.py
```

测试脚本
--------

测试脚本在test目录下，通过[云巴RESTful API][7]实现对小屋的控制，先进入test目录：
```bash
cd test
```
修改publish.sh里如下部分为你自己的参数：
```python
APPKEY="563c4afef085fc471efdf803"
ALIAS="pi_house"
SECKEY="sec-zxhrt0bbwTHkRBsj8b66VL1dbQ52IFKdkfnZzdI6Qli0zPIx"
```
其中**APPKEY**为你在[云巴Portal][5]所建应用的AppKey；**ALIAS**为云巴小屋的别名，**请与config.py中保持一致**；**SECKEY**为你在[云巴Portal][5]所建应用的Secret Key。然后就可以控制云巴小屋了：

开关门：
```bash
./door_open.sh
./door_close.sh
```

控制灯，开灯的三个参数分别为：灯名，频率，占空比(参考[制作过程][2])：
```bash
./light_on.sh living 60 100
./light_on.sh bedroom 60 100
./light_on.sh porch 60 100

./light_off.sh living
./light_off.sh bedroom
./light_off.sh porch
```

播放树莓派本地音乐(需要预先下载文件到相应路径)：
```bash
media_play.sh /home/pi/media/test.mp3
```
播放网络音乐：
```bash
media_play.sh http://www.example.com/test.mp3
```
停止播放
```bash
media_stop.sh
```

暂停播放与恢复播放：
```bash
media_pause.sh
media_resume.sh
```

增加音量与减低音量：
```bash
media_inc_vol.sh
media_dec_vol.sh
```

Web界面
--------
...

[1]: http://www.yunba.io
[2]: https://github.com/yunbademo/yunba-smarthome/blob/master/doc/how_to_make.md
[3]: https://github.com/yunbademo/yunba-smarthome/blob/master/doc/purchase_list.md
[4]: https://github.com/yunbademo/yunba-smarthome/blob/master/doc/message_format.md
[5]: http://yunba.io/
[6]: http://yunba.io/docs2/socket.io_API/
[7]: http://yunba.io/docs2/restful_Quick_Start/