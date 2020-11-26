import unittest

from Peca import Peca
from constantes import Cores


class peca_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_definir_posicao(self):
        largura = 800  # 800 x 800
        # sendo tamanho do quadrado 100
        # para a linha 0 e coluna 0, o x e y será 50 ou seja a peça será desenhada
        # a partir do centro do quadrado até o raio definido
        tamQuadrado = largura / 8
        lin = 0
        col = 0
        p = Peca(lin, col, Cores.amareloClaro, tamQuadrado)
        p.converterPosicao()
        self.assertEqual((p.x, p.y), (50, 50))

        lin = 0
        col = 1  # soma 100 no X para a coluna 1 e assim sucessivamente
        p = Peca(lin, col, Cores.amareloClaro, tamQuadrado)
        p.converterPosicao()
        self.assertEqual((p.x, p.y), (150, 50))

        lin = 0
        col = 2  # soma 200
        p = Peca(lin, col, Cores.amareloClaro, tamQuadrado)
        p.converterPosicao()
        self.assertEqual((p.x, p.y), (250, 50))

        # para a linha segue a mesma lógica ocorrendo no Y
        lin = 1 # soma 100 no y
        col = 2  # soma 200 no x
        p = Peca(lin, col, Cores.amareloClaro, tamQuadrado)
        p.converterPosicao()
        self.assertEqual((p.x, p.y), (250, 150))

    def test_mover_e_calcular(self):
        largura = 800  # 800 x 800
        tamQuadrado = largura / 8 # 100
        lin = 1
        col = 2
        p = Peca(lin, col, Cores.amareloClaro, tamQuadrado)
        p.mover(2, 1)  # novo X e Y calculado
        self.assertEqual((p.x, p.y), (150, 250))
        self.assertEqual((p.lin, p.col), (2, 1))

