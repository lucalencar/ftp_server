import ftplib
from ftplib import FTP
import os

clear = lambda: os.system('clear')

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

# Conectar ao servidor FTP
ftp = FTP()
ftp.connect(FTP_HOST, FTP_PORT)
ftp.login(FTP_USER, FTP_PASSWORD)


#Função menu para listar arquivos e diretórios / criar, deletar e mudar para algum diretório / voltar para diretório anterior 
def menu():
    while(True):
        print ('1. Listar arquivos e diretórios')
        print ('2. Criar novo diretório')
        print ('3. Deletar diretório')
        print ('4. Mudar para diretório')
        print ('5. Voltar para o diretório anterior')
        print ('6. Sair')
        print

        choice = int(input('> Digite uma opção: '))

        if choice == 1:
            clear()
            print ('Listar arquivos e diretórios: \n')            
            ftp.dir()
            
        elif choice == 2:
            clear()
            try:
                newdir = input('> Digite o nome do novo diretório: ')
                ftp.mkd(newdir)
                print('Diretório ', newdir, ' criado com sucesso!')
            except ftplib.all_errors as e:
                clear()
                print('Diretório já existe!')
        
        elif choice == 3:
            clear()
            try:
                deldir = input('> Digite o nome do diretório para remover: ')
                ftp.rmd(deldir)
                print('Diretório ', newdir, ' deletado com sucesso!')
            except ftplib.all_errors as e:
                clear()
                print('Diretório não existe!')        
        
        elif choice == 4:
            clear()
            try:
                mudar_dir = input('> Digite o nome do diretório: ')
                print(ftp.cwd(mudar_dir))
            except ftplib.all_errors as e:
                clear()
                print('Nome de diretório inválido!')
        
        elif choice == 5:
            clear()
            print(ftp.cwd('../'))
        
        elif choice == 6:
            print ('Saíndo do cliente\n')
            exit(0)
        
        else:
            clear()
            print ('Opção inválida! Digite uma das opções abaixo: \n')
            

menu()
