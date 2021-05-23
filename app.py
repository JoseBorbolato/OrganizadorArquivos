#from ComandosUteisOS import ARQUIVOS
import os

# função que vai organizar meus arquivos de IMAGEM, MUSICA E OUTROS
PASTA = os.path.join(os.path.abspath('.'), 'Meus Documentos')

tipos = {
    'IMAGENS': ['.gif', '.png', '.jpg', '.bmp'],
    'MUSICAS': ['.mp3']
}

# DEFINIR PASTAS
DIRETORIOS = [
    os.path.join(PASTA, 'IMAGENS'),
    os.path.join(PASTA, 'MUSICAS'),
    os.path.join(PASTA, 'OUTROS')
]


def criaDiretorios(caminho):

    for diret in DIRETORIOS:
        if not os.path.isdir(diret):
            os.mkdir(diret)


def organizaPasta(caminho):
    criaDiretorios(caminho)

    tipos_existentes = [[x, x[x.rfind('.'):]] for x in os.listdir(caminho)]
    for arq in tipos_existentes:
        if os.path.isdir(os.path.join(caminho, arq[0])):
            pass
        else:
            for pasta, extensao in tipos.items():
                if arq[1] in extensao:
                    os.rename(os.path.join(caminho, arq[0]), os.path.join(
                        PASTA, pasta, arq[0]))

            '''print(os.path.join(caminho, arq[0]), os.path.join(
                PASTA, 'OUTROS', arq[0]))'''


organizaPasta(PASTA)
