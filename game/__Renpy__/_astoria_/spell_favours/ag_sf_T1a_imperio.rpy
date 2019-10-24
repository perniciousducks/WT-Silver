

### Susan Imperio Events ###

label ag_se_imperio_sb: # Move label
    $ astoria_chibi.zorder = 4 # In front of Susan.
    $ ag_se_imperio_sb.start()

    label end_ag_se_imperio_sb:

    # Reset
    $ astoria_chibi.zorder = 3 # Default

    $ astoria_busy = True
    $ susan_busy = True

    jump main_room



label ag_se_imperio_sb_E1:
    call play_music("stop")
    call hide_characters
    #TODO Astoria chibi zorder above Susan chibi
    call ast_chibi("stand","mid","base")
    hide screen bld1
    with d3
    call sus_walk(action="enter", xpos="desk", ypos="base", speed=2.5)
    pause.2

    call sus_main("Hello, [sus_genie_name]. You wanted to see me?.","open","base","worried","mid", xpos="right", ypos="base")

    call play_music("astoria_theme")
    call ast_main("Hey [ast_susan_name]!","grin","narrow","base","L", xpos="base", ypos="base")
    call sus_main("Astoria? What are you doing here?","open","base","worried","R")
    call ast_main("Oh, don't mind me...","base","base","base","R")

    call ast_chibi(action="wand",xpos="530",ypos="base")
    call ast_main("I'm only here to put a curse on you.","grin","narrow","angry","mid")
    call sus_main("P-Put a curse on me?!!","open","wide","worried","wide")

    call ast_chibi(action="wand_casting",xpos="530",ypos="base")
    call sus_main("No! Professor, do someth--","scream","wide","worried","mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    hide screen susan_main
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans="hpunch")

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi(action="wand_imperio",xpos="530",ypos="base")
    with hpunch
    pause.8

    call play_music("trance")
    call sus_main("W-what are you-","open","wide","worried","wide")
    call nar("Susan's eyes flicker and a blank expression spreads across her face.")
    call sus_main("-doing...","upset","base","base","up")
    call sus_main("...","upset","narrow","base","up")

    call ast_chibi(action="wand",xpos="530",ypos="base")
    call ast_main("OK, so what should we do now?","grin","base","angry","mid",xpos="close",ypos="base")
    call ast_main("We could do whatever we want [ast_genie_name]!","open","base","base","R")
    m "How about we have her take her clothes off?"
    call ast_main("All of them?!","clench","base","worried","mid")
    m "What? Didn't that work last time?"
    g9 "Maybe she secretly wants to be a exhibitionist!"
    call ast_main("I only made her take her top off.","open","base","base","mid")
    g9 "Then there you go!"
    call ast_main("OK...","smile","base","base","L")
    call ast_main("Susan, are you listening?","open","closed","base","mid")
    call sus_main("Yes...","upset","narrow","worried","up")
    call ast_main("Good, I want you to pay attention.","open","base","base","L")
    call sus_main("...","base","narrow","base","up")
    call ast_main("And...","base","narrow","base","R")
    call ast_main("Wait a second... [ast_genie_name], what's the point if it's just you and I who see it?","annoyed","base","base","mid")
    g9 "It's the perfect place to start."
    m "Now tell her to lift up her top..."
    call ast_main("Very well, [ast_genie_name]...","clench","base","base","L")
    call ast_main("Susan, I want you to show us your...{w} your...{w} Show us your boobs!","clench","base","base","L")
    call sus_main("...","base","narrow","base","mid")

    call play_sound("gulp")
    call sus_main("*gulp*","upset","closed","worried","down")

    call play_sound("gulp")
    g4 "*Gulp!*"

    hide screen susan_main
    $ susan_wear_top = False
    call update_sus_uniform
    call sus_main("","upset","closed","worried","mid")
    pause.5

    m "Oh no, Miss Bones!"
    g9 "What are you doing?!"
    hide screen bld1
    with d3
    pause.8

    call gen_chibi("jerking_off_behind_desk")
    pause.5

    call ast_main("...","annoyed","narrow","base","mid")
    call sus_main("I-I-I'm sorry, Professor Dumbledore, I don't know what's come over me...","open","narrow","worried","down")
    call sus_main("I'm Sorry you have to see this...","upset","closed","base","mid")
    call ast_main("See what Susy?","grin","narrow","angry","mid")
    call sus_main("My gross boobs...","open","closed","worried","mid")
    call ast_main("(I knew they were gross!)","grin","base","angry","L")
    call sus_main("Please Sir--","open","narrow","worried","mid")
    call sus_main("Don't think less of me...","upset","closed","worried","mid")

    hide screen susan_main
    $ susan_wear_bra = False
    call update_sus_uniform
    call sus_main("","upset","closed","worried","mid")
    call ctc

    g4 "{size=+10}Nice!{/size}"
    call ast_main("Sir!","scream","closed","angry","mid")
    m "What? You can't blame me for this!"
    call ast_main("I thought we we're doing this so I could cast the spell more successfully","clench","narrow","angry","mid")
    call ast_main("(Please stop...)","annoyed","narrow","angry","R",cheeks="blush")
    m "Don't you think her breasts are pretty?"
    call ast_main("{b}No!{/b} they're huge and soft and squishy and, and, and,... gross!","clench","closed","angry","mid")
    g9 "You're right about them looking huge and soft..."
    call ast_main("Sir!","clench","narrow","angry","mid")
    call sus_main("Did I do something wrong?","upset","narrow","worried","R")
    call ast_main("Oh shut up, [ast_susan_name]!","scream","base","angry","L")
    call sus_main("[ast_susan_name]!? W-why are you always being so mean to me?","open","wide","worried","wide")
    call ast_main("Pfft... you know...","annoyed","narrow","angry","R")
    call sus_main("A-... Are you just going to let her say that, s-sir?","scream","base","angry","mid")
    g4 "What's that?"
    m "I was a little...{w=0.4} *ugh*... distracted..."

    call nar(">You keep stroking your rock-hard cock whilst marvelling at Susan's heaving chest.")
    g4 "(So big, soft and squishy...)"
    call sus_main("Sir, what are you?-","upset","base","worried","down")
    call ast_main("Alright, I think you're enjoying this a little too much!","clench","base","angry","mid")
    m "Just give me a minute..."
    pause.2

    call play_music("stop")
    call hide_characters
    call ast_chibi("reset","530","base")
    hide screen bld1
    with fade
    pause.8

    call ast_main("","annoyed","base","angry","R")
    call sus_main("W-w-what...","open","base","base","up")

    call nar(">Susan's eyes flicker once more as the blank expression spreads across her face.")

    call gen_chibi("sit_behind_desk")
    with d3
    pause.1

    call play_music("astoria_theme")
    g4 "(Damn it! Why did she do that?)"
    call sus_main("...","upset","base","worried","down")
    call ast_main("Put your clothes on, Susy.","smile","base","base","mid")
    call sus_main("...","upset","narrow","worried","mid")

    hide screen susan_main
    $ susan_wear_bra = True
    call update_sus_uniform
    call sus_main("","upset","narrow","worried","mid")
    pause.5
    call nar("Susan begins dressing herself in silence...")

    hide screen susan_main
    $ susan_wear_top = True
    call update_sus_uniform
    call sus_main("","upset","narrow","base","mid")
    pause.5
    call nar("Her eyes unfocused, staring blankly into space.")

    m "Aww... why'd you do that?"
    call ast_main("You were getting too excited, old man.","clench","base","angry","mid")
    m "So what?"
    call ast_main("How am I going to get any better if you keep distracting me!","annoyed","narrow","angry","R")
    m "Couldn't you at least make her dance or something..."
    call ast_main("We could do that...","annoyed","base","base","L")
    m "Then why don't we?"
    call ast_main("Because it's boring!","annoyed","narrow","base","ahegao")
    call ast_main("I want to do something fun!","open","closed","base","mid")
    m "Ugh... fine..."
    call ast_main("But not today...","annoyed","base","base","mid")
    call ast_main("I should put bessy here back in her barn before people start to notice.","grin","base","angry","L")
    call sus_main("(Hmm...)","upset","wide","worried","wide")
    m "Alright..."
    call ast_main("Just call me for the next practice session!","smile","narrow","base","mid")
    m "Will do."
    m "Oh, please take Susan to professor Tonks' to be obliterated..."
    call ast_main("Obliviated?","base","base","worried","mid")
    m "Yeah, that!"
    call ast_main("Can't you do it?","annoyed","base","base","mid")
    m "My wand casting hand is a bit tired for some reason..."
    call ast_main("Fine...","annoyed","base","worried","R")
    if daytime:
        call ast_main("Have a nice day, Sir!","grin","closed","base","mid")
        m "You too..."
    else:
        call ast_main("Night then, Sir!","grin","closed","base","mid")
        m "Good night..."

    call ast_walk("door","base", speed=2.5)
    pause.2
    call ast_chibi("stand","door","base", flip=False)
    with d3
    pause.5

    call ast_main("Come on Susy, time to give professor Tonks a visit.","open","base","base","mid", ypos="head")
    call sus_main("...","upset","narrow","worried","down", ypos="head")

    call sus_walk(action="leave", speed=2.5)

    call ast_main("(This is so much fun!)","grin","closed","base","mid")

    call play_sound("door")
    call hide_characters
    call ast_chibi("hide")
    hide screen bld1
    with d3
    pause.5

    call bld
    m "(Maybe leaving Tonks out of this was a bad idea...{w} Nah... {w=0.3} She's had her fun...)"

    # Increase affection once (this is the first event)
    if ag_se_imperio_sb.counter == 1:
        $ ast_affection += 1

    jump end_ag_se_imperio_sb


label ag_se_imperio_sb_E2:
    call ast_main("Let's try something else this time!","grin","narrow","base","mid", xpos="close", ypos="base", trans="fade")
    g9 "Of course!"
    call ast_main("Great, I can't wait to see the look on Susan's dumb face...","grin","closed","base","mid")
    m "Let me just bring her up here."

    call play_music("stop")
    m "..."
    call ast_main("...","annoyed","base","base","R")

    call hide_characters
    call ast_chibi("stand","530","base")
    hide screen bld1
    with d3
    call sus_walk(action="enter", xpos="desk", ypos="base", speed=2.5)
    pause.2


    call sus_main("You wanted to see me, [sus_genie_name]?","open","base","worried","mid", xpos="right", ypos="base")
    call sus_main("Astoria? Why are you here?","open","base","worried","R")

    call play_music("astoria_theme")
    call ast_main("Oh... no reason...","annoyed","base","base","down", xpos="base", ypos="base")
    call sus_main("Is there something wrong, Professor?","upset","base","worried","mid")
    m "As a matter of fact there is..."
    call sus_main("R-really? Is this about me returning my books to the library a day late?","open","wide","base","wide")
    call sus_main("I swear it won't happen again!","open","closed","worried","mid")
    m "What? No, I'm afraid there's an issue with your uniform..."
    call sus_main("Oh... Is it because I'm not wearing the school robe?","open","base","worried","down")
    call sus_main("I can wear it from now on if you like!","upset","base","base","mid")
    m "Actually, Wearing too many clothes is the problem."
    call sus_main("W-w-what???","scream","wide","base","wide")
    call sus_main("You can't be serious sir!","open","wide","base","mid")
    m "I am, Ms Bones..."
    g9 "Hiding away those glorious milk duds of yours is a serious offence!"
    call sus_main("","open","wide","base","wide")
    call ast_main("(Pffft, gloriously gross)","annoyed","base","angry","R")
    call sus_main("P-professor Dumbledore! Why would you want me to do s-something like that!","scream","base","angry","mid", trans="hpunch") #Perhaps she should be a bit intrigued =Blush

    call ast_chibi(action="wand",xpos="530",ypos="base")
    call sus_main("I think I better go...","upset","closed","worried","mid")
    call ast_chibi(action="wand_casting",xpos="530",ypos="base")
    call ast_main("","grin","base","angry","L")
    pause.5

    # Astoria casts imperio.
    stop music fadeout 2.0
    hide screen susan_main
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans="hpunch") # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi(action="wand_imperio",xpos="530",ypos="base")
    with hpunch
    pause.8

    call play_music("trance")
    call sus_main("...","upset","narrow","base","mid", xpos="right", ypos="base")
    call ast_main("*ha-ha-ha-ha!*","grin","closed","base","mid", xpos="base", ypos="base")
    call ast_main("Her face was priceless when you said milk duds...","grin","base","base","L")
    m "You liked that?"
    call ast_main("Of course! Anything to bring Bessy here down a peg.","smile","base","base","L")

    call ast_chibi(action="wand",xpos="530",ypos="base")
    call ast_main("So what should we make her do today, [ast_genie_name]?","smile","base","base","mid")
    m "Something fun, perhaps?"
    call ast_main("*Hmmm*...","annoyed","narrow","base","R")
    m "Maybe something a little more... adventurous?"
    call ast_main("You mean like making her show you her milk duds?","upset","narrow","base","mid")
    m "Well if you insist..."
    call ast_main("*ugh*... you're such a filthy pervert!","clench","narrow","angry","mid")
    m "We can do something else if you-"
    call ast_main("I didn't say no...","upset","closed","base","mid")
    m "Oh... well how about you make it so-"
    call ast_main("I get to choose, [ast_genie_name]!","scream","closed","angry","mid")
    m "What? Why?"
    call ast_main("Because it's my spell and my wand!","open","narrow","angry","mid")
    call ast_main("Not to mention you'd probably do something over the top and gross...","open","narrow","angry","R")
    m "Probably..."
    m "So what's your plan?"
    call ast_main("Just wait and see old man!","clench","narrow","angry","mid")
    call ast_main("Susan, can you hear me?","open","closed","base","L")
    call sus_main("Yes...","upset","narrow","base","up")
    call ast_main("You now have an uncontrollable urge to take your top off, OK?","open","closed","base","mid")
    call sus_main("Okay...","upset","narrow","worried","mid")
    call ast_main("Awesome! Now act like you normally would, [ast_susan_name]!","grin","base","angry","L")
    call sus_main("...","upset","narrow","base","up")

    hide screen blktone
    call nar(">The blank expression slowly fades from Susan's eyes...")
    call sus_main("ugh...","upset","narrow","base","up")
    call sus_main("What happened?","open","narrow","worried","mid")
    call ast_main("Nothing Susy, Dumbledore was just explaining how your uniform wasn't up to scratch.","grin","base","base","mid")
    call sus_main("My uniform... You're right... Too many clothes...","open","narrow","worried","down")
    call sus_main("I need to take off my top...","open","base","worried","down")
    call ast_main("Mhmm, that's right, Susy... Why don't you show the old man here your gross boobs... Don't you think he's old?","grin","base","angry","mid")
    call sus_main("I... I suppose,...","upset","narrow","worried","L")
    call ast_main("That's right... Only a nasty slut would show her boobs to such a wrinkly old man...","grin","narrow","angry","L")
    m "Hey!"
    call ast_main("Quiet sir,... don't ruin my fun!","clench","narrow","angry","mid")
    m "Fine..."
    call sus_main("I-I'm not a slut...","upset","narrow","worried","down")
    call ast_main("Well I'm sure you'll be able to keep your top on then, [ast_susan_name].","open","closed","base","mid")
    call sus_main("I... There's something wrong sir!","open","base","worried","mid")
    call sus_main("I can't help it...","upset","narrow","worried","down")
    call ast_main("","grin","base","angry","L")
    pause.2

    hide screen susan_main
    $ susan_wear_top = False
    $ susan_wear_bra = False
    call update_sus_uniform
    call sus_main("","upset","closed","worried","mid")
    call ctc

    g4 "Nice!"
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("jerking_off_behind_desk")
    pause.8

    call ast_main("[ast_genie_name]! Are you touching yourself?","scream","base","base","mid")
    m "Ugh... can you blame me?..."
    g4 "It's not every day you get to see a rack like this..."
    call ast_main("Well stop it! It's gross!","clench","narrow","angry","mid")
    m "Alri--"
    call sus_main("Please sir... it's too much!","open","closed","base","mid")
    call sus_main("It's bad enough that I can't help showing you my breasts...","open","closed","worried","mid")
    call ast_main("Wait...","smile","base","base","mid")
    call ast_main("Keep going, sir!","clench","narrow","angry","mid")
    m "What?"
    call sus_main("What?","scream","wide","base","mid")
    call ast_main("Well if bessy here hates it... Then I love it!","clench","narrow","angry","L")
    call ast_main("Besides, it's not like I can see anything under the desk.","open","closed","base","mid")
    call sus_main("(...)","upset","closed","worried","mid")
    m "So you're OK with this?"
    call ast_main("*Mhmm*... just don't expect me to touch it old man!","upset","narrow","angry","mid")
    call sus_main("W-why is this happening!","open","closed","base","mid")
    call ast_main("No one asked you, slut!","clench","narrow","angry","L")
    call sus_main("I am not a slut!","scream","closed","angry","mid")
    call sus_main("", "upset")
    call ast_main("Ha! You're standing here, letting old man dumbledore ogle your fat tits while he jerks his wrinkly old cock!","open","closed","base","mid")
    call ast_main("If that's not a slut then I don't know what is!","clench","narrow","angry","L")
    m "(There's no way Tonks would allow this, perhaps this was a good idea after all...)"
    call sus_main("I-- don't know why I'm doing this...","upset","narrow","worried","mid")
    call sus_main("You probably cursed me!","open","suspicious","angry","mid")
    call ast_main("Duh!","grin","narrow","angry","L")
    call sus_main("Well stop it!","open","base","angry","R")
    call ast_main("Nuh!","open","closed","base","mid")
    call sus_main("Please astoria...","upset","narrow","worried","down")

    call nar(">You start to zone out as the two girls argue, focusing on Susan's heaving bosom.")
    g4 "Ugh yeah... that's it..."
    call ast_main("You can leave once Dumbledore here's done.","open","closed","base","mid")
    call sus_main("What? you mean I have to wait until he...","open","base","worried","mid")
    call sus_main("This is unbelievable!","scream","base","angry","mid")
    call sus_main("I'm going to report both of you to the ministry of magic!","open","closed","angry","mid")
    call sus_main("My aunt is the head of the department of magical law enforcement you know!","open","base","angry","mid")
    call ast_main("yeah... I've met your creepy old aunt.","annoyed","narrow","base","R")
    call sus_main("What? Did you curse her too, you evil little witch?","open","wide","base","R")
    call ast_main("I wish...","annoyed","narrow","base","R")
    call sus_main("Well she's going to lock both of you away in azkaban!","open","closed","angry","mid")
    call sus_main("You'll never see me or anyone else again...","scream","closed","angry","mid")
    call ast_main("Yeah, sure!","grin","base","angry","L")
    call sus_main("Ugh! You're both sick!","open","narrow","angry","mid")
    g4 "Mmmm, keep shaking those tits of yours..."
    g4 "I'm almost there {b}slut!{/b}"
    call sus_main("I am not a {size=+10}slut!{/size}","scream","closed","angry","mid",trans="vpunch")
    call nar(">As Susan yells at the top of her voice, the effort causes her gigantic tits to rise and slap back together.")
    call sus_main("","open")

    g4 "{size=+10}HERE IT COMES!{/size}"
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("cumming_behind_desk")
    call cum_block
    g4 "{size=+10}AHHH... YESS!!!!{/size}"
    call ast_main("Woah... I didn't think you'd have that much in you, sir...","clench","base","base","mid")

    call sus_main("{size=+10}Hmph! I hope you Enjoy azkaban, perverts!{/size}","scream","narrow","angry","down")
    call sus_main("","upset")

    call ast_main("","annoyed","narrow","base","R")
    call gen_chibi("cum_on_desk")
    pause.5

    call nar(">As you shoot your massive load Susan's leg twitches slightly...")

    call ast_main("Let's delve deeper shall we...","grin","narrow","angry","L")
    m "W-what?"
    call ast_main("Susy, can you hear me?","open","base","base","L")
    call sus_main("Yes...", "open")
    call sus_main("", "upset")
    call ast_main("She's just so easy to put under the spell...","base","narrow","worried")
    call ast_main("Nothing like Tonks, there's something wrong here...",eyes="base",pupils="R")
    m "W-what do you mean?"
    call ast_main("Quiet!","clench","base","base","mid")
    g4 "..."
    call ast_main("Susy, I want you to speak the truth and nothing but the truth, okay?","open","base","base","L")
    call sus_main("Okay...","open")
    call sus_main("", "upset")
    m "What are you?-"
    call ast_main("...","upset","base","base","mid") # Stares at you
    g4 "..."
    call ast_main("Susy, do you like baring your chest to the headmaster?","open","base","base","L")
    call ast_main("Are you just another one of those closeted sluts?","clench","narrow")
    m "(Oh shit...)"
    call sus_main("I...I...","open","base","worried")
    call ast_main("Tell me!","scream")
    call ast_main("","clench")
    call sus_main("I...{w=0.8} I do!","open","closed")
    call ast_main("I knew it!","scream","narrow","angry") # Angry
    call sus_main("","upset","narrow")
    call ast_main("Where's the fun if she's enjoying it!","clench",pupils="mid")
    m "*Errr-*"
    call ast_main("I want to humiliate this cow, but she's just another slut!","scream")
    m "A closeted slut..."
    call ast_main("Excuse me?",mouth="open",eyebrows="worried")
    call ast_main("",mouth="upset")
    m "Miss Greengrass... is there any other \"Hufflepuff\" students you know of selling favours?"
    call ast_main("Why would I know or care what \"Hufflepuffs\" are doing?",mouth="clench")
    m "Just because she enjoys it doesn't mean it's not humiliating for her..."
    m "What would the other \"Hufflepuffs\" think of her if she knew what you have her do?"
    call sus_main("...", "upset","narrow","base","down")
    call ast_main("What do you mean?","upset","base","base")
    m "Ask her the right questions..."
    call ast_main("...",eyes="closed")
    call ast_main("Susy!","open","narrow","base","L")
    call ast_main("","base")
    call sus_main("...",pupils="mid")
    call ast_main("Are you ashamed of what you've done?","open","base")
    call ast_main("","base")
    call sus_main("Yes...","open","base")
    call sus_main("!!!","grin","eager",pupils="L") # Smiles
    call ast_main("Would your house think less of you if they knew what you're doing here?","grin")
    call sus_main("Yes...",pupils="R")
    m "Well, there you go!"
    call ast_main("*ha-ha-ha!*","smile")
    m "(Nailed it...)"
    m "So, are we continuing with the training?"
    call ast_main("Of course we are! I want to be able to put every student at the school under my spell!",eyebrows="angry",pupils="mid")
    call ast_main("",eyes="closed")
    g4 "..."
    m "Then wouldn't the reason for Susan's shame go away as well?"
    call ast_main("And they will all be under my comm-","scream","closed")
    call ast_main("Oh yeah, that's true...","open","base","base","mid")
    call ast_main("...","annoyed")

    call ast_main("Susy, put your clothes back on.","grin","base","base","L")

    call sus_main("","base","narrow","base","mid")
    pause.5
    call nar("Susan begins dressing herself in silence...")

    hide screen susan_main
    $ susan_wear_top = True
    $ susan_wear_bra = True
    call update_sus_uniform
    call sus_main("","base","narrow","base","mid")
    pause.5

    call play_music("stop")
    call hide_characters
    call ast_chibi("reset","530","base")
    call ast_walk("door","base", speed=2.5)
    pause.2
    call ast_chibi("stand","door","base", flip=False)
    with d3
    pause.5

    call play_music("astoria_theme")
    call ast_main("Come on Susy, time to give professor Tonks another visit","open","base","base","L", ypos="head")
    call sus_main("...","upset", ypos="head")

    call sus_walk(action="leave", speed=2.5)

    if daytime:
        call ast_main("See you, [ast_genie_name]!","grin","closed","base","mid")
        m "..."
    else:
        call ast_main("Good night then, Sir!","grin","closed","base","mid")
        m "Good night."

    call play_sound("door")
    call hide_characters
    call ast_chibi("hide")
    hide screen bld1
    with d3
    pause.5

    # Increase affection once (this is the second event)
    if ag_se_imperio_sb.counter == 2:
        $ ast_affection += 1

    jump end_ag_se_imperio_sb


label ag_se_imperio_sb_E3:
    call ast_main("","smile","base","base","mid",xpos="close",ypos="base",trans="fade")
    m "Ready for another go with the curse?"
    call ast_main("You bet [ast_genie_name]! I can't wait to see the look on Susy's stupid face this time!","grin","narrow","angry","down")
    m "Shall I bring her up here?"
    call ast_main("Do you even need to ask?","smile","narrow","base","mid")
    m "I suppose not..."

    call play_music("stop")
    call hide_characters
    call ast_chibi("stand","530","base")
    hide screen bld1
    with d3
    call sus_walk(action="enter", xpos="desk", ypos="base", speed=2.5)
    pause.2

    call sus_main("You wanted to see me sir?","open","base","worried","mid", xpos="right", ypos="base")
    call sus_main("Astoria?...","upset","base","worried","R")
    call sus_main("What are you doing here?","upset","narrow","worried","R")

    call play_music("astoria_theme")
    call ast_chibi(action="wand",xpos="530",ypos="base")
    call ast_main("Yeah yeah, whatever...","open","base","base","R", xpos="base", ypos="base")

    call ast_chibi(action="wand_casting",xpos="530",ypos="base")
    call sus_main("Well I'm not sure why I was brought here...","open","base","worried","mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    hide screen susan_main
    call ast_main("IMPERIO!{w=0.8}{nw}","scream","base","angry","mid", trans="hpunch")

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call play_sound("spell")
    call ast_chibi(action="wand_imperio",xpos="530",ypos="base")
    with hpunch
    pause.8

    call play_music("trance")
    call sus_main("Wait, wha-","open","wide","base","wide")
    m "Couldn't even wait this time?"
    call ast_main("Quiet old man.","open","narrow","angry","mid")
    call ast_chibi(action="wand",xpos="530",ypos="base")
    call ast_main("Susan, I want you to keep listening to my commands and act normally as you take your top off!","smile","narrow","angry","L")
    g4 "!!!"

    hide screen susan_main
    $ susan_wear_top = False
    call update_sus_uniform
    call sus_main("","upset","base","worried","mid")
    pause.5

    call nar(">As Susan begins to talk her arms seem to have a mind of their own, quietly removing her top as she speaks.")
    call sus_main("Was this about the l-library books that I returned a day late s-sir?","open","narrow","worried","down")
    call sus_main("I promise it won't happen again...","upset","closed","worried","mid")
    g9 "Don't you worry about the books, Ms Bones!"
    call sus_main("T-Then what is it?","base","narrow","base","mid")
    call ast_main("Just get those milk bags out!","clench","narrow","angry","L")

    hide screen susan_main
    $ susan_wear_bra = False
    call update_sus_uniform
    call sus_main("","base","base","base","mid")
    pause.5

    g4 "(!!!)"
    call ast_main("Maybe it's because of you showing off your gross boobs?","annoyed","base","base","R")
    call sus_main("Astoria! H-how can you say something so rude! I'd never...","open","closed","angry","mid")
    call sus_main("","upset","wide","worried","down",trans="hpunch")
    pause.8
    call nar(">Susan's eyes drift down to her exposed chest.")
    call sus_main("WHAT?!?!?","scream","wide","worried","down")
    call sus_main("I'm so sorry, professor Dumbledore!","upset","closed","worried","mid")
    call sus_main("I don't know what's come over me!","open","closed","base","mid")
    call ast_main("Maybe it's just because you're a nasty slut!","annoyed","base","base","L")
    call sus_main("I am not a {size=+10}slut{/size}, Astoria!","scream","closed","angry","mid")
    call ast_main("Pfft... we both know that's not true... We both know you love showing your headmaster those oversized bean bags of yours...","annoyed","base","base","R")
    call sus_main("I-- don't know why this is happening...","open","wide","worried","wide")
    call sus_main("You must have cursed me!","scream","narrow","angry","R")
    call ast_main("Bingo!","grin","base","angry","L")
    call sus_main("Professor! You h-have to stop her!","scream","wide","base","mid")
    hide screen astoria_main
    with d3
    m "Ugh... I'm afraid not Susan..."
    call ast_main("","grin","narrow","angry","L",xpos="base",ypos="base")
    call sus_main("WHAT?!","scream","wide","base","wide")
    call sus_main("W-w-w-well my aunt will just send you-","upset","narrow","angry","mid")

    call nar(">Astoria strengthens her grip on her wand, increasing the effect the spell has on Susan.")

    call sus_main("to ...azkaban...","open","narrow","base","up")
    call sus_main("...","upset","narrow","base","mid")
    call ast_main("Alright... that'll shut her up...{w} what should we make her do this time, [ast_genie_name]?","grin","base","base","mid",xpos="close",ypos="base")
    m "Hmmm... Are you actually going to let me choose this time or are you just asking to be annoying?"
    call ast_main("Hey! I am not annoying!","scream","closed","angry","mid",trans="hpunch")
    m "Well are you going to let me pick then?"
    call ast_main("Fine... Just nothing too disgusting!","clench","narrow","base","mid")
    call ast_main("Or boring... that'd be even worse!","upset","narrow","angry","mid")

    m "Alright well, first things first..." #I'll add a menu here with more options once art assets are drawn for them

    hide screen blktone
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("jerking_off_behind_desk")
    pause.8

    show screen bld1
    call nar(">Your hands sneak under your desk and around your engorged cock.")
    g9 "That's better..."
    call ast_main("(...)","annoyed","narrow","angry","R")
    m "What?"
    call ast_main("I told you not to be boring! We already did this last time!","open","closed","base","mid")
    g9 "If this is too boring, why don't you get her to suck me off?"
    call ast_main("Sir! I said it shouldn't be something disgusting...","clench","base","base","mid")
    call ast_main("I don't wanna have to see your nasty old cock!","clench","narrow","angry","R")
    m "Ugh... Fine... What do you want to do then?"
    call ast_main("Well seeing as how you asked...","open","closed","base","mid")
    call ast_main("Susy, are you listening?","open","narrow","base","L")

    show screen blktone
    call sus_main("yes...","upset","narrow","base","up")
    call ast_main("I want you to crawl under the headmaster's desk.","grin","base","base","L")
    m "I thought you didn't want her to suck me off?"
    call ast_main("Shut it, and stop being so disgusting!","scream","closed","angry","mid")
    call sus_main("...","upset","narrow","base","up")
    call ast_main("Now go, [ast_susan_name]!","grin","narrow","angry","mid")

    call hide_characters
    call sus_chibi("hide")
    hide screen blktone
    call blkfade

    call nar("Susan slowly starts walking around your desk before obediently crawling under.")
    pause.5
    hide screen blkfade
    call ast_main("","smile","base","base","down",xpos="mid",ypos="base",trans="fade")
    hide screen bld1
    call ctc

    show screen blktone
    call ast_main("And you're not allowed to come out until I say so.","open","closed","base","mid")
    sus "yes..."
    call ast_main("And if you actually are just a slut then let that slut out! Show us you really love it!","clench","narrow","base","down")
    sus "...Love it?"
    sus "I love it..."
    call ast_main("Good!","clench","base","angry","L")
    m "Isn't that a little much?"
    call ast_main("Pfft! That's rich coming from you sir!","annoyed","narrow","base","mid")
    call ast_main("If it was up to me she'd be clucking like a chicken right now!","annoyed","narrow","angry","R")
    call ast_main("Not doing nasties with her mouth!","clench","narrow","base","down")
    m "Fair enough..."
    call ast_main("But you've helped me so take this as a reward...","annoyed","narrow","base","mid")
    call ast_main("Now, make sure to give Susan a reward for being so obedient as well...","open","closed","angry","mid")
    m "You don't have to tell me twice!"
    call nar(">You renew your efforts, encouraged by the image of the well-endowed redhead hidden under your desk.")
    call ast_main("And susy...","open","narrow","base","down")
    sus "Yes..."
    call ast_main("Time for you to wake up...","grin","narrow","angry","down")
    sus "..."

    call play_music("susan_theme")
    hide screen blktone
    hide screen bld1
    with d3
    pause.5
    show screen bld1
    with hpunch
    sus "W-w-what's happening?"
    call play_sound("kick")
    with vpunch
    pause.2
    sus "Ouch..."
    pause.5
    sus "Where am I?"
    call ast_main("Don't you remember crawling under your headmaster's desk, begging him to jerk his nasty old cock for you?","open","closed","base","mid")
    with hpunch
    sus "WHAT?"
    sus "I'd never do something like that!"
    call ast_main("Really? Because it sure looks like you did...","grin","base","base","R")
    sus "I--"
    sus "I don't know why..."
    call ast_main("If you don't like it down there, why don't you just hop out then?","annoyed","base","base","R")
    sus "I can't!"
    call ast_main("Really? why's that, susy?","grin","narrow","base","down")
    sus "I don't know... I just can't!"
    call ast_main("Hmmm... it must be because you're such a nasty little slut then...","open","closed","base","mid")
    with hpunch
    sus "I- I am not!"
    call ast_main("Are you sure?","grin","base","angry","down")
    sus "I... Y-yes..."
    call ast_main("because it sure doesn't look like that...","open","narrow","base","down")
    call ast_main("In fact, it looks like you're the nastiest little slut this school has ever seen!","grin","closed","base","mid")
    g4 "That's it, Astoria..."
    sus "Professor... {b}please...{/b}"
    call ast_main("Please what, Susan?","open","closed","base","mid")
    call ast_main("Please stop?","open","narrow","base","down")
    call ast_main("Or please coat me in cum?","clench","narrow","angry","down")
    with hpunch
    sus "ASTORIA!"
    call ast_main("Answer the question, Susy...","open","base","base","mid")
    sus "..."
    sus "Please sir..."
    sus "{size=-3}Coat{/size} {size=-3}me{/size} {size=-3}in{/size} {size=-3}your{/size} {size=-3}cum...{/size}"
    call ast_main("I knew it!","scream","base","angry","L")
    call ast_main("You're a dirty little slut after all aren't you!","clench","narrow","angry","down")
    sus "I am not! I don't know why I'm down here!"
    call ast_main("Alright then... if you're such a good girl...","open","closed","base","mid")
    call ast_main("Why don't you tell me what it's like down there?","smile","narrow","base","down")
    sus "Down here?"
    sus "Under professor Dumbledore's desk?"
    call ast_main("Mhmm... I bet it's nasty down there...","clench","narrow","angry","down")
    call ast_main("It probably smells gross with all the yucky cum he shoots against that desk of his...","open","base","base","R")
    call ast_main("Not to mention his big, smelly old cock...","annoyed","narrow","base","ahegao")
    m "Ahem..."
    call ast_main("Quiet, sir!","clench","narrow","angry","mid")
    call ast_main("So go on, Susy... tell me what it's like...","open","closed","base","mid")

    sus "It... It's..."
    call nar(">you hear Susan take a deep breath before she begins to speak.")
    sus "{size=+10}It's incredible!{/size}"
    call ast_main("","grin","narrow","angry","mid")
    sus "Everything about it is fantastic!"
    call ast_main("","smile","base","base","mid")
    sus "The cum stains on the back of the desk..."
    call ast_main("","clench","narrow","base","mid")
    sus "The thick smell of semen in the air..."
    call ast_main("","clench","narrow","base","R")
    sus "The way Dumbledore's stroking his {b}cock{/b}..."
    call ast_main("","smile","narrow","angry","R")
    sus "That cock... that's the best part..."
    sus "I just want to--"
    call ast_main("(Eeeegh--...)","scream","closed","angry","mid",trans="hpunch")

    sus "..."
    call nar(">You hear Susan's words trail off into nothingness as she takes another breath...")
    sus "I wish I could live down here! Is that what you wanted to hear you evil witch?!"
    call ast_main("Almost...","grin","narrow","base","down")
    call ast_main("I want you to tell me the truth... say you're a slut...","grin","base","angry","mid")
    call ast_main("Then I'll let you go...","open","closed","base","mid")
    sus "Really?"
    sus "Alright..."
    sus "{size=-5}I'm a...{/size} {size=-3}slut...{/size}"
    call ast_main("Hmmm, I'm not sure I heard anything... What about you, sir?","annoyed","base","base","R")
    m "Ah...{w=0.3} almost..."
    call ast_main("Go on Susy... one more time...","smile","narrow","base","down")
    with hpunch
    sus "I'm a slut, OK!"
    g4 "Ah... YES..."
    sus "I'm a nasty slut who crawled under her headmaster's desk and--"

    g4 "HERE IT COMES SLUT!"
    hide screen bld1
    call gen_chibi("cumming_behind_desk")
    call cum_block
    sus "No wait! Astoria, you said I could go--"
    call cum_block
    g4 "ARGHHHH!!!"
    call nar("Susan's sudden yelps prove too much for you as your cock begins to fire off an immense load onto Susan's face...")
    g4 "HERE IT IS SLUT!!!"
    call cum_block
    sus "..."

    call ast_main("That's it, [ast_genie_name]! Make sure you get it all out...","grin","narrow","angry","mid")
    g4 "Ahhh... don't worry about that..."
    call nar(">You give your cock a few final pumps, working out the last of your load onto Susan's waiting face...")

    call gen_chibi("cum_on_desk")
    pause.5
    g4 "There we go..."
    call ast_main("Nice work, [ast_genie_name]...","open","closed","base","mid")
    call ast_main("You can come out now, Susy...","smile","narrow","base","down")
    sus "..."

    call play_music("stop")
    hide screen astoria_main
    call blkfade

    call nar(">Susan slowly crawls out from under your desk...")

    call sus_chibi("stand","desk","base")
    call ast_chibi("reset","530","base")
    $ susan_face_covered = True
    hide screen blkfade
    call sus_main("","upset","narrow","worried","L",xpos="right",ypos="base",trans="fade")
    call ctc

    call play_music("astoria_theme")
    call ast_main("Oh my god! He absolutely covered you!","scream","base","base","mid",xpos="base",ypos="base")
    call sus_main("...","upset","narrow","base","L")
    call ast_main("I didn't know you had it in you, sir!","clench","base","base","mid")
    call ast_main("Nice work!","annoyed","base","base","mid")
    m "Thanks..."
    call ast_main("And Susy... that look suits you.","grin","narrow","angry","L")
    call sus_main("Are you done, Astoria?","open","narrow","base","L")
    call ast_main("Yes, you can get dressed.","smile","narrow","base","L")

    call nar(">Susan slowly wipes the cum from her face as she gets dressed.")

    hide screen susan_main
    $ susan_face_covered = False
    call sus_main("I hope you two are happy...","upset","narrow","base","down")

    $ susan_wear_top = True
    $ susan_wear_bra = True
    call update_sus_uniform

    if daytime:
        call ast_main("We're going to be late for classes, Susy!","annoyed","narrow","base","R")
        call ast_main("Let's head to Tonks' study, shall we?...","smile","narrow","base","R")
        sus "..."
        m "See ya..."
        call ast_main("Until next time, [ast_genie_name]!","grin","closed","base","mid")
    else:
        call ast_main("It's getting a bit late Susy, let's head to Tonks' study...","annoyed","narrow","base","R")
        sus "..."
        m "Ugh... uhm... good night."
        call ast_main("Good night, [ast_genie_name]!","grin","closed","base","mid")

    call play_sound("door")
    call hide_characters
    call ast_chibi("leave")
    call sus_chibi("leave")
    hide screen bld1
    with d3
    pause.8

    call bld
    m "(That girl is even worse than me...)"

    $ susan_wardrobe_unlocked = True
    if ast_affection < 24: # Save compatibility
        $ ast_affection = 24

        $ TBA_message("This concludes all events for Susan and Astoria as of version %s." % title_version)
        $ TBA_message("Susan's wardrobe has been unlocked!")
        $ TBA_message("Astoria's affection stat has been maxed out.\nYou can now use all of her wardrobe options.")

    # Increase affection once (this is the third event)
    #if ag_se_imperio_sb.counter == 3:
    #    $ ast_affection += 1

    jump end_ag_se_imperio_sb





#humiliate self for genie and astoria
#training labels are on the other page.

label hornify_spell_1: #first level hornify spell
    #Start grinding her hips in front of genie
    m "Ready to try out a brand new spell?"
    call ast_main("Probably almost as ready as you are to see me use it, Sir!","smile","narrow","angry","mid")
    m "Well if it's half as exciting as what the name suggests..."
    call ast_main("Then we'll have Susan begging for your dirty old cock in no time!","grin","narrow","angry","mid")
    call ast_main("Maybe I should get a magical photo of her covered in cum!","smile","base","worried","mid")
    call ast_main("Imagine that in the school paper!","grin","narrow","angry","mid")
    m "Magic photos?"
    call ast_main("Haven't you ever read a newspaper, sir? I thought that's all old people like you did!","upset","narrow","angry","mid")
    call ast_main("I wonder if I could take it just as you shoot it all over her...","smile","base","worried","L")
    call ast_main("Imagine that for a front page scoop!","grin","narrow","narrow","mid")
    m "I'm not sure they'd run that story some how..."
    call ast_main("You're the headmaster aren't you, sir? Make them run it!","smile","narrow","angry","mid")
    m "Let's just focus on your magic for the moment, leave the journalism for later."
    call ast_main("Hmph!", "annoyed", "narrow","angry", "R")
    call ast_main("If you want me to focus on magic then bring those boobs on legs up here so I have someone to practice on!", "annoyed", "narrow","angry", "mid")
    m "Couldn't have said it better myself..."
    call ast_main("Hang on, wait!","smile","base","narrow","mid")
    ">Astoria runs around your desk and hops up on your lap..."
    call ast_main("There, ready!","smile","happyCl","base","mid", flip=True, xpos=100)
    m "..."
    ">Without further ado you summon the well-endowed, Hufflepuff to your hallowed office."
    call sus_main("You wanted to see me, sir?","base","worriedCl","worried","down")
    ">Without even consciously realizing, Susan calmly removes her top and bra, bearing her magnificent breasts to you and Astoria..."
    m "mmm, that I did..."
    ">The sight of Susan's milky tits rapidly cause your cock to spring to life, straining against the weight of Astoria on your lap."
    call sus_main("Ast-","open","wide","worried","mid")
    call ast_main("Sir! We haven't even started yet!","smile","angry","base","R")
    m "Don't blame me for this, [astoria_name]!"
    call ast_main("I do! I expect you to wait until we start...", "annoyed", "happyCl","base", "R")
    call sus_main("Excuse me!","scream","worriedCl","angry","mid")
    call sus_main("Why are you sitting on Dumbledore's lap Astoria?","open","suspicious","angry","mid")
    call sus_main("And what are you starting?","open","narrow","worried","mid")
    m "We brought you up here to help with a magic experiment."
    call sus_main("Really?","open","wide","worried","mid")
    call sus_main("B-but that still doesn't explain why Astoria is-","open","suspicious","worried","mid")
    call ast_main("IMPERIO!","scream","closed","angry","mid")
    ">With a puff of golden smoke Astoria's wand goes off, entrancing the poor redhead once more..."
    m "Hey, Isn't that the old spell?"
    call ast_main("Of course it is sir! Can't you hear things at all?","pout","narrow","angry","R")
    call ast_main("I cast it because I wanna change some stuff about bessy here.","smile","angry","narrow","mid")
    call ast_main("I think she can still cast spells at us if she wants...", "annoyed", "narrow","narrow", "mid")
    call ast_main("Plus I wanna be able to boss her around in class!","grin","happyCl","base","mid")
    call ast_main("So listen up Susan!","open","closed","angry","mid")
    call sus_main("Yes...","open","base","worried","empty")
    call ast_main("From now on, you have to do whatever I say, whenever I say, OK?","open","narrow","narrow","mid")
    call sus_main("Yes...","open","base","worried","empty")
    call ast_main("Awesome!","grin","happyCl","base","mid")
    call ast_main("And you can't ever cast a spell on me or the headmaster!","open","narrow","angry","mid")
    call sus_main("Yes...","open","base","worried","empty")
    call ast_main("And you aren't allowed to play with yourself unless I say!","open","closed","angry","mid")
    call sus_main("Yes...","open","base","worried","empty")
    m "What was that for?"
    call ast_main("Can you imagine how much a big boobed bimbo like Bessy here probably plays with herself?", "upset","narrow","angry","R")
    call ast_main("I'm just doing her a favour by giving her some more free time...","smile","narrow","narrow","mid")
    m "..."
    call ast_main("OK, all done, you can go back to normal now Susy!","open","happyCl","base","mid")
    ">The colour rushes back into Susan's eyes as she snaps back to life."
    call sus_main("-sitting on your lap!","open","suspicious","worried","mid")
    call ast_main("I'm sitting here because the headmaster refuses to get any comfy furniture!","pout","closed","narrow","mid")
    ">You feel astoria's butt adjust ever so slightly, causing the barest bit of friction to your cock..."
    m "Ugh... th-that's right..."
    call sus_main("Ok... so what's this experiment you needed me to help with?","upset","narrow","worried","mid")
    call ast_main("The headmaster and I want to test the effects of a new spell I just learned!","grin","narrow","narrow","mid")
    call ast_main("And we needed someone to cast it on...","grin","narrow","angry","mid")
    call sus_main("What? I-I'm not so sure about that... What does it do?","open","suspicious","worried","wide")
    call ast_main("We're not really sure... All we know is that I have to target it somewhere on your body...","smile","angry","worried","mid")
    call ast_main("Guess where?","grin","narrow","angry","mid")
    call sus_main("You don't mean...","open","wide","worried","wide")
    call sus_main("I don't think I want to help with this experiment Dumbledore! I'm going to leave now...","open","worriedCl","worried","mid",flip=True)
    ">Susan turns to leave, but is compelled by Astoria's previous imperio to be unable to leave until excused..."
    call sus_main("I can't... I can't leave!","upset","worriedCl","worried","wide")
    call ast_main("We know! Just get back here and let us cast the spell!", "annoyed", "narrow","base", "R")
    call sus_main("...","upset","narrow","worried","empty")
    ">Susan begrudgingly walks back in front of your desk, sullenly standing before you and Astoria."
    call sus_main("Whatever you two have done, my aunt-","scream","closed","angry","mid")
    call ast_main("Shhh!","clench","narrow","angry","mid")
    call sus_main("...","upset","narrow","worried","empty")
    call ast_main("That's better, now I can focus...","pout","narrow","base","L")
    call ast_main("ready sir?","smile","happyCl","base","mid")
    m "Ready as ever, [astoria_name]..."
    call ast_main("HORNIFY BOOBS!","scream","narrow","angry","mid")
    ">With that, a thin bolt of pink electricity jumps from the end of Astoria's wand onto Susan's breasts before fading away into them..."
    call sus_main("!!!","open_tongue","wide","worried","empty")
    call sus_main("Ahhh! what have you done!","open","wide","worried","mid",cheeks="blush")
    call sus_main("Where are my clothes!","scream","worried","angry","down",cheeks="blush")
    call ast_main("Pfft, you took them off ages ago.","smile","base","base","R")
    call ast_main("And I just cast a little spell is all.","grin","narrow","narrow","mid")
    ">Astoria begins to rock back and forth on your lap, causing a sinful bolt of pleasure through your cock as you buck back into the evil little witch..."
    call ast_main("Sir...","pout","wink","ahegao","R")
    call ast_main("Now what's the spell feel like Susy?","smile","wink","ahegao","mid")
    call sus_main("Agh... it's like... it's like they're on fire!","open","wide","worried","down",cheeks="blush")
    call ast_main("mmmm.... Bad fire?", "annoyed", "narrow","narrow", "mid")
    ">Astoria rolls her hips hard against your cock..."
    call ast_main("Or good fire?","smile","narrow","narrow","mid")
    call sus_main("{b}Good{/b} fire...","upset","","base","base",cheeks="blush")
    call ast_main("And where is the good fire?","base","base","base","base")
    call sus_main("Ugh... I... I don't want to say...","base","base","base","base")
    call ast_main("Why not?","base","base","base","base")
    call sus_main("it's too embarrassing!","base","base","base","base")
    call ast_main("Don't worry, you love being embarrassed in front of the headmaster and I...","base","base","base","base")
    call ast_main("It makes the fire feel even better...","base","base","base","base")
    call ast_main("{b}doesn't it?{/b}","base","base","base","base")
    call sus_main("Ah...","base","base","base","base")
    call sus_main("It's in...","base","base","base","base")
    call sus_main("My breasts... They feel so...","base","base","base","base")
    call sus_main("Ah... I need to...","base","base","base","base")
    ">Unable to hold back any longer, susan's hands fly towards her breasts before they start to roll and knead the tender globes of flesh..."
    call sus_main("Ah.... w-wow...","base","base","base","base")
    call sus_main("I've never felt anything like...","base","base","base","base")
    call sus_main("{image=textheart}{image=textheart}{image=textheart}","base","base","base","base")
    ">As Susan's hands mesmerisingly tend to her own tits, your cock begins to strain in earnest against the girl above."
    ">You shamelessly start to hump against astoria, desperate for any stimulation to accompany the sight before you."
    call ast_main("Mmmm... your liking this aren't you...","base","base","base","base")
    ">Before you can say anything, Susan issues a defeated response..."
    call sus_main("yes...","base","base","base","base")
    ">A cheeky grin forms across Astoria's face as she holds her butt firm against your cock."
    call ast_main("Are you going to cum?","base","base","base","base")
    m "..."
    call sus_main("...","base","base","base","base")
    call ast_main("Tell me.","base","base","base","base")
    m "y-"
    call sus_main("Ah... yes...{image=textheart}","base","base","base","base")
    call ast_main("Mmmm...","base","base","base","base")
    ">Astoria pushes hard into your lap."
    m "Argh..."
    call ast_main("It makes sense a cow like you would cum from having her udders played with...","base","base","base","base")
    call ast_main("Not to mention when she's doing it in front of her headmaster. *tsk*tsk*tsk*","base","base","base","base")
    call sus_main("Y-you made me do this!","base","base","base","base")
    call ast_main("What?","base","base","base","base")
    call ast_main("You came up here and asked the headmaster and me to watch you...","base","base","base","base")
    call ast_main("Didn't you...","base","base","base","base")
    ">Susan struggles unsuccessfully against the effect of the imperio spell."
    call sus_main("I don't- maybe- I- why?...","base","base","base","base")
    call ast_main("Because you wanted Dumbledore and me to know what a nasty slut you were...","base","base","base","base")
    call ast_main("You were so proud about being able to cum from just your big gross tits being played with!","base","base","base","base")
    call sus_main("I- I'm proud...","base","base","base","base")
    ">Astoria has begun humping your lap in earnest, punctuating every word with a little thrust."
    call ast_main("You should be!","base","base","base","base")
    call ast_main("It's not easy cumming from just your tits...","base","base","base","base")
    call ast_main("Only the biggest sluts in the world can do it!","base","base","base","base")
    call sus_main("...The biggest...","base","base","base","base")
    call ast_main("That's right...","base","base","base","base")
    call ast_main("Now go on...","base","base","base","base")
    m "Argh..."
    ">Your cock is riding the edge after Astoria's relentless assault."
    call ast_main("{b}Cum{/b}","base","base","base","base")
    ">Astoria punctuates her sentence by pressing her buttcrack hard against your cock and holding it there as she shakes her butt.."
    m "ARGH! FUCK YES!"
    ">That, combined with the sight of the innocent redhead cumming helplessly as she claws at her own tits prove too much for your poor cock..."
    m "FUCKING TAKE THIS YOU WHORES!"
    call sus_main("{image=textheart}{image=textheart}{image=textheart}","base","base","base","base")
    ">Your hips writhe desperately against Astoria giggling body as you pump a huge load of cum into the inside of your robe."
    m "Ugh... keep fucking moving..."
    ">Both astoria and susan take your advice to heart, the redhead groping her tits anew and the blonde shamelessly grinding against you."
    m "You dirty little sluts..."
    ">Your hips slow as your orgasm begins to subside."
    m "Mmmm... that's it..."
    call ast_main("All done now sir?","base","base","base","base")
    m "Yeah... I could go for a nap right about now..."
    call ast_main("Don't fall asleep now old man, we've still got bessy here putting on a show for us...","base","base","base","base")
    call sus_main("Arghh...{image=textheart}{image=textheart}{image=textheart}","base","base","base","base")
    call sus_main("I thought...","base","base","base","base")
    call sus_main("why do...{image=textheart}{image=textheart}{image=textheart} they still feel so {b}gooood{/b}.","base","base","base","base")
    call ast_main("Hmmm... I thought that it would wear off after the first one...","base","base","base","base")
    call ast_main("Oh well, I'm bored now.","base","base","base","base")
    ">Astoria hops off your lap, causing you to notice a huge cum stain on her skirt..."
    call ast_main("!!!","base","base","base","base")
    call ast_main("Sir!","base","base","base","base")
    m "What?"
    call ast_main("My butt is {b}covered{/b} in your gross cum!","base","base","base","base")
    m "Well what did you expect after that?"
    call ast_main("Hmph!","base","base","base","base")
    call ast_main("I expected your robe to stop it all!","base","base","base","base")
    call ast_main("Clearly a gross old man like you has way too much cum in those big yucky balls of yours!","base","base","base","base")
    call ast_main("Susan!","base","base","base","base")
    call sus_main("Y-yes A-Astoria...","base","base","base","base")
    call ast_main("Clean me up and then go back to class...","base","base","base","base")
    call ast_main("Oh, and put your clothes on before you go...","base","base","base","base")
    call sus_main("Clean you... how?","base","base","base","base")
    call ast_main("Lick it up, Bessy!","base","base","base","base")
    call sus_main("You can't be serious!","base","base","base","base")
    ">However, Susan's shock and disgust are undermined by her helpless body moving towards Astoria's skirt."
    call ast_main("And make sure you get it all!","base","base","base","base")
    call sus_main("I-","base","base","base","base")
    call ast_main("!!!","base","base","base","base")
    call ast_main("Wow, she's really going for it!","base","base","base","base")
    call sus_main("...","base","base","base","base")
    m "..."
    call ast_main("I forgot how big cow's tongues were.","base","base","base","base")
    m "Alright, that's it. Unless you intend to sort out the problem your creating right now I think you two better head off."
    call ast_main("What? Already?","base","base","base","base")
    m "Only if you don't want to hop back up on my lap..."
    ">You give your cum-soaked lap an inviting pat."
    call ast_main("Ugh, fine. You better be done Susan.","base","base","base","base")
    ">Susan moves her head away from the Astoria's cute skirt."
    call sus_main("Mhmm...","base","base","base","base")
    call ast_main("Good, well swallow that and head to class.","base","base","base","base")
    call ast_main("Let me know when you want to try out the next spell...","base","base","base","base")
    ">Astoria throws Susan a cheeky grin."
    call ast_main("Bye bessy...","base","base","base","base")
    ">With that, Astoria hops out of your office, leaving Susan alone to silently collect her clothes and leave, forgetting the whole incident only moments after closing the door."
    m "(I sort of feel bad for her...)"
    m "(No, there's boobs at stake, we have to forge on...)"
    jump main_room_menu





label hornify_spell_2: #second level hornify spell
    call ast_main("Ready to practice that hornify spell again?","base","base","base","base")
    m "Are you sure you wanna practice that one again? We could start to learn a new spell instead."
    m "Don't forget you have to have to visit Tonks each time we try one..."
    call ast_main("Pfft, what's she going to do? Make me try on another cute skirt?","base","base","base","base")
    ">Astoria gives her hips a quick shake, almost flashing you due to the shortness of it."
    call ast_main("I'm soooo scared... Now hurry up and get Bessy here, it's almost milking time!","base","base","base","base")
    m "..."
    ">With that you summon the poor redhead up to your office for another session of degrading humiliation."
    call sus_main("You wanted to see me sir?","base","base","base","base")
    ">Susan calmly begins to take her top off, not letting it interrupt her as she greets Astoria."
    call sus_main("Oh... H-hi, astoria... what are you doing here?","base","base","base","base")
    call ast_main("Getting ready to watch a show...","base","base","base","base")
    call sus_main("What show?","base","base","base","base")
    call ast_main("You on your knees while Professor Dumbledore coats you in his sticky, icky cum!","base","base","base","base")
    call sus_main("What? I don't-","base","base","base","base")
    call ast_main("Shhhh.... Don't talk unless I tell you to, OK?","base","base","base","base")
    call sus_main("...","base","base","base","base")
    ">Susan nods, a terror in her eyes as she gazes down silently at the smiling young blonde."
    call ast_main("Now why don't you kneel in front of me right here...","base","base","base","base")
    call ast_main("And sir, hurry up and get over here!","base","base","base","base")
    m "Ugh... the things I do to help my students..."
    ">You put on a mock air of reluctance as you stroll over to Susan, pulling your cock from it's robe and presenting the imposing thing to a frightened young Susan."
    call ast_main("Wow...","base","base","base","base")
    call ast_main("It's big...","base","base","base","base")
    pause
    call ast_main("For an old man like you!","base","base","base","base")
    call sus_main("...","base","base","base","base")
    call ast_main("Go on then... make it shoot... stuff...","base","base","base","base")
    ">You slowly start to stroke your cock only inches from Susan's face..."
    m "If you want this to go a little quicker at least make her move a little..."
    call ast_main("Just wait a second sir, I haven't even cast it yet!","base","base","base","base")
    call sus_main("???","base","base","base","base")
    call ast_main("Hornify cum!","base","base","base","base")
    ">Another flash as the pink bolt of lightning shoots from the end of astoria's wand and strikes susan's head."
    call sus_main("!!!","base","base","base","base")
    ">Susan's hips immediately start to quiver as she struggles to maintain her composure."
    call ast_main("Now what this spell does, susy, is it makes you feel really good...","base","base","base","base")
    call ast_main("Once you cover yourself in the headmaster's gross smelly cum...","base","base","base","base")
    call sus_main("!!!!!!","base","base","base","base")
    call ast_main("Until then...","base","base","base","base")
    call ast_main("Well... you're slutty, little brain won't be able to think of much else...","base","base","base","base")
    call ast_main("So why don't you help the headmaster out and give him a little show, hmmm?","base","base","base","base")
    call sus_main("...","base","base","base","base")
    call ast_main("You can speak now Bessy...","base","base","base","base")
    call sus_main("...","base","base","base","base")
    call sus_main("{size=-5}Please sir...{/size}","base","base","base","base")
    call sus_main("cover me...","base","base","base","base")
    m "Mmmm, keep shaking those tits of yours and I won't have any other option!"
    call ast_main("hahahaha","base","base","base","base")
    call sus_main("*sob*T-thank you sir *sob*","base","base","base","base")
    call ast_main("Awww, is little susy sad that her tits are gonna be covered in cum?","base","base","base","base")
    call sus_main("...","base","base","base","base")
    call ast_main("Or maybe you're crying because your headmaster hasn't cum yet...?","base","base","base","base")
    call sus_main("*sob*I-I am not...","base","base","base","base")
    call ast_main("So you don't want Dumbledore to cum all over you then?","base","base","base","base")
    call sus_main("I didn't say that!","base","base","base","base")
    call ast_main("haha, typical. You Hufflepuff whores are always after one thing.","base","base","base","base")
    call sus_main("...","base","base","base","base")
    call ast_main("Maybe this would go faster if you sucked on dumbledore's gross old cock...","base","base","base","base")
    call sus_main("What? You can't be serious! Isn't this enough?","base","base","base","base")
    call ast_main("I don't know... Is it, sir?","base","base","base","base")
    menu:
        "-\"This is fine.\"-":
            call ast_main("*pfft*","base","base","base","base")
            call sus_main("really?","base","base","base","base")
            call sus_main("You mean I don't have to...","base","base","base","base")
            call sus_main("{b}suck{/b} it...","base","base","base","base")
            m "Not unless you want to. It'd probably speed things up a bit though..."
            call sus_main("...","base","base","base","base")
            call sus_main("...","base","base","base","base")
        "-\"Suck it!\"-":
            call sus_main("Professor dumbledore!","base","base","base","base")
            call ast_main("See! I told you he wants you to suck it!","base","base","base","base")
            call ast_main("Open Wide slut!","base","base","base","base")
            call sus_main("...","base","base","base","base")
            call sus_main("...","base","base","base","base")
    ">With that, Susan closes her eyes and nervously puts the head of your cock in her mouth..."
    call sus_main("!!!","base","base","base","base")
    call sus_main("It's disgusting!","base","base","base","base")
    call ast_main("HAHAHAHAHAHA","base","base","base","base")
    m "Now, now [susan_name]..."
    call ast_main("Yeah, susy, don't be rude to the headmaster!","base","base","base","base")
    call sus_main("But, but-","base","base","base","base")
    call ast_main("Hornify cock!","base","base","base","base")
    ">Another flash of lightning erupts from the Slytherin's wand as it flies towards poor Susan..."
    ">Susan's eyes lock forward in a mixture of pleasure and fear as she plunges her inexperienced mouth onto your cock."
    call ast_main("There, not so gross now is it, Susy?","base","base","base","base")
    call sus_main("*Slrp*glp*slrp*","base","base","base","base")
    ">Susan just runs her tongue as fast as she can along the underside your cock as she holds the tip in her mouth."
    m "Ugh... slow down there [susan_name]..."
    call ast_main("Mmmmm, this look suits you, susy...","base","base","base","base")
    call sus_main("*Slrp*glp*slrp*","base","base","base","base")
    m "Ugh... are you sure you should have cast it twice?"
    call sus_main("*Slrp*glp*slrp*?","base","base","base","base")
    call ast_main("It'll be fine... Exponential can't be that much more can it?","base","base","base","base")
    call sus_main("*Slrp*!!!*glp*","base","base","base","base")
    call ast_main("She's not even feeling them both yet anyway...","base","base","base","base")
    call sus_main("*Slrp*glp*slrp*","base","base","base","base")
    ">Susan's mouth softly cradles your cock as she assaults the tip..."
    call sus_main("*Slrp*glp*slrp*","base","base","base","base")
    m "Ugh... I said slow down slut!"
    call sus_main("*Slrp*glp*slrp*","base","base","base","base")
    ">Susan refuses to acknowledge you, desperate to drain you as fast as she can..."
    call ast_main("Mmmm, that's it bessy...","base","base","base","base")
    call ast_main("Are you ready yet, sir?","base","base","base","base")
    m "Ugh... almost there..."
    ">Astoria leans in close to Susan."
    call sus_main("*Slrp*glp*slrp*","base","base","base","base")
    call ast_main("{size=-5}Hear that? He's going to coat you with his nasty cum...{/size}","base","base","base","base")
    call sus_main("*Slrp{image=textheart}*glp*{image=textheart}slrp*","base","base","base","base")
    g4 "ARGH, THAT'S IT YOU LITTLE WHORES!"
    call ast_main("Get ready slut-","base","base","base","base")
    call sus_main("*Slrp{image=textheart}*!!!*{image=textheart}slrp*","base","base","base","base")
    ">Your cock can handle Susan's amateur tongue no longer."
    g4 "AHH TAKE THIS SLUTS!"
    ">You pull your dick out of Susan's mouth with a satisfying pop as it begins to fire it's load."
    call sus_main("!!!","base","base","base","base")
    call ast_main("Told you!","base","base","base","base")
    ">You close your eyes as you furiously jerk your cock off onto Susan's blank face..."
    call sus_main("...this...","base","base","base","base")
    ">With that, Susan's mind seems to have taken too much, saving the poor girl from the excess pleasure by fainting..."
    call sus_main("...","base","base","base","base")
    ">She slumps to the floor, her hips still jerking intermittently..."
    call ast_main("...","base","base","base","base")
    m "!!!"
    call ast_main("Hahahaha! I guess casting it twice was too much for poor old Bessy.","base","base","base","base")
    call ast_main("Looks like you were right for once, sir.","base","base","base","base")
    m "Well we'll know for next time."
    call ast_main("Are you kidding? Someone like Susan deserves way worse than this!","base","base","base","base")
    m "...(What's she got against this girl?)"
    call ast_main("Good job by the way, sir, you covered her! I can smell her from here...","base","base","base","base")
    m "About that..."
    call ast_main("Not now, sir, I wanna wake her up.","base","base","base","base")
    call ast_main("Surgere!","base","base","base","base")
    ">A brief flash of white appears at the end of Astoria's wand."
    call sus_main("W-w-wha happened? where am I?","base","base","base","base")
    call ast_main("Don't you remember professor dumbledore's wrinkly old cock coating you in his nasty, smelly cum?","base","base","base","base")
    call ast_main("Hmmm?","base","base","base","base")
    call sus_main("I-i Stop-","base","base","base","base")
    call ast_main("Shhh...","base","base","base","base")
    call sus_main("!!!","base","base","base","base")
    call ast_main("I think I'm getting sick of smelling you honestly...","base","base","base","base")
    call ast_main("Why don't you head back to your room.","base","base","base","base")
    call sus_main("!!!","base","base","base","base")
    call ast_main("Take the scenic route, I think you'll need the fresh air...","base","base","base","base")
    call sus_main("!!!","base","base","base","base")
    ">You can see a desperate pleading in the poor redheads eyes as she realizes the humiliation she's about to endure..."
    m "don't you think that's a little much [astoria_name]?"
    call ast_main("Pfft, no... Besides, Everyone already stares at her big tits, it's not like anything will change...","base","base","base","base")
    call sus_main("...","base","base","base","base")
    call ast_main("Bye bye, Susy, don't forget to have fun!","base","base","base","base")
    call ast_main("And no magic to hide or clean up the headmaster's cum either!","base","base","base","base")
    call sus_main("......","base","base","base","base")
    ">With that, Susan silently walks a death march towards the door..."
    ">The door closes behind the cum drenched redhead as she puts her clothes back on and forgets the entire encounter..."
    call ast_main("hahaha, everyone's going to be talking about this for weeks!","base","base","base","base")
    m "You don't think you're taking this too far?"
    call ast_main("Not far enough! besides, who's going to punish me? you?","base","base","base","base")
    m "I'm not the one to worry about... Don't forget tonkerbell..."
    call ast_main("I'm sooo scared... What's she going to do?","base","base","base","base")
    m "She is Susan's aunt."
    call ast_main("And a huge perv like you! I've got her wrapped around my finger.","base","base","base","base")
    m "..."
    call ast_main("Speaking of, I better go see her now...","base","base","base","base")
    m "Have fun..."
    call ast_main("I will, she's probably got some more cool clothes for me.","base","base","base","base")
    call ast_main("See ya, sir!","base","base","base","base")
    ">With that, Astoria turns and walk out the door on the way to tonks' office..."
    m "Hmmm..."
    jump main_room_menu










label hornify_spell_3: #third level hornify spell
    ">Astoria quickly walks around your desk and hops up onto your lap."
    m "What's the special occasion?"
    call ast_main("You want to practice that spell don't you?","base","base","base","base")
    ">Astoria starts shamelessly rolling her hips on your cock."
    call ast_main("I'm just getting ready...","base","base","base","base")
    ">Astoria then gives her butt a little wriggle until your cock is resting in-between her butt cheeks."
    call ast_main("There, you can bring susy up here now...","base","base","base","base")
    m "You're comfortable sitting here then?"
    call ast_main("Hmph, I need something soft after what that meanie Tonks did!","base","base","base","base")
    call ast_main("Besides, a filthy old man like you should count their lucky stars I'm sitting here...","base","base","base","base")
    m "Suit yourself... but don't say I didn't warn you..."
    ">With that you give a playful thrust into Astoria before summoning Susan up to your office."
    call sus_main("Hello Professor Dumbledore.","base","base","base","base")
    call sus_main("Oh... um... hello Astoria...","base","base","base","base")
    call sus_main("You wanted to see me sir?","base","base","base","base")
    call ast_main("Pfft... you bet he does...","base","base","base","base")
    ">Astoria wriggles her bum against your cock to make her point..."
    call sus_main("Astoria!","base","base","base","base")
    call ast_main("Shhhh, Susy... just stay still for a sec, OK?","base","base","base","base")
    ">Susan's bodies stiffens in response to Astoria's lingering spell."
    call sus_main("...","base","base","base","base")
    call ast_main("You ready to go, sir?","base","base","base","base")
    m "I don't see why not."
    call ast_main("Ready, Susy?","base","base","base","base")
    call sus_main("...","base","base","base","base")
    ">A look of fear forms in Susan's eyes..."
    call ast_main("Hornify uniform!","base","base","base","base")
    ">A pink flash erupts from the end of Astoria's wand..."
    call sus_main("!!!","base","base","base","base")
    m "Her uniform?"
    call ast_main("What? You've got a problem with it?","base","base","base","base")
    m "no, no, it's just a little tame compared to last time..."
    m "Maybe tonks really did teach you a lesson."
    call ast_main("Pfft as if! I wasn't even done yet!","base","base","base","base")
    call ast_main("hornify exhibitionism!","base","base","base","base")
    call sus_main("!!!","base","base","base","base")
    m "Hmmm, that's a little more interesting..."
    call ast_main("Not done yet!","base","base","base","base")
    call sus_main("...","base","base","base","base")
    call ast_main("Susy, walk out and come back in!","base","base","base","base")
    ">Susan turns and walks outside, closing the large door behind her."
    m "What's that supposed to do?"
    call ast_main("So she forgets about the spells!","base","base","base","base")
    call ast_main("This way we can trick her into thinking she came to us...","base","base","base","base")
    ">With that the door swings open as Susan bones enters."
    call sus_main("Hello Professor Dumbledore.","base","base","base","base")
    call sus_main("Oh... um... hello Astoria...","base","base","base","base")
    call sus_main("W-Why are you sitting on Dumbledore's lap?","base","base","base","base")
    call ast_main("Because it's the softest place in the room.","base","base","base","base")
    call sus_main("Oh, ah o-ok then...","base","base","base","base")
    ">You notice a red flush appear over Susan's face as her thighs slowly start to roll together."
    call sus_main("D-did you want to {b}see{/b} me sir?","base","base","base","base")
    call ast_main("Don't you remember why you're here, susy?","base","base","base","base")
    call sus_main("U-um... I thought you... I-I guess not...","base","base","base","base")
    call ast_main("You wanted to show Dumbledore and me your plans for the new Hufflepuff uniform.","base","base","base","base")
    call sus_main("I-I did?","base","base","base","base")
    call ast_main("Mhmm! Something about the current one being way too \"prudish\"!","base","base","base","base")
    call ast_main("Isn't that right Dumbledore?","base","base","base","base")
    ">Astoria pushes hard into your cock..."
    m "I do seem to remember the word conservative being thrown around..."
    call sus_main("So you two are going sit there and {b}watch{/b} me...","base","base","base","base")
    call sus_main("-while I show off my new {b}uniform{/b}...","base","base","base","base")
    call ast_main("If you don't want t-","base","base","base","base")
    call sus_main("NO! Ugh... I mean, no, I want to show you...","base","base","base","base")
    call ast_main("Show us what?","base","base","base","base")
    call sus_main("My... new uniform...","base","base","base","base")
    ">Astoria begins rocking her hips slowly on your lap."
    call ast_main("Well, go on then...","base","base","base","base")
    call sus_main("...","base","base","base","base")
    call sus_main("Ok...","base","base","base","base")
    ">You notice the desperate need and lust in Susan's voice begin to overtake her nervousness..."
    call sus_main("The first thing I t-think needs to be changed is the s-skirt...","base","base","base","base")
    call ast_main("Really? How's that?","base","base","base","base")
    ">Astoria changes her rocking motion from forwards and backwards to side to side."
    call sus_main("I think it needs to be shor-shorter...","base","base","base","base")
    call ast_main("Shorter?","base","base","base","base")
    call sus_main("Mhmm...","base","base","base","base")
    call ast_main("How much shorter?","base","base","base","base")
    call sus_main("Well, um, a fair-","base","base","base","base")
    call ast_main("Why don't you show us...","base","base","base","base")
    ">Astoria presses your cock hard into her buttcrack..."
    m "Ugh..."
    call sus_main("Here?... in front of...","base","base","base","base")
    call ast_main("Go on...","base","base","base","base")
    call sus_main("A-Alright...","base","base","base","base")
    call sus_main("I ugh... think that the skirt should-","base","base","base","base")
    ">Susan starts to fold it inwards at the belt, causing it to ride up..."
    call sus_main("probably at least...","base","base","base","base")
    call sus_main("This short...","base","base","base","base")
    ">The shy redhead stands before you with her skirt irresistibly rolled up as high as it can go..."
    m "You don't think that's a little too high Ms Bones?"
    ">You look down and notice the desperate redhead's juices start to drip down from underneath the tiny skirt..."
    call sus_main("I-I don't think so...","base","base","base","base")
    call ast_main("Really? I can make out your panties!","base","base","base","base")
    call sus_main("You can?...","base","base","base","base")
    call sus_main("...","base","base","base","base")
    ">You notice Susan's thighs squeeze together helplessly in pleasure."
    call sus_main("well a-anyway, I think this is a good length for the hufflepuff uniform...","base","base","base","base")
    call ast_main("I bet you do...","base","base","base","base")
    call sus_main("W-what do you think sir?","base","base","base","base")
    ">You start to rock your hips against Astoria, causing her to bob up and down in front of Susan as you answer..."
    menu:
        "-Shorter-":
            m "I'd say you could stand to go a little shorter..."
            call sus_main("Really? Thank you sir...","base","base","base","base")
            ">With that, Susan starts to roll up her skirt a little more, shamelessly bringing her soaked panties into view..."
            call ast_main("Wow, that took a lot of convincing...","base","base","base","base")
            ">Astoria speeds up her hips as she starts to bounce on your lap."
            call sus_main("Well it's not my fault the school skirt is so horribly long!","base","base","base","base")
            call ast_main("Of course not...","base","base","base","base")
        "-It's fine-":
            m "That's short enough i'd say..."
            call sus_main("Really? You don't want it a little...","base","base","base","base")
            call ast_main("Sir! Of course he wants it shorter!","base","base","base","base")
            call sus_main("b-but he said...","base","base","base","base")
            call ast_main("You want it shorter, don't you, sir?","base","base","base","base")
            ">Astoria presses her ass into your cock with a playful hop."
            m "Ugh... gods yes..."
            call sus_main("...","base","base","base","base")
            ">Susan has a guilty smirk on her lips as she rolls her skirt ever so higher, showing off her soaked panties..."
    m "Well I don't think anyone could complain about a skirt like that..."
    call sus_main("T-thank you s-sir...","base","base","base","base")
    call ast_main("That's not all though is it, Susy?","base","base","base","base")
    call sus_main("N-no...","base","base","base","base")
    call ast_main("I think you want to change your top as well don't you?","base","base","base","base")
    call sus_main("Ah... yes... I want to show you... my... {p}ideas...","base","base","base","base")
    call ast_main("Mmmm... go on then...","base","base","base","base")
    ">Astoria has shamelessly started to grind against your cock while teasing the poor redhead..."
    call sus_main("First th-things first... The vest needs to go...","base","base","base","base")
    call ast_main("...","base","base","base","base")
    ">Astoria silently watches as Susan throws her vest to the ground..."
    call ast_main("What's next?","base","base","base","base")
    call sus_main("Well I think it should be a rule that...","base","base","base","base")
    ">Astoria's hips continue to grind against you, a needy heat beginning to emanate from them..."
    call sus_main("You shouldn't be allowed to do up your first two buttons on your shirt...","base","base","base","base")
    call ast_main("Why's that?","base","base","base","base")
    call sus_main("Oh... um... it's so that you don't overheat in class...","base","base","base","base")
    call ast_main("Overheat?","base","base","base","base")
    call sus_main("Um... as well as it helps to, um...","base","base","base","base")
    call ast_main("Shhh, keep going...","base","base","base","base")
    call sus_main("...","base","base","base","base")
    ">Susan's thighs start to shamelessly drip as she continues to debase her uniform for Astoria and yourself."
    call sus_main("Well... I also think that you should roll the bottom up and through the middle too...","base","base","base","base")
    ">With that Susan flips her top to make it little more than a tube top in front of the two of you..."
    call sus_main("There... I-I think that this should be the new Hufflepuff uniform...","base","base","base","base")
    ">With that, Susan stands still, proudly presenting her slutty attire to you and the young Slytherin grinding on your cock."
    pause
    call ast_main("Is that all?","base","base","base","base")
    call sus_main("I think so...","base","base","base","base")
    call sus_main("So what do you think?","base","base","base","base")
    call ast_main("It'll definitely get rid of the idea that hufflepuff are prudes!","base","base","base","base")
    call sus_main("...","base","base","base","base")
    call sus_main("What do you think, sir?","base","base","base","base")
    ">Before you're able to muster a response, Astoria shamelessly starts grinding in front of Susan, doing everything she can to shame the poor girl..."
    call ast_main("Mmmm, the headmaster sure feels like he likes it...","base","base","base","base")
    call sus_main("Feels like-","base","base","base","base")
    call sus_main("You mean?","base","base","base","base")
    call ast_main("Yep, his nasty old cock is all hard from having to look at your slutty little uniform...","base","base","base","base")
    ">A look of both shame and extreme arousal pass over Susan's face as her hips start to quiver..."
    call sus_main("Is it true sir... Do you think this uniform is too {b}slutty{/b}?","base","base","base","base")
    menu:
        "-Shame her-":
            m "Of course girl!"
            call ast_main("...","base","base","base","base")
            ">Astoria continues to encourage you along with her playful lap dance..."
            m "You expect to dress like that and not be called a whore?"
            call sus_main("I-I-I was just trying","base","base","base","base")
            m "To what? Get me to cum just by looking at you?"
            call sus_main("...","base","base","base","base")
            call ast_main("She isn't far off from the feel of you...","base","base","base","base")
            ">Astoria gives a forceful rub to the tip of your cock..."
            m "Urghh... You're not helping you little minx..."
            call sus_main("So I shouldn't dress like this then?","base","base","base","base")

        "-Be nice...-":
            m "Nonsense, a girl is only as slutty as she acts..."
            m "I'm sure you'll be able to go to classes and act normally dressed like that..."
            call ast_main("Really sir? It wouldn't surprise me if Susy rubs one out in the middle of class!","base","base","base","base")
            call sus_main("Astoria! I would never do such a thing sir!","base","base","base","base")
            call sus_main("Can you imagine what people would say if they s-saw me touching myself in class!","base","base","base","base")
            call sus_main("There would be talk for weeks about how much of a {b}slut{/b} I am and how I should so {b}ashamed{/b}...","base","base","base","base")
            ">Susan's hips spasm with need..."
            call sus_main("Maybe I shouldn't go to class like this...","base","base","base","base")
    call ast_main("Nonsense! You have to go to class and show everyone your cute new uniform!","base","base","base","base")
    call sus_main("I do?","base","base","base","base")
    call ast_main("Mhmm! How else are you going to get people's opinions about it?","base","base","base","base")
    call sus_main("Y-you're right!","base","base","base","base")
    call sus_main("I know, I should make a petition!","base","base","base","base")
    call ast_main("*pffft*","base","base","base","base")
    call ast_main("That's a great idea Susie! Why don't you ask as many people as you can about your new uniform!","base","base","base","base")
    call sus_main("How many do I need to get to make this Hufflepuffs new uniform?","base","base","base","base")
    menu:
        "-Ten-":
            m "Ten should do."
            call sus_main("Only ten?!","base","base","base","base")
            call sus_main("I'll have this done before lunch!","base","base","base","base")
            call ast_main("Yeah, that's not enough, sir!","base","base","base","base")
            call sus_main("Astoria!","base","base","base","base")
            call ast_main("Fine, I guess that just means he must really like your uniform...","base","base","base","base")
        "-Fifty-":
            m "Fifty signatures would probably be enough..."
            call sus_main("OK sir, I'll try my hardest to get that many!","base","base","base","base")
        "-One hundred-":
            m "One hundred."
            call sus_main("One hundred?!","base","base","base","base")
            call sus_main("I can't get one hundred signatures in just one day!","base","base","base","base")
            call sus_main("Especially not if I go to all my classes...","base","base","base","base")
            call ast_main("Just skip them!","base","base","base","base")
            call sus_main("Play hooky?","base","base","base","base")
            call sus_main("What would everyone think!","base","base","base","base")
    call sus_main("Well, I better get to class then!","base","base","base","base")
    call ast_main("Have fun, Susy...","base","base","base","base")
    ">With that, the excited, ashamed and scantily dressed young girl blindly exited your office with a horny little smile on her face."
    call ast_main("Pfft, I can't wait to hear the rumours going around about Susie the Floozy once she asks for signatures for that uniform!","base","base","base","base")
    call ast_main("This is going to be great! I'm going to chase her around to see what people say.","base","base","base","base")
    ">Astoria hops off of your lap, ready to chase after the redheaded slut..."
    m "Wait a minute, you don't plan on leaving me like this do you?"
    call ast_main("You mean your- gross!","base","base","base","base")
    call ast_main("Your lucky I sat on your lap today! If you think I'm going to actually touch that monster of yours...","base","base","base","base")
    call ast_main("That's what Susie's for!","base","base","base","base")
    m "Well why didn't you get her to deal with this then?"
    call ast_main("You know what happens if I send her out with your cum all over her...","base","base","base","base")
    call ast_main("Just be a good headmaster and wait for Susy to come back later today.","base","base","base","base")
    m "Ugh, fine... But it's not good to leave a man with blue balls..."
    call ast_main("Ew... sir!","base","base","base","base")
    ">Astoria then rushes off to watch the flaming wreck that is Susan's social life..."
    m "..."
    jump main_room_menu



label sluttify_spell_1: #first level sluttify spell
    #Pink heart dress and no underwear
    #Susan greatly embarrassed
    #Tonks comes in after the petition incident
    #Susan relieved to see her and have some protection
    #Tonks ignores her and immediately starts talking to astoria and genie
    #Astoria explains the imperio stuff before tonks agrees and asks to watch the rest of the show
    #Susan is shocked but forced to stay silent while the three watch her degrade herself
    #Astoria asks if there are any other spells tonks wants cast
    #Astoria explains the hornify one
    #Tonks says maybe next time

label sluttify_spell_2: #second level sluttify spell
    #Astoria and tonks come up to the office and start talking the plan for what they'll do to Susan today
    #Tonks pusing the envelope further than Astoria, curious to see the hornify spell in action
    #Summon susan up to the office
    #Sluttify and hornify boobs her
    #Astoria on your lap while Tonks starts touching herself
    #Everyone else shocked
    #Tonks tells astoria off for grinding one out of her headmaster, tells you off for everything and tells susan off for being so sexy before resuming touching herself
    #Everyone goes back to looking at susan
    #she starts playing with her boobs while calling everyone else perverts
    #Calls tonks out as Auntie causing her to orgasm
    #Tonks then gets bored, tells you two to tidy yourselves up before leaving

label sluttify_spell_3: #third level sluttify spell
    #Pink heart dress and no underwear
    #Have Tonks come up excited, talking about she hasn't come that hard in years
    #Tells Astoria to hop up on dumbledore's lap so they can get started
    #Have Astoria use sluttify and hornify incest
    #Tonks excited
    #Aggressively starts teasing susan while playing with herself
    #Your cock gets hard, causing Astoria to pull it out and put it in between her legs
    #Start thigh fucking astoria as susan and tonks get eachother off
    #Tonks asks astoria to hit her with hornify boobs again
    #Genie goes to tell her about the two hornifies being too strong before astoria cuts him off by casting it
    #Susan shamefully orgasms in front of everyone
    #You fill Astoria's skirt with cum
    #Tonks notices and starts cumming
    #Tonks leaves, tells you to tidy up susan before sending her home
    #Astoria excited by how much Tonks is getting into it, ignores your huge load


label orgasmio_spell_1: #first level orgasmio spell
    #Mild orgasm
label orgasmio_spell_2: #second level orgasmio spell
    #Intense orgasm
label orgasmio_spell_3: #third level orgasmio spell
    #Extreme orgasm, Astoria casts the spell multiple times

label tentacle_spell_1: #first level tentacle spell
    #Mild tentacle orgasm for susan and mild intercrural sex between genie and ast
label tentacle_spell_2: #second level tentacle spell
    #Extreme tentacle orgasm for susan and borderline sex between genie and ast
label tentacle_spell_3: #third level tentacle spell
    #Extreme tentacles and hornify for Susan, Astoria cums on genie's dick rubbing against her pussy

label hermione_spell: #Branching path event based on Astoria and Genie casting spells on Hermione.
    m "Ready to practice some more spells?"
    ast "You bet! What are we going to {b}blast{/b} Susan with today?"
    m "Actually, I was thinking we could bring someone else up..."
    ast "Really?"
    ast "I don't know about this, sir... It's not one of my friends is it?"
    m "Are you friends with Hermione Granger?"
    ast "That know-it-all {b}bitch{/b}?!"
    ast "Bring her up here..."
    m "So you're not friends then?"
    ast "Friends? Hermione's worse than Susan! She's worse than anyone!"
    ast "She's so high and mighty with her high grades and her big tits! ARGH!!!"
    ast "I swear she gets off on rubbing both of them in everyone's face!"
    m "I guess I'll bring her up here then..."
    ast "You better..."
    ">With that, you summon Hermione up to your office..."
    her "Hello [genie_name], you wanted to see me?"
    her "Oh... Hello Astoria..."
    ast "..."
    her "Did you two want anything?"
    ast "Only this..."
    ">Astoria is giddy with excitement as she slowly pulls her wand from her pocket..."
    ">however, Hermione realises her intentions immediately, pulling her wand out in response!"
    her "Petrificus TOTALUS!"
    ">Hermione launches a bolt from the end of her wand towards the small witch in front of you."
    menu:
        "-Move her out of the way-":
            jump astoria_leash_walk
        "-Let her take it-":
            jump hermione_breaks_astoria





label hermione_breaks_astoria:
    ">You sit there and watch as Astoria takes the full brunt of the spell, locking her body together like a plank of wood."
    her "[genie_name]! What are you doing?"
    m "What? I wasn't going to cast a spell on you?"
    her "But you were just going to let her hex me?"
    m "I guess... I wasn't going to let her do anything too bad..."
    her "What was she going to cast?"
    m "Um... I can't remember the name of it..."
    her "Tell. Me."
    m "I think it was imperial or something..."
    her "IMPERIO?! You were going to let her cast {b}imperio{/b} on me?"
    m "Just to play around... At worst she would have made you show me your boobs."
    her "If you let her cast Imperio on me she can make me do {b}anything{/b}!"
    ast "..."
    her "honestly, [genie_name]..."
    m "It wasn't my idea..."
    ast "*(Snitch!)*"
    her "*Pfft* Of course it was {b}her{/b} Idea..."
    her "Nasty Slytherins... She probably tricked you into letting her do it somehow..."
    m "..."
    her "Still, I hope you'll do the right thing for once and punish her for trying to cast an unforgivable curse?"
    menu:
        "-Let Hermione punish Astoria-":
            m "Actually, I think it's only fair you get to take care of it."
            m "You were going to be the victim after all."
            her "Wait... You want me to be the one to {b}punish{/b} her?"
            m "Only if you-"
            her "I accept!"
            m "That was quick."
            her "Are you kidding? This is the opportunity of a lifetime!"
            ast "..."
            her "Finally, a chance to get back at these nasty witches..."
            m "So, what's the plan?"
            her "Don't think you get to be involved, [genie_name]!"
            m "What? Why not?"
            her "You were going to let her cast it! You're just as much at fault as her!"
            m "I feel like we're getting bogged down in semantics..."
            her "Ugh... Your punishment is that you don't get to be involved at all..."
            m "Aww..."
            her "Now come on Astoria... You've got a date with the Gryffindor glory hole..."
            ast "!!!"
            her "Ready?"
            ast "!!!"
            her "Imperio..."
            ">The green smoke flies from hermione wand and up Astoria's nose before filling her eyes..."
            her "Follow me..."
            ">With that Hermione and a helpless astoria wander out of your office..."
            m "(Greedy bitch... What am I supposed to do now?)"
            jump main_room


        "-Take care if it yourself-":
            pass
    m "I'll take it from here then..."
    ast "(Phew...)"
    her "Oh no... You've just agreed to punish her..."
    her "You don't get to decide how..."
    ast "(Oh no...)"
    her "Petrificus totalus really is a fun spell... I'm not sure if you know this Astoria, but you can be posed just like a Barbie doll..."
    ">To prove her point, Hermione steps over to Astoria and folds her arms upwards in mock shock."
    her "See?"
    ast "..."
    her "I could even bend you over the desk..."
    ast "!!!"
    her "Pull your skirt up..."
    ast "..."
    her "And just let [genie_name] have his way with you..."
    ast "..."
    her "Would you like that? Hmm? Was that what you were going to do to me?"
    ast "..."
    her "Have you seen [genie_name]'s cock though? It's huge... It'd probably break a tiny little girl like you..."
    her "Not that you wouldn't love it... If I let you, you'd probably scream for more..."
    her "But that's not what we're going to do {b}today{/b}..."
    "With that, Hermione steps forward and grabs a hold of your cock..."
    her "We're playing a different game..."
    ast "..."
    her "We're playing the game of cumrag!"
    ast "!!!"
    her "[genie_name]'s got the cum..."
    ">With that, Hermione begins to enthusiastically start jerking you off."
    her "And you get to be the rag!"
    ast "!!!"
    her "Doesn't that sound like fun?"
    ast "..."
    her "Oh wait... I forgot that you can't talk..."
    #Latin for hermione unparalyzing astoria's mouth
    ast "Screw you, mudblood!"
    ">As soon as the words exit her mouth, hermione's hand flies from her side to slap Astoria's face. Hard."
    ast "!!!"
    her "You slytherins... All you do is spit venom..."
    ">Hermione goes back to jerking you off..."
    her "About time you got a bit thrown back at you..."
    ast "What? You think making the headmaster cum on me is going to change anything?"
    her "Probably not... I don't think I can change an evil little witch like you..."
    ast "..."
    her "But that doesn't mean that I shouldn't at least try to teach you a lesson."
    ast "How to jerk off old man cock? Ha, I bet you're an expert..."
    m "Mmmmm... That she is..."
    her "Thank you, sir..."
    ast "Wait... {p}how often has she been coming up here, sir?"
    m "Oh, um... A little bit..."
    her "*ahem*"
    m "OK... A lot..."
    ast "Then why did you suggest her for spell practice, unless..."
    ast "You did this on purpose, didn't you sir!"
    m "I don-"
    her "Of course he did! He'd never let me get hit with your curse, would you [genie_name]?"
    m "O-of course not..."
    her "See... He probably just needed some help to {b}break{/b} you in..."
    ast "That's not... You wouldn't do that would you sir?"
    m "..."
    ast "sir!"
    her "Ugh... I'm sick of listening to you blabber on..."
    her "Petrificus totalus!"
    ">Another flash as Hermione paralyses Astoria once more."
    ast "!!!"
    her "There, much better... Now, are you almost there, [genie_name]?"
    m "Ugh... almost..."
    her "Need a little more... {b}stimulation{/b}?"
    m "Mmmm... What did you have in mind?"
    her "I could show you my breasts..."
    her "Or... I could show you {b}hers{/b}..."
    menu:
        "-Hermione's-":
            m "Yours will do nicely, [hermione_name]."
            ast "..."
            her "Hmmm, I don't know why I even asked, it's not like Astoria has boobs anyway."
            ast "!!!"
            #Hermione pulls up her top
            m "Ugh... that's it slut, don't stop..."
            ast "..."
            pass



        "-Astoria's-":
            m "Why don't we sneak a peek at Miss Greengrass..."
            her "Really? I don't think there'll be much to see..."
            ast "..."
            m "Humour me."
            ">With that, Hermione pulls off Astoria's top as if she were changing the costume on a doll."
            her "ha, they're even smaller than I though!"
            ast "..."
            ">Hermione's starts rolling her hand around the tip of your cock, smearing it in pre-cum."
            m "Ugh... that's it slut, don't stop..."
            ast "..."
            pass
    m "mmm... here it comes you little sluts..."
    her "Ready Astoria?"
    ast "!!!"
    g9 "ARGH! TAKE THIS YOU LITTLE WHORE!"
    ">Your cock explodes, coating the poor Slytherin in cum while hermione mercilessly pumps you dry."
    her "Mmmm, let it all out... cover the witch."
    ast "..."
    m "Fuck... this feels a bit wrong..."
    her "Good! Serves you right for letting Astoria try to curse me."
    her "And you..."
    her "Have you learned your lesson?"
    ast "..."
    ">Astoria's eyes burn in a storm of fury and humiliation."
    her "Hmmm... Doesn't look like it..."
    her "I bet you'd just call me a mudblood again if I let you..."
    ast "..."
    ">A shine in Astoria's eyes all but confirm Hermione's suspicions."
    her "I guess I'll just have to wash your mouth out then..."
    her "Do you have any soap, [genie_name]?"
    m "Oh, um-"
    her "Of course you don't... If you did this room probably wouldn't reek of cum..."
    her "I know! We can kill two birds with one stone. I'll just wash out Astoria's mouth with cum!"
    ast "!!!"
    #fade to black
    #show astoria clean with mouth full of cum and tears down her face
    her "There, all done!"
    ast "..."
    ">Hermione then forces Astoria's mouth closed before gently stroking her throat, forcing her to involuntarily swallow your load like a naughty dog with their medication."
    her "{b}Perfect...{/b} Now, are you going to be able to manage to obliviate Astoria and send her back to her room, [genie_name]?"
    m "Oblivi-what?"
    her "Ugh... If you don't want to cast it just say so."
    her "OBLIVIATE!"
    ">A flash goes off as Astoria's eyes empty."
    her "I suppose you want me to take her back to her room as well?"
    m "If you don't mind."
    her "It's fine..."
    m "..."
    her "..."
    m "How many?"
    her "At least a hundred."
    m "One hundred points to \"Gryffindor\" then!"
    $ gryffindor += 100
    her "Thank you, [genie_name]."
    ">With that, Hermione unparalyses the dazed Slytherin before leading her out of your office and back to her dorm."
    jump main_room




label astoria_leash_walk:
    ">You quickly push Astoria to the side, leaving you to take the full force of Hermione's spell."
    g4 "ARGH!"
    ast "IMPERIO!"
    ">As your body stiffens from the spell, you see the life drain from Hermione's eyes as the puff of cursed smoke flies up her nostrils."
    ast "YES! We did it sir!"
    m "..."
    ast "Oh, did her spell hit you?"
    m "..."
    ast "Ha-ha! That's what you get for not reacting quicker..."
    m "!!!"
    ast "Now... what should we do with Miss know-it-all?"
    ast "Should I make her show us her boobies?"
    ast "What do you think, Hermione? I bet you'd hate that, wouldn't you!"
    her "I'd love it."
    ast "{size=+5}What?!{/size}"
    m "..."
    ast "Why?"
    her "It makes me feel {b}so{/b} good."
    ast "Wait... Have you shown the headmaster your boobs before?"
    her "Yes."
    ast "How many times have you shown him, you little tramp?"
    her "I can't remember."
    ast "What? Have you been having sex with the headmaster?"
    her "Yes..."
    ast "sir!"
    m "..."
    ast "Oh... right... paralysed..."
    ast "..."
    ast "You really are the biggest teacher's pet in the world, aren't you."
    ast "So, did you do it for a better grade?"
    her "No..."
    ast "That's surprising..."
    ast "So, sir,  why did you suggest her if you've already been there?"
    ast "Unless you wanted me to fool around with her..."
    ast "sir! You're such a dirty old pervert!"
    ast "So what can I do then?"
    ast "Is there even anything that the headmaster can do that would embarrass you anymore, slut?"
    her "I don't think so..."
    ast "Huh, I knew you were useless, sir!"
    ast "I guess I'll have to come up with my own super smart way to shame Miss know-it-all then!"
    ast "Ready for the best, most humiliating idea ever, Hermione?"
    her "Yes..."
    ast "Let's walk around the school together!"
    her "Together... With a slytherin?"
    ast "I bet you'd hate that, wouldn't you?"
    her "Yes..."
    ast "Would you hate it even more if you were wearing a leash?"
    her "Yes..."
    ast "And a sign that says... um..."
    her "..."
    ast "Mudblood slut!"
    her "..."
    ">It's barely noticeable but you can see a flicker of rage flash beneath Hermione's eyes."
    ast "You'd hate that, wouldn't you?"
    her "More than anything..."
    ast "Perfect!"
    ast "ACCIO LEASH!"
    ">A leash and collar fly quickly in through your window."
    m "(Woah... How'd she do that?)"
    ast "Well, have fun being stuck here all by yourself, sir."
    ast "Hermione and I are going to go on a walk around the school."
    her "..."
    ast "See ya sir!"
    ">With that, Astoria leads a dazed Hermione out of your office and into the wider wizarding world."
    jump main_room
