

# Favour tier 2 - Grope Her

label cc_pf_T2a_groping:
    call nar("not implemented yet")
    jump end_cho_event







### Old Writing ###

label cho_favor_2:
    m "(Right, then I'll just fondle Cho's ass a little.)"
    menu:
        "-Touch her ass-":
            if chof2_first: #have to include new boolean chof2_first=False
                $ chof2_first = False
                g9 "Miss Chang, I'd like to touch your ass."
                call cho_main("My...ass?","smile","suspicious","sad","downR")
                m "Yes. I'd like to touch it."
                call cho_main("I knew you liked my ass.","horny","shocked","base","mid")
                call cho_main("{size=-4}(i knew he couldn't resist for long.){/size}","quiver","shocked","base","R")
                call cho_main("if you want to touch my firm ass, it's going to cost you.","scream","closed","base","mid")
                call cho_main("I'll do it for 40 house points.","open","base","base","R")
                m "That's a lot just to grab a students ass."
                ">Cho twists her petite, muscular body."
                ">You can see the firm lines of her ass under her uniform."
                call cho_main("come on, Professor... isn't it worth it?","smile","base","base","mid")
                m "That is a nice ass..."
                m "But I could get Hermione to do it for..."
                menu:
                    "-25 points-":
                        m "I could get Hermione to do it for only 25 points."
                        call cho_main("25?","scream","wide","angry","mid")
                        call cho_main("25? What cheap slag.","upset","shocked","angry","R")
                        call cho_main("I'll do it for 40.","open","base","angry","mid")
                        m "Alright, 40. But it better be worth it."
                        jump chofbm
                    "-35 points-":
                        m "I could get Hermione to do it for 35 points."
                        call cho_main("{size=-2}35? Really?....{/size}","pout","suspicious","angry","down")
                        call cho_main("{size=+2}If her fat ass is worth 35 then mine must be worth 40.{/size}","open","closed","angry","mid")
                        m "Fine."
                        jump chofbm
                    "-50 points-":
                        m "I could get Hermione to do it for 50 points."
                        call cho_main("50!","open","wide","angry","mid")
                        call cho_main("50! are you serious! No way.","smile","suspicious","angry","down")
                        call cho_main("but, she doesn't even work out...","pout","suspicious","sad","downR")
                        m "I suppose you're ass will do for now, but I'm only paying you 40 house points."
                        call cho_main("my ass will do?!","scream","suspicious","angry","down")
                        call cho_main("i'll show you whose ass is better!","smile","suspicious","angry","down")
                        $ cho_mood +5 #new variable cho_mood
                        jump chofbm
                    "-Nothing-":
                        m "I could get Hermione to do it for absolutely nothing."
                        call cho_main("Nothing?","open","wide","angry","mid")
                        call cho_main("what a little slut.","horny","suspicious","base","downR")
                        call cho_main("you'll still haVE to pay me, of course.","soft","closed","angry","mid")
                        call cho_main("40 house Points.","open","suspicious","angry","down")
                        m "Very Well, Miss Chang."
                        jump chofbm
            else:
                    m "Miss Chang. I'd like to touch your butt again."
                    if cho_whoring  == 1: #new variable cho_whoring
                        call cho_main("well...okay. but it'll cost you 40 house points","open","angry","sad","R")
                        m "Very well. Now come over here, girl."
                        jump chofbm
                    if cho_whoring  == 2:
                        call cho_main("alright, professor.","horny","base","sad","R")
                        call cho_main("40 house points, right?","soft","angry","base","mid")
                        m "Of course, Miss Chang."
                        jump chofbm
                    if cho_whoring  == 3:
                        call cho_main("You do?","horny","base","base","mid")
                        call cho_main("are you going to wank off?","quiver","suspicious","sad","down")
                        menu:
                            "Of course.":
                                m "Of course."
                                call cho_main("i guess I'd better take off my panties.","quiver","suspicious","sad","downR")
                            "No Way.":
                                m "Of course not. What do you take me for, a pervert?"
                                call cho_main("Well...","smile","suspicious","base","R")
                        jump chofbm

label chofbm:
#Cho chibi walks over to Dumbledore's desk and turns around.
    if cho_whoring  == 1:
        if not chof2_first:
            call cho_main("AlrighT...{w=2} you can touch me a little.","horny","base","sad","R")
            ">Cho is standing just inches in front of you, the firm globes of her ass-"
            stop music
            $ renpy.play('sounds/scratch.wav')
            call cho_main("Hey! Hogwarts, like most respectable institutions for magical learning, is located in the UK.","scream","closed","angry","mid")
            call cho_main("Please, stick to the metric system.","upset","closed","angry","mid")
            ">Ah, yes...well..."
            #play music fadein 1.5
        else:
            call cho_main("Alright...","horny","base","sad","R")
            call cho_main("Alright...you can touch me a little.","quiver","base","sad","R")
        ">Cho is standing mere centimeters in front of you, the firm globes of her ass barely visible under her skirt."
        ">Cho's hands remain firmly planted on the edge of your desk."
        ">You feel her quiver as the tips of your fingers touch her warm thighs."
        ">Cho's hands grip the desk firmly as your hands begin to slide up her legs."
        ">You reach her panties, and after feeling the contrast between flesh and soft fabric, you guide your palms over both cheeks."
        ">You give both a series of firm squeezes, appreciating the thick tight muscles underneath."
        call cho_main("prof-Professor...","horny","closed","sad","mid")
        ">You hear Cho stiffle a nervous cry. Her ass squeezes tight under your palms."
        call cho_main("That's enough, right Professor?","pout","base","sad","R")
        menu:
            "\"Yes\"":
                m "Yes. I think that did the trick."
                call cho_main("THank you, Professor.","smile","base","base","R")
                m "40 points to Ravenclaw."
                $ ravenclaw += 40
                jump chof2end
            "\"Absolutely not!\"":
                m "Absolutely not. I'm paying you 40 house points for this, girl."
                call cho_main("But, [cho_genie_name], I-","soft","wide","sad","mid")
                ">You give Cho's ass an aggressive squeeze."
                m "I'll tell you when it's enough."
                call cho_main("Fine.","pout","shocked","angry","R")
                $ cho_mood += 2
                ">Cho's ass feels smooth and warm under your touch. Nevertheless, you begin to savage the poor girls ass."
                call cho_main("Ow.","upset","shocked","angry","mid")
                call cho_main("Ow. ow. That hurts!","open","shocked","angry","mid")
                call cho_main("Professor!","scream","shocked","angry","mid")
                call cho_main("Professor! Professor, please stop.","open","shocked","angry","mid")
                menu:
                    "-Do as she asks-":
                        ">You come to your senses and let the poor girl's ass be."
                        ">Cho quickly pulls her skirt back down, rubbing her tender asscheeks."
                        call cho_main("Thank you, [cho_genie_name].","upset","closed","base","mid")
                        call cho_main("Can I have my house points now?","soft","angry","sad","mid")
                        m "Of course, Miss Chang. You've earned them."
                        m "40 points to Ravenclaw."
                        $ ravenclaw += 40
                        jump chof2end
                    "-Keep going-":
                        ">You ignore the foolish girl's cries and continue to abuse her ass, sliding your hands under her panties."
                        call cho_main("Stop!","scream","wide","angry","mid")
                        ">You grab Cho's ass tightly and squeeze with all your might."
                        ">The star Quidditch player falls forward over your desk."
                        call cho_main("It hurts!","scream","wide","sad","mid")
                        ">You roll your hands over her ass and begin to guide your thumbs to her tight, little, brown hole."
                        ">You can feel her starting to fight, as you squeeze tightly and pull her cheeks apart."
                        call cho_main("Professor Dumbledore!","scream","closed","angry","mid")
                        ">You suddenly release her ass and rain your firm hands across her cheeks."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch
                        call cho_main("...","upset","closed","sad","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch
                        call cho_main("ockk!","upset","suspicious","sad","downR")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch
                        call cho_main("(it hurts so bad!)","smile","wide","sad","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch
                        ">Cho's breathing is heavy and her legs shake under your assault."
                        ">A thick, red outline of your hand is bruising on her buttcheeks."
                        call cho_main("Ack!","scream","wide","sad","mid")
                        call cho_main("Ack!...","horny","wide","angry","mid")
                        call cho_main("Ack!...Professor!","scream","wide","angry","mid")
                        ">Cho finally gains enough control to wriggle free of your grasp, and quickly moves away."
                        #Cho chibi walks to the middle of the room.
                        call cho_main("That's too far!","scream","closed","angry","mid")
                        call cho_main("I never agreed to any of that.","scream","shocked","angry","mid")
                        call cho_main(".......i want 60 points.","scream","closed","angry","mid")
                        menu:
                            "-She earned 60-":
                                m "Very well. That was more than we agreed to. 60 points to Ravenclaw."
                                call cho_main("Thank you, sir.","upset","shocked","base","R")
                                $ cho_mood += 5
                                $ ravenclaw += 60
                                jump chof2end
                            "\"That was a bit much. 80 points\"":
                                m "I think I got a little carried away."
                                call cho_main("...","upset","suspicious","angry","downR")
                                m "80 points to Ravenclaw."
                                call cho_main("Really?","soft","suspicious","angry","down")
                                call cho_main("Well, I suppose it wasn't that bad...","pout","suspicious","sad","downR")
                                $ cho_mood +1
                                $ ravenclaw += 80
                                jump chof2end
                            "\"(How dare she!) 0 points!\"":
                                m "How dare you defy your headmaster, Rumbledwarf!"
                                m "If you don't come back here, you'll get nothing."
                                call cho_main("What!","scream","wide","sad","mid")
                                call cho_main("That's not fair!","scream","wide","angry","mid")
                                m "Well?"
                                call cho_main("Fine!","upset","suspicious","angry","down")
                                $ cho_mood +15
                                #Cho chibi returns to Dumbledore's desk.
                                ">Cho returns to your desk."
                                ">You catch a glimpse of her furious tears as she presents you her tender ass."
                                ">Wasting no time, you quickly tear the poor girls panties down and plant your hands on her firm flesh."
                                call cho_main("...","horny","wide","angry","R")
                                pause
                                ">Pulling her cheeks apart, you begin to rub your thumbs across the tight ring of her virgin asshole."
                                call cho_main("...","horny","suspicious","sad","downR")
                                call cho_main("......","quiver","suspicious","sad","down")
                                ">You can feel Cho's body tensing up."
                                ">You wet a finger with your saliva and begin to prod her asshole."
                                call cho_main(".........","horny","wide","sad","L")
                                m "Just relax."
                                ">Finally, you feel it give and your thick digit begins to slowly slide in."
                                call cho_main("Profes-....","quiver","suspicious","sad","downR")
                                ">Cho fights the urge to cry out. Letting you continue."
                                ">It's clear she wants her points more than anything."
                                m "{size=-2}(Don't you worry girl. You'll get your points.){/size}"
                                ">Once your finger is completely buried you begin to pull it back."
                                ">The muscle clings to your finger as it slides out."
                                call cho_main("...","horny","base","sad","R")
                                ">You can feel Cho tensing up again."
                                ">Your finger slides in and out of her tight asshole."
                                ">Cho falls forward onto the desk. Her breathing is getting faster, more ragged."
                                call cho_main("...","horny","closed","sad","mid")
                                ">Suddenly, you feel her muscular ring pulse, squeezing your finger with unbearable tightness."
                                call cho_main("Professor!","quiver","wide","sad","L")
                                ">Cho cums hard on your finger, before completely collapsing."
                                m "40 points to Ravenclaw."
                                call cho_main("{size=-2}.....yay.{/size}","horny","suspicious","sad","down")
                                $ ravenclaw += 40
                                jump chof2end
    if cho_whoring  == 2:
        call cho_main("...","smile","base","base","mid")
        call cho_main("......","smile","base","base","mid")
        call cho_main("......Aren't you going to touch me?","smile","base","base","mid")
        ">Cho pulls up the bottom of her skirt, revealing her ass, then bends forward over your desk."
        call cho_main("Well?","smile","base","base","mid")
        ">Cho wiggles her ass at you."
        m "By the sands...."
        ">Your hands fly toward Cho's tight cheeks and grip them firmly."
        ">You give both a series of firm squeezes, practically drinking in the feel of the tight muscle underneath."
        cho_sexy "Prof-Professor..."
        ">You hear Cho stiffle a cry. Her ass squeezes tight under your palms."
        call cho_main("That's not enougH, is it, Professor?","smile","base","base","mid")
        menu:
            "No, that's quite enough.":
                m "No, no. That's quite enough. Thank you, Miss Chang."
                call cho_main("....uh. Yes. Thank you, Professor.","smile","base","base","mid")
                m "40 points to Ravenclaw."
                $ ravenclaw += 40
                jump chof2end
            "Not Enough.":
                m "You're right. After all, I'm paying you 40 house points for this, girl."
                call cho_main("Yes, sir. But...","smile","base","base","mid")
                m "But what?"
                ">Cho begins to shake her hips suggestively, and move her ass."
                ">She hooks her thumbs in the waist of her panties and pulls them outward."
                cho_sexy "Well, sir. I suppose for 60 points I could take these ANNOYING panties off."
                call cho_main("And let you feel me, sir...","smile","base","base","mid")
                menu:
                    "60 it is.":
                        m "Well then, 60 it is."
                        $ ravenclaw += 60
                        call cho_main("{size=-4}(Wow, that was easy.){/size}","smile","base","base","mid")
                        call cho_main("{size=-4}(I bet his nasty, old cock is going crazy...){/size}","smile","base","base","mid")
                        ">Cho slowly pushes her panties down past her hips, until they finally fall to her feet."
                        ">She steps out of them and spreads her feet wide before putting her hands on your desk."
                        ">The young Quidditch star arches her back, thrusting her firm ass toward you."
                        m "Very good, Miss Chang."
                        call cho_main("Thank you, sir.","smile","base","base","mid")
                        jump chof2wl2
                    "50 seems more fair.":
                        m "I think 50 points seems more fair. Don't you?"
                        call cho_main("50?","smile","base","base","mid")
                        ">Cho begins to wiggle her panties around her ass seductively."
                        call cho_main("Come on, I think it's worth much more than that...","smile","base","base","mid")
                        menu:
                            "50 points.":
                                m "50 points."
                                call cho_main("Well, okay.","smile","base","base","mid")
                                call cho_main("{size=-4}(60 points was high anyway.){/size}","smile","base","base","mid")
                                $ ravenclaw += 50
                                ">Cho pushes her panties down and puts her hands on your desk."
                                jump chof2wl2
                            "Fine. 55 points.":
                                m "Very well, Miss Chang. I'll give you 55 points."
                                call cho_main("hm. 55 points seems fair.","smile","base","base","mid")
                                $ ravenclaw += 55
                                ">Cho moves her ass seductively, releasing her panties and placing her hands flat on your desk."
                                call cho_main("but, Professor...","smile","base","base","mid")
                                m "Yes?"
                                cho_sexy "I don't think I can reach. Will you help me?"
                                m "Of course, Miss Chang. It's important for the headmaster to take a hands on approach."
                                ">You lean forward and slowly slide Cho's panties down, revealing the girls perfect ass."
                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                jump chof2wl2
                            "No.":
                                ">You give Cho's ass an aggressive squeeze."
                                m "No. I don't think so."
                                call cho_main("What?","smile","base","base","mid")
                                call cho_main("well...i guess I could do it for 50.","smile","base","base","mid")
                                menu:
                                    "Yes.":
                                        m "Very well. 50 house points. You drive a hard bargain, Miss Chong."
                                        call cho_main("MY name Is Chang. And yes, I do.","smile","base","base","mid")
                                        $ ravenclaw += 50
                                        $ cho_mood +1
                                        ">Cho quickly pushes her panties off her hips, letting them fall to the ground before bending over your desk."
                                        jump chof2wl2
                                    "No.":
                                        m "No."
                                        call cho_main("Oh, okay.","smile","base","base","mid")
                                        ">Cho lets her panties snap back into place. Nevertheless, you begin to gently squeeze the girls firm ass."
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("......","smile","base","base","mid")
                                        call cho_main(".........","smile","base","base","mid")
                                        call cho_main("is that enough, sir?","smile","base","base","mid")
                                        menu:
                                            "Yes. That's enough.":
                                                ">You nod."
                                                m "Yes. That was fine, Miss Chang."
                                                ">Cho quickly pulls her skirt back down, smoothing her panties."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                m "40 points to Ravenclaw."
                                                $ ravenclaw += 40
                                                jump chof2end
                                            "Keep going.":
                                                ">You ignore the girl's question and continue to molest her ass, sliding your hands under her panties."
                                                call cho_main("I knew you couldn't resist.","smile","base","base","mid")
                                                ">You grab Cho's bare ass tightly and give it a quick squeeze."
                                                m "40 points to Ravenclaw."
                                                call cho_main("THank you, Professor.","smile","base","base","mid")
                                                $ ravenclaw += 40
                                                jump chof2end

        label chof2wl2:
        ">You stare at Cho's tight, young ass, drinking it in."
        ">It looks like all of her Squidstitching has paid off."
        ">The asian girls ass looks incredible."
        cho_seductive "Well?"
        ">You grab Cho's firm ass in booth hands and squeeze tightly."
        ">Your thick cock strains against your robes."
        menu:
            "-Jerk off-":
                ">You stare at the girl's ass, mezmerized."
                ">You continue to molest her firm ass with one hand, while the other pulls your cock out of your wizard robes."
                call cho_main("what are you doing?","smile","base","base","mid")
                ">You begin to pump your cock, squeezing her ass."
                cho_seductive "A-alright, but I want an extra five... {w=.5} no TEN points."
                menu:
                    "Fine.":
                        ">You give your throbbing cock three quick pumps before nodding."
                        m "Fine. You'll get your points, girl."
                        call cho_main("okay, professor. but you'd better stop before...you know.","smile","base","base","mid")
                        ">Cho shakes her ass from side to side."
                        ">You give it a light smack as it comes back, stroking your cock."
                        cho_sexy_surprise "..."
                        ">Cho bounces her ass up and down a few times. You slap it hard."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("{size=-4}(It hurts...but it also feels good.){/size}","smile","base","base","mid")
                        call cho_main("Professor Dumbl-{nw}","smile","base","base","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("{size=-4}(OH blimey. that's starting to feel really good.){/size}","smile","base","base","mid")
                        ">Every slap brings your cock closer, until you feel a familiar pressure in your magic balls."
                        menu:
                            "-Cum-":
                                ">Finally, it's too much for you, and with one final smack-"
                                $ renpy.play('sounds/slap_02.mp3')
                                show screen white
                                "{size=+4}SLAP!{/size}"
                                #Shake the screen
                                hide screen white
                                ">Finally, it's too much for you, and with one final smack, your cock erupts all over Cho's ass."
                                m "Arg, you fucking slut!"
                                #Genie cums. - I'd need to know which screen to put here
                                cho_wideEyes "What is {size=+2}that?{/size}"
                                cho_wideEyesLookingBack "{size=+4}Are you cumming?{/size}"
                                ">Your cum splatters across the young girl's ass in thick, messy spurts."
                                call cho_main("Oh, my God...","smile","base","base","mid")
                                ">Your wrinkly old balls pull tight and you dump the last of your cum in a fat glob that lands on her asshole."
                                call cho_main("You {size=+2}completely{/size} covered me in your {size=+2}nasty{/size} {size=+3}old{/size} {size=+4}wizard cum!{/size}","smile","base","base","mid")
                                call cho_main("i'm a complete mess, you jerk!","smile","base","base","mid")
                                call cho_main("You owe me an extra 10 points!","smile","base","base","mid")
                                $ cho_mood +=1
                                menu:
                                    "Yes.":
                                        m "Yeah, sure. 10 more points to Ravenclaw."
                                        $ ravenclaw += 10
                                        call cho_main("look at this mess!","smile","base","base","mid")
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("{sIze=-2}...Thank you, sir.{/size}","smile","base","base","mid")
                                        ">Cho quickly pulls her panties up over her cum soaked ass and smoothes her skirt."
                                        call cho_main("this should be okay.","smile","base","base","mid")
                                        jump chof2end
                                    "Too bad.":
                                        m "It's not my fault you made me cum."
                                        call cho_main("!!","smile","base","base","mid")
                                        m "You should be more careful."
                                        call cho_main("you can't be serious!","smile","base","base","mid")
                                        call cho_main("your smelly cum is all oveR my ass! i smell like...liKe...like Hermione!","smile","base","base","mid")
                                        m "Too bad."
                                        call cho_main("you're nothing but a dirty old wizard!","smile","base","base","mid")
                                        ">Cho grabs her panties from the floor and storms off leaving a trail of cum dripping to your door."
                                        $ cho_mood +5
                                        jump chof2end
                            "Better not.":
                                ">You stop at the last moment and put your cock away."
                                ">Your swollen balls throb with pressure."
                                call cho_main("are you okay?","smile","base","base","mid")
                                m "I'm a wizard, girl."
                                jump chof2end
                    "I'll give you 15.":
                        ">You give your throbbing cock a few quick pumps before rubbing the head across her ass cheek."
                        m "I'll give you 15."
                        call cho_main("15?...okay, Professor.","smile","base","base","mid")
                        ">Cho shakes her ass from side to side, lightly dragging her ass across the tip of your cock."
                        ">You give you cock a quick stroke before guiding it back against Cho's ass."
                        cho_sexy_surprise "What are doing back there..."
                        ">Cho bounces her ass up and down a few times. You slap your cock head against it."
                        call cho_main("{size=-4}(Oh my god...i can't believe i'm letting an old man rub his cock on my ass.){/size}","smile","base","base","mid")
                        call cho_main("Professor Dumbledore, make sure you tell me before you-{w=.5}{nw}","smile","base","base","mid")
                        ">You give your cock several good pumps and bring your free hand down across Cho's firm ass."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("Professor Dumbledore, make sure you tell me bEFOre you-CUM!","smile","base","base","mid")
                        call cho_main("(Oh blimey!)","smile","base","base","mid")
                        ">Then you rub your tip across her warm, naked ass flesh, dragging a trail of precum."
                        call cho_main("Professor...","smile","base","base","mid")
                        ">You slap your bulging cock against her ass again and bury the head between her cheeks."
                        ">You pump your cock like a madman, until you feel a familar pressure in your magic balls."
                        menu:
                            "Cum.":
                                ">Finally, it's too much for you, and with one final pump, your cock erupts between Cho's ass cheeks."
                                m "By Grabthar's Hammer!"
                                #Genie cums. - Find chibi
                                cho_wideEyes "Oh my God...What is that?"
                                cho_wideEyesLookingBack "{size=+2}Are you cumming?{/size}"
                                ">Your cum splatters between the young girl's meaty cheeks in thick, messy spurts."
                                call cho_main("Oh, my God...","smile","base","base","mid")
                                ">You pump your cock a few more times and dump the last of your cum in a fat, messy glob right against her asshole."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("my ass feels so gross!","smile","base","base","mid")
                                call cho_main("it's sO sticky. You owe me an extra 10 points!","smile","base","base","mid")
                                menu:
                                    "Why not?":
                                        m "Yeah, sure. 10 more points to Ravenclaw."
                                        $ ravenclaw += 10
                                        call cho_main("look at this mess!","smile","base","base","mid")
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("{sIze=-2}...Thank you, sir.{/size}","smile","base","base","mid")
                                        ">Cho quickly pulls her panties up over her cum soaked ass and smoothes her skirt."
                                        call cho_main("this should be okay.","smile","base","base","mid")
                                        jump chof2end
                                    "Too bad.":
                                        m "It's not my fault your ass made me cum."
                                        call cho_main("!!!","smile","base","base","mid")
                                        m "You should be more careful."
                                        call cho_main("you can't be serious!","smile","base","base","mid")
                                        call cho_main("your smelly cum is all iN my ass! i smell like...liKe...like Hermione!","smile","base","base","mid")
                                        m "Too bad."
                                        call cho_main("you're nothing but a dirty old wizard!","smile","base","base","mid")
                                        ">Cho grabs her panties from the floor and storms off leaving a trail of cum dripping to your door."
                                        $ cho_mood +5
                                        jump chof2end
                            "Warn Her.":
                                m "I'm almost there!"
                                call cho_main("Really?","smile","base","base","mid")
                                ">Suddenly, you feel Cho push back against you."
                                ">Your cock is wrapped tightly within her warm, muscular ass cheecks."
                                cho_sexy "Cum, Professor!"
                                ">Cho's ass rubs up and down, her ass tightly gripping your cock."
                                ">Finally, it's too much for you and with a grunt you bury your cock between her cheeks and cum violently."
                                m "Support Aka-{nw}"
                                cho_sexy "Shut up and cum, you dirty old man!"
                                m "Support Aka-gaaahhhh! You whore!"
                                #Genie cums. - find chibi
                                ">Spurt after nasty spurt of your cum shoots between the young girls ass, bubbling out over the top of her cheeks."
                                call cho_main("my ass feels so dirty!","smile","base","base","mid")
                                ">Completely spent, your fall back in your chair."
                                m "Well done girl."
                                call cho_main("thank you professor.","smile","base","base","mid")
                                ">Cho slips her panties back on, pulling them up over her cum filled crack."
                                ">Then she lightly pats her sticky ass."
                                call cho_main("Can't make a mess in the Hall, can I?","smile","base","base","mid")
                                jump chof2end
    if cho_whoring  ==3:
        ">Cho pulls up the bottom of her skirt, revealing her bare ass, then bends forward over your desk."
        call cho_main("Well?","smile","base","base","mid")
        ">Cho wiggles her naked ass at you."
        m "By the sands....you naughty girl."
        ">Your hands fly toward Cho's firm flesh and you grip her bare cheeks firmly."
        ">You give both a series of firm squeezes, practically drinking in the feel of the tight muscle underneath."
        cho_sexy "Dumbledore..."
        ">You hear Cho attempt to stiffle a moan. Her muscualar ass squeezes tight."
        call cho_main("You a want little more, don't you sir?","smile","base","base","mid")
        call cho_main("You...{w=1.5} you want to cum, don't you?","smile","base","base","mid")
        menu:
            "No, I want to preserve my essence.":
                m "No, Miss Chang. I'm on to you, you succubus!"
                call cho_main("....uh. What?","smile","base","base","mid")
                m "40 points to Ravenclaw."
                $ ravenclaw += 40
                call cho_main("....thank you?","smile","base","base","mid")
                jump chof2end
            "Of course!":
                m "{size=-4}(I understand. You nasty little girl.){/size}"
                m "You'd better earn these 40 points girl."
                call cho_main("Yes, sir. But...","smile","base","base","mid")
                m "But what?"
                ">Cho begins to shake her hips suggestively, and move her ass."
                ">Every so often you get a glimpse of her cute, little asshole."
                ">Cho leans forward, pulling her ass cheeks apart."
                call cho_main("Well, sir. i suppose for just 65 points I could","smile","base","base","mid")
                cho_sexy "Well, sir. I suppose for just 65 points I could put your big, strong cock between these."
                cho_sexy "And rub you up and down until you cum."
                menu: #[No.]
                    "65 it is.":
                        m "Well then, 65 it is."
                        call cho_main("{size=-4}(wow, that was easy.){/size}","smile","base","base","mid")
                        call cho_main("{size=-4}(I bet his nasty, old wizard balls are completely full of cum.){/size}","smile","base","base","mid")
                        ">Cho arches her back, thusting her firm ass toward you."
                        ">Then the young Quidditch star slowly backs into your cock, before wrapping her ass tightly around you."
                        m "Very good, Miss Chang."
                        call cho_main("Thank you, sir.","smile","base","base","mid")
                        jump chof2hd
                    "55 feels more right.":
                        m "I think 55 points is much more appropriate. Don't you?"
                        call cho_main("55?","smile","base","base","mid")
                        ">Cho begins to bounce and jiggle her ass seductively."
                        call cho_main("Come on, I think it's worth much more than that...","smile","base","base","mid")
                        cho_seductively "{size=-4}To cum...{/size}"
                        cho_seductively "{size=-2}To cum right...{/size}"
                        cho_seductively "{size=-1}To cum right{/size}...{w} here."
                        menu:
                            "55 points.":
                                m "55 points."
                                call cho_main("Well, okay.","smile","base","base","mid")
                                call cho_main("{size=-4}(60 points was high anyway.){/size}","smile","base","base","mid")
                                ">Cho pushes her ass back against you."
                                jump chof2hd
                            "Fine. 60 points.":
                                m "Very well, Miss Chang. I'll give you 60 points."
                                call cho_main("hm. 60 points isn't too bad.","smile","base","base","mid")
                                ">Cho moves her ass seductively, pulling her cheeks open wide before settling back against your cock."
                                call cho_main("Professor Dumbledore...","smile","base","base","mid")
                                m "Yes?"
                                call cho_main("your cock feels so...","smile","base","base","mid")
                                cho_sexy "So thick."
                                ">You lean forward and slowly slide your cock up and down Cho's valley."
                                call cho_main("Mmm. Thank you, sir.","smile","base","base","mid")
                                jump chof2hd
                    "No.":
                        ">You slap your stone hard cock against Cho's ass aggressively."
                        m "No. I don't think so."
                        call cho_main("What?","smile","base","base","mid")
                        call cho_main("well...i guess I could do it for 50.","smile","base","base","mid")
                        menu:
                            "Yes":
                                m "Very well. 50 house points. You drive a hard bargin, Miss Chong."
                                call cho_main("MY name Is Chang. And yes, I do.","smile","base","base","mid")
                                $ ravenclaw += 50
                                $ cho_mood +1
                                ">Cho quickly pushes her ass against you."
                                jump chof2hd
                            "No.":
                                m "No."
                                call cho_main("Oh, okay.","smile","base","base","mid")
                                ">Cho releases her cheeks, letting her ass clap together."
                                ">She bends over your desk and you begin to gently squeeze the girls firm, naked ass."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("......","smile","base","base","mid")
                                call cho_main(".........","smile","base","base","mid")
                                call cho_main("is that enough, sir?","smile","base","base","mid")
                                menu:
                                    "Yes. That's enough.":
                                        ">You nod."
                                        m "Yes. That was fine, Miss Chang."
                                        ">Cho quickly pulls her skirt back down, smoothing the fabric over her ass."
                                        call cho_main("Thank you, sir.","smile","base","base","mid")
                                        m "40 points to Ravenclaw."
                                        $ ravenclaw += 40
                                        jump chof2end
                                    "Keep going.":
                                        ">You ignore the girl's question and continue to molest her ass, sliding your hands deep between her ass cheeks."
                                        call cho_main("I knew you couldn't resist.","smile","base","base","mid")
                                        ">You lean forward and give Cho's ass a quick bite before leaning back."
                                        m "40 points to Ravenclaw."
                                        call cho_main("Thank you, Professor.","smile","base","base","mid")
                                        $ ravenclaw += 40
                                        jump chof2end

        label chof2hd:
        ">You can feel Cho's warmth spreading out over your body from her ass."
        ">You give her firm cheeks a quick slap."
        $ renpy.play('sounds/slap_02.mp3')
        show screen white
        "{size=+4}SLAP!{/size}"
        #Shake the screen
        hide screen white
        cho_seductive "Professor!"
        ">You grab Cho's firm ass in booth hands and squeeze it tightly around your cock."
        ">Your thick cock strains and throbs."
        call cho_main("let me do all the work.","smile","base","base","mid")
        menu:
            "Fuck her ass cheeks.":
                ">You stare at the girl's ass, mezmerized."
                ">Finally, you stand up and push Cho down over your desk."
                call cho_main("sir, what are you doing?","smile","base","base","mid")
                ">You squeeze her cheeks tight and begin to pump your cock through the tunnel."
                cho_seductive "A-alright, you can do that, but I want an extra five points."
                menu: #[I'll give you 15] [No more points]
                    "Fine.":
                        ">You give the girl's ass several quick pumps before answering."
                        m "Very well, girl."
                        call cho_main("okay, Professor, but...but warn me before you cum.","smile","base","base","mid")
                        ">Cho shakes her ass from side to side, causing your slimy cock to pop free."
                        ">You give Cho's ass a light smack, squeezing your cock with her cheeks."
                        cho_sexySurprise "..."
                        ">You thrust forward enjoying the sensation on your head, then slap Cho hard."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("{size=+4}(Oh my god!){/size}","smile","base","base","mid")
                        ">You feel Cho's thighs tighten with her ass."
                        call cho_main("{size=+4}(why does it feel so good?){/size}","smile","base","base","mid")
                        cho_sexy "{size=+4}(My pussy is tingling with every thrust of his nasty, old cock...){/size}"
                        call cho_main("Professor Dumbl-{w=.5}{nw}","smile","base","base","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        call cho_main("{sizE=+4}(oh! Oh, blimey!){/size}","smile","base","base","mid")
                        ">You feel Cho shifting her weight, and then notice her hand squeezed tight between her legs."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        m "You're enjoying this aren't you?"
                        call cho_main("no! no, I'm not!","smile","base","base","mid")
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        m "Liar!"
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white
                        ">Suddenly, you feel Cho's body start to convulse and her legs begin to shake uncontrollably."
                        call cho_main("proF {w}prof-PRofessor! I'm.{w=.75}{nw}","smile","base","base","mid")
                        call cho_main("PRofeSsor! I'm-I'm.{w=.75}{nw}","smile","base","base","mid")
                        call cho_main("I'm{W=.5}-I'm CUMMING!","smile","base","base","mid")
                        ">Cho's orgasm pushes you over the edge and you feel a familar twitch your wizard balls."
                        menu:
                            "Cum on her cheeks.":
                                "Finally, it's too much for you, and with one final thrust, your cock erupts all over Cho's ass."
                                m "Take it, you whore!"
                                #Genie cums.
                                cho_stupid"..."
                                cho_stupid"......"
                                "Your cum splatters between the young girl's ass cheeks in thick, messy spurts."
                                cho_stupid"........."
                                "Your wrinkly old balls pull tight and you dump the last of your cum in a fat glob that lands on her asshole."
                                m "(Points) to Ravenclaw."
                                cho_stupid"........yessh."
                            "Cum in her ass.":
                                ">As you thrust forward you feel your head rub against the girls tight ring."
                                ">At the very brink you pull her cheeks open and press your cockhead against the tight entrance."
                                cho_stupid "...ahhh"
                                ">You push forward, fighting against the muscles."
                                cho_stupid "...ahhh....Ohhhh"
                                ">Finally, the ring gives way and your cock *pops* into her ass."
                                cho_stupid "...ahhh....ohhhh...Oomph!"
                                ">The pressure is too much and your cock explodes, dumping your cum safely in Cho's asshole."
                                #Genie cums - find sprite
                                m "Arg! You fucking cum dumpster!"
                                ">Load after load pumps into the girls tight, little hole until you feel her stomach bloat under you."
                                cho_stupid "Gack!"
                                cho_stupid "ooomph!"
                                $ renpy.play('sounds/pop02.mp3')
                                "Your cock pops out of the poor girls ass and you fall back in your chair, exhausted."
                                show screen blktone
                                #Cho chibi is standing in the middle of the room.
                                call cho_main("i don't feel So good...what happened?","smile","base","base","mid")
                                menu:
                                    "I filled your ass with cum.":
                                        m "You came so hard you passed out and I filled your ass with cum."
                                        cho _Shocked "..."
                                        cho _Shocked "......"
                                        cho _Shocked "........."
                                        cho_mouthfull "...."
                                        $ renpy.play('sounds/burp.mp3')
                                        call cho_main("i need to go!","smile","base","base","mid")
                                        jump chof2end
                                    "I don't know. That was weird.":
                                        m "I don't know. That was weird."
                                        m "But you got your points."
                                        call cho_main("THank you, Prof...","smile","base","base","mid")
                                        cho_mouthfull "Prof-"
                                        $ renpy.play('sounds/burp.mp3')
                                        call cho_main("i think i need To go seE moaning Myrtel!","smile","base","base","mid")
                                        $ renpy.play('sounds/run.mp3')
                                        jump chof2end
            "Let her.":
                m "As you wish, Miss Chang."
                ">You sit back in your chair and let Cho settle down against your lap."
                call cho_main("does this feel good?","smile","base","base","mid")
                ">Cho slowly drags her ass up and down over your cock."
                m "Fantastic, girl."
                ">Cho squeezes her ass around your dripping cock."
                ">The athletic, young Quidditch star arches her back and bounces her ass up a down, teasing the tip of your cock."
                m "You tease!"
                ">You suddenly bring your palm down across her meaty cheek."
                $ renpy.play('sounds/slap_02.mp3')
                show screen white
                "{size=+4}SLAP!{/size}"
                #Shake the screen
                hide screen white
                cho_sexySurprise "Professor!"
                ">Cho bounces her ass up and down a few more times, before  settling down on your lap."
                call cho_main("{size=-4}(Oh my god...i can't believe i'm rubbing my ass over an old wizard's cock.){/size}","smile","base","base","mid")
                call cho_main("{size=-4}(My ass is so slimy...the smell is so thick...){/size}","smile","base","base","mid")
                call cho_main("Professor Dumbledore, m-make sure you tell me before you-","smile","base","base","mid")
                ">You can already feel the beginning of your orgasm."
                ">You give the girls tight ass several slaps..."
                call slap_her

                call cho_main("Professor Dumbledore, make sure you tell me before you-{w=.75}{nw}","smile","base","base","mid")
                call slap_her

                call cho_main("Professor Dumbledore, make sure you tell me bEFOre you-CUM!","smile","base","base","mid")
                call cho_main("{size=+4}(Oh blimey!){/size}","smile","base","base","mid")
                ">Cho slides back against your lap and begins to grind against you as you pump your cock between her cheeks."
                cho_arounsed "Professor..."
                ">You can see the top of your cock popping in and out of her ass cleavage, leaving a puddle of slime in the valley."
                ">After several more pumps you feel a familar pressure building..."
                menu:
                    "Cum.":
                        ">Finally, it's too much for you, and with one final thrust, your cock erupts between Cho's ass cheeks."
                        m "Cor' blimey, you bloody wanker!"
                        #Genie cums. - find chibi
                        cho_wideEyes "Oh my God...What is that?"
                        cho_wideEyesLookingBack "{size=+2}Are you cumming?{/size}"
                        ">Your cum splatters between the young girl's meaty cheeks in thick, messy spurts."
                        call cho_main("Oh, my God...","smile","base","base","mid")
                        ">You pump your cock a few more times and dump the last of your cum at the top of her ass."
                        call cho_main("...","smile","base","base","mid")
                        call cho_main("my ass feels so gross!","smile","base","base","mid")
                        call cho_main("it's so sticky.","smile","base","base","mid")
                        cho_sexy "It's so sticky. You owe me an extra 10 points!"
                        menu:
                            "Yes.":
                                m "Yeah, sure. 10 more points to Ravenclaw."
                                $ ravenclaw += 10
                                call cho_main("look at this mess!","smile","base","base","mid")
                                call cho_main("I'll never get this cleaned up...","smile","base","base","mid")
                                call cho_main("{sIze=-2}...Thank you, sir.{/size}","smile","base","base","mid")
                                ">Cho stands up. Cum dripping down her firm ass, running in long, slimy rivulets down her thighs."
                                call cho_main("{size=-4}(He came so much...){/size}","smile","base","base","mid")
                                cho_happy "{size=-4}(I bet Hermione never makes him cum like this.){/size}"
                                ">Cho pulls her skirt back over her sticky ass and smoothes the fabric. Dark stains appear as the cum soaks through."
                                call cho_main("this should be okay.","smile","base","base","mid")
                                m "Yes, of course. Though, just to be safe you'd better try to avoid the prefects..."
                                jump chof2end
                            "Too bad.":
                                m "You're the one who made me cum."
                                call cho_main("!!!","smile","base","base","mid")
                                m "You should be more careful."
                                call cho_main("you can't be serious!","smile","base","base","mid")
                                call cho_main("your smelly cum is all over my arse! i smell like...liKe...like Hermione!","smile","base","base","mid")
                                m "Too bad."
                                call cho_main("you're nothing but a dirty old wizard!","smile","base","base","mid")
                                "Cho pulls her skirt down and storms off, leaving a trail of cum dripping to your door."
                                $ cho_mood +5
                                jump chof2end
                    "Warn Her.":
                        m "I'm going to cum!"
                        call cho_main("Really?","smile","base","base","mid")
                        ">Suddenly, you feel Cho move forward, and her hands quickly pull your cock down between her thighs before pushing back against you."
                        ">Your cock is wrapped tightly within her warm, muscular thighs, pressed tightly against her virgin pussy."
                        ">Cho rocks her hips back and forth, thrusting you through her slippery thighs."
                        cho_sexy "Cum, Professor!"
                        ">You can feel the heat and juice dripping from Cho's pussy, clinging to your cock."
                        ">Finally, it's too much for you and with a grunt you grab the girl's hips and cum violently."
                        m "Arg, you whor-{w=.75}{nw}"
                        cho_sexy "Shut up and cum, you nasty, old wizard!"
                        m "Arg, you whor-errrrrr!"
                        #Genie cums. - find chibi
                        ">Spurt after nasty spurt of your cum shoots between the young girls thight thighs, drenching your desk."
                        cho_sexy "So much cum!"
                        ">Completely spent, your fall back in your chair."
                        m "Good job Ms Chang."
                        call cho_main("thank you professor.","smile","base","base","mid")
                        ">Cho carefully straightens her skirt."
                        ">Then she leans back over your desk and runs her finger through your warm, dripping cum."
                        call cho_main("i think you made a bit of a mess...","smile","base","base","mid")
                        ">Then, bringing the slimy mess to her soft lips she sucks her finger clean."
                        call cho_main("Oops...","smile","base","base","mid")
                        jump chof2end

    label chof2end:
    #cho walking out
    call play_sound("door")
    hide screen cho_chang
    with d3
    jump day_main_menu
