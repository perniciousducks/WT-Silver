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
    call gen_chibi("jerking_off_behind_desk") 
    with d3
    pause 1
    
    call bld 
    m "How should I finish this thing?"
    
    label how_to_finish:
    menu:
        "{color=#858585}...(LOCKED)...{/color}" if not hg_ps_get_panties_OBJ.inProgress:
            ">You lack the item required for this option."
            jump  how_to_finish
        "-Hermione's panties-" if hg_ps_get_panties_OBJ.inProgress:
            $ cum_on_panties = True #True when choose to cum on Hermione's panties.
        "-On the floor!-":
            $ cum_on_panties = False #TRUE when chosen to cum on the floor.

### JERKING OFF ###
hide screen bld1
show screen blktone
call nar(">You decide to spend some time by jerking off...") 
pause.5

if d_flag_01 and not cum_on_panties:
    call nar(">You fantasize about Princess Jasmine...") 
if d_flag_02 and not cum_on_panties:
    call nar(">You fantasize about Lara Croft...") 
if cum_on_panties:
    call nar(">You fantasize about Hermione...") 
    
g4 "Yes... that's a good slut!"
pause.5

call nar(">You are ready to cum...") 
pause.2

if d_flag_01 and not cum_on_panties:
    g4 "Suck my almighty cock, you princess-whore!!!"
if d_flag_02 and not cum_on_panties:
    g4 "Suck my almighty cock, you whore!!!"
if cum_on_panties:
    g4 "Suck my almighty cock, you little whore!!!"

hide screen blktone
call gen_chibi("cumming_behind_desk") 
with hpunch
pause 1

if not cum_on_panties:
    call nar(">You cum on the floor.") 
if cum_on_panties:
    $ hg_SoakedPantiesFlag = True #TRUE when you have the panties in your possession (before you return them to Hermione).
    call nar(">You cum all over Hermione's panties, and then use them to wipe the cum off the floor...") 
    call gen_chibi("cum_on_desk") 
    pause.5
    
    call nar(">You received the item: \"Cum-soaked panties\".") 

call gen_chibi("cum_on_desk") 
pause.2

call bld 
m "..."
m "This was a pretty sweet jerk-off session..."
m "Back to being productive!"
    
### SETTING ALL THE FLAGS BACK TO DEFAULT ###
$ d_flag_01 = False
$ d_flag_02 = False
$ d_flag_03 = False
$ cum_on_panties = False #True when choose to cum on Hermione's panties.

hide screen genie_jerking_sperm_02
call gen_chibi("hide") 
show screen genie
hide screen bld1

if daytime:
    jump night_start
else:
    $ achievement.unlock("wanker")
    jump day_start
