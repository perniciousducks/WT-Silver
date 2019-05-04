define vpunch_repeat = Move((0, 10), (0, -10), .5, bounce=True, repeat=True, delay=4.5)

label panty_raid_event: #LV.8 (Whoring = 21 - 23)
    show screen blkfade
    with d5

    call room(hide_screens=True)
    call room("main_room")
    call reset_menu_position

    $ gen_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ g_c_u_pic = "sex_slow_ani"

    centered "{size=+7}{color=#cbcbcb}Panty Raid{/color}{/size}"
    narrator "Based on story written by {size=+8}WaxerRed{/size}.{w=1.0}{size=-3}\nProofreading&Editing: Lineup, Johnny, LoafyLemon{w=1.0}\nImplementation: Lineup, LoafyLemon{/size}"

    $ temp_time = daytime

    label panty_raid_event_menu:
    menu:
        "For best experience it is recommended to play the story in chronological order."
        "Part 1 - Defiance":
            $ pathvalue = 0
        "Part 2 - Acceptance":
            $ pathvalue = 1
        "Part 3 - Realization":
            $ pathvalue = 2
        "Part 4 - Obedience":
            $ pathvalue = 3
        "":
            pass
        "Go back":
            call room(hide_screens=True)
            #Reset
            $ daytime = temp_time
            if daytime:
                $ interface_color = "gold"
            else:
                $ interface_color = "gray"
            call update_gen_chibi
            jump enter_room_of_req

    stop music fadeout 1.0


    #Add day/night with music before and after she comes back. Add in transition used in A bad time to disrobe story or similar
    #Change expressions.

    $ temp_time = daytime #Switch 'daytime' back to this at the end of the store.
    $ daytime = True
    $ interface_color = "gold"
    call music_block

    #First Level
    if pathvalue == 0:
        call her_chibi("stand","mid","base")
        pause 1.0
        call hide_blkfade
        call her_main("Hello professor.", mouth="open", eye="base", flip=False)
        call her_main("", mouth="base")
        m "Good day [hermione_name]."
        m "How would you feel about going out and earning 35 points for your house today?"
        call her_main("I would love to...{w=0.3} as long as it doesn't involve me humiliating myself in front of my peers.", mouth="open", eye="baseL", cheeks="blush")
        call her_main("", mouth="normal", cheeks="blush")
        g9 "Well then, perhaps today is your lucky day."
        call her_main("Really?", mouth="open", eye="base", cheeks="blush")
        call her_main("", mouth="soft", cheeks="blush")
        m "Yes, in fact you may wish to remain as unseen as possible during your activities today."
        call her_main("(That doesn't sound suspicious at all...)", mouth="disgust", eye="down", cheeks="blush")
        call her_main("", mouth="normal", eye="base", cheeks="blush")
        g9 "I would very much like for you to recover one of the most revered and sacred objects in this academy...{w=0.5} No, in the world!"
        call her_main("Oh! You want me to recover a magical artifact?", mouth="open", eye="base")
        call her_main("", mouth="normal", eye="base")
        m "Something like that..."
        call her_main("", mouth="normal", eye="base")
        call her_main("I am glad you're finally asking me to properly utilize my abilities as one of Hogwarts top students.", mouth="open", eye="closed")
        call her_main("{size=-4}I only wish you would have asked this of me sooner..{/size}",mouth="open",eye="glanceL")
        call her_main("", mouth="normal", eye="closed")
        call her_main("Never fear! I am happy to complete a task such as this one!", mouth="smile", eye="base")
        call her_main("", mouth="base", eye="base")
        m "Great, now all the information I have for this 'artifact' is an ancient riddle..."
        m "Are you ready?"
        call her_main("Of course, [genie_name].", mouth="open", eye="soft")
        call her_main("", mouth="base")
        m "Good, here we go..."
        m "\"I am sought by many,{w=0.2} yet the same number already possess me.\""
        call her_main("", mouth="soft", eye="squint")
        m "\"The more I am used, the more valuable I become.\""
        call her_main("The sword of Gryffindor...{w=0.5}{nw}", mouth="open", eye="closed")
        call her_main("no, wait...{w=0.5}{nw}", mouth="angry", eye="shocked")
        call her_main("..the elder wand?", eye="base")
        call her_main("", mouth="disgust")
        m "I am not done yet [hermione_name]..."
        call her_main("Sorry...{w=0.5}{nw}", eye="down", cheeks="blush")
        call her_main("", mouth="normal", eye="base")
        m "\"The only thing man covet more than my form is the secret I hid.\""
        call her_main("hmm...{w=0.5}{nw}", mouth="upset", eye="baseL")
        call her_main("", mouth="normal", eye="base")
        m "... \"Sometimes I am plain and white, but I look my best when skimpy and black.\""
        call her_main("", eye="squint")
        g4 "No wait! \"skimpy and pink.\""
        call her_main("This is an ancient riddle...?", mouth="open", eye="frown")
        call her_main("", mouth="upset", eye="baseL")
        m "Hush girl.. {w=1.0}{nw}"
        m "\"In order to find me you must get close to earth, then look up to the heavens.\""
        call her_main("...", mouth="upset", eye="base")
        m "..."
        m "\"No schoolgirl fetish would be complete without me.\""
        call her_main("[genie_name]...?!", mouth="open", eye="frown")
        g9 "\"The answer is on page 74, Spell: seitnaP backwards.\""
        call her_main("PROFESSOR!", mouth="scream", eye="frown")
        call her_main("", mouth="angry", eye="frown")
        m "Yes?{w=0.5} Did you figure it out?"
        call her_main("If you wanted to see my..{w=0.3} *ahem*{w=0.3} 'undergarments' you could have just asked...", mouth="disgust", eye="suspicious", cheeks="blush")
        call her_main("{size=-4}(You didn't have to make the whole story up to catch my attention...){/size}", mouth="upset", eye="glanceL", cheeks="blush")
        g9 "By Merlin's beard! I think you've got it girl... {w=0.5}\n{size=-4}for the most part at least.{/size}"
        call her_main("[genie_name], my classes start soon, can we just get over with it so I can get my points and leave?", mouth="open", eye="closed", cheeks="blush")
        call her_main("", mouth="upset", eye="glance")
        g9 "Such eagerness...{w=0.3} but where's the challenge in handing me yours?"
        call her_main("Sorry, you wanted me to hand you a pair?", mouth="open", eye="wide_stare", cheeks="blush")
        m "Of course, but not yours silly girl.."
        call her_main("", mouth="angry", cheeks="blush")
        g9 "This is meant to be a treasure hunt! Go out and find someone's panties out in the world then bring them to me."
        call her_main("But, [genie_name]?!", mouth="shock", eye="frown", cheeks="blush")
        call her_main("", mouth="angry", cheeks="blush")
        m "You're a bright young gal, I'm sure you'll think of something... Make haste!"
        call her_main(".......", mouth="disgust", cheeks="blush")
        pause 1.0
        call her_main("", eye="down", cheeks="blush")
        m "What are you standing there for?"
        call her_main("Isn't there any other way I coul-..{w=0.5}{nw}", eye="glance", cheeks="blush")
        m "No."
        call her_main("{size=-4}...fine.{/size}", eye="down", cheeks="blush")

        call her_walk(action="leave", speed=2.5)

        show screen blkfade
        with d3

        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Three hours later...{/color}{/size}"

        $ daytime = False
        $ interface_color = "gray"
        call music_block
        show screen fireplace_fire
        pause 1.0
        call hide_blkfade

        call play_sound("knocking")
        pause 1.0
        m "Enter!"

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call her_main("Good evening, [genie_name].", mouth="open", eye="baseL")
        call her_main("", mouth="normal", eye="baseL")
        m "Hello again, [hermione_name]."
        call her_main("", cheeks="blush")
        m "Did you finish your assignment?"
        call her_main("about that...", mouth="soft", eye="glanceL", cheeks="blush")

        call her_walk(xpos="desk", ypos="base", speed=1.0)

        "She elegantly drops a pair of frilly pink panties on your desk."
        call her_main("And for extra credit...", mouth="soft", eye="down", cheeks="blush")
        hide screen bld1
        hide screen hermione_main
        with d3
        "She adds a matching pink lingerie bra to the spoils on your desk."
        show screen bld1 with d3
        g9 "You absolute minx!"
        call her_main("", mouth="normal", eye="baseL", cheeks="blush")
        g9 "You've outdone yourself [hermione_name], how did you manage this feat?"
        call her_main("I would prefer not to talk about it...", mouth="disgust", eye="down", cheeks="blush")
        g9 "Well you can certainly colour me impressed."
        call her_main("Does that mean I've earned some extra house points?", mouth="open", eye="baseL")
        m "I think the situation calls for it..."
        call her_main("", mouth="smile", eye="baseL")
        g9 "90 points to Gryffi-... {w=0.5}{nw}"
        g4 "90 points to Gryffi-... {fast} wait a second..."
        call her_main("", mouth="smile", eye="base")
        "> You take another look at the undergarments and notice something unusual."
        call her_main("", mouth="base", eye="base")
        "> Both panties and a bra has a small piece of paper tied to it."
        call her_main("", mouth="normal", eye="base")
        "> You reach out and grab the closest pair of undergarments then study the paper."
        call her_main("", mouth="normal", eye="baseL")
        "8.99$\n{size=-3}Thank you for shopping with us and hope to see you back soon!{/size}\nMadam Mafkin"
        m "[hermione_name]..."
        call her_main("Yes, [genie_name]?", mouth="crooked_smile", eye="closed")
        m "Do you know why is there a price tag on these?"
        call her_main("...!", mouth="angry", eye="wide")
        call her_main("Uh.... Well, the person I boug-... {w=0.3}*ahem*{w=0.2} {size=+2}BORROWED{/size} these from must have forgotten to take the price tag off.", mouth="open", eye="squint")
        call her_main("", mouth="normal")
        m "I see...{w=0.3} Well whoever you took them from must be a bit slow to forget something like that, don't you agree?"
        call her_main("Uhh...", eye="down")
        m "I would even dare to call them...{w=0.2} a moron."
        call her_main("...", mouth="upset")
        call her_main("", eye="worriedL")
        g9 "A bloated...{w=0.2} Scatterbrained,{w=0.2} moron!"
        call her_main("{size=+4}[genie_name]!{/size}", mouth="open", eye="frown")
        call her_main("", mouth="normal")
        m "Yes, [hermione_name]?"
        call her_main("Fine...", mouth="annoyed", eye="annoyed")
        call her_main("it was me!", mouth="angry", eye="down")
        call her_main("I couldn't do it, so I bought them at the shop...", mouth="disgust")
        m "So...{w=0.5} You're the bloated, scatterbrained moron then?"
        call her_main("Sir, this has been embarrassing enough...{w=0.5}\nCan I just go back to my dormitory please?", eye="glance")
        m "[hermione_name]..."

        menu:
            "\"Cheaters never Prosper.\"":
                m "Well, I must say I am disappointed with your actions [hermione_name]."
                call her_main("I am so sorry [genie_name]..", mouth="disgust", eye="down")
                call her_main("", eye="glance")
                m "Not only you disobeyed me but also tried to trick me, your headmaster, into thinking these belonged to some colleague of yours."
                call her_main("it won't happen again..", eye="down")
                call her_main("", eye="glance")
                g4 "For your own sake it better doesn't or I will have to take action."
                call her_main("", eye="down")
                m "Dismissed."
                call her_main("Yes sir.")

            "\"Yes, they do.\"":
                m "Well, I must say...{w=0.3} I am impressed with your courage [hermione_name]."
                call her_main("I am sorry [genie_name] I wo-..{w=0.2}{nw}", mouth="disgust", eye="down")
                call her_main("Wait what?", mouth="shock", eye="worried")
                call her_main("", mouth="soft", eye="worried")
                m "I never imagined you'd posses such \"out of the box\" problem solving!"
                call her_main("Really?", mouth="open", eye="worried")
                call her_main("", mouth="soft", eye="worried")
                g9 "You fumbled the landing, but otherwise cheated like a pro!"
                call her_main("Thank you...", mouth="soft", eye="worried")
                call her_main("(I guess..?)", mouth="soft", eye="glanceL")
                call her_main("", mouth="soft", eye="worriedL")
                m "Now, I won't overburden you with compliments..."
                call her_main("", mouth="soft", eye="worried")
                m "Take your house points and go...{w=0.5} 35 points to Gryffindor!"
                call her_main("{size=+4}Really?!{/size}{w=0.2} Thank you so much [genie_name]!", mouth="smile", eye="base", cheeks="blush")

                call her_walk(xpos="mid", ypos="base", speed=1)

                m "I hope next time you do better though."
                call her_main("(Next time...?!)", mouth="shock", eye="shocked", cheeks="blush", flip=True)
                call her_main("(Think about the points Hermione, the points......)", mouth="angry", eye="worriedCl", cheeks="blush", flip=True)

        call her_walk(action="leave", speed=2.5)

        show screen blkfade with d3
        stop music fadeout 1.0
        hide screen fireplace_fire
        centered "{size=+7}{color=#cbcbcb}~End of part one{/color}{/size}"
        jump panty_raid_event_menu

    #Second Level
    if pathvalue == 1:
        call hide_blkfade
        pause 1.5
        call play_sound("knocking")
        pause 1.0
        m "Come in!"

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call her_main("Hello [genie_name], you called?", mouth="open", eye="base", flip=False)
        call her_main("", mouth="base")
        m "Hello to you too, [hermione_name]."
        g9 "Say..{w=0.3} would you like to earn some points today girl?"
        call her_main("Possibly..", mouth="open")
        call her_main("But that depends on the task required of me.", eye="closed")
        call her_main("", mouth="soft", eye="baseL")
        m "I would like you to try yourself at {size=+4}'that'{/size} favour again."
        call her_main("*sigh* I knew that sooner or later you would ask me about it, [genie_name]..", mouth="open", eye="closed")
        call her_main("Do I have a choice?", mouth="upset", eye="worried")
        g9 "Certainly, if you don't mind those 'Slytherin Harlots' taking the house cup!"
        call her_main("I Do mind...", eye="down_raised")
        call her_main("", eye="worried")
        g9 "Then you'd better head on out and steal some girl's panties!"
        call her_main("{size=-4}...100 points{/size}", mouth="open", eye="worriedL")
        call her_main("", mouth="upset")
        m "35."
        call her_main("...75 points", mouth="open", eye="worriedCl")
        call her_main("", mouth="upset")
        m "40.."
        call her_main("...50 points", mouth="upset")
        m "45..."
        call her_main("Fine.", mouth="disgust", eye="glanceL")
        call her_main("", mouth="upset", eye="baseL")
        g9 "We got a deal then, splendid!"
        call her_main("", mouth="normal", eye="base")
        m "You're free to go then."
        call her_main("Thank you sir.", mouth="open", eye="base")

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call bld
        m "Oh and one more thing.."
        call her_main("Yes?", mouth="soft", eye="baseL", flip=True)
        m "Make sure they're not new this time."
        call her_main(".....okay.....", mouth="disgust", eye="down", flip=True)
        hide screen hermione_main
        hide screen bld1
        with d3
        pause 0.5

        call play_sound("door")
        call her_chibi("hide")
        with d3
        pause 1.0

        show screen blkfade
        with d3
        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Four hours later...{/color}{/size}"
        $ daytime = False
        $ interface_color = "gray"
        call music_block
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0
        show screen fireplace_fire
        pause 1.0

        call hide_blkfade
        pause.5

        call her_walk(action="enter", xpos="desk", ypos="base", speed=3.0)

        call play_sound("bump")
        "She drops a slightly used pair of plain panties on your desk."
        call her_main("", mouth="soft", eye="baseL", cheeks="blush", flip=False)
        m "I don't see any tags, thats good, did you learn from your previous error?"
        call her_main("Yes sir...", mouth="disgust", eye="down", cheeks="blush")
        call her_main("", mouth="soft", eye="down", cheeks="blush")

        menu:
            "\"Let her Go.\"":
                m "Well, quality leaves a bit to be desired but a good step forward."
                call her_main("", mouth="soft", eye="base", cheeks="blush")
                m "45 points to Gryffindor!"
                call her_main("Thank you, [genie_name].", mouth="open", eye="base", cheeks="blush")
                call her_main("Am I free to go now?", mouth="soft", eye="base", cheeks="blush")
                m "Yes, you are free to go."

                call her_walk(xpos="mid", ypos="base", speed=1.0)

                $ renpy.play('sounds/sniff.mp3')
                g9 "{size=-4}Such nice fragrance, I wonder to whom these belong?{/size}"
                call her_main(".........(I'm sorry Ginny).........", mouth="disgust", eye="down", cheeks="blush", flip=True)

                call her_walk(action="leave", speed=2)

            "\"Ask for details.\"":
                m "So, who was the lucky lady?"
                call her_main("No one.", mouth="open", eye="worriedL", cheeks="blush")
                call her_main("", mouth="soft", cheeks="blush")
                m "Come on now."
                call her_main("Umm...{w=0.3} Does that really matter?", mouth="open", eye="base", cheeks="blush")
                call her_main("", mouth="soft", cheeks="blush")
                m "It does to me."
                call her_main("*sigh*", mouth="soft", eye="worriedCl", cheeks="blush")
                call her_main("It was Ginny, sir...", mouth="open", eye="worried", cheeks="blush")
                call her_main("", mouth="soft", cheeks="blush")
                m "Interesting...{w=0.5} I don't know who that is."
                call her_main("She's a sister of one of my friends...", mouth="open", eye="worriedL", cheeks="blush")
                call her_main("", mouth="normal", cheeks="blush")
                m "Is she hot? Or cute?"
                call her_main("...", eye="down", cheeks="blush")
                m "Well?"
                call her_main("I guess she is kind of both..", mouth="soft", cheeks="blush")
                g9 "(Splendid! Maybe she can introduce her to me sometimes)"
                call her_main("", eye="base", cheeks="blush")
                m "So, how did you do it?"
                call her_main("I offered to do her laundry along with mine this week...", mouth="open", eye="down", cheeks="blush")
                call her_main("", mouth="soft", cheeks="blush")
                m "And?"
                call her_main("And whilst I was working, I grabbed one of her...{w=0.4} 'panties'...{w=0.3} and shoved them in my pocket.", mouth="soft", eye="glanceL", cheeks="blush")
                m "And?"
                call her_main("If she she asked what happened to them... I would've just said that they had gotten lost in the wash.", eye="glance", cheeks="blush")
                call her_main("", mouth="normal", cheeks="blush")
                m "And?"
                call her_main(" And... that’s really it.", mouth="open", eye="base")
                call her_main("", mouth="normal")
                g4 "How dull.{w=0.5} 45 stupid house points to Gryffindor."
                call her_main("Do those count the same as regular points?", mouth="annoyed")
                m "I suppose..."
                call her_main("Goodnight then sir.", mouth="open", eye="base")

                call her_walk(xpos="door", ypos="base", speed=3.0)

                m "{size=-4}Ginny..{w=1.0} its time for you to meet 'George'.{/size}{w=0.2}{nw}"
                call gen_chibi("jerking_off_behind_desk")
                $ renpy.play('sounds/zipper.mp3')
                g9 "{size=-4}Ginny.. Its time for you to meet 'George'.{/size}{fast}"
                call her_main("", mouth="angry", eye="shocked", cheeks="blush", flip=True)
                pause 0.8
                call her_main("(I better leave now...)", mouth="disgust", eye="baseL", cheeks="blush", flip=True)
                hide screen hermione_main
                hide screen bld1
                with d3
                pause 0.5

                call her_chibi("leave")

        call blkfade

        stop music fadeout 1.0
        hide screen fireplace_fire
        call gen_chibi("sit_behind_desk")
        centered "{size=+7}{color=#cbcbcb}~End of part two{/color}{/size}"
        jump panty_raid_event_menu

    # Third Level
    elif pathvalue == 2:
        call hide_blkfade
        pause 1.0
        call play_sound("knocking")
        pause 0.5
        her "I'm coming in.{w=1.0}{nw}"

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        g9 "Well, well, well.. if it isn't my favourite minx!"
        call her_main("Good morning to you too, [genie_name].", mouth="open", eye="closed", flip=False)
        call her_main("", mouth="base", eye="base")
        m "What brings you here this time?"
        call her_main("Well... I..", mouth="open", eye="baseL", cheeks="blush")
        call her_main("", mouth="upset", cheeks="blush")
        m "Don't you worry, I'm just teasing you."
        call her_main("", mouth="normal", eye="base", cheeks="blush")
        m "But we've made it quite a habit by now, didn't we?"
        m "You coming here every morning and asking for points.."
        call her_main("", eye="worried", cheeks="blush")
        m "..for which in return you bring me panties of that colleague of yours.."
        call her_main("", eye="down_raised", cheeks="blush")
        g9 "..I wonder if she realized by now that a washing machine can only eat so much panties."
        call her_main("", mouth="soft", eye="glanceL", cheeks="blush")
        m "but surely that's something worth risking your reputation over, am I right?"
        call her_main("...", mouth="annoyed", eye="glanceL")
        g9 "I'll take that as a yes."
        m "You know what to do, off you go."
        call her_main("Fine.", mouth="open", eye="closed")
        call her_main("", mouth="annoyed", eye="glance")
        g9 "That ‘a girl."

        call her_walk(action="leave", speed=2.5)

        call blkfade

        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Few hours later...{/color}{/size}"
        $ daytime = False
        $ interface_color = "gray"
        call music_block
        show screen fireplace_fire
        pause 1.0
        call hide_blkfade

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        g9 "Hello [hermione_name], looking good."
        call her_main("Uh-huh. Sir, if I'm not mistaken... {w=0.3}Hogwarts does not have a 'linguistic' class, do we?", mouth="open", eye="concerned")
        call her_main("", mouth="upset")
        m "(Why is she asking me?{w=0.3} Oh Right, 'headmaster' Rumbleboar)"
        m "Do you really think we have a class you wouldn't know about?"
        call her_main("True... Then, do you know of how many \"Connie's\" attend Hogwarts?", mouth="open", eye="base")
        call her_main("", mouth="normal")
        call her_main("There aren't any in Gryffindor or Ravenclaw I believe, but I'm not sure for some of the other houses.", mouth="open", eye="soft")
        call her_main("", mouth="normal")
        m "I feel as though there's some context missing."
        call her_main("Uhmmm... alright, so...{w} I was in the Gryffindor girl’s dorm, working on my 'task.'", mouth="open")
        call her_main("", mouth="normal")
        m "The perfect hunting grounds."
        call her_main("I am astonished that I'll have to agree with you but yes... I had the pick of the litter with no absence of choice.{w=0.3} Speaking of...", mouth="open", eye="closed")

        call her_walk(xpos="desk", ypos="base", speed=1.0)

        $ renpy.play('sounds/cloth_sound.mp3')
        "She drops a bunched-up ball of about half a dozen girl's panties on your desk, coming in an array of different sizes, designs and colours."
        call her_main("I usually don’t conduct such a shotgun approach to work, although...", mouth="open", eye="base", cheeks="blush")
        call her_main("", mouth="soft", cheeks="blush")
        g9 "In this instance it appears to have served you well, full marks for stealing panties from your schoolmates."
        call her_main("It would have flustered me if I hadn't told my dorm mates time and time again, it is all of our responsibilities to keep our dorm tidy.", mouth="annoyed", eye="baseL", cheeks="blush")
        call her_main("Loss of said property is expected when leaving their undergarments strewn around as if a hurricane blew through their drawers.", mouth="open", eye="base")
        call her_main("", mouth="soft")
        m "Yes, Yes... But how does this connect back to a ‘Connie’?"
        call her_main("Right... Well, I obviously chose a time that I believed all my dorm mates would be gone.", mouth="open", eye="worriedCl")
        call her_main("", mouth="normal")
        call her_main("But just as I was shoving the last pair into my bag, Katie Bell walked in...", mouth="angry", eye="down_raised", cheeks="blush")
        call her_main("She caught me red handed!", mouth="disgust", eye="down", cheeks="blush")
        call her_main("", eye="concerned")
        g9 "Or caught silky handed!{w=1.0}{nw}"
        m "Or caught silky handed!{fast} ...panty handed?"
        call her_main("", eye="down")
        m "..."
        m "Sounded better in my head...{w=0.5} give me a minute and I'll come up with something that works..."
        call her_main("I've never been more embarrassed in my entire life!", eye="concerned", cheeks="blush")
        call her_main("", mouth="annoyed", eye="glanceL")
        m "Pff, as if you've never said 'that' before."
        call her_main("I mean it! And I was mortified standing there clutching her panties while stumbling over my words for an excuse.", mouth="open", eye="concerned", cheeks="blush")
        call her_main("", mouth="upset", cheeks="blush")
        m "And what did she do?"
        call her_main("Well... that's the odd thing, while I was floundering like a fish she was just grinning at me. And then she said and I quote-", mouth="open", eye="base")
        call her_main("\"Heh, I always had a feeling about you Granger... But if you want them, you'll need to do me a favor. Meet me tonight and we can help Connie with her Linguistic homework.\"", mouth="open", eye="baseL")
        call her_main("", mouth="base", eye="base")
        m "Connie with her linguist?-{w=1.0}{nw}"
        g9 "Connie with her linguist?-{fast} oh I see.."
        call her_main("As embarrassing as initial circumstances are, I would never turn down a request to help a student with homework! But I don't think we have a linguistic class or what Connie she was-", mouth="open", eye="concerned")
        call her_main("", mouth="soft", eye="base")
        g9 "Cunnilingus [hermione_name]... She was asking for Cunnilingus."
        call her_main("Huh? But she said she wanted study help.")
        m "It was a metaphor... She was assuming you were a bit more 'worldly' than you really are."
        call her_main("I am plenty worldly!", mouth="angry", eye="angry")
        call her_main(".....", mouth="upset", eye="angryL")
        call her_main("", eye="worried")
        pause 0.5
        call her_main(".... What’s Cunnilingus?", mouth="open", eye="worried")
        call her_main("", mouth="upset")
        m "*Sigh*, she was asking for Dinner beneath the bridge."
        call her_main("Dinner? But if she wanted to eat with me why didn't she-", mouth="open", eye="base")
        call her_main("", mouth="upset")
        m "Metaphor, [hermione_name]... She wanted you to sip from her furry cup."
        call her_main("Huh?", mouth="open", eye="concerned")
        call her_main("", mouth="upset")
        m "Muff Diving.."
        call her_main("", eye="worried")
        m "Munch her carpet.."
        call her_main("", mouth="clench", eye="angryCl")
        m "Deluxe wash.."
        call her_main("Stop not making any sense!", mouth="clench", eye="angry")
        call her_main("", mouth="annoyed")
        m "Are you really supposed to be this school’s top student? She was asking you to eat her out."
        call her_main("Eat her what out?", mouth="open")
        call her_main("", mouth="annoyed", eye="angryL")
        m "Alright... work with me. She wanted you...{w=1.0} Still with me here?"
        call her_main("Yes obviously...", mouth="open", eye="angryCl")
        call her_main("(...does he think I'm an idiot?)", mouth="annoyed", eye="angryL")
        m "Okay then repeat after me."
        call her_main("", eye="soft")
        m "She wanted you.."
        call her_main("She wanted me...", mouth="open", eye="soft")
        call her_main("", mouth="normal")
        m "To take your tongue..."
        call her_main("Thake myh tonghue?", mouth="open_tongue")
        call her_main("", mouth="open_wide_tongue", eye="suspicious")
        pause 1.0
        g9 "And stick it in her vagina!"
        call her_main("{size=+8}WHAT?!{/size}", mouth="shock", eye="wide", cheeks="blush")
        call her_main("Why would she want that?!", mouth="shock", eye="wide_stare", cheeks="blush")
        call her_main("", mouth="angry", cheeks="blush")
        g9 "Because in my experience it feels awesome...{w=0.5}{nw}"
        m "Because in my experience it feels awesome...{fast} Wait, did that make it sound like I have a vagin-"
        call her_main("You're wrong! She- She-", mouth="shock", eye="angryCl", cheeks="blush")
        call her_main("", mouth="angry", eye="WorriedCl", cheeks="blush")
        m "What? Never done it before?"
        call her_main("{size=+4}OF COURSE NOT!{/size}", mouth="angry", eye="angry", cheeks="blush")
        g9 "I mean, I assumed you didn't have any real friends... But to get to your age and never eat another girl out? How shameful."
        call her_main("Not everyone in this school is as gross as you!", mouth="angry", eye="annoyed", cheeks="blush")
        g9 "well, there's one way to prove me wrong. Go find ‘Katie’ and ask her yourself."
        call her_main("", mouth="annoyed", eye="annoyed", cheeks="blush")
        call her_main("Maybe I will...", mouth="open", eye="angryCl")
        call her_main("", mouth="upset", eye="annoyed")
        call her_main("She will surely-...{w=0.5}{nw}", mouth="open", eye="closed")
        call her_main("{size=+4}HOLD ON!{/size}", mouth="scream", eye="wide")
        call her_main("", mouth="shock")
        m "What?"
        call her_main("I-I-I-I-I.....", mouth="angry", eye="wide_stare", cheeks="blush")
        m "Just spit it out!"
        call her_main("I was so nervous with her that I just said yes! She'll be expecting me soon!", mouth="mad", eye="down_raised", cheeks="blush")
        g9 "You better get to it then, [hermione_name]!"
        call her_main("But I- But I- I couldn't- ", mouth="shock", eye="down", cheeks="blush")
        call her_main("", mouth="angry", cheeks="blush")
        call her_main("I'll just have to inform her that it was a misunderstanding, yes that will have to do.", eye="glanceL", cheeks="blush")
        call her_main("", eye="glance", cheeks="blush")
        g9 "Sure, and risk her spilling the beans to your entire dorm that the proud Hermione Granger steals girls’ panties."
        call her_main("...", eye="down", cheeks="blush")
        call her_main("", eye="angryCl", cheeks="blush")
        g9 "Hey, for sixty points would you let me watc-"
        call her_main("Absolutely not!", mouth="scream", eye="angry", cheeks="blush")
        call her_main("", mouth="angry", eye="angry", cheeks="blush")
        m "That's a bummer.."
        call her_main("", mouth="angry", eye="angryL", cheeks="blush")
        m "You can go then."
        call her_main("...", mouth="annoyed", cheeks="blush")
        call her_main("......", mouth="annoyed", eye="worried", cheeks="blush")
        call her_main("What about the points sir?", mouth="open", eye="concerned", cheeks="blush")
        call her_main("", mouth="annoyed", eye="worried", cheeks="blush")
        m "Oh yes, right.."
        m "45 points to Gryffindor!"
        call her_main("Thank you sir...", mouth="open", eye="concerned")
        call her_main("", mouth="upset", eye="baseL")
        pause 0.5

        call her_walk(xpos="mid", ypos="base", speed=1)

        g9 "Bon apetite!"
        call her_main("", mouth="open", eye="baseL", flip=True)
        pause 0.5
        call her_main(".....", mouth="angry", eye="base", flip=True)
        call her_main("(What did I get myself into this time..?)", mouth="angry", eye="down_raised", cheeks="blush", flip=True)

        call her_walk(action="leave", speed=2)

        call blkfade

        stop music fadeout 1.0
        hide screen fireplace_fire
        pause 1.0
        call play_sound("knocking")
        pause 1.0
        fem "Who is it?"
        pause 0.5
        her "It's me.. Hermione granger."
        call play_sound("door")
        her "Hello Katie I-..{w=1.5}{nw}"
        $ renpy.play('sounds/giggle2.mp3')
        "Katie" "Hey there sweet cheeks.{image=textheart}{w=0.5} I have been waiting for you. {image=textheart}{image=textheart}{image=textheart}"
        her "We need to ta-..{w=1.0}{nw}"
        "Katie" "I know exactly what we need.{image=textheart}"
        $ renpy.play('sounds/slap_03.mp3')
        "> Katie grabs Hermione and pulls her in the room{nw}"
        $ renpy.play('sounds/door2.mp3')
        "> Katie grabs Hermione and pulls her in the room{fast} then shuts the door."
        pause 1.0
        $ renpy.play('sounds/09_lock.wav')
        pause 0.5
        her "Why did you lock the door...?!"
        $ renpy.play('sounds/cloth_sound.mp3')
        "> Katie starts taking off her clothes."
        her "Wha- wha- what-t-t are you d-doing?!"
        $ renpy.play('sounds/giggle.mp3')
        "Katie" "Aren't you talkative today?{w=0.5} I would save my breath if I was you. {image=textheart}{image=textheart}{image=textheart}"
        "Katie" "I'm quite{w=0.2} {image=textheart}horny{image=textheart}{w=0.2} so you might be 'stuck' for a while."
        $ renpy.play('sounds/push_on_bed.mp3')
        "> She pushes Hermione onto the bed." with vpunch
        her "{size=+4}W-wait?!{/size}"
        $ renpy.play('sounds/sit_on_bed.mp3')
        "> Then she swiftly straddles her face in cowgirl position." with hpunch
        $ renpy.play('sounds/gltch.mp3')
        her "..........!!!{w=1.0}{nw}"
        her "*Hmph*"
        $ renpy.play('sounds/gasp2.mp3')
        "Katie" "Ahh!{image=textheart} {w=0.5}So much better..{image=textheart}{image=textheart}{image=textheart}"
        "Katie" "I'll start moving now.{w=0.5} You ready?"
        her "*nwh*!!!"
        $ renpy.play('sounds/giggle3.mp3')
        "Katie" "I'll take that as a yes. {image=textheart}{image=textheart}{image=textheart}"
        $ renpy.play('sounds/jump_on_bed.mp3')
        her "*Hmph{cps=10}hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh{/cps}*{nw}" with vpunch_repeat
        pause 1.0
        centered "{size=+7}{color=#cbcbcb}~End of part three{/color}{/size}"
        jump panty_raid_event_menu

    #Fourth Level
    elif pathvalue == 3:
        centered "{size=+7}{color=#cbcbcb}A Couple months later after the 'linguistic' incident{/color}{/size}"
        call hide_blkfade
        pause 1.0

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call her_main("Hello, [genie_name].{image=textheart}", mouth="smile", eye="wink", flip=False)
        call her_main("", mouth="smile", eye="base")
        g9 "[hermione_name]! My favourite slut."
        m "I have another riddle for you."
        call her_main("Oh, this ought to be fun.", mouth="grin")
        call her_main("Could you make it a 'hard' one [genie_name]?", mouth="open_wide_tongue")
        call her_main("", mouth="smile")
        g9 "You'll enjoy this one for sure...{w=0.3} Ready?"
        call her_main("Ready!", eye="happyCl")
        call her_main("", eye="base")
        m "\"I am as soft and pure as a kitten, though far more desirable.\""
        call her_main("Hmmmm...", mouth="base", eye="baseL")
        call her_main("Boobs?{w=0.3} Titjob?", mouth="soft", eye="base")
        call her_main("", mouth="smile", eye="base")
        m "Nope, in this case contrary to a titjob, it being both small and tight is usually preferred."
        call her_main("Sex?", mouth="grin", eye="glance")
        call her_main("", mouth="base", eye="glance")
        m "Nope...{w=0.5} \"While boys may want me, they wouldn’t be caught dead ever just buying me for themselves.\""
        call her_main("Well that definitely rules out sex.", mouth="open", eye="baseL")
        call her_main("", mouth="base")
        m "\"The less of me there is, the more...'desirable' I become to behold.\""
        call her_main("Oh! Oh! Panties!", mouth="crooked_smile", eye="closed")
        call her_main("", eye="base")
        g9 "Spot on."
        call her_main("Mine or someone else’s?", mouth="smile", eye="happy")
        m "Someone else's if you don't mind, [hermione_name]."
        call her_main("On it! I'll be back soon...", eye="base")

        call her_walk(action="leave", speed=2.5)

        call blkfade

        stop music fadeout 1.0
        centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"
        $ daytime = False
        $ interface_color = "gray"
        call music_block
        show screen fireplace_fire
        pause 1.0
        call hide_blkfade

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call her_main("Hello [genie_name], I hope I didn't keep you waiting for too long...", mouth="smile", eye="happy")

        call her_walk(xpos="desk", ypos="base", speed=1.0)

        call her_main("I had a little..{w=0.5} 'setback'{w=0.2} if you know what I mean..", mouth="grin", eye="glance", cheeks="blush")
        call her_main("", mouth="base", cheeks="blush")
        pause 0.5
        hide screen bld1
        hide screen hermione_main
        with d3
        "She drops a pair of laced white panties on your desk."
        show screen bld1 with d3
        m "No trouble at all [hermione_name].{w=0.5} And you have excellent taste as always."
        $ renpy.play('sounds/sniff.mp3')
        g9 "These smell fantastic!"
        call her_main("You're too kind [genie_name].", mouth="grin", eye="happy", cheeks="blush")
        hide screen bld1
        hide screen hermione_main
        with d3
        pause 1.0
        call gen_chibi("jerking_off_behind_desk")
        $ renpy.play('sounds/zipper.mp3')
        ">You take your cock out and start stroking it..."
        call gen_chibi("jerking_off_behind_desk")
        call her_main("Mmmm, [genie_name] need any help with that?", mouth="base", eye="suspicious", cheeks="blush")
        m "These already feel a little damp in the middle. Why don’t you tell me why that is?"
        call her_main("Oh you know, girls will be girls and all.", mouth="grin", eye="glance", cheeks="blush")
        g9 "You know, charming the panties off someone is just a figure of speech."
        call her_main("Not anymore... I'd like to think Katie was quite pleased with me.", mouth="smile", eye="glance", cheeks="blush")
        m "Katie? Katie Bell? The same delicious dyke that wanted you to clam joust with her?"
        call her_main("Maybe...", eye="glanceL", cheeks="blush")
        call her_main("Although, Katie keeps raising the fee every time I ask.", eye="happyCl", cheeks="blush")
        call her_main("", mouth="open", cheeks="blush")
        call her_main("Not that I mind, but my tongue can get quite sore sometimes.", mouth="open_tongue", cheeks="blush")
        call her_main("Especially since we've started the alphabet-lingous thing.", mouth="open_wide_tongue", eye="ahegao_squint", cheeks="blush")
        call her_main("", mouth="open_wide_tongue", eye="ahegao_squint", cheeks="blush")
        g4 "Ugh!"
        call cum_block
        call gen_chibi("cumming_behind_desk")
        call her_main("", eye="glance", cheeks="blush")
        pause 1.5
        call gen_chibi("came_on_desk")
        call her_main("Oh, poor [genie_name], I had no idea you were so pent up. You can start calling me out more than twice a day, if two a day isn't enough.", mouth="soft", eye="concerned", cheeks="blush")
        m "During the day? But what about your classes?"
        call her_main("Hmm? Oh well, missing one or two wouldn't hurt... Especially if the headmaster has an important 'assignment' for me.", mouth="base", eye="glance", cheeks="blush")
        m "I'll consider it... Now let's circle back to you, Katie and your binge of her minge."
        call her_main("Professor.. How dare you.. I would never even think to shamelessly do something so heinous with a classmate and give you all the juicy details...", mouth="annoyed", eye="baseL")
        call her_main("For less than 40 house points.", mouth="grin", eye="wink", cheeks="blush")
        call her_main("", mouth="base", eye="glance", cheeks="blush")
        m "Maybe next time [hermione_name]. I'm a little... spent for tonight."
        call her_main("We both know you could go for longer if you wanted to...", mouth="soft", eye="glance", cheeks="blush")
        call her_main("but you’re right, we'll leave it for later.", mouth="base", eye="happy", cheeks="blush")
        call her_main("See you tomorrow [genie_name].", mouth="smile", eye="wink", cheeks="blush")

        call her_walk(action="leave", speed=2.5)

        pause 1.0
        m "...Hmmm...{w=1.0} I don't think I ever gave her points."
        pause 0.5

        show screen blkfade with d9
        stop music fadeout 5.0
        hide screen fireplace_fire
        call gen_chibi("sit_behind_desk")
        centered "{size=+7}{color=#cbcbcb}~End of part four{/color}{/size}"
        jump panty_raid_event_menu
