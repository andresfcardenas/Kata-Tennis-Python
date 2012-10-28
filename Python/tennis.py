#! /usr/bin/env python
import random

REGULATORY_SCORES = ['0', '15', '30', '40', 'Deuce', 'Advantage', 'Win']

class Player:
    """Esta clase representa un jugador
    """
    def __init__(self):
        self.score = REGULATORY_SCORES[0]

    def modify_score(self,p , other_item=None, printed=True):
        """Modifica el puntaje del jugador
        que se le pasa como parametro.
        """
        if other_item == None:
            self.score = REGULATORY_SCORES[
                REGULATORY_SCORES.index(self.score) + 1
            ]
        elif other_item > 3 and other_item < 7:
            self.score = REGULATORY_SCORES[other_item]
        
        if printed:
            print "Player {0} {1}\n".format(p, self.get_score())

    def get_score(self):
        """Retorna el puntaje del jugador
        """
        return self.score


def game(p1, p2):
    """Esta funcion representa un juego
    """
    while True:
        player = random.randrange(1, 3)
        if player == 1:
            p1.modify_score(player)
        else:
            p2.modify_score(player)

        if (p1.get_score() == REGULATORY_SCORES[4] and
            p2.get_score() < REGULATORY_SCORES[3]):
            p1.modify_score(player, 6)
        elif (p1.get_score() < REGULATORY_SCORES[3] and
            p2.get_score() == REGULATORY_SCORES[4]):
            p2.modify_score(player, 6)

        if (p1.get_score() == REGULATORY_SCORES[3] and
            p2.get_score() == REGULATORY_SCORES[3]):
            p1.modify_score(player, 4, False)
            p2.modify_score(player, 4, False)

        if (p1.get_score() == REGULATORY_SCORES[5] and
            p2.get_score() == REGULATORY_SCORES[5]):
            p1.modify_score(player, 4, False)
            p2.modify_score(player, 4, False)

        if p1.get_score() == REGULATORY_SCORES[6]:
            p1.modify_score(player, 4, False)
            return 0
        elif p2.get_score() == REGULATORY_SCORES[6]:
            p2.modify_score(player, 4, False)
            return 0

p1 = Player()
p2 = Player()
game(p1, p2)