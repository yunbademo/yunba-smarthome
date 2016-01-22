这里介绍怎样让 [云巴智能小屋][1] 运行起来，doc 目录下有以下详细文档：

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
你需要在 [云巴Portal][5] 注册，并创建一个应用，这是免费的。然后修改配置文件 config.py 中的以下部分为你自己的参数：
```python
APPKEY = '563c4afef085fc471efdf803'
TOPIC = 'smart_home_topic'
ALIAS = 'pi_house'
CUSTOMID = 'pi_house'
```
其`APPKEY`为你在 [云巴Portal][5] 上所建应用的 AppKey；`TOPIC`为上报消息的 Topic，可以按自己 需求定义；`ALIAS`为云巴小屋的别名，控制消息会像这个别名发送，可以按自己需求定义；`CUSTOMID`为用户 ID，可以按自己需求定义（参考[云巴Socket.io API][6]）。

输入以下命令就可以完成运行了：
```bash
sudo python main.py
```

测试脚本
--------

测试脚本在 test 目录下，通过 [云巴RESTful API][7] 实现对小屋的控制，先进入 test 目录：
```bash
cd test
```
修改 publish.sh 里如下部分为你自己的参数：
```python
APPKEY="563c4afef085fc471efdf803"
ALIAS="pi_house"
SECKEY="sec-zxhrt0bbwTHkRBsj8b66VL1dbQ52IFKdkfnZzdI6Qli0zPIx"
```
其中`APPKEY`为你在[云巴Portal][5]所建应用的 AppKey；`ALIAS`为云巴小屋的别名；**请与 config.py 中保持一致**；`SECKEY`为你在 [云巴Portal][5] 所建应用的 Secret Key。然后就可以控制云巴小屋了：

开关门：
```bash
./door_open.sh
./door_close.sh
```

控制灯，开灯的三个参数分别为：灯名，频率，占空比（参考 [制作过程][2]）：
```bash
./light_on.sh living 60 100
./light_on.sh bedroom 60 100
./light_on.sh porch 60 100

./light_off.sh living
./light_off.sh bedroom
./light_off.sh porch
```

播放本地音乐（需要预先下载文件到相应路径）：
```bash
./media_play.sh /home/pi/media/test.mp3
```

播放网络音乐：
```bash
./media_play.sh http://www.example.com/test.mp3
```

停止播放
```bash
./media_stop.sh
```

暂停与恢复播放：
```bash
./media_pause.sh
./media_resume.sh
```

增加与降低音量：
```bash
./media_inc_vol.sh
./media_dec_vol.sh
```

Web UI
--------

[Web UI][8] 是基于 [云巴JavaScript SDK][9] 开发的云巴智能小屋控制界面，需要修改 [web/js/main.js][10] 中以下部分为你自己的参数：
```js
var config = {
  APPKEY: '563c4afef085fc471efdf803',
  TOPIC: 'smart_home_topic',
  ALIAS: 'pi_house',
}
```

其中`APPKEY`为你在 [云巴Portal][5] 所建应用的AppKey；`TOPIC`为上报消息的Topic；`ALIAS`为云巴小屋的别名；**请与 config.py 中保持一致**。

然后将整个 web 目录放在你使用的 web 服务器（如 nginx）的可访问目录下，并解决js调用跨域问题（参考我们工程师的博客 [用nginx的反向代理机制解决前端跨域问题][11]），完成后通过浏览器访问 http://\<domain_or_ip\>/web/html/index.html（\<domain_or_ip\> 表示你的域名或 ip），并点击订阅按钮，就可以看到小屋上报的状态以及对小屋进行相关控制了。

[1]: http://www.tudou.com/programs/view/BYpGTDNi72E/
[2]: https://github.com/yunbademo/yunba-smarthome/blob/master/doc/how_to_make.md
[3]: https://github.com/yunbademo/yunba-smarthome/blob/master/doc/purchase_list.md
[4]: https://github.com/yunbademo/yunba-smarthome/blob/master/doc/message_format.md
[5]: http://yunba.io/
[6]: http://yunba.io/docs2/socket.io_API/
[7]: http://yunba.io/docs2/restful_Quick_Start/
[8]: https://github.com/yunbademo/yunba-smarthome/tree/master/web
[9]: http://yunba.io/docs2/Javascript_SDK/
[10]: https://github.com/yunbademo/yunba-smarthome/blob/master/web/js/main.js
[11]: http://www.cnblogs.com/gabrielchen/p/5066120.html
