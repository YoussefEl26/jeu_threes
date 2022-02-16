import sys
sys.path.append("../Tiles/")
from Tiles_acces import *
# 1.1 La fonction initialisera un plateau correspondant à un début de partie.
def init_play():
    plat = {
        "n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0]}
    return plat

# 1.8 Retourne True si la partie est terminée,False sinon
def check_game_over(plat):
    if get_nb_empty_rooms(plat) == 0:
        return False
    else:
        return True

# 1.9 Retourne le score du plateau
def get_score(plat):
    i = 0
    score = 0
    while i < len(plat["tiles"]):
        score += (plat["tiles"][i])
        i += 1
    return score