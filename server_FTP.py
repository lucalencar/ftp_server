#Utilizando a biblioteca de servidor FTP do python
#A classe DummyAuthorizer verifica  usuários, senhas e permissões dos diretórios listados
from pyftpdlib.authorizers import DummyAuthorizer
#FTPHandler é a classe que implementa o protocolo FTP que vai possibilitar o cliente à se comunicar com o servidor
from pyftpdlib.handlers import FTPHandler
#A classe FTPServer é responsável por criar o socket 'listening' no endereço especificado(host, port). 
from pyftpdlib.servers import FTPServer

#Host para o servidor FTP, no caso localhost. 
FTP_HOST = "127.0.0.1"

#Porta para conexão do servidor FTP. precisa ser maior que 1023 para que não necessite rodar o script ftpserver.py como ROOT
FTP_PORT = 2121

#nome do usuário para conectar ao servidor ftp
FTP_USER = "cinerum"

#senha do usuário para conectar ao servidor ftp
FTP_PASSWORD = "12345"

#diretório padrão que o usuário terá acesso no servidor FTP
FTP_DIRETORIO = "/home/cinerum/"


#Primeira classe à instanciar, responsável por lidar com autenticações e permissões dos usuários virtuais do servidor FTP. 
authorizer = DummyAuthorizer()

#Depois de instanciar o authorizer, definimos um novo usuário com permissões de read/write
authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRETORIO, perm="elradfmw")
authorizer.add_anonymous(FTP_DIRETORIO)

handler = FTPHandler
handler.authorizer = authorizer

#Inicia o servidor FTP
server = FTPServer((FTP_HOST, FTP_PORT), handler)
server.serve_forever()
