#!/usr/bin/python2
import socket
import os
import subprocess
addr = ('johnwesthoff.com', 9990)
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    stream = sock.makefile('w+')
    #Request a song
    print('Asking for a song')
    stream.write('Gimme a song!\r\n')
    stream.flush()
    print('Request sent!')
    song = stream.readline()
    sock.close();
    print('Response read!')
    print('Now playing {}'.format(song))
    process = subprocess.Popen('mpsyt', shell=True, stdin=subprocess.PIPE)
    process.communicate('set player mpv\nplayurl {}\nq\n'.format(song))
    process.wait()
