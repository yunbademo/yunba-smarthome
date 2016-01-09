#!/usr/bin/env python

import os
import time
import sys
import subprocess
import RPi.GPIO as GPIO

#mplayer -loop 0 PATH

class Player:

    def __init__(self):
        print('player init')
        self.p = None
        self.status = 'stop'

    def __del__(self):
        print('player del')

    def play(self, path):
        if self.status != 'stop':
            self.stop()

        dev_null = open(os.devnull, 'w')
        args = ['/usr/bin/mplayer', '-loop', '0', path]

#        self.p = subprocess.Popen(args, stdin=subprocess.PIPE)
        self.p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=dev_null, stderr=dev_null)
        self.status = 'play'

    def stop(self):
        if self.status == 'stop':
            return

        #self.p.communicate('q')
        self.p.stdin.write('q')

        self.status = 'stop'

    def pause(self):
        if self.status != 'play':
            return

        self.p.stdin.write('p')

        self.status = 'pause'

    def resume(self):
        if self.status != 'pause':
            return

        self.p.stdin.write('p')

        self.status = 'play'

if __name__ == '__main__':
    player = Player()
    TEST_URL = 'http://sc.111ttt.com/up/mp3/11219/2A78B09675979C6093C58E3E39740FC8.mp3'
    TEST_LOCAL = '/home/pi/music/test.mp3'
    sleep = 5

    print('play url')
    player.play(TEST_URL)

    time.sleep(sleep)
    print('play local')
    player.play(TEST_LOCAL)

    time.sleep(sleep)
    print('pause')
    player.pause()

    time.sleep(sleep)
    print('resume')
    player.resume()

    time.sleep(sleep)
    print('stop')
    player.stop()

