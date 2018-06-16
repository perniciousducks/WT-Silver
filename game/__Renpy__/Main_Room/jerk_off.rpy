label jerk_off:

    $ d_flag_01 = False #Jasmine
    $ d_flag_02 = False #Lara
    $ d_flag_03 = False #


    if i_of_iv <= 2:
        $ d_flag_01 = True
    else:
        $ d_flag_02 = True
        
#    $ cum_on_panties = True #True when choose to cum on Hermione's panties.
#    m "Hm... Who shall be my target?"
#    menu:
#        "\"Princess Jasmine!\"":
#            m "Yes, the princess... That dirty slut!"
#            $ jerking_off_to_jasmine = True #Princess Jasmine has been chosen as a target for a jerk-off session
#            pass
#        "\"Lara Croft\"":
#            $ jerking_off_to_lara = True
#            pass
#        "-Cancel-":
#            jump desk

    hide screen bld1
    hide screen genie
    call gen_chibi("jerking_off_behind_desk") from _call_gen_chibi_61
    with d3
    pause 1
    
    call bld from _call_bld_98
    m "How should I finish this thing?"
    
    label how_to_finish:
    menu:
        "{color=#858585}...(LOCKED)...{/color}" if not hg_ps_PantyThief_OBJ.inProgress:
            ">You lack the item required for this option."
            jump  how_to_finish
        "-Hermione's panties-" if hg_ps_PantyThief_OBJ.inProgress:
            $ cum_on_panties = True #True when choose to cum on Hermione's panties.
        "-On the floor!-":
            $ cum_on_panties = False #TRUE when chosen to cum on the floor.

### JERKING OFF ###
hide screen bld1
show screen blktone
call nar(">You decide to spend some time by jerking off...") from _call_nar_489
pause.5

if d_flag_01 and not cum_on_panties:
    call nar(">You fantasize about Princess Jasmine...") from _call_nar_490
if d_flag_02 and not cum_on_panties:
    call nar(">You fantasize about Lara Croft...") from _call_nar_491
if cum_on_panties:
    call nar(">You fantasize about Hermione...") from _call_nar_492
    
g4 "Yes... that's a good slut!"
pause.5

call nar(">You are ready to cum...") from _call_nar_493
pause.2

if d_flag_01 and not cum_on_panties:
    g4 "Suck my almighty cock, you princess-whore!!!"
if d_flag_02 and not cum_on_panties:
    g4 "Suck my almighty cock, you whore!!!"
if cum_on_panties:
    g4 "Suck my almighty cock, you little whore!!!"

hide screen blktone
call gen_chibi("cumming_behind_desk") from _call_gen_chibi_62
with hpunch
pause 1

if not cum_on_panties:
    call nar(">You cum on the floor.") from _call_nar_494
if cum_on_panties:
    $ hg_ps_PantyThief_SoakedPantiesFlag = True #TRUE when you have the panties in your possession (before you return them to Hermione).
    call nar(">You cum all over Hermione's panties, and then use them to wipe the cum off the floor...") from _call_nar_495
    call gen_chibi("cum_on_desk") from _call_gen_chibi_63
    pause.5
    
    call nar(">You received the item: \"Cum-soaked panties\".") from _call_nar_496

call gen_chibi("cum_on_desk") from _call_gen_chibi_64
pause.2

call bld from _call_bld_99
m "..."
m "This was a pretty sweet jerk-off session..."
m "Back to being productive!"
    
### SETTING ALL THE FLAGS BACK TO DEFAULT ###
$ d_flag_01 = False
$ d_flag_02 = False
$ d_flag_03 = False
$ cum_on_panties = False #True when choose to cum on Hermione's panties.

hide screen genie_jerking_sperm_02
call gen_chibi("hide") from _call_gen_chibi_65
show screen genie
hide screen bld1

if daytime:
    jump night_start
else: 
    jump day_start
