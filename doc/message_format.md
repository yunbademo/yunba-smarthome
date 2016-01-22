灯状态上报
--------

状态变化时上报，格式为`灯名:状态`，`on` 表示开，`off` 表示关：
```json
{"act": "light", "living": "on", "porch": "off", "bedroom": "on"}
```

温湿度上报
--------

周期性上报，`h` 表示相对湿度，`t` 表示温度：
```json
{"act": "humtem", "h": 65.6, "t": 23.1}
```

门状态上报
--------

状态变化时上报，`closed` 表示关，`open` 表示开：
```json
{"act": "door", "st": "closed"}
{"act": "door", "st": "open"}
```

音乐状态上报
--------

状态变化时上报，`st` 为当前音乐播放状态，有 3 种取值：`play` 正在播放，`stop` 停止状态，`pause` 暂停状态：
```json
{"act": "media", "st": "play"}
{"act": "media", "st": "stop"}
{"act": "media", "st": "pause"}
```

请求上报
--------

UI 可以向小屋发送这个消息，小屋收到后会上报前面列出的所有状态：
```json
{"act": "report_req"}
```

灯的控制
--------

开灯的3个参数分别是`灯名`，`频率`，`占空比`：
```json
{"act": "light_on", "name": "living", "freq": 1, "dc": 100}
{"act": "light_on", "name": "bedroom", "freq": 1, "dc": 100}
{"act": "light_on", "name": "porch", "freq": 1, "dc": 100}
```

关灯只需要一个参数`灯名`：
```json
{"act": "light_off", "name": "living"}
{"act": "light_off", "name": "bedroom"}
{"act": "light_off", "name": "porch"}
```

门的控制
------

开门和关门：
```json
{"act": "door_open"}
{"act": "door_close"}
```

音乐控制
--------

播放本地音乐，`path` 为音乐文件路径：
```json
{"act": "media_play", "path": "/home/test.mp3"}
```

播放网络音乐，`path` 为音乐文件 URL：
```json
{"act": "media_play", "path": "http://www.example.com/test.mp3"}
```

停止播放：
```json
{"act": "media_stop"}
```

暂停与恢复播放：
```json
{"act": "media_pause"}
{"act": "media_resume"}
```

增加与降低音量：
```json
{"act": "media_inc_vol"}
{"act": "media_dec_vol"}
```
