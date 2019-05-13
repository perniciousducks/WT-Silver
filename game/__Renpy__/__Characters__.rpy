
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
    centered = Character("", what_style="centered_text", window_style="centered_window")
    vcentered = Character("", what_style="centered_vtext", window_style="centered_window")
    
    #Genie
    m = Character(None, image=Image("characters/genie/mage.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g = Character(None, image=Image("characters/genie/mage2.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g2 = Character(None, image=Image("characters/genie/mage3.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g4 = Character(None, image=Image("characters/genie/mage4.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g5 = Character(None, image=Image("characters/genie/mage5.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g6 = Character(None, image=Image("characters/genie/mage6.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g7 = Character(None, image=Image("characters/genie/mage7.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g8 = Character(None, image=Image("characters/genie/mage8.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g9 = Character(None, image=Image("characters/genie/mage9.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g10 = Character(None, image=Image("characters/genie/mage10.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g11 = Character(None, image=Image("characters/genie/mage11.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g12 = Character(None, image=Image("characters/genie/mage12.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g13 = Character(None, image=Image("characters/genie/mage13.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g14 = Character(None, image=Image("characters/genie/mage14.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")
    g15 = Character(None, image=Image("characters/genie/mage15.png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")

    #Snape      #ToDo replace those screens with the normal head sprite positions.
    sna_ = [""]
    for i in xrange(1,26):
        sna_.append("")
        sna_[i] = Character("Severus Snape", image=Image("characters/snape/head/head_" + str(i) + ".png", xalign=1.0, yalign=0.0),  show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")

    #Dumbledore
    dum_ = [""]
    for i in xrange(1,6):
        dum_.append("")
        dum_[i] = Character(None, image=Image("characters/misc/dumbledore/dum_"+str(i)+".png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")

    #Santa
    san_ = [""]
    for i in xrange(1,7):
        san_.append("")
        san_[i] = Character("Santa", image=Image("characters/misc/santa/santa_"+str(i)+".png", xpos=20, yalign=1.0),  ctc="ctc3", ctc_position="fixed")

    ### STUDENTS ###
    her  = Character('[hermione_name]', ctc="ctc3", ctc_position="fixed")
    lun  = Character('Luna',  ctc="ctc3", ctc_position="fixed")
    cho  = Character('Cho',  ctc="ctc3", ctc_position="fixed")
    sus  = Character('Susan',  ctc="ctc3", ctc_position="fixed")
    ast  = Character('Astoria',  ctc="ctc3", ctc_position="fixed")
    twi  = Character('Fred and George', show_side_image=Image("characters/misc/weasley_twins/base_01.png", xalign=1.0, yalign=1.0), ctc="ctc3", ctc_position="fixed")
    fre  = Character('Fred', ctc="ctc3", show_side_image=Image("characters/misc/weasley_twins/fred_01.png", xalign=1.0, yalign=1.0), ctc_position="fixed")
    ger  = Character('George', ctc="ctc3", show_side_image=Image("characters/misc/weasley_twins/george_01.png", xalign=1.0, yalign=1.0), ctc_position="fixed")

    ### TEACHERS ###
    sna  = Character('Severus Snape', ctc="ctc3", ctc_position="fixed")
    ton  = Character('Tonks',  ctc="ctc3", ctc_position="fixed")
    spo  = Character('Professor Sprout',  ctc="ctc3", ctc_position="fixed")

    ### Other Characters ###
    hat  = Character('Sorting Hat',  ctc="ctc3", show_side_image=Image("characters/misc/hat/hat.png", xalign=1.0, yalign=1.0), ctc_position="fixed")
    helf = Character("House-Elf", ctc="ctc3", ctc_position="fixed")
    nar = Character('Narrator', show_side_image=Image("characters/misc/dumbledore/dum_narritor.png", xalign=0, yalign=1.0), ctc="ctc3", ctc_position="fixed")
    sil = Character('Team Silver', show_side_image=Image("characters/misc/dumbledore/dum_narritor.png", xalign=0, yalign=1.0), ctc="ctc3", ctc_position="fixed")

    maf  = Character('Madam Mafkin',  ctc="ctc3", show_side_image=Image("characters/misc/mafkin/maf_1.png", xalign=1.0, yalign=1.0), ctc_position="fixed")
    abe  = Character('Aberforth',  ctc="ctc3", ctc_position="fixed")
    myr  = Character('Moaning Myrtle',  ctc="ctc3", ctc_position="fixed")
    vol  = Character('Lord Voldemort',  ctc="ctc3", ctc_position="fixed")
    faw  = Character('Fawkes', color="#f21111", ctc="ctc3", ctc_position="fixed")

    fem  = Character('Female Student',  ctc="ctc3", ctc_position="fixed")
    mal  = Character('Male Student # 1',  ctc="ctc3", ctc_position="fixed")
    mal2 = Character('Male Student # 2',  ctc="ctc3", ctc_position="fixed")
    sly1 = Character('Slytherin student',  ctc="ctc3", ctc_position="fixed")
    sly2 = Character('Another Slytherin student',  ctc="ctc3", ctc_position="fixed")
    qcr  = Character('Quidditch Crowd',  ctc="ctc3", ctc_position="fixed")