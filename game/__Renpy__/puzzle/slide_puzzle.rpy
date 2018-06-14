label start_slide_puzzle:
    $ imagepuzzle = [["images/room_of_requirement/puzzle/puzzle_part_"+str((y+1)+(4*(x)))+".png" for x in range(0,4)] for y in range(0,4)] 
    $ imagepuzzle[3][3] = "empty"
    $ emptyposition = 15
    python:
        for x in range(0,15):
            xposS = int(x/4)
            yposS = int(x%4)
            tempimage = imagepuzzle[xposS][yposS]
            xposE = int(((x+3)%15)/4)
            yposE = int(((x+3)%15)%4)
            imagepuzzle[xposS][yposS] = imagepuzzle[xposE][yposE]
            imagepuzzle[xposE][yposE] = tempimage
    jump update_puzzle_slide
        
      
label update_puzzle_slide:  
    show screen puzzle_board
    $ move = ui.interact() 
    hide screen puzzle_board    
        
    if move == -1:
        jump cupboard 
        
    $xposS = int(move/4)
    $yposS = int(move%4)
    $xposE = int(emptyposition/4)
    $yposE = int(emptyposition%4)
    
    if (((xposS == xposE-1 or xposS == xposE+1) and yposS == yposE) or ((yposS == yposE-1 or yposS == yposE+1) and xposS == xposE)):
        $imagepuzzle[xposE][yposE] = imagepuzzle[xposS][yposS]
        $imagepuzzle[xposS][yposS] = "empty"
        $ emptyposition = move

    python:
        for x in range(0,4):
            for y in range(0,4):
                if ((imagepuzzle[y][x] != "images/room_of_requirement/puzzle/puzzle_part_"+str((y+1)+(4*(x)))+".png" and (y+1)+(4*(x)) != 16) or imagepuzzle[3][3] != "empty"):
                    renpy.jump("update_puzzle_slide")
    
    #do stuff when finish
    m "Finally... Sweet, phoenix tears! Down the hatch we go."
    #sound effect needet
    m "...."
    m "I feel no difference..."
    m "Hold on a minute there's a book/notes in here..."
    # implement popup
    jump cupboard
 
        
    
screen puzzle_board:
    imagebutton: # X
        xpos 1013
        ypos 13
        idle "interface/map/close_ground.png"
        hover "interface/map/close_hover.png"
        action Return(-1)
        
    frame:
        xalign 0.5
        yalign 0.5
        xsize 425
        ysize 425
        
        add "images/room_of_requirement/puzzle/lock.png"
        
        for x in range(0,4):
            for y in range(0,4):
                $ somestring = imagepuzzle[x][y]
                if somestring != "empty":
                    imagebutton:
                        idle somestring 
                        xpos 25+94*x 
                        ypos 25+94*y 
                        xmargin 0
                        ymargin 0
                        action Return((y)+(4*(x)))
                                
    zorder 8