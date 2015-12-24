from socketIO_client import SocketIO
import RPi.GPIO as GPIO
import logging
import time
import thread
import Adafruit_DHT as dht

logging.basicConfig(level=logging.INFO)

GPIO.setmode(GPIO.BCM)

PIN_LIVING = 4
PIN_PORCH = 17
PIN_FIREPLACE = 27

GPIO.setup(PIN_LIVING,GPIO.OUT)
GPIO.setup(PIN_PORCH,GPIO.OUT)
GPIO.setup(PIN_FIREPLACE,GPIO.OUT)

FREQ = 100 # frequency in Hz
FIRE_FREQ = 30 #  flickering effect

living = GPIO.PWM(PIN_LIVING, FREQ)
living.start(0)

porch = GPIO.PWM(PIN_PORCH, FREQ)
porch.start(0)

fire = GPIO.PWM(PIN_FIREPLACE, FIRE_FREQ)
fire.start(0)


def on_socket_connect_ack(args):
    print 'on_socket_connect_ack', args
    socketIO.emit('connect', {'appkey': '52fcc04c4dc903d66d6f8f92', 'customid': 'python_demo_local'})

def on_connack(args):
    print 'on_connack', args
    socketIO.emit('subscribe', {'topic': 'testtopic2'})

#    print "publish2_to_alias"
#    socketIO.emit('publish2_to_alias', {'alias': 'alias_mqttc_sub', 'msg': "hello to alias from publish2_to_alias"});

def on_puback(args):
    print 'on_puback', args
#    if args['messageId'] == '11833652203486491112':
#        print '  [OK] publish with given messageId'

def on_suback(args):
    print 'on_suback', args
#    socketIO.emit('publish', {'topic': 'testtopic2', 'msg': 'from python', 'qos': 1})

#    socketIO.emit('publish', {
#        'topic': 'testtopic2',
#        'msg': 'from python with given messageId',
#        'qos': 1,
#        'messageId': '11833652203486491112'
#        })

    socketIO.emit('publish2', {
        'topic': 't2thi',
        'msg': 'from publish2',
        "opts": {
            'qos': 1,
            'apn_json':  {"aps":{"sound":"bingbong.aiff","badge": 3, "alert":"douban"}},
            'messageId': '11833652203486491113'
        }
    })

    socketIO.emit('set_alias', {'alias': 'mytestalias1'})

def on_message(args):
    print 'on_message', args

def on_set_alias(args):
    print 'on_set_alias', args

    socketIO.emit('publish2', {
        'topic': 'testtopic2',
        'msg': 'from publish2',
        "opts": {
            'qos': 1,
            'apn_json':  {"aps":{"sound":"bingbong.aiff","badge": 3, "alert":"douban"}}
        }
    })


#    socketIO.emit('get_alias')
#    socketIO.emit('publish_to_alias', {'alias': 'mytestalias1', 'msg': "hello to alias"})
#    socketIO.emit('get_topic_list', {'alias': 'mytestalias1'})
#    socketIO.emit('get_state', {'alias': 'mytestalias1'})

def on_get_alias(args):
    print 'on_get_alias', args

def on_alias(args):
#    socketIO.emit('get_alias_list', {'topic': 'testtopic2'})
    print 'on_alias', args

def on_get_topic_list_ack(args):
    print 'on_get_topic_list_ack', args

def on_get_alias_list_ack(args):
    print 'on_get_alias_list_ack', args

def on_publish2_ack(args):
    print 'on_publish2_ack', args
#    if args['messageId'] == '11833652203486491113':
#        print '  [OK] publish2 with given messageId'

def on_publish2_recvack(args):
    print 'on_publish2_recvack', args

def on_get_state_ack(args):
    print 'on_get_state_ack', args

socketIO = SocketIO('sock.yunba.io', 3000)
socketIO.on('socketconnectack', on_socket_connect_ack)
socketIO.on('connack', on_connack)
socketIO.on('puback', on_puback)
socketIO.on('suback', on_suback)
socketIO.on('message', on_message)
socketIO.on('set_alias_ack', on_set_alias)
socketIO.on('get_topic_list_ack', on_get_topic_list_ack)
socketIO.on('get_alias_list_ack', on_get_alias_list_ack)
socketIO.on('puback', on_publish2_ack)
socketIO.on('recvack', on_publish2_recvack)
socketIO.on('get_state_ack', on_get_state_ack)
socketIO.on('alias', on_alias)                # get alias callback

socketIO.wait()

