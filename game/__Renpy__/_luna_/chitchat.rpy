label luna_chitchat:
    #if luna_dom >= luna_sub:
    #    $ renpy.call('luna_chitdom_'+str(luna_dom)+'_'+str(renpy.random.randint(1, 3)))
    #else:
    #    $ renpy.call('luna_chitsub_'+str(luna_sub)+'_'+str(renpy.random.randint(1, 3)))
    "Work in Progress"
    return

###########################DOM RESPONSES###########################

#Dom 0 - Base level Luna
label luna_chitdom_0_1:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_1 
    return
label luna_chitdom_0_2:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_2 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_3 
    return
label luna_chitdom_0_3: 
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_4 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_5 
    return

#Dom 1 - Very Slightly Dommy
label luna_chitdom_1_1:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_6 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_7 
    return
label luna_chitdom_1_2:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_8 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_9 
    return
label luna_chitdom_1_3: 
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_10 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_11 
    return

#Dom 2 - Slightly Dommy
label luna_chitdom_2_1:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_12 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_13 
    return
label luna_chitdom_2_2:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_14 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_15 
    return
label luna_chitdom_2_3: 
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_16 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_17 
    return

#Dom 3 - Dommy
label luna_chitdom_3_1:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_18 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_19 
    return
label luna_chitdom_3_2:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_20 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_21 
    return
label luna_chitdom_3_3: 
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_22 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_23 
    return





###########################SUB RESPONSES###########################

#sub 1 - Very Slightly subby
label luna_chitsub_1_1:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_24 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_25 
    return
label luna_chitsub_1_2:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_26 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_27 
    return
label luna_chitsub_1_3: 
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_28 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_29 
    return

#sub 2 - Slightly subby
label luna_chitsub_2_1:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_30 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_31 
    return
label luna_chitsub_2_2:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_32 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_33 
    return
label luna_chitsub_2_3: 
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_34 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_35 
    return

#sub 3 - subby
label luna_chitsub_3_1:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_36 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_37 
    return
label luna_chitsub_3_2:
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_38 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_39 
    return
label luna_chitsub_3_3: 
    m "How have you been [luna_name]?"
    call luna_main("Well enough [l_genie_name]...", 8, 2, 2, 3) from _call_luna_main_40 
    call luna_main("But I could certainly be better!", 9, 1, 2, 2) from _call_luna_main_41 
    return