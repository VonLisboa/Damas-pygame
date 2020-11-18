import unittest

from Peca import Peca
from Configurations import Configurations
from Tabuleiro import Tabuleiro


class tabuleiro_test(unittest.TestCase):

    def test_posicionar_peca(self):
        tab = Tabuleiro("meuTab", Configurations())
        arrayTab = tab.tabuleiro.copy()
        self.assertEqual(arrayTab, [])
        tab.posicionarPeca()
        arrayTab2 = tab.tabuleiro.copy()

        for linha in arrayTab2:
            for pos in range(0, int(len(linha)), 2):
                if linha[0] == 0 and linha[1] != 0:
                    self.assertNotIsInstance(linha[pos], Peca)
                    self.assertIsInstance(linha[pos+1], Peca)
                if linha[0] != 0:
                    self.assertIsInstance(linha[pos], Peca)
                    self.assertNotIsInstance(linha[pos + 1], Peca)

    def test_mover_peca(self):
        tab = Tabuleiro("meuTab", Configurations())
        tab.posicionarPeca()
        peca = tab.tabuleiro[0][1]
        tab.movimentar(peca, 3, 3)
        self.assertNotIsInstance(tab.tabuleiro[0][1], Peca)
        self.assertIsInstance(tab.tabuleiro[3][3], Peca)

        peca = tab.tabuleiro[3][3]
        tab.movimentar(peca, 5, 7)
        self.assertNotIsInstance(tab.tabuleiro[3][3], Peca)
        self.assertIsInstance(tab.tabuleiro[5][7], Peca)

        peca = tab.tabuleiro[5][7]
        tab.movimentar(peca, 4, 1)
        self.assertNotIsInstance(tab.tabuleiro[5][7], Peca)
        self.assertIsInstance(tab.tabuleiro[4][1], Peca)

    def test_remover_peca(self):
        tab = Tabuleiro("meuTab", Configurations())
        tab.posicionarPeca()
        peca1 = tab.tabuleiro[0][1]
        peca2 = tab.tabuleiro[0][3]

        self.assertIsInstance(peca1, Peca)
        self.assertIsInstance(peca2, Peca)

        tab.remover([peca1, peca2])
        peca1 = tab.tabuleiro[0][1]
        peca2 = tab.tabuleiro[0][3]

        self.assertNotIsInstance(peca1, Peca)
        self.assertNotIsInstance(peca2, Peca)
