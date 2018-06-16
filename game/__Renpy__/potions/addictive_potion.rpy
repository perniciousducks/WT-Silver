

### CUM ADDICTION ###

label potion_scene_3_1_1: #cum addiction - work in progress, has some scenes adjusted for it
    m "[hermione_name], today I have a very special potion that I would like you to drink."
    call her_main("What does this one do?","normal","frown") from _call_her_main_6047
    m "As always, it's going to be a surprise."
    call her_main("You're not going to try to transform me into a cat again are you [genie_name]?","normal","frown") from _call_her_main_6048
    call her_main("","normal","frown") from _call_her_main_6049
    m "Of course not, now would you kindly drink the potion?"
    call her_main("...","annoyed","angryL") from _call_her_main_6050
    call her_chibi("drink_potion","mid","base") from _call_her_chibi_179
    
    call nar(">Hermione cautiously starts drinking the potion.") from _call_nar_603
    call her_main("","cum","worriedCl") from _call_her_main_6051
    pause .5
    call her_chibi("stand","mid","base") from _call_her_chibi_180
    
    call her_main("This isn't a potion! This is just a bottle full of your cum!","scream","angryCl") from _call_her_main_6052
    call her_main("Ughhh and it's cold as well.","disgust","narrow") from _call_her_main_6053
    m "So it just tastes like cum to you?"
    call her_main("Of course it does, what else would it taste like?","angry","angry") from _call_her_main_6054
    call nar(">Hermione starts unconsciously licking her lips.") from _call_nar_604
    call her_main("At least warn me next time you make me drink your cum, [genie_name].","open","worriedL") from _call_her_main_6055
    m "What do you mean next time?"
    call her_main("Well, you're such a pervert you'll probably try and do this again. At least warn me so it's not such a shock.","annoyed","annoyed") from _call_her_main_6056
    m "Ok, [hermione_name], I'll make sure to warn you next time."
    call her_main("Is that all then, [genie_name]?","annoyed","angryL") from _call_her_main_6057
    m "Yes [hermione_name], 20 points to Gryffindor."
    call her_main("Thank you, [genie_name].","open","suspicious") from _call_her_main_6058
    call nar(">Hermione leaves the room with the remaining potion firmly in her grasp.") from _call_nar_605  
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with d3
    
    call her_walk("mid","leave",2) from _call_her_walk_122
    
    $ addicted = True
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_3_1_2: #Scene where Hermione comes back addicted to your cum (replace sucking noises with actual text)
    call play_sound("door") from _call_play_sound_202 #Sound of a door opening.
    call her_chibi("stand","mid","base") from _call_her_chibi_181
    pause.5
    
    show screen bld1
    call nar(">Hermione quickly enters your office.") from _call_nar_606
    call her_main("What the hell did you do to me?","scream","worriedCl") from _call_her_main_6059
    m "Whatever are you talking about, [hermione_name]?"
    call her_main("Ughh, it doesn't matter, just let me suck it.","annoyed","worriedL") from _call_her_main_6060
    m "Why on earth would you want to do that? You're a top student, that doesn't sound appropriate."
    call her_main("You know exactly what you did to me. Now let me suck your filthy old cock.","angry","angry") from _call_her_main_6061
    
    menu:
        "-Let her suck your dick-":
            m "Well if you insist, [hermione_name]."
        "-Make her beg-":
            m "I don't think that you deserve to after calling it filthy and old."
            m "Perhaps if you asked nicely..."
            call her_main("Fine. Please let me suck your dick [genie_name].","upset","wink") from _call_her_main_6062
            m "Hmmm, I don't think that was sincere enough."
            call her_main("Please [genie_name], let me suck your big, thick dick. Pretty please.","angry","worriedCl",emote="05") from _call_her_main_6063
            m "Much better."
         
    call blkfade from _call_blkfade_194 
    pause 1
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_left
    show screen g_c_u
    
    call her_chibi("hide") from _call_her_chibi_182
    hide screen blktone
    hide screen bld1
    call hide_blkfade from _call_hide_blkfade_141
    call ctc from _call_ctc_339
    
    $ hermione_main_zorder = 8
    
    show screen bld1
    call nar(">As soon as you remove your cock from your robe Hermione is on top of you.") from _call_nar_607
    call her_main("","disgust","glance") from _call_her_main_6064
    $ g_c_u_pic = "hand_ani"
    with d3      
    her "Do you have any idea how hard it was sitting through classes today?"
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3      
    her "*Slurp!* *Slurp!* *Slurp!*"    ###start sucking etc....
    call her_main("","annoyed","angryL") from _call_her_main_6065
    $ g_c_u_pic = "hand_ani"
    with d3   
    her "Being this aroused."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Slurp!* *Gobble!* *Slurp!*"
    call her_main("","grin","baseL") from _call_her_main_6066
    $ g_c_u_pic = "hand_ani"
    with d3   
    her "With no way to relieve myself."
    her "I tried everything."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Gobble!* *Slurp!* *Slurp!*"
    call her_main("","smile","glance") from _call_her_main_6067
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "I even masturbated in the girls bathroom."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Gobble!!* *Gltch!!* *Gobble!!!*"
    call her_main("","annoyed","annoyed") from _call_her_main_6068
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "But nothing worked."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Slurp!* *Gulp!* *Slurp!*"
    call her_main("","base","ahegao_raised") from _call_her_main_6069
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "All I could think about was the taste of your filthy cum."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Slurp!* *Gulp!* *Gulp!*"
    m "My my, someone is becoming quite the slut wouldn't you say [hermione_name]"
    her "*Slurp!* *Gulp!* *Slurp!*"
    call her_main("","open_tongue","glance") from _call_her_main_6070
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "You know why this is happening to me."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3  
    her "*Slurp!* *Slurp!* *Gulp!*"
    call her_main("","smile","glance") from _call_her_main_6071
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "Whatever was in that delicious potion you made me drink this morning."
    hide screen hermione_main
    m "Delicious? I thought you said it was just a bottle full of my cum?"
    m "Are you sure that you're just not a little slut who's become addicted to her Headmaster's semen?"
    call her_main("I'm sure. There was something else in there.","angry","wink") from _call_her_main_6072
    hide screen hermione_main
    m "Whatever you say [hermione_name]. Now if you want your reward you better get back to work."
    call her_main("","base","suspicious") from _call_her_main_6073
    $ g_c_u_pic = "hand_ani"
    with d3 
    her "..."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3   
    her "*Slurp!* *Slurp!* *Gulp!*"
    call nar(">She is incredibly enthusiastic. You can feel your load building.") from _call_nar_608
    
    menu:
        "-Cum down her throat-":
            m "Here it comes, slut!"
            call nar(">Hermione quickly swallows the majority of your shaft. You can feel the tip of your head pressed against the entrance to her throat.") from _call_nar_609
            m "You'll have to do better than that if you want your reward [hermione_name]."
            call nar(">You place your hands on the back of her head pull her head into you.") from _call_nar_610
            call her_main("{size=+7}!!!{/size}","scream","worriedCl") from _call_her_main_6074
            hide screen hermione_main
            call nar(">The sensation of entering her throat sends you over the edge.") from _call_nar_611
            m "Better start swallowing slut!"
            call nar(">You start pumping your thick load directly into her stomach.") from _call_nar_612
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            call nar(">Hermione's eyes widen and tears form as she senses your semen enter her.") from _call_nar_613
            call her_main("hhaanooo hhhheerrr","scream","wide") from _call_her_main_6075
            hide screen hermione_main
            call nar(">Her hands shoot down into her pants as she starts violently orgasming.","start") from _call_nar_614
            call nar(">The sight of her pleasuring herself as you use her throat only prolongs your orgasm.","end") from _call_nar_615
            m "You dirty little girl. Getting off from your headmaster sticking his cock down your throat."
            m "I bet your loving this, being used as a nothing more than a toy."
            call nar(">She says nothing but quickens the pace of her masturbation.","start") from _call_nar_616
            call nar(">You finally pull out of keen mouth with a satisfactory pop.","end") from _call_nar_617
            call her_main("It won't stop!","shock","worriedCl") from _call_her_main_6076
            hide screen hermione_main
            m "What won't?"
            call her_main("I-I can't stop cumming [genie_name]...","angry","base") from _call_her_main_6077
            hide screen hermione_main
            call nar(">The stimulation proves too much and she passes out.") from _call_nar_618
            
        "-Cum in her mouth-":
            m "This is it, girl! Get ready!"
            call nar(">Hermione starts swirling her tongue and focusing on the tip of your shaft.") from _call_nar_619
            g4 "That's done it slut! Start swallowing!"
            call nar(">You explode into her mouth.") from _call_nar_620
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            call her_main("mmmmmmm... *gulp* *gulp*","full_cum","dead") from _call_her_main_6078
            hide screen hermione_main
            call nar(">Hermiones eyes go blank as she starts swallowing down your load.") from _call_nar_621
            m "That's it, swallow it down like a good girl. You earned your prize."
            call her_main("*gulp* *gulp* *gulp* *gulp*","cum","worriedCl") from _call_her_main_6079
            hide screen hermione_main
            call nar(">As she swallows you notice her legs start to convulse as she starts to orgasm.") from _call_nar_622
            call her_main("*gulp* *gulp* *gulp* ","full_cum","dead") from _call_her_main_6080
            hide screen hermione_main
            call nar(">You finally remove your shaft from her hungry mouth.") from _call_nar_623
            m "Very good girl. Almost entirely clean... except for a bit of cum on the tip."
            m "I can't dirty my robes now can I? Better wipe this off."
            call nar(">You wipe yourself clean on the tip of her nose.") from _call_nar_624
            call her_main("...","cum","worriedCl") from _call_her_main_6081
            hide screen hermione_main
            m "There, much better."
            call nar(">Her legs have not stopped quivering since you first came.") from _call_nar_625
            m "Well aren't you going to say anything [hermione_name]?"
            call her_main("Thank you maste-","silly","dead") from _call_her_main_6082
            hide screen hermione_main
            call nar(">She collapses into a heap on the ground with her legs still shaking.") from _call_nar_626
            
        "-Cum on her face-":
            m "Get ready, girl! here it comes!"
            call nar(">Hermione increases her efforts and starts focusing on the head of your penis.") from _call_nar_627
            m "Not so quick [hermione_name]."
            $ g_c_u_pic = "hand_ani"
            with d3 
            call nar(">You quickly pull your penis out from her mouth.") from _call_nar_628
            call her_main("What are you doing [genie_name]?","shock","wide") from _call_her_main_6083
            hide screen hermione_main
            m "Giving you your well earned reward."
            $ g_c_u_pic = "cum_on_face_ani"
            with d3 
            $ uni_sperm = True
            call nar(">You start pumping your cock quickly and explode all over the young witch's face") from _call_nar_629
            m "Take it you filthy cum slut!"
            call her_main("{size=+5}!!!{/size}","soft","ahegao") from _call_her_main_6084
            hide screen hermione_main
            call nar(">Hermione immediately starts masturbating shamelessly in front of you.") from _call_nar_630
            call her_main("{size=+5}I'm cumming{/size}","angry","base") from _call_her_main_6085
            hide screen hermione_main
            m "What was that [hermione_name]?"
            call her_main("I-I'm cumming","scream","wide") from _call_her_main_6086
            hide screen hermione_main
            m "Just from a facial? What sort of cumslut have you become Miss Granger?"
            m "What would your parents think? Looking at you covered in some old mans cum."
            call her_main("No. Please stop, I'll-","angry","worriedCl",emote="05") from _call_her_main_6087
            hide screen hermione_main
            m "They'd be ashamed at what you've become. A whore who gets off from being used as a toy."
            call her_main("I-I'm cumming again [genie_name]. It won't stop...","scream","worriedCl") from _call_her_main_6088
            hide screen hermione_main
            call nar(">Hermione's voice trails off as she pass out from the over stimulation.") from _call_nar_631
            
        "-Cum on the floor-":
            m "I'm cumming, whore!"
            call her_main("mmmmmmmm...","open_wide_tongue","base") from _call_her_main_6089
            hide screen hermione_main
            call nar(">She goes to bury her face into her crouch but you put your palm on her forehead and push her away.") from _call_nar_632
            $ g_c_u_pic = "hand_ani"
            with d3 
            call her_main("[genie_name], what are you doing?","angry","wide") from _call_her_main_6090
            hide screen hermione_main
            m "giving you your reward!"
            call nar(">After a few quick pumps you point your dick at the floor and explode.") from _call_nar_633
            call her_main("PROFESSOR! Why would you waste that?","angry","down_raised") from _call_her_main_6091
            hide screen hermione_main
            m "It's not wasted [hermione_name], your reward is right there waiting for you."
            call her_main("I'm not going to eat that. The floor in here is disgusting.","angry","base") from _call_her_main_6092
            hide screen hermione_main
            m "Well you can always wait until tomorrow morning then."
            call her_main("TOMORROW MORNING!? I can't wait that long! Can't you just cum again?","angry","wide") from _call_her_main_6093
            hide screen hermione_main
            m "No [hermione_name], I'm a tired old man and it's time for me to go to sleep."
            m "You can either eat off the floor or you can come back tomorrow."
            call her_main("...Fine.","upset","closed") from _call_her_main_6094
            hide screen hermione_main
            call nar(">She begrudgingly starts scooping your cum off the floor with her fingers.") from _call_nar_634
            
            menu:
                "-Watch her-":
                    call her_main("","full_cum","dead") from _call_her_main_6095
                    call nar(">She scoops up as much as she can into her palm and quickly moves it to her mouth.","start") from _call_nar_635
                "-Make her lick it up-":
                    m "Not with your fingers [hermione_name]."
                    call her_main("What do you mean not with my fingers? How else am I supposed to eat it?","angry","base") from _call_her_main_6096
                    hide screen hermione_main
                    m "You have a perfectly good tongue, I suggest that you put it to use."
                    call her_main("You expect me to LICK your old cum off the floor?","angry","down_raised") from _call_her_main_6097
                    hide screen hermione_main
                    m "I do. Unless of course you would prefer to go back to your room hungry and unsatisfied."
                    call her_main("...","angry","base") from _call_her_main_6098
                    hide screen hermione_main
                    call nar(">She bends over with her head to the floor.") from _call_nar_636
                    $ aftersperm = True
                    call her_main("(This is so degrading...)","open_wide_tongue","angry") from _call_her_main_6099
                    hide screen hermione_main
                    call nar(">She puts her tongue out licks your cum.","start") from _call_nar_637
                    
            call nar(">The effect is instantaneous.","end") from _call_nar_638
            $ aftersperm = True
            call her_main("I-I'm cumming...","cum","worriedCl") from _call_her_main_6100 #small text
            hide screen hermione_main
            m "What was that?"
            call her_main("I'm cumming!","silly","dead") from _call_her_main_6101
            hide screen hermione_main
            call nar(">Hermione's hand shoots under her skirt as she starts violently orgasming.") from _call_nar_639
            call her_main("What's wrong with me [genie_name]?","silly","ahegao") from _call_her_main_6102
            hide screen hermione_main
            m "A lot of things [hermione_name], considering you just ate my cum off the ground."
            call her_main("I can't stop cumming...","shock","baseL",cheeks="blush",tears="soft") from _call_her_main_6103
            hide screen hermione_main
            call nar(">Hermione loses conciousness.") from _call_nar_640
            
    hide screen bld1
    hide screen hermione_main
    call nar(">Hermione is in an unconscious heap on the floor.") from _call_nar_641
    
    menu:
        "-Carry her back to her room as is-":   
            call nar(">You pick her limp body up and carry her to her room.","start") from _call_nar_642
            call nar(">As you enter the dormitory you hear her talk in her sleep.","end") from _call_nar_643
            call her_main("Of course I swallow... just form a line...","open","worriedCl") from _call_her_main_6104
            hide screen hermione_main
            call nar(">You place her carefully back into her bed.") from _call_nar_644
            m "Sleep tight, slut."
        "-Clean her up and take her back to her room-":   
            $ uni_sperm = False
            call nar(">You pick her limp body up and carry her to her room.","start") from _call_nar_645
            call nar(">As you enter the dormitory you hear her mumble in her sleep.","end") from _call_nar_646
            call her_main("You want a kiss [genie_name]? Of course I don't mind...","open","closed") from _call_her_main_6105
            hide screen hermione_main
            call nar(">You place her carefully back into her bed.") from _call_nar_647
            m "Sleep tight, Hermione."
            
    call blkfade from _call_blkfade_195
    pause.5
    
    hide screen hermione_main
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_left
    hide screen desk
    show screen genie
    hide screen blktone
    $ addicted = False
    $ uni_sperm = False
    $ aftersperm = False
    call hide_blkfade from _call_hide_blkfade_142
    
    $ hermione_main_zorder = 5
    $ hermione_sleeping = True

    jump night_main_menu
    
    label potion_scene_7: #hyper sensitivity potion
    m "I'd like you to drink a potion today."
    her "Alright then."
    m "Just like that? No putting up a fight or demanding to know what it is?"
    her "Would you tell me what it is?"
    m "No, probably not."
    her "Then why ask?"
    m "Fair enough, here it is."
    menu:
        "-Drop it on her chest-":
            jump potion_scene_7_1
        "-Hand it to her-":
            jump potion_scene_7_2
        "-Drop it on her skirt-":
            jump potion_scene_7_3

            
            
### HYPER SENITIVITY POTION ###
            
label potion_scene_3_2_1: #Hyper sensitive breasts
    call nar(">You fumble with the potion, spilling it over Hermione's front, soaking her shirt through.") from _call_nar_648
    her "Professor! What were you thinking?"
    call nar(">You place the still half full bottle back on your desk in front of you.") from _call_nar_649
    m "It was an accident, my hands aren't what they once were."
    her "Ughhh, now I'm going to have to go change before classes."
    her "I expect to be compensated accordingly."
    m "Ok, ok. How about I give you a nice massage to calm you down."
    her "A massage? That's hardly fair compensation!"
    m "Are you sure?"
    her "Positive."
    m "Ok, I'll make a bet with you then."
    her "...{p}Go on..."
    m "I'll start massaging you. If you don't like it after two minutes then you can tell me to stop."
    her "And what do I get for telling you to stop?"
    m "two hundred points."
    her "two hundred points!"
    m "But if you don't ask me to stop I get to massage you for as long as I like, wherever I like."
    her "Deal."
    m "Are you sure?"
    her "No offense [genie_name], but I think I can resist a massage for 200 points."
    m "you sound confident. Care to raise the stakes?"
    her "Are you saying that I can earn more than 200 points?"
    m "five hundred."
    her "{size=+10}Five HUNDRED!{/size}" #size up
    her "Deal."
    m "I haven't even told you what happens if you lose."
    her "it doesn't matter, For 500 points I would turn down a massage from Viktor Krum himself."
    m "Well for the sake of the bet I'll explain anyway."
    m "I expect you to strip naked if you want to be massaged after your two minutes are up."
    her "Naked!"
    m "Only if you lose."
    her "Well I suppose that's OK then, it's not like I'll have to do it."
    m "well are you ready?"
    her "Yes, let's make it quick. I have to go back to the dorms and change after this. My shirt is soaked through."
    call nar(">Hermione walks over and stands in front of you.") from _call_nar_650
    her "So what's your plan? Do you expect me to give in just because you rub my shoulders?"
    m "Shoulders? Who said anything about shoulders?"
    her "Are you going to grope my butt again?"
    m "No, no. Today we're sticking with the fundamentals."
    call nar(">You grab her breasts through her soaked shirt.") from _call_nar_651
    her "!!!"
    m "There we are. I'll start the time now shall I?"
    her "What is wrong with me?"
    m "Nothing, apart from underestimating your elders."
    her "My breasts... they're on fire."
    m "If they were I think I would know."
    call nar(">You gently roll her nipples between your thumbs and forefingers.") from _call_nar_652
    her "!!!"
    her "Please [genie_name], you have to stop."
    m "You're not allowed to ask me to stop until the two minutes are up."
    m "And by my count there's still over a minute and a half to go."
    call nar(">You kneed her breasts firmly.") from _call_nar_653
    her "I'm calling off the bet..."
    m "Now now, no one likes a quitter."
    her "This isn't a joke, it feels like..."
    her "It feels amazing..."
    m "I told you I'm good."
    her "No [genie_name], this is the best thing I've ever felt."
    her ""
    
label potion_scene_3_2_2: #Hyper sensitive mouth/throat
    
label potion_scene_3_2_3: #Hyper sensitive pussy
    
    
### HYPNO POTION ###    
    
### FACE NEEDS UPDATE ###
### EYE COLOR NEEDS TO BE CHANGED ###

label potion_scene_3_3_1: #Hypno potion
    m "[hermione_name], I have another special potion for you today."
    call her_main("Who are you even buying these off?","normal","frown") from _call_her_main_6106
    m "A good magician never tells."
    call her_main("Magician? You're a wizard, and this better not have any long-term side effects.","normal","frown") from _call_her_main_6107
    call her_main("I'm still coughing up fur balls every now again from that polyjuice potion.","normal","frown") from _call_her_main_6108
    m "Of course it won't, now would you kindly drink the potion."
    call her_main("...","annoyed","angryL") from _call_her_main_6109
    call her_chibi("drink_potion","mid","base") from _call_her_chibi_183
    with d3
    hide screen hermione_blink
    call nar(">Hermione cautiously starts drinking the potion.") from _call_nar_654
    call her_main("","cum","worriedCl") from _call_her_main_6110
    pause .5
    call her_chibi("stand","mid","base") from _call_her_chibi_184
    
    call her_main("This isn't bad at all.","base","squint") from _call_her_main_6111
    call her_main("I feel...","base","happyCl") from _call_her_main_6112
    m "You feel what?"
    call her_main("I-I feel grea--","annoyed","down") from _call_her_main_6113
    call nar(">Hermione's eyes go blank and she stares forward blankly.") from _call_nar_655
    call her_main("What am I?","grin","dead") from _call_her_main_6114
    m "Uhm..."
    m "(Should have thought of something. At least the potion seems to work. Lets see...)"
    menu:
        "-You're an air-headed bimbo-":
            show screen blktone
    #call set_h_hair(hair_style="B",color=2)
    call her_main("I am an airheaded bimbo who only wants to make people happy...","soft","dead") from _call_her_main_6115
    menu:
        "-You love being covered in my cum-":
            pass
    $ hermione_badge = "characters/hermione/accessories/badges/cum_badge.png"
    $ hermione_badges = True
    call her_main("I love being covered in your cum...","soft","dead") from _call_her_main_6116
    menu:
        "-Your breasts are incredibly sensitive to pleasure-":
            pass
    call her_main("My breasts are incredibly sensitive to pleasure......","soft","dead") from _call_her_main_6117
    pause.5
    
    hide screen blktone
    call nar(">Hermione closes her eyes and appears to nod off.") from _call_nar_656
    call her_main("......","base","closed") from _call_her_main_6118
    call her_main("Where am I?","upset","wink") from _call_her_main_6119
    m "You're in my office."
    call her_main("I am?","upset","wink") from _call_her_main_6120
    call her_main("How did I get here?","upset","wink") from _call_her_main_6121
    m "You walked in here about 2 minutes ago."
    call her_main("Huh, I must have forgotten, silly old me.","base","squint") from _call_her_main_6122
    call her_main("So professor, what am I doing here?","base","down") from _call_her_main_6123
    call her_main("Aaaaaaah!!!!","shock","worriedCl",cheeks="blush") from _call_her_main_6124
    call her_main("What happened to my outfit?!","shock","down_raised") from _call_her_main_6125
    call her_main("I can't be seen wearing all this stuff!!!","disgust","down") from _call_her_main_6126
    
    if hermione_wear_top:
    
        call set_hermione_action("lift_top") from _call_set_hermione_action_140
        pause.5
    
        $ hermione_wear_top = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_141
        pause.5
    
        call her_main("That's soooooo much better!","soft","ahegao") from _call_her_main_6127
    
    if hermione_wear_bottom:
        call her_main("It really suuuuucks that I have to wear anything at all in this boring nunnery...","annoyed","ahegao") from _call_her_main_6128
        call her_main("(I can still wear something shorter. Like a skirt...)","") from _call_her_main_6129
        call her_main("(A reeealy short one!!!{image=textheart}{image=textheart}{image=textheart})","grin","happyCl") from _call_her_main_6130
    
        call set_hermione_action("lift_bottom") from _call_set_hermione_action_142
        pause.5
    
        $ hermione_wear_bottom = False
        call set_hermione_action("none","skip_update") from _call_set_hermione_action_143
        pause.5
        
        call her_main("I bet you like watching me strip mistah{image=textheart}","smile","glance") from _call_her_main_6131
        
    call her_main("I'm not sure what under-thingies I should wear though...","annoyed","down_raised") from _call_her_main_6132
    call her_main("Definitely something in pink!!!","smile","happyCl") from _call_her_main_6133
    hide screen hermione_main
    call blkfade from _call_blkfade_196
    
    call nar("Hermione pulls out her wand and casts a spell...") from _call_nar_657
    
    #Setting up Bimbo clothes.
    $ h_hair_color = 2 #Blonde
    $ h_lipstick = "red"
    
    $ h_request_wear_top = True
    $ h_top = "uni_top_5"
    
    $ h_request_wear_bottom = True
    $ h_skirt = "uni_skirt_4_low"
    $ h_skirt_color = "purple"
    
    $ h_request_wear_bra = True
    $ h_bra = "bra_lace"
    $ h_bra_color = "pink"
    
    $ h_request_wear_panties = True
    $ h_panties = "panties_lace"
    $ h_panties_color = "pink"
    
    $ h_request_wear_neckwear = True
    $ h_neckwear = "neck_lace_choker"
    
    $ h_request_wear_stockings = True
    $ h_stockings = "stockings_fishnets"
    
    call load_hermione_clothing_saves from _call_load_hermione_clothing_saves_7
    call update_her_hair from _call_update_her_hair_4 #Always update hair before the uniform! In case she wears cat-ears!
    call update_her_uniform from _call_update_her_uniform_98
    
    pause.5
    call her_main("","base","glance") from _call_her_main_6134
    call hide_blkfade from _call_hide_blkfade_143
    call ctc from _call_ctc_340
    
    call her_main("Do you like it mistah?","grin","happyCl") from _call_her_main_6135
    
    menu:
        g9"!!!"
        "-You look amazing!-":
            call her_main("Thank youuuuu!!!{image=textheart}{image=textheart}{image=textheart}","grin","ahegao") from _call_her_main_6136
            call her_main("Aaaaanyway...","open","baseL") from _call_her_main_6137
            call her_main("Is there anything you want from me mistah... I'll do anything!{image=textheart}","soft","glance") from _call_her_main_6138
        "-Where is your badge, cumslut?!-":
            call her_main("Oh no I forgot that!","soft","wide") from _call_her_main_6139
            call her_main("I'm soooo sorry!!!","shock","worriedCl",cheeks="blush") from _call_her_main_6140
            call her_main("It's this one, isn't it...","soft","down") from _call_her_main_6141
            call nar("Hermione conjures an -I {image=textheart} Cum- badge, which magically attaches itself to her breasts.") from _call_nar_658
            
            $ h_request_wear_body_accs = True
            $ hermione_body_accs_list = []
            $ hermione_body_accs_list.append("badge_I_love_cum")
            
            call load_hermione_clothing_saves from _call_load_hermione_clothing_saves_8
            call update_her_uniform from _call_update_her_uniform_99
            
            call her_main("Yay! Do you like it?","grin","happyCl") from _call_her_main_6142
            call her_main("Anything else you want from me mistah?... I'll do anything!{image=textheart}","soft","glance") from _call_her_main_6143
    
    
    m "I'm just going to ask you a few questions."
    call her_main("(...)","annoyed","angry") from _call_her_main_6144
    call her_main("(And here I hoped he'd just ask to fuck...)","annoyed","angryL") from _call_her_main_6145
    call her_main("(Questions are so boooring! I hope they are at least naughty...)","annoyed","ahegao") from _call_her_main_6146
    call her_main("Are those questions going to be hard, mistah?","grin","worriedCl",emote="05") from _call_her_main_6147
    call her_main("I don't like hard questions.","grin","worriedCl") from _call_her_main_6148
    m "Don't worry they'll be nice and easy for you."
    call her_main("yay!","smile","happyCl") from _call_her_main_6149
    m "First question, Who are you?"
    call her_main("That's an easy one! I'm Hermione Granger, the prettiest girl in the whole school!","smile","happyCl",emote="06") from _call_her_main_6150
    m "And what are your hobbies?"
    call her_main("Doing my makeup{image=textheart}, dancing{image=textheart} and dressing happy{image=textheart}!","base","happyCl") from _call_her_main_6151
    m "Dressing happy?"
    call her_main("You know, wearing nice things to make other people happy!{image=textheart}","base","ahegao_raised") from _call_her_main_6152
    m "You like making people happy?"
    call her_main("Of course mistah professor, making people happy{image=textheart} makes me happy{image=textheart}!","smile","happyCl") from _call_her_main_6153
    call her_main("Once I finish school I want to get a job where all I do is make people happy{image=textheart}!","base","happyCl") from _call_her_main_6154
    m "Ok, final question;"
    m "How would you like to make yourself happy?"
    call her_main("Make myself happy?","annoyed","down") from _call_her_main_6155
    call her_main("But I'm already happy, silly!","base","happyCl") from _call_her_main_6156
    m "Even happier."
    call her_main("Even happier? {size=+10}YAY!{/size}","smile","happyCl",emote="06") from _call_her_main_6157
    call her_main("So how am I going to be happier? Am I going to get naked?","grin","baseL") from _call_her_main_6158
    m "That'd be a good start."
    call her_main("{image=textheart}AAAAAAWWWEEESOOOOOOOOMMME!{image=textheart}","grin","ahegao") from _call_her_main_6159
    
    call set_hermione_action("lift_top") from _call_set_hermione_action_144
    pause.5
    
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call set_hermione_action("none","skip_update") from _call_set_hermione_action_145
    pause.5
    
    call her_main("You know they don't let us walk around naked at school?","annoyed","angryL") from _call_her_main_6160
    m "Really? I can't imagine why not."
    call her_main("I know right? It's like so dumb! Everyone would just be happier{image=textheart} if they got to be naked.","soft","ahegao") from _call_her_main_6161
    
    call set_hermione_action("lift_skirt") from _call_set_hermione_action_146
    pause.5
    
    $ hermione_wear_bottom = False
    $ hermione_wear_panties = False
    call set_hermione_action("none","skip_update") from _call_set_hermione_action_147
    pause.5
    
    call her_main("I know everyone who sees me naked is happy!","base","glance") from _call_her_main_6162
    m "You've certainly made me happy."
    call her_main("Thanks mistah professor sir! That makes me so happy{image=textheart}!","grin","worriedCl") from _call_her_main_6163
    m "(I don't think I can stand her saying the word happy much more...)"
    m "Now Hermione, I want you to touch your breasts."
    call nar(">Hermione moves her hands up to her breasts") from _call_nar_659
    call set_hermione_action("lift_breasts") from _call_set_hermione_action_148

    call her_main("Like this? This feels sooooo gooood!","base","down") from _call_her_main_6164
    call her_main("It's like mah hands are moving on their own...","soft","ahegao") from _call_her_main_6165
    call her_main("It's soooo goodd but It's weeeiiird... I need something... anything...","open","worriedCl") from _call_her_main_6166
    m "Would you like to touch yourself down there?"
    call her_main("Yes mistah [genie_name]. please.","shock","worriedCl") from _call_her_main_6167
    
    menu:
        "-make her beg-":
            m "I want you to beg."
            call her_main("Please mistah sir...","shock","worriedCl") from _call_her_main_6168
            m "Please what?"
            call her_main("Ohmigawd Please let me touch myself down there... I'll do anything...","clench","worried",cheeks="blush",tears="soft") from _call_her_main_6169
            m "Anything?"
            call her_main("Anything. I just need to feel happy...","silly","worried",cheeks="blush",tears="soft") from _call_her_main_6170
            m "Tell me what you are and I'll let you."
            call her_main("I'm Hermione, the school slut.","grin","ahegao") from _call_her_main_6171
            m "More."
            call her_main("geez, I'm a dumb bimbo fuckbunny... that just wants to feel happy...","silly","ahegao") from _call_her_main_6172
            m "And what makes you happy?"
            call her_main("Making you happy{image=textheart} [genie_name].","silly","dead") from _call_her_main_6173
            m "Good girl."
        "-let her touch herself-":
            m "Go on then."
            call her_main("Thank you soooo{image=textheart} much [genie_name]!","silly","ahegao") from _call_her_main_6174
            
    call set_hermione_action("covering") from _call_set_hermione_action_149
    call her_main("This is soooo goood","grin","ahegao") from _call_her_main_6175
    call her_main("Mistah [genie_name] can you please do something for me?","grin","wink",cheeks="blush") from _call_her_main_6176
    m "What's that?"
    call her_main("If it's not tooo much trouble could you...","silly","ahegao") from _call_her_main_6177
    call nar(">Hermione starts pinching her nipple.") from _call_nar_660
    call set_hermione_action("pinch") from _call_set_hermione_action_150
    call her_main("could you please cum on me?","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_6178
    m "Well if it makes you happy."
    call nar(">you stand up and head towards her.") from _call_nar_661
    call her_main("thank you, thank you thank you! You're the best headmaster {size=+5}EVER!{/size}","smile","happyCl",emote="06") from _call_her_main_6179
    
    hide screen hermione_main
    call blkfade from _call_blkfade_197
    
    hide screen genie
    call gen_chibi("jerking_off","desk","base") from _call_gen_chibi_114
    show screen chair_left
    show screen desk

    hide screen blktone
    hide screen bld1
    call hide_blkfade from _call_hide_blkfade_144
    call ctc from _call_ctc_341
    
    call set_hermione_action("covering") from _call_set_hermione_action_151
    call her_main("...","base","ahegao_raised") from _call_her_main_6180
    call set_hermione_action("pinch") from _call_set_hermione_action_152
    call her_main("I don't know how other girls do it...","annoyed","down") from _call_her_main_6181
    m "Do what?"
    call her_main("Stop themselves from coming here and getting you to cover them in yummy cummy!","annoyed","down") from _call_her_main_6182
    call set_hermione_action("covering") from _call_set_hermione_action_153
    call her_main("I mean I can barely stop mahself coming here everyday!","smile","happyCl") from _call_her_main_6183
    m "That's it..."
    call set_hermione_action("pinch") from _call_set_hermione_action_154
    call her_main("Hmmm, I just luv playin' with mah boobies{image=textheart}{image=textheart}{image=textheart}","base","ahegao_raised") from _call_her_main_6184
    call her_main("They're just so soft...","open","ahegao_raised",cheeks="blush") from _call_her_main_6185
    call set_hermione_action("covering") from _call_set_hermione_action_155
    call her_main("And they feel soo good. They're really sensi--","base","ahegao_raised",cheeks="blush") from _call_her_main_6186
    call her_main("Sensi---","base","ahegao_raised",cheeks="blush") from _call_her_main_6187
    call set_hermione_action("pinch") from _call_set_hermione_action_156
    call her_main("What's the word?","annoyed","ahegao_raised",cheeks="blush") from _call_her_main_6188
    m "Sensitive."
    call set_hermione_action("covering") from _call_set_hermione_action_157
    call her_main("That's right they're really sensitive!","silly","ahegao_raised",cheeks="blush") from _call_her_main_6189
    m "So am I..."
    call her_main("Are you going to cum?","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_6190
    call set_hermione_action("pinch") from _call_set_hermione_action_158
    call her_main("Please do it on my face!","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_6191
    call her_main("No wait my tits...","scream","worriedCl",cheeks="blush") from _call_her_main_6192
    call set_hermione_action("covering") from _call_set_hermione_action_159
    call her_main("No wait my face!","silly","ahegao_raised",cheeks="blush") from _call_her_main_6193
    
    menu:
        "-Cum on her face-":
            g4 "Here it comes slut!"
            call her_main("{image=textheart}!!!{image=textheart}","shock","wide",cheeks="blush") from _call_her_main_6194
            call gen_chibi("cumming","desk","base") from _call_gen_chibi_115
            $ u_sperm = "characters/hermione/face/auto_07.png"
            $ uni_sperm = True
            g4 "that's it, all over your face."
            call set_hermione_action("pinch") from _call_set_hermione_action_160
            call her_main("...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush") from _call_her_main_6195
        "-Cum on her tits-":
            g4 "Here it comes fuckbunny!"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","shock","wide",cheeks="blush") from _call_her_main_6196
            call gen_chibi("cumming","desk","base") from _call_gen_chibi_116
            $ u_sperm = "characters/hermione/face/auto_02.png"
            $ uni_sperm = True
            g4 "All over your tits."
            call set_hermione_action("pinch") from _call_set_hermione_action_161
            call her_main("It's so warm...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush") from _call_her_main_6197
        "-cover her in cum-":
            g4 "Here it comes whore!"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","shock","wide",cheeks="blush") from _call_her_main_6198
            call gen_chibi("cumming","desk","base") from _call_gen_chibi_117
            $ u_sperm = "characters/hermione/face/auto_05.png"
            $ uni_sperm = True
            g4 "that's right slut, All over you."
            call set_hermione_action("pinch") from _call_set_hermione_action_162
            call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush") from _call_her_main_6199
    
    call gen_chibi("hold_dick","desk","base") from _call_gen_chibi_118
    call her_main("...","grin","ahegao") from _call_her_main_6200
    $ hermione_dribble = True
    call her_main("That felt {size=+5}SOOOOO!{/size} good!","silly","ahegao") from _call_her_main_6201
    call set_hermione_action("lift_breasts") from _call_set_hermione_action_163
    
    call her_main("Can we do it again! Please! Pretty please! Pretty please with cum on top!","silly","dead") from _call_her_main_6202
    m "Not today."
    call her_main("Awwwwww.","shock","worriedCl") from _call_her_main_6203
    
    hide screen hermione_main
    call blkfade from _call_blkfade_198
    
    call gen_chibi("hide") from _call_gen_chibi_119
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base") from _call_her_chibi_185
    call hide_blkfade from _call_hide_blkfade_145
    
    call her_main("Well ok... I suppose I'll head to class then.","open","down") from _call_her_main_6204
    m "About that. I think it'd be better if you went back to your dorm."
    call her_main("Why's that mistah [genie_name] sir?","annoyed","base") from _call_her_main_6205
    m "I think you need to have a little nap and let this wear off."
    call her_main("whatever you say sir!","annoyed","closed") from _call_her_main_6206
    call set_hermione_action("none","skip_update") from _call_set_hermione_action_164
    call her_main("And thanks again!{image=textheart} You're the best!","smile","happyCl",emote="06") from _call_her_main_6207

    call her_walk("desk","leave",2.5) from _call_her_walk_123
    
    m "(Maybe I should have told her to get dressed first...)"
    
    $ reward_her_red_lipstick = True #Unlocks red lipstick
    call give_reward(">Hermione can now use red lipstick!","images/store/lipstick.png") from _call_give_reward_20 #Need lipstick shop image!
    
    call reset_hermione_main from _call_reset_hermione_main_9
    
    call music_block from _call_music_block_19
    jump day_main_menu
      

### AHEGAO POTION ###

label potion_scene_3_4_1: 
    m "How long until your next class [hermione_name]?"
    call her_main("about fifteen minutes sir.","open","base") from _call_her_main_6208
    m "in that case I think you might have to be a little late."
    call her_main("what? why?","open","worried") from _call_her_main_6209
    g4 "Well, it might be a bit hard for you to attend class with my cock buried in your tight little pussy."
    call her_main("Oh...","soft","squintL") from _call_her_main_6210
    m "That's not going to be a problem is it [hermione_name]?"
    call her_main("of course not [genie_name]! Let me just take my clothes off...","grin","ahegao") from _call_her_main_6211

    show screen blkfade
    with d3
    hide screen bld1
    hide screen hermione_blink
    #SEX
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_main("ahhhhhhhhh....{image=textheart}","scream","wide") from _call_her_main_6212
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ ccg_folder = "herm_sex"
    $ ccg1 = "blank"
    $ ccg3 = "blank"
    $ ccg2 = 1
    show screen ccg
    hide screen blkfade
    with d3
    her "Ah...{image=textheart}"
    g4 "mmmm, you like that don't you slut?"
    $ ccg2 = 2
    her "yes...{image=textheart}"
    $ ccg2 = 3
    her "even though I have to miss class..."
    $ ccg2 = 4
    her "I Honestly don't care...{image=textheart}"
    $ ccg2 = 5
    her "This just feels too goooood..."
    pause
    ">You quietly pull out the small vial from your pocket and pull the stopper out."
    $ ccg2 = 6
    her "Mmmm, don't slow down [genie_name]..."
    g4 "You asked for it!"
    ">You speed up the pace as you go to pour a drop onto her ass, your hand barely managing to stay stable..."
    $ ccg2 = 7
    her "Harder [genie_name]!!!"
    pause
    ">You feel hermione suddenly push her pussy back towards you, causing you to spill about a quarter of the vial onto her ass..."
    $ ccg3 = "p1"
    m "..."
    $ ccg2 = 8
    her "What was that?"
    m "Ugh... nothing... just a bit of spit. Keep going slut."
    $ ccg2 = 9
    her "Ah...{image=textheart} alright then..."
    ">You quickly put the stopper back into the vial and slip it back into your robes."
    $ ccg2 = 10
    her "Ah... ah... ah..."
    pause
    $ ccg2 = 11
    her "[genie_name], you think you could... ah..."
    g4 "What is it slut?"
    $ ccg2 = 12
    her "Could you please... spank me... ah...?"
    g4 "of course!"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">You give her ass a hard spank, accidentally causing the potion to explode out from underneath your hand, coating her even more."
    $ ccg3 = "p2"
    $ ccg2 = 13
    pause
    her "{size=+10}!!!{/size}"
    ">Hermione's sopping cunt starts contracting around your cock uncontrollably."
    g4 "Mmmm, cumming already slut?"
    $ ccg2 = 14
    her "Y-yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 15
    her "I{image=textheart} can't{image=textheart} stop..........{image=textheart}{image=textheart}{image=textheart}"
    ">True to her word, you don't feel an end to her relentless spasming."
    g4 "I love it when cum on my cock whore!"
    $ ccg2 = 16
    pause
    her "no...{image=textheart} sir...{image=textheart} you...{image=textheart} don't...{image=textheart} understand...{image=textheart}"
    $ ccg2 = 17
    her "It...{image=textheart} won't...{image=textheart} stop...{image=textheart}"
    g4 "I don't see how that's my problem!"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">You give her ass another hard slap, savoring the feeling of another orgasm flowing through the young witch."
    $ ccg2 = 18
    her "{size=+10}!!!{/size}"
    $ ccg2 = 19
    her "its......{image=textheart} {image=textheart} "
    $ ccg2 = 20
    pause
    her "my{image=textheart}  whole{image=textheart}  body...{image=textheart}{image=textheart}{image=textheart} "
    g4 "Speak up slut!"
    $ ccg2 = 21
    her "My body's...{image=textheart} {image=textheart} on fire..."
    $ ccg2 = 22
    her "I can't...{image=textheart}"
    $ ccg2 = 23
    her "why...{image=textheart}"
    $ ccg2 = 24
    her "Why {image=textheart}does {image=textheart}it {image=textheart}feel {image=textheart}this {image=textheart}goooooooooood...{image=textheart}{image=textheart}{image=textheart}"
    g4 "enjoying yourself are we?"
    $ ccg2 = 25
    her "No...{image=textheart} ah... yesssss....{image=textheart}"
    $ ccg2 = 26
    her "it's like...{image=textheart}"
    $ ccg2 = 27
    her "each time you thrust...{image=textheart}{image=textheart} that big fat {image=textheart}cock{image=textheart} in me...{image=textheart}"
    $ ccg2 = 28
    pause
    her "it's like I {image=textheart}{image=textheart}cum{image=textheart}{image=textheart}..."
    her "But it never resets..."
    $ ccg2 = 29
    her "Each time is just another stronger {image=textheart}orgasm{image=textheart}..."
    $ ccg2 = 30
    her "{size=+10}AND{image=textheart} THEY{image=textheart} NEVER{image=textheart} STOOO{image=textheart}OOOP!!!!!!"
    g4 "Sounds nice... and what about when I give your fat ass a nice... slap?"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">You give her ass another hard slap, holding your hand against her warm flesh, swirling the potion around underneath it."
    $ ccg2 = 31
    her "{size=+20}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{/size}"
    $ ccg2 = 32
    her "{image=textheart}my{image=textheart} {image=textheart}brain...{image=textheart}"
    $ ccg2 = 33
    her "You're{image=textheart} going{image=textheart} to{image=textheart} kill{image=textheart} me...{image=textheart}"
    g4 "Stop being so overdramatic..."
    pause
    $ ccg2 = 34
    her "I'm not...{image=textheart}"
    her "Ah.....{image=textheart} some....{image=textheart} thing....{image=textheart} is....{image=textheart} wrong....{image=textheart}"
    ">Hermione's words start to slow, eventually only being able to mutter a squeak of a word every time you thrust into her."
    g4 "Maybe it was the potion I poured all over your ass earlier?"
    $ ccg2 = 35
    her "{size=+20}{image=textheart}{image=textheart}what?{image=textheart}{image=textheart}{/size}"
    g4 "Don't worry, the effects should wear off in about an hour..."
    $ ccg2 = 36
    her "{size=+20}!!!!!!!{/size}"
    g4 "In the mean time, why don't you just sit back and enjoy the ride."
    $ ccg2 = 37
    her "{image=textheart}e-e-enjoy....{image=textheart}"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    $ ccg2 = 38
    pause
    her "{size=+20}!!!!!!!{/size}"
    $ ccg2 = 39
    her "Pleeeease...{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 40
    her "my...{image=textheart}mind...{image=textheart}is...{image=textheart}breaking...{image=textheart}"
    ">You start to pick up the pace, treating her as nothing more than your mewling fuckmeat..."
    g4 "MMMM, you always know what to say to get me going!!"
    $ ccg2 = 41
    her "...{image=textheart}{image=textheart}{image=textheart}"
    ">Eventually the endless spasming of her drenched pussy around your cock proves too much."
    g4 "Ah!!! Here It comes whore!"
    $ ccg2 = 42
    pause
    her "{image=textheart}........{image=textheart}"
    ">You start firing cum directly into her womb."
    $ ccg3 = "s4"
    $ ccg2 = 43
    pause
    her "{image=textheart}!!!{image=textheart}"
    g4 "TAKE THIS!!!"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">You give her ass one last slap, stinging your hand as you shoot the last rope into her waiting cunt."
    $ ccg3 = "s5"
    $ ccg2 = 44
    pause
    her "{image=textheart}........{image=textheart}"
    her "{image=textheart}...............{image=textheart}"
    $ ccg2 = 45
    pause
    her "{image=textheart}.......................{image=textheart}"
    show screen blkfade
    with d3
    ">Eventually hermione's eyes roll back into her head as she collapses forward onto your desk."
    ">you carry her unconscious body back to her room to sleep the last of the potion off."
    hide screen ccg
    hide screen hermione_main
    hide screen hermione_blink
    show screen genie
    hide screen blkfade
    with d3
    $ hermione_takes_classes = True
    jump day_main_menu