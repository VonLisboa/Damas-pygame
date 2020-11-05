import pygame

from Peca import Peca
from constantes import Cores
from Configurations import Configurations


class Tabuleiro:

    def __init__(self, n=None):
        self.peca = None
        self.nome = n
        self.tabuleiro = []
        #conf = Configurations()
        #self.posicionarPeca(conf)


    def iniciarTabuleiro(self, interface, conf):

        interface.fill(conf.corA)

        for col in range(conf.colunas):
            for lin in range(col % 2, conf.linhas, 2):
                pygame.draw.rect(interface, conf.corB, (col * conf.quadrado, lin * conf.quadrado, conf.quadrado, conf.quadrado))



    def posicionarPeca(self, conf):
        for lin in range(conf.linhas):
            self.tabuleiro.append([])
            for col in range(conf.colunas):
                if col % 2 == (lin + 1) % 2:
                    if lin < 3:
                        self.tabuleiro[lin].append(Peca(lin, col, Cores.vermelho))
                    elif lin > 4:
                        self.tabuleiro[lin].append(Peca(lin, col, Cores.azul))
                    else:
                        self.tabuleiro[lin].append(0)
                else:
                    self.tabuleiro[lin].append(0)

    def desenharPecas(self, interface, conf):
        self.iniciarTabuleiro(interface, conf)
        self.posicionarPeca(conf)
        for lin in range(conf.linhas):

            for col in range(conf.colunas):
                peca = self.tabuleiro[lin][col]
                #print(peca)
                if peca != 0:
                    quadradoTam = conf.getResolucaoSelecionada()/8
                    peca.definirPosicao(quadradoTam)
                    peca.iniciarPeca(interface, quadradoTam)

    def getPeca(self, lin, col):
        return self.tabuleiro[lin][col]

