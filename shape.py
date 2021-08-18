
# CS 5001

# links to the animated sun, man and fish 
# https://drive.google.com/file/d/1BOSlV-ipSJ-Fabw2FFsxuaXvmojlu-qT/view?usp=sharing (draws the final scene)
# https://drive.google.com/file/d/16oV1NiDl5qUWGnNyhcLpmSsxMT5gTZSu/view?usp=sharing (fish )
# https://drive.google.com/file/d/1G6j_yEAMMP_snzMYkZwR-qfof-irr3ko/view?usp=sharing ( sun )
# https://drive.google.com/file/d/1kJTxeJJlpRuPS_pWY0gLRLurAL1VB0PW/view?usp=sharing ( man )
 
# imported package graphicsPlus, time, random and sys
import graphicsPlus as gr
import time
import random
 
import sys
 
# move animates the shape by moving the shape by the given coordinates 
def move( shapes, dx, dy ):
    """ Draw all of the objects in shapes by dx in the x-direction
    and dy in the y-direction """
    # for each item in shapes
    for item in shapes:
        item.move( dx, dy)
 
# def init_man defines the river fucntion with three parameters x, y and scales 
def init_man(x, y, scale): 
    # define the man shapes and put them into a list 
  
    # Head: Create a circle with the color brown 
    head = gr.Circle( gr.Point ( x+scale*10, y-scale*50), 20*scale)  
    head.setFill('brown') 
  
    # arms : Create a rectangle with the color blue for the arms 
    arms = gr.Rectangle( gr.Point ( x+scale*110, y), gr.Point(x-scale*80, y-scale*30 )) 
    arms.setFill('blue') 
  
    # stomach : Create a rectangle with the color blue for the sh  
    stomach = gr.Rectangle( gr.Point ( x+scale*70, y+scale*60), gr.Point(x-scale*50, y )) 
    stomach.setFill('blue') 
  
    # # leg2 : Create a rectangle with the color red for pants 
    leg1 = gr.Rectangle( gr.Point ( x-scale*20, y+scale*60), gr.Point(x-scale*40, y+scale*180 )) 
    leg1.setFill('red') 
  
    #   # leg2 : Create a rectangle with the color red for pants  
    leg2 = gr.Rectangle( gr.Point ( x+scale*60, y+scale*60), gr.Point(x+scale*40, y+scale*180 )) 
    leg2.setFill('red') 
  
   
    # man creates the list of all the basic shapes created by zelle 
    man = [ head, arms, leg1, leg2, stomach ] 
    return man 
  
  
  
# def init_sun defines the river fucntion with three parameters x, y and scales 
def init_sun(x, y, scale): 
     # create a circle with the sun 
    inner_sun = gr.Circle( gr.Point ( x-scale*260, y-scale*200), 120*scale)  
    inner_sun.setFill('orange') 
  
    outer_sun= gr.Circle( gr.Point ( x-scale*260, y-scale*200), 150*scale)  
    outer_sun.setFill('yellow') 
  
    # leg1 = gr.Rectangle( gr.Point ( x-scale*20, y+scale*60), gr.Point(x-scale*40, y+scale*180 )) 
    # leg1.setFill('red') 
  
     
    # created a list for the two circeles creating the sun complex object 3 
    sun = [ outer_sun, inner_sun ] 
    return sun 
  
  
# def init_river defines the river fucntion with three parameters x, y and scales 
def init_river(x, y, scale): 
  
    # # diving board : Create a rectangle with the color brown  
    diving_board = gr.Rectangle( gr.Point ( x+scale*180, y+scale*180), gr.Point(x-scale*260, y+scale*250 )) 
    diving_board.setFill('brown') 
  
    # create a swiming river with the color skyblue 
    water = gr.Rectangle( gr.Point ( x+scale*780, y+scale*880), gr.Point(x-scale*260, y+scale*250 )) 
    water.setFill('skyblue') 
  
    # create a list of the complex shapes  
    river = [  diving_board, water ] 
  
    return river 
  
# def init_fish draws the fish for the water. This is another polygon object which forms a fish as my third complex object. 
def init_riverFish( x, y, scale ): 
  
    # define a polygon for the body 
    bodylist = [ gr.Point( x + 5*scale, y - 5*scale ), 
                 gr.Point( x + 25*scale, y - 2*scale ), 
                 gr.Point( x + 45*scale, y - 8*scale ), 
                 gr.Point( x + 70*scale, y - 15*scale ), 
                 gr.Point( x + 100*scale, y - 6*scale ), 
                 gr.Point( x + 90*scale, y - 20*scale ), 
                 gr.Point( x + 100*scale, y - 34*scale ), 
                 gr.Point( x + 80*scale, y - 30*scale ), 
                 gr.Point( x + 55*scale, y - 27*scale ), 
                 gr.Point( x + 45*scale, y - 30*scale ), 
                 gr.Point( x + 24*scale, y - 40*scale ), 
                 gr.Point( x + 0*scale, y - 30*scale ), 
                 gr.Point( x - 8*scale, y - 28*scale ) ] 
    fishbody = gr.Polygon( bodylist) 
    fishbody.setFill( 'grey') # paint the fish grey 
    fishbody.setOutline( 'black' ) # black outline for the fish  
    fishbody.setWidth( 4 ) 
  
    fish = [ fishbody ]  
  
    # return the list 
    return fish 
 
#  shapes is a list of zelle objects that make a complex shape
def draw( shapes, win ):
 
    for thing in shapes:
        thing.draw( win ) # loop draws the complex shapes 
 
def animate_man( shapes, frame_num, win ): # shapes is equal to the man list returned in init_man and animation
    # added some movement to the man 
    if frame_num < 50:
        move( shapes, 1, 0)
    else:
        move( shapes, -1, 0)
 
def animate_fish( shapes, frame_num, win ): # shapes is equal to the fish list returned in init_fish 
    # added some movement to the man  
    if frame_num < 10: 
        move( shapes, 0, 0) 
    else: 
        move( shapes, -5, 0) 
  
def animate_fish1( shapes, frame_num, win ): # shapes is equal to the fish list returned in init_fish 
    # added some movement to the man  
    if frame_num < 10: 
        move( shapes, 0, 0) 
    else: 
        move( shapes, -5, 0) 
  
def animate_fish2( shapes, frame_num, win ): # shapes is equal to the fish list returned in init_fish 
    # added some movement to the man  
    if frame_num < 10: 
        move( shapes, 0, 0) 
    else: 
        move( shapes, -5, 0) 
 
def animate_sun( shapes, frame_num, win ): # shapes is equal to the sun list returned in the init_sun
# added some movement to the man 
    if frame_num < 10:
        move( shapes, 0, 0)
    else:
        move( shapes, -5, 0)
 
if __name__ == "__main__":
    main()