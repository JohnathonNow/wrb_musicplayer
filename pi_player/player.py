import socket
addr = ('johnwesthoff.com', 9990)
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    stream = sock.makefile('w+')
    while not stream.closed:
        #Request a song
        print('Asking for a song')
        stream.write('Gimme a song!\r\n')
        stream.flush()
        print('Request sent!')
        song = stream.readline()
        print('Response read!')
        print('Now playing {}'.format(song))
    
