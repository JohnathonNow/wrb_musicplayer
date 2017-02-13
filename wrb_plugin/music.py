from Queue import Queue
import socket
import thread
MAX_ATTEMPTS = 5

def music(SENDER,MESSAGE,CMD,send):
    '''Usage:   !music URL

        Plays a YouTube video pointed to by 
        URL through the bluetooth speakers.'''
    MESSAGE = MESSAGE.replace(CMD, '')
    music_queue.put(MESSAGE)
    send.send('{} told me to play {}.'.format(SENDER, MESSAGE))
    
music_queue = Queue()
COMMANDS = {'!music': music}
HANDLERS = {}
listen()

#create a server for the pi to connect to
def listen(port=9990):
    sock = None
    failures = 0
    while sock == None and failures < MAX_ATTEMPTS:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
        except:
            sock = None
            failures = failures + 1
    if sock != None:
        print("Music Server Connected!")
        try:
            sock.listen(0) 
            while True:
                client, address = sock.accept()
                thread.start_new_thread(handle, (client, ))
        except KeyboardInterrupt:
            sock.close()
            raise
    else:
        print("Music Server could not listen!")

def handle(client):
    stream = client.makefile('w+')
    stream.readline()
    stream.write(music_queue.get())
    stream.write('\n')
    stream.flush()
    stream.close()

thread.start_new_thread(listen, ())
