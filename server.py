import socket
from googletrans import Translator

translator = Translator()
server_lang = 'en'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1337))
server.listen()

client, addr = server.accept()