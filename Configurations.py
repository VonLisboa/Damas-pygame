import pygame

from constantes import Cores
from db import DataBase


class Configurations:
    resolucao = [500, 600, 700, 800]
    cores = [{"White x Black": (Cores.branco, Cores.preto)},
             {"Red x Black": (Cores.vermelho, Cores.preto)},
             {"White x Blue": (Cores.branco, Cores.azul)},
             {"Green x White": (Cores.verde, Cores.branco)},
             {"Green x Blue": (Cores.verde, Cores.azul)}]

    coresPeca = [{"Azul x Vermelho": (Cores.azul, Cores.vermelho)},
             {"Red x Black": (Cores.vermelho, Cores.preto)},
             {"Amarelo x Blue": (Cores.amarelo, Cores.azul)},
             {"Green x Blue": (Cores.verde, Cores.azul)}]

    linhas = colunas = 8

    def __init__(self):
        self.db = DataBase()
        self.indexCor, self.indexCorPeca, self.indexResolucao = self.db.load_configurations()
        self.corA, self.corB = self.cores[self.indexCor].get(list(self.cores[self.indexCor].keys())[0])
        self.corPA, self.corPB = self.coresPeca[self.indexCorPeca].get(list(self.coresPeca[self.indexCorPeca].keys())[0])
        self.largura = self.altura = self.resolucao[self.indexResolucao]
        self.quadrado = self.largura / 8

    def setResolucao(self, i):
        self.index = i
        self.largura = self.altura = self.resolucao[i]
        pygame.display.set_mode((self.largura, self.altura))
        self.quadrado = self.largura / 8
        self.db.update_resolucao(self.indexResolucao)
        return self.largura, self.altura

    def getResolucaoString(self, i):
        return str(self.resolucao[i]) + " x " + str(self.resolucao[i])

    def getCores(self, i):
        k = list(self.cores[i].keys())[0]
        return k

    def getResolucoes(self):
        l = []
        for i in range(0, len(self.resolucao)):
            l.append((self.getResolucaoString(i), i))
        return l

    def getCoresTabulerio(self):
        l = []
        for i in range(0, len(self.cores)):
            l.append((self.getCores(i), i))
        return l

    def setCorTabuleiro(self, i):
        self.indexCor = i
        self.corA, self.corB = self.cores[i].get(list(self.cores[i].keys())[0])
        self.db.update_cor(self.indexCor)

    def getCoresList(self, i):
        k = list(self.coresPeca[i].keys())[0]
        return k

    def getCoresPeca(self):
        l = []
        for i in range(0, len(self.coresPeca)):
            l.append((self.getCoresList(i), i))
        return l

    def setCorPeca(self, i):
        self.indexCorPeca = i
        self.corPA, self.corPB = self.coresPeca[i].get(list(self.coresPeca[i].keys())[0])
        self.db.update_cor_peca(self.indexCorPeca)

    def getResolucaoSelecionada(self):
        return self.altura

    def getTamanhoQuadrado(self):
        return self.quadrado
