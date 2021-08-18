# Caroline Ninganga
# CS 5001
# Project 5
# Man walking by the river
 
import graphicsPlus as gr
import shapes2 as cs
import time
import random
 
import sys
 
# links to the animated sun, man and fish  
# https://drive.google.com/file/d/1BOSlV-ipSJ-Fabw2FFsxuaXvmojlu-qT/view?usp=sharing (draws the final scene) 
# https://drive.google.com/file/d/16oV1NiDl5qUWGnNyhcLpmSsxMT5gTZSu/view?usp=sharing (fish ) 
# https://drive.google.com/file/d/1G6j_yEAMMP_snzMYkZwR-qfof-irr3ko/view?usp=sharing ( sun ) 
# https://drive.google.com/file/d/1kJTxeJJlpRuPS_pWY0gLRLurAL1VB0PW/view?usp=sharing ( man ) 
 
 
# draws the entire scene with man river, sun, fish 
def scene( argsList ):  
  
    # this is the graphics window 
    win = gr.GraphWin( "My window", 1000, 1000 ) 
  
    # This controls the scale location and size of the scene 
    x = 0 
    y = 0 
    scale = 1 
  
    #only save command line args if they are proivded. This section allows the user to enter the specified arguments.  
    if len(argsList) == 4: 
        x = int (argsList[1]) 
        y = int (argsList[2]) 
        scale = float (argsList[3]) 
  
    print(argsList) 
  
  
    # draw the fish, fish1, fish2 into the window at different locations 
    fish =  cs.init_riverFish( x+350*scale, y+50*scale, scale*0.5)
    fish1 = cs.init_riverFish( x+400*scale, y+100*scale, scale*0.5) 
    fish2 = cs.init_riverFish( x+550*scale, y+150*scale, scale*0.5) 
    fish3 = cs.init_riverFish( x+600*scale, y+200*scale, scale*0.5) 
    fish4 = cs.init_riverFish( x+650*scale, y+200*scale, scale*0.5) 

    # fish2 = cs.init_riverFish( x+400*scale, y+500*scale, scale*0.5) 
    # fish2 = cs.init_riverFish( x+400*scale, y+500*scale, scale*0.5) 
  
  
    # draw the man into the window  
    man = cs.init_man( x+450*scale, y+450*scale, scale*0.5) 
  
  
    # # draw the river into the window 
    river = cs.init_river( x+200*scale, y+550*scale, scale) 
  
    # line 22 to 24 call the draw function which draws the zelle shapes that draw the csmplex shapes  
    cs.draw(man, win) 
    cs.draw(river, win) 
    cs.draw(fish, win ) 
    cs.draw(fish1, win) 
    cs.draw(fish2, win) 
    cs.draw(fish3, win) 
    cs.draw(fish4, win) 
  
  
    # this loop helps animate csmplex shapes created using range 100 
    for i in range(50): 
        if win.checkMouse() != None:  
            break 
        elif win.checkKey() == 'q': 
            break 
        cs.animate_man(man, i, win) # moves the man back and forth 
        cs.animate_fish(fish, i, win)# adds animation to the 1st fish 
        cs.animate_fish1(fish1, i, win)# adds animation to the 2nd fish  
        cs.animate_fish2(fish2, i, win)# adds animation to the 3rd fish 
        cs.animate_fish3(fish3, i, win)# adds animation to the 3rd fish 
        cs.animate_fish4(fish4, i, win)# adds animation to the 3rd fish 

  
        win.update() # at each iteration the window has to update 
        time.sleep(0.1) # tells the loop to pause for a tenth of a secsnd, meaning that ten loops is roughly one secsnd of animation time. 
  
    # pause until user gets mouse 
    # c.undraw() 
  

    # wait for a mouse click 
    win.getMouse() 
    # close the window 
    win.close() 
  
if __name__ == "__main__": 
    scene( sys.argv) 
 