Light status report:

	{"act": "light", "living": "on", "porch": "off", "bedroom": "on"}

Humidity and temperature:

	{"act": "humtem", "h": 65.6, "t": 23.1}

Door status report:

	{"act": "door", "st": "closed"}
	{"act": "door", "st": "open"}

Light control:

	{"act":"light_on", "name":"living", "freq":1, "dc":100}
	{"act":"light_on", "name":"bedroom", "freq":1, "dc":100}
	{"act":"light_on", "name":"porch", "freq":1, "dc":100}

	{"act":"light_off", "name":"living"}
	{"act":"light_off", "name":"bedroom"}
	{"act":"light_off", "name":"porch"}


Door control:

	{"act":"door_open"}

	{"act":"door_close"}

Media control:
	{"act":"media_play", "path":"http://www.example.com/test.mp3"}
	{"act":"media_play", "path":"/home/test.mp3"}

	{"act":"media_stop"}

	{"act":"media_pause"}

	{"act":"media_resume"}
