
# House Elf
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
            with move(1.0)

        #Skip Transitions
        elif trans in ["None","none","skip"]:
            pass
        else: #for typos and preventing crashes...
            with d3

    #Default transition.
    else:
        if not wardrobe_active:
            with d3

    return



init python:
    # Character tables

    ### GENIE ### (others are in scripts.rpy)
    m = Character(None, window_left_padding=250, show_side_image=Image("characters/genie/mage.png", xpos=20, yalign=1.0), show_two_window=False, color="#402313", ctc="ctc3", ctc_position="fixed")
    g4 = Character(None, window_left_padding=250, show_side_image=Image("characters/genie/mage4.png", xpos=20, yalign=1.0), show_two_window=False, color="#402313", ctc="ctc3", ctc_position="fixed")
    g9 = Character(None, window_left_padding=250, show_side_image=Image("characters/genie/mage9.png", xpos=20, yalign=1.0), show_two_window=False, color="#402313", ctc="ctc3", ctc_position="fixed")

    ### House-Elf ###
    helf = Character("House-Elf", window_left_padding=250, show_two_window=False, color="#402313", ctc="ctc3", ctc_position="fixed")

    ### SNAPE HEAD ###
    sna_ = [""] #Please don't use this screen! Use 'call sna_head' instead!
    for i in range(1,26):
        sna_.append("")
        sna_[i] = Character("Severus Snape", color="#402313", show_side_image=Image("characters/snape/head/head_" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")


    ### HERMIONE HEAD (OLD) ###
    her_ = [""] #Please don't use this screen! Use 'call her_head' instead!
    for i in range(1,43):
        her_.append("")
        her_[i] = Character('[hermione_name]', color="#402313", window_left_padding=250, window_right_padding=270, show_side_image=Image("images/15_hermione_head/" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")


    ### DUMBLEDORE HEAD ###
    dum_ = [""]
    for i in range(1,6):
        dum_.append("")
        dum_[i] = Character(None, window_left_padding=250, color="#402313", show_side_image=Image("characters/dumbledore/dum_"+str(i)+".png", xpos=20, yalign=1.0), show_two_window=False, ctc="ctc3", ctc_position="fixed")



    ### STUDENTS ###
    her  = Character('[hermione_name]', color="#402313", window_left_padding=250, show_two_window=True, ctc="ctc3", ctc_position="fixed", window_right_padding=250)
    her2 = Character('[hermione_name]', color="#402313", window_right_padding=270, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).
    lher = Character('Hermini', color="#402313", window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed", window_right_padding=250)
    herA = Character('Prude Hermione', color="#402313", window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed", window_right_padding=250)

    lun  = Character('Luna', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cho  = Character('Cho', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sus  = Character('Susan', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ast  = Character('Astoria', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")

    twi  = Character('Fred and George', color="#402313", show_two_window=True, show_side_image=Image("characters/weasley_twins/base_01.png", xalign=1.0, yalign=1.0), ctc="ctc3", ctc_position="fixed", window_right_padding=100)
    fre  = Character('Fred', color="#402313", show_two_window=True, ctc="ctc3", show_side_image=Image("characters/weasley_twins/fred_01.png", xalign=1.0, yalign=1.0), ctc_position="fixed", window_right_padding=250)
    ger  = Character('George', color="#402313", show_two_window=True, ctc="ctc3", show_side_image=Image("characters/weasley_twins/george_01.png", xalign=1.0, yalign=1.0), ctc_position="fixed", window_right_padding=250)



    ### TEACHERS ###
    sna  = Character('Severus Snape', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sna  = Character('Severus Snape', color="#402313", window_right_padding=270, show_two_window=True, ctc="ctc3", ctc_position="fixed")  #Text box used for "head only" speech. (Because it has padding).
    ton  = Character('Tonks', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")

    spo  = Character('Professor Sprout', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    hoo  = Character('Madam Hooch', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    hat  = Character('Sorting Hat', color="#402313", show_two_window=True, ctc="ctc3", show_side_image=Image("characters/misc/hat/hat.png", xalign=1.0, yalign=1.0), ctc_position="fixed", window_right_padding=250)
    msp  = Character('Genie', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")



    ### Other Characters ###
    s = Character(None, color="#402313", ctc="ctc3", ctc_position="fixed")
    nar = Character('Narrator ', show_two_window=True, window_left_padding=250, show_side_image=Image("characters/dumbledore/dum_narritor.png", xalign=0, yalign=1.0), color="#402313", ctc="ctc3", ctc_position="fixed")

    maf  = Character('Madam Mafkin', color="#402313", show_two_window=True, ctc="ctc3", show_side_image=Image("characters/mafkin/maf_1.png", xalign=1.0, yalign=1.0), ctc_position="fixed", window_right_padding=270)
    abe  = Character('Aberforth', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    myr  = Character('Moaning Myrtle', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    vol  = Character('Lord Voldemort', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    faw  = Character('Fawkes', color="#f21111", window_right_padding=270, show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")

    fem  = Character('Female Student', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    mal  = Character('Male Student # 1', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    mal2 = Character('Male Student # 2', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sly1 = Character('Slytherin student', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sly2 = Character('Another Slytherin student', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ann  = Character('The Announcer', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr1  = Character('Somebody from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr2  = Character('Another voice from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")

    l    = Character('Lola', color="#402313", window_right_padding=270, show_two_window=True, ctc="ctc3", ctc_position="fixed")
    dahr = Character(None, color="#402313", window_left_padding=270, show_side_image=Image("images/store/dahr.png", xalign=0.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc4", ctc_position="fixed")
