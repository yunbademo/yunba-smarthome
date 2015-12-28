#!/usr/bin/env python

import time
import sys
import thread
from socketIO_client import SocketIO
import config

class Messenger:

    def __init__(self, message_callback):
        self.can_pub = False
        print('messenger init')
        self.message_callback = message_callback
        thread.start_new_thread(self.timer, ())

    def __del__(self):
        print('messenger del')

    def on_socket_connect_ack(self, args):
        print 'on_socket_connect_ack: ', args
        self.socketIO.emit('connect', {'appkey': config.APPKEY})

    def on_connack(self, args):
        print 'on_connack: ', args
        self.socketIO.emit('subscribe', {'topic': config.TOPIC})

    def on_puback(self, args):
        print 'on_puback: ', args

    def on_suback(self, args):
        print 'on_suback: ', args
        self.socketIO.emit('set_alias', {'alias': config.ALIAS})

    def on_message(self, args):
        print 'on_message: ', args
        if self.message_callback != None:
            self.message_callback(args)

    def on_set_alias(self, args):
        print 'on_set_alias: ', args

    def on_get_alias(self, args):
        print 'on_get_alias: ', args

    def on_alias(self, args):
        print 'on_alias: ', args

    def on_get_topic_list_ack(self, args):
        print 'on_get_topic_list_ack: ', args

    def on_get_alias_list_ack(self, args):
        print 'on_get_alias_list_ack: ', args

    def on_publish2_ack(self, args):
        print 'on_publish2_ack: ', args

    def on_publish2_recvack(self, args):
        print 'on_publish2_recvack: ', args

    def on_get_state_ack(self, args):
        print 'on_get_state_ack: ', args

    def timer(self):
        self.socketIO = SocketIO('sock.yunba.io', 3000)

        self.socketIO.on('socketconnectack', self.on_socket_connect_ack)
        self.socketIO.on('connack', self.on_connack)
        self.socketIO.on('puback', self.on_puback)
        self.socketIO.on('suback', self.on_suback)
        self.socketIO.on('message', self.on_message)
        self.socketIO.on('set_alias_ack', self.on_set_alias)
        self.socketIO.on('get_topic_list_ack', self.on_get_topic_list_ack)
        self.socketIO.on('get_alias_list_ack', self.on_get_alias_list_ack)
#        self.socketIO.on('puback', self.on_publish2_ack)
        self.socketIO.on('recvack', self.on_publish2_recvack)
        self.socketIO.on('get_state_ack', self.on_get_state_ack)
        self.socketIO.on('alias', self.on_alias)
        self.can_pub = True
        self.socketIO.wait()

    def publish(self, msg, qos):
        if self.can_pub == True:
            self.socketIO.emit('publish', {'topic': config.TOPIC, 'msg': msg, 'qos': qos})

if __name__ == '__main__':
    msg = Messenger(None)
    while True:
        time.sleep(1)

