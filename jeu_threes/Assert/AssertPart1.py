import sys
sys.path.append("../Game")
from Play import *
sys.path.append("../Tiles/")
from Tiles_moves import *
sys.path.append("../Ui")
from Play_display import *
sys.path.append("../Tiles/")
from Tiles_acces import *
plat = init_play()
#Assert Q1.1
assert init_play() == plat
#Assert Q1.2
assert check_indice(plat, 2)==True
assert check_indice(plat, 0)==True
assert check_indice(plat,-1)==False
assert check_indice(plat, 4)==False
#Assert Q1.3
assert check_room(plat, 0, 0)==True
assert check_room(plat, 3, 3)==True
assert check_room(plat, 3, 4)==False
assert check_room(plat, 4, 3)==False
assert check_room(plat,-1, 0)==False
assert check_room(plat, 0,-1)==False
#Assert Q1.4
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 2, 3, 0,
                  0, 0, 6, 1,
                  0, 48, 12, 1,
                  0, 24, 0, 0]}
assert get_value(plat, 0, 0)==0
assert get_value(plat, -1, 0)==False
assert get_value(plat, 0, -1)==False
assert get_value(plat, 0, 1)==2
assert get_value(plat, 2, 1)==48
assert get_value(plat, 4, 0)==False
assert get_value(plat, 0, 4)==False
#Assert Q1.5
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 2, 3, 0,
                  0, 0, 6, 1,
                  0, 48, 12, 1,
                  0, 24, 0, 0]}
set_value(plat,0,1,2)
print(plat["tiles"])

#Assert Q1.6
assert is_room_empty(plat, 0, 0)== True
assert is_room_empty(plat, 1, 0)== True
assert is_room_empty(plat, 2, 1)== False
assert is_room_empty(plat, 3, 3)== True
#Assert Q1.7
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 2, 3, 0,
                  0, 0, 6, 1,
                  0, 48, 12, 1,
                  0, 24, 0, 0]}
assert get_nb_empty_rooms(plat)==8
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 2, 3, 2,
                  0, 1, 6, 1,
                  0, 48, 12, 1,
                  0, 24, 0, 0]}
assert get_nb_empty_rooms(plat)==6
#Assert Q1.8
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 2, 3, 0,
                  0, 0, 6, 1,
                  0, 48, 12, 1,
                  0, 24, 0, 0]}
assert check_game_over(plat)==True
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [1, 2, 3, 1,
                  1, 1, 6, 1,
                  1, 48, 12, 1,
                  1, 24, 1, 1]}
assert check_game_over(plat)==False
#Assert Q1.9
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 2, 3, 0,
                  0, 0, 6, 1,
                  0, 48, 12, 1,
                  0, 24, 0, 0]}
assert get_score(plat)==97
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [1, 2, 3, 1,
                  1, 1, 6, 1,
                  1, 48, 12, 1,
                  1, 24, 1, 1]}
assert get_score(plat)==105
#Assert Q1.10
medium_display(plat)