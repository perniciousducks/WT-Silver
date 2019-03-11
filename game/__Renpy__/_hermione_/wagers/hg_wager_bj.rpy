label hg_wager_bj:
    g9 "Well if you want to avoid losing the points you could come over here and get on your knees."
    m "And put my dick in your mouth!"
    
    if her_whoring < 15:
        call her_main("I don't want to lose those points, but that is too much!", mouth="angry", eye="angry")
        call her_main("Isn't there anything else I could do?", mouth="open", eye="base")
        m "You're no fun!"
        m "Come over here and let me give your butt a squeeze then I'll only deduct 10 points from Gryffindor."
        if her_whoring < 9:
            call her_main("No! what kind of girl do you take me for [genie_name]!", mouth="scream", eye="angry")
            m "Fine, 20 points from Gryffindor!"
            $ gryffindor -= 20
            pause.5
            call her_chibi("leave","door","base")
        else:
            call her_main("Okay, I can do that", mouth="open", eye="soft", cheeks="blush")
            call her_main("", mouth="base", eye="soft")
            g9 "Well, get over here then!"
            call her_walk_desk_blkfade
            call blkfade
            hide screen genie
            call her_main("Should I turn around, [genie_name]?", mouth="open", eye="worriedCl")
            call her_main("", mouth="upset", eye="worried")
            m "No, not this time."
        
            call her_main("Okay then...", mouth="annoyed", eye="glanceL")
            show screen no_groping_01
            with d1
            $ menu_x = 0.5
            $ menu_y = 0.3 #Menu is moved down.
            call hide_blkfade
            call ctc
            show screen groping_01
            m "Have you been working out [hermione_name]? This feels great!"
            call her_main("No...can we just get this over with?", mouth="annoyed", eye="glance")
            call her_main("{size=-5}All this because of a stupid card game{/size}", mouth="upset", eye="worriedCl")
            m "I know, we should definitely do this again"
            if hg_pf_DanceForMe_OBJ.points >= 2: #If snape walked in during the dance favour.
                call play_music("dark_fog")
                call play_sound("door")
                call sna_walk("door","mid",2)    
                call bld
                call sna_main("",xpos="base",ypos="base")
                call ctc
                call sna_main( "Hello Geni...", face="snape_09")
                call sna_main( "What do we have here?!?", face="snape_20")
                call her_main("{size=+5}Professor Snape?!{/size}", mouth="shock", eye="shocked", xpos="left",ypos="base")
                call her_main("It's not what it looks like!", mouth="scream", eye="wideL")
                hide screen hermione_main
                call sna_main( "So you're not having your headmaster feel you up?", face="snape_20")
                call sna_main( "And enjoying it, by the looks of it!", face="snape_20")
                call her_main("I knew playing another round of cards wasn't a good idea...", mouth="mad", eye="worriedCl", cheeks="blush")
                call her_main("...", mouth="annoyed", eye="annoyed", cheeks="blush")
                call her_main("Take your hands off me now!!", mouth="scream", eye="angryCl", cheeks="blush")
                m "Fine, calm down miss Granger"
                call her_main("Don't tell me to calm down!!!", mouth="scream", eye="angry", cheeks="blush")
                hide screen hermione_main
                call sna_main("Don't feel as if you have to stop on my behalf.", face="snape_01")
                m "Fine, I'll stop... But I'm still taking 20 points from Gryffindor!"
                #call blkfade
                show screen no_groping_01
                ">You take your hands off Hermione"
                hide screen blktone8 #resets hermione to center of room and genie to sitting down
                hide screen ctc
                hide screen bld1
                call her_chibi("stand","mid","base")
                call gen_chibi("sit_behind_desk")
                call sna_main("The perfect Hermione Granger letting her headmaster feel her up over a card game and some house points!", face="snape_15")
                call sna_main("How sweet...!", face="snape_14")
                call her_main("Can I leave now?", mouth="annoyed", eye="down")
                m "You are excused miss Granger, but I will be taking 20 points from Gryffindor."
                $ gryffindor -= 20 #should take gryffindor points and then hermione leaves
                hide screen bld1
                hide screen hermione_main
                with d3
                call her_walk("mid","leave",2)
                call sna_main("How did you talk her into that?", face="snape_18")
                m "We made a bet involving house points and she lost, why did you have to barge your way in like that?"
                m "It was just getting good!"
                call sna_main("You should hang a tie on the door or something!", face="snape_02")
                call sna_main("How was I supposed to know you were busy with the girl?", face="snape_03")
                m "Just knock next time!"
                m "It's not like I know how to lock that door!"
                m "Can't a mythical creature feel up a schoolgirl in peace around here?"
                call sna_main("Fine, I'll leave you to it, I've seen more of her before anyway...", face="snape_06")
                hide screen bld1 #screen fades black and snape walks out
                with d3
                call sna_walk("mid","leave",3)
            else : #If she hasn't stripped twice.
                call her_main("No, it's bad enough doing this to gain house points, it's much worse to prevent losing them!", mouth="clench", eye="angryL")
                m "You don't enjoy it? Even a little?"
                call her_main("No, Sir. I'm just doing this to fix the problem I created...", mouth="disgust", eye="glance")
                m "Well, to each their own, I am enjoying this very much!"
                call her_main("Are you done yet?")
                m "Fine, I'll let you go..."
                show screen no_groping_01
                m "I'll only take 10 points from Gryffindor as we agreed."
                m "10 Points from Gryffindor!"
                $ gryffindor -= 10
                call blkfade
                hide screen no_groping_01
                call her_chibi("stand","mid","base")
                call gen_chibi("sit_behind_desk")
                call hide_blkfade
                call her_main("Thank you, [genie_name]", mouth="open", eye="base")
                hide screen hermione_main
                with d3
                call her_walk("mid","leave",2)
    else: #If her whoring is higher than 15 (when she can do blowjob favour)
        call her_main("Gryffindor really can't afford to lose 20 points...", mouth="soft", eye="worried")
        call her_main("Okay then, I'll do it", mouth="open", eye="closed")
        if hg_pf_SuckIt_OBJ.points > 0: #if shes done the blowjob favour these show
            call her_main("Not like I haven't done it before", mouth="base", eye="happy", cheeks="blush")
            if her_whoring > 18:
                call her_main("And it does feel good having my mouth full of your cock...", mouth="soft", eye="happyCl", cheeks="blush")
        m "Get over here then!"
        call her_walk_desk_blkfade #Fade to black and then hermione is sucking genies dick with him stood up, unless theres a chibi for him sitting down
        call play_music("playful_tension")
        hide screen hermione_main
        hide screen genie
        call her_chibi("hide")
        show screen chair_left
        call u_play_ani #Should start the blowjob animation
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc
        call her_main("*Urk*, *Slurp*, *Gobble*",ypos="head") #should have her head showing while sucking his cock.
        m "Oh, that's great"
        m "Put some work into it."
        call her_main("*Gulp*, *Gobble*, *Gltch*")
        m "Your mouth feels amazing, you're a natural!"
        call u_pause_ani
        call her_main("I'm glad you like it [genie_name]")
        call u_play_ani
        call her_main("*Gobble*, *Slurp*, *Gobble*")
        call play_music("dark_fog")#Snape walks in
        call play_sound("door")
        call sna_walk("door","mid",2)
        call bld
        call sna_main("", face="snape_01",xpos="base",ypos="base")
        call ctc
        call sna_main("I want a rematch!", face="snape_05")
        call u_pause_ani
        m "{size=-5}Don't stop, [hermione_name]!{/size}"
        m "What do you mean, rematch? I beat you fair and square!"
        call u_play_ani
        call her_main("*Slurp*, *Gulp*, *Urk*", ypos="head")
        call sna_main("I'm certain you were cheating, my deck is way better than yours", face="snape_03")
        call sna_main("Hold on... what's that noise?", face="snape_17")
        m "Probably ghosts {size=-5}This place must be haunted{/size}"
        m "And I'm just better than you, just accept it."
        call her_main("*Gulp*, *Gobble*, *Gltch*")
        call sna_main("{size=-5}That doesn't sound like any ghost I've ever heard...{/size}", face="snape_01")
        call sna_main("Are you sure?", face="snape_11")
        call her_main("*Slurp*, *Gobble*, *Urk*")
        call sna_main("There it is again!", face="snape_05")
        m "Yes, definitely ghosts..."
        m "Are you changing the subject now because you can't accept the fact I beat you at wizard cards!"
        m "{size=-5}I'm about to cum [hermione_name]!{/size}"
        call her_main("*Gurk*, *Gulp*, *Gulp*")
        call sna_main("No, something is going on here, what are you doing?", face="snape_07")
        m "...Just standing at my desk."
        menu:
        #Tell him not to worry about it.
        #Tell him the ghost is gone.
            "-Tell him not to worry about it.-":
                m "There's nothing suspicious happening here {size=-5}Ugh!{/size}"
                call ctc
                hide screen bld1
                call blkfade
                call set_u_ani("cum_in_mouth_ani")
                call u_play_ani
                call cum_block
                g4 "{size=+7}ARGH!{/size}"
                call sna_main("...", face="snape_17")
                m "..."
                call sna_main("Hmm, it seems the weird sound is gone", face="snape_11")
                call sna_main("I’ll leave you to it then...", face="snape_18")
                call sna_walk("mid","door",3) #snape walks to the door, pauses on gulp sound
                pause.2
                $ renpy.play('sounds/gulp.mp3')
                call her_main("*Gulp*", mouth="full_cum", eye="ahegao")
                $ renpy.play('sounds/07_run.mp3') #snape runs back and draws his wand
                pause 2
                show screen snape_defends
                g4 "...?!"
                call sna_main("Reveal yourself! I won't let you harm him!", face="snape_14")
                m "Severus, wait!"
                call sna_main("I knew something was wrong from the start, you can't hide from me, now reveal yourself or prepare to die!", face="snape_03")
                $ uni_sperm = True #Should cover her in cum
                if hg_pf_DanceForMe_OBJ.points < 2: #if hermione hasn't stripped twice
                    m "What are you doing Severus?"
                    call her_main("...")
                    m "You're being very strange..."
                    g4 "I didn’t know you cared so much about my well being..."
                    call sna_main("I thought... never mind, I'll just go.", face="snape_11")
                    call sna_chibi("stand","mid","base",flip=True) #snape turns and leaves
                    hide screen bld1
                    with d3
                    pause.2
                    call sna_walk("mid","leave",3)
                else: #if hermione has stripped twice (so snape walked in on her)
                    call sna_main("Miss Granger?! I tho-... I...")
                    
                    if her_whoring > 20:
                        call her_main("Hello, Professor Snape.", mouth="cum", eye="base")
                        call her_main("I was just giving the headmaster some help with an ‘itch'", mouth="soft", eye="soft")
                        call sna_main("I was expecting a poor excuse, at least you're honest with it!", face="snape_17")
                        call her_main("Well I've done a lot worse in here...", mouth="smile", eye="soft", cheeks="blush")
                        call sna_main("I bet you have!", face="snape_13")
                    else: #whoring of 20 or less
                        call u_end_ani
                        call her_chibi("stand","desk","base")
                        call gen_chibi("sit_behind_desk")
                        call her_main("Oh, hello there professor...", mouth="cum", eye="glanceL", cheeks="blush")
                        call her_main("I was just helping the headmaster with some cleaning under his desk", mouth="cum", eye="down", cheeks="blush")
                        $ random_choice = renpy.random.randint(0, 2)
                        if random_choice == 0:
                            call sna_main("Sure... And I live a double life as a death eater...", face="snape_13")
                        elif random_choice == 1:
                            call sna_main("Sure... And I'm the sheriff of Nottingham...", face="snape_13")
                        else:
                            call sna_main("Sure... And my name is Hans Gruber...", face="snape_13")
                    m "I believe that your work is done Miss Granger, I'll refrain from deducting those points...."
                    call sna_main("Avoiding house point deductions are we? Is it that simple to get in your pants miss Granger?", face="snape_14")
                    call sna_main("If I had known...", face="snape_18")
                    call her_main("In your dreams...!", mouth="annoyed", eye="annoyed")
                    call sna_main("In any case, you're a lucky man... Albus.", face="snape_21")
                    call sna_main("I'll leave you two to it....", face="snape_09")
                    call sna_chibi("stand","mid","base",flip=True) #snape turns and leaves
                    hide screen bld1
                    with d3
                    pause.2
                    call sna_walk("mid","leave",3)
                m "Well, that was something..." 
                $ uni_sperm = False
                if her_whoring < 20: #if she has lower whoring than 21
                    call her_main("That was mortifying!", mouth="angry", eye="angryCl")
                    call her_main("How could you make me keep going?!?", mouth="angry", eye="angry")
                    m "Well, you were down there already, how could I not?"
                    call her_main("Well, he found out anyway!", eye="angryCl")
                    m "And he didn't care, I don't see the problem here."
                    call her_main("You are unbelievable sometimes!", eye="angry")
                    call her_main("I'm going now, don't expect me to do anything for you any time soon!", mouth="scream", eye="angry")
                    jump end_hg_pf #should reset it all
                else: #if whoring is higher than 20
                    call her_main("The old me would have been embarrassed by that...", mouth="clench", eye="concerned", cheeks="blush")
                    call her_main("But I thought it was hot!", mouth="grin", eye="happy", cheeks="blush")
                    g9 "I'll bet you did!"
                    call her_main("I've got to lose to you more often!", mouth="smile", eye="soft")
                    m "Well you did a great job, I'll try to win even harder now!"
                    call her_main("Well anyway, I must be going. Good bye [genie_name]", mouth="open", eye="base")
                    jump end_hg_pf #should reset it all
            "-Tell Him the ghost is gone-":
                g4 "Wait..."
                call her_main("Glick?")
                m "No, I think I think I should be able to exorcise these spirits myself..."
                call sna_main("You can do that?",face="snape_11")
                call her_main("...")

                if her_whoring > 21:
                    call her_main("*Slurp*, *Slurp*, *Gobble*")
                    g4 "Ghh, of... of course I can..."
                    call sna_main("I didn't think you could still use your powers like that...", face="snape_11")
                    call her_main("*Gltch*, *Slurp*, *Gobble*")
                    g4 "What? Oh, yeah... of course I can, I've exercised plenty..."
                    call her_main("*Gulp*, *Gulp*, *Gobble*")
                    g4 "ARGH... plenty"
                    call sna_main("Are you...","snape_05")
                    menu:
                        "-Try to get him to Leave-":
                            m "Fine? Yes, I just need some concentration... It'd be easier if you left me to it. The final expulsion could become quite messy..."
                            call her_main("*...?*")
                            call sna_main("Well, I'd love to see that...","snape_02")
                            m "No... Gngh, Trust me. You don't... Now, if you could..."
                            call sna_main("Fine, but you're going to have to teach me how to do that later...","snape_01")
                            m "Not sure if that's...."
                            call her_main("*Slurp*, *Slurp*, *Gobble*")
                            g4 "Oh, holy spirit that resides in this place..."
                            call her_main("*Slurp*, *Slurp*, *Urk*")
                            g4 "Please help me release this anguish... I mean, let me help release you from this anguish."
                            call sna_main("Well, you seem to know what you're doing so I'll leave you to it...","snape_05")
                            hide screen bld1
                            with d3
                            pause.2
                            call sna_walk("mid","leave",3)
                            g4 "And not a moment to soon.... Take this you whore!"
                            call ctc
                            hide screen bld1
                            call blkfade
                            call set_u_ani("cum_in_mouth_ani")
                            call u_play_ani
                            call cum_block
                            $ uni_sperm = True #Should cover her in cum.
                            call her_main("*Cough*,*Cough*")
                            m "Who said you could continue?"
                            call her_main("From my perspective it looks like you appreciated the initiative...", mouth="cum", eye="soft")
                            m "..."
                            m "Fine, I won't deduct those points..."
                            call her_main("Thank you...", mouth="open", eye="base")
                            call her_main("In that case I'll take my leave...", mouth="smile", eye="happy")
                            g9 "That girl..."
                            jump end_hg_pf #should reset hermione if I understand correctly.
        
                        "-Let her keep going and deal with the aftermath-":
                            m "Yeah... I'm good,"
                            call her_main("*Slurp*, *Slurp*, *Gobble*")
                            call sna_main("Is there anything I could assist with?","snape_05")
                            g4 "{size=+7}What?!?{/size}"
                            call her_main("...?")
                            call sna_main("With the exorcism...", face="snape_16")
                            m "Oh..."
                            call her_main("*Slurp*, *Slurp*, *Slurp*")
                            m "No... It's all good... I can feel the ghostly presence being expelled as we speak..."
                            g4 "Now take this you whore!"
                            hide screen bld1
                            call blkfade
                            call set_u_ani("cum_in_mouth_ani")
                            call u_play_ani
                            call cum_block
                            call ctc
                            g4 "..."
                            call sna_main("...",face="snape_11")
                            m "..."
                            call sna_main("I had no clue exorcism would be this...",face="snape_03")
                            call sna_main("Extreme...","snape_02")
                            m "Hah, yeah... But I've done this plenty of times..."
                            m "Actually, there's quite a bit of ghostly residue I have to deal with now so it might be best if..."
                            call sna_main("Whatever, I'd just leave it to the house elves...","snape_03")
                            m "It's not as simple as it may seem, it's not like warm water is going to do it..."
                            call sna_main("Fine, I'll head off in that case.","snape_01")
                            hide screen bld1 #should go black
                            with d3
                            pause.2
                            call sna_walk("mid","leave",3)
                            m "You can come out now [hermione_name]..."
                            $ uni_sperm = True #Should cover her in cum
                            call her_main("Thank you for your ghostly residue, [genie_name]", mouth="cum", eye="ahegao")
                            m "You're welcome, I can't believe he bought it..."
                            call her_main("What do you expect from the head of Slytherin?", mouth="cum", eye="narrow")
                            m "yes.. Well.. I think that's enough for today."
                            m "You've done more than enough to save those points."
                            call her_main("Thank you, [genie_name]", mouth="smile", eye="happy")
                            if daytime: #should play if day time
                                call her_main("Good bye.", mouth="open", eye="base")
                                m "Bye, [hermione_name]"
                            else:
                                call her_main("Good night.", mouth="open", eye="base")
                                m "Good night, [hermione_name]"
                            $ uni_sperm = False
                            jump end_hg_pf
                else: #whoring not higher than 21
                    call her_main("*Mmphaa...*")
                    m "Hold on... Yes, I think the ghostly presence has departed..."
                    call sna_main("Already?",face="snape_05")
                    g4 "Yes, they must've felt how powerful my exorcistic abilities were and moved on somewhere else..."
                    call sna_main("Well that's no fun... I was hoping to see it happen for myself.",face="snape_03")
                    m "Trust me, there's not going to be any watching going on here..."
                    call sna_main("...",face="snape_05")
                    call sna_main("Anyway, I was coming to see if you were up for another round of cards...", face="snape_17")
                    call sna_main("But I suppose you're quite spent after that whole ordeal", face="snape_02")
                    #
                    #
                    # Add special cardgame match?
                    #
                    #
                    m "Yes, I'm not in the mood now anyway...."
                    call sna_main("...",face="snape_05")
                    call sna_main("I'll just go then.",face="snape_01")
                    hide screen bld1
                    with d3
                    pause.2
                    call sna_walk("mid","leave",3)
                    m "..."
                    g4 "...Why did you stop?"
                    call her_main("What?", mouth="annoyed", eye="annoyed")
                    call her_main("I thought you wanted me to...", mouth="clench", eye="down")
                    m "If I wanted you to then I would've said so..."
                    call her_main("I could continue if you want me to...", mouth="soft", eye="soft")
                    m "No, the mood's ruined now..."
                    call her_main("Are you still taking those points away?", mouth="open", eye="base")
                    menu: 
                        "-No-":
                            m "No, you're excused..."
                            call her_main("Thank you professor...", mouth="smile", eye="happy")
                            jump end_hg_pf
                        "-Yes-":
                            m "Of course I am, you didn't finish the job!"
                            call her_main("...", mouth="annoyed", eye="annoyed")
                            call her_main("But, Snape was going to...")
                            call her_main("...", mouth="upset", eye="down")
                            call her_main("Fine...", mouth="clench", eye="annoyed")
                            m "20 Points from Gryffindor!"
                            $ gryffindor -= 20
                            $ her_mood += 12
    jump end_hg_pf