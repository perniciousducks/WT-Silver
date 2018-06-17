
## Random Mood Expressions for Her_Main ##
############################################

## Neutral ##
label her_main_rndm_neutral: #01(06,45,52), 03,54,82,84,(198),201 #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","base","base") #01,06,45 and 52 are exactly the same!
    elif rndm_one_of_six == 2:
        call her_main("","normal","base") #
    elif rndm_one_of_six == 3:
        call her_main("","base","baseL") #
    elif rndm_one_of_six == 4:
        call her_main("","annoyed","base") #
    elif rndm_one_of_six == 5:
        call her_main("","base","closed") #
    elif rndm_one_of_six == 6:
        call her_main("","annoyed","baseL") #
    return


## Happy ##
label her_main_rndm_happy: #01(06,45,52), 53,54,68,74,84 #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","base","base") #01,06,45 and 52 are exactly the same!
    elif rndm_one_of_six == 2:
        call her_main("","base","squint") #sly. naughty
    elif rndm_one_of_six == 3:
        call her_main("","base","baseL") #look left
    elif rndm_one_of_six == 4:
        call her_main("","grin","baseL") #smile, look left
    elif rndm_one_of_six == 5:
        call her_main("","base","happyCl") #happy eyes
    elif rndm_one_of_six == 6:
        call her_main("","base","closed") #confident, look down
    return


## Naughty ##
label her_main_rndm_naughty: #58,59,78,106,111,124,128,129,134,136, #DONE
    $ rndm_one_of_ten = renpy.random.randint(1, 10)
    if rndm_one_of_ten == 1:
        call her_main("","base","glance") #
    elif rndm_one_of_ten == 2:
        call her_main("","base","down") #
    elif rndm_one_of_ten == 3:
        call her_main("","base","ahegao_raised") #
    elif rndm_one_of_ten == 4:
        call her_main("","grin","ahegao") #
    elif rndm_one_of_ten == 5:
        call her_main("","smile","angry") #
    elif rndm_one_of_ten == 6:
        call her_main("","base","down") #
    elif rndm_one_of_ten == 7:
        call her_main("","base","glance") #
    elif rndm_one_of_ten == 8:
        call her_main("","base","suspicious") #
    elif rndm_one_of_ten == 9:
        call her_main("","silly","ahegao") #
    elif rndm_one_of_ten == 10:
        call her_main("","grin","ahegao") #
    return


## Naughty w/ Blush ##
label her_main_rndm_naughty_wBlush: #188,200,205,209,213 #DONE
    $ rndm_one_of_five = renpy.random.randint(1, 5)
    if rndm_one_of_five == 1:
        call her_main("","base","baseL",cheeks="blush") #+
    elif rndm_one_of_five == 2:
        call her_main("","soft","baseL",cheeks="blush") #+
    elif rndm_one_of_five == 3:
        call her_main("","base","ahegao_raised",cheeks="blush") #+
    elif rndm_one_of_five == 4:
        call her_main("","grin","wink",cheeks="blush") #+
    elif rndm_one_of_five == 5:
        call her_main("","base","ahegao_raised",cheeks="blush") #+
    return


## Annoyed ##
label her_main_rndm_annoyed: #12,50,61,69,79(81),83,103,185, #DONE
    $ rndm_one_of_eight = renpy.random.randint(1, 8)
    if rndm_one_of_eight == 1:
        call her_main("","annoyed","angryL") #
    elif rndm_one_of_eight == 2:
        call her_main("","annoyed","annoyed") #
    elif rndm_one_of_eight == 3:
        call her_main("","annoyed","angry") #
    elif rndm_one_of_eight == 4:
        call her_main("","annoyed","angryL") #
    elif rndm_one_of_eight == 5:
        call her_main("","annoyed","annoyed") #eyes closed
    elif rndm_one_of_eight == 6:
        call her_main("","annoyed","closed") #grumpy, look left
    elif rndm_one_of_eight == 7:
        call her_main("","annoyed","angryL") #annoyed
    elif rndm_one_of_eight == 8:
        call her_main("","annoyed","annoyed") #annoyed
    return


## Annoyed w/ Blush ##
label her_main_rndm_annoyed_wBlush: #182b,184b,191,199,203,208b #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","upset","worriedCl",cheeks="blush") #embarrased, eyes closed
    elif rndm_one_of_six == 2:
        call her_main("","annoyed","closed",cheeks="blush") #eyes closed
    elif rndm_one_of_six == 3:
        call her_main("","angry","angry",cheeks="blush") #angry
    elif rndm_one_of_six == 4:
        call her_main("","disgust","down_raised",cheeks="blush") #embarrased, look down
    elif rndm_one_of_six == 5:
        call her_main("","annoyed","angryL",cheeks="blush") #annoyed smirk + look left
    elif rndm_one_of_six == 6:
        call her_main("","angry","worriedCl",cheeks="blush") #embarrased
    return


## Angry ##
label her_main_rndm_angry: #05,07,09,12,47(49), 77, #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","angry","angry") #
    elif rndm_one_of_six == 2:
        call her_main("","normal","frown") #
    elif rndm_one_of_six == 3:
        call her_main("","annoyed","frown") #
    elif rndm_one_of_six == 4:
        call her_main("","annoyed","angryL") #
    elif rndm_one_of_six == 5:
        call her_main("","angry","angry") #same as 49
    elif rndm_one_of_six == 6:
        call her_main("","angry","angry") #
    return


## Angry w/ Blush ##
label her_main_rndm_angry_wBlush: #187,191,207,209,213, #DONE
    $ rndm_one_of_five = renpy.random.randint(1, 5)
    if rndm_one_of_five == 1:
        call her_main("","angry","angry",cheeks="blush") #angry + teeth
    elif rndm_one_of_five == 2:
        call her_main("","angry","angry",cheeks="blush") #angry + teeth
    elif rndm_one_of_five == 3:
        call her_main("","mad","angry",cheeks="blush") #angry + teeth
    elif rndm_one_of_five == 4:
        call her_main("","grin","wink",cheeks="blush") #wink + smile
    elif rndm_one_of_five == 5:
        call her_main("","base","ahegao_raised",cheeks="blush") #naughty
    return