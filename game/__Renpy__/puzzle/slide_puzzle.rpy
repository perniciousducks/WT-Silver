label start_slide_puzzle:
    $ imagepuzzle = [["images/room_of_requirement/puzzle/puzzle_part_"+str((y+1)+(4*(x)))+".png" for x in range(0,4)] for y in range(0,4)] 
    $ imagepuzzle[3][3] = "empty"
    $ emptyposition = 15
    hide screen gridmissing
    show screen puzzle_board
    $renpy.log("test")
    $ _return = ui.interact()
    hide screen puzzle_board
    $ move = _return;
       
        
    jump update_puzzle_slide
        
    
label update_puzzle_slide:
    $xposS = int(move/4)
    $yposS = int(move%4)
    $xposE = int(emptyposition/4)
    $yposE = int(emptyposition%4)
    
    if (((xposS == xposE-1 or xposS == xposE+1) and yposS == yposE) or ((yposS == yposE-1 or yposS == yposE+1) and xposS == xposE)):
        $imagepuzzle[xposE][yposE] = imagepuzzle[xposS][yposS]
        $imagepuzzle[xposS][yposS] = "empty"
        $ emptyposition = move
    
    show screen puzzle_board
    $ move = ui.interact() 
    hide screen puzzle_board
    jump update_puzzle_slide
    
screen puzzle_board:
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
                        xpos 21+94*x 
                        ypos 25+94*y 
                        xmargin 0
                        ymargin 0
                        action Return((y)+(4*(x)))
                        
        add "images/room_of_requirement/puzzle/grid.png"          
    zorder 8