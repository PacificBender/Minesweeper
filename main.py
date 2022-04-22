import pyglet
from pyglet import image
from pyglet import shapes
from functions_need import *
from pyglet.gl import *
list_number_bombe = ["1", "2", "3", "4", "5", "6", "7", "8"]

#######################################
#       properties of rectangle       #
#######################################
# Nombre de bombe
n_b = 0
# offset
x0 = 7
y0 = 5
# distance between rectangle a-x b-y
a = 30
b = 30
# size des rectangles
width = 15
height = 20
# couleur des rectangles
color = (50, 255, 30)
# nombre de rectangle dans la fenetre = rnge²
rnge = 1
# creating a batch object
batch = pyglet.graphics.Batch()


# input in terminal
# nombre de bombe, taille de grille = rnge²
n_b, rnge = input_var_game()

#######################################
#        properties of window         #
#######################################
# creating window in function_need
# .. en attente de xinput pour determiner taille et nombre bombe
# creating a batch object (created in functions_need)
#batch = pyglet.graphics.Batch()

# ## WINDOW
window = pyglet.window.Window(2*rnge*width, 2*rnge*width, "Minsweeper")
pyglet.gl.glClearColor(0.5, 0, 0, 1)

# ## GRID
# empty grid for adding bomb
empty_grid = make_empty_ms_grid(rnge)
# grid with bomb adding
grid_bombe = add_randomly_bombv3(empty_grid, n_b)
# ==> grid_rect = list of list of rectangle
# ==> xrec,yrec == [[x du rectangle], [y du rectangle]] (coordonées de chaque rectangle)
grid_rect = [[]]
grid_rect, xrec, yrec, coor_shape = rectangle_grid(
    x0, y0, rnge, width, height, color, a, b, grid_rect)

# ## FLAG IMAGE CLICK DROIT
# image du flag
flag_hidden = pyglet.resource.image("pngegg2.png")
pic = image.load("pngegg2.png")
# grille de coordonnée des positions des flags
list_pos_flag = [[]]
list_pos_flag.pop(0)
# coordonnées des flags
pos_flag = []
# liste de flags 
list_image_flag = []
#nombre de bombe flagué
f_b = 0
#nombre de flag posé en tout
f_nb = 0

flag_win = False
flag_loose = False

flag_event_right_click = False


#######################################
#                 GO                  #
#######################################
@window.event
def on_draw():
    global grid_rect 
    global grid_bombe
    # global window
    print(flag_loose) 
    if not flag_loose:

        if not flag_win:
            window.clear()
            dessin(grid_bombe, x0, y0)
            
            # draw du flag            
            for im in list_image_flag:
                im.draw()

        elif flag_win:
            window.clear()
            grid_rect = [[]*rnge]
            # window.set_size(400, 400)
            # scale = rnge/2
            # glScalef(scale, scale, scale)
            dessin_win(window, rnge, width)
            # batch.draw()
            
    if flag_loose: 
        window.clear
        #These arguments are x, y and z respectively. This scales your window.
        grid_rect = [[]*rnge]
        dessin_loose(window, rnge, width)

    
    batch.draw()
# window = pyglet.window.Window(2*rnge*width, 2*rnge*width, "Minsweeper")
            
@window.event
def on_mouse_release(x,y,button, modifiers):
    # global variabl linke between window-event for position mouse on click
    # 
    pos_flag = []
    global list_pos_flag
    global flag_win
    global flag_loose
    global list_image_flag
    # nombre de bombe flagué 
    global f_b
    global f_nb
    
    # coordonnées des flags dans la grille de rect
    xrec_flag = 0 
    yrec_flag = 0
    
    coordone_shape = []
    if button == 1:
        for ix in range(rnge):
            for iy in range(rnge):
                
                # si x,y (position de la souris au moment du clique)
                # se trouve dans la liste de coordonnées de rectangle 
                if xrec[ix]<= x <= xrec[ix]+width:  
                    if yrec[iy]<= y <= yrec[iy]+height:
                        coordone_shape.append(xrec[ix])
                        coordone_shape.append(yrec[iy])
                        
                        # flag_loose = left_click_event(x, y, grid_bombe, grid_rect, rnge, xrec, yrec, ix, iy, width, height)  
                        if (grid_bombe[ix][iy]["state"] == "hidden"):
                            
                            # si case avec aucune bombe autour d'elle
                            if (grid_bombe[ix][iy]["content"] == " "):
                                test_hide_unhide_xy(ix, iy, rnge, grid_bombe, grid_rect)
                                
                            # case avec au moins une bombe autour d'elle
                            elif (grid_bombe[ix][iy]["content"] in list_number_bombe):
                                grid_rect[ix][iy].opacity = 0
                                
                            # big boom big badaboom
                            elif (grid_bombe[ix][iy]["content"] == "B"):
                                flag_loose = True
                if flag_loose:
                    break
            if flag_loose:
                break

    elif button == pyglet.window.mouse.RIGHT:
        for ix in range(rnge):
            for iy in range(rnge):
                
                # si x,y (position de la souris au moment du clique)
                # se trouve dans la liste de coordonnées de rectangle 
                if xrec[ix]<= x <= xrec[ix]+width:
                    if yrec[iy]<= y <= yrec[iy]+height:
                        
                        # si case caché
                        if (grid_bombe[ix][iy]["state"] == "hidden"):
                            grid_bombe[ix][iy]["state"] = "flag"
                            # grid_rect[ix][iy].opacity = 20
                            xrec_flag = xrec[ix]
                            yrec_flag = yrec[iy]
                            pos_flag.append(xrec_flag)
                            pos_flag.append(yrec_flag)
                            list_pos_flag.append(pos_flag)
                            pos_flag = []
                            
                            gfg_pic = pyglet.sprite.Sprite(pic, xrec_flag, yrec_flag)
                            list_image_flag.append(gfg_pic)    
                            
                            if grid_bombe[ix][iy]["content"] == "B":
                                f_b += 1
                            f_nb +=1
                            
                            if f_b == n_b and f_nb == n_b:
                                print("gagné")
                                flag_win = True
                                break

                        elif (grid_bombe[ix][iy]["state"] == "flag"):
                            
                            if len(list_pos_flag) > 1:
                                for i in range(len(list_pos_flag)):
                                    if [xrec[ix], yrec[iy]] == list_pos_flag[i]:
                                        list_pos_flag.pop(i)
                                        list_image_flag.pop(i)
                                        break
                            elif len(list_pos_flag) == 1:
                                if [xrec[ix],yrec[iy]] == list_pos_flag[0]:
                                    list_pos_flag.pop(0)
                                    list_image_flag.pop(0)       
                            
                            if grid_bombe[ix][iy]["content"] == "B":
                                f_b -= 1
                            f_nb -=1              
                            
                            if f_b == n_b and f_nb == n_b:
                                print("gagné")
                                flag_win = True

                            grid_rect[ix][iy] = shapes.Rectangle(x0+(ix*a), y0+(iy*b), width, height, color, batch)
                            grid_rect[ix][iy].opacity = 100
                            grid_bombe[ix][iy]["state"] = "hidden"  
                    if flag_win:
                        break
                if flag_win:
                    break
            if flag_win:
                break


pyglet.app.run()    