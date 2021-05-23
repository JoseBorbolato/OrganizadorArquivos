import os

# caminho absoluto da pasta
PATH = os.path.abspath('.')
print(PATH)

# caminho absoluto da pasta com o nome do arquivo
PATH = os.path.abspath(__file__)
print(PATH)

# Dirname --> Pega o caminho da pasta "PAI". ou seja, da pasta anterior
PATH = os.path.dirname(os.path.abspath('.'))
print(PATH)

# Nesse caso, o caminho absoluto contém o nome de um arquivo, então o DIRNAME retorna o diretório corrente do arquivo
PATH = os.path.dirname(os.path.abspath(__file__))
print(PATH)

# listar arquivos de um diretório
print(os.listdir())

# criar novo diretório
#os.mkdir('Nome da pasta')

# Unindo diretórios
PATH = os.path.join(PATH, 'Nome da pasta')
print(PATH)


PATH = os.path.dirname(PATH)
print(PATH)

# Listando os arquivos e pastas de um diretório
# os.listdir() -> sem parâmetros, ele lista os arquivos do diretório atual

ARQUIVOS = os.listdir()
print(ARQUIVOS)

# conferindo as extensões dos arquivos
# endswith
MEUSDOCS = os.path.join(os.path.abspath('.'), 'Meus Documentos')
for arqs in os.listdir(MEUSDOCS):
    print(arqs[arqs.rfind('.'):])


# Funçao os.path.isdir('caminho')
NEWPATH = os.path.join(PATH, 'PastaInexistente')
print(f'O caminho{NEWPATH} existe?: {os.path.isdir(NEWPATH)}')
print(f'O caminho{PATH} existe?: {os.path.isdir(PATH)}')


# movendo um arquivo para outras pastas.
# os.rename(arquivo,destino)

#os.rename(os.path.join(PATH, 'teste.rtf'),os.path.join(PATH, 'Meus Documentos', 'teste.rtf'))
print('\n\n\n\n')

tipos = {
    'IMAGENS': ['.gif', '.png', '.jpg', '.bmp'],
    'MUSICAS': ['.mp3']
}

variavel = {x: y for x, y in tipos.items() if '.mp3' in y}
print(list(variavel.keys())[0])
