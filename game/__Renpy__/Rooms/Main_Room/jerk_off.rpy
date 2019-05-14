label jerk_off:

    $ d_flag_01 = False #Jasmine
    $ d_flag_02 = False #Lara
    $ d_flag_03 = False #

    if i_of_iv <= 2:
        $ d_flag_01 = True
    else:
        $ d_flag_02 = True

    hide screen bld1
    hide screen genie
    call gen_chibi("jerking_off_behind_desk")
    with d3
    pause 1

    call bld
    m "How should I finish this thing?"

    label how_to_finish:
    menu:
        "-Hermione's panties-" if hg_ps_get_panties.inProgress:
            $ her_panties_soaked = True #True when choose to cum on Hermione's panties.
        "{color=#858585}...(LOCKED)...{/color}" if not hg_ps_get_panties.inProgress:
            ">You lack the item required for this option."
            jump  how_to_finish

        "-Cho's panties-" if has_cho_panties:
            $ cho_panties_soaked = True
        "{color=#858585}...(LOCKED)...{/color}" if not has_cho_panties:
            ">You lack the item required for this option."
            jump  how_to_finish

        "-On the floor!-":
            pass

### JERKING OFF ###
hide screen bld1
show screen blktone
call nar(">You decide to spend some time by jerking off...")
pause.5

if her_panties_soaked:
    call nar(">You fantasize about Hermione...")

elif cho_panties_soaked:
    call nar(">You fantasize about Cho...")

else:
    if d_flag_01:
        call nar(">You fantasize about Princess Jasmine...")
    if d_flag_02:
        call nar(">You fantasize about Lara Croft...")

g4 "Yes... that's a good slut!"
pause.5

call nar(">You are ready to cum...")
pause.2

if her_panties_soaked:
    g4 "Suck my almighty cock, you little whore!!!"

elif cho_panties_soaked:
    g4 "Suck my almighty cock, you exotic goddess!!!"

else:
    if d_flag_01:
        g4 "Suck my almighty cock, you princess-whore!!!"
    if d_flag_02:
        g4 "Suck my almighty cock, you whore!!!"

hide screen blktone
call gen_chibi("cumming_behind_desk")
with hpunch
pause 1

if her_panties_soaked:
    call nar(">You cum all over Hermione's panties, and then use them to wipe the cum off the floor...")
    call gen_chibi("cum_on_desk")
    pause.5

    $ achievement.unlock("pantiesfap")
    call nar(">You received the item: \"Cum-soaked panties\".")

elif cho_panties_soaked:
    call nar(">You cum all over Cho's panties, and then use them to wipe the cum off the floor...")
    call gen_chibi("cum_on_desk")
    pause.5

    call nar(">You received the item: \"Cum-soaked panties\".")

else:
    call nar(">You cum on the floor.")

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

hide screen genie_jerking_sperm_02
call gen_chibi("hide")
show screen genie
hide screen bld1

if daytime:
    jump night_start
else:
    jump day_start
