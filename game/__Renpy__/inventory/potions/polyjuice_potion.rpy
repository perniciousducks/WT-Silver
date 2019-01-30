

### POLYJUICE POTION ###

#Cat ears.

label potion_scene_1_1_1: #catears (keep in mind Genie is trying to transform her into another girl)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?","base","base")
    m "Today I have a new type of favour for you to perform."
    call her_main("What do you mean new? What do I have to do?","normal","frown")
    m "It's quite simple, today you will be drinking a potion"
    call her_main("Is that it? How much will I get paid?","open","suspicious")
    m "20 points."
    call her_main("Hmmm, what type of potion is it?","annoyed","suspicious")
    call her_main("Polyjuice? Amortentia? Babbling Beverage? Felix Felicis?","grin","worriedCl",emote="05")
    m "That's a secret [hermione_name]."
    call her_main("...","annoyed","down")
    m "Well [hermione_name], what do you say? Will you drink a harmless little potion?"
    m "For Gyrffindor?"
    call her_main("Fine...","open","closed")
    call nar(">Hermione takes a whiff of the thick potion.")
    call her_main("This smells disgusting. Like mud and wet dog fur.","disgust","narrow")
    call her_main("Do I really have to drink this?","open","worried")
    m "You do. I suggest holding your nose if the smell is too much."
    call her_main("For Gryffindor.","mad","worriedCl",tears="soft_blink")

    call her_chibi("drink_potion","mid","base")

    call nar(">Hermione holds her nose and quickly downs the flask.")
    call her_main("","full","ahegao_intense")
    pause
    call her_main("","angry","base",tears="soft")

    call her_chibi("stand","mid","base")

    her "Ughhh. That was horrible."
    m "Well done."
    call her_main("Now will you at least tell me what this potion does.","angry","base",tears="soft")
    m "It should be noticeable any second now..."
    call her_main("Well? Is it supposed to make my breasts bigger? They don't feel any bigger.","annoyed","down")
    m "No. Hmmmm, it mustn't have worked."
    call her_main("What was it supposed to do?","annoyed","ahegao")
    m "There's no point in telling you now. It was going to be a surprise."
    m "Damn Twins must've conned me."
    call her_main("Is that all [genie_name]?","soft","base")
    m "Yes, [hermione_name], 20 points to Gryffindor."
    call her_main("Thank you [genie_name].","base","base")
    call nar(">Hermione heads off to class.")
    $ gryffindor += 20

    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    hide screen ctc
    with Dissolve(.3)

    call her_walk("mid","leave",2)

    $ cat_ears_potion_return = True #Triggers Hermione return

    #Equip Cat-Ears
    $ h_ears = "cat_ears"
    $ h_request_wear_ears = True
    $ hermione_wear_ears = True
    call update_her_uniform

    $ hermione_busy = True
    jump main_room

label potion_scene_1_1_2: #Scene where Hermione comes back after classes angry and confused at being given cat ears and a tail.
    call play_sound("door") #Sound of a door opening.
    call her_chibi("stand","mid","base")

    show screen bld1
    call her_main("How could you do this to me [genie_name]?","angry","angry")
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
            hide screen bld1
            hide screen hermione_main
            hide screen blktone
            hide screen ctc
            with d3

            call her_walk("mid","leave",2)

            $ cat_ears_potion_return = False #Triggers Hermione return
            $ h_request_wear_ears = False
            $ hermione_wear_ears = False
            call update_her_uniform

            $ hermione_busy = True
            jump main_room

        "-Make her suck you off-" if her_whoring >= 17:
            pass

    m "Wait [hermione_name], how would you like to earn 75 additional points?"
    call her_main("75 points? How?","annoyed","suspicious")
    m "By sucking my cock."
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

    $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_left
    show screen g_c_u

    call her_chibi("hide")
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    with fade
    call ctc

    call bld
    m "Good god what is with your tongue?! It feels like velcro."
    her "*Slurp?*"
    $ g_c_u_pic = "hand_ani"
    with d3
    $ hermione_zorder = 8
    call her_main("It's because of your stupid potion, it's \nmade my tongue all rough.","open_wide_tongue","angry")
    call her_main("Do you want to stop?","grin","baseL")
    hide screen hermione_main
    m "No, keep going, just try not to focus on the tongue work too much."
    call her_main("Yes [genie_name].","annoyed","angryL")
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
    m "You immediately put your hands back on her ears and start stroking them as she sucks you."### start sucking
    her "*Slurp!* *Purr* *Slurp!*"
    m "Oh gods yes. This is Fantastic."
    her "*Purr* *Slurp!* *Purr*"
    m "Get ready girl... Here it comes."
    her "*Purr* *Purr* *Purr*"
    call nar(">You grab her ears and pull her head into you causing the tip of your cock to rest on her purring throat.") #show genie climax scene
    g4 "{size=+10}ARGH!!!!!!!!!!!!!!!!{/size}"
    her "*Purr* *Purr* *Purr*"
    call nar(">You shoot you load directly down her throat.") #have picture 125 and 126 play each time she swallows
    call ctc

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
    hide screen hermione_main
    m "One last thing."
    m "Who's a good girl?"
    call her_main("..........","annoyed","worriedL")
    call her_main("I am...","smile","baseL")

    $ hermione_zorder = 5
    hide screen hermione_main
    hide screen chair_left
    call her_chibi("hide")
    call gen_chibi("hide")
    show screen genie
    hide screen bld1
    hide screen blktone
    with fade

    $ cat_ears_potion_return = False #Triggers Hermione return
    $ hermione_wear_ears = False
    call update_her_uniform

    $ hermione_busy = True
    jump main_room


#Luna transformation. #DONE

label potion_scene_1_2: #Luna potion
    m "Might I offer you a drink?"
    call her_main("You're not trying to get me drunk on Butterbeer again are you?","normal","base",xpos="right",ypos="base")
    m "Nothing of the sort, just a harmless little potion."
    call nar(">You hand her the potion bottle.")
    call her_main("Another of your mysterious potions?","open","suspicious")
    her "Let me guess, you won't tell me what it does and I'll embarrass myself in front of the whole class?"
    m "Not at all."
    call her_main("That's new.","annoyed","suspicious")
    her "... and somehow worrying"
    her "So what exactly is it then?"
    m "It's your regular, run-off-the-mill Polyjuice Potion."
    call her_main("Ugh. Those taste like muck.","normal","worriedCl")
    her "...and what will it turn me into?"
    m "That, Miss Granger, is a secret."
    call her_main("Typical.","normal","baseL",tears="soft")
    m "It'll taste a lot sweeter if you imagine all the points you'll earn for Gryffindor."
    m "How much of a lead did Slytherin have on you again?"
    her "You're right, [genie_name]. I can't let Gryffindor down!"
    hide screen hermione_main
    with d3
    pause.2

    call her_chibi("drink_potion","mid","base")
    pause 2

    call nar(">She downs the thick potion.")
    pause.5

    call her_chibi("stand","mid","base")
    pause.2

    call her_main("Blehgh.","disgust","narrow")
    her "I was wrong, not muck. Snot. It's as thick as Trollsnot."
    m "As long as you keep it down, you'll earn Gryffindor a great deal of points."
    her "And I will."
    call her_main("So what now? I just go to class?","upset","wink")
    m "Not yet, tell me something about yourself."
    call her_main("Well, ever since I started my \"Extracurricular activities\" with you my attendance and grades have started slipping.","open","closed")
    m "Troubling indeed."

    if her_whoring <= 13:
        call her_main("It is! [genie_name], I used to be at the top of the class. My scores were impeccable. ","scream","angryCl")
        m "And how are your scores now?"
        call her_main("Well I'm still at the top... Just not by as much.","annoyed","angryL")
        m "Well, there are times when academic excellence shouldn't be your primary concern."
        call her_main("Hmmph, and what /should/ be my primary concern then?","annoyed","suspicious")
        m "Currently. I'd say your face is pretty high on the list"
        call her_main("Excuse me. That is hardly appropriate for a headmaster.","open_tongue","glance")
        m "No, I'm serious. You should really see the look on your face."

    else:
        call her_main("Not really. I realise there are other things I can excel in.","base","base")
        m "Like sucking cocks for house-points"
        call her_main("Professor!","scream","angryCl")
        m "Oh don't be so modest. If sucking dick was a class, you'd be Magna Cum Laude."
        call her_main("Thank you professor. You know, there's time to earn some more points before class. If you're feeling generous I could...","scream","angryCl")
        m "I'd have to know on whose face I'll be cumming though "
        call her_main("What do you mean? ...My face of course... I mean ...*urp*","scream","angryCl")
        m "Maybe you should check the mirror"

    hide screen hermione_main
    with hpunch
    hide screen hermione_blink
    call lun_chibi("stand","base","base")
    pause.5

    "*POOF*"

    $ luna_xpos = 400 #400 = "right"
    $ changeLuna("base","base","sad","mid")
    show screen luna_main
    with d3

    her "Ughhh... I feel like I'm going to throw up! Did the Polyjuice work??"
    m "Like a charm."
    call nar(">Hermione starts examining herself, feeling out her outfit and pausing at her breasts.")
    $ changeLuna("base","seductive","raised","mid")
    her "Apparently I'm still a girl. Someone from Ravenclaw?"
    m "Keen powers of observation, Miss Granger"
    call nar(">Hermione grabs a lock of her hair")
    $ changeLuna("pout","base","base","crossed")
    her "Definitely a blonde, though she could absolutely use a comb"
    $ changeLuna("base","base","base","crossed")
    call nar(">Suddenly Hermione feels something stuck in the mess of blonde. On closer examination it appears to be a wand.")
    $ changeLuna("base","wide","angry","mid")
    her "..."
    her "You turned me into Loony Lovegood... I mean Luna Lovegood!?!"
    m "Very astute, [hermione_name]."
    if not luna_known:
        m "(No idea who that is, but she looks good.)"
    $ changeLuna("pout","wide","angry","mid")
    her "Why on earth would you want me to look like Luna? She's completely mental!"
    m "I'm not seeing anything really wrong with her."
    $ changeLuna("pout","base","sad","mid")
    her "She has... imaginary friends and believes in things that can't possibly exist [genie_name]. She is absolutely mad."
    m "Fortunately, I'm not really interested in her mental health. I am interested in her impressive, and quite real, chest."
    $ changeLuna("base","seductive","raised","mid")
    her "You can't possibly be interested in that... that girl's paltry breasts."
    m "Currently they're yours. And they don't look so paltry from where I'm sitting [hermione_name]. Do I detect a hint of jealousy?"
    $ changeLuna("base","base","angry","mid")
    her "Not at all, I suppose it is only natural that someone of your advanced age has trouble with their eyesight."
    m "(definitely struck a nerve there.) Is that any way to talk to your elders, [hermione_name]? Perhaps you need a good spanking to remind you of your manners. We old people are good at giving those."
    $ changeLuna("disgust","base","sad","mid")
    her "I..I apologize, [genie_name]. I don't know what came over me."
    m "Apology accepted. I'm sure they can't hold a candle to the brilliance of your boobs."
    $ changeLuna("pout","base","base","R")
    her "I'd like to think I'm more than just a pair of breasts... but thank you [genie_name]. That was flattering. In a way."
    m "If you want to dispel all doubt, we could compare. Why don't you lift your shirt and show me what you... err... She's got under that sweater."
    $ changeLuna("pout","wide","angry","R")
    her "I'm still not entirely comfortable with this..."
    call nar(">Hermione quickly strips off her Ravenclaw top, followed by her bra.")
    hide screen luna_main
    with d3

    $ luna_wear_top = False
    $ luna_wear_bra = False
    call update_luna_chibi_uniform
    call lun_chibi("stand","base","base")
    pause.5

    $ changeLuna("base","seductive","raised","R")
    show screen luna_main
    with d3

    her "There, see. Perfectly ordinary breasts. Absolutely no need to keep looking at them."
    m "I'm not quite convinced, the soft pale skin, the cute pink nipples and they look like quite a handful. I think you might have some serious competition here [hermione_name]."
    $ changeLuna("upset","seductive","angry","mid")
    her "You can't be serious! They're saggy and couldn't even fill a first-year's palm!"
    m "Hmmm, I'm not sure. I think a closer examination is required."
    hide screen luna_main
    with d3

    #call lun_walk("mid","desk",1.7) #Needs walking chibi that is topless.
    call lun_chibi("stand","desk","base") #Temporary!

    call nar(">In a huff, Hermione walks over and presents her new set of breasts")
    show screen luna_main
    with d3

    m "Yes yes, upon closer inspection it seems I was wrong. Luna's breasts are indeed second to your own."
    $ changeLuna("pout","seductive","angry","mid")
    her "I'm glad you came to your senses. Thank you, If you're completely satisfied, I'll cover these hideous things up now."
    m "Completely, [hermione_name]. 20 points to Gryffindor."
    hide screen luna_main
    with d3

    $ luna_wear_top = True
    $ luna_wear_bra = True
    call update_luna_chibi_uniform
    call lun_chibi("stand","desk","base")
    pause.5

    $ changeLuna("base","closed","base","mid")
    show screen luna_main
    with d3

    her "Well I best be off to classes."
    m "You're going to class looking like a fellow classmate?"
    $ changeLuna("base","base","raised","mid")
    her "It's not going to be a problem. Luna's barely in class as it is, I can just pretend to be her. Maybe I'll even improve her test scores. You'll notify the teachers I can't attend class right?"
    m "Absolutely. (Not a chance) But, what if you bump into her in the halls?"
    $ changeLuna("pout","seductive","base","mid")
    her "Believe me [genie_name], Luna will probably think I'm some kind of Wrackspurt that's messing with her head."
    hide screen luna_main
    with d3

    call lun_walk("desk","leave",2.7)

    $ hermione_busy = True

    jump main_room


#Lamia transformation.

label potion_scene_1_3: #Lamia potion
    call her_main("That's dumb.","scream","worriedCl")
    m "I literally don't know."
    jump main_room


#Clone transformation.

label potion_scene_1_4: #Clone potion
    m "Do you ever feel conflicted about what we do in here [hermione_name]?"
    her "Conflicted? I suppose I do... why do you ask?"
    m "because I have a new potion that can help you come to terms with this internal conflict."
    her "What? How?"
    m "It splits your mind into two parts, allowing you to confront yourself and address the problem."
    her "Splits my mind?! That doesn't sound very safe!"
    m "It only splits your mind metaphorically. I ensure you it's as safe as can be."
    her "Well if you made it yourself then I trust it. I mean it's not like the weasley twins made it."
    m "Of course not... Now if you'd kindly drink it we can get to the bottom of your conflicted nature."
    her "..."
    her "Well here goes..."
    call nar(">Hermione drinks the potion.")
    her "Mmmmmm it's so sweet..."
    herA "Ughhhh, it's so sour..."

    #Hermione split into two versions of herself, one slutty, one prudish
    #Slutty one wants to have sex with Genie
    #Genie obliges
    #Slutty Hermione enjoying it immensely
    #Genie trying to convince pruddy Hermione to join in
    #Prude Hermione wants no part in it, although she is slightly aroused
    #Slut Hermione
    #Genie cums in Hermione
    #Slut Hermione wants to go again
    #Slut Hermione offers to suck Genie to get him hard
    #Genie says why don't we get prude Hermione to do it
    #Slut Hermione says that's a great idea
    #Prude Hermione refuses
    #Slut Hermione and Genie force her to her knees
    #Genie talks dirty to Prude Hermione while Slutty Hermione encourages her
    #Genie ends up covering her in cum
    #Prude Hermione partially speechless
    #Slutty Hermione wants to go again but Genie is spent
    #Hermione reforms into one person
    #Genie ridicules her, saying that even the most prudish and reseverved version of herself ended up sucking him off
    #Hermione feels both shame and pride
    #THE END

    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    hide screen ctc
    with Dissolve(.3)

    call her_walk("mid","leave",2)

    $ hermione_busy = True
    jump main_room
