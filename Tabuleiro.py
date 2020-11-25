import pygame

from Peca import Peca


class Tabuleiro:

    def __init__(self, n, conf):
        self.conf = conf
        self.peca = None
        self.nome = n
        self.tabuleiro = []
        self.jogadorA = self.jogadorB = 12
        self.jogadorARei = self.jogadorBRei = 0

    def desenharTabuleiro(self, interface):
        interface.fill(self.conf.corA)
        for col in range(self.conf.colunas):
            for lin in range(col % 2, self.conf.linhas, 2):
                pygame.draw.rect(interface, self.conf.corB,
                                 (col * self.conf.quadrado, lin * self.conf.quadrado, self.conf.quadrado, self.conf.quadrado))

    def posicionarPeca(self):
        for lin in range(self.conf.linhas):
            self.tabuleiro.append([])
            for col in range(self.conf.colunas):
                if col % 2 == (lin + 1) % 2:
                    if lin < 3:
                        self.tabuleiro[lin].append(Peca(lin, col, self.conf.corPA, self.conf.getTamanhoQuadrado()))
                    elif lin > 4:
                        self.tabuleiro[lin].append(Peca(lin, col, self.conf.corPB, self.conf.getTamanhoQuadrado()))
                    else:
                        self.tabuleiro[lin].append(0)
                else:
                    self.tabuleiro[lin].append(0)

    def desenharPecas(self, interface):
        self.desenharTabuleiro(interface)
        self.posicionarPeca()
        for lin in range(self.conf.linhas):
            for col in range(self.conf.colunas):
                peca = self.tabuleiro[lin][col]
                if peca != 0:
                    peca.converterPosicao()
                    peca.desenhar(interface)

    def movimentar(self, peca, lin, col):
        self.tabuleiro[peca.lin][peca.col], self.tabuleiro[lin][col] = self.tabuleiro[lin][col], self.tabuleiro[peca.lin][peca.col]
        peca.mover(lin, col)

        if lin == self.conf.linhas - 1 or lin == 0:
            peca.setRei()
            if peca.cor == self.conf.corPA:
                self.jogadorBRei += 1
            else:
                self.jogadorARei += 1

    def getPeca(self, lin, col):
        return self.tabuleiro[lin][col]

    def remover(self, pecas):
        for p in pecas:
            self.tabuleiro[p.lin][p.col] = 0
            if p != 0:
                if p.cor == self.conf.corPB:
                    self.jogadorA -= 1
                else:
                    self.jogadorB -= 1

    def ganhador(self):
        if self.jogadorA <= 0:
            return self.conf.corPA
        elif self.jogadorB <= 0:
            return self.conf.corPB

        return None

    def getMovimentosValidos(self, peca):
        movimentos = {}
        esquerda = peca.col - 1
        direita = peca.col + 1
        linha = peca.lin

        if peca.cor == self.conf.corPA or peca.rei:
            movimentos.update(self._diagonalEsquerda(linha + 1, min(linha + 3, self.conf.linhas), 1, peca.cor, esquerda))
            movimentos.update(self._diagonalDireita(linha + 1, min(linha + 3, self.conf.linhas), 1, peca.cor, direita))

        if peca.cor == self.conf.corPB or peca.rei:
            movimentos.update(self._diagonalEsquerda(linha - 1, max(linha - 3, -1), -1, peca.cor, esquerda))
            movimentos.update(self._diagonalDireita(linha - 1, max(linha - 3, -1), -1, peca.cor, direita))


        return movimentos

    def _diagonalEsquerda(self, inicio, final, passo, cor, esquerda, capturados=[]):
        movimentos = {}
        ultimo = []
        for r in range(inicio, final, passo):
            if esquerda < 0:
                break

            atual = self.tabuleiro[r][esquerda]
            if atual == 0:
                if capturados and not ultimo:
                    break
                elif capturados:
                    movimentos[(r, esquerda)] = ultimo + capturados
                else:
                    movimentos[(r, esquerda)] = ultimo

                if ultimo:
                    if passo == -1:
                        lin = max(r - 3, 0)
                    else:
                        lin = min(r + 3, self.conf.linhas)
                    movimentos.update(self._diagonalEsquerda(r + passo, lin, passo, cor, esquerda - 1, capturados=ultimo))
                    movimentos.update(self._diagonalDireita(r + passo, lin, passo, cor, esquerda + 1, capturados=ultimo))
                break
            elif atual.cor == cor:
                break
            else:
                ultimo = [atual]

            esquerda -= 1
        return movimentos

    def _diagonalDireita(self, inicio, final, passo, cor, direita, capturados=[]):
        movimentos = {}
        ultimo = []
        for r in range(inicio, final, passo):
            if direita >= self.conf.colunas:
                break

            atual = self.tabuleiro[r][direita]
            if atual == 0:
                if capturados and not ultimo:
                    break
                elif capturados:
                    movimentos[(r, direita)] = ultimo + capturados
                else:
                    movimentos[(r, direita)] = ultimo

                if ultimo:
                    if passo == -1:
                        lin = max(r - 3, 0)
                    else:
                        lin = min(r + 3, self.conf.linhas)
                    movimentos.update(self._diagonalEsquerda(r + passo, lin, passo, cor, direita - 1, capturados=ultimo))
                    movimentos.update(self._diagonalDireita(r + passo, lin, passo, cor, direita + 1, capturados=ultimo))
                break
            elif atual.cor == cor:
                break
            else:
                ultimo = [atual]

            direita += 1
        return movimentos