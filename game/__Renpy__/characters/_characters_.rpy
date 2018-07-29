### General Characters that need a speach bouble can be made here ###
screen house_elf:
    add "characters/house-elf/house-elf.png" xpos 700 ypos 200
    zorder snape_zorder

label helf_main(text="", trans=None, remove=False):
    hide screen house_elf
    show screen bld1

    if remove == True:
        pause 0.1
        return

    show screen house_elf
    show screen bld1
    
    call transition(trans)
   
    helf "[text]"

    return

label transition(trans=""):
    #Transitions
    if trans != None:         #d3 is default.
        if trans == "d1":
            with d1
        elif trans == "d3": #Default anyways.
            with d3
        elif trans == "d5":
            with d5
        elif trans == "d7":
            with d7
        elif trans == "d9":
            with d9

        elif trans == "fade":
            with fade
        elif trans == "hpunch":
            with hpunch
        elif trans == "vpunch":
            with vpunch

        #Skip Transitions
        elif trans == "none" or trans == "skip":
            pass
        else: #for typos and preventing crashes...
            with d3
            
    #Default transition.
    else:
        with d3
        
    return