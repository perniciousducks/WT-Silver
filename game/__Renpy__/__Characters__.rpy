
# House Elf
screen house_elf():
    add "characters/misc/house-elf/house-elf.png" xpos 700 ypos 200
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

#Narrator
label nar(text="",action=""):

    if action != "end": #Narration ended, blktone was already active.
        show screen blktone5
        with d3

    if text != "":
        "[text]"

    if action != "start": #Narration just started, blktone won't get hidden.
        hide screen blktone5
        with d3

    return



#Transitions
label transition(trans=None):

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
        elif trans == "move":
            with move

        #Skip Transitions
        elif trans in ["None","none","skip"]:
            pass
        else: #for typos and preventing crashes...
            with d3

    #Default transition.
    else:
        if not hide_transitions:
            with d3

    return

init python:
    ### Characters ###
    # Name has to be left empty "" otherwise quickmenu will be shown
    centered = Character(None, what_style="centered_text", window_style="centered_window")
    vcentered = Character(None, what_style="centered_vtext", window_style="centered_window")
    
    #Genie
    gen = Character('Genie')
    m = Character("", show_side_image=Image("characters/genie/mage.png"))
    g = Character("", show_side_image=Image("characters/genie/mage2.png"))
    g2 = Character("", show_side_image=Image("characters/genie/mage3.png"))
    g4 = Character("", show_side_image=Image("characters/genie/mage4.png"))
    g5 = Character("", show_side_image=Image("characters/genie/mage5.png"))
    g6 = Character("", show_side_image=Image("characters/genie/mage6.png"))
    g7 = Character("", show_side_image=Image("characters/genie/mage7.png"))
    g8 = Character("", show_side_image=Image("characters/genie/mage8.png"))
    g9 = Character("", show_side_image=Image("characters/genie/mage9.png"))
    g10 = Character("", show_side_image=Image("characters/genie/mage10.png"))
    g11 = Character("", show_side_image=Image("characters/genie/mage11.png"))
    g12 = Character("", show_side_image=Image("characters/genie/mage12.png"))
    g13 = Character("", show_side_image=Image("characters/genie/mage13.png"))
    g14 = Character("", show_side_image=Image("characters/genie/mage14.png"))
    g15 = Character("", show_side_image=Image("characters/genie/mage15.png"))

    #Snape      #ToDo replace those screens with the normal head sprite positions.
    sna_ = [""]
    for i in xrange(1,26):
        sna_.append("")
        sna_[i] = Character("Severus Snape", show_side_image=Image("characters/snape/head/head_" + str(i) + ".png"),  show_who_xalign=0.5)

    #Dumbledore
    dum_ = [""]
    for i in xrange(1,6):
        dum_.append("")
        dum_[i] = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/dum_"+str(i)+".png", xpos=20, yalign=1.0))

    #Santa
    san_ = [""]
    for i in xrange(1,7):
        san_.append("")
        san_[i] = Character("Santa", show_side_image=Image("characters/misc/santa/santa_"+str(i)+".png", xpos=20, yalign=1.0))

    ### STUDENTS ###
    her = Character('[hermione_name]')
    lun = Character('Luna')
    cho = Character('[cho_name]')
    sus = Character('Susan')
    ast = Character('Astoria')
    twi = Character('Fred and George', show_side_image=Image("characters/misc/weasley_twins/base_01.png"))
    fre = Character('Fred', show_side_image=Image("characters/misc/weasley_twins/fred_01.png"))
    ger = Character('George', show_side_image=Image("characters/misc/weasley_twins/george_01.png"))

    ### TEACHERS ###
    sna = Character('Severus Snape')
    ton = Character('Tonks')
    spo = Character('Professor Sprout')
    hoo = Character('Madam Hooch')
    ### Other Characters ###
    hat = Character('Sorting Hat', show_side_image=Image("characters/misc/hat/hat.png"))
    helf = Character("House-Elf")
    nar = Character('Narrator', show_side_image=Image("characters/misc/dumbledore/dum_narritor.png"))
    sil = Character('Team Silver', show_side_image=Image("characters/misc/dumbledore/dum_narritor.png"))

    maf = Character('Madam Mafkin', show_side_image=Image("characters/misc/mafkin/maf_1.png"))
    abe = Character('Aberforth')
    myr = Character('Moaning Myrtle')
    vol = Character('Lord Voldemort')
    faw = Character('Fawkes', color="#f21111")

    fem = Character('Female Student')
    mal = Character('Male Student # 1')
    mal2 = Character('Male Student # 2')
    sly1 = Character('Slytherin student')
    sly2 = Character('Another Slytherin student')
    qcr = Character('Quidditch Crowd')
    who = Character('Female voice')
    whom = Character('Male voice')
    who2 = Character('???')