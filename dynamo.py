from shutil import move, copy
from os import path, mkdir, getlogin
from time import sleep

print("-="*50)

#Obter o nome do projeto e fazer a verificação da existência do arquivo.
while True:
    nome_Projeto = str(input("Digite o nome do projeto: "))
    diretorio = (f"c:/Users/{getlogin()}/Documents/{nome_Projeto}")
    verificacao = path.exists(diretorio)
    if verificacao == True:
        print("Esse projeto já existe!")
    else:
        break

#Opção de adicionar o arquivo Readme
while True:
    readme_File = str(input("Deseja adicionar o arquivo Readme (yes/no): "))
    if readme_File != "yes" and readme_File != "no":
        print("Tente novamente!")
    else:
        break

#Diretorios
assets = str(f"{diretorio}/assets")
css_Dir = str(f"{diretorio}/assets/css")
javaS_Dir = str(f"{diretorio}/assets/js")

#Criação das pastas
mkdir(diretorio)
mkdir(assets)
mkdir(css_Dir)  
mkdir(javaS_Dir)

#Criação dos arquivos
if readme_File == "yes":
    with open("README.md", 'w') as readme:
        readme.write(f"# {nome_Projeto}")
    move("README.md", diretorio)

with open ("style.css", 'w') as css:
    pass

with open ("script.js", 'w') as js:
    pass

#Mover arquivos para o destino final.
move("style.css", css_Dir)
move("script.js", javaS_Dir)
copy("Executavel\index.html", diretorio)

print("-="*50)
print("Projeto criado com sucesso!")
print("-="*50)
sleep(5)
