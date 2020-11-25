from random import randint

from Peca import Peca


def bot_joga(tabuleiro, jogo, conf):
   for lin in range(conf.linhas):
       p = tabuleiro.tabuleiro[lin][randint(0, 7)]
       if not isinstance(p, Peca):
           continue
       else:
           if p.cor != conf.corPA:
               continue
           else:
                jogo.seleciona(p.lin, p.col)
                if len(jogo.movimentosValidos) > 0:
                    k = [*jogo.movimentosValidos]
                    nlin, ncol = k[randint(0, len(k)-1)]
                    jogo.seleciona(nlin, ncol)
                    break