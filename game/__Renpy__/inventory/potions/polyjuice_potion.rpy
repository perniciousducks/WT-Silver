#Need a check if it's her first potion (is_first_potion)
#Need a check if she has drunk any kind of polyjuice potion (polyjuice_drunk)
#Need Check if she has drunk Luna potion before (her_luna_polyjuice_drunk)
#All scenes (cat/Luna) needs posing, add ending where it fails, whoring level requirements.
#Character is incorectly positioned in some segments (infront of textbox) - done
#The image segment changing when she swallows looks a bit weird
#I probably fucked up some statements on how it should display when she has drunk Luna potion before/not drunk it before.

### POLYJUICE POTION ###

#Cat ears. 

init:
    $ hg_pp_polyjuice = event_class(title = "Polyjuice", start_label = "hg_pp_polyjuice", 
    events = [[["hg_pp_polyjuice_T1_intro"],["hg_pp_polyjuice_T1_E1"],["hg_pp_polyjuice_T1_E2"],["hg_pp_polyjuice_T1_E3"]]],
    iconset = [["heart_empty", "heart_green"]],
    #Extra variables
    done_blowjob=False)
    
label hg_pp_polyjuice: #catears (keep in mind Genie is trying to transform her into another girl)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?","base","base")
    if hg_pp_polyjuice.counter < 1: # Add counter check for all potions instead
        m "So, are you ready to try out one of my potions?"
        her "As ready as I'll ever be..."
        m "great!"
        m "I have this potion for you to try out."
    else:
        m "I have another potion for you to try out today..."
        if hg_pp_polyjuice.counter > 0:
            her "Is this another polyjuice potion?"
            m "...{w}no?"
            if her_whoring < 12:
                her "I'm not drinking another one... I remember what happened last time."
                m "(Damn, looks like she wont be as keen now that she knows what she's drinking...)"
                jump hermione_requests
            else:
                her "You're lying..."
                her "Do I have to?"
                m "You don't have to do anything [hermione_name]..."
                m "But if you do decide to, it would make me very happy...."
                her "..."
                m "And there's some points in it for you as well..."
        else:    
            if her_whoring >= 12:    
                call her_main("If it makes you happy, [genie_name].","smile","base")
                call her_main("...","annoyed","down_raised")
            elif her_whoring >= 6:
                call her_main("And what kind of potion is it? It looks gross...","normal","frown")
                m "Well, wouldn't it spoil half the enjoyment of it if I told you?"
                call her_main("Depends whose enjoyment you're talking about...","open","suspicious")
                m "20 points."
                call her_main("Hmmm, can't you tell me what kind of potion it is?","annoyed","suspicious")
                call her_main("Polyjuice? Amortentia? Babbling Beverage? Felix Felicis?","grin","worriedCl",emote="05")
                m "That's going to have to stay a secret [hermione_name]."
                call her_main("...","annoyed","down")
                m "Well [hermione_name], what do you say? Will you drink a harmless little potion?"
                m "For Gryffindor?"
                call her_main("Fine...","open","closed")
            else: #Fail
                call her_main("And what kind of potion is it? It looks gross...","normal","frown")
                m "Well, wouldn't it spoil half the enjoyment of it if I told you?"
                her "I'm not going to drink some random potion for your amusement."
                m "There's some points in it for you of course."
                her "..."
                her "No thanks..."
                jump hermione_requests
    
    $ renpy.sound.play("sounds/sniff.mp3")    
    call nar(">Hermione takes a whiff of the thick potion.")
    call her_main("It smells disgusting. Like mud and wet dog fur.","disgust","narrow")
    call her_main("Do I really have to drink this?","open","worried")
    m "You do. I suggest holding your nose if the smell is too much."
    call her_main("For Gryffindor.","mad","worriedCl",tears="soft_blink")

    hide screen hermione_main
    with d3
    pause.2

    $ renpy.sound.play("sounds/gulp.mp3")    
    call her_chibi("drink_potion","mid","base")
    pause 2
    call nar(">She downs the thick potion.")
    pause.5
    call her_chibi("stand","mid","base")
    pause.2
    call her_main("Blehgh.","disgust","narrow")
    m "Well done."
    
    if hg_pp_polyjuice.counter > 0:
        her "Here we go again I suppose..."
        her "Nothing's happening..."
        m "You'll just have to wait a minute remember?"
        her "In that case I'll be back after class..."
        her "Can't wait for the effects to kick in... it was bad enough the first time..."
        m "I'm sure another extra 10 points should make it worth it, [hermione_name], 30 points to Gryffindor."
        call her_main("Thank you [genie_name].","base","base")
        call nar(">Hermione heads off to class.")
        $ gryffindor += 30
    else:
        call her_main("Now will you at least tell me what this potion does?","angry","base",tears="soft")
        m "It should be noticeable any second now..."
        call her_main("Well? Is it supposed to make my breasts bigger? They don't feel any bigger.","annoyed","down")
        m "No. Hmmmm, it mustn't have worked."
        call her_main("What was it supposed to do?","annoyed","ahegao")
        m "There's no point in telling you now. It was going to be a surprise."
        call her_main("Is that all [genie_name]?","soft","base")
        m "Yes, [hermione_name], 20 points to Gryffindor."
        call her_main("Thank you [genie_name].","base","base")
        call nar(">Hermione heads off to class.")
        $ gryffindor += 20

    call her_walk(action="leave", speed=2)


    #$ cat_ears_potion_return = True #Triggers Hermione return

    #Equip Cat-Ears
    #$ h_ears = "cat_ears"
    #$ h_request_wear_ears = True
    #$ hermione_wear_ears = True
    #call update_her_uniform
    $ hg_pp_polyjuice.inProgress = True
    $ hermione_busy = True

    jump main_room
    
label hg_pp_polyjuice_T1_intro:
    call her_walk(action="enter", xpos="mid", ypos="base", speed=1.6)
    
    call her_main("How could you do this to me [genie_name]?","angry","angry", xpos="mid", ypos="base", trans="hpunch")
    her "Try and turn me into a cat!"
    call her_main("In the middle of class!","annoyed","worriedL")
    m "I didn't try and turn you into a cat [hermione_name]."
    call her_main("Then why do I have ears and a tail?","scream","angryCl")
    m "I have no idea. The potion I gave you was supposed to turn you into a different girl."
    call her_main("What!? You didn't use polyjuice potion did you [genie_name]?","shock","wide")
    m "What's that?"
    call her_main("There's no point playing dumb [genie_name].","annoyed","annoyed")
    call her_main("Well at least I know that it will wear off by morning.","annoyed","angryL")
    
    if her_whoring >= 17:
        call her_walk(xpos="door", speed=2)
        nar "You see Hermione reaching for the door knob but an idea strikes you."
        menu:
            "-Make her suck you off-":
                # Introduction to kitty blowjob scene
                label hg_pp_polyjuice_suck_intro:
                $ hg_pp_polyjuice.done_blowjob = True
                m "Wait, [hermione_name]!"
                call her_chibi("stand","door",flip=False)
                with d3
                her ".......?"
                call her_walk(xpos="desk", speed=2.5)
                call her_main("What is it, [genie_name]?","upset","angry")
                call her_main("Haven't you humiliated me enough?","annoyed","closed")
                call her_main("","annoyed","baseL")
                m "Would you like to earn 75 additional points?"
                call her_main("75 points? How?","annoyed","suspicious")
                
                g9 "By sucking my cock, obviously."
                call her_main("Right now? I look like a cat! Why would you ask me at a time like this?","angry","wide")
                call her_main("You're not some sort of pervert who likes animals are you?","angry","base")
                m "Of course not, I just think that you have a very unique look at the moment and that it would be a shame not to do anything with it."
                call her_main("Fine, just promise me you aren't going to do anything weird.","upset","closed")
                m "I promise. Now, kneel."
                
                #Fade to black
                show screen blkfade with d3
                pause.5
                ">Hermione walks over and kneels before you."
                $ gen_chibi_xpos = -10
                $ gen_chibi_ypos = 10
                call set_u_ani("blowjob_ani","hand_ani", 0,10)
                $ g_c_u_pic = "hand_ani"
                call u_pause_ani
                hide screen hermione_main
                hide screen genie
                call her_chibi("hide")
                show screen chair_left
                hide screen blkfade
                with d5
                
                m "Good girl."
                m "Now open wide."
                call her_main("...","open_wide_tongue","base")
                call u_play_ani
                
                ">Hermione takes you into her mouth"
                hide screen hermione_main
                hide screen genie
                call ctc
                m "Good god what is with your tongue?! It feels like velcro."
                her "*Slurp?*"
                
                call u_pause_ani
                
                call her_main("It's because of your stupid potion, it made my tongue all rough.","open_wide_tongue","angry")
                call her_main("Do you want to stop?","grin","baseL")
                hide screen hermione_main
                m "No, keep going, just try not to focus on the tongue work too much."
                call her_main("Okay, [genie_name].","annoyed","angryL")
                hide screen hermione_main
                
                call u_play_ani
                
                call nar(">Hermione swallows your cock again, taking care not to apply too much pressure with her tongue.") #start sucking scene. might insert more sucking noises for a little while or add pauses
                m "So..{w=1.0} did you attend all your classes today?"
                
                call u_pause_ani
                
                call her_main("Of course [genie_name].","base","glance")
                
                hide screen hermione_main
                call u_play_ani
             
                m "Even looking like this?"
                m "What would everyone have thought? Would they just assume that you were a victim of a prank?"
                m "Or would they just think that slutty little Miss Granger was just begging for attention again."
                m "Wearing skimpy outfits and trying to look like a pussy-cat."
                call nar(">You try place your hand on the back of her head but her new ears are in the way.")
                m "These are quite soft."
                call nar(">You start feeling and petting her brand new ears.","start")
                call nar(">Hermione starts involuntary purring..","end")
                #
                # Add a purr sound? :D
                #
                pause 1.0
                g4 "Oh good heavens!"
                m "It's like your whole mouth has become a vibrator."
                call u_pause_ani
                call her_main("I can't help it [genie_name], when someone touches my ears I just purr.","base","happyCl")
                hide screen hermione_main
                m "It feels amazing, now cock back in the mouth girl."
                call her_main("Yes [genie_name].","smile","happyCl",emote="06")
                call u_play_ani
                hide screen hermione_main
                with d3
                call nar(">You immediately put your hands back on her ears and start stroking them as she sucks you off.")
                her "*Slurp!* *Purr* *Slurp!*"
                m "Oh god yes. This is Fantastic."
                her "*Purr* *Slurp!* *Purr*"
                m "Get ready girl... Here it comes."
                her "*Purr* *Purr* *Purr*"
                call nar(">You grab her ears and pull her head into you causing the tip of your cock to rest in her vibrating throat.")
                g4 "{size=+10}ARGH!!!!!!!!!!!!!!!!{/size}"
                #######################################
                call set_u_ani("cum_in_mouth_ani","hand_ani", 0,10)
                $ g_c_u_pic = "cum_in_mouth_ani"
                call cum_block
                her "*Purr* *Purr* *Purr*"
                call nar(">You shoot you load directly down her throat.") 
                call ctc
                
                with d3
                call her_main("","full_cum","dead")
                pause .1
                call her_main("*gulp* *Purr* *Purr*","cum","worriedCl")
                call her_main("","full_cum","dead")
                pause .1
                call her_main("*gulp* *Purr* *gulp*","cum","worriedCl")
                call her_main("","full_cum","dead")
                pause .1
                call her_main("*Purr* *gulp* *gulp*","cum","worriedCl")
                #
                call nar(">You pull your cock out of her purring mouth.")
                call her_main("Mmmmm, it might be this potion but that tasted good...","base","glance")
                hide screen hermione_main
                m "Well, you certainly earned your 75 points."
                $ gryffindor += 75
                with d3
                call her_main("Thank you [genie_name]. Will that be all.","base","ahegao_raised")
                m "One last thing."
                m "Who's a good girl?"
                call her_main("..........","annoyed","worriedL")
                call her_main("I am...","smile","baseL")
                
                show screen blkfade with d3

                call hide_characters
                call u_end_ani
                call her_chibi(xpos="desk")
                call gen_chibi("sit_behind_desk")
                
                hide screen blkfade with d5
                pause 1.0
            "-Let her go-":
                m "Maybe next time.."
                pass

    call her_walk(action="leave", speed=2)
    $ hermione_busy = True
    jump main_room

label hg_pp_polyjuice_T1_introCC:
    call her_walk(action="enter", xpos="mid", ypos="base", speed=1.6)

    if her_know_polyjuice:
        her "I can't believe you had me drink this again..."
        m "What's the problem? I think you look cute..."
        if her whoring < 6:
            her "The problem?"
            her "People kept making fun of me and pulling my tail!"
            m "And how did that make you feel?"
            her "Humiliated!"
            her "They kept asking if I was been a good kitty and if I wanted scratches..."
            her "And you know the worst thing?"
            m "What?"
            her "The darn potion sort of made me want scratches..."
            m "I see...{w} then we at least learnt something new here today."
        else:
            her "My class members had very similar thoughts..."
            her "One of the boys were entranced by the motion of my tail..."
            her "It seemed to have its own mind..."
            m "And how did that make you feel?"
            her "I'm not sure..."
    else:
        $ her_know_polyjuice = True
        call her_main("How could you do this to me [genie_name]?","angry","angry", xpos="mid", ypos="base", trans="hpunch")
        her "Try and turn me into a cat!"
        call her_main("In the middle of class!","annoyed","worriedL")
        m "I didn't try and turn you into a cat [hermione_name]."
        call her_main("Then why do I have ears and a tail?","scream","angryCl")
        m "I have no idea. The potion I gave you was supposed to turn you into a different girl."
        call her_main("What!? You didn't use polyjuice potion did you [genie_name]?","shock","wide")
        m "What's that?"
        call her_main("There's no point playing dumb [genie_name].","annoyed","annoyed")
        call her_main("Well at least I know that it will wear off by morning.","annoyed","angryL")
        

    menu:
        "-Let her go-":
            m "Goodnight [hermione_name]."
            call her_main("Goodnight [genie_name].","upset","closed")

            call her_walk(action="leave", speed=2)

            #$ cat_ears_potion_return = False #Triggers Hermione return
            #$ h_request_wear_ears = False
            #$ hermione_wear_ears = False
            #call update_her_uniform

            $ hermione_busy = True

            jump main_room

        "-Make her suck you off-" if her_whoring >= 17:
            pass

    m "Wait [hermione_name], how would you like to earn 75 additional points?"
    call her_main("75 points? How?","annoyed","suspicious")
    m "By sucking my cock."
    if polyjuice_drunk:
        her "Again?"
        her "I thought you found my tounge way to rough in this state?"
        m "Well, the purring certainly made well up for that aspect."
        her "Okay then..."
    else:    
        call her_main("Like this? I look like a cat! Why would you ask me at a time like this?","angry","wide")
        call her_main("You're not some sort of pervert who likes animals are you?","angry","base")
        m "Of course not, I just think that you have a very unique look at the moment and that it would be a shame not to do anything with it."
        call her_main("Fine, just promise me you aren't going to do anything weird.","upset","closed")
        m "I promise. Now, kneel."
    call blkfade
    pause.5

    ">Hermione walks over and kneels before you."
    m "Good girl."
    call her_main("...","open_wide_tongue","base")
    ">Hermione takes you into her mouth"                ###Have the chibi scene of her sucking
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie

    $ gen_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_left
    show screen g_c_u

    call her_chibi("hide")
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    with fade
    call ctc

    if polyjuice_drunk:
        call bld
        her "*Lick*"
        m "There's that tounge again...{w} could you try using your throat a bit more?"
        her "*Slurp*" #annoyed eyes
        $ g_c_u_pic = "hand_ani"
        with d3
        her "You sure you want me to continue?"
        m "Yes!"

    else:
        call bld
        m "Good god what is with your tongue?! It feels like velcro."
        her "*Slurp?*"
        $ g_c_u_pic = "hand_ani"
        with d3
        call her_main("It's because of your stupid potion, it's \nmade my tongue all rough.","open_wide_tongue","angry")
        call her_main("Do you want to stop?","grin","baseL")
        hide screen hermione_main
        m "No, keep going, just try not to focus on the tongue work too much."

    call her_main("Of course [genie_name].","annoyed","angryL")
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3

    call nar(">Hermione swallows your cock again, taking care\nnot to apply too much pressure with her tongue.") #start sucking scene. might insert more sucking noises for a little while or add pauses
    m "So you still went to all your classes?"
    $ g_c_u_pic = "hand_ani"
    with d3
    call her_main("Of course [genie_name].","base","glance")
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    m "Even looking like this?"                         ###start sucking
    if polyjuice_drunk:
        her "You had me do it before... at least I knew what to expect this time..."
        m "Slutty little Miss Granger... begging for attention..."
        m "making herself look like a cat for attention..."
        call nar(">You place your hands on her ears once again and give them a soft patting.","start")
        call nar(">Hermione starts purring as her pupils expands looking into yours.","end")
        m "There it is!"
        m "Keep going girl, this feels amazing..."
        call nar(">You momentarily stop patting her as you close your eyes with pleasure.")
        m "Don't stop!"
        $ g_c_u_pic = "hand_ani"
        with d3
        her "You stopped patting me!"
        m "Oh, sorry..."
        $ g_c_u_pic = "blowjob_ani"
        with d3
        hide screen hermione_main
        with d3
        call nar(">You gently stroke the back of Hermiones ears as she begins purring once again.")

    else:
        m "What would everyone have thought? Would they just assume that you were under an evil slytherin spell?"
        m "Or would they just think that slutty little Miss Granger was just begging for attention again."
        m "Wearing skimpy outfits and trying to look like a cat."
        call nar(">You go to place your hand on the back of her head but her new ears block the way.")
        m "These are quite soft."
        call nar(">You start feeling and patting the ears.","start")
        call nar(">Hermione starts involuntary purring","end")
        m "Oh good heavens!"
        m "It's like your whole mouth has become a vibrator."
        $ g_c_u_pic = "hand_ani"
        with d3
        call her_main("I can't help it [genie_name], whenever \nanything touches my ears I just purr.","base","happyCl")
        hide screen hermione_main
        m "It feels amazing, now cock back in the mouth girl."
        call her_main("Yes [genie_name].","smile","happyCl",emote="06")
        $ g_c_u_pic = "blowjob_ani"
        with d3
        hide screen hermione_main
        with d3
        call nar(">You immediately put your hands back on her ears and start stroking them as she sucks you.")### start sucking
        
    her "*Slurp!* *Purr* *Slurp!*"
    m "Oh god yes. This is Fantastic."
    her "*Purr* *Slurp!* *Purr*"
    m "Get ready girl... Here it comes."
    her "*Purr* *Purr* *Purr*"
    call nar(">You grab her ears and pull her head into you causing the tip of your cock to rest on her purring throat.") #show genie climax scene
    g4 "{size=+10}ARGH!!!!!!!!!!!!!!!!{/size}"
    her "*Purr* *Purr* *Purr*"
    call nar(">You shoot you load directly down her throat.") 
    call ctc

#This scene looks a bit weird
    $ g_c_u_pic = "cum_in_mouth_ani"
    with d3
    call her_main("","full_cum","dead")
    pause .1
    call her_main("*gulp* *Purr* *Purr*","cum","worriedCl")
    call her_main("","full_cum","dead")
    pause .1
    call her_main("*gulp* *Purr* *gulp*","cum","worriedCl")
    call her_main("","full_cum","dead")
    pause .1
    call her_main("*Purr* *gulp* *gulp*","cum","worriedCl")
    call nar(">You pull your cock out of her purring mouth.")
    call her_main("Mmmmm, it might be this potion but that tasted \ngood...","base","glance")
    hide screen hermione_main
    m "Well, you certainly earned your 75 points."
    $ gryffindor += 75
    $ g_c_u_pic = "hand_ani"
    with d3
    call her_main("Thank you [genie_name]. Will that be all.","base","ahegao_raised")
    m "One last thing."
    m "Who's a good girl?"
    call her_main("..........","annoyed","worriedL")
    call her_main("I am...","smile","baseL")

    call hide_characters
    call her_chibi("hide")
    call gen_chibi("sit_behind_desk")
    hide screen bld1
    hide screen blktone
    with fade

    $ cat_ears_potion_return = False #Triggers Hermione return
    $ hermione_wear_ears = False
    call update_her_uniform

    $ hermione_busy = True

    jump main_room

    #Tick that adds that she has drunk any sort of polyjuice potion so she will now recognize it.

#Luna transformation. #DONE

# label potion_scene_1_2: #Luna potion
    # m "Might I offer you a drink?"
    # call her_main("You're not trying to get me drunk on Butterbeer again are you?","normal","base",xpos="right",ypos="base")
    # m "Nothing of the sort, just a harmless little potion."
    # call nar(">You hand her the potion bottle.")
    # if is_first_potion:
        # first_potion = False
        # her "I can't believe you're making me drink random potions..."
    # else:    
        # call her_main("Another of your mysterious potions?","open","suspicious")
    # if polyjuice_drunk:
        # her "Yuck... another polyjuice potion..."
        # her "Do I really have to drink it again?"
        # m "If you'd like to continue our favour trading it would certainly be in your best interest [hermione_name]."
        # her "..."
        # her "Can you at least tell me what you've put in it?"
        # m "What's the fun in that? You're going to have to drink it and find out..."
        # if her_whoring <= #low
            # her "I'm not going to drink it again, especially since I have no idea who... or what it might turn me into."
            # #End Scene
        # if her whoring <= #high
            # her "Well, I might be a little bit curious..."
            # her "Okay then..."
    # else:    
        # her "Let me guess, you won't tell me what it does and I'll embarrass myself in front of the whole class?"
        # m "Not at all."
        # call her_main("That's new.","annoyed","suspicious")
        # her "... and somehow worrying"
        # her "So what exactly is it then?"
        # m "It's your regular, run-off-the-mill Polyjuice Potion."
        # call her_main("Ugh. Those taste like muck.","normal","worriedCl")
        # her "...and what will it turn me into?"
        # m "That, Miss Granger, is a secret."
        # call her_main("Typical.","normal","baseL",tears="soft")
        # m "It'll taste a lot sweeter if you imagine all the points you'll earn for Gryffindor."
        # m "How much of a lead did Slytherin have on you again?"
        # her "You're right, [genie_name]. I can't let Gryffindor down!"
    # hide screen hermione_main
    # with d3
    # pause.2

    # $ renpy.sound.play("sounds/gulp.mp3")
    # call her_chibi("drink_potion","mid","base")
    # pause 2

    # call nar(">She downs the thick potion.")
    # pause.5

    # call her_chibi("stand","mid","base")
    # pause.2

    # call her_main("Blehgh.","disgust","narrow")
    # if polyjuice_drunk:
        # her "Pinching my nose barely helps..."
        # her "So, do I leave or?"
        # m "No, just wait here for a moment..."    
        # m "Why don't you tell me a little bit about how your day's been going."
        # her "Okay..."
        # if her_whoring <= 13:
            # her "Well, there's not much to tell you that you don't already know."
            # her "Lately I've been questioning my previous outlook on life in general."
            # m "In what way exactly?"
            # her "Well, since we started our... mutually benefitial... what ever we call this..."
            # her "The general atmosphere in our commonroom has been in an all time high because of how many house points we're racking in."
            # m "That's good, you must feel a great sense of pride and acomplishment..."
            # her "Of course, the only issue is that I would never be able to tell them I'm the one to thank for it..."
            # her "If they just had one look of my face they'd be able to tell what was up."
            # m "Speaking of face..."
        # else:
            # her "Well, generally its been quite dull up until now."
            # her "I would be lying if I said I wasn't a little bit excited when you called on me."
            # m "Oh, you'll be getting your fair share of excitement soon enough... Well, not this version of you."
            # her "What version of me will be..."
    # else:    
        # her "I was wrong, not muck. Snot. It's as thick as Trollsnot."
        # m "As long as you keep it down, you'll earn Gryffindor a great deal of points."
        # her "And I will."
        # call her_main("So what now? I just go to class?","upset","wink")
        # m "Not yet, tell me something about yourself."
        # call her_main("Well, ever since I started my \"Extracurricular activities\" with you my attendance and grades have started slipping.","open","closed")
        # m "Troubling indeed."

        # if her_whoring <= 13:
            # call her_main("It is! [genie_name], I used to be at the top of the class. My scores were impeccable. ","scream","angryCl")
            # m "And how are your scores now?"
            # call her_main("Well I'm still at the top... Just not by as much.","annoyed","angryL")
            # m "Well, there are times when academic excellence shouldn't be your primary concern."
            # call her_main("Hmmph, and what /should/ be my primary concern then?","annoyed","suspicious")
            # m "Currently. I'd say your face is pretty high on the list"
            # call her_main("Excuse me. That is hardly appropriate for a headmaster.","open_tongue","glance")
            # m "No, I'm serious. You should really see the look on your face."
        # else:
            # call her_main("Not really. I realise there are other things I can excel in.","base","base")
            # m "Like sucking cocks for house-points"
            # call her_main("Professor!","scream","angryCl")
            # m "Oh don't be so modest. If sucking dick was a class, you'd be Magna Cum Laude."
            # call her_main("Thank you professor. You know, there's time to earn some more points before class. If you're feeling generous I could...","scream","angryCl")
            # m "I'd have to know on whose face I'll be cumming though "
            # call her_main("What do you mean? ...My face of course... I mean ...*urp*","scream","angryCl")

    # hide screen hermione_main
    # with hpunch
    # hide screen hermione_stand
    # call lun_chibi("stand","base","base")
    # pause.5

    # "*POOF*"

    # $ luna_xpos = 400 #400 = "right"
    # $ changeLuna("base","base","sad","mid")
    # show screen luna_main
    # with d3

    # if her_luna_polyjuice_drunk:
        # her "*urgh*... Every time..."
        # her "Did it work?"
        # m "Perfectly..."
        # call nar(">Hermione starts examining herself, feeling out her outfit and pausing at her breasts.")
        # $ changeLuna("base","seductive","raised","mid")
        # her "Well, At least I appear to be a girl.... A ravenclaw."
        # m "I'm surprised you expected something different."
        # call nar(">Hermione grabs a lock of her hair")
        # $ changeLuna("pout","base","base","crossed")
        # her "Hmm, a blonde... that narrows things down. Not a good sign..."
        # m "And why might that be?"
        # call nar(">Hermione reaches up into her fair and finds a thin wooden object lodge in the mess.")
        # $ changeLuna("base","wide","angry","mid")
        # her "..."
        # her "I'm...{w} You...{w} You turned me into Luna Lovegood again?"
        # m "Yeah!"
        # $ changeLuna("pout","wide","angry","mid")
        # her "What is your obsession with this crazy blonde girl?"
        # m "Now now, you're the one looking like her remember."
        # m "Unless you're reffering to yourself there's nothing wrong with the way she looks."
        # $ changeLuna("pout","base","sad","mid")
        # her "..."    
        # m "Now, I'd like to see those great assets of hers..."
        # if her_whoring <= #Lowish
            # her "This again? I already told you, I'm not going to flaunt another students... assets."
            # m "Then why would you drink the potion?"
            # her "You didn't tell me what it was going to do [genie_name]."
            # m "Oh, yeah..."
            # her "I'm not going bare my... her chest... for you."
            # m "Well you wont be recieveing any of those points..."
            # her "..."
            # her "Yeah, that's still going to be a no, bye [genie_name]."
            # #Hermione walks out Scene end
            # #Hermione mood gets worse
    # else:    
        # her "Ughhh... I feel like I'm going to throw up! Did the Polyjuice work??"
        # m "Like a charm."
        # call nar(">Hermione starts examining herself, feeling out her outfit and pausing at her breasts.")
        # $ changeLuna("base","seductive","raised","mid")
        # her "Apparently I'm still a girl. Someone from Ravenclaw?"
        # m "Keen powers of observation, Miss Granger"
        # call nar(">Hermione grabs a lock of her hair")
        # $ changeLuna("pout","base","base","crossed")
        # her "Definitely a blonde, though she could absolutely use a comb"
        # $ changeLuna("base","base","base","crossed")
        # call nar(">Suddenly Hermione feels something stuck in the mess of blonde. On closer examination it appears to be a wand.")
        # $ changeLuna("base","wide","angry","mid")
        # her "..."
        # her "You turned me into Loony Lovegood... I mean Luna Lovegood!?!"
        # m "Very astute, [hermione_name]."
        # if not luna_known:
            # m "(No idea who that is, but she looks good.)"
        # $ changeLuna("pout","wide","angry","mid")
        # her "Why on earth would you want me to look like Luna? She's completely mental!"
        # m "I'm not seeing anything wrong with her."
        # $ changeLuna("pout","base","sad","mid")
        # her "She has... imaginary friends and believes in things that can't possibly exist [genie_name]. She is absolutely mad."
        # m "Fortunately, I'm not really interested in her mental health. I am interested in her impressive, and quite real, chest."
        # if her_whoring <= #Lowish
            # her "I can't belive what you're suggesting, you're asking me to show off another students breasts?"
            # m "Well, what else would you have me do? Look at your face?"
            # her "That's crossing the line [genie_name], I might not think very highly of Loony... Luna..."
            # her "But I'm not going bare my... her chest... for you."
            # m "Then you wont be recieveing any of those points..."
            # her "..."
            # her "Yeah, that's still going to be a no, bye [genie_name]."
            # #Hermione walks out Scene end
            # #Hermione mood gets worse
        # else:    
            # $ changeLuna("base","seductive","raised","mid")
            # her "You can't possibly be interested in that... that girl's paltry breasts."
            # m "Currently they're yours. And they don't look so paltry from where I'm sitting [hermione_name]. Do I detect a hint of jealousy?"
            # $ changeLuna("base","base","angry","mid")
            # her "Not at all, I suppose it is only natural that someone of your advanced age has trouble with their eyesight."
            # m "(definitely struck a nerve there.) Is that any way to talk to your elders, [hermione_name]? Perhaps you need a good spanking to remind you of your manners. We old people are good at giving those."
            # $ changeLuna("disgust","base","sad","mid")
            # her "I..I apologize, [genie_name]. I don't know what came over me."
            # m "Apology accepted. I'm sure they can't hold a candle to the brilliance of your boobs."
            # $ changeLuna("pout","base","base","R")
            # her "I'd like to think I'm more than just a pair of breasts... but thank you [genie_name]. That was flattering. In a way."
            # m "If you want to dispel all doubt, we could compare. Why don't you lift your shirt and show me what you... err... She's got under that sweater."
            # $ changeLuna("pout","wide","angry","R")
            # her "I'm still not entirely comfortable with this..."
    # call nar(">Hermione quickly strips off her Ravenclaw top, followed by her bra.")
    # hide screen luna_main
    # with d3

    # $ luna_wear_top = False
    # $ luna_wear_bra = False
    # call update_luna_chibi_uniform
    # call lun_chibi("stand","base","base")
    # pause.5

    # $ changeLuna("base","seductive","raised","R")
    # show screen luna_main
    # with d3

    # if her_luna_polyjuice_drunk:
        # her "I assume you'd like a closer look like last time?"
        # m "Of course, get those cute pink nipples up here."
    # else:
        # her "There, see. Perfectly ordinary breasts. Absolutely no need to keep looking at them."
        # m "I'm not quite convinced, the soft pale skin, the cute pink nipples and they look like quite a handful. I think you might have some serious competition here [hermione_name]."
        # $ changeLuna("upset","seductive","angry","mid")
        # her "You can't be serious! They're saggy and couldn't even fill a first-year's palm!"
        # m "Hmmm, I'm not sure. I think a closer examination is required."
    # hide screen luna_main
    # with d3

    # #call lun_walk("mid","desk",1.7) #Needs walking chibi that is topless.
    # call lun_chibi("stand","desk","base") #Temporary!

    # call nar(">In a huff, Hermione walks over and presents her new set of breasts")
    # show screen luna_main
    # with d3

    # if her_luna_polyjuice_drunk:
        # m "You look a bit flustered [hermione_name]."
        # $ changeLuna("pout","seductive","angry","mid")
        # her "You're staring directly at my chest [genie_name] and I can't help but feel a bit guilty as its not my own..."
        # m "Well, hopefully this should take your mind off that... 20 points to Gryffindor."
        # her "Thank you, [genie_name]...."
    # else:    
        # m "Yes yes, upon closer inspection it seems I was wrong. Luna's breasts are indeed second to your own."
        # $ changeLuna("pout","seductive","angry","mid")
        # her "I'm glad you came to your senses. Thank you, If you're completely satisfied, I'll cover these hideous things up now."
        # m "Completely, [hermione_name]. 20 points to Gryffindor."
    # hide screen luna_main
    # with d3

    # $ luna_wear_top = True
    # $ luna_wear_bra = True
    # call update_luna_chibi_uniform
    # call lun_chibi("stand","desk","base")
    # pause.5

    # $ changeLuna("base","closed","base","mid")
    # show screen luna_main
    # with d3

    # her "Well I best be off to classes."
    # m "You're going to class looking like a fellow classmate?"
    # $ changeLuna("base","base","raised","mid")
    # her "It's not going to be a problem. Luna's barely in class as it is, I can just pretend to be her. Maybe I'll even improve her test scores. You'll notify the teachers I can't attend class right?"
    # m "Absolutely. (Not a chance) But, what if you bump into her in the halls?"
    # $ changeLuna("pout","seductive","base","mid")
    # her "Believe me [genie_name], Luna will probably think I'm some kind of Wrackspurt that's messing with her head."
    # hide screen luna_main
    # with d3

    # call lun_walk("desk","leave",2.7)

    # $ hermione_busy = True

    # jump main_room

    # #Tick that adds that she has drunk any sort of polyjuice potion so she will now recognize it.
    # #Tick that she has drunk the luna polyjuice potion
    # #Tick that Genie now knows what Luna looks like

# #Lamia transformation.

# label potion_scene_1_3: #Lamia potion
    # call her_main("That's dumb.","scream","worriedCl")
    # m "I literally don't know."
    # jump main_room


# #Clone transformation.

# label potion_scene_1_4: #Clone potion
    # m "Do you ever feel conflicted about what we do in here [hermione_name]?"
    # her "Conflicted? I suppose I do... why do you ask?"
    # m "because I have a new potion that can help you come to terms with this internal conflict."
    # her "What? How?"
    # m "It splits your mind into two parts, allowing you to confront yourself and address the problem."
    # her "Splits my mind?! That doesn't sound very safe!"
    # m "It only splits your mind metaphorically. I ensure you it's as safe as can be."
    # her "Well if you made it yourself then I trust it. I mean it's not like the weasley twins made it."
    # m "Of course not... Now if you'd kindly drink it we can get to the bottom of your conflicted nature."
    # her "..."
    # her "Well here goes..."
    # call nar(">Hermione drinks the potion.")
    # her "Mmmmmm it's so sweet..."
    # her "Ughhhh, it's so sour..."

    # #Hermione split into two versions of herself, one slutty, one prudish
    # #Slutty one wants to have sex with Genie
    # #Genie obliges
    # #Slutty Hermione enjoying it immensely
    # #Genie trying to convince pruddy Hermione to join in
    # #Prude Hermione wants no part in it, although she is slightly aroused
    # #Slut Hermione
    # #Genie cums in Hermione
    # #Slut Hermione wants to go again
    # #Slut Hermione offers to suck Genie to get him hard
    # #Genie says why don't we get prude Hermione to do it
    # #Slut Hermione says that's a great idea
    # #Prude Hermione refuses
    # #Slut Hermione and Genie force her to her knees
    # #Genie talks dirty to Prude Hermione while Slutty Hermione encourages her
    # #Genie ends up covering her in cum
    # #Prude Hermione partially speechless
    # #Slutty Hermione wants to go again but Genie is spent
    # #Hermione reforms into one person
    # #Genie ridicules her, saying that even the most prudish and reseverved version of herself ended up sucking him off
    # #Hermione feels both shame and pride
    # #THE END


    # call her_walk(action="leave", speed=2)

    # $ hermione_busy = True

    # jump main_room
