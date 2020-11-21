import unittest

import pygame

from Configurations import Configurations
from Jogo import Jogo


class jogo_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_mudar_vez(self):
        conf = Configurations()
        display = pygame.display.set_mode((conf.largura, conf.altura))
        jogo = Jogo(display, conf)
        self.assertEqual(jogo.vez, conf.corPB)
        jogo.mudarVez()
        self.assertEqual(jogo.vez, conf.corPA)
        jogo.mudarVez()
        self.assertEqual(jogo.vez, conf.corPB)
        jogo.mudarVez()
        self.assertEqual(jogo.vez, conf.corPA)

    def test_desenha_mover(self):
        pass