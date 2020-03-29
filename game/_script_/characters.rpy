
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

    with trans

    helf "[text]"

    return

# Narrator (not the same as 'nar' character)
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

# Characters

# Add to character store to avoid name conflict with Doll instance
define character.cho = Character('[cho_name]')

init python:

    # Genie
    gen = Character('Genie')
    m = Character("Genie")
    g2 = Character("Genie")
    g3 = Character("Genie")
    g4 = Character("Genie")
    g5 = Character("Genie")
    g6 = Character("Genie")
    g7 = Character("Genie")
    g8 = Character("Genie")
    g9 = Character("Genie")
    g10 = Character("Genie")
    g11 = Character("Genie")
    g12 = Character("Genie")
    g13 = Character("Genie")
    g14 = Character("Genie")
    g15 = Character("Genie")
    g16 = Character("Genie")

    # Dumbledore
    dum_ = [""]
    for i in xrange(1,6):
        dum_.append("")
        dum_[i] = Character("Dumbledore")

    # Santa
    san_ = [""]
    for i in xrange(1,7):
        san_.append("")
        san_[i] = Character("Santa")

    # Students
    her = Character('[hermione_name]')
    lun = Character('[lun_name]')
    sus = Character('[susan_name]')
    ast = Character('[astoria_name]')
    twi = Character('Fred and George')
    fre = Character('Fred')
    ger = Character('George')

    # Teachers
    sna = Character('Severus Snape')
    ton = Character('[tonks_name]')
    spo = Character('Professor Sprout')
    hoo = Character('Madam Hooch')

    # Other characters
    hat = Character('Sorting Hat')
    helf = Character("House-Elf")
    nar = Character('Narrator')
    sil = Character('Team Silver')

    malf = Character('Malfoy')
    cra = Character('Crabbe')
    goy = Character('Goyle')

    maf = Character('Madam Mafkin')
    abe = Character('Aberforth')
    myr = Character('Moaning Myrtle')
    vol = Character('Lord Voldemort')
    faw = Character('Fawkes', color="#f21111")

    fem = Character('Female Student')
    mal = Character('Male Student')
    mal2 = Character('Another Male Student')
    sly1 = Character('Slytherin student')
    sly2 = Character('Another Slytherin student')
    qcr = Character('Quidditch Crowd')
    who = Character('Female voice')
    whom = Character('Male voice')
    who2 = Character('???')
