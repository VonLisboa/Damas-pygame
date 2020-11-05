import pygame
import sqlite3
import os

from constantes import Cores


class Configurations:
    resolucao = [500, 600, 700, 800]
    cores = [{"White x Black": (Cores.branco, Cores.preto)},
             {"Red x Black": (Cores.vermelho, Cores.preto)},
             {"White x Blue": (Cores.branco, Cores.azul)},
             {"Green x Blue": (Cores.verdeClaro, Cores.azul)}]

    linhas = colunas = 8

    def __init__(self):
        # adicionar sqlite pra salvar e recarregar configurações
        self.createTableConfiguracao()
        self.indexCor, self.indexResolucao = self.insertConfiguracao()
        self.corA, self.corB = self.cores[self.indexCor].get(list(self.cores[self.indexCor].keys())[0])
        self.largura = self.altura = self.resolucao[self.indexResolucao]
        self.quadrado = self.largura / 8


    def createTableConfiguracao(self):
        if not (os.path.exists('jogoDamas.db')):
            conn = sqlite3.connect('jogoDamas.db')
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE configuracao (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    cor INTEGER NOT NULL,
                    resolucao INTEGER NOT NULL
            );
            """)
            print('Tabela criada com sucesso.')
            cursor.execute('INSERT INTO configuracao (cor, resolucao) VALUES (0, 0)')
            conn.commit()
            print('Dados inseridos com sucesso.')
            conn.close()

    def insertConfiguracao(self):
        if (os.path.exists('jogoDamas.db')):
            conn = sqlite3.connect('jogoDamas.db')
            cursor = conn.cursor()
            cursor.execute('SELECT cor, resolucao from configuracao')
            for linha in cursor.fetchall():
                return linha
            conn.close


    def updateCor(self, indexCor):
        conn = sqlite3.connect('jogoDamas.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE configuracao SET cor =' + str(indexCor) +  ' WHERE id = 1')
       # cursor.execute('INSERT INTO configuracao (cor, resolucao) VALUES (0, 0)')
        conn.commit()
        print('Dados atualizados com sucesso.')
        conn.close

    def updateResolucao(self, indexResolucao):
        conn = sqlite3.connect('jogoDamas.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE configuracao SET resolucao =' + str(indexResolucao) +  ' WHERE id = 1')
        conn.commit()
        print('Dados atualizados com sucesso.')
        conn.close


    def setResolucao(self, i):
        self.index = i
        self.largura = self.altura = self.resolucao[i]
        pygame.display.set_mode((self.largura, self.altura))
        self.quadrado = self.largura / 8
        self.updateResolucao(self.indexResolucao)
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
        self.updateCor(self.indexCor)

    def getResolucaoSelecionada(self):
        return self.altura

    def getTamanhoQuadrado(self):
        return self.quadrado
