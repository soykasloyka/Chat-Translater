import socket

lang = input('Please enter your language:')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1337))

while True:
    message = input('Input your message:')

    if message == '!q':
        client.close()
        break
    else:
        client.send(f'[{lang}]{message}'.encode())