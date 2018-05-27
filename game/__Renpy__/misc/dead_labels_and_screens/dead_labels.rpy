
#Was 16_inverntory.rpy
label inventory:
    menu:
        "-Books-":
            if "book_01" in books: 
                menu:
                    "-Read book # 1-" if book_01_units <= 19:
                        pass
                    "-Read book # 1 (Finished)-" if book_01_units == 20:
                        ">You already finished this one."
                        
            "You don't own a single book."
            jump inventory
        "-Gifts-":
            pass
        "-Never mind-":
            jump cupboard
#


#Was 37_clothing_events
### Gryffindor Stockings ###
label equip_gryyf_stockings:

    call her_main("",xpos=510) #510=default Hermione xpos
    $ wardrobe_active = 0 #activates dissolve in her_main 

    if wardrobe_events_active: #NOT IN USE
        pass
    else:
        if whoring < 3:
            call her_main("Is that!?","open","worried")
            call her_main("A pair of Gryffindor stockings!?","shock","wide")
            m "Yep?"
            call her_main("They're sold out from the uniform shop on the very first day, of EVERY SINGLE YEAR!","shock","wide")
            m "Probably?"
            call her_main("I NEED THEM! What'll it cost me!?","angry","worriedCl",emote="05")
            m "No cost"
            call her_main("!","shock","wide")
            m "It's a gift, [hermione_name], to show you what a great guy ME, Proffesor DeltaDwarf, really is!"
            call her_main("...")
            call her_main("hhmppphhh", "body_42")
            call her_main("hahahahahahaha!","smile","happyCl",cheeks="blush",emote="06")
            call her_main("ahhh....","base","concerned",cheeks="blush",tears="soft")
            call her_main("You're too funny! Thanks for the gift! I'll put them on right away","base","base")
            g6 "(...What did I say?)"
            call her_main("I've always wanted a pair of these! They're warm, and they reduce unwanted attention from the boys","base","base")
            call her_main("I will be the next best thing to having a skirt that's twice as long!","smile","baseL")
            m "Just glad to help, [hermione_name]!"
            g4 "(hehehe... hope you remember those words after I've made you so needy and desperate you'll suck off a hundred boys just to get off once)"
            call her_main("They feel great!","base","base")
            call her_main("",xpos=120) #Hermione xpos middle
            call blk_tone
            call set_h_stockings("gryff_stockings")
            call ctc_wPause
            call hide_blk_tone
            call her_main("Thanks again, [genie_name]! You're too kind","base","base",xpos=510) #Hermione default xpos
            g9 "(We'll see)"
            $ request_gryyf_stockings = True
    
        elif whoring >= 3 and whoring <= 6:
    
            $ hermione_wear_skirt = True
            $ hermione_wear_top = True
       
            call her_main("Is that...","open","worried")
            $ hermione_emote_exclam = True
            call her_main("A pair of Gryffindor stockings!?","shock","wide")
            m "Yep?"
            call her_main("They're sold out from the uniform shop on the very first day, of EVERY SINGLE YEAR!","shock","wide")
            m "K?"
            call her_main("....")
            $ hermione_emote_exclam = False
            $ hermione_emote_hearts = True
            call her_main("I NEED THEM!", "body_34")
            call her_main("What'll it cost me!?", "body_34")
            call her_main("WHAT DO I HAVE TO DO!?","scream","worriedCl")
            $ hermione_emote_hearts = False
            m "Just a small favour"
            call her_main("(!)","shock","wide")
            m "All I want, [hermione_name], is to see how great they look on you."
            m "Easy, right?"
            call her_main("...")
            call her_main("You just want to see me in stockings? That should be no problem...", "body_14")
            call her_main("(Is he up to something?)","normal","frown")
            call her_main(".....")
            call her_main("","base","base",xpos=120) #Hermione xpos middle
            call blk_tone
            call set_h_stockings("gryff_stockings")
            call ctc_wPause
            call hide_blk_tone
            call her_main("What do you think, [genie_name]?",xpos=510) #510=default Hermione xpos
            m "Impressive..."
            m "They look great, [hermione_name]!"
            call her_main("[genie_name]! My appearance has no bearing on my academic ability.","scream","closed",cheeks="blush") #Embarrassed mouth wide eyes closed angry
            call her_main("......","open","annoyed",cheeks="blush")
            call her_main("(That does make me feel kinda nice, though...)","open","annoyed",cheeks="blush") #Embarrassed mouth open angry
            g9 "But, I'm having a hard time seeing all the details with that skirt in the way"
            call her_main("(Oh no...)","angry","worried") #Worried, teeth showing
            call her_main("(I knew it! That pervert!)","angry","angry") #Angry, teeth showing
            call her_main("(sigh...)","angry","angry")
            call her_main("(alright, [hermione_name], we've done this before, it's as easy as Arithmancy)","angry","angry")
            call her_main("(there's nothing embarrassing about this!)","clench","worried",cheeks="blush",tears="soft") #Worried, embarrassing, small tears
            call her_main("I'm just showing that bastard a little square of fabric", "body_186")
            call her_main("That's all!")
            call her_main("And think of how much more I'll get done without boys staring at my legs all day...","angry","suspicious",cheeks="blush") #Worried, angry, embarrassed
            m "I'm waiting, [hermione_name]. Don't tell me you don't want your gift?"
            call her_main("No, [genie_name], I want it.")
            g9 "Then earn it, [hermione_name]"
            call her_main("....","upset","worriedCl",cheeks="blush") #embarrassed, eyes closed, mouth closed
            call her_main("",xpos=120) #Hermione xpos middle
            call blk_tone
            call set_hermione_action("lift_skirt")
            $ skirt_up = True
            show screen hermione_03 #Hermione lifts her skirt
            with d3
            call her_main("","angry","suspicious",cheeks="blush",xpos=120) #Hermione xpos middle
            call ctc_wPause
            call hide_blk_tone
            $ skirt_up = False
            show screen hermione_blink #Hermione stands still.
            with fade
            call her_main("",xpos=510) #510=default Hermione xpos
            m "They suit you, [hermione_name]"
            call her_main("Again with the sweet talk?")
            call her_main("(it won't work on someone like me...)", "body_182")
            m "Your panties, your stockings... they make you look so pretty"
            call her_main("(ahh! he called me pretty)", "body_188")
            call her_main("You saw what you wanted... now I can go, right [genie_name]?","angry","suspicious",cheeks="blush")
            #call her_main("Please?","angry","suspicious",cheeks="blush")
            m "(True, I did get a great panty shot)"
            g9 "(But I could try to get more out of her...)"
            m "What should I do?"
            menu:
                "What a cutie! Let her go":
                    m "Of course, [hermione_name]. Enjoy your stockings"
                    $ hermione_emote_hearts = True
                    call set_hermione_action("")
                    call update_her_uniform
                    call her_main("Thanks, [genie_name]! I'll wear them whenever you want.","grin","wink",cheeks="blush")
                    call her_main("(phew. why does it feel like a dodged a bullet, though?)","grin","wink",cheeks="blush")
                    $ hermione_emote_hearts = False
                    $mad = 0
            
                "Cute is boring. Break her.":
                    m "That was certainly adequate, [hermione_name]..."
                    call her_main("(Adequate...?)","annoyed","annoyed",xpos=120)
                    m "But..."
                    call her_main("oh no...","shock","wide",xpos=120)
                    m "You're one of our top students..."
                    m "And there were still areas I couldn't see..."
                    m "You're not giving it 100\%, here!"
                    call her_main("(No way...)","shock","wide",xpos=120)
                    g4 "You're going to remove your skirt"
                    g4 "Then you're going to remove your panties."
                    g9 "And then I'm going to get a proper look. Just as we agreed."
                    call set_hermione_action("")
                    $ hermione_emote_anger = True
                    call her_main("NO", "body_218")
                    g4 "(?)"
                    call her_main("NO WAY!")
                    call her_main("THERE IS ABSOLUTELY NO WAY AM I GOING TO DO THAT!!!")
                    call her_main("I'm not some cheap slytherin slut that you can just play with!","scream","angry",cheeks="blush",tears="messy")
                    g4 "..."
                    m "Would you like to have your gift taken back from you?"
                    $ hermione_emote_anger = False
                    $ hermione_emote_exclam = True
                    call her_main("....","clench","worried",cheeks="blush",tears="soft")
                    m "Forfeit your points?"
                    $ hermione_emote_exclam = False
                    call her_main("...........","clench","worried",cheeks="blush",tears="soft")
                    m "How about I remove some points for disobeying the head master?"
                    call her_main("...............","shock","wide",xpos=145)
                    m "And end our tutoring arrangement all together..."
                    m "I wonder what will happen to your report card?"
                    m "I wonder what your parents will think..."
                    g9 "When they realize they've raised a failure"
                    call her_main("Stop it...","shock","down_raised",cheeks="blush",tears="crying")
                    g9 "(Hmm?)"
                    call her_main("I get it already...","shock","down_raised",cheeks="blush",tears="crying",xpos=120)
                    call her_main(".......","shock","down_raised",cheeks="blush",tears="crying")
                    $mad += 55
                    ">With tears rolling down her soft cheeks, Hermione begins to unzip her skirt"
                    ">Her trembling hands make it difficult just to keep hold of the zipper"
                    ">Eventually she gets it, and after hooking her thumb over her panties, she lowers the rest of her dignity to the floor"    
                    $ hermione_wear_skirt = False
                    #$ h_request_wear_panties = False
                    call update_her_uniform
                    call blk_tone
                    call ctc_wPause
                    $ hermione_wear_panties = False
                    call update_her_uniform
                    call her_main("","scream","worriedCl",cheeks="blush",tears="messy")
                    call ctc_wPause
                    m "Hands behind your back, [hermione_name]. I want to see everything."
                    call her_main(".....","angry","suspicious",cheeks="blush",tears="messy")
                    call set_hermione_action("hands_behind")
                    call set_hermione_action("")
                    call ctc_wPause
                    ">Too weak to fight back, Hermione does as she's told"
                    call hide_blk_tone
                    call her_main("","angry","suspicious",cheeks="blush",tears="messy",xpos=510) #510=default Hermione xpos
                    m "Good girl."
                    g9 "(What a spectacular body...)"
                    call her_main(".......","angry","suspicious",cheeks="blush",tears="messy")
                    call her_main("(After all he's done to me... why do i feel...)","angry","suspicious",cheeks="blush",tears="messy")
                    call her_main("(like i'm still on fire...)","angry","suspicious",cheeks="blush",tears="messy")
                    call her_main("this doesn't make any sense","angry","suspicious",cheeks="blush",tears="messy")
                    call her_main("Ahh... hehehehehehehe","angry","dead",cheeks="blush",tears="crying")
                    m "(...has she lost it already?)"
                    call her_main("(whatever... it doesn't need to make sense)")
                    call her_main("(You're headed straight to Azkaban once this is over, anyway)","angry","dead",cheeks="blush",tears="crying")
                    call her_main("(so at least for now, keep looking at my body!)","angry","dead",cheeks="blush",tears="crying")
                    call her_main("(my whole body needs to melt)","angry","dead",cheeks="blush",tears="crying")
                    g9 "(hehehehe, i hope [hermione_name] can feel it)"
                    g9 "(how a bitch feels when she's in heat)"
                    ">Slowly but surely, you see a trickle of nectar begin to leak out of Hermione."
                    $ hermione_dribble = True
                    call h_update_body
                    call her_main("","grin","dead",cheeks="blush",tears="messy")
                    call blk_tone
                    call ctc_wPause
                    call her_main("(This is....)")
                    call her_main("(too good)")
                    g9 "(heh. Once I'm done with you, you'll be dripping like this every day)"
                    call her_main("(more....)")
                    call her_main("(I want to be tutored more by him!)")
                    call hide_blk_tone
                    m "..."
                    g9 "....."
                    call her_main (".....")
                    m "We're done here, [hermione_name]"
                    call her_main(".....","grin","dead",cheeks="blush",tears="messy")
                    m "You can keep the stockings."
                    call her_main(".......","grin","dead",cheeks="blush",tears="messy")
                    m "And 50 points to Gryffindor for your outstanding performance."
                    $ gryffindor += 50
                    call her_main("..........","grin","dead",cheeks="blush",tears="messy")
                    g4 "What do you say when you've been given a gift?"
                    call her_main("..........","grin","dead",cheeks="blush",tears="messy")
                    call her_main("Thank you, [genie_name]","grin","dead",cheeks="blush",tears="messy")
                    g9 "That's right, [hermione_name]."
                    m "Don't forget your clothes on the way out."
                    call blk_tone
                    call her_main("(my... p..)","grin","dead",cheeks="blush",tears="messy")
                    call her_main("(..pussy is throbbing)","grin","dead",cheeks="blush",tears="messy")
                    call her_main("(i might become an addict if i'm not careful)","grin","dead",cheeks="blush",tears="messy")
                    ">Hermione retrieves her clothes and starts putting them back on"
                    call her_main("(just the panties touching...)","angry","dead",cheeks="blush",tears="crying")
                    call her_main("(feels incredible!)","angry","dead",cheeks="blush",tears="crying")
                    "You can't help but notice stains on the pure white fabric that's hugging her leaking cunt "
                    call set_hermione_action("hands_free")
                    call set_hermione_action("")
                    $ hermione_wetpanties = True
                    $ hermione_wear_panties = True
                    call hide_blk_tone
                    call her_main("","angry","dead",cheeks="blush",tears="crying")
                    call ctc_wPause
                    call her_main("(ahh, i've made them all sloppy)","angry","dead",cheeks="blush",tears="crying",xpos=510) #510=default Hermione xpos
                    g9 "We're going to have a lot of fun in future, [hermione_name]"
                    call her_main("","angry","dead",cheeks="blush",tears="crying")
                    $ hermione_wear_skirt = True
                    $ hermione_dribble = False
                    call update_her_uniform
                    with d3
                    call her_main("","grin","dead",cheeks="blush",tears="messy")
                    ">'Leaking' overlay now equip-able!"
                    ">'Wet panties' overlay now equip-able!"
                    $ hermione_wetpanties = True
                    $ dribble_equippable = True
                    $ wetpanties_equippable = True
       
            hide screen blktone
            hide screen bld1
            hide screen hermione_main
            hide screen hermione_stand_f #Hermione stands still.
            with d3
            call her_walk(400,610,2)
            $ request_gryyf_stockings = True
            ">Gryffindor stockings now equip-able!"
            #call reset_hermione_main
       
            jump end_hg_pf
    
        jump day_request_clothing

    #else: #NOT IN USE
    #    if whoring < 3:
    #        ">Hermione can now wear gryffindor stockings!"
    #        call set_h_stockings("gryff_stockings")
    #        $ request_gryyf_stockings = True
    #        jump wardrobe
    #    if whoring  >= 3 and whoring <= 6:
    #        ">Hermione can now wear gryffindor stockings!"
    #        ">Hermione's panties have gotten mysteriously wet!"
    #        call set_h_stockings("gryff_stockings")
    #        $ request_gryyf_stockings = True

    #        $ hermione_wetpanties = True
    #        $ dribble_equippable = True
    #        $ wetpanties_equippable = True
    #        jump wardrobe
#

#From 21_chitchats
### CHITCHAT EVENTS ###
label chitchat_event_01: #Snape says: so you tutor her now?". Happens after tutoring unlocks.
    hide screen snape_main
    with d3
##############################################################################
#########   JJ Edits   12/29/2014  ###########################################
#    sna_[1] "So..."
#    sna_[1] "I hear miss Granger is taking private lessons from you now?"
#    m "Yeah, I suppose she does..."
#    m "Not sure where this fits into our plan though."
#    sna_[9] "What do you mean? It fits perfectly."
#    sna_[9] "I myself and a couple of other teacher are failing the crap out of that girl!"
#    sna_[9] "As a result she spends more time with studying..."
#    sna_[9] "Even taking private lessons now..."
#    sna_[18] "This way she has very little time left to be noisy and cause me headaches."
#    m "I see..."
#    sna_[10] "Yes, yes... just, you so know..."
#    sna_[10] "Don't actually teach her anything useful, alright?"
#    m "I'll do my best."
#    sna_[1] "Well, if there is that's all..."
###  Altered this chit chat to reflect JJ's tutoring results  
    sna_[1]  "The Granger girl is driving me mad with her accusations.  They must stop!  I think she was even coming on to me!"  
    sna_[7] "As though I would fall for such a transparent ploy! Though she does look to have a luscious body under that frumpy sweater..."
    sna_[4] "Have you done anything to deal with her?  If you have not..."
    sna_[9] "I found a lovely potion in my cupboard that will put her into a long, wasting slumber for which there is no antidote."
    m  "Don’t worry, Severus.  I have her well in hand."  
    sna_[10]  "Oh, really?  How?"  
    m "Well, for starters she is seeing me for magic lessons.  I am teaching her how to do magic without wands or incantations."
    sna_[17] "But that’s nearly impossible for someone of her age!  All but the most powerful wizards and witches must use wands."  
    sna_[2] "And at her ability level she will need to verbalize all but the simplest spells."
    m  "Not to worry.  I plan to teach her how I do magic and I don’t need to do any of that."
    sna_[6] "That's ridiculous!  Your magic only works for you!"
    m "Exactly!"
    sna_[18] "Oh, you are devious!  But you said for starters..."
    m "Are you familiar with a Professor Trelawney?"
    sna_[15] "Sybil Trelawney?  That idiot?!?  Her so-called classes are a blot upon the school’s reputation!"
    sna_[7] "She’s a laughing-stock among all of the other schools in Europe!"
    m "I see. It seems I’ve instructed Miss Granger to re-enroll in Trelawney’s Divination class during her usual study time."
    m "As it turns out, Miss Granger over the years has transferred her magical aura into her wand."
    m  "She is in desperate need of instruction on how to read magical auras."
    sna_[7] "What rubbish is this?  Magical auras?  Transferring to a wand?  There's no such thing!"
    m "Ah, well, we must not disabuse Miss Granger of that notion, shall we?"
    m "She has lost the confidence that she can do much magic at all without her wand now."
    sna_[8] "That's...despicable.  I wish I had thought of that."
    m  "I’ve also asked that Trelawney person to have Miss Granger make up all the work she may have missed before and provide after-class tutoring."
    m  "I think it amounts to a couple of years of class work and of course less time to study in her other classes..."
    sna_[8] "......................"
    sna_[18] "That’s...that’s more brutal than I think I would have been.  And I hate the Granger bitch!"
    m  "Miss Granger is convinced that her troubles are because she has lost her innate magic aura.  I pointed out that the solution is simple.  "
    m  "To retrieve it she must masturbate with her wand several times per day.  This is where you can help."
    m  "You might want to let her know if you notice her aura is dwindling so she'll increase her efforts to regain it."
    sna_[18]  "..........................."
    sna_[15]  "Ah ha ha ha!  I am so very, very glad you are my ally and not my enemy."
    m "That’s kind of you to say Severus."  
    sna_[18]  "I think I'll return to my office and think about how best to leverage this new information before my next class begins."
    m "Good day, Severus."
# End alteration  JJ
    
    

    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snape_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_walk_01_f 
    with d3

    $ chitchat_event_01_happened = True #Activates next event - Event_15 Hermione sells her first favour.
    $ snape_busy = True
    $ days_without_an_event = 0
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    
    jump day_main_menu
#







