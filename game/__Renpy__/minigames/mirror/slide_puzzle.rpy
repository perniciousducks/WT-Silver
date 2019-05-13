label start_slide_puzzle:
    $ puzzle_tries = 0
    $ imagepuzzle = [["images/rooms/room_of_requirement/puzzle/puzzle_part_"+str((y+1)+(4*(x)))+".png" for x in range(0,4)] for y in range(0,4)]
    $ imagepuzzle[3][3] = "empty"
    python:
        for x in range(0,16):
            xposS = int(x/4)
            yposS = int(x%4)
            tempimage = imagepuzzle[xposS][yposS]
            xposE = int(((x+3)%16)/4)
            yposE = int(((x+3)%16)%4)
            imagepuzzle[xposS][yposS] = imagepuzzle[xposE][yposE]
            imagepuzzle[xposE][yposE] = tempimage
        for x in range(0,16):
            xposS = int(x/4)
            yposS = int(x%4)
            if imagepuzzle[xposS][yposS] == "empty":
                emptyposition = x

        #This is to make it solvable
        tempimage = imagepuzzle[1][0]
        imagepuzzle[1][0] = imagepuzzle[2][0]
        imagepuzzle[2][0] = tempimage
    jump update_puzzle_slide


label update_puzzle_slide:
    show screen puzzle_board
    $ p_move = ui.interact()
    hide screen puzzle_board

    if int(p_move) == -1:
        jump main_room

    $xposS = int(p_move/4)
    $yposS = int(p_move%4)
    $xposE = int(emptyposition/4)
    $yposE = int(emptyposition%4)
    $ puzzle_tries = puzzle_tries + 1

    if (((xposS == xposE-1 or xposS == xposE+1) and yposS == yposE) or ((yposS == yposE-1 or yposS == yposE+1) and xposS == xposE)):
        $imagepuzzle[xposE][yposE] = imagepuzzle[xposS][yposS]
        $imagepuzzle[xposS][yposS] = "empty"
        $ emptyposition = p_move

    if p_move == -2:
        jump open_pyzzle_box

    python:
        for x in range(0,4):
            for y in range(0,4):
                if ((imagepuzzle[y][x] != "images/rooms/room_of_requirement/puzzle/puzzle_part_"+str((y+1)+(4*(x)))+".png" and (y+1)+(4*(x)) != 16) or imagepuzzle[3][3] != "empty"):
                    renpy.jump("update_puzzle_slide")


    jump open_pyzzle_box

label open_pyzzle_box:
    if unlocked_7th or p_move == -2:
        m "Fuck it... {size=18}*Smash*{/size}"
        m "A broken bottle..."
        m "Oh well, too late now. Back to my usual-"
    elif unlocked_7th == False:
        m "Finally... "
        m "What is this?"
        m "Sweet, phoenix tears! Down the hatch we go."
        $renpy.play("sounds/pop03.mp3")
        $renpy.play("sounds/gulp.mp3")
        pause
        $renpy.play("sounds/gulp.mp3")
        m "...."
        m "I feel no difference..."
        $ achievement.unlock("puzzle")

    m "Hold on a second, there's a book in here..."
    m "Seems to be some sort of notebook, I'll skim through it....."
    hide screen chair_right
    hide screen genie
    show screen reading
    with Dissolve(0.3)
    m "My dear phoenix has been losing his feathers lately, I think it's time soon..... "
    m "*Time for what?*"
    m "That Potter boy is mighty cute, looks just like his father.... "
    g9 "*Well, well....*"
    m "Severus gave me a weird look today, I wonder what he thinks about my......"
    g4 "*This is all trash...*"
    m "*Wait a minute.... this seems interesting.*"
    m "I was walking around in the seventh floor corridor looking for a bathroom..."
    m "Whilst searching, a room that I had never seen before appeared, filled with chamber pots... But when I returned later, it was gone."
    m "* I've seen enough magic to know where this is going... I should investigate that corridor on the seventh floor.*"
    show screen chair_right
    show screen genie
    hide screen reading
    with Dissolve(0.3)
    call give_reward("You've unlocked something on the 7th floor, check your map to get there.","/interface/icons/head/head_genie_question_mark.png")
    $ unlocked_7th = True
    if deck_unlocked:
        m "What's this?"
        call give_reward("You have found a card on the bottom of the box!", "images/cardgame/t1/other/elf_v1.png")
    $ unlocked_cards += [card_item_elf]
    jump main_room

screen puzzle_board():

    use close_button(close_var=lambda : -1)

    if puzzle_tries > 150:
        imagebutton:
            xpos 240
            ypos 100
            idle "interface/slide/fuck.png"
            hover "interface/slide/fuck_hover.png"
            action Return(-2)

    frame:
        background #00000000
        xalign 0.5
        yalign 0.5
        xsize 425
        ysize 425

        add "images/rooms/room_of_requirement/puzzle/lock.png"

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
