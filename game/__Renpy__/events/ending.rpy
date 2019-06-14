

### Yule Ball Ending ###

label ball_ending_start:
    call nar("Are you sure you wish to start this event?")

    menu:
        "Yes!":
            $ gave_the_dress = True #Turns True when Hermione has the dress.
            m "[hermione_name], that ball you've mentioned..."
            m "When did you say it would start again?"
            call her_main("The autumn ball?!","grin","base")
            call her_main("I'm so excited!!! I can't wait for it!","grin","happyCl")
            call her_main("Just two more days, [genie_name]","base","glance")
            m "That soon, huh?"
            call her_main("Yep! I still have a ton op preparations to make though.","soft","baseL")
            m "Well then I better not keep you occupied any longer..."
            m "Unless..."
            g9 "Maybe we could..."
            call her_main("Have some fun?","soft","glance")
            g9 "You can read my mind, girl."
            jump hermione_favor_menu
        "No.":
            jump hermione_talk


label ball_ending_E1:

    $ ss_event_pause += 2

    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME

    call sna_walk(action="enter", xpos="desk", ypos="base", speed=2.5)
    pause 1.5

    call sna_main("Genie...","snape_01", xpos="base", ypos="base")
    m "Severus?"
    call sna_main("I think I may have figured out why your magic does not work the way it should...","snape_05")
    g4 "Seriously?!"
    call sna_main("Yes...","snape_23")
    sna "It's quite obvious actually... I'm surprised that it didn't cross my mind before."
    call sna_main("You see, the thing is that every building in \"Hogwarts\" is enchanted with all kinds of protection spells...","snape_24")
    m "Protection spells, huh?"
    call sna_main("Yes...","snape_23")
    sna "Very powerful, old and nasty magic..."
    call sna_main("Even the land itself is heavily enchanted for kilometers in every direction...","snape_24")
    m "Hm..."
    call sna_main("Basically, any number of spells could be interfering with your powers around here...","snape_25")
    m "Wait, then how come that you have no problems with casting your spells?"
    call sna_main("My magic is \"Hogwarts\" magic, friend...","snape_05")
    sna "But I bet your powers are alien enough to be perceived as a threat."
    m "Interesting..."
    call sna_main("I think if you manage to get far enough from the school grounds...","snape_24")
    m "I will be able to go home... finally..."
    call sna_main("Yes, and the best time to do that would be tonight...","snape_02")
    call sna_main("While everyone is preoccupied with that bloody \"Autumn ball\" you could sneak out unnoticed...","snape_23")

    ### SHAKE HANDS WITH SNAPE ###
    hide screen snape_main
    call blkfade

    hide screen genie
    hide screen bld1
    call sna_chibi("hide")
    show screen chair_left
    show screen g_c_u
    $ gen_chibi_xpos = 220
    $ gen_chibi_ypos = 205
    $ g_c_u_pic = "images/rooms/main_room/hand_00.png"
    play music "music/11 The Quidditch Match.mp3" fadein 1 fadeout 1 # EPIC THEME.
    pause 1

    m "Right, tonight is the night of the \"Autumn ball\"..."
    m "So it ends tonight then..."
    call sna_main("Seems like it...","snape_09")
    call hide_blkfade
    pause.5

    call sna_main("In case I'm right and will never see you again...","snape_05")
    m "Right..."
    call blkfade

    $ g_c_u_pic = "images/rooms/main_room/hand_01.png"
    call hide_blkfade
    pause 2

    call sna_main("The past several month were the best months of my life, Genie...","snape_26")
    call sna_main("Thank you for that, you incredible traveler from another world...")
    call sna_main("Thank you, my friend...")
    m "I don't know what to say, Severus..."
    call sna_main("Then don't say anything...","snape_06")
    call sna_main("Just move on to your next adventure...")
    call sna_main("Our world has stalled you long enough...")
    m "Thank you for keeping me company and being my only friend here, Severus."
    call sna_main("Thank you for being mine...","snape_27") #TEARS?
    call sna_main("I'd better go now...","snape_06")

    # Goes to the door, stops and turns around.
    call blkfade

    hide screen snape_main
    hide screen chair_left
    hide screen g_c_u
    show screen genie
    pause.5

    call sna_chibi("stand","desk","base")
    hide screen bld1
    call hide_blkfade
    pause.5

    call sna_walk(xpos="door", ypos="base", speed=3)
    pause.5

    call sna_chibi("stand","door","base")
    pause.5

    call sna_main("One more thing though...","snape_01", ypos="head")
    m "Yes?"
    call sna_main("If it all goes well...","snape_24")
    call sna_main("Will I find the real Albus Dumbledore in that chair tomorrow?")
    m "I believe so..."
    call sna_main("Hm...","snape_04")
    call sna_main("Albus can't know that I was aware of his absence...","snape_03")
    call sna_main("Is there a way to tell you guys apart?","snape_01")
    m ".............."
    m "How about a secret password?"
    call sna_main("A password?","snape_05")
    m "Yes... just ask me tomorrow: \"Who rules?\"."
    call sna_main("\"Who rules?\"","snape_01")
    g9 "\"Robin Williams!\""
    call sna_main("Robin Wil-... ehm... I'm sorry, who?","snape_05")
    m "You didn't see \"flubber\"?\nGreat movie. Just came out."
    call sna_main("Can't say that I have...","snape_02")
    call sna_main("Alright then...","snape_06")
    call sna_main("Have a save trip home...")
    m "Thank you. Have fun with hosting the ball..."
    call sna_main("*Sigh*","snape_06")
    pause.3

    call bld("hide")
    pause.3

    stop music fadeout 1.0

    call sna_chibi("stand","door","base", flip=True)
    with d3
    pause.3

    call sna_chibi("leave","door","base")
    pause.8

    call bld
    m "............................"
    m "So this is it then...?"
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    m "Seems like my time in this world has come to an end..."
    m "......................."

    if not public_whore_ending: #YOUR PERSONAL WHORE ENDING. WRITING A LETTER.
        m "That Means I'll probably never see the girl again..."
        m "..........."
        m "When I first met her she was so annoying..."
        m "to be honest, all the training I put her through changed very little in that regard..."
        m "But we did have a few special moments together..."
        m ".............."
        m "......................"
        m "I doesn't feel right to leave her without saying goodbye properly..."
        m "And yet I don't want to miss my chance to sneak out unnoticed..."
        m "I don't like long goodbyes..."
        m "Hm..."
        m "I suppose I could leave her a note or something..."

        m "Let's see..."
        call bld
        hide screen genie
        show screen paperwork
        with d3
        m "\"Dear...\""
        show screen genie
        hide screen paperwork
        with d3
        m "Hm... How shoud I adress her?"

        menu:
            m "Dear..."
            "\"Miss Granger\"":
                 $ word_01 = "Hermione Granger"
            "\"Nasty whore\"":
                $ word_01 = "Nasty whore"
            "\"Slut\"":
                $ word_01 = "Slut"
            "\"Cumbucket\"":
                $ word_01 = "Cumbucket"
            "\"Human female\"":
                $ word_01 = "Human female"
            "\"friend\"":
                $ word_01 = "Friend"

        hide screen genie
        show screen paperwork
        with d3
        m "Yes, \"Dear [word_01]\" fits perfectly..."
        ">scribble-scribble-scribble..."
        ">scribble-scribble-scribble..."
        m "\"...it is time for me to go back...\""
        show screen genie
        hide screen paperwork
        with d3
        m "What should I write now?"

        menu:
            m "...time to go back..."
            "\"home\"":
                $ word_02 = "home"
            "\"to the mothership\"":
                $ word_02 = "to the mothership"
            "\"to Dimension \"X\"":
                $ word_02 = "to Dimension \"X\""
            "\"to my world\"":
                $ word_02 = "to my world"
            "\"To my Home Planet - Krypton\"":
                $ word_02 = "to my Home Planet - Krypton"

        hide screen genie
        show screen paperwork
        with d3
        m "Yes, \"Time to go back [word_02]\" that will do..."
        ">scribble-scribble-scribble..."
        ">scribble-scribble-scribble..."
        m "\"...farewell my little...\""
        show screen genie
        hide screen paperwork
        with d3
        m "What should I write now?"

        menu:
            m "...farewell my little... "
            "\"cock-hungry slut\"":
                $ word_03 = "cock-hungry slut"
            "\"cum receptacle\"":
                $ word_03 = "cum receptacle"
            "\"Girl\"":
                $ word_03 = "girl"
            "\"Witch\"":
                $ word_03 = "witch"

        hide screen genie
        show screen paperwork
        with d3
        m "Yes, \"farewell my little [word_03]\" sounds about right..."
        ">scribble-scribble-scribble..."
        ">scribble-scribble-scribble..."
        show screen genie
        hide screen paperwork
        with d3
        m "And now to sign it as..."

        label stupid_kent:
            pass

        menu:
            m "..."
            "\"Genie\"":
                $ word_04 = "Genie"
            "\"Clark Kent\"":
                $ word_04 = "Clark Kent"
                hide screen genie
                show screen paperwork
                with d3
                m "Yes, \"sincerely yours, [word_04]\"..."
                show screen genie
                hide screen paperwork
                with d3
                m "..........."
                m "No, that doesn't make any sense..."
                jump stupid_kent
            "\"Lord Voldemort\"":
                $ word_04 = "Lord Voldemort"
            "\"Traveler\"":
                $ word_04 = "Traveler"

        hide screen genie
        show screen paperwork
        with d3
        m "Yes, \"[word_04]\"..."
        show screen genie
        hide screen paperwork
        with d3
        m "........................"
        m "Yes, this should do..."

    m "Well, off I go then..."

    call blkfade

    hide screen genie
    show screen chair_left
    show screen desk
    call gen_chibi("stand","desk","base")
    hide screen bld1
    call hide_blkfade

    call bld
    m "........."

    call gen_walk(xpos="door", ypos="base", speed=2.8)
    pause.5

    call bld
    m "...................."
    m "Agrabah... here I come..."
    call ctc

    call gen_chibi(action="leave")
    pause.3

    ">.......................{w}............................{w}.....................{w}......................"
    pause.7
    call blkfade

    stop music fadeout 1.0

    centered "{size=+7}{color=#cbcbcb}Outskirts of hogwarts{/color}{/size}"

    call play_music("night_outside")


    ### Scene Setup ###

    $ ccg_folder = "ball"
    $ ccg(layer1="171", layer2="blank", layer3="blank")

    pause.3
    call hide_blkfade
    call ctc

    m "Severus was right..."
    pause.5
    call play_sound("walking_on_grass")

    $ ccg(layer2="172")

    m "The farther away I get from the school grounds..."
    m "The more powerful I'm starting to feel..."

    $ ccg(layer3="173")
    pause.5

    m "I think  this is far enough..."
    m "Time to undo the spell and go back home..."
    m ".........."
    m "...................."
    m "Agrabah, here I come..."

    if not persistent.game_complete: # FIRST PLAYTHOURGH.
        call ctc

        show screen blkfade
        with d9
        pause .5

        play music "music/Plaint.mp3" fadein 1 fadeout 1 #SAD CREDITS MUSIC.

        centered "{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n
                  {size=+5}{color=#cbcbcb}This is ending \"00\" out of \"02\".{/color}{/size}"

        centered "{size=+7}{color=#cbcbcb}Thank you for playing!{/color}{/size}\n\n"

        $ renpy.play('sounds/scratch.wav')
        stop music
        with hpunch
        g4 "Wait, I'm still here!"

        centered "{size=+7}{color=#cbcbcb}WHAT?!{/color}{/size}"

        g4 "I said I am still here, dammit!"

        centered "{size=+7}{color=#cbcbcb}Oh... :({/color}{/size}"

        $ ccg(layer3="blank")
        hide screen blkfade
        with d9

        play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.

    m "....................."
    if persistent.game_complete:
        m "No, I can't just leave like this!"
    else:
        m "I can't just leave like this!"

    m "I must see the girl one last time..."

    call ctc

    hide screen ccg
    call blkfade
    stop music fadeout 1.0

    if not persistent.game_complete: # FIRST PLAY THROUGH.

        centered "{size=+7}{color=#cbcbcb}Fine whatever...{/color}{/size}"

    call play_music("ball")

    centered "{size=+7}{color=#cbcbcb}\"The Annual Hogwarts Autumn Ball\"{/color}{/size}"

    jump ball_ending_E2


label ball_ending_E2:
    call blkfade

    if gallery_active == False: # Regular play-through of the scene.
        $ ball_ending_2 = public_whore_ending # Sets this to True or False

    # Scene Setup
    $ interface_color = "gold"

    hide screen bld1
    hide screen blktone
    call her_chibi("hide")
    show screen blkback
    call cg_scene(layer="02", folder="ball")


    #Setting up Hermione's outfit.

    #Hermione Hair
    call set_her_hair(style="updo", color="brown")

    #Hermione Clothes
    call reset_her_transparency

    $ h_neckwear               = "blank"
    $ hermione_body_accs_list  = []
    $ h_gloves                 = "blank"
    $ h_stockings              = "blank"
    $ h_request_wear_robe      = False
    $ h_request_wear_mask      = False
    $ h_request_wear_gag       = False

    $ h_ears                   = "blank"
    $ hermione_makeup_list     = []
    $ h_glasses                = "blank"
    $ h_request_wear_hat       = False

    call update_her_uniform

    call set_her_outfit(hg_dress_yule_ball_ITEM) #Updates uniform.

    hide screen hermione_main
    hide screen room # MAIN BG (DAY).

    hide screen notes
    hide screen done_reading
    hide screen done_reading_near_fire
    hide screen main_room_menu
    with fade
    pause.1

    hide screen bld1
    hide screen blktone
    call hide_blkfade
    call ctc

    call bld
    m "I'd better make sure to avoid being noticed..."
    m "......................"
    m "That's a whole lot of people out there..."
    m "How big exactly is this school?"
    m ".................."
    m ".................................."
    m "I don't see the girl anywhere..."
    m ".............."
    m "......................"
    m "Well, she has got to be here somewhere..."
    m "................"
    m "................................."

    call blktone

    #Public whore ending.
    if ball_ending_2: #Students talking.
        mal "Have you heard that rumour about Hermione Granger?"
        mal2 "That she is a major slut?"
        mal "Huh? No, that's not a rumour, that's a fact."
        mal "The rumour was that she is being paid in house points to whore herself out."
        mal2 "Hm... I don't believe that. I think she is just a slut."
        fem "Who's a slut?"
        mal "Oh, hey you..."
        fem "So, who's a slut?"
        mal2 "Hermione Granger..."
        fem "Tsk! You, guys are talking about that whore again?"
        fem "That girl jerks off a couple of dicks, gives a few blowjobs and suddenly she is the school's new sensation."
        fem "Pathetic little muggle-born..."
        mal "You should not be jealous of her--"
        fem "Jealous? Of her? Puh-lease!"
        fem "I have no use for popularity that comes from putting cocks in my mouth!"
        mal "Well, if you ever change your mind..."
        fem "Huh?"
        mal "Feel free to use me as a stepping stone on your road to fame!"
        fem "You wish!"
        mal2 "Hey, guys, I think that's Hermione over there!"
        mal "You're right!"
        mal2 "You think if I ask her to the dance I might get lucky later?"
        mal "Not if I ask her first!"
        call play_sound("walking")
        pause 2
        mal2 "Hey, wait up! That was my idea!"
        call play_sound("running")
        pause 2
        fem "Guys...?"
        fem "........................."
        fem "Tsk... Men........"

    #Your whore ending.
    else: #Students talking.
        mal "(Have you heard the rumours?)"
        mal2 "(Yeah. They say Hermione took one for the team.)"
        fem "(Whoring herself out for house points!)"
        fem "(How disgraceful!)"
        mal "(Those are just rumours!)"
        fem "(I think it's more than just that...)"
        mal "(Oh, shut up. You are just jealous.)"
        mal2 "(Yeah, you wish you had Hermione's courage!)"
        mal "(Exactly! She is as loyal to \"Gryffindor\" as no one else!)"
        mal "(Even if that's true, what about it?)"
        mal "(Thanks to her sacrifice our house will be getting the cup this year!)"
        mal2 "(Yeah, and what did you ever do for our house?)"
        fem "(I..... But....)"
        mal "(Exactly! So don't you bad-mouth Hermione then!)"
        mal2 "(You said it, man.)"
        fem "(*Pouting*)"

    hide screen bld1
    call hide_blktone
    call ctc


    call cg_scene(layer="01", folder="ball", trans="d7")
    call ctc

    call bld
    m "(There she is!)"

    mal "Hermione, hey..."
    call her_main("Oh, hello.","base","base",ypos="head")
    mal "You look... so beautiful tonight, Hermione."
    call her_main("Thank you, you are too sweet.","base","closed")
    mal2 "Can I have the next dance?"
    mal "What? Back off buddy, I was here first!"
    mal2 "Like hell you were!"
    mal "Alright, pal! That does it!"
    mal2 "I'm not your \"pal\", buddy!"
    call her_main("..............","open","surprised")
    show screen blktone8
    with d3

    stop music fadeout 3.0
    m "Here is my chance!"
    m "(Pst! Girl!)"
    call her_main("???","upset","base")
    m "(Girl, it's me! Over here!)"
    call her_main("[genie_name]?","open","base")
    m "(Shush! Keep your voice down and follow me.)"
    call her_main("Oh?","open","base")
    pause.1

    hide screen blktone8
    hide screen blktone
    hide screen bld1
    call cg_scene("02", trans="fade")
    call ctc

    call her_main("Sir, what is going on? Why are you... lurking in the shadows?","upset","base")
    m "Just be quiet and listen for a second! Can you do that for me?"
    call play_music("playful_tension") # SEX THEME.
    call her_main("Yes, sir...","upset","base")
    m "Well, here is the thing then..."
    m "There is something you need to kn--"
    call her_main("Of course sir!","grin","squint",cheeks="blush")
    m "What?"
    call her_main("Let's just make this quick, alright?","soft","glanceL",cheeks="blush")
    g4 "Let's make what quick?"
    call her_main("You want me to thank you for the dress now, don't you, sir?","base","glance",cheeks="blush")
    m "The dress? No, no that's not why I am here."
    call her_main("It is fine, sir. I do not mind.","soft","glanceL",cheeks="blush")
    m "Listen to me, girl! I am not who you think--"
    call her_main("Please, sir, let me suck on your cock a little.","open_tongue","concerned",cheeks="blush")
    g4 "Gh--!!!"
    call her_main("Just a little will do. Please. I'm begging you...","open_tongue","concerned",cheeks="blush")
    g4 "Damn you, you damn witch!"
    g4 "Stop this! I really need to talk to you!"
    call her_main("Well of course, sir.","base","glance",cheeks="blush")
    call her_main("Put your dick in my mouth and talk to me.","open_tongue","concerned",cheeks="blush")
    call her_main("Talk dirty to me...")
    g4 "*growl!*"
    m "*Sigh....*"
    m "Fine, let's have it your way..."
    m "But you are abusing your power, girl!"
    call her_main("*Giggle!*","crooked_smile","worriedCl",cheeks="blush")
    m "And after we're done, we'll have that talk!"

    # SUCKING
    show screen blkfade
    with d7

    her "*Slurp!* *Slurp!* *Slurp!*"
    m "................."

    hide screen bld1
    hide screen blkfade
    call cg_scene("03")
    call ctc

    her "*Slurp!* *Gulp!* *Slurp!*"
    her "*Slurp--"
    call cg_scene("04")
    her "Huh?.........."
    her "...................."
    call cg_scene("03")
    her "*Slurp!* *Gulp!* *Slurp!*"
    m "Yes... Like that.... oh... yes..."
    her "*Gulp!* *Slurp!* *Slurp!*"
    her "*Gulp--"
    call cg_scene("04")
    her "...................." #LOOKING BACK
    m "Just keep going girl."
    m "I will let you know if I see someone coming..."
    her "Oh... That's not that, sir..."
    m "Hm?"
    her "They are supposed to make the announcement soon..."
    call cg_scene("03")
    her "*Slurp!* *Gulp!* *Slurp!*"
    m "The announcement?"
    her "*Slurp!* *Slurp!* *Slurp!*"
    her "*Slurp--"
    call cg_scene("04")
    her "Yes. About the coronation..."
    call cg_scene("03")
    her "*Gulp!* *Slurp!* *Gulp!*"
    m "What...?"
    her "*Slurp--"
    call cg_scene("04")
    her "The Hogwarts autumn ball's queen coronation, sir."
    m "Oh... Is that's a thing?"
    m "Any chance you may be chosen?"
    her "A chance?"
    her "It's already been decided, sir."
    m "What?"
    her "Oh, I mean I hope I will win..."
    her "Since I am the one who organized the whole thing it is only fair..."
    her "Wouldn't you agree sir?"
    m "Well... Sounds like cheat--"
    call cg_scene("07")
    her "*Slurp!* *Slurp!* *Slurp!*"
    call cg_scene("04")
    her "Wouldn't you agree sir?"
    m "Ehm..."
    her "Wouldn't you agree sir?"
    call cg_scene("06")
    with hpunch
    her "{size=+7}*gobble!*{/size}" #DEEPTHROATING
    g4 "{size=+7}Oh, yes!!!{/size}"
    her "*gobble!* *gobble!* *gobble!*"
    her "*gobble---"
    call cg_scene("04")
    her "Good. I knew you would approve."
    call cg_scene("07")
    her "*Slurp!* *Slurp!* *Gulp!*"
    m "Oh... This is magnificent..."
    her "*Slurp!* *Slurp!* *Gulp!*"

    call bld
    sna "*Khem!*"
    sna "Attention, maggots!"
    m "(Snape?)"
    sna "I said, quiet down everyone!"
    sna "It is time to announce who will be this year's queen of the annual \"Hogwarts autumn ball\"."
    call bld("hide")

    her "Slurp--"
    call cg_scene("04")
    her "Oh no! I think they are about to start..."
    her "But I can't just leave you in this..."
    her "...condition, sir."

    her "What should I do?"
    m "Just go, girl. We can finish this up later."
    her "But... But you got me this dress, sir. And..."
    her ".........."
    her "No, I can't just leave you like this, sir."
    m "Fine! Finish the job then."
    m "If you put some effort into this we'll be done in no time."
    m "I believe in you, girl."
    her "Hm..."
    her "Then you must promise me something, sir."
    m "Yes, what is it?"
    her "Please, do not restrain yourself."
    g9 "Heh... I rarely do, girl."

    call bld
    sna "This year's \"Hogwarts Autumn Ball\" queen is..."
    sna "Let's see... Can't open the damn envelope..."
    call bld("hide")
    her "Alright. There is no time lose then."
    m "Yes! That's the spirit!"

    if ball_ending_2: #Students talking. Ending "Public whore".
        call cg_scene("03")
        her "*Slurp!* *Gulp!* *Slurp!*"
        m "Yes..."
        call cg_scene("08")
        her "*Gulp!* *Slurp!* *Gulp!*"
        her "*Slurp--"
        call cg_scene("91")
        her "Sir, is this really the proper way to treat one of your students?"
        m "Huh?"
        call cg_scene("08")
        her "*Slurp!* *Gulp!* *Gulp!*"
        her "*Slurp--"
        call cg_scene("92")
        her "I am like a fragile and impressionable little dove..."
        her "Entrusted to your care by my parents..."
        call cg_scene("93")
        her "You were supposed to treat me \"right\", sir..."
        her "And what did you do instead?"
        m "*Khem!* Let me repeat my previous statement:..."
        m "{size=+7}\"huh?\"{/size}"
        call cg_scene("94")
        her "You put your penis in my innocent mouth, sir!"
        call cg_scene("95")
        her "*Slurp!* *Slurp!* *Slurp!*"
        g9 "Oh, I see! Yes, I like this innocent girl act!"
        her "*Slurp--"
        call cg_scene("91")
        her "You pretended to be kind to me..."
        her "You bought me this dress..."
        call cg_scene("92")
        her "And then....................."
        call cg_scene("07")
        her "*Slurp!* *Gulp!* *Gulp!*"
        her "*Slurp--"
        call cg_scene("92")
        her "You took advantage of me, sir!"
        her "Tricked me into sucking your big cock!"
        g4 "Oh... Yes! You're good!"
        call cg_scene("96")
        her "I'm supposed to be enjoying the ball with my classmates right now..."
        call cg_scene("93")
        her "But what am I doing instead?"
        call cg_scene("07")
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "Oh..."
        call cg_scene("97")
        her "*Slurp!* *Gulp!* *Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp--"
        call cg_scene("98")
        her "I'm on my knees, sucking my headmaster off!"
        call cg_scene("97")
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Oh, yes you are, you little slut!"
        her "*Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp!* *Slurp!* *Gulp!*"
        g4 "You are really good at this dirty talk stuff..."
        g9 "You should try writing children's books, or something..."
        call cg_scene("07")
        her "*Slurp--"
        call cg_scene("91")
        her "Oh, but I would not know how, sir..."
        call cg_scene("92")
        her "because I am but a child myself..."
        g4 "You nasty little thing!"
        call cg_scene("97")
        her "*Slurp!* *Slurp!* *Gulp!* *Slurp!* *Slurp!*"
        call bld

        sna "Miss Granger?"
        sna "{size=-4}(Where is that girl?){/size}"
        ">A murmur is running though the crowd of students..."
        call bld("hide")

        her "*Slurp!* *Slurp!* *Gulp!*"
        her "*Gulp--"
        call cg_scene("91")
        her "Sir, am I being an obedient little slut?"
        g4 "Yes you are, girl!"
        call cg_scene("93")
        her "Would you say I am a good student?"
        g9 "I would say that you are an excellent student, girl!"
        call cg_scene("92")
        her "Good..."
        call cg_scene("99")
        her "I am making my mommy and my daddy proud!"
        call cg_scene("95")
        her "*Slurp!* *Slurp!* *Gulp!*"
        g4 "Oh, girl, you are killing me!"
        her "*Slurp-slurp-slurp-slurp!!!*"
        g4 "Oh, yes! Like that!"
        her "*Slurp--"
        call cg_scene("93")
        her "Do I deserve a reward, sir?"
        call cg_scene("100")
        her "I would like you to reward me with your cum, please."
        g4 "Grh!"
        call cg_scene("97")
        her "*Slurp!* *Slurp!* *Slurp!*"
        g4 "Geh! Almost...!"
        her "{size=+5}*Slurp-gulp-slurp-slurp!!!*{/size}"
        g4 "{size=+5}Here it com--{/size}"
        call cg_scene("101")
        her "*Slurp--.........................."
        her "!!!"
        call ctc

        call blkfade
        call cg_scene("102", trans="skip")
        g4 "{size=+5}What the...!? Why did you stop?!{/size}"
        g4 "{size=+5}What the hell are you doing--{/size}"
        call hide_blkfade
        call ctc

        her "{size=+5}Cum for me. sir! Cum for me!{/size}"
        with hpunch
        g4 "{size=+5}What the hell is this?!{/size}"
        call cg_scene("103")
        her "{size=+5}Cum for me. sir! I want your hot cum on me!{/size}"
        g4 "Argh! You whore!"
        call cg_scene("104")
        her "{size=+5}Yes I am!{/size}"
        her "{size=+5}Nothing but a cum hungry whore, sir!{/size}"
        with hpunch
        g4 "{size=+7}Argh!!!{/size}"
        g4 "{size=+7}Take this, then!!!{/size}"

        show screen white
        pause .1
        hide screen white
        with hpunch

        g4 "{size=+7}ARGH!{/size}"
        call cg_scene("105")
        her "{size=+5}Ah! Yes, sir! Yes! cum for me!{/size}"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch

        g4 "{size=+7}ARGH!{/size}"
        g4 "{size=+7}Argh!!! YES!!!{/size}"
        call cg_scene("106")
        her "Ah... yes... ah..."
        g4 "Oh... ght... *panting*"
        call cg_scene("105")
        her "Thank you sir..."
        call cg_scene("107")
        her "..........................................."
        call ctc

        call blkfade
        pause.5

        m "What on earth just happened, girl?!"
        call her_main("What do you mean, sir?","soft","glanceL",cheeks="blush", ypos="head")
        call cg_scene("02")
        call hide_blkfade

        m "Do I really need to point this out to you, girl?"
        g4 "{size=+5}Do I really?{/size}"
        call her_main("Oh... You mean the hair thing...?","soft","glanceL",cheeks="blush")
        m "Yes...\"the hair thing\"..."
        call her_main("Well, what did you expect me to do, sir?","crooked_smile","worriedCl",cheeks="blush")
        m "Literally anything..."
        g4 "...but {size=+7}THAT!{/size}"
        call her_main("But... I need to look my best for the coronation...","open","base")
        m "And a hairdo full of cum is supposed to ensure that?"
        call her_main("Well... yes...","soft","glanceL",cheeks="blush")
        call her_main("You see, cum is a great hair fixative and--","open","base")

        stop music fadeout 1.0
        sna "Miss Granger..................?"
        sna "You are about to miss your own coronation, girl!"
        sna "(Not that I care...)"

        call her_main("The coronation! I must go now!","open","surprised")
        call play_sound("running")
        pause 3

        m ".............................."
        m "................"
        m "..."
        with hpunch
        g4 "{size=+9}WHAT THE HELL...?!!{/size}"
        call ctc

        call blkfade

        ">..............{w}..................{w}...................."

    else:
        call cg_scene("06")
        with hpunch
        her "{size=+5}*GOBBLE!*{/size}"
        g4 "{size=+5}Yeeeeeeeeeees!{/size}"

        call bld
        sna "There! Hm...?"
        sna "(Well of course... Why am I not surprised?)"
        sna "Miss Hermione Granger of the \"Gryffindor\" house..."
        ">Loud applause and cheering."
        sna "Miss Granger, if you would be so kind to grace us with your presence..."
        call bld("hide")

        her "*GOBBLE--GOBBLE--GOBBLE!*"
        m "Yes! That's a good slut!"
        her "{size=+5}*gobble--gobble--gobble!!!*{/size}"
        m "Yes. Now, move your tongue..."
        m "Lick my balls, girl. Come on!"
        call cg_scene("10")
        her "*gobble!* *Lick!* *Lick!* *gobble!*"
        m "Yes... Like that."
        m "What a good whore you are..."
        her "*Lick!* *Lick!* *gobble!* *Lick!*"
        m "Now look up at me whore."
        call cg_scene("11")
        her "???................"

        call play_sound("spitting")
        show screen white
        pause.3
        hide screen white
        call cg_scene("12", trans="vpunch")
        call ctc

        her "*gobble??!*"
        m "No, don't you stop now!"
        call cg_scene("13")
        her "*gobble--gobble--gobble!*"
        m "Yes, whore! Yes!"

        call bld
        sna "MIss Granger?"
        sna "If you would, please..."
        sna "Miss Granger?"
        call bld("hide")

        call play_sound("spitting")
        show screen white
        pause.3
        hide screen white
        call cg_scene("14", trans="vpunch")
        call ctc

        her "!!!!!!!!!!!"
        her "......................................?"
        m "What's the matter, my little spit bucket?"
        m "Keep sucking my cock!"
        call cg_scene("15")
        her "*gobble--gobble--gobble!*"
        m "Yes. Good whore."
        her "*gobble--gobble--gobble!*"
        m "Keep deepthroating me like that, yes!"
        her "*gobble!* *gobble!* *gobble!*"
        m "The balls! Don't forget to work your tongue!"
        call cg_scene("16")
        her "*gobble!* *Lick!...* *Lick!...*"
        m "Yes! Keep at it and we will be done here in no time!"
        m "Oh, I almost forgot..."
        call play_sound("spitting")
        pause.3
        call cg_scene("17", trans="vpunch")
        call ctc

        her "..........................."
        her ".................."
        call cg_scene("18")
        her "*gobble!* *gobble!* *Lick...* *gobble!*"
        m "you just look so pretty with your face all covered in my spit!"
        call cg_scene("19")
        her "*gobble!* *gobble!* *Lick...* *gobble!*"
        m "Hm..."
        her "*gobble!* *gobble!* *Lick...* *gobble!*"
        m "Maybe we should show your pretty face to everyone?"
        m "Should I call some of your classmates over?"
        call cg_scene("17")
        her "!!!!!!!!!!!!!!!"
        m "Relax..."
        m "I want to get caught as much as you do."
        call cg_scene("19")

        call bld
        sna "Miss Granger?"
        sna "{size=-4}(Where is that girl?){/size}"
        ">A murmur is running though the crowd of students..."
        call bld("hide")

        m "Alright, listen up, whore."
        call cg_scene("20")
        her "*gobble??*"
        m "I need you to stay still now."
        her "???"
        call cg_scene("21")
        m "Yes, just like that."
        her "................"

        call cg_scene("22")
        her "....................................."
        m "I plan to choke you with my cock a little..."
        m "It'll be fun... just relax..."
        her "......................................"
        m "Your throat is the best, girl."
        her "..........."
        call cg_scene("23")
        m "So warm and tight..."
        her "............................................."
        her "...................."
        her "......."
        call cg_scene("24")
        with hpunch
        her "!!!"
        m "I know, I know, you can't really breathe..."
        g9 "But that's what makes this so much fun!"

        with hpunch
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "Stop struggling, slut. You are not going anywhere!"
        with hpunch
        her "{size=+9}!!!!!!!!!!!!!!!!{/size}"

        call bld
        sna "Miss Granger..................?"
        sna "You are about to miss your own coronation, girl!"
        call bld("hide")

        g9 "Heh..."
        g9 "Your queen is right here..."
        g4 "Chocking on my engorged cock!"
        call cg_scene("26")
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "Oh. You are turning blue, love."
        m "Will you be alright?"
        call cg_scene("27")
        her "{size=+9}!!!!!!!!!!!!!!!!........................{/size}"
        m "Look up whore!"
        her "{size=+3}........................{/size}"
        g4 "I said, look at me!"
        call cg_scene("28")
        her "{size=+9}??!.....................{/size}"

        call play_sound("spitting")
        pause.5

        call cg_scene("29", trans="vpunch")
        her "{size=+9}*!!!!!!!!!!!!!!!!!!*{/size}" # 4 (EYE)

        call cg_scene("30")
        her "...................................................................................."
        g4 "There you go! You wear it well!"
        call cg_scene("31")
        her "...........................................................*SOB!*"
        with hpunch
        g4 "Gght!"
        g4 "Here it comes!"
        g4 "I know you are fighting for air down there..."
        call cg_scene("32")
        g4 "But all you will get from me is a load of hot cum!"
        call cg_scene("33")
        with hpunch
        her "{size=+9}GHT!!!!!!!!!!!!!!!!{/size}"
        with hpunch
        g4 "{size=+9}ARGH!{/size}"
        with hpunch
        call cg_scene("34")
        her "{size=+9}*GULP!-GULP!-GULP!-GULP!-GULP!*{/size}"
        g4 "{size=+5}Yes, whore! Drink my cum!{/size}"
        her "*GULP!-GULP!-GULP!-GULP......*"
        with hpunch
        g4 "Not done, yet. Not done! Argh!"
        call cg_scene("35")
        her "{size=-4}*GULP!* *Gulp!* *Gulp...*{/size}"
        m "Oh, yes..."
        call cg_scene("36")
        her "...................................................."
        m "Well, I think that was the last of it--"
        with hpunch
        g4 "{size=+5}Huh?!!{/size}"
        call blkfade

        stop music fadeout 1.0
        g4 "Hey, what are you--"
        ">Hermione gets up abruptly and runs off without saying a word..."
        call play_sound("running")
        pause 3
        m "Hm...?"
        m "Oh, that's right... The coronation thing..."
        m "............."
        ">..............{w}..................{w}...................."

    pause 1


    if ball_ending_2: #Students talking. Ending "Public whore".
        call sna_main("Miss Granger...?","snape_03", ypos="head")
        call sna_main("You decided to show up after all?","snape_04")
        call sna_main("What an unpleasant surprise...","snape_03")

        call her_main("Professor...","upset","base",ypos="head")
        call sna_main("Well, go ahead then...","snape_10")
        call sna_main("Here is the tiara...")

        $ h_hat                    = "tiara"
        $ h_request_wear_hat       = True
        call her_main("Professor...","upset","base",ypos="head")

        call sna_main("And the stage is yours...")
        call her_main("Thank you, professor.","base","closed")
        pause.7

        hide screen bld1
        hide screen blkfade
        call cg_scene("108")

        call play_sound("applause")
        call ctc

        her "..............."
        her ".................................."
        call cg_scene("109")

        call play_music("ball")
        her "Hello, everyone!"
        her "Thank you for making me your ball queen for two years in a row!"
        show screen blktone
        call bld

        m "!!!"
        m "Her hairdo looks perfect!"
        m "I suppose I was wrong and--"
        g4 "Nope, there it is!"
        g4 "Dripping down behind her ear!"
        hide screen blktone
        call bld("hide")

        call cg_scene("110")
        her "I would like to dedicate my speech to every girl in this room..."
        show screen blktone
        call bld

        g4 "What was she thinking pulling a stunt like that?"
        hide screen blktone
        call bld("hide")

        call cg_scene("111")
        her "I shall not go as far as to say that I do not deserve this honor..."
        her "Because I think I do..."
        call cg_scene("112")
        her "But I am still very grateful to stand here before all of you tonight..."
        show screen blktone
        call bld

        mal "(huh?)"
        mal "(What's that stuff on her forehead you wager?)"
        mal2 "(Sweat...?)"
        mal "(Hm... Probably..)"
        hide screen blktone
        call bld("hide")

        call cg_scene("113")
        her "I would especially like to thank our esteemed teachers for their hard work."
        show screen blktone
        call bld

        g4 "Doesn't she feel it by now?!"
        g4 "She'd better cut her speech short!"
        hide screen blktone
        call bld("hide")

        her "Hogwarts truly did become a second home for all of us..."
        call cg_scene("114")
        her "I know that I speak for every student in this building when I say this."
        show screen blktone
        call bld

        mal "(That doesn't look like sweat though...)"
        mal2 "(Yeah...)"
        mal2 "(Some weird goo seeping out of her hair...)"
        fem "(Are you guys really {size=+5}that{/size} dim?)"
        mal "(What?)"
        fem "(That's cum... obviously.)"
        mal2 "(What? Bullshit, girl!)"
        fem "(I think I know cum when I see it.)"
        mal "(I bet you do. *Chuckle*)"
        fem "(Whatever. Just take a better look...)"
        fem "(She must've let some guy bury his cock in her hairdo and pump it full of semen.)"
        mal "(Hm... Hair fucking then? Is it a thing now?)"
        mal2 "(You girls do the craziest things.)"
        fem "(*Humph!* Not all of us are sluts, you know.)"
        mal "(Unfortunately not...)"
        fem "(\"Unfortunately\"?!)"
        fem "(Tsk! You, men are so clueless about everything!)"
        fem "(You could never build a meaningful relationship with a slut!)"
        mal "(What's a \"meaningful relationship\"?)"
        fem "(It's when your girl is also your best friend.)"
        mal "(Oh, I don't need {size=+5}that{/size}!)"
        mal "(I already have a best friend, this ugly bugger right here.)"
        mal2 "(Dito, mate!)"
        mal "(But I sure could use a slut in my life!)"
        mal2 "(Dito, mate!)"
        fem "(...you guys are...)"
        fem "Such Idiots!!!"
        hide screen blktone
        call bld("hide")

        call cg_scene("115")
        her "I remember when I was just a little girl..."
        show screen blktone
        call bld

        m "Huh?"
        hide screen blktone
        call bld("hide")

        her "Frightened of my power... confused..."
        show screen blktone
        call bld

        m "Hm..."
        m "There... She did it again..."
        hide screen blktone
        call bld("hide")

        her "Who knows what would have become of me if not for Hogwarts!"
        show screen blktone
        call bld

        m "And again..."
        m "Why does she keep on jerking her shoulder in that awkward manner...?"
        hide screen blktone
        call bld("hide")

        her "I am so lucky to be a student here..."
        call ctc


        ### REVEAL TITS ###

        stop music
        call cg_scene("116")
        call ctc

        show screen blktone
        show screen bld1
        with hpunch

        g4 "!!!"
        call sna_main("!!!","snape_11")
        hide screen blktone
        call bld("hide")

        call play_music("ball")
        her "Thank you, everyone..."
        call cg_scene("117")
        her "Let me say this again..."
        call cg_scene("118")
        her "Thank you for making me your ball queen this year..."
        call ctc

        call blktone
        mal "(Am I hallucinating?)"
        mal2 "(No, it's really happening... I see it too...)"
        mal "(Hermione... Granger's... tit...)"
        mal "(Major wardrobe malfunction, mate!)"
        fem "(Oh no! Poor thing! We must let her know!)"
        mal "(Don't you dare to take this away from us, girl!)"
        fem "(But...!!)"
        call hide_blktone
        call ctc

        her "And most of all I am thankful to my parents..."
        her "The people who raised me..."
        her "Mommy... Daddy..."
        call cg_scene("119")
        her "I wish you could see how much Hogwarts changed me..."
        her "I wish you could see your little girl right now..."
        her "{size=-5}Ah...{/size}{image=textheart}"
        call ctc

        call blktone
        g4 "The whore is blushing! She is well aware of what's going on!"
        g4 "Nasty slut!"
        g4 "(She planned the whole thing??!)"
        m "(By the great desert sands... What have I unleashed!?)"
        call hide_blktone

        call cg_scene("120")
        her "..............................."
        her ".................."
        call ctc

        call blktone
        mal "(Now she just sorta stands there...)"
        mal2 "(Giving us a better look...?)"
        mal "(Do You think she is aware of her tit being visible at all?)"
        fem "(What a shameless display...)"
        fem "(And to think that I almost felt sorry for the slut...)"
        fem "........................"
        with hpunch
        fem "{size=+7}Cover up, you shameless slut!!!{/size}"
        mal "(!!!)"
        mal2 "(Have you lost your mind, yelling like that?!)"
        with hpunch
        fem "{size=+7}Gryffindor whore!!!{/size}"
        call hide_blktone

        call cg_scene("121")
        her "{size=-3}Ah...{/size}{image=textheart}"
        her "...............................a-ha...{image=textheart}{image=textheart}{image=textheart}"
        call ctc

        call bld
        "Somebody from the crowd" "Show us both of them, Hermione!"
        "Another voice from the crowd" "Look! Her face is all covered in cum!"
        "Somebody from the crowd" "Have you no shame anymore, Hermione?!"
        "Another voice from the crowd" "Cover up, you slut!"
        call bld("hide")

        call cg_scene("122")
        her "Oh... That's right..."
        her "I almost forgot..."
        call cg_scene("123")
        her "{size=+5}Go Gryffindor!{/size}"
        call play_sound("applause")
        "*Wild whisting and cheering!*"
        call cg_scene("120")
        her "......................................"
        her ".........................................................."
        call ctc

        call sna_main("Quiet down everyone!","snape_12", ypos="head")
        call sna_main("As for you, miss Granger...","snape_12")
        call sna_main("I think that's enough.","snape_12")
        call sna_main("Cover up and get off the stage... Go...","snape_12")
        pause.1
        call bld("hide")

        call cg_scene("122")
        her "\"Cover up\", sir?"
        call cg_scene("119")
        her "Oh? What is this? One of my breasts is completely naked..."
        call cg_scene("120")
        her "How embarrassing..."
        call cg_scene("121")
        her "Ah...{image=textheart}{image=textheart}{image=textheart}"
        call ctc

        call bld
        "Somebody from the crowd" "Whore!"
        "Another voice from the crowd" "Gryffindor slut!"
        "Somebody from the crowd" "I love you, Hermione!"
        "Another voice from the crowd" "Gryffindor rules!!!"

        call sna_main("Miss Granger, I said that's enough!","snape_18", ypos="head")
        pause.1
        call bld("hide")

        her "As you say, professor..."
        call sna_main("And wipe your face, girl. You look repulsive.","snape_12", ypos="head")
        pause.1
        call bld("hide")

        call cg_scene("122")
        her "Oh, this? This is just my--"
        call sna_main("Don't care! Get off the stage already!","snape_18", ypos="head")
        call sna_main("Now!","snape_18")
        pause.1
        call bld("hide")

        call cg_scene("120")
        call ctc

        call blkfade
        call play_sound("applause")
        ">Wild whisting and cheering persists as Hermione descends off the stage..."
        pause 1
        stop music fadeout 3.0
        ">.......................{w}....................{w}......................."


        ### BACK AT THE ALCOVE ###

        call cg_scene("02")
        call hide_blkfade
        call ctc

        call her_main("[genie_name]...","soft","glanceL",cheeks="blush",ypos="head")
        call her_main("There was something you wanted to discuss with me?")
        g4 "Not right now, whore!"
        call blkfade

        call her_main("Sir?!","base","glance",cheeks="blush")
        g4 "I want to fuck you so badly! Come over here!"
        call play_music("playful_tension") # SEX THEME.
        call her_main("Of course, sir...","silly","ahegao_squint",cheeks="blush")


        ### INSERTION ###

        call play_sound("insert")
        with hpunch
        with kissiris
        pause.5
        g4 "{size=+7}OH YEEEES!{/size}"

        call cg_scene("46")

        show screen bld1
        call hide_blkfade
        call ctc

        her "Aaah!!!"
        g4 "Your acceptance speech was a disgrace, girl!"
        call cg_scene("50")
        her "I thought it went rather well..."
        g4 "Showing off your tits like that?!"
        call cg_scene("56")
        her "Only one... ah..."
        g4 "What?"
        her "Only one tit, sir..."
        g4 "Whatever happened to that idealistic and self-righteous girl you once were?!"
        call cg_scene("59")
        her "You fucked her out of me, sir!"
        g4 "You're damn right I did!"
        call cg_scene("124", trans="d2")
        her "You fucked her out of me with your enormous cock, sir!"
        g4 "Argh! You whore!"

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        with hpunch

        call cg_scene("58")
        her "Ah!!!"
        g4 "Quiet, whore! Someone will hear you!"

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        with hpunch

        her "Ah! [genie_name]!"
        g4 "I said, be quiet!"

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        with hpunch

        call cg_scene("55")
        her "Ah! [genie_name]!"
        call cg_scene("124")
        her "Yes! Fuck me harder!"
        m "Are you raising your voice on purpose, whore?"
        g4 "Do you want to get caught like this?"
        g4 "On your professor's cock?"
        call cg_scene("125")
        her "Ah! Maybe..."
        call cg_scene("124")

        her "Call me a \"mudblood\", sir!"
        m "What?"
        call cg_scene("51")
        her "Call me a \"mudblood\", please!"
        m "A \"mudblood\"?"
        call cg_scene("58")
        her "Ah! Yes! Yes! I am a mudblood whore!"
        g4 "Whatever!"

        call play_sound("slap")
        show screen white
        pause.5
        hide screen white
        with hpunch

        call play_sound("slap")
        show screen white
        pause.4
        hide screen white
        with hpunch

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch

        call play_sound("slap")
        show screen white
        pause.2
        hide screen white
        with hpunch

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        with hpunch


        call cg_scene("64")
        her "AAAAAAAAAAAAAAAAH!"
        her "Yes!!! Yeeees! Ah!"
        call cg_scene("63")
        her "Fuck me [genie_name]! Fuck me harder!!!"
        g4 "Grht! Harder than this, whore?!"
        g4 "!!!"
        g4 "Crap!  Someone's coming!"
        call cg_scene("64")
        her "No, sir, not yet. But if you keep spanking me--"
        g4 "No, whore! A bunch of students are coming this way!"
        call cg_scene("127")
        her "What?!"

        ### STUDENTS ###

        sly1 "Well, well, well... What have we here?"
        call cg_scene("126")
        call ctc

        her "!!!"
        sly1 "I thought it could be you, \"gryffindor\" filth..."
        sly1 "Moaning like a whore..."
        sly1 "Getting fucked by... Oh..."
        with hpunch
        sly1 "Professor Dumbledore!?"
        m "Hello, boys..."
        her ".........................."
        sly1 "Oh... Em... We didn't know..."
        sly1 "We'll be leaving now..."
        m "What? Don't be silly, boys."
        m "You are more than welcome to stay."
        sly1 "We are?"
        call cg_scene("128")
        her "What?!"
        m "Of course."
        call cg_scene("129")

        her "Professor!!!?"
        m "The girl's frontal area is completely at your disposal."
        call cg_scene("130")
        her "Professor! No!"
        m "What's wrong, slut?"
        call cg_scene("129")
        her "Sir, don't call me that in front of them, please..."
        m "What's the matter? Why are you Acting shy all a of sudden?"
        her "Can't you see that they are from \"Slytherin\"?!"
        m "So what?"
        her "Our two houses... we have a history."
        m "Oh..."
        m "Well, then you shall become the bridge between \"slytherin\" and \"gryffindor\"."
        m "Hermione Granger, the ambassador of peace!"
        call cg_scene("130")
        her "No, sir! I refuse!"
        her "And stop moving your hips while we're talking, sir!"
        m "Boys, what is taking you so long?"
        m "I said, the whore is yours!"
        her "Professor Dumbled-"
        sly1 "Shut up, filth!"


        ### SPIT ON FACE ###

        call play_sound("spit")
        show screen white
        call cg_scene("132", trans="skip")
        pause.2
        hide screen white
        with hpunch
        call ctc

        call cg_scene("133")
        her "!!!"
        m "There you go!"
        sly2 "Ha-ha-ha! Nice one! Look at her stupid face!"
        call cg_scene("134")
        her "You... You...!"
        sly1 "We really enjoyed your speech, \"gryffindor slut\"."
        sly2 "Yeah... Sure did..."
        her "That wasn't meant for you, you slytherin scum!"
        sly1 "Wasn't meant for us? What are you, stupid?"
        sly1 "You bared your filthy, muggle-born flesh on stage! In front of the entire school!"
        sly1 "{size=+7}Of course it was for everyone, you dumb cunt!{/size}"
        call cg_scene("135")
        her "Sir! Stop fucking me!"
        m "Huh? You mean, like this?"
        with hpunch
        pause.3

        her "Ah-aha! No, professor, stop it!"
        m "Stop? I think I will fuck you harder instead!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3

        call cg_scene("133")
        her "Aahah!!!"
        sly1 "Yes... You are ours now, slut!"
        call ctc


        ### DICKS OUT ###

        call cg_scene("136")
        her "What?! What are you doing?!"
        call cg_scene("137")
        her "Put your filthy dicks away immediately!"
        with hpunch
        pause.3
        call cg_scene("138")
        her "Ah... Aha..."
        sly1 "Yes... I wanted to do this for quite some time now..."
        her "Professor!"
        m "Huh? Oh, don't you mind me girl."
        m "Imagine that I'm not even here..."

        call play_sound("spit")
        show screen white
        call cg_scene("139", trans="skip")
        pause.2
        hide screen white
        with hpunch
        call ctc

        call cg_scene("140")
        her "Stop it! Stop spitting in my face, you bastards!"
        sly1 "Make us, whore!"
        her "I am warning--"

        call play_sound("spit")
        show screen white
        call cg_scene("141", trans="skip")
        pause.2
        hide screen white
        with hpunch
        call ctc

        call cg_scene("142")
        her "{size=+5}*Gulp!*{/size}"
        sly2 "Ha-ha-ha! Right in the mouth! Good one, mate!"
        sly1 "And she swallowed it too!"
        call cg_scene("140")
        her "That's was an accident!"
        sly1 "Was it? Let's see."
        her "Huh?"

        call play_sound("spit")
        show screen white
        call cg_scene("141", trans="skip")
        pause.2
        hide screen white
        with hpunch
        call ctc

        call cg_scene("142")
        her "{size=+5}*GULP!*{/size}"

        sly2 "She did it agagin!"
        call cg_scene("140")
        her "That's because I didn't expect it... That's just a reflex!"
        sly1 "That's one hot reflex!"
        g4 "Oh... yes..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "Ah... Ah-aha..."
        her "You will pay for this, you spineless slytheri--"
        sly1 "Shut it, mudblood!"
        call cg_scene("143", trans="hpunch")
        call ctc


        ### DICK IN MOUTH ###

        her "!!!........................................................."
        sly2 "Cool! I'm next!"
        her "*Gulp!*"
        sly1 "Suck my cock, bitch! Suck it I said!"
        m "Do what the boy tells you, girl."
        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch

        m "Come on!"
        call cg_scene("144")
        her "*Slurp...*"
        sly1 "She's doing it! Hermione Granger sucking me off, lads!"
        sly2 "Awesome! Can't wait to give it a go myself!"
        sly1 "Oh... wow... she's good..."
        her "*Slurp!* *Slurp!* *Gulp!*"
        sly1 "Oh yes... Yes..."
        sly1 "Oh... You are so good at this, whore!"
        sly1 "It's... I..."

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        call cg_scene("145", trans="hpunch")
        her "{size=+7}*gobble?!?*{/size}"
        sly1 "{size=+5}Yes, yes! Swallow it all!!!{/size}"


        ### CUMMING ###

        call cg_scene("146")
        her "{size=+5}*Gulp-gulp-gulp-gulp!*{/size}"
        her "*{size=+3}Gulp-gulp-gulp...*{/size}"
        her "*Gulp-gulp-gulp...*"
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        call cg_scene("147")
        her "Gu-aha..."
        her "Is this all you got? Pathetic!"
        sly2 "Oh... Shut up whore... You sucked me dry..."
        call cg_scene("137")
        her "Come on! Who's next?!"
        sly2 "Me! I'm next!"
        call cg_scene("148", trans="hpunch")
        call ctc

        call cg_scene("149")
        her "*Slurp!* *Slurp!* *Slurp!*"
        g4 "Oh... Yes... Yes!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Slurp!* *Slurp!* *Slurp!*"
        sly2 "Oh! Her mouth is so slippery and warm!"
        her "*Slurp!* *Slurp!* *Slurp!*"
        g4 "Yes! Suck that cock, you whore!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Gulp!* Gulp!* *Slurp!*"
        sly2 "I don't know... gh... How much longer..."
        sly2 "...I could keep up like that."
        her "*Slurp--Slurp-Slurp-slurp!*"
        her "*Slurp-Gulp-Slurp-Slurp-gulp!!!*"
        sly2 "Oh, man... Oh man..."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp!!*"
        sly2 "I... I..."
        sly2 "..................."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp!!*"
        with hpunch
        sly2 "{size=+7}I'm cummiiiiiiiiing!{/size}"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        call cg_scene("150", trans="hpunch")
        her "{size=+7}*gobble?!?*{/size}"
        call cg_scene("149")
        her "{size=+5}*Gulp-gulp-gulp-gulp!*{/size}"
        her "{size=+3}*Gulp-gulp...*{/size}"
        her "*Gulp....."
        sly2 "Ah... my cock..."
        call cg_scene("152")
        her "Gu-aha..."
        call cg_scene("151")
        her "Next! Come on! Is this all you got?"
        sly1 "I'm next, mudblood!"
        call cg_scene("154")
        her "{size=-5}Ah... Don't call me that, you bastard...{/size}{image=textheart}"
        sly1 "Gonna fuck your face real good, whore!"
        sly1 "And after I fill your mouth with my cum, you're gonna thank me!"
        sly1 "Aren't you, mudblood whore?"
        call cg_scene("153")
        her "Fuck you!"

        call play_sound("spit")
        show screen white
        call cg_scene("141", trans="skip")
        pause.2
        hide screen white
        with hpunch
        call ctc

        call cg_scene("142")
        her "{size=+5}*GULP!*{/size}"

        sly1 "That's what I thought!"
        call cg_scene("154")
        her "You worthless...\"slythe-"
        call cg_scene("155")
        her "!!?"
        call cg_scene("156")
        her "*Slurp!* *Slurp!* *Slurp!*"
        sly1 "Yes! Yes, you mudblood filth! Suck my cock! Suck it!"
        m "This is quite extraordinary..."
        sly1 "Sir?"
        m "It's just..."
        m "Her pussy..."
        call cg_scene("155")
        her "*Slurp?*"
        m "It's tightens every time you call the girl a \"mudblood\"..."
        m "Try calling her that again, boy."
        sly1 "Gladly, sir."
        call cg_scene("156")
        her "*Slurp!* *Slurp!* *Slurp!*"
        sly1 "Yes, whore! I love fucking your \"mudblood\" face!"
        sly1 "And you're loving every moment of this, aren't you?"
        sly1 "Aren't you, mudblood?"
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Yup... Every time you say that..."
        m "Huh?"
        m "What is this? Her legs are shaking!"
        m "Are you cumming, girl?"
        call cg_scene("157")
        her "..............................................."
        m "I think you are!"
        m "Come on, boy let's speed this thing up a little!"
        m "Let's fuck her from the both ends while she is orgasming like a dirty slut!"
        sly1 "Of course, sir."

        sly1 "Take, this, \"mudblood\" whore!"
        with vpunch
        pause.3
        with vpunch
        pause.3
        with vpunch
        pause.3

        g4 "And this!!!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3

        her "{size=+7}!!!!!!!!{/size}"
        g4 "Yes! Her pussy is flooded with juice!"
        sly1 "Agh! Her mouth as well, sir."
        sly1 "I don't know how much longer I... oh..."
        sly1 "Argh!"
        sly1 "{size=+3}Take this, whore!{/size}"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause.1
        hide screen white
        call cg_scene("159", trans="hpunch")
        her "{size=+7}*gobble?!?*{/size}"
        sly1 "{size=+5}Yes, yes! Swallow it all!!!{/size}"


        ### CUMMING ###

        call cg_scene("160")
        her "{size=+5}*Gulp-gulp-gulp-gulp!*{/size}"
        her "*{size=+3}Gulp-gulp-gulp...*{/size}"
        her "*Gulp-gulp-gulp...*"
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        her "....................."
        call cg_scene("154")
        her "Gu-aha..."
        sly2 "You drained my balls, bitch..."
        m "Alright, boys! Let's bring this little party to a worthy conclusion."
        her "{size=+7}I'm cumming!{/size}"
        m "Yeah, whatever, whore."
        m "So, rest of you boys, you just jerk off in her face now, alright?"
        sly1 "Of course, sir."
        sly2 "Yes, sir!"
        m "Yes, just plaster her face with cum. She loves that shit!"
        call cg_scene("161")
        her "{size=+3}No! I am already cumming... Stop!{/size}"
        sly1 "Heh... Hermione Granger... What a whore!"
        sly2 "Yeah! Nothing but a mudblood cunt!"
        her "{size=+9}AAAAAH!!!!!{/size}"
        her "{size=+3}Yes! I'm a whore! I'm a whore!{/size}"
        sly1 "She even admits it!"
        sly2 "I don't think I can last much longer!"
        sly1 "Me neither!"
        sly2 "ARGH!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        call cg_scene("162", trans="hpunch")
        call ctc

        her "{size=+8}AAAAAAAAAAAAH!{/size}"
        her "{size=+3}My face!!{/size}"
        sly1 "Take this, whore!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        call cg_scene("163", trans="hpunch")
        call ctc

        her "{size=+5}AAAAAAAAAAAAH!{/size}"
        sly2 "Argh! Here! Me too!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        call cg_scene("164", trans="hpunch")
        call ctc

        call cg_scene("165")
        call ctc

        her "{size=+4}I'm cumming!{/size}"
        m "Well, don't mind if I do!"
        call cg_scene("166")
        her "{size=+3}No professor, I............!{/size}"
        g4 "Argh!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        call cg_scene("167", trans="hpunch")
        call ctc

        her "{size=+8}AAAAAAAAAAAAH!{/size}"
        call cg_scene("168")
        her "{size=+5}No! My face! My pussy! Ah! I can't stop cumming!!!{/size}"
        sly1 "What a slut!"
        sly2 "Whore!"
        sly1 "Mudblood!"
        her "{size=+8}AAAAAAAAAAAAH!{/size}"

        call play_sound("spit")
        show screen white
        pause.3
        hide screen white
        call cg_scene("169", trans="vpunch")
        call ctc

        call cg_scene("170")
        her "{size=+8}*Gulp!*{/size}"
        call cg_scene("168")
        her "{size=+8}I'll go insane!{/size}"
        call ctc


        ### WHITE FADE ###

        show screen white
        with d9
        pause 1

        ">.............{w}......................{w}....................."

        m "Well, thank you for your cooperation, boys."
        sly1 "Of course, sir, professor Dumbledore."
        sly2 "Glad to be of help, sir."
        sly1 "Thank you, professor."
        sly2 "Alright, let's go back to the ball?"
        sly1 "Yeah, let's go!"
        sly2 "Bye, mudblood whore!"
        sly1 "Yeah, thank you for being such a slut!"
        call her_main("..........................","soft","ahegao", cheeks="blush", tears="mascara_soft", ypos="head")

        call play_sound("footsteps")
        call cg_scene("02")
        pause 2

        hide screen white
        with d9

        sly1 "{size=-4}(Man, professor Dumbledore sure is one cool dude.){/size}"
        sly2 "{size=-4}(Yeah... Who would have thought.){/size}"
        sly1 "{size=-4}(True. I can't help but respect the man...){/size}"
        m "Aw... What nice boys..."
        sly2 "{size=-4}(Yeah... I hope I will be as agile as he is when I am that ancient.){/size}"
        g4 "I'm not ancient, you young punks!"
        m "Although I suppose in a way I am..."

        call her_main("..........................","soft","ahegao",cheeks="blush",tears="mascara_soft")
        m "Whore! Why so quiet?"
        call her_main("I...","silly","ahegao",cheeks="blush",tears="mascara_soft")
        call her_main("I am... not sure...")
        call her_main("What...? What is.......","soft","ahegao",cheeks="blush",tears="mascara_soft")
        m "Come on, girl. Pull yourself together!"
        call her_main("I... I... What?","open","concerned",cheeks="blush",tears="mascara_soft")
        call her_main("I don't understand... I...")
        m "Hm..."
        m "I will be leaving now."
        call her_main("Leaving...?","soft","ahegao",cheeks="blush",tears="mascara_soft")
        m "Yes. Maybe you should too..."
        m "Go clean yourself up and rest or something."
        call her_main("But I can't leave... No... I must...","open","concerned",cheeks="blush",tears="mascara_soft")
        call her_main("The formal dance... I must...")
        m "A dance? You can't dance in this condition."
        call her_main("No! I am the ball queen! I must....","soft","ahegao",cheeks="blush",tears="mascara_soft")
        m "Well, suit yourself."
        m "I'm leaving..."
        call her_main("Good bye... sir...","soft","ahegao",cheeks="blush",tears="mascara_soft")
        m "............."
        m "Farewell, girl."
        call ctc

        call blkfade
        call cg_scene("90")
        pause.5
        call hide_blkfade

        call play_music("festive")
        call ctc

        m "Hm..."
        m "Maybe I should stay and watch Hermione's post-multiple-orgasm dancing?"
        m "No... This ball is almost over. This is my only chance to sneak out unnoticed."
        call ctc

        call blkfade
        pause.5


    ### Your Whore Ending ###

    else:
        call sna_main("Miss Granger...?","snape_03", ypos="head")
        call sna_main("You decided to show up after all? What an unpleasant surprise...","snape_04")
        call her_main("...............................","full","ahegao",cheeks="blush",tears="mascara", ypos="head")
        call sna_main("What happened to your face, girl?","snape_13")
        call her_main(".......................................","full","down",cheeks="blush",tears="mascara")
        call sna_main("Hm... Well, go ahead then...","snape_13")
        call sna_main("Here is the tiara...","snape_13")

        $ h_hat                    = "tiara"
        $ h_request_wear_hat       = True
        call her_main(".......................................","full","down",cheeks="blush",tears="mascara")

        call sna_main("And the stage is yours...","snape_13")
        pause.7

        call cg_scene(layer="37", folder="ball")
        hide screen bld1
        call hide_blkfade

        call play_sound("applause")
        call ctc

        her "..............."
        her ".................................."
        her ".........................................................................."

        call play_music("ball")
        call cg_scene("38", trans="d3")
        her "Ah-a.........................................."

        call bld
        m "Is that...?"
        m "are Leftovers of my cum still in her mouth?"
        g4 "What the hell is she doing?"
        call bld("hide")

        call cg_scene("39", trans="d3")
        her "...................................."
        her "Helwo eweruone..." #Misspelled on purpose.
        call cg_scene("40", trans="d3")
        her "Fenk you for being heah today..." #Misspelled on purpose.

        call bld
        m "I can barely understand a word she is saying..."
        call bld("hide")

        her "Fifst of all I would like foo fenk Profeffor Dumblefore..." #Misspelled on purpose.

        call bld
        m "Me?"
        call bld("hide")

        her "................"
        call cg_scene("37", trans="d3")
        stop music fadeout 1.0
        her ".................................................."
        call ctc

        call cg_scene("41", trans="d3")
        call play_sound("gulp")
        her "{size=+5}*GULP!!!*{/size}"
        call cg_scene("42", trans="d3")
        her "Gua-ha..."
        her "Thank you, professor."
        call bld

        with hpunch
        g4 "YOU WHORE!!!"
        g4 "When did you get this nasty!"
        call bld("hide")

        call play_music("ball")
        call cg_scene("43", trans="d3")
        her "I would also like to thank my parents..."
        her "Then I would like to thank my fellow students!"
        call bld

        call play_sound("applause")
        ">Loud cheering and whistling..."
        call bld("hide")

        her "And the teachers of course..."
        call cg_scene("44", trans="d3")

        call bld
        ">A few rather feeble applauses..."
        call bld("hide")
        call ctc

        call blktone
        mal "(So it's Hermione Granger again this year...)"
        fem "(Tsk... Why am I not surprised?)"
        mal2 "(Maybe because she deserves it?)"
        mal "(Yeah! Stop hating on Hermione!)"
        fem "(Tch... Whatever.)"
        mal "(By the way, when Hermione came upstage...)"
        mal2 "(Yeah, there was something in her mouth. I noticed it too.)"
        fem "(I bet it was someone's cum!)"
        mal "(WHAT!!?)"
        mal2 "(Get your head out of the gutter, girl!)"
        fem "(Why not?)"
        fem "(Everyone knows she is sleeping with Professor Dumbledore!)"
        mal "(No, not your gossips again.)"
        mal2 "(Wait, I want to hear this one. Tell us more.)"
        fem "(What is there to tell?)"
        fem "(Hermione Granger is a whore. She enjoys sucking cocks....)"
        fem "(Yes, she loves to suck cocks but she loves sperm even more!)"
        mal "(....)"
        fem "(She is a sperm addict! She must swallow half a cup of sperm every day...)"
        fem "(Because if she doesn't she goes into a sex-craze...)"
        mal2 "(.....)"
        fem "(And when that happenes she cannot control herself and will gladly sleep with the first man she sees.)"
        mal "(.............)"
        mal2 "(.....................)"
        fem "(Hm? Why are you staring at me like that?)"
        mal "(What? We are not staring.)"
        mal2 "(Yes, keep talking. You are good at this!)"
        fem "(Good at what?!)"
        fem "(Wait a second, are you guys getting off on this?)"
        mal "(Heh... Look at the crow calling the raven black!)"
        fem "(What do you mean?)"
        mal2 "(You are blushing like crazy, girl! And your eyes are all misty!)"
        mal "(Yeah! You enjoy this as much as we do!)"
        fem "(!!!?)"
        fem "You guys are idiots!"

        call play_sound("running")
        pause 3
        mal "(What? What did I say?)"
        mal2 "(Who knows, bro? Bitches be crazy...)"
        mal "(They do be crazy...)"
        call hide_blktone

        call cg_scene("43", trans="d3")
        her "Thank you, everyone for being such a big help in organizing today's event."
        her "And thank you for choosing me as your queen again this year..."
        call cg_scene("45", trans="d3")
        her "What a pleasant but completely unexpected surprise...!"
        her "And one more thing..."
        call cg_scene("43", trans="d3")
        her "{size=+5}Go gryffindor!{/size}"
        call bld

        call play_sound("applause")
        ">The crowd explodes with loud cheers and whistles interspersed by occasional booing..."
        call bld("hide")
        call ctc

        call blkfade
        pause.7

        stop music fadeout 1.0
        m "Great speech..."
        m "Very arousing... Ehm, I mean inspiring."
        call her_main("Thank you, sir.","soft","glanceL",cheeks="blush",ypos="head")
        m "Swallowing my load in front of the entire school?"
        g9 "Very nice touch."
        call her_main("........................................................","crooked_smile","worriedCl", cheeks="blush")

        call play_music("playful_tension") # SEX THEME.

        call cg_scene("02")
        show screen bld1
        call hide_blkfade

        m "Alright, girl. Let's have that talk now..."
        call her_main("....................","upset","base")
        m "There is something I need to tell you..."
        m "Not sure where to start though..."
        m "........................................"
        m "Well, first of all I am--"
        call her_main("Sir, I think I know exactly what you are about to say.","open","base")
        m "You do?"
        call her_main("Of course.","open","base")
        call her_main("One hasty blowjob is not nearly enough to repay my debt to you, am I right?","base","glance",cheeks="blush")
        m "What? No, that's not what I--"
        call her_main("It's fine, sir. Really.","base","glance",cheeks="blush")
        call her_main("Let me just pull my panties down a little...","soft","glanceL",cheeks="blush")
        g4 "Damn you girl! Will you let me finish!?"
        call her_main("Of course sir...","base","glance",cheeks="blush")
        m "Huh?"
        call her_main("Just make sure you don't hit my dress, alright?","open_tongue","concerned",cheeks="blush")
        g4 "*Low growl!*"
        g4 "Come here, whore!"
        g4 "Suppose I might as well fuck you one last time!"
        call her_main("(One last time?)","upset","base")
        call ctc


        ### INSERTION ###

        call blkfade
        call play_sound("insert")
        with hpunch
        with kissiris

        call her_main("{size=+5}Ahh!!!{/size}","open","surprised",cheeks="blush",tears="soft")
        g4 "Oh, yes!"

        call cg_scene("46")
        hide screen bld1
        call hide_blkfade
        call ctc

        her "Ah-ah..."
        m "Hm? Your pussy..."
        m "It's dripping wet, girl."
        call cg_scene("47")
        her "Ah...{image=textheart} It is, sir?"
        her "That's probably from before..."
        m "From before?"
        m "You mean from when you were choking on my cock?"
        her "Ah...{image=textheart} Yes, sir..."
        m "Did it make you cum?"
        call cg_scene("48")
        her "A little..."
        m "Well, you are just precious then, aren't you?"
        her "ah......"
        m "Arent't you, whore?!"
        her "Ah... Whatever you say, sir."
        m "Yes, you are precious, you slut!"
        call cg_scene("49")
        her "............."
        m "Squeezing my cock with your little pussy!"
        her "......................"
        m "Hm...?"
        m "Why are you being so quiet?"
        call cg_scene("51")
        her "Oh... I'm just afraid that someone would--"
        m "I think that's because you want to get spanked!"
        her "What!?"

        call play_sound("slap")
        show screen white
        pause.1
        hide screen white
        call cg_scene("52", trans="hpunch")

        her "EEeeeeeeeegh!"
        m "Quiet, whore! Someone would hear!"
        call cg_scene("53")
        her "Sir, I--"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("54", trans="hpunch")

        her "{size=+7}EEghh!!!{/size}"
        m "Be quiet, I said!"
        m "Or do you want to get caught like this? On your headmaster's cock?"
        m "Do you, Miss queen of the autumn ball?"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("55", trans="hpunch")

        her "Ah..."
        m "Yes, you're liking this aren't you?!"
        call cg_scene("56")
        her ".............."
        g4 "Answer me, slut!"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("55", trans="hpunch")

        her "Yes, sir! I love it!!!"
        call cg_scene("53")
        her "Spank me harder, sir! I deserve it!"
        m "That's the spirit!"
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("55", trans="hpunch")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("55", trans="hpunch")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("58", trans="hpunch")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("58", trans="hpunch")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("59", trans="hpunch")
        call ctc

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("59", trans="hpunch")
        call ctc

        her "{size=+7}Aaaaaah............................{/size}"


        call blktone
        sna "Attention, maggots!"
        sna "The \"Hogwarts Autumn Ball\" formal dance is about to begin..."
        call hide_blktone

        call cg_scene("60")
        her "!!!"
        her "The dance! I completely forgot!!?"
        call cg_scene("61")
        her "Sir, excuse me, but you will have to let me go..."
        g4 "Ah... Your pussy is something else!"
        her "Sir... Ah... I am serious."
        her "As the queen I am expected to lead the dance."
        g4 "Yes... Like that, just like that... Oh, yes."
        call cg_scene("62")
        her "Sir, are you even listening?"
        m "Oh, I hear you alright. And let me make you a counteroffer."
        call cg_scene("61")
        her "Sir?"
        m "Instead of letting you go..."
        m "I will stick my cock up your ass."
        m "Huh? How about that?"
        her "What? B-but..."
        m "I think that is a great plan!"
        her "Sir, no! I--"
        m "One sec, one sec..."
        call blkfade

        m "Let me take my dick out of your pussy first..."

        call play_sound("boing")
        with hpunch
        pause.3


        ### INSERTION ###

        call her_main("Ah...","open","surprised",cheeks="blush",tears="soft", ypos="head")
        call her_main("Sir, no. You must listen to me--","open_tongue","concerned",cheeks="blush")
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris

        call her_main("{size=+7}!!!!!!!!!!!!!!!!!{/size}","scream","surprised",cheeks="blush",tears="soft")
        call her_main("My...{w} My...{w} My...")
        m "Shut it, girl! You are being loud."
        with hpunch
        call her_main("{size=+7}My anus!!!!!!!!!!!!!{/size}","scream","surprised",cheeks="blush",tears="soft")
        g4 "Dammit, girl. I said, be quiet."

        call cg_scene("63")
        call hide_blkfade

        her "{size=+7}I can't! I don't care! It hurts!!!{/size}"
        g4 "Maybe you don't care, but I do, you whore!"
        call cg_scene("64")
        her "{size=+5}Your cock is so huge!{/size}"
        g4 "We'll get caught because of you, you stupid slut!"
        m "Maybe this will help you shut up..."

        # Fishhooking.
        call cg_scene("65")
        her "!!!............"
        g4 "That's right, you slut. Keep quiet!"
        call cg_scene("66")
        her "Ah... Blah..."
        g4 "Your butthole... It's so damn tight..."
        call cg_scene("67")
        her "Ah... blah... ah..."
        g4 "You are drooling allover my hand, you nasty slut!"
        her "Ah... Blah-blhah... ah... bla-ah..."

        call blktone
        stop music fadeout 1.0
        sna "Well, we are about to start..."
        sna "Get into pairs now..."
        sna "No! Male - female pairs, you dull creatures. What do you think this is? A laboratory assignment?"

        call hide_blktone
        call cg_scene("69", trans="fade")

        call play_music("festive")
        m "Don't you worry about missing out on your dance, whore."
        m "We will do a little bit of dancing of our own..."
        her "Ah..."
        m "Yes. This year's ball queen is performing a complicated pirouette with a dick buried deep in her tiny asshole!"
        call cg_scene("69")
        her "Ah... I am ahh..."
        m "Did you say something, your majesty?"
        her "Ah... I am the autumn ball queen... ah..."
        m "Well of course you are!"
        m "But you're also a whore!"
        call cg_scene("68")
        her "I'm a whore..."
        call cg_scene("70")
        her "{size=+7}I'm a whore!!!{/size}"
        call cg_scene("71")
        her "{size=+10}I'm a whoooooooore!!!{/size}"
        g4 "Yes you are!"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        call cg_scene("72", trans="hpunch")

        her "{size=+5}I'm a whore!!!{/size}"
        g4 "Yes you are!"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        her "{size=+5}I'm a whore!!!{/size}"
        g4 "Yes you are!"

        call play_sound("slap")
        show screen white
        pause.3
        hide screen white
        with hpunch
        call cg_scene("73")
        her "{size=+5} I'm cumming!!!{/size}"

        with hpunch
        g4 "Argh! My cock!"
        call cg_scene("74")
        her "{size=+10}I'M CUMMING! I'm a whore!{/size}"
        g4 "I can't fucking move it anymore!"
        her "{size=+10}I'm CUMMING!{/size}"

        g4 "My cock is stuck in your asshole, slut!"
        her "{size=+10}I'm a whooore!!!{/size}"
        g4 "I said relax your muscles a little, dammit!"
        call cg_scene("73")
        her "{size=+7}I can't! I'm cumming!!!{/size}"
        g4 "Fine! Have it your way. I am switching back to your pussy then."
        call cg_scene("75")
        her "Huh?"
        call blkfade

        g4 "Can't pull out!"
        g4 "Relax your damn anus, girl!..."

        call play_sound("boing")
        with hpunch
        pause.3

        call her_main("...........","angry","ahegao",cheeks="blush",tears="messy", ypos="head")
        m "There..."


        ### INSERTING ###

        call play_sound("insert")
        with hpunch
        with kissiris
        pause.5

        hide screen bld1
        hide screen blkfade
        call cg_scene("77")
        her "{size=+10}AAAAAAAAAAAH!!{/size}"
        her "It's in my pussy again..."
        g4 "Yes it is, slut!"
        call cg_scene("79")
        her "But I'm still cumming!"
        her "What is happening to me, sir!?"

        m "Relax girl, I know what I'm doing!"
        m "This is normal for a slut."
        call cg_scene("78")
        her "{size=+5}No! I will go insane!!!{/size}"
        g4 "You will not. Just ride the wave."
        g4 "Enjoy the sensation while I keep on pounding your pussy!"
        her "{size=+5}Ah!!!{/size}"

        call cg_scene("81")
        her "{size=+5}Oh!!!{/size}"
        her "{size=+5}I'm a whore!!!{/size}"
        g4 "Yes you are!"
        her "{size=+5}I'm a slut!!!{/size}"
        g4 "Yes you are!"
        g4 "Oh... I think I am getting close myself..."
        g4 "Argh!"

        $ menu_x = 0.5 #Menu is moved to the left side.

        menu:
            "-Cum inside Hermione's pussy-":
                $ d_flag_01 = True # Came into pussy

                g4 "You think your pussy is ready for this, whore!?"
                her "Sir?!"
                g4 "Take this, then!"

                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                call cg_scene("86", trans="hpunch")

                her "{size=+5}Ah! AAaaah!!{/size}"
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

                her "{size=+5}Ah! I can feel it! It's so hot!{/size}"
                g4 "Argh! Yes!"
                call cg_scene("87")

                her "{size=+5}It's filling me up! It's filling me up!!!{/size}"
                g4 "Yes! You whore! I'll pump your british cunt full of my cum!"

                call cg_scene("88")
                her "[genie_name]! My dress!"
                g4 "What?"
                her "Make sure you don't get any on my dress!"
                g4 "Shut up about your dress, whore! You are ruining the momment!"
                call cg_scene("87")
                her "{size=+5}I'm sorry! Your whore is sorry!!!!{/size}"
                g4 "Yes! Much better!"
                g4 "Oh......."

            "-Cum inside Hermione's butt-":
                $ d_flag_01 = False # Came into asshole

                g4 "Your butthole should better be ready for this, whore!"
                her "What?!"

                call play_sound("insert")
                pause.5
                her "Ah..."

                call play_sound("boing")
                with hpunch
                with kissiris
                call cg_scene("82")
                her "{size=+10}AAaaaahhhhh!!!{/size}"
                her "{size=+5}It's in my butthole again!{/size}"
                call cg_scene("81")
                her "{size=+5}No, sir, please! Don't cum inside of my anus!{/size}"
                her "{size=+5}No, I will die!!!{/size}"
                g4 "You will not die, you silly girl."
                g4 "You will orgasm like crazy. Maybe even pass out for a while, but that's all..."
                her "No, sir, please... I'm scared..."
                g4 "Take this, whore!"
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch

                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                call cg_scene("82")
                her "{size=+5}Ah! I can feel it!!!{/size}"
                g4 "Argh! Yes!"
                call cg_scene("83")
                her "{size=+5}It's filling me up! It's filling me up!!!{/size}"
                g4 "Yes! You whore! I'll pump you full of my cum!"
                call cg_scene("84")
                her "[genie_name]! My dress!"
                g4 "What?"
                her "Make sure you don't get any on my dress!"
                g4 "Shut up about your dress, whore! You are ruining the momment!"
                call cg_scene("85")
                her "{size=+5}I'm sorry! Your whore is sorry!!!!{/size}"
                g4 "Yes! Much better!"

        call ctc

        show screen blkfade
        with d9

        stop music fadeout 1.0
        call her_main("Ah...","silly","ahegao",cheeks="blush",tears="mascara_soft", ypos="head")
        call her_main("I can... barely... stand...")
        g4 "I know what you mean, girl."
        g4 "This was our most intense fuck session yet!"
        call her_main("Yes... I never knew I could...","silly","ahegao",cheeks="blush",tears="mascara_soft")
        call her_main("...orgasm so hard...")
        call her_main("Sir... That thing you wanted to discuss with me...","soft","ahegao",cheeks="blush",tears="mascara_soft")
        m "Yeah... You know what? I actually wrote you a little letter on the matter..."
        call her_main("A letter?","open","concerned",cheeks="blush",tears="mascara_soft")
        m "Yeah... It should explain a couple of things..."
        call her_main("Oh... Alright...","silly","ahegao",cheeks="blush",tears="mascara_soft")
        m "Just read it tomorrow morning..."
        m "Or whenever..."
        m "Or don't read it at all, I don't care..."
        g4 "............."
        call her_main("Sir...?","base","worried",cheeks="blush",tears="mascara")
        m "Stop it with the eyes! You're making me feel uncomfortable..."
        m "I wrote you a letter, so what?"
        call her_main("I think it's sweet.............","base","worried",cheeks="blush",tears="mascara")
        g4 "I said, stop gawking at me girl. I thought you were late for your dance or something!"
        call her_main("THE DANCE!","open","wide",cheeks="blush",tears="mascara")
        call her_main("I'm sorry, I have to go!")
        call her_main("I will see you later, sir!")

        call play_sound("running")
        pause 3
        m "......................"
        m "No you won't......."
        m "Farewell... Hermione..."
        pause.7

        ">..................................{w}.....................................{w}................................"

        call play_music("ball")

        if d_flag_01: # Came into pussy
            call cg_scene("89")
        else: # Came into asshole
            call cg_scene("90")

        ">You linger at the alcove for a short while longer..."
        ">You watch Hermione participate in the formal dance..."
        hide screen bld1
        call hide_blkfade
        call ctc

        ">She is tired and exhausted no doubt, but she hides it well..."
        call bld

        m "(Hm... The girl really is strong...)"
        m "(In all sorts of ways...)"
        call bld("hide")

        if d_flag_01: # Came into pussy
            ">You notice a tiny stream of glistening liquid dripping down the inner sides of her legs unnoticed by the crowd..."
        else: # Came into asshole
            ">You notice that she sort of clenches her buttocks together every now and then."
            ">Probably doing her best to keep the enormous load you deposited up her butthole just a moment ago inside..."

        call bld
        m "................................................."
        m "..............."
        m "(I'd better go now...)"
        call bld("hide")
        call ctc

    if gallery_active:
        jump return_gallery
    else:
        pass


    ### FINAL SCENE ###

    ### GENIE IS LEAVING ###
    call blkfade
    pause 1
    stop music fadeout 1.0

    centered "{size=+7}{color=#cbcbcb}Outskirts of hogwarts{/color}{/size}"

    ### Scene Setup ###
    $ interface_color = "gray"

    hide screen cg # Single layer CG screen.

    $ ccg_folder = "ball"
    $ ccg(layer1="171", layer2="blank", layer3="blank")
    pause.3
    call hide_blkfade

    call play_music("night_outside")
    call ctc

    call play_sound("walking_on_grass")
    m "......."
    pause.5

    $ ccg(layer2="172")
    m "Well, now it is really time for me to go..."

    $ ccg(layer3="173")
    pause.5

    m "Good bye world of bizzare magic..."
    m "Good bye my who--......"
    m "Good bye, Hermione..."
    m "............"
    m "......"

    call play_sound("magic")
    with hpunch

    $ ccg(layer2="174", layer3="blank")
    pause.2

    $ ccg(layer2="175")
    pause.2

    $ ccg(layer3="blank")
    pause.2

    $ ccg(layer2="blank")
    call ctc

    show screen blktone
    with d7

    show screen blktone8
    with d7
    pause .5


    $ achievement.unlock("ending")
    stop music fadeout 1.0

    if public_whore_ending: # PUBLIC WHORE ENDING
        centered """{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n
              {size=+5}{color=#cbcbcb}This is ending \"02\" of \"02\".{/color}{/size}"""
    else: # YOUR PERSONAL WHORE
        centered """{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n
              {size=+5}{color=#cbcbcb}This is ending \"01\" of \"02\".{/color}{/size}"""

    hide screen blktone8
    with d7

    if persistent.game_complete:
        jump ball_ending_E3
    else:
        jump ball_ending_credits



    ### FINAL CREDITS ###

label ball_ending_credits:

    play music "music/02 - Shanghai Honey.mp3" fadein 1 fadeout 1 # ORANGE RANGE THEME.

    $ dermo = "ch_sna defend"

    show screen credits_chibi
    centered """{cps=20}{size=+5}{color=#ea91b0}-Witch Trainer-{/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}(The following credits are the creators of the orignal game, Witch Trainer,\nand did not take part in creating,\nor are affiliated in any way with the Silver mod.){/color}{/size}\n\n
    {color=#e5e297}-\{Written and directed by\}-{/color}\n{size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Head programmer\}-{/color}\n {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Artwork by\}-{/color}\n   {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Additional Artwork\}-{/color}\n   {size=+5}{color=#cbcbcb}DAHR{/color}{/size}\n\n
    {color=#e5e297}-\{Texts proofread and edited by\}-{/color}\n   {size=+5}{color=#cbcbcb}LYK.D9{/color}{/size}\n\n
    {color=#e5e297}-\{Technical advisor\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO{/color}{/size}\n\n
    {color=#e5e297}-\{Game testers\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO\nLYK.D9\nDAHR\nAKABUR{/color}{/size}\n\n{/cps}"""

    $ xder = 160
    $ yder = 160
    $ dermo = "jerking_off_03_ani"
    show screen uni_cr
    hide screen credits_chibi

    centered """{cps=40}
    {size=+5}{color=#e5e297}-\{Sound Effects\}-{/color}{/size}\n{color=#cbcbcb} http://www.freesound.org/ {/color}\n\n
    {size=+5}{color=#e5e297}-\{Music provided by\}-{/color}{/size}\n{color=#cbcbcb} http://incompetech.com/ {/color}\n\n
    {size=+5}{color=#e5e297}-\{MUSIC\}-{/color}{/size}\n{color=#e5e297}\"(Orchestral) Playful Tension\" {/color}{color=#cbcbcb}by Shadow16nh.{/color}\n
    {color=#e5e297}\"Prologue\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"Shanghai Honey\"{/color} {color=#cbcbcb}by orange range.{/color}\n
    {color=#e5e297}\"Introducing Colin\"{/color} {color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"Neville's Waltz\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"The Quidditch Match\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"Anguish\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Awkward Meeting\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Brittle Rille\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Chipper Doodle v2\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Dark Fog\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Despair\" {/color}{color=#cbcbcb}by erenik.{/color}\n
    {color=#e5e297}\"Game Over Theme\" {/color}{color=#cbcbcb}Final Fantasy VII OST.{/color}\n
    {color=#e5e297}\"Boss Theme\" {/color}{color=#cbcbcb}Final Fantasy VII OST.{/color}\n
    {color=#e5e297}\"Hitman\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Music for Manatees\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Plaint\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Under-the-Radar\" {/color}{color=#cbcbcb}by  PhobyAk.{/color}{/cps}"""

    $ xder = 670
    $ yder = 410
    $ dermo = "ch_hem run_f"

    centered """{cps=40}
    {size=+2}{color=#e5e297}-\{CREATOR OF THIS GAME WOULD ALSO LIKE TO PERSONALLY THANK\}-{/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}Dahr{/color}{/size}\n
    {color=#e5e297}for still working for me pretty much free of charge, for inspiring me to keep on going and simply for being a good friend and colleague. {/color}\n\n
    {size=+5}{color=#cbcbcb}Xaljio{/color}{/size}\n
    {color=#e5e297} for not only being my personal \"Ren'Py\" consultant but also an extremely thorough game-tester.\n\n{/color}
    {size=+5}{color=#cbcbcb}Lyk.D9 (a.k.a. Silentchill){/color}{/size}\n
    {color=#e5e297}for toiling tirelessly over my texts full of typos and broken grammar.{/color}\n\n
    {size=+5}{color=#cbcbcb}Bookfisher{/color}{/size}\n
    {color=#e5e297}For everything.\n\n{/color}
    {size=+5}{color=#cbcbcb}The fate (universe or higher power){/color}{/size}\n
    {color=#e5e297}For giving me an opportunity to release another game while retaining complete creative freedom.{/color}\n\n\n
    {size=-1}{color=#cbcbcb}A whole bunch of other people who helped me with development of this game in one way or another,\n but whom I forgot to mention.{/color}\n
    {color=#cbcbcb}And of course to everyone else who supports\nme and my work.{/color}{/size}{/cps}"""

    hide screen uni_cr

    centered """{cps=70}
    {color=#cbcbcb}This is not a commercial video game. The entire project was independently founded solely through\nhttp://www.patreon.com/ and\nby \"Hentai United\" subscribers.{/color}\n\n\n
    {color=#e5e297}{size=-1}-People who supported development of this game with extraordinary amount of money-{/size}{/color}\n
    {color=#cbcbcb}Lawrence Dash, Wirefull, Dorago, Benoit Yan Larose, Talisca{/color}\n\n
    {size=-1}{color=#e5e297}-\"INVESTOR\" pledges-{/color}{/size}\n
    {color=#cbcbcb}Ace, Linus Furtenbach (Bluue), Eduardo Pereira Carneiro, Vicente Sampedro Burgos, Morning Dawnstar, Wolo, John Layon, stefan mitrano, Gavin Spears, sergio.{/color}\n\n
    {size=-1}{color=#e5e297}-\"AGENT\" pledges-{/color}{/size}\n
    {color=#cbcbcb}Cameron MacDowell, Zarsher, Guynonymous, Nerzha, Silvanus2004, Xipomus, Carpy Rex, Adler, Deitan-Baruch St-Amand, Martin Neal, wetrx, mark howard, Kenneth Aguilar, alt, David McClellan, Leo H Wilkin, Thorn, TheDudeAbides, Alexandre Rouleau, thomas taylor, Alexander, Redmoonx22, Valdee, Alexander Lykke Landkildehus, Lucas Ferrari, Dom, derek zhang,Charlatan, Preston C T, waylan, Forrest, Loopy, JohnnyBB, Phantom Void, Kyaa, Stephen Richardson, mark herzog, will newton, Sascha Klug, Joshua McDonald, Undying S, John Cawley III, KitsuneEyes, Slingthatcat, Kieran James, Homod saleh al-shammri, randomuser89, Paul Keating, Antonio B, Marko, Tobias, Akhil Chokshi, Smiling_Jack, Clif Morgan, Derek Heynsbergen, Jack Cartwright, Damien Zaid, callmemusashi Mozambiqued, Nemesis Valentine Vanyar, Stalker, Jason, 4nubis, Curtis, Michael Simon, AB, The Wanderer (Mark Hawker), paul, JEB, Voe, Aselobar, Elgrangato82, froste, YllegaL, Bisongun, Skye Tomlinson, Parad0x, Eric Chen, Destiny, Podchamawa Petrovitch, Will, lc, Sathyan Mathai, Lisandro Gil, bill tedd, Tommy Turner, Marcel Kral, Oric13, Ren Ashjiro, anthony donihee, Honey Withers, Christopher, TofuCats, Drake King, Bookfisher Herring, Dustpan, dusty parrott, Bjorn, Robert Jolly, wilson yang, Tudor G, Arzaz, Etienne Ngo, xazathothx, Robert L Schliff, RO, DavidB, Daedilus, david green, Matt, Ketil, ALEXANDER KOVALEV, Oa, John, PG, largo_leet, David, Artemsgvozdem, heyPert.{/color}{/cps}"""

    #nvl clear
    centered """{cps=70}{size=-1}{color=#e5e297}-\"REBEL\" pledges-{/color}{/size}\n
    {size=-4}{color=#cbcbcb}1234ghumm, A. R., AJ Ferolie, Catalyst Greenhorn, Abraham Benitio, Actafool812, Adam, Casax5, Adam, FearTheDee, Akasection, Alejandro Luna, Aleksandr, Alex Odoul, Alex P., Alexander Randolph, Maidaniuk Yurii, Alexander, Alexei, Alkosh, Allan Pineda, Altagar, Andreas Janning, Andrei Kuz, Andrey Nikolaev, Anton Belyankin, Anton Tropicflames, Antonio Jos Mucoz Gonzalez, Antonio Rivera, Artur Kevorkov, Baran, BearPerson, BeepBep, Benjamin Drew, Bernard Winters, Bob Mannaro, Boyko, Brad, Brandon Gauthier, Brandon Mirr, Brent, Brett Williams, Bruce Gates, Byakuya36, Cirrus, Calmea, Carez, Carnosaur, Chad Dunkerley, Charles Able, Chemmy, Chris, Christopher Coulter, Christopher Woo, Christopher, Conner Owen, Conrad Boucher, Cruise Russo, Cyanide Sam, DMetal, Dakota Rude, Damian Boggs, Daniel Beard, Daniel Nathans, Daniel Smith, Daniel Szczuka, Daniel Torres, Danno, Danny Johansson, Danny Nguyen, Darkflame256, David Lestina, David Ruskin, David, Dean, Devin Barr, Dirk Delva, Donaj88, Donoth Aveano, DoornailsAreJealous, Demodraken, Double A, Drity, Edward le coyte, Eldar Scum, Eric Hsu, Evan waleske, Fabian, Faux, Fetsch Sebastian, Finrock, Fix, Formless, FoxPrince623, Frank Pietsch, Fraziel, Frederic Chen, Garrett Smith, Geoff Levario, Georgika, Gregc, Greg Hartley, Gregory G, Gunderson, Harm Harm, Harry Tizard, Hooverspleen, Ian W, Innes French, Jacob Thompson, Jacob, Jake Smith, Janis Feldbergs, Janus, Jared Whisenand, Jarred Leverton, Jason Buisman, Jason Chong, Jeff Abrams, Jeff, Jeremiah, John F, John S, John doe, John, Jonathan Backer, Jonathan, Joseph Balbuena, Joseph Oliveira, Josh Stegmaier, Juan Gomez, Jurdia, Justin Golden, Karl Stevenson, Karolis, Kenneth Guevarra, Kenneth Jackson, Kenny Huang, Kimo Linder-Fattah, Kolkina, Kristian Lund Jensen, Kryssler, Kurrel, Kyle Sarty, Kyuubi43, LIndy, Levone W., Jonathan Liu, Lockkaliber, Lord G, Lord Rayek, Lothvarthian Malik, Lukas Vystup, Luke Arrowsmith, Magmanox, Majushi, Mario Mueller, Mark Walrusburg, Martino Livio Martinello, Mason Davis, Matt Sullivan, Matthew Young, Michael Klepper, Michael McPherson, Michael O'Hara, Michael, Mike M., Mike Orlando, MinoCrossing, Miran, Mitchell Goodwin, Monky of Space, Morten Brunebjerg Hansen, Myers, N Metso, Naintoxe, Nairolf, Nathan S, Neo Savoric, Niels T, NugLord, Number37, Nym Nemo, Oliver Pirie, Oscar Lan, PS, Passionately Odd Syntax, Patrick Fochler, Patrick, Paul Allen, Peter Grnlykke, Professor Snape, PuddingPowder, Pel-Tore, Rabe, Raglan Strom, Randolph Carter, Random, Reaver78, Rekoar, Reny Frederiksen, Richard Buettner, RickRub, Rightmind, Rob, Robert Doughty, Robert Simmons, Rodrigo Das Flores, Rune Daugaard Lundsteen, Runkle, Russell, SJ M, SYukito, Sane 300, Sayting, Sinedd, Scorch289, Sean Carstensen, Sebastian Tauch, Sehad, Shane Fitzsimons, Shawn Aiken, Skellman, Skull616, SlaveToTheSound, Smaug, Some Guy, Steffen Nissen, Stephen Krieger, Steve Jones, Steven Cunningham, Syr, TGriz, Talon Grant, Teemu, Thae, The Masked Masturbator, This Isntmahname, Thomas Frobish, Thomas Grimes, Thomas Vazquez, Timmothy Firewood, Tom Arne Vestby2, Tony Taylor, Tony Veliz, Truvor, Tuki, Tyler, Venron, Vervalsen, Vi9, Visp, Wanderer, Weenie Beenie, Wesley Gamble, XDrakeX, Xev, YummyTiger, Yuu Yi, Zach Rzepiela, Zakmonster, Zeath, Zenzard, Zim outside, Zoggy, alvin suryaputra, am1tg3, andrew gardiner, artisticMink, barry r king, bloodangel99, butts, caleb4532, charles turnbull, cvonsuela28, dingo egret, dingo1489, eXotic, fernando frias, gliph13, ippherita, izys, jabix, jassem dashti, john smith, josiah richter, karkazin, kyle mock, lia sven, lucas2684, n1ghtfox, nobody, potatohead, progste, randellspec, retchedegg, robster, silvarius2000, srt20022003, strider19, tehcalipwnt, terribleplan, thegreatbambe, timmy turner, varoksa, xenus, ziric.{/color}{/size}\n\n{/cps}"""

    #nvl clear
    centered """{cps=70}
    {size=-1}{color=#e5e297}-\"ACTIVIST\" pledges-{/color}{/size}\n
    {size=-4}{color=#cbcbcb}Adam, Alvin, AmateurArtist98, Anders Sandahl, Naqqash Chaudhry, Andre, Andrew E., Bayushi, Ben Belcastro, Brandon Louie, Brandon Robinet, Brian Wilson, Carmen Williams, Chad Bennett, Dan George, Darklogic, Darknezzz, Dave Shevlin, David Crosby, David Sparkes, Douglas Jones, Draconic Paragon, DragonTamer, Ervin, Francis Dixson, Fredinator, Gene Boglin, George Craig, Greg, Guillaume Mroz, Gustaf Johansson, Hirin, Ian Lindop, IanDasein, Inge, Izzy Sabur, JBTClown, JP, Jack, Jacob Kain, Jan Hanenkamp, Jan M., Jan, Johannes Uwer, John Turner, Joshua Baadsgaard, KiSwordsman, Krux2022, L, Legio 20th, Marconi Ribeiro, Mike, Marius L, Mathias Frandsen, Matthew Marqueta, Max, Michael Webb, Miha Antauer, Mikhail V. Platonov, Mitch, Mountainj6, MrDurper, Sean Hill, Sam, Muirewedd, Neogeta, Nick Foronda, Nick, Noah Gerhards, Oren Barzilai, Pashike, Peeves, Phil Fairbanks, Philip G Honore, Riu Bas, Robert, Reinis Aleksejevs, Rougespartan181, Robert Lesundak, SO, SYH, Sacs, Sapherin, Sayyid, Sean, Shawn MacInnis, Simanith, Soda Zero, Speculations, Stephen Evans, Stonedrake, TRONboy, Tamenund Jones, Tintron, Victor Jd, Vincent McCool, Vitaliy Kasianenko, Vorcai0, Wolfcub, X.p., X39, Yan Luong, Zaker, chippy, joesco726, kurorol2, lambroll, ljennia, matthew lampell, moonwalkin, nh, raaq, six2make4, zack, Andry Sidorov.{/color}{/size}\n\n
    {size=-1}{color=#e5e297}-\"SUPPORTER\" pledges-{/color}{/size}\n
    {size=-4}{color=#cbcbcb}AS84, Aaron Gregory, Gianfranco Calzoni, Aarvil Kemph, Aestus, Alex Martin, Andrea, Andreas, Andrew, Antilles, Antonboeg, Aran, Armando Soto, Azuliar, Batman, Balint Sule, Ben Rog-Wilhelm, Benjamin Cathey, Beth, Brad Hingston, Brandon Grant, Brendan, Brian Borden, Bru, Canyon, Capperroff, Chaintan, Christian Wong, Colton Clayton, Corey S., D, Damian Paradis, Daniel Chai, Daniel Geach, Daniel, Danny Mullay, Darpy, Dave doedry, David Leitner, Dax, Doctor Worm, Dragonman, Edd Holmes, Erebe, Eric Speaker, Fattycakes, FearTheDee, FeyOne, Filip Jaromin, Florian Eberle, FooldiverDX, Fortifel, Frank Bull, G V, Gaetano, Gary Tinsley, Gerald, Gerald, Gerhalt, Gregoire Fauconnier, Gregory, Happy Days, Hellomellowyellow, Hurf durf, Ian Sayer, Ilya, Ivan Nadasaki, J Solomon, Jack Simons, Jack Trebles, James Brown, James Do, Jan-Kristoffer Brekke, Jayro Zipzapili, Jesse Doerksen, Jim, John Jon'zz, John Smith, Jonas Högman, Jose Gonzalez, Joshua West, Julian Silva, KC maps, Kabuto, Kasper Nohr, Kenny Bailey, Kevin McKie, Kuroguma, Lanthanio, Louie Castro, MaiconMM, Majinken, Malcom Reynolds, Marc Voigt, Marcel Muller, Marius Thomassen, MarkAurel, Martin Ax, Matri, Matt, Matthew Lam, Max Robitzsch, MehMonkeys, MercuryTwins, Messor Marra, Michael Troseth, Michael, Michael, Michael, Mike Bow, Mike Jones, Mike Moperz, Mikhail, N0body, NalfeinDoUrden, Nate A, Nicholas Alan McGuire, Nikuss, Nils Harder, Nitrat, Nordicberserk, Notsutos, Oberon, Onyxdime, Oxion1988, Ozzy, Paradosi, Pasi Huttunen, Patrick Gill, Paul Coad, patrick welsh, Paul, Pshenitsyn, PeeM, Peter Nikolas, Peter Ryskin, Pitt85, Preator, Pulimanne, Randall Lively, Richard Dumont, Richard Heying, Richard Soderberg, Riley Heffernan, Robert Bodo, Robert Davis, Rodrigo Rosado, Ronald, Roy Zimmermann, Ryan Bossard, Ryan Calhoun, Salvadore Broadfoot, Scott Barrie, Sebastien Elie, Sebastien Jalbert, SgtAfro, Shadefalcon, Stefano Sottocorna, SilverAxe, Sixxiie, Sky Valverde, Sodajuice, Steffen Sloth, TK, TP Samblanet, Taylor Patton, Taylor, Tenebrys Hentai Flash Games, Matthew Pruter, John Stanko, craig chadwick, TheOriginalJ, Thomas, Timeyy, Tony Li, TonyNinja, Tracy Scops, Travis Haapala, TrikJoker, Tyler Jones, Tyson, Urza Viderico, VC, Vasder, Vay Jay, Victor Sarosi, Warren P Nelson, Wayne Chattillon, William Farris, William Golding, Wlodzimierz Donatowicz, Xaljio, Xisis, brett, bronzeRanger, clerk4470, ghosti1, gillen, ismael torres, jaron uecker, levi tibbals, oakland, otakuguy01, rip_cpu, severin, sirpoffalot, teh_cabbage, tenko, trajor white, wilhelm, winsloven, Arkadii Terentiev, xxx, DAHR.{/color}{/size}\n\n
    {color=#e5e297}{size=-4}-\{Thank you, Joseph Antoni, for organizing all these 750+ names for me.\}-{/size}{/color}{/cps}"""

    pause 1
    call ctc

    jump ball_ending_E3



### Back At Hogwarts ###

label ball_ending_E3:
    show screen blkfade
    with d9

    stop music fadeout 3.0
    ">................................{w}...........................{w}................................."
    pause.5

    centered "{size=+7}{color=#cbcbcb}The morning after...{/color}{/size}"



    # Scene Setup

    $ daytime = True
    $ interface_color = "gold"

    $ h_request_wear_hat = False
    $ hermione_wear_hat = False
    call set_her_hair(style="curly", color="brown")

    call set_her_outfit(None) #Updates uniform.
    call reset_hermione

    hide screen ccg
    hide screen blktone
    hide screen blktone8
    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.
    hide screen notes
    hide screen done_reading
    hide screen done_reading_near_fire
    hide screen chair_left
    hide screen bld1


    $ show_weather()
    show screen weather

    show screen main_room
    show screen chair_right

    hide screen genie
    hide screen owl
    hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
    hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.


    show screen chair_right
    show screen dumbledore

    hide screen blkback
    hide screen blkfade
    with d9

    if public_whore_ending: # PUBLIC WHORE ENDING

        call play_sound("door")
        call sna_chibi("stand","door","base", flip=False)
        pause.8

        call sna_walk(xpos="mid", ypos="base", speed=2)
        pause.8

        call bld
        call play_music("snape_theme")
        dum_[1]"Good morning, Severus."
        call sna_main(".......................................","snape_09", xpos="base", ypos="base")
        dum_[1]"I have the most extraordinary tale to share with you, old friend."
        sna "......................................"
        dum_[1]"But before I do..."
        sna "........................................"
        dum_[2] "Ehm... Severus?"
        sna "........................................."
        call sna_main("Who rules?","snape_06")
        dum_[2] "I beg your pardon?"
        call sna_main("Who rules?","snape_26")
        dum_[2] "...who rules what?"
        sna "R...?"
        dum_[2] "R?"
        call sna_main("Robin....?","snape_27")
        dum_[2] "You don't make any sense, Severus."
        call sna_main("Ah, bloody hell...................","snape_29")
        pause.5
        call ctc

        stop music fadeout 1.0

        hide screen snape_main
        hide screen bld1
        show screen blkfade
        with d7
        pause.1


    else: # PERSONAL WHORE ENDING

        call play_sound("door")
        call her_chibi("stand","door","base", flip=False)
        pause.8

        call her_walk(xpos="mid", ypos="base", speed=3)
        pause.8

        call play_music("hermione")
        call her_main("Sir, if this is about yesterday...","upset","closed", xpos="right", ypos="base")
        dum_[1]"Good morning, Miss Granger."
        call her_main("It's not like I actually enjoyed it or anything, you know...","annoyed","annoyed")
        dum_[1]"Miss Granger, I found this letter on my desk..."
        dum_[1]"It's addressed to you..."
        call her_main("A letter, sir?","soft","base")
        call her_main("Oh, of course! The one you wrote for me, sir.","grin","worriedCl",emote="05")
        dum_[1]"This letter is not from me, miss Granger."
        call her_main("It is not?","annoyed","suspicious")
        call her_main("Oh, I see...","grin","worriedCl",emote="05")
        call her_main("There is no need to be so shy about this, sir. It's alright.")
        dum_[1]"*ahem*... here it is."
        call her_main("Thank you, sir.","base","base")
        call her_main("Let's see....","annoyed","down")
        hide screen hermione_main
        with d3
        stop music fadeout 7.0
        pause.1

        #Define Letter.
        $ letter_from_genie_OBJ = mail_letter_class()
        $ letter_from_genie_OBJ.text = "{size=-7}To: Hermione Granger\n\n{/size}{size=-4}Dear Hermione.\nI am not who you think I am... Not even human so to speak. For months now I have been posing as a person known to you as Professor Dumbledore. But it is time for me to go back to the place I belong. By the time you will receive this letter I shall be long gone. We shall never cross paths again, but I promise you that I will cherish the memories of my brief time in your strange world. \n\nFarewell, my little [hermione_name]. {size=-3}\n\n-Yours truly, Genie-{/size}"

        #Read Letter.
        $ letter = letter_from_genie_OBJ

        $ menu_x = 0.5
        $ menu_y = 0.9

        show screen letter
        with d5

        menu:
            "-Done reading-":
                pass

        call reset_menu_position

        hide screen letter
        call bld("hide")

        call her_main( ".............................................................................................................................................................","disgust","shocked",cheeks="blush")
        dum_[1]"I assume the sender of this letter is that Genie fellow?"
        dum_[1]"The one who has been impersonating me for the past several months?"
        call her_main( ".............................................................................................................................................................","disgust","shocked",cheeks="blush")
        dum_[1]"Well, now that I am back..."
        dum_[1]"I will be putting an end to all that \"favour-selling-business\" of course."
        call her_main("","scream","angry",emote="01")
        pause.1
        with hpunch
        call play_music("hermione")
        her "{size=+7}What?!!{/size}"
        call her_main("How am I supposed to win any points then?","disgust","glance")
        dum_[1]"The same way you always did, miss Granger."
        call her_main("Huh...?","open","annoyed",cheeks="blush")
        dum_[1]"With hard work."
        call her_main("That's just stupid!","angry","angry",cheeks="blush")
        dum_[2] "Miss Granger, would you mind to guard your tongue when--"

        ### TITS ###
        hide screen hermione_main
        $ hermione_wear_bra = False
        call set_her_action("lift_top")
        call her_main("","annoyed","annoyed", xpos="mid", ypos="base", trans="fade")
        stop music
        call ctc

        dum_[3] "{size=+4}!!!{/size}"
        call her_main("Or would you rather see my pussy, sir?","scream","angry",emote="01")
        call her_main("","annoyed","angry")

        hide screen hermione_main
        $ hermione_wear_panties = False
        call set_her_action("lift_skirt")
        call her_main("","angry","annoyed", trans="fade")
        call ctc

        with hpunch
        dum_[5] "{size=+7}GHT!!!{/size}"
        her "I am willing to do anything to get those points, sir!"

        call set_her_action("")
        call her_main("And I mean {size=+9}ANYTHING!!!{/size}","scream","angry",emote="01", trans="hpunch")

        call her_walk_desk_blkfade

        call play_sound("climb_desk")
        pause.7

        dum_[4] "Oh, dear... {image=textheart} "
        pause 1


    $ renpy.play('sounds/win2.mp3')

    centered "{size=+7}{color=#cbcbcb}-\{Thank you for playing!\}-{/color}{/size}\n\n"

    pause 2

    $ persistent.game_complete = True # Turns TRUE after you beat the game. Unlocks the gallery.


    ### Items ###

    $ persistent.gold = 0
    $ persistent.gold = persistent.gold + gold

    # ADD persistand items

    # ADD persistant books

    if public_whore_ending:
        $ persistent.ending_02 = True # Unlocked ending 01.
    else:
        $ persistent.ending_01 = True # Unlocked ending 01.


    $ renpy.full_restart()



    ### THE END ###
