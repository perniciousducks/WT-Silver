

label luna_favour_2: ###SIT ON MY LAP #DONE

    m "{size=-4}(I'll just ask her to sit on my lap...){/size}"
    if lun_whoring <= 3: #FIRST TIME
        if lun_whoring <= 3:
            $ lun_whoring += 1
        call play_music("chipper_doodle")
        m "Before we get started, Would you like a seat, [lun_name]?"
        call lun_main("I would, but there's no chair [lun_genie_name]...","normal","angry","raised","mid")
        m "Well how about you come sit on my lap then?"
        call lun_main("...","upset","suspicious","angry","mid")
        m "Come on, it'll be just like santa claus."
        call lun_main("...","upset","suspicious","angry","R")
        call lun_main("You better make this worth it [lun_genie_name]...","upset","mad","angry","R")
        m "Don't worry, I'm sure you'll be very happy with your \'reward\'."
        call lun_main("...","upset","suspicious","angry","mid")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."

        $ luna_flip = -1
        $ luna_xpos = 120

        call lun_chibi("stand","300","base")
        hide screen blkfade
        with d3

        menu:
            "-Pull her onto your lap-" if lun_sub >= 2:
                if lun_sub <= 3:
                    $ lun_sub += 1
                $ luna_grope = True
                call lun_main("...","upset","suspicious","angry","R")
                call lun_main("Actually, I'm not sure if...","normal","mad","base","R")
                ">You grab Luna around the waist and pull her onto your lap."
                call lun_main("Professor! What are you doing?","upset","wide","raised","R")
                m "just giving you a helping hand..."
                ">you start slowly rubbing your crouch against her soft ass."
                m "mmm that's it..."
                call lun_main("...","normal","suspicious","sad","down")
                call lun_main("(this is so humiliating...)","upset","suspicious","sad","down")

                jump luna_lap_dance

            "-Tell her to sit down-":
                $ luna_grope = False
                m "go on [lun_name]..."
                call lun_main("...","upset","mad","angry","R")
                call lun_main("Do I really have to do this?","upset","mad","angry","R")
                m "just Sit down [lun_name]..."
                call lun_main("...","upset","mad","angry","R")
                ">Luna softly takes a seat on your lap ."
                m "mmmmm..."
                call lun_main("...","normal","suspicious","sad","R")
                call lun_main("(ugh, he's so hard...)","clench","suspicious","sad","down")

                label luna_lap_dance:
                    m "That's it, now just start moving your waist."
                ">Luna gradually starts grinding her ass against you."
                m "ughh, that's it."
                call lun_main("...","upset","mad","angry","down")
                call lun_main("are you happy now?","upset","mad","mad","R")
                m "Very..."
                call lun_main("Can I leave yet?","upset","mad","angry","mid")
                m "What? We just started!"
                call lun_main("Well I don't have all day.","upset","mad","angry","R")
                m "Hmmm, well I'll see what I can do to speed this up..."

                menu:
                    "-Grab her waist-":
                        ">You take a hold of her waist."
                        call lun_main("!!!","clench","wide","base","mid")
                        call lun_main("I don't think touching was part of the arrangement [lun_genie_name]...","upset","angry","mad","R")
                        $ current_payout = 75
                        m "Don't worry [lun_name], you'll be compensated fairly."
                        ">You pull her hard against your crouch, rubbing your cock between her cheeks."
                        call lun_main("...","grin","suspicious","sad","down")
                        m "That's it [lun_name], not much longer now."
                        call lun_main(".......","upset","mad","angry","R")
                        m "mmmm, almost there..."
                        call lun_main("What?!!!","upset","wide","mad","R")

                        show screen blkfade
                        hide screen luna_main
                        with d3

                        "Luna quickly pulls away from you and stands up."

                        $ luna_flip = 1

                        call gen_chibi("sit_behind_desk")
                        call lun_chibi("stand","desk","base")
                        hide screen blkfade

                        call lun_main("Professor!","soft","angry","mad","mid",xpos="base",ypos="base")
                        m "What on earth did you stop for?"
                        call lun_main("Sitting on your lap is one thing.","upset","mad","angry","R")
                        call lun_main("But letting you do that...","normal","suspicious","mad","mid")
                        call lun_main("I simply refuse!","clench","mad","mad","R")
                        m "fine fine."
                        call lun_main("Honestly [lun_genie_name], who do you think I am?","normal","angry","angry","mid")
                        call lun_main("I think I'd like to be paid now...","normal","angry","angry","R")
                    "-Grope her-" if luna_grope:
                        ">You start running your hands along the outside of her thighs, up to her waist and then over her belly."
                        call lun_main("!!!","clench","wide","base","mid")
                        m "mmmm, lovely."
                        ">You keep grinding your cock against her butt checks."
                        m "yes, just like that [lun_name]."
                        $ current_payout = 40
                        call lun_main("......","clench","suspicious","sad","down")
                        m "gods you've got such a nice ass."
                        ">You Start moving your hands slowly up towards her breasts"
                        call lun_main(".........","upset","suspicious","sad","R")
                        m "That's it [lun_name], just enjoy it."
                        call lun_main("..................","normal","suspicious","sad","R")
                        ">your hands are about an inch below her breasts..."
                        m "mmmm, almost there..."
                        call lun_main("..........................","normal","wide","sad","R")
                        ">Your about to reach her ample tits......"
                        call lun_main("!!!!","clench","wide","mad","mid")

                        show screen blkfade
                        hide screen luna_main
                        with d3

                        "Luna quickly pulls away from you and stands up."

                        $ luna_flip = 1

                        call gen_chibi("sit_behind_desk")
                        call lun_chibi("stand","desk","base")
                        hide screen blkfade

                        call lun_main("Professor!","upset","wide","mad","mid",xpos="base",ypos="base")
                        m "What on earth did you stop for?"
                        call lun_main("Sitting on your lap is one thing!","upset","suspicious","angry","mid")
                        call lun_main("But letting you touch me there...","normal","mad","mad","R")
                        call lun_main("I won't do it!","upset","mad","angry","R")
                        m "alright fine."
                        call lun_main("Honestly [lun_genie_name], you really need to learn some self control.","disgust","mad","mad","mid")
                        call lun_main("I think I'd like to be paid now...","upset","mad","angry","R")



            "-Do nothing-" if lun_dom < 2:
                call lun_main("...","normal","angry","angry","R")
                call lun_main("......","upset","mad","angry","R")
                call lun_main("I guess I'll start then...","normal","suspicious","angry","R")
                ">Luna lightly sits on your lap."
                m "mmmm"
                call lun_main("...","normal","angry","angry","mid")
                call lun_main("......","upset","mad","angry","R")
                call lun_main(".........","upset","mad","mad","R")
                call lun_main("Alright, time's up!","normal","base","base","R")
                ">Luna stands up from your lap"
                m "What, you barely even sat down!"
                call lun_main("*hmph* You should consider yourself lucky you got what you did [lun_genie_name]!","upset","mad","angry","R")
                m "You could have at least moved around a little."
                call lun_main("What? Who do you think I am? Some sort of harlot who'll let you grind yourself against them for as long as you want?","clench","suspicious","angry","R")
                m "well I expected at least a few minutes."
                call lun_main("Well if your that desperate...","base","seductive","base","R")
                ">Luna slams her ass into your crouch"
                m "ah..."
                call lun_main("pathetic...","upset","seductive","angry","R")
                ">She starts rocking back and forward on your lap"
                call lun_main("You really are disgusting [lun_genie_name]...","soft","seductive","base","R")
                m "mmmm"
                call lun_main("begging your students for a lap dance...","upset","mad","mad","R")
                m "yes, yes..."
                call lun_main("well you better pay extra for this...","normal","angry","base","R")
                m "of course..."
                call lun_main("...","normal","seductive","base","down")
                ">luna starts rolling her hips a little faster."
                call lun_main("a lot extra...","upset","suspicious","mad","R")
                m "of course [lun_name]..."
                call lun_main("that's it [lun_genie_name]. just enjoy it...","base","seductive","base","R")
                m "mmm, just a little more..."
                call lun_main("...","upset","mad","raised","down")
                m "yes... almost..."

                show screen blkfade
                hide screen luna_main
                with d3

                ">Luna quickly stands up."

                $ luna_flip = 1

                call gen_chibi("sit_behind_desk")
                call lun_chibi("stand","desk","base")
                hide screen blkfade

                call lun_main("Times up!","base","seductive","angry","R",xpos="base",ypos="base")
                m "What!"
                call lun_main("Times{p}up...","normal","mad","angry","mid")
                m "Ugh, fine."
                call lun_main("Glad you understand,{p} now about my payment...","upset","mad","angry","R")
                $ current_payout = 120


            "-Do nothing-" if lun_dom >= 2:
                if lun_dom <= 3:
                    $ lun_dom += 1
                call lun_main("...","normal","angry","angry","mid")
                call lun_main("......","upset","mad","angry","R")
                call lun_main("I guess I'll start then...","normal","suspicious","angry","R")
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call lun_main("...","base","seductive","base","R")
                call lun_main("You're pathetic...","upset","seductive","angry","R")
                call lun_main("THe worlds greatest wizard...","base","seductive","base","R")
                call lun_main("More like the worlds greatest pervert.","upset","suspicious","angry","R")
                if lun_genie_name == "Old man":
                    $ lun_genie_name = "Pervert"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call lun_main("*hmph* You're not even ashamed are you?","soft","seductive","base","R")
                m "of what?"
                call lun_main("What? begging your student for a lap dance.","upset","mad","angry","R")
                m "I don't recall begging."
                call lun_main("Hmmm...","normal","angry","base","R")
                ">Luna stands up slowly."
                call lun_main("Well then...","upset","mad","angry","R")
                m "what?"
                call lun_main("beg...","upset","seductive","mad","R")

                menu:
                    "-Beg-":
                        pass
                    "-Refuse-":
                        m "I don't think so [lun_name]."
                        call lun_main("*hmph* Fine...","pout","suspicious","angry","R")

                        show screen blkfade
                        hide screen luna_main
                        with d3

                        ">Luna walks around to the front of the desk."

                        $ luna_flip = 1

                        call gen_chibi("sit_behind_desk")
                        call lun_chibi("stand","desk","base")
                        hide screen blkfade

                        call lun_main("I'd like to be paid now [lun_genie_name]...","upset","mad","mad","mid",xpos="base",ypos="base")
                        $ current_payout = 100
                        m "Alright, alright. Here's your gold."
                        $ gold -= current_payout
                        $ luna_gold += current_payout
                        ">You hand Luna [current_payout] gold."
                        call lun_main("Thank you, [lun_genie_name].","normal","angry","angry","R")
                        ">Luna leaves your office."

                m "Please..."
                call lun_main("Please what?","normal","seductive","base","R")
                m "Please keep going [lun_name]..."
                ">Luna slowly places herself back on your lap."
                call lun_main("That's better isn't it?","base","angry","angry","R")
                ">She starts rocking back and forward on your lap"
                call lun_main("You're so hard...","normal","seductive","base","down")
                m "mmmm"
                call lun_main("I bet you'd cum if I kept going wouldn't you...","normal","seductive","raised","R")
                m "yes..."
                call lun_main("well you better be prepared to pay extra for the privilige...","normal","angry","angry","R")
                m "of course..."
                call lun_main("...","upset","mad","angry","R")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call lun_main("a {size=+5}lot{/size} extra...","upset","seductive","mad","R")
                m "of course [lun_name]..."
                call lun_main("Good. just enjoy yourself then...","base","happyCl","base","R")
                m "mmm, just a little more..."
                call lun_main("...[lun_genie_name]","normal","seductive","angry","R")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call lun_main("come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(agh... almost there...){/size}"
                call lun_main("come for your little girl...","base","suspicious","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna_main
                with d3
                call cum_block

                g4 "Argh! YES!"
                call lun_main("ugh... pathetic...","base","seductive","mad","R")
                call lun_main("...","upset","mad","angry","R")
                call lun_main("......","normal","mad","raised","down")
                call lun_main(".........","upset","mad","mad","down")
                call lun_main("Alright, time's up!","base","seductive","angry","R")

                show screen blkfade
                hide screen luna_main
                with d3

                ">Luna stands up from your lap"

                $ luna_flip = 1

                call gen_chibi("sit_behind_desk")
                call lun_chibi("stand","desk","base")
                hide screen blkfade

                call lun_main("*hmph* You [lun_genie_name]!","normal","suspicious","angry","mid",xpos="base",ypos="base")
                m "You can hardly blame me for this."
                call lun_main("What? You're the one who begged for it, of course it's your fault.","upset","angry","mad","R")
                m "well you didn't have to be so good at it."
                call lun_main("I was just making sure that I earned my reward.","upset","mad","angry","mid")
                call lun_main("Speaking of which...","base","seductive","base","R")
                $ current_payout = 200



        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        if current_payout <= 50:
            call lun_main("(only [current_payout]?) *hmph*","upset","mad","angry","R")
            call lun_main("Thank you, [lun_genie_name].","normal","suspicious","angry","R")
        else:
            call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
        ">Luna leaves your office."

    elif lun_whoring <= 4: #SECOND TIME
        if lun_whoring <= 4:
            $ lun_whoring += 1
        call play_music("chipper_doodle")
        m "Can I offer you another seat [lun_name]?"
        if lun_sub > lun_dom:
            call lun_main("...","normal","base","sad","down")
            call lun_main("Alright [lun_genie_name]...","normal","base","sad","R")
            m "Good girl."
            call lun_main("...","upset","base","sad","down")
        else:
            call lun_main("Fine...","normal","base","angry","R")
            call lun_main("But I expect to be fairly compensated [lun_genie_name]...","normal","angry","angry","mid")
            m "yes, yes..."
            call lun_main("...","normal","angry","angry","R")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."
        #chibi stuff
        $ luna_flip = -1
        $ luna_xpos = 120

        call lun_chibi("stand","300","base")
        hide screen blkfade
        with d3

        menu:
            "-Ask her to remove her skirt first-" if lun_sub >= 2:
                if lun_sub <= 3:
                    $ lun_sub += 1
                $ luna_grope = True
                m "How about you take off your skirt before we start?"
                call lun_main("!!!","normal","wide","sad","R")
                call lun_main("You're not serious are you?","normal","suspicious","sad","R")
                m "I am [lun_name], or do you not want hogwarts to keep purchasing new copies of the quibbler?"
                call lun_main("...","normal","suspicious","sad","down")
                call lun_main("......","normal","suspicious","sad","R")
                m "I'm waiting."
                call lun_main("Fine...","clench","suspicious","sad","down")
                hide screen luna_main
                show screen blkfade
                with d3
                $ luna_wear_bottom = False
                ">Luna slowly removes her skirt, revealing her black silk panties."
                show screen luna_main
                hide screen blkfade
                with d3
                m "I like your panties..."
                call lun_main("...","normal","suspicious","sad","down")
                call lun_main("(this is so degrading)","clench","suspicious","sad","down")
                m "Now take a seat..."
                call lun_main("yes [lun_genie_name]...","normal","suspicious","sad","R")
                ">Luna softly takes a seat on your lap."
                call lun_main("...","upset","suspicious","sad","down")
                jump luna_lap_dance_2

            "-Tell her to sit down-" if lun_sub >= lun_dom:
                $ luna_grope = False
                m "come on now..."
                call lun_main("...","upset","mad","sad","R")
                call lun_main("......","upset","mad","sad","R")
                m "Sit down [lun_name]."
                call lun_main("...","upset","mad","sad","R")
                ">Luna softly takes a seat on your lap ."
                m "mmmmm..."
                call lun_main("...","normal","suspicious","sad","R")
                call lun_main("(ugh, he's so hard...)","clench","suspicious","sad","down")

                label luna_lap_dance_2:
                    m "That's it, now just start moving your ass."
                ">Luna gradually starts grinding her waist against you."
                m "ughh, that's it."
                call lun_main("...","upset","mad","sad","down")
                call lun_main("is this alright?","normal","seductive","sad","R")
                m "yes, just keep going..."
                call lun_main("For how long?","upset","mad","sad","mid")
                m "As long as it takes [lun_name]."
                call lun_main("fine...","upset","mad","sad","R")
                call lun_main("...","upset","mad","sad","down")
                call lun_main("..........","upset","suspicious","sad","down")
                call lun_main("Is there anything I can do to speed this up?","normal","suspicious","sad","R")

                menu:
                    "-enjoy yourself-":
                        $ current_payout = 65
                        m "Just keep doing what you're doing..."
                        call lun_main("...","clench","suspicious","sad","down")
                        call lun_main("How about this?","normal","seductive","sad","R")
                        ">Luna starts jiggling her ass slightly as she rocks back and forth."
                        m "Mmmm, yes!"
                        ">You start thrusting into her ever so slightly."
                        call lun_main("...","grin","suspicious","sad","down")
                        m "That's it [lun_name], not much longer now."
                        call lun_main(".......","normal","seductive","sad","R")
                        m "mmmm, almost there..."
                        call lun_main("Already?","upset","wide","sad","R")
                        m "Almost... this is really good..."
                        call lun_main("it is?","base","seductive","sad","R")
                        m "yeah, just keep moving that perfect little ass of yours..."
                        call lun_main("...","base","seductive","sad","R")
                        call lun_main("How's this?","grin","seductive","sad","down")
                        ">She starts rocking back and forward on your lap"
                        m "mmmmm"
                        call lun_main("You're so hard [lun_genie_name]...","base","seductive","sad","down")
                        m "mmmm"
                        call lun_main("are you almost there?","normal","seductive","sad","R")
                        m "yes..."
                        call lun_main("well I expect to be-","upset","seductive","angry","R")
                        m "shhh, don't ruin it."
                        call lun_main("...","upset","mad","sad","R")
                        ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                        m "ah..."
                        call lun_main("...","upset","seductive","sad","R")
                        m "keep going [lun_name]..."
                        call lun_main("........","base","closed","sad","R")
                        m "mmm, just a little more..."
                        call lun_main("...[lun_genie_name]...","normal","angry","sad","down")
                        ">Luna starts grinding hard against your lap."
                        m "{size=-2}(mmmm...){/size}"
                        call lun_main("......","base","suspicious","sad","mid")
                        g4 "{size=+4}(agh... almost there...){/size}"
                        call lun_main("............","base","suspicious","sad","mid",tears="soft")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        ">You start shooting your load against the inside of your cloak."
                        hide screen luna_main
                        with d3
                        call cum_block

                        g4 "Argh! YES!"
                        call lun_main("ugh...","base","seductive","sad","R")
                        call lun_main("...","upset","mad","sad","R")
                        call lun_main("......","normal","mad","sad","down")
                        call lun_main(".........","upset","seductive","sad","down")
                        call lun_main("Are you finished now [lun_genie_name]?","base","seductive","sad","R")
                        m "Almost... just stay there for a little longer..."
                        call lun_main("......","base","seductive","sad","R")

                        show screen blkfade
                        hide screen luna_main
                        with d3

                        ">Luna waits for a few seconds before standing up."

                        $ luna_flip = 1
                        $ luna_wear_bottom = True

                        call gen_chibi("sit_behind_desk")
                        call lun_chibi("stand","desk","base")
                        hide screen blkfade

                        call lun_main("will that be all, [lun_genie_name]?","normal","suspicious","sad","mid",xpos="base",ypos="base")
                        m "Yes, thank you, [lun_name]."
                        call lun_main("You're welcome, [lun_genie_name].","upset","angry","sad","R")
                        call lun_main("Well I better be off to class then.","upset","mad","sad","mid")
                        m "Don't you want your payment first?"
                        call lun_main("Oh right...","base","seductive","sad","R")

                    "-Grope her-" if luna_grope:
                        $ current_payout = 35
                        ">You start running your hands along the outside of her thighs."
                        call lun_main("...","clench","wide","sad","mid")
                        m "mmmm, lovely."
                        ">You keep grinding your cock against her butt checks."
                        call lun_main("....","clench","seductive","sad","R")
                        m "yes, just like that [lun_name]."
                        "You move your hands up to her waist"
                        call lun_main("......","clench","suspicious","sad","down")
                        m "gods you've got such a nice ass."
                        call lun_main("t-thank you [lun_genie_name]...","upset","happyCl","sad","R",tears="crying")
                        ">You Start moving your hands slowly up over her smooth stomach."
                        call lun_main(".........","upset","suspicious","sad","R",tears="crying")
                        m "That's it [lun_name], just enjoy yourself..."
                        call lun_main("..................","normal","suspicious","sad","R")
                        ">your hands are about an inch below her breasts..."
                        m "mmmm, almost there..."
                        call lun_main("..........................","normal","wide","sad","R")
                        ">You quickly move your hands up and grab a hold of her supple breasts over her vest."
                        call lun_main("!!!!","clench","wide","mad","mid")
                        "Luna quickly tries to pull away from you."

                        menu:
                            "-let her up-":
                                $ current_payout = 55

                                show screen blkfade
                                hide screen luna_main
                                with d3

                                ">Luna quickly stands up and moves around to the front of your desk."

                                $ luna_flip = 1

                                call gen_chibi("sit_behind_desk")
                                call lun_chibi("stand","desk","base")
                                hide screen blkfade

                                call lun_main("Professor!","upset","wide","mad","mid",xpos="base",ypos="base")
                                call lun_main("Grabbing me there wasn't part of the deal!","normal","mad","mad","R")
                                m "I just couldn't resist..."
                                call lun_main("*hmph*","upset","mad","angry","R")
                                m "My apologies, [lun_name]."
                                call lun_main("It's alright... just don't let it happen again!","disgust","mad","mad","mid")
                                call lun_main("I think I'd like to be paid now...","upset","mad","angry","R")

                            "-Hold her down-":
                                if lun_sub <= 4:
                                    $ lun_sub += 1
                                call lun_main("Professor!","upset","wide","mad","mid")
                                call lun_main("I'd like to leave now!","normal","mad","mad","R")
                                m "just a bit longer [lun_name]..."
                                ">You start grinding your hard cock between her ample cheeks."
                                call lun_main("!!!","upset","wide","sad","down")
                                call lun_main("I insist you let me go!","pout","wide","mad","R")
                                m "If you leave now you can forget about hogwarts purchasing any more of your father's newspaper, [lun_name]."
                                call lun_main("...","upset","suspicious","sad","down")
                                call lun_main("you're despicable, [lun_genie_name]...","upset","mad","angry","R",tears="soft")
                                ">You give her tits a couple of firm squeezes..."
                                call lun_main("ah{image=textheart}...","upset","angry","sad","down",tears="soft")
                                call lun_main("this isn't right...","upset","angry","sad","R",tears="soft")
                                m "I know, I know... But it's hard to resist..."
                                call lun_main(".................","normal","seductive","sad","down",tears="soft")
                                call lun_main("....................ah...{image=textheart}","soft","seductive","sad","down",tears="soft")
                                call lun_main("[lun_genie_name], you need to stop now...","upset","angry","sad","R",tears="soft")
                                m "Just a bit longer..."
                                call lun_main("please...","upset","angry","sad","down",tears="crying")
                                m "mmmm, I suppose this will have to do..."
                                ">You give her tits a final pinch..."
                                call lun_main("ah...","upset","angry","sad","down",tears="crying")

                                show screen blkfade
                                hide screen luna_main
                                with d3

                                ">Luna quickly stands up and moves around to the front of your desk."

                                $ luna_flip = 1

                                call load_luna_clothing_saves

                                call gen_chibi("sit_behind_desk")
                                call lun_chibi("stand","desk","base")
                                hide screen blkfade

                                call lun_main("Professor!","upset","wide","mad","mid",xpos="base",ypos="base")
                                call lun_main("Grabbing me there wasn't part of the deal!","normal","mad","mad","R")
                                m "Sorry, [lun_name], I just couldn't help myself..."
                                call lun_main(".......just please try to control yourself next time...","disgust","mad","mad","mid")
                                m "So you want there to be a next time?"
                                call lun_main("as long as I'm getting paid.","upset","mad","angry","R")
                                call lun_main("speaking of which...","upset","mad","angry","mid")
                                call lun_main("can I please be paid now?","upset","mad","sad","down")


            "-Do nothing-" if lun_sub <= lun_dom:
                call lun_main("...","normal","angry","angry","mid")
                call lun_main("......","upset","mad","angry","R")
                call lun_main("I suppose I'll start then...","normal","suspicious","angry","R")
                ">Luna lightly places herself on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call lun_main("...","base","seductive","base","R")
                call lun_main("You're so pathetic...","upset","seductive","angry","R")
                call lun_main("THe worlds greatest wizard...","base","seductive","base","R")
                call lun_main("More like the worlds greatest pervert.","upset","suspicious","angry","R")
                if lun_name == "Miss Lovegood":
                    $ lun_name = "Princess"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call lun_main("*hmph* You're not even ashamed are you?","soft","seductive","mad","R")
                m "of what?"
                call lun_main("What? begging your student for a lap dance.","upset","mad","angry","R")
                m "I don't recall begging."
                call lun_main("Hmmm...","normal","angry","base","R")
                ">Luna stands up slowly."
                call lun_main("Well then...","upset","mad","angry","R")
                m "what?"
                call lun_main("beg...","upset","seductive","mad","R")
                m "Please..."
                call lun_main("Please what?","normal","seductive","base","R")
                m "Please keep going [lun_name]..."
                ">Luna slowly places herself back on your lap."
                call lun_main("That's better isn't it?","base","angry","angry","R")
                ">She starts rocking back and forward on your lap"
                call lun_main("ugh, You're so hard...","upset","suspicious","mad","down")
                m "mmmm"
                call lun_main("I bet you'd cum if I kept going wouldn't you...","base","seductive","angry","R")
                m "yes..."
                call lun_main("well you better be prepared to pay extra for the privilige...","normal","angry","angry","R")
                m "of course..."
                call lun_main("...","upset","mad","angry","R")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call lun_main("a {size=+5}lot{/size} extra...","base","seductive","mad","R")
                m "of course [lun_name]..."
                call lun_main("Good. just enjoy yourself then...","base","happyCl","base","R")
                m "mmm, just a little more..."
                call lun_main("...[lun_genie_name]","base","seductive","angry","R")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call lun_main("come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(agh... almost there...){/size}"
                call lun_main("come for your queen...","base","suspicious","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna_main
                with d3
                call cum_block

                g4 "Argh! YES!"
                call lun_main("mmmm... pathetic...","base","seductive","mad","R")
                call lun_main("...","upset","angry","angry","R")
                call lun_main("......","normal","mad","mad","down")
                call lun_main(".........","upset","suspicious","mad","down")
                call lun_main("Alright, time's up!","base","seductive","angry","R")

                show screen blkfade
                hide screen luna_main
                with d3

                ">Luna stands up from your lap"

                $ luna_flip = 1

                call gen_chibi("sit_behind_desk")
                call lun_chibi("stand","desk","base")
                hide screen blkfade

                call lun_main("*hmph* You naughty [lun_genie_name]!","normal","suspicious","angry","mid",xpos="base",ypos="base")
                m "You can hardly blame me for this."
                call lun_main("What? You're the one who begged for it, of course it's your fault.","upset","angry","mad","R")
                m "well you didn't have to be so good at it."
                call lun_main("I was just making sure that I earned my reward.","base","mad","angry","mid")
                call lun_main("Speaking of which...","base","seductive","base","R")
                $ current_payout = 200


            "-Ask Nicely-" if lun_dom >= 2:
                if lun_dom <= 3:
                    $ lun_dom += 1
                m "can you please sit on my lap [lun_name]?"
                call lun_main("...","base","seductive","base","R")
                call lun_main("well seeing as how you asked so nicely...","base","suspicious","base","R")
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call lun_main("...","base","seductive","angry","down")
                call lun_main("You're pathetic...","base","seductive","angry","R")
                call lun_main("THe worlds greatest wizard...","base","seductive","base","R")
                call lun_main("More like the worlds greatest pervert.","base","suspicious","angry","down")
                if lun_genie_name == "Old man":
                    $ lun_genie_name = "Pervert"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call lun_main("*hmph* You're not even ashamed are you?","soft","seductive","angry","down")
                m "of what?"
                call lun_main("What? begging your student for a lap dance.","base","mad","angry","R")
                m "I don't recall begging."
                call lun_main("Hmmm...","base","seductive","angry","R")
                ">Luna stands up slowly."
                call lun_main("Well then...","upset","mad","angry","R")
                m "what?"
                call lun_main("beg...","upset","seductive","mad","R")
                m "Please..."
                call lun_main("Please what?","base","seductive","raised","mid")
                m "Please keep going [lun_name]..."
                ">Luna slowly places herself back on your lap."
                call lun_main("That's better isn't it?","base","angry","angry","R")
                ">She starts rocking back and forward on your lap"
                call lun_main("You're so hard...","base","seductive","mad","down")
                m "mmmm"
                call lun_main("I bet you'd cum if I kept going wouldn't you...","base","seductive","raised","R")
                m "yes..."
                call lun_main("well you better be prepared to pay extra for the privilige...","base","angry","angry","R")
                m "of course..."
                call lun_main("...","base","mad","angry","R")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call lun_main("a {size=+5}lot{/size} extra...","base","seductive","mad","down")
                m "of course [lun_name]..."
                call lun_main("Good. just enjoy yourself then...","base","happyCl","angry","R")
                m "mmm, just a little more..."
                call lun_main("...[lun_genie_name]","base","seductive","base","R")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call lun_main("come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(agh... almost there...){/size}"
                call lun_main("come for your little girl...","soft","angry","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna_main
                with d3
                call cum_block

                g4 "Argh! YES!"
                call lun_main("ugh... pathetic...","base","seductive","mad","R")
                call lun_main("...","upset","angry","angry","R")
                call lun_main("......","base","mad","raised","down")
                call lun_main(".........","base","suspicious","mad","R")
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, that's enough now [lun_name]."
                call lun_main("Who says you get to decide when this ends?","upset","suspicious","angry","R")
                ">Luna starts rolling her hips, focusing on the head of your cock."
                g11 "ah, please, not after I just came."
                call lun_main("really?","base","mad","raised","R")
                call lun_main("But you sounded so sincere earlier when you were begging for this.","soft","seductive","sad","R")
                call lun_main("Surely you don't want it to end already?","base","seductive","angry","R")
                ">she pushes hard against your cock."
                g11 "ah..."
                call lun_main("That's it [lun_genie_name], just keep enjoying yourself.","base","mad","angry","down")
                g11 "I can't, it's too sensitive..."
                call lun_main("I don't see how that's my problem.","base","mad","sad","R")
                ">She starts moving as fast as she can."
                g11 "{size=-2}ahhh...{/size}"
                call lun_main("come on [lun_genie_name]...","base","suspicious","angry","R")
                g11 "{size=+4}aghhh!{/size}"
                call lun_main("shoot another filthy load...","base","suspicious","mad","R")
                g4 "{size=+4}*Argh!* It's too much!{/size}"
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","suspicious","mad","down")
                ">You start shooting another load against the inside of your sodden cloak."
                hide screen luna_main
                with d3
                call cum_block

                g4 "Argh!"
                call lun_main("good boy...","base","seductive","mad","R")

                show screen blkfade
                hide screen luna_main
                with d3

                ">Luna stands up from your lap"

                $ luna_flip = 1

                call gen_chibi("sit_behind_desk")
                call lun_chibi("stand","desk","base")
                hide screen blkfade

                call lun_main("*hmph* You nasty old [lun_genie_name]!","base","suspicious","angry","mid",xpos="base",ypos="base")
                m "ah..."
                call lun_main("Enjoy yourself a little too much did we?","base","angry","mad","R")
                m "That was too much, [lun_name]..."
                call lun_main("Stop complaining. I was just making sure that I earned my reward.","base","mad","angry","mid")
                call lun_main("Speaking of which...","base","seductive","base","R")
                $ current_payout = 250


        if lun_dom >= lun_sub:
            m "Alright, alright. Here's your gold."
        else:
            m "Here's your payment [lun_name]."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        if current_payout <= 50:
            call lun_main("(only [current_payout]?) *hmph*","upset","mad","angry","R")
            call lun_main("Thank you, [lun_genie_name].","normal","suspicious","angry","R")
        else:
            call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
        ">Luna leaves your office."

    elif lun_whoring >= 5 and lun_whoring < 13: #THIRD TIME
        if lun_whoring <= 5:
            $ lun_whoring += 1
        call play_music("chipper_doodle")
        m "Can I offer you another seat [lun_name]?"
        if lun_sub > lun_dom:
            call lun_main("...","normal","base","sad","down")
            call lun_main("Alright [lun_genie_name]...","normal","base","sad","R")
            m "Good girl."
            call lun_main("...","upset","base","sad","down")
        else:
            call lun_main("Fine...","normal","base","angry","R")
            call lun_main("But I expect to be fairly compensated [lun_genie_name]...","normal","angry","angry","mid")
            m "yes, yes..."
            call lun_main("...","normal","angry","angry","R")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."
        #chibi stuff
        $ luna_flip = -1
        $ luna_xpos = 120

        call lun_chibi("stand","300","base")
        hide screen blkfade
        with d3

        menu:
            "-Pull her onto your lap-" if lun_sub >= 3:
                if lun_sub <= 4:
                    $ lun_sub += 1
                $ luna_grope = True
                ">You grab Luna by the waist and pull her hard onto your lap."
                call lun_main("!!!","normal","wide","sad","R")
                call lun_main("There's no need to be so forceful [lun_genie_name]!","pout","angry","sad","R")
                m "Sorry, it's hard to help myself when I've got such an eager slut in front of me. You don't mind do you?"
                call lun_main("...","base","suspicious","sad","down")
                call lun_main("......","normal","seductive","sad","R")
                m "Do you?..."
                call lun_main("{size=-5}No...{/size}","normal","suspicious","sad","down")
                call lun_main("...","normal","suspicious","sad","R")
                m "No what?"
                call lun_main("{size=-5}No... sir...{/size}","clench","suspicious","sad","down")
                m "Good girl..."
                ">You push your cock hard against her ass."
                call lun_main("ah... thank you [lun_genie_name]...","base","suspicious","sad","down")
                call lun_main("...","upset","suspicious","sad","down")
                jump luna_lap_dance_3

            "-Tell her to sit down-" if lun_sub >= lun_dom:
                $ luna_grope = False
                if lun_sub <= 3:
                    $ lun_sub += 1
                m "why don-"
                ">Luna quickly sits down on your lap, wriggling around slightly until your cock rests between her cheeks."
                call lun_main("(ah...{image=textheart})","base","mad","sad","down")
                call lun_main("......","upset","wide","sad","R")
                m "Some one's eager today..."
                call lun_main("...","upset","mad","sad","down")
                ">Luna softly starts rocking her hips back and forth."
                m "mmmmm..."
                call lun_main("...","normal","suspicious","sad","R")
                call lun_main("(he's so hard...{image=textheart})","base","suspicious","sad","down")

                label luna_lap_dance_3:
                    m "That's it, now just start moving your ass a little more."
                ">Luna starts forcefuly grinding her supple ass against you."
                m "mmmm, that's it."
                call lun_main("...","upset","mad","sad","down")
                call lun_main("is this good?","normal","seductive","sad","R")
                m "yes, just keep going..."
                call lun_main("For how long?","upset","mad","sad","mid")
                m "As long as it takes [lun_name]."
                call lun_main("fine...","upset","mad","sad","R")
                call lun_main("...","upset","mad","sad","down")
                call lun_main("..........","upset","suspicious","sad","down")
                call lun_main("Is there anything I can do to speed this up?","base","suspicious","sad","R")
                call lun_main("Not that I want it to end...","base","suspicious","sad","down")
                call lun_main("It's just that people will start to ask questions if-","normal","seductive","sad","R")

                menu:
                    "-enjoy yourself-":
                        $ current_payout = 75
                        m "shhh... Just keep doing what you're doing..."
                        call lun_main("...","clench","suspicious","sad","down")
                        call lun_main("How about this?","normal","seductive","sad","down")
                        ">Luna starts jiggling her ass slightly as she rocks back and forth."
                        m "Mmmm, yes!"
                        ">You start thrusting into her ever so slightly."
                        call lun_main("...","pout","suspicious","sad","down")
                        m "That's it [lun_name], not much longer now."
                        call lun_main(".......","normal","seductive","sad","R")
                        m "mmmm, almost there..."
                        call lun_main("Already?","upset","wide","sad","R")
                        m "Almost... this is really good..."
                        call lun_main("it is?","base","seductive","sad","R")
                        m "yeah, just keep moving that perfect little ass of yours..."
                        call lun_main("...","base","seductive","sad","R")
                        call lun_main("How's this?","grin","seductive","sad","down")
                        ">She starts rocking back and forward on your lap"
                        m "mmmmm"
                        call lun_main("You're so hard [lun_genie_name]...","base","seductive","sad","down")
                        m "mmmm"
                        call lun_main("are you almost there?","base","seductive","sad","R")
                        m "yes..."
                        call lun_main("well I expect to be-","upset","seductive","angry","R")
                        m "shhh, don't ruin it."
                        call lun_main("...","upset","mad","sad","R")
                        ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                        m "ah..."
                        call lun_main("...","upset","seductive","sad","R")
                        m "keep going [lun_name]..."
                        call lun_main("........","base","closed","sad","R")
                        m "mmm, just a little more..."
                        call lun_main("...[lun_genie_name]...","base","angry","sad","down")
                        ">Luna starts grinding hard against your lap."
                        m "{size=-2}(mmmm...){/size}"
                        call lun_main("......","base","suspicious","sad","mid")
                        g4 "{size=+4}(agh... almost there...){/size}"
                        call lun_main("............","base","suspicious","sad","mid",tears="soft")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        ">You start shooting your load against the inside of your cloak."
                        hide screen luna_main
                        with d3
                        call cum_block

                        g4 "Argh! YES!"
                        call lun_main("ugh...","base","seductive","sad","R")
                        call lun_main("...","upset","mad","sad","R")
                        call lun_main("......","normal","mad","sad","down")
                        call lun_main(".........","upset","seductive","sad","down")
                        call lun_main("Are you finished now, [lun_genie_name]?","base","seductive","sad","R")
                        m "Almost... just stay there for a little longer..."
                        call lun_main("ok......","base","seductive","sad","down")

                        show screen blkfade
                        hide screen luna_main
                        with d3

                        ">Luna waits for a few seconds before standing up."

                        $ luna_flip = 1

                        call gen_chibi("sit_behind_desk")
                        call lun_chibi("stand","desk","base")
                        hide screen blkfade

                        call lun_main("will that be all, [lun_genie_name]?","base","suspicious","sad","mid",xpos="base",ypos="base")
                        m "Yes, thank you, [lun_name]."
                        call lun_main("You're welcome, [lun_genie_name].","upset","angry","sad","R")
                        call lun_main("Well I better be off to class then.","upset","mad","sad","mid")
                        m "Don't you want your payment first?"
                        call lun_main("Oh right...","base","seductive","sad","R")

                    "-Grope her-" if luna_grope:
                        $ current_payout = 35
                        ">You start running your hands along the outside of her thighs."
                        call lun_main("ah...{image=textheart}","base","wide","sad","mid")
                        m "mmmm, lovely."
                        ">You keep grinding your cock against her butt checks."
                        call lun_main("....","clench","seductive","sad","down")
                        m "yes, just like that [lun_name]..."
                        "You move your hands to her knees, just at the edge of her skirt."
                        call lun_main("......","base","suspicious","sad","down")
                        m "gods you've got such nice legs."
                        call lun_main("t-thank you [lun_genie_name]...","normal","happyCl","sad","R",tears="soft")
                        ">You Start slowly moving your hands back towards her waist, pulling up her skirt slightly as you go."
                        call lun_main(".........","upset","suspicious","sad","R",tears="soft")
                        m "That's it [lun_name], just enjoy yourself..."
                        call lun_main("..................","normal","suspicious","sad","R")
                        ">you move your hands to the inside of her thighs..."
                        m "mmmm, that's it..."
                        call lun_main("..........................","normal","wide","sad","R")
                        ">You start stroking the insides of her thighs, moving closer towards her sex each time."
                        call lun_main("!!!!","clench","wide","mad","mid")
                        if lun_sub <= 4:
                            $ lun_sub += 1
                        call lun_main("Professor...","upset","wide","mad","mid",tears="soft")
                        call lun_main("please...","normal","mad","mad","R",tears="soft")
                        m "just a bit longer [lun_name]..."
                        ">You start grinding your hard cock between her ample cheeks."
                        call lun_main("...","upset","wide","sad","down",tears="soft")
                        call lun_main("[lun_genie_name]...","upset","mad","angry","R",tears="soft")
                        ">You start lightly running your the tips of your fingers up and down her thighs..."
                        call lun_main("ah{image=textheart}...","upset","angry","sad","down",tears="soft")
                        call lun_main("[lun_genie_name]... this isn't right...","upset","angry","sad","R",tears="crying")
                        m "you don't seem to mind..."
                        call lun_main("(I'll let him keep going for a little bit more...)","normal","seductive","sad","down",tears="crying")
                        call lun_main("(Then I'll make him stop).......ah...{image=textheart}","soft","seductive","sad","down",tears="crying")
                        call lun_main("[lun_genie_name], how much longer do you need?...","upset","angry","sad","R",tears="crying")
                        m "Just a bit longer..."
                        ">Luna keeps rubbing her ass against your sensitive cock."
                        m "ugh, that's it [lun_name]."
                        call lun_main("p-please hurry, [lun_genie_name]...","upset","suspicious","sad","R",tears="crying")
                        m "Well I think I might know a way to speed this up."
                        call lun_main("really?","base","mad","sad","R",tears="crying")
                        call lun_main("what are-","soft","seductive","sad","R",tears="crying")
                        ">You quickly move your hands up and grab a hold of her supple breasts through her vest."
                        call lun_main("!!!!","clench","wide","mad","mid",tears="crying")
                        ">Luna's body quivers as her hips roll against you."
                        m "mmm that's it, [lun_name]..."
                        call lun_main("...","base","mad","sad","down",tears="crying")
                        m "I think someone's enjoying herself."
                        call lun_main("What?","base","mad","sad","R",tears="crying")
                        call lun_main("You think I enjoy this? Feeling your disgusting old cock grind against me?","base","mad","sad","down",tears="crying")
                        m "{size=-2}ahhh...{/size}"
                        call lun_main("while you paw at me like some filthy old pervert?","base","suspicious","sad","empty",tears="crying")
                        m "{size=+4}aghhh!{/size}"
                        call lun_main("you really are a filthy old man aren't you...","base","suspicious","sad","R",tears="crying")
                        g4 "{size=+4}*Argh!* that's is, [lun_name]! here it comes!{/size}"
                        call lun_main("!!!!","clench","wide","sad","down",tears="crying")
                        ">You start shooting a massive load against Luna's ass"
                        hide screen luna_main
                        with d3
                        call cum_block

                        g4 "Argh!"
                        call lun_main(".....","mad","wide","base","down",tears="crying")

                        show screen blkfade
                        hide screen luna_main
                        with d3

                        ">Luna stands up from your lap"

                        $ luna_flip = 1

                        call gen_chibi("sit_behind_desk")
                        call lun_chibi("stand","desk","base")
                        hide screen blkfade

                        call lun_main("*hmph*","base","suspicious","angry","mid",tears="crying",xpos="base",ypos="base")
                        m "ah... gods that was good"
                        call lun_main("I think I'd like to leave now [lun_genie_name]...","base","seductive","base","R",tears="soft")

            "-Ask Nicely-" if lun_dom >= lun_sub:
                if lun_dom <= 3:
                    $ lun_dom += 1
                m "can you please sit on my lap [lun_name]?"
                call lun_main("...","base","seductive","base","R")
                call lun_main("......","base","mad","angry","R")
                call lun_main("well seeing as how you asked so nicely...","base","suspicious","base","R")
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call lun_main("...","base","seductive","angry","down")
                call lun_main("You're pathetic...","base","seductive","angry","R")
                call lun_main("THe worlds greatest wizard...","base","seductive","base","R")
                call lun_main("More like the worlds greatest pervert.","base","suspicious","angry","down")
                if lun_genie_name == "Old man":
                    $ lun_genie_name = "Pervert"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call lun_main("*hmph* You're not even ashamed are you?","soft","seductive","angry","down")
                m "of what?"
                call lun_main("What? begging your student for a lap dance.","base","mad","angry","R")
                m "I don't recall begging."
                call lun_main("Hmmm...","base","seductive","angry","R")
                ">Luna stands up slowly."
                call lun_main("Well then...","upset","mad","angry","R")
                m "what?"
                call lun_main("beg...","upset","seductive","mad","R")
                m "Please..."
                call lun_main("Please what?","base","seductive","raised","mid")
                m "Please keep going [lun_name]..."
                ">Luna slowly places herself back on your lap."
                call lun_main("That's better isn't it?","base","angry","angry","R")
                ">She starts rocking back and forward on your lap"
                call lun_main("You're so hard...","base","seductive","mad","down")
                m "mmmm"
                call lun_main("I bet you'd cum if I kept going wouldn't you...","base","seductive","raised","R")
                m "yes..."
                call lun_main("well you better be prepared to pay extra for the privilige...","base","angry","angry","R")
                m "of course..."
                call lun_main("...","base","mad","angry","R")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call lun_main("a {size=+5}lot{/size} extra...","base","seductive","mad","down")
                m "of course [lun_name]..."
                call lun_main("Good. just enjoy yourself then...","base","happyCl","angry","R")
                m "mmm, just a little more..."
                call lun_main("...[lun_genie_name]","base","seductive","base","R")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call lun_main("come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(agh... almost there...){/size}"
                call lun_main("come for your little girl...","soft","angry","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna_main
                with d3
                call cum_block

                g4 "Argh! YES!"
                call lun_main("ugh... pathetic...","base","seductive","mad","R")
                call lun_main("...","upset","angry","angry","R")
                call lun_main("......","base","mad","raised","down")
                call lun_main(".........","base","suspicious","mad","R")
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, that's enough now [lun_name]."
                call lun_main("Who says you get to decide when this ends?","upset","suspicious","angry","R")
                ">Luna starts rolling her hips, focusing on the head of your cock."
                g11 "ah, please, not after I just came."
                call lun_main("really?","base","mad","raised","R")
                call lun_main("But you sounded so sincere earlier when you were begging for this.","soft","seductive","sad","R")
                call lun_main("Surely you don't want it to end already?","base","seductive","angry","R")
                ">she pushes hard against your cock."
                g11 "ah..."
                call lun_main("That's it [lun_genie_name], just keep enjoying yourself.","base","mad","angry","down")
                g11 "I can't, it's too sensitive..."
                call lun_main("I don't see how that's my problem.","base","mad","sad","R")
                ">She starts moving as fast as she can."
                g11 "{size=-2}ahhh...{/size}"
                call lun_main("come on [lun_genie_name]...","base","suspicious","angry","R")
                g11 "{size=+4}aghhh!{/size}"
                call lun_main("shoot another filthy load...","base","suspicious","mad","R")
                g4 "{size=+4}*Argh!* It's too much!{/size}"
                call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","suspicious","mad","down")
                ">You start shooting another load against the inside of your sodden cloak."
                hide screen luna_main
                with d3
                call cum_block

                g4 "Argh!"
                call lun_main("good boy...","base","seductive","mad","R")

                show screen blkfade
                hide screen luna_main
                with d3

                ">Luna stands up from your lap"

                $ luna_flip = 1

                call gen_chibi("sit_behind_desk")
                call lun_chibi("stand","desk","base")
                hide screen blkfade

                call lun_main("*hmph* You nasty old [lun_genie_name]!","base","suspicious","angry","mid",xpos="base",ypos="base")
                m "ah..."
                call lun_main("Enjoy yourself a little too much did we?","base","angry","mad","R")
                m "That was too much [lun_name]..."
                call lun_main("Stop complaining. I was just making sure that I earned my reward.","base","mad","angry","mid")
                call lun_main("Speaking of which...","base","seductive","base","R")
                $ current_payout = 250


            "-Beg-" if lun_dom >= 3:
                if lun_dom <= 3:
                    $ lun_dom += 1
                m "can you please sit on my lap [lun_name]?"
                call lun_main("...","base","seductive","base","R")
                call lun_main("......","base","mad","angry","R")
                call lun_main("keep going...","base","suspicious","base","R")
                m "please place your perfect little ass on my lap princess..."
                call lun_main("that's better...","base","suspicious","base","R")
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call lun_main("...","base","seductive","angry","down")
                call lun_main("that's it [lun_genie_name]...","base","seductive","base","R")
                call lun_main("just sit back and enjoy yourself...","base","seductive","base","R")
                call lun_main("enjoy the feeling of your disgusting old cock rub against me...","base","suspicious","angry","down")
                ">Luna stands moving her hips backward and forwards..."
                m "ah..."
                call lun_main("*hmph* that's it... tell me how good it feels.","soft","seductive","angry","down")
                m "w-what?"
                call lun_main("tell me how good it feels to rub that filthy cock of your against me...","base","mad","angry","R")
                m "..."
                call lun_main("go on... or else.","base","seductive","angry","R")
                ">Luna goes to stand up slowly."
                m "alright... I'll do it."
                ">Luna sits back down onto your lap"
                call lun_main("good boy...","base","seductive","base","R")
                m "it's like I'm rubbing up against a ...cloud..."
                call lun_main("a cloud?","upset","seductive","raised","R")
                m "I mean it's soft..."
                ">Luna slowly grinds against your shaft."
                call lun_main("I suppose that's better than nothing.","base","angry","raised","R")
                m "mmmm, keep going [lun_name]..."
                call lun_main("pervert...","base","suspicious","mad","R")
                m "yes..."
                call lun_main("do you even know old I am?","base","angry","angry","R")
                m "of course..."
                call lun_main("well...","base","mad","angry","R")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah... 18?"
                call lun_main("{size=-5}18?{/size} you don't sound so sure about that [lun_genie_name]...","base","seductive","mad","down")
                m "..."
                call lun_main("what if I'm 17?","base","suspicious","sad","R")
                m "mmm..."
                call lun_main("I bet that'd just make you harder wouldn't it?","normal","seductive","base","R")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call lun_main("come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(agh... almost there...){/size}"
                call lun_main("come for your little girl...","soft","angry","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna_main
                with d3
                call cum_block

                g4 "Argh... YES!"
                call lun_main("ugh... pathetic...","base","seductive","mad","R")
                call lun_main("...","upset","angry","angry","R")
                call lun_main("......","base","mad","raised","down")
                call lun_main(".........","base","suspicious","mad","R")
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, no more please [lun_name]."
                call lun_main("good boy...","base","seductive","mad","R")
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3
                call lun_main("*hmph* You're such nasty old [lun_genie_name]!","base","suspicious","angry","mid")
                call lun_main("But I suppose I don't mind, as long as I get my reward.","base","mad","angry","mid")
                call lun_main("Speaking of which...","base","seductive","base","R")
                $ current_payout = 250


        if lun_dom >= lun_sub:
            m "Alright, alright. Here's your gold."
        else:
            m "Here's your payment [lun_name]."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        if current_payout <= 50:
            call lun_main("(only [current_payout]?) *hmph*","upset","mad","angry","R")
            call lun_main("Thank you, [lun_genie_name].","normal","suspicious","angry","R")
        else:
            call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
        ">Luna leaves your office."

    else: #Hermione involved
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        m "Can I offer you another seat [lun_name]?"
        call lun_main("so you want another lapdance...","normal","seductive","angry","mid")
        m "if it's not too much trouble..."
        call lun_main("not at all...","base","seductive","base","R")
        call lun_main("but just for fun... why don't you get hermione up here?","base","angry","sad","down")
        m "really?"
        call lun_main("...","normal","angry","angry","mid")
        m "Alright, I'm not going to say no to that!"
        call lun_main("good... let me just get in position first...","base","seductive","angry","mid")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."
        #chibi stuff
        $ luna_flip = -1
        $ luna_xpos = 120
        $ luna_chibi_xpos = 300
        hide screen blkfade
        with d3
        ">Luna lightly sits on your lap."
        m "mmmm"
        ">You start to feel yourself get hard against her ass"
        call lun_main("go on... bring her up here...","upset","mad","angry","R")
        ">you summon hermione up to your office."
        call play_sound("door")
        call her_chibi("stand","desk","base")

        call update_her_uniform
        call ctc

        call her_main("hello Professor!","base","closed")
        call her_main("hey luna! oh, has he got you on lapdance duty today then?","smile","happyCl",emote="06")
        call lun_main("if you can even call it that...","normal","seductive","angry","R")
        call lun_main("most of the time he just makes me grind up against him while he creams his robe...","base","base","base","down")
        call lun_main("I feel bad for the elves who have to clean it up...","base","mad","angry","down")
        ">Luna starts bouncing slowly on your lap, lifting her weight on and off your crouch."
        call her_main("mmm, so what am I here for then?","base","glance")
        m "ah... ask luna..."
        call lun_main("well I was thinking you could give him a little show while I grind a load out of him...","normal","wide","sad","R")
        call her_main("mmmm, what did you have in mind?","base","suspicious")
        call lun_main("Playing with those nice tits of your would probably do it...","base","base","sad","R")
        m "ah... yes..."
        call her_main("probably...","base","down")
        call her_main("but are you sure it's just him who wants a show?","base","suspicious")
        call lun_main("what?","open","wide","sad","mid", cheeks="blush")
        ">Luna starts grinding even faster."
        call lun_main("what are you talking about?","normal","wide","sad","down", cheeks="blush")
        call her_main("from the looks of it you don't need any help cranking a nice big load out of [genie_name]...","open","down")
        call her_main("so the only reason you'd bring me up here to show of my tits...","base","glance")
        call her_main("is so you can get a look as well...","base","suspicious")
        call her_main("not that I mind...","smile","baseL")
        call her_main("I just want you to be honest...","base","squint")
        call lun_main("...","normal","mad","sad","R", cheeks="blush")
        call lun_main("Fine...","upset","mad","sad","down", cheeks="blush")
        call her_main("say it...","base","suspicious")
        call lun_main("I want to look at your boobs alright!","open","happyCl","sad","mid", cheeks="blush")
        ">hermione quickly removes her top and bra."
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call update_her_uniform
        call her_main("see, that's not so hard now is it?","base","suspicious")
        call lun_main("no...","base","seductive","sad","mid", cheeks="blush")
        ">Luna slows down, but starts grinding her mound hard against your cock."
        call her_main("now why don't you too perverts just sit back and relax...","base","down")
        call set_her_action("lift_breasts")
        call her_main("while I give you something fun to look at ok?","grin","baseL")
        call lun_main("yes hermione...","base","base","sad","mid", cheeks="blush")
        m "Yes..."
        call lun_main("mmmmm, he's so hard...","base","seductive","sad","down", cheeks="blush")
        call set_her_action("pinch")
        call her_main("I can imagine","grin","dead")
        m "ugh..."
        call lun_main("he's probably going to cum soon...","base","mad","sad","R", cheeks="blush")
        m "probably..."
        call her_main("and what about you?","base","glance")
        call set_her_action("covering")
        call her_main("how do you feel?","base","down")
        call lun_main("so good...","base","seductive","sad","down", cheeks="blush")
        call lun_main("...","base","mad","sad","up", cheeks="blush")
        ">luna tilts her hips back, grinding as much of her sex against you as possible..."
        ">you swear you can feel her wetness seeping through your robe."
        m "ah..."
        call set_her_action("pinch")
        call her_main("good...","open","baseL")
        call lun_main("ah...","base","angry","sad","up", cheeks="blush")
        ">Luna starts rubbing hard against your lap."
        m "{size=-2}(mmmm...){/size}"
        call lun_main("yes...","base","seductive","sad","up", cheeks="blush")
        call set_her_action("lift_breasts")
        call her_main("why don't you two see if you can cum together?","base","glance")
        g4 "{size=+4}agh... almost there...{/size}"
        call lun_main("m-me too...","base","seductive","sad","up", cheeks="blush")
        call set_her_action("pinch")
        call her_main("cum for me you nasty perverts!","base","suspicious")
        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
        call lun_main("ah...{image=textheart}{image=textheart}{image=textheart}","open","angry","sad","up", cheeks="blush")
        ">You start shooting your load against the inside of your cloak as you feel an explosion of wetness from luna's pussy."
        hide screen luna_main
        with d3
        call cum_block

        g4 "Argh! YES!"
        call lun_main("ugh... amazing...","base","seductive","sad","up", cheeks="blush")
        call set_her_action("covering")
        call her_main("mmmm...","base","glance", cheeks="blush")
        call lun_main("...","base","seductive","sad","up", cheeks="blush")
        call lun_main("......","base","angry","sad","down", cheeks="blush")
        call lun_main(".........","base","seductive","sad","R", cheeks="blush")
        ">Luna slowly keeps rolling her sensitive pussy on your cock..."
        g4 "ugh, that's enough now [lun_name]."
        call lun_main("alright...","normal","base","sad","down", cheeks="blush")
        ">Luna stands up from your lap"
        $ luna_flip = 1
        $ luna_xpos = 600
        $ luna_chibi_xpos = 500
        hide screen blkfade
        with d3

        $ hermione_wear_top = True
        $ hermione_wear_bra = True
        call update_her_uniform
        call set_her_action("none","update")
        call her_main("feel better you two?","base","glance")
        call lun_main("yes...","base","mad","sad","up", cheeks="blush")
        m "ah... you sluts..."
        call her_main("well come on then luna, we've got some studying to do. Can you pay us now, [genie_name]?","base","down")

        m "Alright, alright. Here's your gold and points."
        $ gryffindor += 25
        $ ravenclaw += 25
        m "15 points to \"gryffindor\" and \"ravenclaw\"."
        $ gold -= 80
        $ luna_gold += 40
        m "and here's your gold."
        ">You hand Luna and hermione 40 gold each."
        call her_main("Thank you [genie_name]!","base","base")
        call lun_main("...Thank you sir.","normal","seductive","sad","R")
        ">Luna and hermione leave your office, talking as they go."

        $ hermione_busy = True


    hide screen hermione_main
    hide screen luna_main
    with d3

    call gen_chibi("sit_behind_desk")
    pause.2

    call play_sound("door")
    call lun_chibi("hide")
    call her_chibi("hide")

    $ luna_busy = True

    jump main_room
