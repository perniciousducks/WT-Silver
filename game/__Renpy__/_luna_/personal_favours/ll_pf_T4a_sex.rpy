
    #repeatable Hermione summon event
    #Hermione immediately comments about Luna being under the desk due to the smell
    #Talks about how perverted this is
    #Starts calling Luna names as she strips and starts to play with herself
    #Genie asks her why she's stripping and also criticising Luna
    #Asks what she's expected to do when the room reeks like cum so badly
    #Hermione says it's too much
    #insists on spending the rest of the day watching Luna under your desk
    #FTB as both Luna and Hermione spend the rest of the day under your desk

# Luna sex with Genie #NEEDS TESTING

### Intro ###

# Luna leads you to the lake where you have sex...
# This random event unlocks the favor, after it you get the menu option in her favor menu.

label ll_pf_sex_T1_intro:

    call play_sound("knocking")
    ">*knock* *knock* *knock*"

    call play_sound("door")
    call lun_walk("door","mid",2)

    call lun_main("Good morning, [lun_genie_name]!","base","happyCl","sad","mid",cheeks="blush", xpos="mid" , ypos="base")

    g9 "Miss Lovegood!{w} Here to surprise me again?"

    call lun_main("I found a cure, [lun_genie_name]!","base","happyCl","base","mid")
    call lun_main("A way for both of us to get rid of our wrackspurts at once!","base","wide","base","mid")
    g9 "You don't say!"
    #call lun_main("When do you think you'll approach the rest of the wizarding world with this knowledge?","open","wide","base","mid")
    m "[luna_name], you weren't the only one thinking of something ingenious to get rid of those nasty beasts!"
    g9 "I could teach you a thing or two as well!{w} After you've showen me your suggestion..."
    call lun_main("That's very exciting don't you think?{w} We can finally get rid of this scourge once and for all!","base","happyCl","base","mid")
    call lun_main("Everyone deserves to hear about it!","base","happyCl","base","mid")

    m "Why don't you fill me in first... What's your solution?"
    #m "I was hoping you'd be able to help me iron out a few kinks to perfect it..."
    call lun_main("Of course, Sir...{w} But you'd have to...","open","wink","sad","mid")
    call lun_main("Sir could you please...{w} follow me?...","base","wink","sad","R")
    m "Follow you? To where."
    call lun_main("Just down to the lake... It's not far.","base","base","sad","mid")
    g9 "The lake you say?"
    m "Very desolate and quited...{w} It's perfect!"
    call lun_main("I can give you a tour of the school while we're at it!","base","wink","base","mid")
    call lun_main("And once we are there you can tell me about your ideas!","base","wink","base","mid")
    g9 "Sounds like a plan!{w} lets go!"
    call lun_main("Great!{w} Please follow me, Sir...","base","happyCl","sad","mid")

    # Roll out...
    show screen chair_left
    show screen desk
    call gen_chibi("stand","desk","base")
    hide screen bld1
    with d3

    call lun_walk("mid", "door", 2, loiter=False)
    call play_sound("door")

    call gen_walk(action="leave", speed=3)

    show screen blkfade
    with d3

    ">Together you and Luna gently meander around the grounds, all the while Luna happily explains the history of it all..."
    call lun_main("And this is the school library...","open","closed","base","mid")
    m "This place is huge! We could definitely find somewhere to do it in here!"
    call lun_main("I wouldn't recommend it... If we accidentally get cum on any of the books they'll probably attack us...","open","angry","sad","downL")
    m "(Is she being serious?)"
    m "Well, where do you suggest?"
    call lun_main("hmmm, we need somewhere we don't have to worry about being found...","pout","seductive","sad","down")
    call lun_main("And also somewhere the wrackspurts we expel won't bother anyone...","pout","angry","sad","downL")
    call lun_main("...","pout","closed","sad","mid")
    call lun_main("I know, let's go to the lake! Wrackspurts hate cold water!","open","wide","base","mid")
    m "They do?"
    call lun_main("Of course! Just think about how much a cold shower gets rid of them.","base","happyCl","mad","mid")
    m "You're a clever one."
    call lun_main("Thank you, [lun_genie_name]!","base","happyCl","base","mid")

    call ll_pf_sex_T1_lake_sex

    jump end_luna_event


### Menu Branch ###

label ll_pf_sex:


    # You have sex with Luna and somebody knocks at the door...
    # This should be one of the later ones, but for now it's the only one.
    jump ll_pf_sex_T1_E1



    # End event jump
    # (only used when the event isn't called.)
    label end_luna_sex_event:

        if lun_whoring < 12: # Points til 12
            $ lun_whoring += 1

        if ll_pf_sex_OBJ.level < 3:
            $ ll_pf_sex_OBJ.level = len(seen_luna_sex_list)

    # Stats
    $ ll_pf_sex_OBJ.points += 1

    jump end_luna_event






label ll_pf_sex_T1_lake_sex: # Call label
    show screen blkfade
    with d3

    ">With that, Luna grabs your hand and leads you down to the lakeside, out into the open moonlight."

    $ ccg_folder = "luna_fucking"
    $ ccg("lake_1","blank","blank")

    hide screen blkfade
    with d3

    call lun_main("Is this alright, [lun_genie_name]?","open","wink","sad","mid")
    m "This seems as good a place as any."
    call lun_main("So can you finally teach me?","open","wide","base","mid")
    m "Oh, alright then... Seeing as how you asked so nicely..."
    call lun_main("Oh thank you, thank you, thank you!","open","happyCl","base","mid")
    call lun_main("So how does it work?","open","wink","sad","mid")
    m "You'll need to take your top off."
    call lun_main("Okay!","base","happyCl","base","mid")
    $ luna_wear_top = False
    ">Without even the slightest bit of hesitation, Luna rips off her top and throws it to the ground."
    call lun_main("What's next?","base","seductive","sad","mid")
    m "Bend over."
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","seductive","sad","empty")

    hide screen luna_main
    show screen blkfade
    with d3

    ">Without saying anything, Luna goes to bend over, desperate to give herself to you..."
    m "Now pull down your skirt..."
    lun "{image=textheart}!!!{image=textheart}"
    ">Luna enthusiastically yanks down her skirt and pants, revealing her sopping pussy."
    lun "Please, [lun_genie_name]..."

    menu:
        "-Tease her-":
            ">You step forwards and gently start rubbing the head of your cock against her wet entrance."
            lun "a-ah..."
            ">Luna desperately starts thrusting towards you, begging for penetration."
            lun "Please, [lun_genie_name], I need it..."
            m "Need what?"
            lun "Your cock...{w=0.3} please, I need it...{w=0.3} The wrackspurts..."
            ">Luna's hips continue to buck in the air almost pathetically..."
            lun "I-I-I-"
            pass
        "-Slam it in!-":
            pass

    hide screen ccg
    pause
    $ lun_cg_path         = "images/CG/luna_fucking/"
    $ lun_cg_base         = lun_cg_path+"lake_2.png"
    $ lun_cg_genie        = lun_cg_path+"blank.png"
    $ lun_cg_dick         = lun_cg_path+"blank.png"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos         = 0
    $ lun_cg_ypos         = 0
    $ luna_wear_top       = True
    $ lunCG(pupil='up', eye='excited', mouth='open_tongue', eyebrow='sad', cheeks='blush', extra_1='blank', extra_2='blank', extra_3='blank', tears='blank')

    hide screen blkfade
    with d3

    ">Tired of talking, you decide to end the poor girl's suffering by slamming into her needy little fuckhole."
    lun "{size=+10}{image=textheart}!!!{image=textheart}{/size}"
    m "That's it you little slut!"
    $ lunCG('up', 'seductive', 'base')
    lun "{size=-5}{image=textheart}wow...{image=textheart}{/size}"
    $ lunCG('left', 'seductive', 'open')
    ">Before you're able to even start a steady pace of fucking the girl, her hips start violently slamming against you..."
    m "Ugh... steady on there, [luna_name], we've only just started!"
    $ lunCG('dr', 'furious', 'open')
    lun "{image=textheart}a-ah...{w=0.3} I can't...{w=0.3} [lun_genie_name]...{w=0.3} it's just...{w=0.3} too... {image=textheart}{b}goood{/b}...{image=textheart}"
    $ lunCG('up', 'furious', 'open_tongue', extra_1='speed')
    ">All you can do is stand there as Luna fucks herself senseless on your cock..."
    lun "{image=textheart}ah...{image=textheart}the wrackspurts...{image=textheart}{w=0.3} they're going...{image=textheart}{w=0.3} aaaahhh..."
    $ lunCG('dl', 'tired', 'pout')
    lun "I'm almost...{w=0.3} sad to lose...{w=0.3} them...{image=textheart}{image=textheart}"
    $ lunCG('ahegao', 'furious', 'open_tongue', overlay='fade')
    lun "They feel {image=textheart}{b}amazing{/b}...{image=textheart}"
    m "About that..."
    $ lunCG('left', 'wink', 'base')
    lun "W-what?"
    m "This isn't wickspots or whatever you call them..."
    $ lunCG('left', 'wide', 'open')
    lun "It isn't?... then... ah...{image=textheart} what's this feeling..."
    m "This is sex..."
    $ lunCG('dr', 'tired', 'pout', extra_1='blank')
    ">Luna's hips slam into your stomach and hold there."
    lun "Oh..."
    m "..."
    $ lunCG('dl', 'seductive', 'base')
    lun "Hmmm..."
    $ lunCG('left', 'wink', 'base')
    lun "So, sex forces us to eject the wrackspurts... but the feeling good is normal?"
    m "..."
    m "You got it."
    $ lunCG('up', 'furious', 'open', extra_1='speed')
    ">Luna's hips resume their assault, desperate to make up for the lost time."
    $ lunCG('left', 'seductive', 'base')
    lun "So we're... using {b}sex{/b}... to eject them..."
    m "..."
    $ lunCG('dr', 'mad', 'base')
    lun "That... would explain... the red tint... to their aura..."
    m "(Does this bitch ever shut up?)"
    ">Weary of her analysis you begin to take matters into your own hands."
    $ lunCG('ahegao', 'furious', 'open')
    ">Grabbing a hold of her hips, you start to fuck the witch in earnest."
    g4 "take this, slut!"
    $ lunCG('ahegao', 'furious', 'open_tongue', tears='tears')
    lun "{size=+10}{image=textheart}!!!{image=textheart}{/size}"
    $ lunCG('ahegao', 'furious', 'wide')
    lun "a-ahhhhh..."
    ">You keep pounding her from behind. Luna's lovely breasts jiggle a little with every thrust."
    ">You turn your attention to her butt... It's so milky and... pert... she's such a needy little girl...."
    $ lunCG('right', 'wide', 'wide', extra_3='spanking')
    $ renpy.play('sounds/slap.mp3')
    lun "ah...{image=textheart}{image=textheart}{image=textheart}"
    ">You give her buttocks another loud slap."
    $ lunCG('up', 'furious', 'open_tongue', 'mad')
    $ renpy.play('sounds/slap.mp3')
    lun "Thank you, [lun_genie_name]."
    ">You pick up the pace and feel you're getting close..."
    $ lunCG('ahegao', 'furious', 'wide', 'sad')
    lun "Yes! Yes! Thank you! Thank you! I'm almost... almost...{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
    $ lunCG('ahegao', 'furious', 'open_tongue', 'mad')
    ">You feel Luna's tight cunt start to spasm and grip down hard on your cock..."
    m "Argh! You dirty little slut! Who said you could cum yet!"
    $ lunCG('left', 'furious', 'open')
    lun "I had too, [lun_genie_name]."
    ">Her hips refuse to slow their pase as she speaks..."
    $ lunCG('ahegao', 'furious', 'base')
    lun "I {b}need{/b} it..."
    $ lunCG('up', 'wide', 'wide', extra_2='cum_1')
    ">You let out a roar and start cumming uncontrollably right into her pussy..."
    lun "ahh!{image=textheart} Yes!{image=textheart} ah...{image=textheart} it's so {b}hot{/b}...{image=textheart}"
    $ lunCG('ahegao', 'furious', 'open_tongue')
    lun "Your cum is {b}filling{/b} me up..."
    $ lunCG('dl', 'tired', 'open')
    lun "{size=-3}It's...{/size}{w} {size=-7}i...{/size}{w} {size=-9}I'm cumming...{image=textheart}{image=textheart}again...{image=textheart}{/size}"
    ">You keep firing cum deep inside her pussy until the last drop..."
    $ lunCG('ahegao', 'furious', 'open_tongue', 'sad')
    ">You can see that Luna is still trying to thrust onto you, but her legs refuse to listen to her with multiple orgasms taking over her body..."

    show screen blkfade
    with d3

    ">Luna tries to keep going but collapses on the ground with a thump after you pull out of her..."
    m "Ugh...{w} I suppose I better carry her back, she'll freeze out here otherwise."

    menu:
        "-Carry her back to her room-":
            ">You softly pick the statuesque young girl up off the cold grass, cradling her in your arms as you take her to her dorm."
            lun "..."
            lun "{size=-5}you really are a genie, aren't you?{/size}"
            pass

        "-Wipe your cock on her first-":
            m "(Should I?)"
            m "(Eh, why not?)"
            ">With that, you take your softening cock and start smearing the end of it across her nose and face."
            lun "..."
            lun "{size=-5}thank you...{/size}"
            ">You softly pick the cum coated young girl up off the cold grass, cradling her in your arms as you take her to her dorm."
            pass

    ">You return to your office."
    hide screen luncg
    hide screen blkfade
    with d3

    return


label ll_pf_sex_T1_E1: #Luna sex repeatable (in the office)#NEEDS POSING
    #Luna already in the office
    #Ask her if she's ready for a bit of sex
    #Say she was hoping he'd ask about this again
    #ask if he wants to go down to the lake again
    #Says can't be bothered, offers to have sex here
    #Adamant that no one will bother them
    #Moments after they start there's a knock on the door
    #Option to choose who it is
    #Needs check on visiting character progression
    m "How are you feeling today, [luna_name]?"
    call lun_main("Happier now that I'm in here!","base","happyCl","base","mid")
    m "Fantastic... Now, would you be interested in expelling a few more wookspoons together?"
    call lun_main("{b}Together{/b}? You mean...","base","seductive","sad","mid", cheeks="blush")
    call lun_main("Oh, thank you, thank you, thank you, [lun_genie_name]!","base","happyCl","sad","mid", cheeks="blush")

    call ll_pf_sex_start

    jump end_luna_sex_event




label ll_pf_sex_start: # Call label
    hide screen luna_main
    show screen blkfade
    with d3

    ">Before you can say anything else, Luna throws her clothes to the floor and starts desperately thrusting her ass towards you."
    m "Gods, you're a needy little whore, aren't you?"
    lun "{b}yes{/b}..."
    m "Mmmm"

    $ lun_cg_path         = "images/CG/luna_fucking/"
    $ lun_cg_base         = lun_cg_path+"base.png"
    $ lun_cg_genie        = lun_cg_path+"blank.png"
    $ lun_cg_dick         = lun_cg_path+"blank.png"
    $ lun_cg_xpos_abs     = 0
    $ lun_cg_ypos_abs     = 0
    $ lun_cg_xpos       = 0
    $ lun_cg_ypos       = 0

    ">Tired of talking, you decide to end the poor girl's suffering by slamming into her needy little fuckhole."

    $ lunCG(pupil='up', eye='wide', mouth='open_tongue', eyebrow='sad', cheeks='blush', extra_1='blank', extra_2='blank', extra_3='blank', overlay='fade', tears='blank')

    hide screen blkfade
    with d3

    lun "{size=+10}{image=textheart}!!!{image=textheart}{/size}"
    m "That's it you little slut!"
    $ lunCG('ahegao', 'furious', 'open')
    lun "{size=-5}{image=textheart}wow...{image=textheart}{/size}"
    $ lunCG('up', 'angry', 'base', 'base')
    ">She starts grinding her hips against you immediately. Desperate for as much stimulation as she can get..."
    m "Ugh... steady on there, [luna_name], we've only just started!"
    $ lunCG('dl', 'seductive', 'open', 'sad')
    lun "{image=textheart}a-ah... I can't... [lun_genie_name]... it's just... too... {image=textheart}{b}goood{/b}...{image=textheart}"
    $ lunCG('up', 'furious', 'open_tongue')
    ">Not content to just stand there, you start thrusting back into Luna's tight pussy..."
    $ lunCG('ahegao', 'seductive', 'open_tongue', extra_1='speed')
    lun "{image=textheart}ah...{image=textheart}the wrackspurts...{image=textheart} they're going...{image=textheart}aaaahhh..."
    m "I already told you- Argh... They're not real!"
    $ lunCG('dr', 'wide', 'open')
    lun "Ugh... I can see... them... ah...{image=textheart}{image=textheart} with my own two... eyes..."
    $ lunCG('left', 'seductive', 'base')
    lun "Can't you see them? The red mist..."
    $ lunCG('dl', 'tired', 'base')
    lun "There's so many... You should be able to almost... ah... make them out..."
    m "..."
    m "(Am I going crazy?)"

    # Somebody randomly knocks at the door...
    call ll_pf_sex_random

    return



label ll_pf_sex_random: # Call label
    call play_sound("knocking")
    "*knock*knock*knock*"

    m "Crap!"
    $ lunCG('left', 'wink', 'base', 'base')
    lun "Ah... who do you... think it is?"
    m "Umm... It's probably-"

    show screen blkfade
    with d3

    $ random_number = renpy.random.randint(1, 10)

    menu:

        ### Random ###
        "\"I have no clue...\"" if astoria_unlocked or tonks_unlocked:

            # Astoria
            if random_number in [1,2,3] and astoria_unlocked:
                if "astoria" not in seen_luna_sex_list:
                    $ seen_luna_sex_list.append("astoria")
                    call ll_pf_sex_T1_ast_1
                else:
                    call ll_pf_sex_T1_ast_2

            # Tonks
            elif random_number in [3,4,5] and tonks_unlocked:
                if "tonks" not in seen_luna_sex_list:
                    $ seen_luna_sex_list.append("tonks")
                    call ll_pf_sex_T1_ton_1
                else:
                    call ll_pf_sex_T1_ton_2

            # Hermione
            else:
                if "hermione" not in seen_luna_sex_list:
                    $ seen_luna_sex_list.append("hermione")
                call ll_pf_sex_T1_her_1


        ### Specific ###
        "\"Hermione maybe?\"" if game_difficulty <= 2:
            if "hermione" not in seen_luna_sex_list:
                $ seen_luna_sex_list.append("hermione")
            call ll_pf_sex_T1_her_1

        "\"Astoria, that brat!\"" if astoria_unlocked and game_difficulty <= 2:
            if "astoria" not in seen_luna_sex_list:
                $ seen_luna_sex_list.append("astoria")
                call ll_pf_sex_T1_ast_1
            else:
                call ll_pf_sex_T1_ast_2

        "\"Tonks, your teacher...\"" if tonks_unlocked and game_difficulty <= 2:
            if "tonks" not in seen_luna_sex_list:
                $ seen_luna_sex_list.append("tonks")
                call ll_pf_sex_T1_ton_1
            else:
                call ll_pf_sex_T1_ton_2


    return


# Hermione part 1 #NEEDS POSING
label ll_pf_sex_T1_her_1: # Call label
    show screen luncg
    hide screen blkfade
    with d3

    call her_main("[genie_name], I hope you're not too busy to ben-","smile","happyCl")
    call her_main("[genie_name], Luna! What are you two doing?!","smile","happyCl")
    m "ah... Isn't it obvious?"
    call her_main("Ugh... Why are you two fucking then?","smile","happyCl")
    lun "Mmmm... we're getting rid... of some nasty wrackspurts!"
    call her_main("You're still going on about that? I told you before, you're just horny!","smile","happyCl")
    lun "Stop... ah... being closed... minded Hermione..."
    lun "I bet you... didn't even realise that... Dumbledore was a genie at first!"
    call her_main("My goodness, you're such an {b}idiot{/b}!","smile","happyCl")
    lun "Don't be mean Hermione... is it the wrackspurts that are bothering you?"
    lun "I'm sure that we can teach you how to get rid of them by yourself!"
    call her_main("I know how to play with myself, idiot!","smile","happyCl")
    lun "oh..."
    lun "Well if you just want to watch us, I don't mind..."
    call her_main("Don't you have any shame!?","smile","happyCl")
    lun "mmmm... why should I be ashamed... this feels so {b}good{/b}..."
    call her_main("I know it feels good... but you shouldn't let other people watch you do it...","smile","happyCl")
    call her_main("Imagine if the whole school found out!","smile","happyCl")
    lun "Oh, that would be {b}fantastic{/b}!"
    lun "Imagine me... being the person to teach the world how the dispel wrackspurts!"
    call her_main("So you'd be okay with everyone knowing you've had Dumbledore's cock in you?","smile","happyCl")
    lun "I'd give the school a demonstration if I could!"
    ">Hermione's hands drift in between her legs..."
    call her_main("Ugh... you're so fucking {b}dirty{/b} aren't you...","smile","happyCl")
    call her_main("I just thought you were an idiot...","smile","happyCl")
    call her_main("But now... I see you've been a bimbo this whole time without even realizing...","smile","happyCl")
    lun "A bimbo?"
    call her_main("Uh-huh... You've just Dumbledore's blonde bimbo...","smile","happyCl")
    lun "..."
    call her_main("Well, I think I better give you two some alone time...","smile","happyCl")
    lun "You don't want to stay?"
    call her_main("I need to take care of something... Until then...","smile","happyCl")
    call her_main("Why don't you just let [genie_name] empty his balls in you...","smile","happyCl")
    ">With that, Hermione runs her pussy-drenched hand down Luna's face before turning and leaving the room."
    lun "I'm glad I've got a good friend like Hermione..."
    m "..."
    lun "I wish... she could have stayed though..."
    lun "Maybe... I should have asked if... she wanted to take turns..."
    lun "That was probably... rude of me..."
    m "You'd take turns?"
    lun "Of course, sharing is w-what friends do."
    g4 "You filthy slut!"
    ">You start slamming into Luna at full pace."
    g4 "Here it comes you bimbo!"
    ">With that, you start unloading into Luna's pussy."
    lun "a-a-ahh..... soo... goooood..."
    m "..."
    ">Luna slumps forwards onto your desk, drooling as her legs shake uncontrollably."
    lun "{image=textheart}{image=textheart}{image=textheart}"
    ">You slump back into your chair, leaving Luna on your desk, leaking cum."
    m "Are you good to make your own way back?"
    lun "ah... y-y-yea..."
    m "Awesome, I'm just gonna... take a nap..."

    hide screen luncg
    show screen blkfade
    with d3

    ">With that the two of you doze off..."
    ">When you wake you find only a Luna shaped cumstain on your desk."
    hide screen blkfade
    with d3

    return


# Hermione repeatable part
label ll_pf_sex_T1_her_2: # Call label

    call her_main("[genie_name], I really need a good-","smile","happyCl")
    call her_main("Oh... Hello, Luna.","smile","happyCl")
    lun "H-hello Hermione."
    call her_main("I think I'll leave you two alone...","smile","happyCl")
    ">Hermione turns to leave."
    lun "W-wait. Don't go..."
    call her_main("...","smile","happyCl")
    lun "We can share... if you like..."
    call her_main("Share? Share what?","smile","happyCl")
    lun "{b}Him{/b}."
    call her_main("...","smile","happyCl")
    call her_main("Do you really think I'm going to share with you?","smile","happyCl")
    call her_main("Just get naked... and let him take turns...","smile","happyCl")
    call her_main("Fucking us both... senseless...","smile","happyCl")
    call her_main("...","smile","happyCl")
    call her_main("......","smile","happyCl")
    call her_main("Fine! But only because that's what I came here for anyway.","smile","happyCl")
    ">With that, Hermione starts to strip, eager to join the fun."
    m "Don't I get a say in this?"
    call her_main("Oh, shut it. You're hardly going to say no to this are you?","smile","happyCl")
    m "Fair point..."
    #FTB Also, have the favour repeat from this point
    ">With that, Hermione hops up onto your desk, her eyes begging for your cock."
    her "My turn."

    hide screen luncg
    show screen blkfade
    with d3

    hide screen blkfade
    with d3

    return



# Astoria part 1 #NEEDS POSING
label ll_pf_sex_T1_ast_1: # Call label

    $ ast_seen_lun_sex = True
    ">No sooner is the name out of your mouth than a blast of light blasts from the keyhole of your door."
    ast "Alohomora!"
    ">Your door bursts open to reveal a troublesome young witch behind it."
    $ lun_cg_base = lun_cg_path+"base_2.png"
    $ lun_cg_xpos = -200
    $ astoria_scaleratio = 1.2

    hide screen blkfade
    with d3

    call ast_main("Ready to practice ano-","smile","happyCl","base","mid", xpos=400, ypos=-300)
    $ lunCG('right', 'wide', 'open')
    m "!!!"
    lun "!!!"
    call ast_main("{size=+10}Dumby!{/size} {b}What{/b} are you doing?","scream","wide","wide","mid")
    $ lunCG('right', 'wink', 'base')
    lun "Oh... hello, Astoria..."
    $ lunCG('right', 'tired', 'pout', 'sad')
    call ast_main("I wasn't speaking to you, Lovegood! I thought we were only going to practice Imperio when we were together, Dumby!","upset","angry","angry","mid")
    $ lunCG('dl', 'seductive', 'base')
    call ast_main("It's no fair if you get to play around with other students on your own!","pout","closed","angry","mid")
    $ lunCG('up', 'angry', 'open')
    m "It's not what you think, Astoria..."
    $ lunCG('ahegao', 'wide', 'open')
    call ast_main("What, so I'm supposed to think that Loony Luna just bent over and begged you to screw her?!","disgust","closed","narrow","mid")
    $ lunCG('right')
    call ast_main("Speaking of which...","pout","closed","base","mid")
    $ lunCG('dl', 'tired', 'base')
    call ast_main("{size=+3}Why {size=+3}haven't {size=+3}you {size=+3}two {size=+3}{b}stopped{/b}!!!{/size}","scream","angry","angry","mid")
    $ lunCG('right', 'tired', 'open')
    lun "Sorry... Astoria... but this... is an emergency..."
    $ lunCG('up', 'furious', 'open_tongue')
    lun "I had a wrackspurt attack and needed help to purge them..."
    call ast_main("Wrackspurt?...","pout","narrow","narrow","mid")
    $ lunCG('right', 'seductive', 'base')
    call ast_main("Ugh... I always knew you \"ravenclaw\" girls were {b}special{/b}...","disgust","narrow","base","R")
    $ lunCG('up', 'wide', 'open')
    call ast_main("But you really do take the cake, Luna...","disgust","narrow","narrow","mid")
    $ lunCG('right', 'happyCl', 'base', 'sad')
    lun "Thank you, Astoria! I love cake."
    $ lunCG('up', 'furious', 'open_tongue', 'sad', extra_1='speed')
    call ast_main("So, is she just like this then Dumby?","disgust","narrow","narrow","mid")
    m "Pretty much..."
    $ lunCG('up', 'angry', 'open')
    call ast_main("Well, I guess this is OK then...","pout","narrow","narrow","R")
    $ lunCG('ahegao', 'furious', 'open_tongue')
    call ast_main("So long as you clean this room afterwards, it reeks in here!","disgust","narrow","narrow","mid")
    $ lunCG('right', 'angry', 'base', 'sad')
    lun "Isn't it {b}great{/b}..."
    call ast_main("No! It smells gross! I can hardly breathe!","disgust","angry","narrow","mid")
    $ lunCG('up', 'wide', 'open', 'base')
    lun "Those are probably the wrackspurts... We can teach you how to get rid of them if you'd like."
    $ lunCG('right', 'seductive', 'open', 'base')
    call ast_main("No. thanks.","upset","angry","narrow","mid")
    $ lunCG('right', 'furious', 'base', 'sad')
    lun "At least watch us finish then..."
    call ast_main("What? {b}Why{/b}?","pout","angry","angry","mid")
    $ lunCG('right', 'wide', 'open')
    lun "You should know... how to expel them..."
    $ lunCG('up', 'furious', 'open')
    lun "It's just... the {b}best{/b}..."
    $ lunCG('right', 'wink', 'base')
    call ast_main("You want me to watch while Dumby-","disgust","wide","narrow","mid")
    g4 "Argh... This is it whores!"
    $ lunCG('ahegao', 'furious', 'open_tongue', extra_2='cum_1')
    call ast_main("!!!","disgust","wide","wide","mid")
    lun "Yes!"
    g4 "ARGH!!!"
    ">You grab a tight hold of Luna's hips as you start to wildly fill her up with your cum."
    call ast_main("...","upset","angry","angry","mid")
    ">Luna slumps forwards onto your desk, drooling as her legs shake uncontrollably."
    hide screen astoria_main
    with d3
    $ lunCG('ahegao', 'wide', 'open_tongue')
    lun "{image=textheart}{image=textheart}{image=textheart}"

    hide screen luncg
    show screen blkfade
    with d3

    ">You slump back into your chair, leaving Luna on your desk, leaking cum."
    m "Like the show?"
    ">You look around but can't find any trace of the small witch..."
    lun "ah... y-y-yea..."
    m "Awesome, I'm just gonna... take a nap..."

    ">With that the two of you doze off..."
    ">When you wake you find only a Luna shaped cumstain on your desk."

    hide screen blkfade
    with d3

    return


# Astoria repeatable part.
label ll_pf_sex_T1_ast_2: # Call label

    #Upset at Dumby for banging Luna again
    #Comes in after Luna is covered in cum
    #Starts shaming Luna about the smell of the room and her being a cumslut
    #Complains about all big boobed girls being sluts
    #Cum all over her as Astoria watches

    $ lun_cg_base = lun_cg_path+"base_2.png"
    $ lun_cg_xpos = -200

    call ast_main("DUMBY!","smile","happyCl","base","mid")
    $ lunCG('right', 'wide', 'open', 'base')
    hide screen blkfade
    with d3
    lun "Ah... Astoria..."
    call ast_main("Are you two going at it again?","upset","narrow","narrow","mid")
    m "Take a guess."
    $ lunCG('up', 'furious', 'open_tongue', extra_1='speed')
    call ast_main("Ugh! How am I ever supposed to learn any magic if you two won't stop shagging like rabbits!","pout","angry","angry","mid")
    $ lunCG('right', 'seductive', 'base','sad')
    lun "Ah..."
    m "I don't know Astoria, what you're watching here is pretty magical if you ask me."
    $ lunCG('up', 'seductive', 'open')
    call ast_main("Pfft... I'd hardly call an old perv like you banging a {b}bimbo{/b} \"magical\"!","upset","angry","angry","R")
    m "Mmmm, feels pretty magical..."
    m "Why don't you stay and watch... You might learn something."
    $ lunCG('right', 'furious', 'base')
    lun "Ah... yes... stay, Astoria..."
    $ lunCG('ahegao', 'furious', 'open', 'base')
    lun "You should... ah... learn how to get rid of wrackspurts."
    call ast_main("Again with your made up mumbo jumbo?!","open","narrow","narrow","mid")
    call ast_main("If you want to want to be gross with Dumby just say so...","disgust","angry","angry","R")
    $ lunCG('right', 'wide', 'open', 'sad', tears='tears')
    lun "Ah... I'm serious..."
    $ lunCG('up', 'wide', 'open_tongue')
    lun "They're real... and they... ah... make your head... all fuzzy..."
    $ lunCG('ahegao', 'angry', 'open_tongue')
    lun "I can barely... think about anything but {b}this{/b}... sometimes..."
    $ lunCG('ahegao', 'angry', 'base', 'base')
    call ast_main("You're just a big boobed bimbo!","scream","angry","angry","mid")
    call ast_main("{b}All{/b} of you big boobed girls are the same!","disgust","narrow","narrow","mid")
    $ lunCG('ahegao', 'furious', 'open', 'sad')
    lun "Ah..."
    call ast_main("If it's not you fucking Dumby every chance you can get it's Susan strutting around the halls.","pout","narrow","narrow","R")
    $ lunCG('ahegao', 'angry', 'base')
    call ast_main("Or Hermione Granger wearing the sluttiest outfit she can find...","clench","narrow","narrow","L")
    $ lunCG('right', 'seductive', 'base')
    call ast_main("It's ridiculous!","upset","angry","angry","R")
    $ lunCG('right', 'wink', 'base')
    lun "Ah... It's not that..."
    $ lunCG('right', 'wide', 'open')
    g9 "ARGH! HERE IT COMES SLUTS!"
    $ lunCG('ahegao', 'angry', 'open_tongue')
    lun "Yes..."
    call ast_main("I think I'm going to go...","pout","narrow","narrow","R")
    $ lunCG('right', 'wide', 'open', 'sad')
    lun "Ah... No... stay..."
    $ lunCG('ahegao', 'wide', 'base')
    lun "You need to see... them..."
    call ast_main("See who?","pout","narrow","narrow","mid")
    $ lunCG('right', 'wide', 'base')
    lun "The wrackspurts"
    g9 "HERE'S YOUR ROCKSPORTS SLUT!"
    g9 "ARGH!!!"
    call ast_main("...","disgust","wide","wide","mid")
    $ lunCG('ahegao', 'furious', 'open_tongue', 'base')
    ">Your cock explodes inside Luna, unleashing an avalanche of your thick seed into her tight little pussy."
    g9 "FUCK YES!!!"
    $ lunCG('ahegao', 'wide', 'open_tongue', 'sad')
    lun "it's{image=textheart}Ican't{image=textheart}what{image=textheart}ahhhhhhhhh{image=textheart}{image=textheart}{image=textheart}"
    $ lunCG('ahegao', 'angry', 'base')
    lun "..."
    call ast_main("Wow...","disgust","wide","worried","mid")
    $ lunCG('ahegao', 'tired', 'open')
    lun "{image=textheart}ah...{image=textheart} Did you see... them?"
    call ast_main("Pffft","disgust","angry","angry","mid")
    call ast_main("The only thing I saw was a super slut getting banged by her gross old headmaster!","scream","narrow","narrow","mid")
    $ lunCG('dl', 'seductive', 'base')
    lun "mmm{image=textheart}{image=textheart}"
    hide screen astoria_main
    with d3
    ">With that, Astoria turns and leaves, a confused look plastered across her face."
    lun "ah...{image=textheart}{image=textheart}{image=textheart}{image=textheart}"

    hide screen luncg
    show screen blkfade
    with d3

    m "Gods that was good..."
    lun "ah..."
    ">With that, you let Luna recover before letting her slip out of your office and back to school."

    hide screen blkfade
    with d3

    return



# Tonks part 1#NEEDS POSING
label ll_pf_sex_T1_ton_1: # Call label

    $ ton_seen_lun_sex = True
    $ lun_cg_base = lun_cg_path+"base_2.png"
    $ lun_cg_xpos = -200

    $ lunCG('right', 'wide', 'open', 'base')
    hide screen blkfade
    with d3
    call ton_main("Professor Dumbledore!","horny","base","raised","L")
    $ lunCG('dr', 'seductive', 'open', 'sad')
    lun "!!!"
    m "!!!"
    call ton_main("I didn't think you'd be able to land a grade-a bird like this you old horndog!","horny","base","raised","L")
    call ton_main("How'd you manage this one then? Love potion? Points? Gold?","horny","base","raised","L")
    lun "He's helping me... ah... get rid of... my wrackspurts!"
    call ton_main("...","horny","base","base","L")
    call ton_main("Mind control?","horny","base","raised","L")
    m "Nope."
    call ton_main("Then should I ask what the hell a \"wrackspurt\" is?","base","base","raised","L")
    m "Ugh... Luna can explain them..."
    lun "Ah... they're nasty little... mmmm... creatures that make... ah... you want... mmm... to {b}fuck{/b}."
    call ton_main("...","horny","base","raised","L")
    lun "You should... ah... be careful, Ms Tonks... {image=textheart} we're expelling a lot... {image=textheart} of them..."
    call ton_main("Really? And how will I know If these \"wrackspurts\" are after me...?","horny","base","raised","L")
    lun "You'll feel... ah... hot...{image=textheart} down there..."
    call ton_main("Oh... I see...","horny","base","raised","L")
    call ton_main("You know, you should come visit me after hours Miss Lovegood, I think I might also be able to help you out...","horny","base","raised","L")
    m "Hey!"
    lun "Ah... thank you... {image=textheart} Ms tonks... but I don't think... ah... you'll {b}taste{/b} as good..."
    call ton_main("Now, now, you don't know that... I taste like {b}heaven{/b}...","base","base","raised","L")
    lun "There's just... ah{image=textheart} no way... you can...{image=textheart} taste half as good..."
    ">Tonks hand disappears down the front of her pants..."
    call ton_main("Oh I see how it is...","horny","base","raised","L")
    lun "Ah... you do?"
    call ton_main("Uh-huh... You're just Dumbledore's dirty, little, cumslut... aren't you?","base","base","raised","L")
    lun "That's it!"
    call ton_main("So you admit it then?","horny","base","base","L")
    lun "Of course! I'm proud... to be a cumslut!"
    lun "As an auror you should... ah{image=textheart} know the importance of... mmm{image=textheart} warding off evil magic!"
    call ton_main("There's warding...","base","base","base","L")
    call ton_main("And then there's just being covered in cum...","base","base","raised","L")
    lun "Oh..."
    lun "They're both fun!"
    call ton_main("Fuck... you've really done a number on this her, haven't you, Dumbledore...","horny","base","raised","L")
    m "She was like this from the start..."
    lun "Mhmm!"
    call ton_main("Then you've lucked out on finding the horniest little nymph to ever live...","horny","base","base","L")
    lun "I am not... a nymph!"
    call ton_main("Anyway... all this talk of how much you love your headmasters yummy cum...","base","base","raised","L")
    call ton_main("I want to see it...","horny","base","raised","L")
    m "See what?"
    call ton_main("Her, covered in it...","horny","base","base","L")
    lun "You do?"
    call ton_main("Ugh... you bet... nothing like seeing your students soaking in their headmasters spunk...","base","base","raised","L")
    lun "{image=textheart}{image=textheart}{image=textheart}"

    menu:
        "Where should you cum?"
        "-On her face-":
            m "On your knees slut!"
            lun "Mhmm!"
            ">Luna quickly hops off the desk and smiles in front of your cock..."
            lun "Need me to-"
            g4 "Shutup!"
            lun "..."
            g4 "Ugh... here it is you little whore!"
            call ton_main("...","base","base","raised","L")
            ">Eager to show off to your audience you fire off a colossal load over cum over luna's waiting face."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            lun "{size=-5}thank you...{/size}"
            ">Tonk's fingers noticeably begin to speed up."
            call ton_main("Mmmm, damn... where were all the sluts like this when I was in school...","horny","base","base","L")

        "-Fire it in her-":
            g4 "ARGH!!! TAKE IT ALL YOU LITTLE WHORE!"
            ">You start filling up poor Luna as her hungry pussy does it's best to milk you dry."
            lun "Oh thank you! thank you! thank you!"
            call ton_main("Wow...","horny","base","raised","L")
            lun "Ugh...{image=textheart} it's like he's... pumped me full of magic..."
            ">Tonk's fingers noticeably begin to speed up."
            call ton_main("Mmmm, damn... where were all the sluts like this when I was in school...","horny","base","raised","L")

    call ton_main("ah...{w=0.5} this has certainly been...{p}fun.","horny","base","raised","L")
    call ton_main("But I think I best be on my way... I need to take care of some \"rockspoons\" of my own...","base","base","raised","L")
    lun "Ugh... You don't want to see us go again?"
    ">With that slips your softening cock back into her tight hole..."
    m "Ugh... can't we have a break first?"
    lun "..."
    ">Luna simply looks back at you with the eyes of a puppy dog begging for a treat."
    m "Fine... just start off slowly this time!"
    lun "That's no fun..."
    call ton_main("Wow... you two really are going to go again, aren't you?","base","base","raised","L")
    lun "You don't have to... a-ah...{image=textheart} stay if you don't want to..."
    call ton_main("Oh...{p}I may as well stick around for a little bit longer...","base","base","raised","L")
    ">Tonks' angrily fingers her cunt while she stares hungrily at Luna's bouncing boobs."

    show screen blkfade
    with d3
    pause 2
    hide screen blkfade
    with d3

    g9 "NO! MORE!"
    lun "Pleaaaaaase!"
    call ton_main("Yeah, you can make it one more round Dumbledore!","horny","base","raised","L")
    g9 "I've already gone four rounds!"
    lun "But there are still so many-"
    g9 "Well, too bad, I'm about to pass out."
    call ton_main("Hmmm, he's probably right, Luna... He is pretty old.","base","base","raised","L")
    lun "That shouldn't matter!"
    call ton_main("It's also getting rather late. As your teacher, it is my responsibility to make sure you follow curfew.","base","base","raised","L")
    m "The whole cum bath thing is okay though?"
    call ton_main("Surprisingly, there's nothing about a \"cum bath\" in the teachers handbook...","horny","base","raised","L")
    m "Fair enough. You two going to bed suits me anyway."
    call ton_main("Well, come on then, Luna, hurry up and get dressed, I'll walk you home.","horny","base","raised","L")
    lun "Alright then Miss Tonks..."
    ">With an airy smile, Luna picks up her clothes and places them on over her cum soaked form."
    call ton_main("Aren't you going to scourgify yourself before we go?","base","base","raised","L")
    lun "What, Why?"
    call ton_main("No offence honey, but you reek... I'm feeling light headed just standing next to you.","base","base","raised","L")
    lun "Oh that's just the wrackspurts! They're corpses can have that affect on people."
    lun "I {b}love{/b} the smell myself... Besides, I need to wear them to act as a warning to the other wrackspurts while I sleep!"
    call ton_main("You mean you expect me to walk you back to your room covered head to toe in cum?","horny","base","base","L")
    lun "You don't have to... I can make my own way home."
    call ton_main("I wouldn't miss this for the world... All we need is a leash and we can cross a line off my bucket list.","horny","base","raised","L")
    lun "What?"
    call ton_main("Never mind, let's just go before the prefects start whining about curfew.","base","base","raised","L")

    hide screen luncg
    show screen blkfade
    with d3

    ">With that, tonks walks off with the cum-soaked Luna..."
    m "Finally... I thought they'd never leave..."
    ">You collapse into your chair and doze off seconds later."

    hide screen blkfade
    with d3

    return



# Tonks repeatable part
label ll_pf_sex_T1_ton_2: # Call label

    #shocked to see that they're going at it again
    #Immediately starts touching herself
    #Starts talking about how excited she is to take Luna home covered in cum again
    #Talks about how wet she was during it
    #Tonks starts talking about how she wishes she could be so brazen
    #Cum all over Luna and Tonks excitedely takes her home while offering to lick her clean

    call ton_main("Ugh... are you two going at it again?","horny","base","raised","L")
    lun "Ah... these wrackspurts... ah... are quite... powerful..."
    call ton_main("Mmmm, I can believe that... In fact...","horny","base","raised","L")
    #Tonks slides her hands down her pants
    call ton_main("Ah... it looks like they're affecting me too...","horny","base","raised","L")
    m "..."
    lun "So quick! Ah... You better stay here... ah... to let them all out..."
    call ton_main("I wouldn't miss a show like this for the world...","horny","base","raised","L")
    call ton_main("I'd normally have to pay a fortune this definition.","horny","base","raised","L")
    m "Maybe I should start charging?"
    call ton_main("I could say the same to you...","horny","base","raised","L")
    call ton_main("Although I think my charges would be a little more severe...","horny","base","raised","L")
    m "Watch away then..."
    ">Tonks' starts violently fingering herself under her pants..."
    call ton_main("Mmmm, don't mind if I do...","horny","base","raised","L")
    ">The room falls silent save for the rhythmic noise of Luna being fucked and the quiet squelching coming from her perverted teacher."
    lun "Ah... ah... ah..."
    call ton_main("So, Luna.","horny","base","raised","R")
    lun "Yes... ah..."
    call ton_main("Will you be needing another escort home today?","horny","base","raised","L")
    lun "Oh, well I don't think I really need one."
    lun "But I'd be happy for the company! I always love to make new friends."
    call ton_main("I can see that... Will you also be wearing a fresh load of your headmasters cum while we walk?","horny","base","raised","L")
    lun "Of course!"
    call ton_main("Ugh... {image=textheart}fuck{image=textheart}... that's it...","horny","base","raised","L")
    call ton_main("Last time I walked you home...","horny","base","raised","L")
    lun "{image=textheart}Ah... yes? ah...{image=textheart}"
    call ton_main("God, I've never been so turned on in my life!","base","base","raised","R")
    call ton_main("Watching everyone in the school turn to look at you...","horny","base","raised","L")
    call ton_main("Coated in the biggest fucking load of cum...","base","base","raised","L")
    lun "Ah...{image=textheart}"
    call ton_main("And no one said a word...","base","base","raised","L")
    call ton_main("They just {b}fucked{/b} you with their eyes...","horny","base","base","L")
    lun "They did?{image=textheart}"
    call ton_main("Can you blame them? You were such pretty, well-fucked mess...","horny","base","raised","L")
    call ton_main("Ugh... I stayed up all night fingering myself to the sight of you...","base","base","base","L")
    lun "Ah... you did?"
    call ton_main("Mhmmm... I'll probably do it again tonight...","horny","base","base","L")
    lun "Careful... ah... you might release... too many wrackspurts..."
    call ton_main("Oh... Will that make all my students nice and slutty like you?","horny","base","base","L")
    lun "It- ah... it could."
    call ton_main("Mmmm, fantastic...","base","base","raised","L")
    lun "Fantastic? Why...{w=0.3} ah...{w=0.3} would you..."
    ">Before Luna can say anymore, you grab onto her hips before slamming into her."
    lun "Ah...{image=textheart}{image=textheart}{image=textheart}"
    g9 "Here it comes you cumsluts!"

    menu:
        "Cum inside":
            ">With that, you start unloading into Luna's pussy."
            lun "a-a-ahh..... soo... goooood..."
            m "..."
            ">Luna slumps forwards onto your desk, drooling as her legs shake uncontrollably."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            ">You slump back into your chair, leaving Luna on your desk, leaking cum."
            call ton_main("Dumbledore, what do you think you're doing?","open","base","raised","L")
            m "Busting a load?"
            call ton_main("Inside her! Now she won't be able to show off what a little cumslut she is!","open","base","base","L")
            lun "ah..."
            m "You're just upset you don't get to lead her around like a trophy."
            call ton_main("Ugh...","horny","base","base","L")
            call ton_main("At least try and get a little on her dress next time.","open","base","base","L")
            lun "..."
            m "I'll try. Now, are you ready to take Miss Lovegood home?"
            call ton_main("I suppose so... Not that there's much point if she isn't covered in cum...","horny","base","base","L")

        "Coat her face":
            m "On your knees slut!"
            lun "OK!"
            ">Luna quickly hops off the desk and smiles in front of your cock..."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            g4 "Ugh... here it is you little whore!"
            call ton_main("...","horny","base","base","L")
            ">Eager to show off to your audience you fire off a colossal load over cum over luna's waiting face."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            lun "{size=-5}thank you...{/size}"
            ">Tonk's fingers noticeably begin to speed up."
            call ton_main("Mmmm, damn... that's hot...","horny","base","base","L")
            m "Ready to take Miss Lovegood home?"
            call ton_main("You bet! I hope you don't mind taking the long route, Luna...","horny","base","raised","L")

    hide screen luncg
    show screen blkfade
    with d3

    ">With that, Tonks leads Luna out in the halls and takes her back to her room."
    ">You doze off seconds after they leave."

    hide screen blkfade
    with d3

    return
