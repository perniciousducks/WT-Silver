

### Intro ###

# Maybe Luna could explain what Weckspurts are,
# and Genie could suggest to her to masturbate to fight them off.
# This could be a random event to unlock the favor, instead of a menu even you start.

label ll_pf_masturbate_T1_intro:

    call play_sound("knocking")
    "*knock* *knock* *knock*"
    m "Come in..."

    call play_sound("door")
    call lun_walk("door","mid",2.5)
    pause.5

    call lun_main("Hello, [lun_genie_name]...","base","happyCl","base","mid",xpos="right",ypos="base")

    # Add section here
    "Dev note" "This section is missing writing! (ll_pf_masturbate_T1_intro)"

    # Tell her to masturbate.
    call ll_pf_masturbate_T1_start

    call lun_main("Thank you, [lun_genie_name]!","normal","seductive","sad","down")
    m "(What an odd girl.)"
    call nar(">Luna gives you one last smile before leaving your office.")

    call lun_walk("desk","leave",3)

    jump end_luna_event



### Menu Branch ###

label ll_pf_masturbate:

    if ll_pf_masturbate_OBJ.points <= 0:
        # Luna masturbates.
        jump ll_pf_masturbate_T1_E1

    elif ll_pf_masturbate_OBJ.points == 1:
        # Luna masturbates again.
        # You tell her to keep going even after she came once.
        jump ll_pf_masturbate_T1_E2

    else:
        # Has a menu branch with two options.
        # Genie jerks off on her face after she masturbated
        jump ll_pf_masturbate_T1_E3


    # End event jump
    # (only used when the event isn't called.)
    label end_luna_masturbate_event:

        if lun_whoring < 3: # Points til 3
            $ lun_whoring += 1

        if ll_pf_masturbate_OBJ.level < 3:
            $ ll_pf_masturbate_OBJ.level += 1

    # Stats
    $ ll_pf_masturbate_OBJ.points += 1

    jump end_luna_event



### Tier 1 - Event 1 ###

# Masturbate for Genie and then Genie cums on Luna's face

label ll_pf_masturbate_T1_E1:
    $ days_to_luna += renpy.random.randint(1, 2)

    call lun_main("","base","base","base","mid", xpos="mid", ypos="base")
    m "Miss Lovegood. How have you been?"
    call lun_main("Alright... but the wrackspurts seem to have come back..","upset","base","angry","R")
    m "Again? So soon?"
    call lun_main("I'm afraid so [lun_genie_name]...","normal","base","sad","mid")
    call lun_main("Everytime I think about what we did in here...","normal","wide","sad","mid")
    call lun_main("It just makes them feel so much... stronger...","normal","angry","sad","R")
    m "Yes... They must be afraid of my powerful techniques..."
    call lun_main("Do you think so?","normal","closed","sad","R")
    m "I do..."
    m "Why else would they attack you when you think about curing them?"
    call lun_main("You're right...","normal","angry","sad","mid")
    m "So... Are you ready to try and dispel them again?"
    call lun_main("Only if it's not too much trouble [lun_genie_name]... I wouldn't want to disturb you...","upset","angry","sad","R")
    m "Please, as headmaster it's my duty to make sure my students are safe..."
    call lun_main("You're right...","normal","seductive","sad","down")
    call lun_main("I just feel guilty coming up here so often...","normal","seductive","sad","R")
    m "Don't..."
    "*Luna starts grinding her thighs together.*"
    call lun_main("Ok...","base","seductive","sad","down")
    call lun_main("So, is it okay if I start scratching...","base","seductive","sad","mid")
    m "I don't see why not."
    m "Please, why don't you come a bit closer..."

    call lun_walk("mid", "desk", 2)

    # Tell her to masturbate.
    call ll_pf_masturbate_T1_start

    call lun_walk("desk", "leave", 2)

    call bld
    m "(What an odd girl.)"

    jump end_luna_masturbate_event





### Tier 1 - Event 2 ###

# Masturbate for Genie

label ll_pf_masturbate_T1_E2:
    $ days_to_luna += renpy.random.randint(1, 2)

    # Add section here
    "Dev note" "This section is missing writing! (ll_pf_masturbate_T1_E2)"

    m "Please, why don't you come a bit closer..."

    call lun_walk("mid", "desk", 2)

    # Tell her to masturbate.
    call ll_pf_masturbate_T1_start

    # Tell her to keep going.
    call ll_pf_masturbate_T1_continue

    m "Will that be all then, Miss Lovegood."
    call lun_main("I suppose... Altough I don't suppose I could go-","normal","seductive","sad","down")
    call lun_main("No...{w} I better get to bed...","upset","seductive","sad","R")
    call lun_main("Thanks again, [lun_genie_name]!","normal","seductive","sad","down")

    call lun_walk("desk", "leave", 2)

    call bld
    m "(She really is a bit loony...)"

    jump end_luna_masturbate_event



### Tier 1 - Event 3 ###

# Masturbate for Genie and then Genie cum on Luna's face

label ll_pf_masturbate_T1_E3:

    call lun_main("","base","closed","angry","mid", xpos="mid", ypos="base")
    m "[luna_name], are those wrackspurts still causing you-"

    $ luna_wear_top = False # Has to be removed because of the sleeves.
    $ luna_l_arm = 4

    call nar(">Luna quickly puts her hand down her skirt, not even waiting on your reply...")
    call lun_main("Ah... I'm sorry [lun_genie_name]... I just...{w=0.3} needed... this...{image=textheart}","base","seductive","sad","up")
    m "You seem relieved..."
    call lun_main("Ah... {image=textheart} yes...","base","wide","sad","mid")
    call lun_main("These visits are starting to become all I can think about...","base","seductive","sad","down")
    m "Hmmm...{w=0.3} Do you think that's a bad thing?"
    call lun_main("Ah...{w=0.3} of course not!","normal","happyCl","sad","R")
    call lun_main("It just...*Hngh*{w=0.3} means that it's working...","pout","base","sad","mid")
    call lun_main("If only I could spend all day up here...","base","base","sad","mid")
    m "Do you think a full day of treatment would get rid of them?"
    call lun_main("Ah...","base","base","sad","mid")
    call lun_main("Probably not...","soft","seductive","sad","mid")
    call lun_main("But...","base","wide","sad","R")
    call lun_main("Ah...","base","seductive","sad","down")
    call lun_main("I think...{w=0.3} It'd probably feel...","soft","seductive","sad","mid")
    call lun_main("Nice...{image=textheart}{image=textheart}{image=textheart}","base","seductive","sad","R")
    m "Speaking of feeling nice..."
    call lun_main("Ah...{w=0.3} I think I'm...{w=0.5} Cumming [lun_genie_name]...","open_tongue","seductive","sad","down")
    call lun_main("Ah...{image=textheart}","base","seductive","sad","mid")
    call lun_main("Mmmmm{image=textheart}","base","seductive","sad","mid")
    call lun_main("Ah...{w=0.3} I'm cumming...{image=textheart}{image=textheart}","base","wide","sad","up")
    m "Mmmmm, that's it girl..."
    call lun_main("Ah...{image=textheart}","soft","seductive","sad","down", cheeks="blush")
    call nar(">You see a flush of red roll over Luna's face as her body twitches with the throes of her orgasm.","start")
    call nar(">Her fingers keep casually stroking her needy slit...","end")
    m "It seems those wickedspots have been giving you a bit of grief now haven't they?"

    menu:
        "-Start jerking off-":
            call ll_pf_masturbate_T1_jerk_off
        "-behave-":
            call ll_pf_masturbate_T1_continue

    m "Will that be all miss lovegood?"
    lun "Oh, um.{w} Yes..."

    lun "I'll see you next time those wrackspurts come up again..."
    m "See that you do."
    lun "Yes, [lun_genie_name]..."

    call lun_walk("mid", "leave", 2)

    jump end_luna_masturbate_event



# Luna starts to masturbate.

label ll_pf_masturbate_T1_start: # Call label

    $ luna_wear_top = False # Has to be removed because of the sleeves.

    call lun_main("...","pout","base","sad","mid", xpos="mid", ypos="base", trans="fade")
    m "That's it..."
    m "Begin when you're ready Miss lovegood."

    $ luna_l_arm = 4
    call nar(">Luna quickly puts her hand down her skirt, barely waiting for you to finish your sentence...")
    call lun_main("Ah...{w=0.3} thank you [lun_genie_name]...","normal","seductive","sad","down")
    m "You seem relieved..."
    call lun_main("Ah...{w=0.3} of course... I've been waiting to come here since yesterday...","base","wide","sad","mid")
    call lun_main("I think Those slimy wrackspurts have infested the commonroom...","base","seductive","sad","down")
    m "That's quite possible..."
    call lun_main("Ah...{w=0.3} ah...","normal","happyCl","sad","R")
    call lun_main("But getting rid of them...{w=0.4} feels...{w=0.4} so...{w=0.3} so...{w=0.3} good...","pout","base","sad","mid")
    call lun_main("I'm almost glad I've got them...","pout","base","sad","mid")
    m "The positive feelings you have are your body reacting to the wickerspats being expelled from your body."
    call lun_main("Really?","base","closed","sad","R")
    call lun_main("Ah...","normal","base","sad","mid")
    call lun_main("I must...{w=0.3} ah...{w=0.3} Be expelling a lot then...","soft","seductive","sad","mid")
    call lun_main("In fact...","normal","wide","sad","R")
    call lun_main("Ah...","normal","seductive","sad","down")
    call lun_main("I think...{w=0.3} ah...{w=0.3} I'm about to...{w=0.3} ah...","pout","seductive","sad","mid")
    call lun_main("Mmmm, it's just like...{w=0.2} last time...","normal","seductive","sad","R")
    m "Oh, are you cumming already?"
    call lun_main("Cumming?","normal","seductive","sad","down")
    call lun_main("What's?{w=0.3} Ah...{image=textheart}","pout","angry","sad","mid")
    call lun_main("Cumming?{image=textheart}","normal","seductive","sad","mid")
    call lun_main("Ah...{w=0.3} I'm cumming...{image=textheart}{image=textheart}","normal","wide","sad","mid")
    m "Mmmmm that's it girl..."
    call lun_main("Ah...{image=textheart}","normal","wide","sad","down")
    call nar(">You see a flush of red roll over Luna's face as her body twitches with the throes of her orgasm.","start")
    call nar(">However despite this, her fingers remain a flurry of movement under her skirt.","end")
    m "Well, it seems those wickedspots have been giving you a fair bit of grief now haven't they?"

    return



# Luna continues to masturbate

label ll_pf_masturbate_T1_continue: # Call label

    call lun_main("Ah...{image=textheart}yes{image=textheart}","normal","seductive","raised","mid")
    m "Don't worry, that should sort them out for now..."
    call lun_main("Ummm...","base","base","sad","R")
    m "What's wrong?"
    call lun_main("...","normal","happyCl","sad","R")
    call lun_main("Is it...","upset","happyCl","sad","R")
    call lun_main("Okay if I do it once more?","normal","happyCl","sad","R")
    m "What?"
    call lun_main("If you need to do other things I can leave!","base","happyCl","sad","R")
    m "There's no need for that! You can stay here as long as you like..."
    m "I was just a little surprised that you needed to go again is all..."
    call lun_main("Ah...{w=0.3} well...","base","happyCl","base","R")
    call lun_main("These wrackspurts...","normal","happyCl","base","R")
    call lun_main("Ah...","pout","happyCl","sad","R")
    call lun_main("They've been very tiresome...","normal","happyCl","sad","R")
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("Besides...","base","happyCl","base","R")
    call nar(">Luna starts dancing her fingers along under her skirt.")
    call lun_main("Ah...","base","happyCl","sad","R")
    call lun_main("I've been... waiting for this all day...","grin","happyCl","sad","R")
    call nar(">Luna starts to softly moan under her breath.")
    call lun_main("Standing here...","base","happyCl","sad","R")
    m "..."
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","grin","happyCl","base","R")
    call lun_main("In front of my headmaster...","base","happyCl","sad","R")
    call lun_main("While he helps me to...","base","happyCl","base","R")
    m "Shhh, don't speak, just focus..."
    call lun_main("Okay...","normal","happyCl","sad","R")
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("Ah...","grin","happyCl","sad","R")
    call lun_main("{image=textheart}","base","happyCl","sad","R")
    call lun_main("...","upset","happyCl","sad","R")
    call lun_main("Ah... [lun_genie_name]...","normal","seductive","sad","mid")
    call lun_main("I think...","grin","seductive","sad","down")
    call lun_main("Ah...","grin","seductive","sad","R")
    call lun_main("I think I've almost got them...","grin","happyCl","sad","R")
    m "Shhh..."
    call lun_main("Ah...","grin","happyCl","angry","mid")
    call nar(">Luna's fingers start furiously dancing underneath her skirt.")
    call lun_main("Mmmm...","base","happyCl","angry","mid")
    call lun_main("Ah...","grin","happyCl","angry","mid")
    call lun_main("A-ah...","base","seductive","sad","down")
    call lun_main("Yes...","base","seductive","angry","mid")
    m "(I think this is it!)"
    call lun_main("Ah...{w=0.3} ah...{image=textheart}","grin","seductive","sad","R")
    call lun_main("{size=+4}Mmm...{w=0.2} Yes...{image=textheart}{/size}","base","seductive","sad","down")
    call lun_main("{size=+8}ah...{w=0.3} oh...{w=0.3} Frickity!!!{/size}","grin","seductive","sad","mid")
    call lun_main("!!!","grin","wide","sad","mid")
    call nar(">There's a blur of movement under Luna's skirt.")
    call lun_main("Ah! Thank you, [lun_genie_name]!","base","wide","sad","mid")
    call lun_main("!!!","base","wide","sad","mid")
    m "Is everything okay?"
    call lun_main("Ah...{w=0.4} yes{image=textheart} thank you{image=textheart} [lun_genie_name]...{image=textheart}","normal","seductive","sad","R")
    m "So, have the wickspots left you alone now?"
    call lun_main("I think so, [lun_genie_name]...","normal","seductive","sad","mid")
    $ luna_l_arm = 1
    call nar(">Luna slowly pulls her sopping wet hand out from under her skirt as the liquid slowly starts dripping onto the floor.")
    call lun_main("At least That nasty itch seems to have gone away.","base","base","sad","mid")
    m "Fantastic!"

    return



# You jerk off while Luna masturbates
# You end up cumming on her face...

label ll_pf_masturbate_T1_jerk_off: # Call label
    m "Truth be told they've begun to affect me as well..."
    call lun_main("What? They got you too?","base","angry","sad","mid")
    m "I was afraid this might happen with you dispelling all of your personal wrackspurts into this room..."
    m "This is why I didn't want you doing this outside the office..."
    call lun_main("It could have been a disaster [lun_genie_name]...","base","angry","sad","mid")
    call lun_main("But will you be alright?","soft","wink","raised","mid")
    m "Oh, don't worry about me... I'm a {i}master{/i} when it comes to this..."
    call lun_main("Of course... These are your techniques after all...","base","happyCl","sad","mid")
    call lun_main("Would it...","base","seductive","sad","R")
    call lun_main("Would it be okay if I watched [lun_genie_name]?","base","annoyed","sad","mid")
    call lun_main("Just as a way to improve my own technique!","base","wink","base","mid")
    m "Mmmm, I see nothing wrong with it..."
    m "Here, I'll give you a {b}nice{/b} view..."
    show screen blkfade
    hide screen luna_main
    with d3

    ">With that, you slowly rise out of your chair as your cock strains against your robe, brought furiously to life by Luna's own performance."
    ">You then walk around your desk until you stand in front of the pale blonde..."
    m "Here we go..."
    ">As you finally pull your cock from underneath your robe you're met with a shocked gasp from Luna."
    lun "It's so..."
    lun "can I..."
    lun "..."

    ">Before you can say anything else, Luna instinctively drops to her knees."
    $ ccg_folder = "luna_facial"
    $ ccg1 = "1"
    $ ccg2 = "genie"
    $ ccg3 = "blank"
    show screen ccg
    hide screen blkfade
    with d3

    lun "Wow..."
    m "This is the place that those nasty little whiskersprouts like to hide on me..."
    $ ccg1 = "2"
    lun "It's...{w=0.3} big..."
    m "It is..."
    $ ccg1 = "3"
    lun "How often do you have to get rid of them?"
    m "Maybe once or twice a day..."
    $ ccg1 = "4"
    lun "Only twice?"
    m "It depends on the day..."
    ">You begin stroking your cock, the thick stream of pre-cum dripping from the tip easily lubricates your entire length."
    $ ccg1 = "1"
    m "*Ugh* Yeah...{w=0.3} that's it..."
    lun "..."
    $ ccg1 = "5"
    lun "Anything I should be looking for in particular?"
    m "Nothing in particular... just focus on taking it all in..."
    $ ccg1 = "6"
    lun "Taking it all in..."
    ">Luna stares intently at your cock for a few seconds before suddenly snapping from her reverie."
    $ ccg1 = "7"
    lun "Okay [lun_genie_name], I'll take it all in!"
    ">Before you even have time to react, Luna swoops her head in towards your cock, placing her nostrils at the head..."
    $ ccg1 = "8"
    ">Luna takes a huge breath inwards, closing her eyes as she does..."
    $ ccg1 = "9"
    lun "Huh...{w=0.3} It doesn't smell like I thought it would..."
    m "What did you think it would smell like?"
    $ ccg1 = "8"
    lun "Spices!"
    m "..."
    m "And what did it smell like?"
    $ ccg1 = "10"
    lun "Hmmm... It reminds me of a certain Bertie Bott's Every-Flavour bean I once had..."
    $ ccg1 = "11"
    lun "It wasn't very good... But it wasn't bad..."
    m "Well now that you've taken it all-"
    ">As if to purposely interrupt you, Luna leans her head in and quickly runs her tongue across the tip of your sensitive cock..."
    $ ccg1 = "12"
    m "What!"
    $ ccg1 = "13"
    lun "I was just hav-"
    m "Argh, you've done it now!"
    m "here it comes You little minx!"
    $ ccg1 = "14"
    lun "Here comes wha-"
    m "ARGH!!!"
    ">As if in retaliation for her previous interruptions, your cock takes it upon itself to interrupt Miss Lovegoods sentence with a thick deluge of semen."
    $ ccg1 = "15"
    m "There it is you horny little thing... here's what you wanted..."
    $ ccg1 = "16"
    lun "Oh..."
    $ ccg1 = "17"
    lun "What's this?"
    m "Argh..."
    $ ccg1 = "18"
    lun "It smells...{w=0.3} so..."
    $ ccg1 = "19"
    lun "Goood...."
    $ ccg1 = "20"
    lun "Can I...{w=0.3} Taste it?"
    m "I don't see why not."
    lun "..."
    $ ccg1 = "21"
    $ ccg2 = "blank"
    ">Luna slowly pulls a strand of your thick cum before closely examining it..."
    $ ccg1 = "22"
    lun "(My spectrespecs are detecting so much magic...)"
    lun "I've never seen anything like this before..."
    m "It's called cum."
    lun "Cum..."
    $ ccg1 = "23"
    ">With that, Luna finally decides to taste your essence."
    $ ccg1 = "24"
    lun "..."
    $ ccg1 = "25"
    lun "!!!"
    $ ccg1 = "24"
    lun "..."
    $ ccg1 = "26"
    lun "It's..."
    lun "It's......"
    $ ccg1 = "27"
    lun "It's perfect... it's just the best..."
    m "Mmm... that's it...{w=0.3} you always know what to say..."
    $ ccg1 = "28"
    lun "I'm not just..."
    $ ccg1 = "29"
    lun "How can you make this?"
    $ ccg1 = "28"
    lun "There's so much magic..."
    $ ccg1 = "30"
    lun "It's incredible..."
    $ ccg1 = "31"
    lun "It's soaking in through my skin...{w=0.3} I can't..."
    lun "The wrackspurts... I think this is..."
    $ ccg1 = "32"
    lun "Ah...{w=0.3} I think I should probably leave now [lun_genie_name]..."
    m "You're not going to clean yourself up first?"
    $ ccg1 = "33"
    lun "Oh..."
    lun "If it's ok with you [lun_genie_name]... I might clean myself up back in my room..."
    m "Whatever suits you miss lovegood..."
    $ ccg1 = "30"
    lun "Thank you [lun_genie_name]...{w=0.3} for... everything..."

    show screen blkfade
    hide screen luna_main
    hide screen ccg
    with d3

    call lun_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade
    with d3

    return







# Old Writing

label ll_pf_masturbate_T1_E2_old: #Masturbate for Genie and then Genie cum on Luna's face #DONE
    $ lun_whoring = 2
    $ days_to_luna = 3

    call play_sound("knocking")
    "*knock* *knock* *knock*"
    lun "Can I please come in, [lun_genie_name]?"
    call nar(">There's a desperate twang to Luna's voice.")

    menu:
        "-Let her in-":
            m "Of course."
        "-mess with her-":
            m "Who is it?"
            lun "Luna Lovegood, [lun_genie_name]..."
            lun "May I please come in?"
            m "Luna who?"
            lun "Lovegood, [lun_genie_name]..."
            m "Oh miss lovegood! Come in..."

    call play_sound("door")
    call lun_walk("door","mid",2.5)
    pause.5

    call lun_main("...","pout","annoyed","sad","R",cheeks="blush",xpos="right",ypos="base")
    m "Miss Lovegood..."
    m "What can I help you with today?"
    call lun_main("I-I...{w=0.3} need...","soft","seductive","sad","down")
