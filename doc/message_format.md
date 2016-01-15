灯状态上报
--------

状态变化时上报，格式为*灯名:状态*，*on*表示开，*off*表示关：
```
{"act": "light", "living": "on", "porch": "off", "bedroom": "on"}
```

温湿度上报
--------

周期性上报：
```
{"act": "humtem", "h": 65.6, "t": 23.1}
```

门状态上报
--------

状态变化时上报，*closed*表示关，*open*表示开：
```
{"act": "door", "st": "closed"}
{"act": "door", "st": "open"}
```

音乐状态上报
--------

状态变化时上报，*st*为当前音乐播放状态，有3种取值：*play*正在播放，*stop*停止状态，*pause*暂停状态：
{"act": "media", "st": "play"}
{"act": "media", "st": "stop"}
{"act": "media", "st": "pause"}

请求上报
--------

UI可以向小屋发送这个消息，小屋收到后会上报前面列出的所有状态：
```
{"act": "report_req"}
```

灯的控制
--------

开灯的3个参数分别是*灯名*，*频率*，*占空比*：
```
{"act": "light_on", "name": "living", "freq": 1, "dc": 100}
{"act": "light_on", "name": "bedroom", "freq": 1, "dc": 100}
{"act": "light_on", "name": "porch", "freq": 1, "dc": 100}
```

关灯只需要一个参数*灯名*：
```
{"act": "light_off", "name": "living"}
{"act": "light_off", "name": "bedroom"}
{"act": "light_off", "name": "porch"}
```

门的控制
------

开门和关门：
```
{"act": "door_open"}
{"act": "door_close"}
```

音乐控制
--------

播放本地音乐，*path*为音乐文件路径：
```
{"act": "media_play", "path": "/home/test.mp3"}
```

播放网络音乐，*path*为音乐文件URL：
```
{"act": "media_play", "path": "http://www.example.com/test.mp3"}
```

停止播放：
```
{"act": "media_stop"}
```

暂停与恢复播放：
```
{"act": "media_pause"}
{"act": "media_resume"}
```

增加与降低音量：
```
{"act": "media_inc_vol"}
{"act": "media_dec_vol"}
```
