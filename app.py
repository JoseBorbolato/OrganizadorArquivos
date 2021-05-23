#from ComandosUteisOS import ARQUIVOS
import os

# função que vai organizar meus arquivos de IMAGEM, MUSICA E OUTROS
tipos = {
    'IMAGENS': ['.gif', '.png', '.jpg', '.bmp'],
    'MUSICAS': ['.mp3']
}


def criaDiretorios(caminho):
    # DEFINIR PASTAS
    DIRETORIOS = [
        os.path.join(caminho, 'IMAGENS'),
        os.path.join(caminho, 'MUSICAS'),
        os.path.join(caminho, 'OUTROS')
    ]
    for diret in DIRETORIOS:
        if not os.path.isdir(diret):
            os.mkdir(diret)


def organizaPasta(caminho):
    criaDiretorios(caminho)

    tipos_existentes = [[x, x[x.rfind('.'):]] for x in os.listdir(caminho)]
    for arq in tipos_existentes:
        if not os.path.isdir(os.path.join(caminho, arq[0])):
            variavel = {x: y for x, y in tipos.items() if arq[1] in y}
            if bool(variavel):
                os.rename(os.path.join(caminho, arq[0]), os.path.join(
                    caminho, list(variavel.keys())[0], arq[0]))
            else:
                os.rename(os.path.join(caminho, arq[0]), os.path.join(
                    caminho, 'OUTROS', arq[0]))


PASTA = os.path.join(os.path.abspath('.'), 'Meus Documentos')
organizaPasta(PASTA)
