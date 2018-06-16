
## Random Mood Expressions for Her_Main ##
############################################

## Neutral ##
label her_main_rndm_neutral: #01(06,45,52), 03,54,82,84,(198),201 #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","base","base") from _call_her_main_2449 #default look #01,06,45 and 52 are exactly the same!
    elif rndm_one_of_six == 2:
        call her_main("","normal","base") from _call_her_main_2450 #
    elif rndm_one_of_six == 3:
        call her_main("","base","baseL") from _call_her_main_2451 #
    elif rndm_one_of_six == 4:
        call her_main("","annoyed","base") from _call_her_main_2452 #
    elif rndm_one_of_six == 5:
        call her_main("","base","closed") from _call_her_main_2453 #
    elif rndm_one_of_six == 6:
        call her_main("","annoyed","baseL") from _call_her_main_2454 #
    return


## Happy ##
label her_main_rndm_happy: #01(06,45,52), 53,54,68,74,84 #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","base","base") from _call_her_main_2455 #default look #01,06,45 and 52 are exactly the same!
    elif rndm_one_of_six == 2:
        call her_main("","base","squint") from _call_her_main_2456 #sly. naughty
    elif rndm_one_of_six == 3:
        call her_main("","base","baseL") from _call_her_main_2457 #look left
    elif rndm_one_of_six == 4:
        call her_main("","grin","baseL") from _call_her_main_2458 #smile, look left
    elif rndm_one_of_six == 5:
        call her_main("","base","happyCl") from _call_her_main_2459 #happy eyes
    elif rndm_one_of_six == 6:
        call her_main("","base","closed") from _call_her_main_2460 #confident, look down
    return


## Naughty ##
label her_main_rndm_naughty: #58,59,78,106,111,124,128,129,134,136, #DONE
    $ rndm_one_of_ten = renpy.random.randint(1, 10)
    if rndm_one_of_ten == 1:
        call her_main("","base","glance") from _call_her_main_2461 #
    elif rndm_one_of_ten == 2:
        call her_main("","base","down") from _call_her_main_2462 #
    elif rndm_one_of_ten == 3:
        call her_main("","base","ahegao_raised") from _call_her_main_2463 #
    elif rndm_one_of_ten == 4:
        call her_main("","grin","ahegao") from _call_her_main_2464 #
    elif rndm_one_of_ten == 5:
        call her_main("","smile","angry") from _call_her_main_2465 #
    elif rndm_one_of_ten == 6:
        call her_main("","base","down") from _call_her_main_2466 #
    elif rndm_one_of_ten == 7:
        call her_main("","base","glance") from _call_her_main_2467 #
    elif rndm_one_of_ten == 8:
        call her_main("","base","suspicious") from _call_her_main_2468 #
    elif rndm_one_of_ten == 9:
        call her_main("","silly","ahegao") from _call_her_main_2469 #
    elif rndm_one_of_ten == 10:
        call her_main("","grin","ahegao") from _call_her_main_2470 #
    return


## Naughty w/ Blush ##
label her_main_rndm_naughty_wBlush: #188,200,205,209,213 #DONE
    $ rndm_one_of_five = renpy.random.randint(1, 5)
    if rndm_one_of_five == 1:
        call her_main("","base","baseL",cheeks="blush") from _call_her_main_2471 #look left #+
    elif rndm_one_of_five == 2:
        call her_main("","soft","baseL",cheeks="blush") from _call_her_main_2472 #shy + look left #+
    elif rndm_one_of_five == 3:
        call her_main("","base","ahegao_raised",cheeks="blush") from _call_her_main_2473 #eyes rolled up #+
    elif rndm_one_of_five == 4:
        call her_main("","grin","wink",cheeks="blush") from _call_her_main_2474 #wink + smile #+
    elif rndm_one_of_five == 5:
        call her_main("","base","ahegao_raised",cheeks="blush") from _call_her_main_2475 #naughty #+
    return


## Annoyed ##
label her_main_rndm_annoyed: #12,50,61,69,79(81),83,103,185, #DONE
    $ rndm_one_of_eight = renpy.random.randint(1, 8)
    if rndm_one_of_eight == 1:
        call her_main("","annoyed","angryL") from _call_her_main_2476 #
    elif rndm_one_of_eight == 2:
        call her_main("","annoyed","annoyed") from _call_her_main_2477 #
    elif rndm_one_of_eight == 3:
        call her_main("","annoyed","angry") from _call_her_main_2478 #
    elif rndm_one_of_eight == 4:
        call her_main("","annoyed","angryL") from _call_her_main_2479 #
    elif rndm_one_of_eight == 5:
        call her_main("","annoyed","annoyed") from _call_her_main_2480 #eyes closed
    elif rndm_one_of_eight == 6:
        call her_main("","annoyed","closed") from _call_her_main_2481 #grumpy, look left
    elif rndm_one_of_eight == 7:
        call her_main("","annoyed","angryL") from _call_her_main_2482 #annoyed
    elif rndm_one_of_eight == 8:
        call her_main("","annoyed","annoyed") from _call_her_main_2483 #annoyed
    return


## Annoyed w/ Blush ##
label her_main_rndm_annoyed_wBlush: #182b,184b,191,199,203,208b #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","upset","worriedCl",cheeks="blush") from _call_her_main_2484 #embarrased, eyes closed
    elif rndm_one_of_six == 2:
        call her_main("","annoyed","closed",cheeks="blush") from _call_her_main_2485 #eyes closed
    elif rndm_one_of_six == 3:
        call her_main("","angry","angry",cheeks="blush") from _call_her_main_2486 #angry
    elif rndm_one_of_six == 4:
        call her_main("","disgust","down_raised",cheeks="blush") from _call_her_main_2487 #embarrased, look down
    elif rndm_one_of_six == 5:
        call her_main("","annoyed","angryL",cheeks="blush") from _call_her_main_2488 #annoyed smirk + look left
    elif rndm_one_of_six == 6:
        call her_main("","angry","worriedCl",cheeks="blush") from _call_her_main_2489 #embarrased
    return


## Angry ##
label her_main_rndm_angry: #05,07,09,12,47(49), 77, #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","angry","angry") from _call_her_main_2490 #
    elif rndm_one_of_six == 2:
        call her_main("","normal","frown") from _call_her_main_2491 #
    elif rndm_one_of_six == 3:
        call her_main("","annoyed","frown") from _call_her_main_2492 #
    elif rndm_one_of_six == 4:
        call her_main("","annoyed","angryL") from _call_her_main_2493 #
    elif rndm_one_of_six == 5:
        call her_main("","angry","angry") from _call_her_main_2494 #same as 49
    elif rndm_one_of_six == 6:
        call her_main("","angry","angry") from _call_her_main_2495 #
    return


## Angry w/ Blush ##
label her_main_rndm_angry_wBlush: #187,191,207,209,213, #DONE
    $ rndm_one_of_five = renpy.random.randint(1, 5)
    if rndm_one_of_five == 1:
        call her_main("","angry","angry",cheeks="blush") from _call_her_main_2496 #angry + teeth
    elif rndm_one_of_five == 2:
        call her_main("","angry","angry",cheeks="blush") from _call_her_main_2497 #angry + teeth
    elif rndm_one_of_five == 3:
        call her_main("","mad","angry",cheeks="blush") from _call_her_main_2498 #angry + teeth
    elif rndm_one_of_five == 4:
        call her_main("","grin","wink",cheeks="blush") from _call_her_main_2499 #wink + smile
    elif rndm_one_of_five == 5:
        call her_main("","base","ahegao_raised",cheeks="blush") from _call_her_main_2500 #naughty
    return