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
from random import *

#Q2.1
def get_next_alea_tiles(plat,mode):
    if mode == "init":
            tiles = {"mode": "init",
                    0:{"val": 2, "lig": randint(0, 3), "col": randint(0, 3)},
                    1:{"val": 1, "lig": randint(0, 3), "col": randint(0, 3)},
                    "check": True}
    elif mode == "encours":
        b = False
        while b == False:
            lig=randint(0,3)
            col=randint(0,3)
            b=is_room_empty(plat,lig,col)

        val=randint(1,3)
        tiles = {"mode":"encours",
                0:{"val":val, "lig" : lig, "col" :col},
                "check": True}
    return tiles



#Q2.2
def put_next_tiles(plat,tiles):
    i=0
    while i<len(tiles)-2:
        set_value(plat, tiles[i]["lig"], tiles[i]["col"], tiles[i]["val"])
        i+=1
    return plat

#Q2.3
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 1, 0, 3,
                  0, 0, 7, 0,
                  0, 10, 0, 0,
                  0, 0, 14, 15]}
def line_pack(plat,lig,sens):
    if sens == 1:
        ind = 0
        while ind < 3:
            if get_value(plat, lig, ind) == 0:
                set_value(plat, lig, ind, get_value(plat, lig, ind + 1))
                set_value(plat, lig, ind + 1, 0)
            ind += 1
    else:
        ind = 3
        while ind > 0:
            if get_value(plat, lig, ind) == 0:
                set_value(plat, lig, ind, get_value(plat, lig, ind - 1))
                set_value(plat, lig, ind - 1, 0)
            ind -= 1
    return plat

#Q2.4
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 1, 0, 3,
                  0, 0, 7, 0,
                  0, 10, 0, 0,
                  0, 0, 14, 15]}
def column_pack(plat,col,sens):
    if sens == 1 :
        ind = 0
        while ind < 3 :
            if get_value(plat, ind,col) == 0 :
                set_value(plat,ind, col, get_value(plat, ind+1,col))
                set_value(plat,ind+1,col, 0)
            ind+=1
    else :
        ind = 3
        while ind>0 :
            if get_value(plat, ind,col) == 0 :
                set_value(plat,ind, col, get_value(plat, ind-1,col))
                set_value(plat,ind-1,col, 0)
            ind-=1
    return plat
#Q2.5
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 1, 0, 0,
                  3, 3, 3, 3,
                  0, 10, 0, 0,
                  0, 0, 14, 15]}
def line_move(plat,lig,sens):
    if sens==0:
        z=0
        while z<2:
            i = 0
            while i<3:
                line_pack(plat,lig,sens)
                i+=1
            if plat["tiles"][lig*4]==plat["tiles"][lig*4+1]:
                a=get_value(plat, lig, 0)
                b=get_value(plat, lig, 1)
                a=a+b
                set_value(plat,lig,0,a)
                set_value(plat, lig,1,0)

            if plat["tiles"][lig*4+1]==plat["tiles"][lig*4+2]:
                a=get_value(plat, lig, 1)
                b=get_value(plat, lig, 2)
                a=a+b
                set_value(plat, lig, 1, a)
                set_value(plat, lig, 2, 0)

            if plat["tiles"][lig*4+2]==plat["tiles"][lig*4+3]:
                a=get_value(plat, lig, 2)
                b=get_value(plat, lig, 3)
                a=a+b
                set_value(plat, lig, 2, a)
                set_value(plat, lig, 3, 0)
            line_pack(plat, lig, sens)
            z+=1
    if sens==1:
        z=0
        while z<2:
            i = 0
            while i<3:
                line_pack(plat,lig,sens)
                i+=1
            if plat["tiles"][lig*4+3]==plat["tiles"][lig*4+2]:
                a=get_value(plat, lig, 3)
                b=get_value(plat, lig, 2)
                a=a+b
                set_value(plat,lig,3,a)
                set_value(plat, lig,2,0)

            if plat["tiles"][lig*4+2]==plat["tiles"][lig*4+1]:
                a=get_value(plat, lig, 2)
                b=get_value(plat, lig, 1)
                a=a+b
                set_value(plat, lig, 2, a)
                set_value(plat, lig, 1, 0)

            if plat["tiles"][lig*4+1]==plat["tiles"][lig*4]:
                a=get_value(plat, lig, 1)
                b=get_value(plat, lig, 0)
                a=a+b
                set_value(plat, lig, 1, a)
                set_value(plat, lig, 0, 0)
            line_pack(plat, lig, sens)
            z+=1
    return plat
#Q2.6
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 1, 3, 0,
                  3, 3, 3, 3,
                  0, 10, 3, 0,
                  0, 0, 3, 15]}
def column_move(plat,col,sens):
    if sens==1:
        z=0
        while z<2:
            i = 0
            while i<3:
                column_pack(plat,col,sens)
                i+=1
            if plat["tiles"][col]==plat["tiles"][col+4]:
                a=get_value(plat, 0, col)
                b=get_value(plat, 1, col)
                a=a+b
                set_value(plat, 0,col,a)
                set_value(plat, 1,col,0)

            if plat["tiles"][col+4]==plat["tiles"][col+8]:
                a=get_value(plat, 1, col)
                b=get_value(plat, 2, col)
                a=a+b
                set_value(plat, 1, col, a)
                set_value(plat, 2, col, 0)

            if plat["tiles"][col+8]==plat["tiles"][col+12]:
                a=get_value(plat, 2, col)
                b=get_value(plat, 3, col)
                a=a+b
                set_value(plat, 2, col, a)
                set_value(plat, 3, col, 0)
            z+=1
    if sens==0:
        z=0
        while z<2:
            i = 0
            while i<3:
                column_pack(plat,col,sens)
                i+=1
            if plat["tiles"][col+12]==plat["tiles"][col+8]:
                a=get_value(plat, 3, col)
                b=get_value(plat, 2, col)
                a=a+b
                set_value(plat, 3,col,a)
                set_value(plat, 2,col,0)

            if plat["tiles"][col+8]==plat["tiles"][col+4]:
                a=get_value(plat, 2, col)
                b=get_value(plat, 1, col)
                a=a+b
                set_value(plat, 2, col, a)
                set_value(plat, 1, col, 0)

            if plat["tiles"][col+4]==plat["tiles"][col+0]:
                a=get_value(plat, 1, col)
                b=get_value(plat, 0, col)
                a=a+b
                set_value(plat, 1, col, a)
                set_value(plat, 0, col, 0)
            z+=1
    return plat
#Q2.7
def lines_move(plat,sens):
    if sens==0:
        line_move(plat, 0, 0)
        line_move(plat, 1, 0)
        line_move(plat, 2, 0)
        line_move(plat, 3, 0)

    if sens==1:
        line_move(plat, 0, 1)
        line_move(plat, 1, 1)
        line_move(plat, 2, 1)
        line_move(plat, 3, 1)
    return plat
medium_display(lines_move(plat,0))
#Q2.8
plat = {"n": 4,
        "nb_cases_libres": 16,
        "tiles": [0, 1, 3, 0,
                  3, 3, 3, 3,
                  0, 10, 3, 0,
                  0, 0, 3, 15]}
def columns_move(plat,sens):
    if sens==0:
        column_move(plat, 0, 0)
        column_move(plat, 1, 0)
        column_move(plat, 2, 0)
        column_move(plat, 3, 0)

    if sens==1:
        column_move(plat, 0, 1)
        column_move(plat, 1, 1)
        column_move(plat, 2, 1)
        column_move(plat, 3, 1)
    return plat

#Q2.9
def play_move(plateau, sens):
    """Deplace les tuiles du plateau dans un sens donné en appliquant les règles du jeu Threes"""
    if sens == 'g':
        lines_move(plateau,1)
    elif sens == 'd':
        lines_move(plateau, 0)
    elif sens == 'h':
        columns_move(plateau, 1)
    elif sens == 'b':
        columns_move(plateau, 0)