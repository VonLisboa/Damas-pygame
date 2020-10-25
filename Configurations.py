import pygame

from constantes import Cores


class Configurations:
    resolucao = [500, 600, 700, 800]
    cores = [{"White x Black": (Cores.branco, Cores.preto)},
             {"Red x Black": (Cores.vermelho, Cores.preto)},
             {"White x Blue": (Cores.branco, Cores.azul)},
             {"Green x Blue": (Cores.verdeClaro, Cores.azul)}]
    indexResolucao = 0
    indexCor = 0
    corA, corB = cores[indexCor].get(list(cores[indexCor].keys())[0])
    largura = altura = resolucao[indexResolucao]
    linhas = colunas = 8
    quadrado = largura / 8

    def __init__(self):
        pass

    def setResolucao(self, i):
        self.index = i
        self.largura = self.altura = self.resolucao[i]
        pygame.display.set_mode((self.largura, self.altura))
        self.quadrado = self.largura / 8
        return self.largura, self.altura

    def getResolucao(self, i=indexResolucao):
        return str(self.resolucao[i]) + " x " + str(self.resolucao[i])

    def getCores(self, i=indexCor):
        k = list(self.cores[i].keys())[0]
        return k

    def getResolucoes(self):
        l = []
        for i in range(0, len(self.resolucao)):
            l.append((self.getResolucao(i), i))
        return l

    def getCoresTabulerio(self):
        l = []
        for i in range(0, len(self.cores)):
            l.append((self.getCores(i), i))
        return l

    def setCorTabuleiro(self, i):
        self.indexCor = i
        self.corA, self.corB = self.cores[i].get(list(self.cores[i].keys())[0])
