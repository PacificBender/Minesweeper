import pyglet
from random import randint
from pyglet import shapes

# ############################################## #
#                Variables                       #
# ############################################## #
# couleur des rectangles
color = (50, 255, 30)
# creating a batch object
batch = pyglet.graphics.Batch()
# liste des possibilité de nombre de bombe autour case
list_number_bombe = ["1", "2", "3", "4", "5", "6", "7", "8"]
# image pour flag
flag_hidden = pyglet.resource.image("pngegg.png")
# nombre de bombe flaguée
# f_b = 0

def input_var_game():
    flag_input = False
    while not flag_input:
        
        n_b = input("Veuillez insérer un nombre de bombe à combattre: ")
        rnge = input("Veuillez définir la zone de combat (taille grille): ")
        n_b = int(n_b)
        rnge = int(rnge)
        if n_b > 0:
            if rnge > 0:
                if (rnge*rnge) < n_b:
                    print("il y a plus de bombe que de case wesh")
                else:
                    flag_input = True
                print(flag_input)
            else:
                print("nan mais ... !!? ")
        else: 
            print("Sérieusement ?? ")
    return n_b, rnge


# fabrication a l'ancienne d'une grille de rectangle
def rectangle_grid(x0, y0, rnge, width, height, color, a, b, grid_rect = [[]]):
    grid_line = []
    # liste de coordoné des rectangles
    xrec = []
    yrec = []
    # grilles des coordonné des rectangle
    coor_shape = [[]]
    coor_shape.pop(0)

    # grille de rectangle
    for ix in range(rnge):
        # coordoonée x du rectangle position ix, [:iy]
        xrec.append(x0+(ix*a))
        for iy in range(rnge):
            # positionnement des rectangles + offset + distance inter rectangle
            rectanglei = shapes.Rectangle(x0+(ix*a), y0+(iy*b), width, height, color, batch)
            rectanglei.opacity = 100
            # coordonnée y du rectangle position ix,iy
            yrec.append(y0+(iy*b))
            coor_shape.append([x0+(ix*a),y0+(iy*b)])
            # ajout du rectangle dans la liste ligne de rectangle
            grid_line.append(rectanglei)
        # ajout de la ligne dans le tableau de tableau ======> c'est ca la gris ouuuech
        grid_rect.append(grid_line)
        # reinitialisation de la ligne pour la prochaine ligne
        grid_line = []
    # je sais pas trop pq mais j'ai un ajout d'une ligne vide en premiere iteration
    grid_rect.pop(0)
    # batch.draw()
    #returne de la grille de rectangle + des coordonées de chaque rectangle
    return grid_rect, xrec, yrec, coor_shape    

# fabrication de la grille de bombe (oué oué je sais j'ai mis dessin xP)
def dessin(grid_bombe = [[]], x0 = 0, y0 = 0):
    valj = 0
    vali = 0
    couleur = (255,255,255,255)
    # parcour de la grille case par case 
    for i in grid_bombe:
        for j in grid_bombe[vali]:
            # impression du label dans la case correspondant a la valeur de la
            # case de la grille de bombe 
            if grid_bombe[vali][valj]["content"] == "None":
                # juste psk j'avai eu un soucis et maintenant pas obligé de modifier ca 
                grid_bombe[vali][valj]["content"] = "N"

            # paramétrage de la couleur des labels (nb bombe : 1,2,3 ...)
            if grid_bombe[vali][valj]["content"] == "1":
                couleur = (0, 100, 255, 255)
            elif grid_bombe[vali][valj]["content"] == "2":
                couleur = (0, 255, 0, 255)
            elif grid_bombe[vali][valj]["content"] == "3":
                couleur = (255, 0, 0, 255)
            elif grid_bombe[vali][valj]["content"] == "4":
                couleur = (150, 200, 255, 255)
            elif grid_bombe[vali][valj]["content"] == "5":
                couleur = (255, 0, 255, 255)
            elif grid_bombe[vali][valj]["content"] == "6":
                couleur = (255, 255, 0, 255)
            elif grid_bombe[vali][valj]["content"] == "7":
                couleur = (255, 74, 100, 255)
            elif grid_bombe[vali][valj]["content"] == "8":
                couleur = (0, 0, 0, 255)
            elif grid_bombe[vali][valj]["content"] == "B":
                couleur = (0, 100, 255, 255)

            pyglet.text.Label(grid_bombe[vali][valj]["content"],
                x=2*x0 + 30*vali,
                y=2*y0 + 5 +valj*30,
                anchor_x="center", anchor_y="center",color = couleur).draw()
            valj+=1
        valj=0  
        vali+=1
    batch.draw()

def dessin_win(window, rnge, width):
    global grid_rect 
    # window.set_size(400, 400)
    pyglet.text.Label("Victoire",
        x = rnge*width,
        y = rnge*width,
        anchor_x="center", anchor_y="center").draw()
    pyglet.text.Label("Voulez vous rejouer ?",
        x = rnge*width,
        y = (rnge - 2)*width,
        anchor_x="center", anchor_y="center").draw()
    pyglet.text.Label("Oui",
        x = (rnge - 3)*width,
        y = (rnge - 4)*width,
        anchor_x="center", anchor_y="center").draw()    
    pyglet.text.Label("Non",
        x = (rnge + 3)*width,
        y = (rnge - 4)*width,
        anchor_x="center", anchor_y="center").draw()    



def dessin_loose(window, rnge, width):
    global grid_rect 
    # window.set_size(400, 400)
    pyglet.text.Label("Défaite",
        x = rnge*width,
        y = rnge*width,
        anchor_x="center", anchor_y="center").draw()
    pyglet.text.Label("Voulez vous rejouer ?",
        x = rnge*width,
        y = (rnge - 2)*width,
        anchor_x="center", anchor_y="center").draw()
    pyglet.text.Label("Oui",
        x = (rnge - 3)*width,
        y = (rnge - 4)*width,
        anchor_x="center", anchor_y="center").draw()    
    pyglet.text.Label("Non",
        x = (rnge + 3)*width,
        y = (rnge - 4)*width,
        anchor_x="center", anchor_y="center").draw()    
    


# fabrication a la mano d'une grille vide pour la remplir
def make_empty_ms_grid(n = 0):
    result = []
    finalresult = []
    for j in range(n):
        for i in range(n):
            result.append({"content": "None", "state": "hidden"})
        finalresult.append(result)
        result = []
    return(finalresult)


# premiere version de test non reccursif pour comparaison de la valeur de 
# chaque case autour de la case souhaité
# besoin d'explication ? 
def test_val_min_max(vali, valj, finalresult = [[]],taille_max =0):
    p=0
    if (vali-1) >= 0:
        if valj-1>=0:
            if (finalresult[vali-1][valj-1]["content"] == "B") :
                p +=1
        if (finalresult[vali-1][valj]["content"] == "B"):
            p +=1
        if valj+1<=taille_max:
            if (finalresult[vali-1][valj+1]["content"] == "B"):
                p +=1
                
    if valj-1>=0:
        if (finalresult[vali][valj-1]["content"] == "B"):
            p +=1
        if  vali+1<=taille_max:
            if (finalresult[vali+1][valj-1]["content"] == "B"):
                p +=1    
    if (valj+1)<=taille_max:
        if (finalresult[vali][valj+1]["content"] == "B"):
            p +=1

    if vali+1<=taille_max:
        if (finalresult[vali+1][valj]["content"] == "B") :
            p +=1
        if valj+1<=taille_max:
            if (finalresult[vali+1][valj+1]["content"] == "B"):
                p +=1
    # print(p)
    if p > 0:
        finalresult[vali][valj]["content"] = str(p)
    elif finalresult[vali][valj]["content"] == "B":
        pass               
    elif p == 0: 
        finalresult[vali][valj]["content"] = " "
    
    return p, finalresult


# ajout d'une bombe dans une case de maniere aléatoire, (thx Seb :D)
def add_randomly_bombv3(finalresult=[[]], n=0):
    k = 0
    vali = 0
    valj = 0
    taille_max = int(len(finalresult)) - 1
    
    while k < n:
        if n < len(finalresult)*len(finalresult[0]):
            randI = randint(0, len(finalresult)-1)
            randJ = randint(0, len(finalresult[0])-1)
            if finalresult[randI][randJ]['content'] != 'B':
                finalresult[randI][randJ]["content"] = "B"
                k += 1
                

    for i in range(taille_max+1):
        for j in finalresult[vali]:
            if finalresult[vali][valj]["content"] == "None":
                p, finalresult = test_val_min_max(vali, valj, finalresult, taille_max)
            valj+=1
        valj=0
        vali+=1
    return(finalresult)


# #######################################################################
# #                         Fonction reccursive                         #
# #######################################################################

# fonction de test unitaire de case pour savoir si c'est : 
# une case vide, une case bombe, une case liste de nombre de bombe
def if_hide_y(x ,y ,rnge , grid_bombe = [[]], grid_rect = [[]]):
        bombe_number = ["1", "2", "3", "4", "5", "6", "7", "8"]
        if (grid_bombe[x][y]["content"] == " ") & (grid_bombe[x][y]["state"] == "hidden"):
            grid_rect[x][y].opacity = 0
            grid_bombe[x][y]["state"] = "unhide"
            test_hide_unhide_xy(x, y, rnge, grid_bombe, grid_rect)
        elif (grid_bombe[x][y]["content"] in bombe_number) & (grid_bombe[x][y]["state"] == "hidden"):
            grid_rect[x][y].opacity = 0
            grid_bombe[x][y]["state"] = "unhide"
            
# fonction de test pour verifier que la case n+1 n'est pas out of range 
# pour chaque x on verifie tout les y
def if_hide_for_y(x ,y ,rnge , grid_bombe = [[]], grid_rect = [[]]):
    for iy in range(y-1, y+1):
        if y-1 >= 0:
            if_hide_y(x, y-1, rnge, grid_bombe, grid_rect)
        if 0 <= y <= rnge:
            if_hide_y(x, y, rnge, grid_bombe, grid_rect)
        if y+1 <= rnge - 1:
            if_hide_y(x, y+1, rnge, grid_bombe, grid_rect)


# fonction de test pour verifier que la case n+1 n'est pas out of range 
# pour tout x
def test_hide_unhide_xy(x, y, rnge, grid_bombe = [[]], grid_rect = [[]]):
    for ix in range(x-1, x+1):
        if x-1 >=0:
            if_hide_for_y(x-1, y, rnge, grid_bombe, grid_rect)
        if 0 <= x <= rnge:
            if_hide_for_y(x, y, rnge, grid_bombe, grid_rect)
        if x+1 <= rnge-1:
            if_hide_for_y(x+1, y, rnge, grid_bombe, grid_rect)




####################   Fonction pour externalisation d'event ############
# #######################################################################
# #                         click event                                 #
# #######################################################################
# def left_click_event(x, y, grid_bombe, grid_rect, rnge, xrec, yrec, ix, iy, width, height):
#     flag_loose = False
#     try: 
#         # si case caché
#         if (grid_bombe[ix][iy]["state"] == "hidden"):
#             # si case avec aucune bombe autour d'elle
#             if (grid_bombe[ix][iy]["content"] == " "):
#                 test_hide_unhide_xy(ix, iy, rnge, grid_bombe, grid_rect)
#             # case avec au moins une bombe autour d'elle
#             elif (grid_bombe[ix][iy]["content"] in list_number_bombe):
#                 grid_rect[ix][iy].opacity = 0
#             # big boom big badaboom
#             elif (grid_bombe[ix][iy]["content"] == "B"):
#                 flag_loose = True
#                 return flag_loose
#                 # raise TypeError ("Fin du game")
#                 # print("perdu")
#                 # return(0)
                        
#     # Si on veu, on peu arreter le jeu 
#     except TypeError:
#         # print("Fin du game")
#         raise


# def right_click_event(x, y, grid_bombe, grid_rect, rnge, xrec, yrec):
#     for ix in range(rnge):
#         for iy in range(rnge):
#             # si x,y (position de la souris au moment du clique)
#             # se trouve dans la liste de coordonnées de rectangle 
#             if xrec[ix]<= x <= xrec[ix]+width:
#                 if yrec[iy]<= y <= yrec[iy]+height:
#                     # si case caché
#                     if (grid_bombe
#                     [ix][iy]["state"] == "hidden"):
#                         pass
                        
# def chg_state_flag(pic, grid_bombe =[[]], grid_rect=[[]], list_pos_flag = [[]], pos_flag=[], list_image_flag = [], xrec = 0, yrec = 0, ix = 0, iy = 0, f_b=0):
#     flag_win = False
#     if (grid_bombe[ix][iy]["state"] == "hidden"):
        
#         grid_bombe[ix][iy]["state"] = "flag"
#         grid_rect[ix][iy].opacity = 20
#         xrec_global = xrec[ix]
#         yrec_global = yrec[iy]
#         pos_flag.append(xrec_global)
#         pos_flag.append(yrec_global)
#         list_pos_flag.append(pos_flag)
#         pos_flag = []
#         gfg_pic = pyglet.sprite.Sprite(pic, xrec_global, yrec_global)
#         list_image_flag.append(gfg_pic)    
#         print(n_b)
#         if grid_bombe[ix][iy]["content"] == "B":
#             f_b += 1
        
#         if f_b == n_b:
#             print("gagné")
#             flag_win = True
        
        
#     elif (grid_bombe[ix][iy]["state"] == "flag"):
        
#         if len(list_pos_flag) > 1:
#             for i in range(len(list_pos_flag)):
#                 if [xrec[ix], yrec[iy]] == list_pos_flag[i]:
#                     list_pos_flag.pop(i)
#                     list_image_flag.pop(i)
#                     break
#         elif len(list_pos_flag) == 1:
            
            
#             if [xrec[ix],yrec[iy]] == list_pos_flag[0]:
#                 list_pos_flag.pop(0)
#                 list_image_flag.pop(0)                     
        
#         xrec_global = xrec[ix]
#         yrec_global = yrec[iy]
        
#         grid_rect[ix][iy] = shapes.Rectangle(x0+(ix*a), y0+(iy*b), width, height, color, batch)
#         grid_rect[ix][iy].opacity = 100
#         grid_bombe[ix][iy]["state"] = "hidden"     
#     # xrec = 0
#     # yrec = 0
#     return flag_win, f_b, list_pos_flag, list_image_flag, pos_flag, grid_bombe[ix][iy]["state"]
