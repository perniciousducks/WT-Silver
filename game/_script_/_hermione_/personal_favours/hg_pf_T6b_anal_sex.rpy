### Anal Sex ###

# Intro
label hg_anal_sex_1:
    $ hg_pf_sex.change_icon(a="heart_yellow", b="heart_red")

    call her_chibi_scene("lie_on_desk")
    with d3
    call bld
    m "[hermione_name]..."
    call her_main("[genie_name]..?", "annoyed", "squint", "base", "mid", ypos="head")
    m "How familiar you are with the term \"Anal Sex\"?"
    call her_main("What?!", "soft", "wide", "worried", "shocked")
    m "I asked you a question..."
    call her_main("Ninety house points...", "annoyed", "narrow", "annoyed", "mid")
    m "Seriously?"
    call her_main("Yes!", "mad", "worriedCl", "worried", "mid")
    call her_main(".............................", "disgust", "narrow", "base", "mid_soft")
    m "Well alright then. Ninety house points it is."

    stop music fadeout 1.0
    call her_main("...........", "annoyed", "base", "worried", "R")
    m "Let's see..."
    call her_main(".................", "angry", "worriedCl", "worried", "mid",emote="05")
    m "Hm..."

    call her_chibi_scene("sex_pause", trans=fade)

    call her_main("!!!", "angry", "wide", "base", "stare")
    g4 "Oh, come on!"
    call her_main("Ouch!", "mad", "worriedCl", "worried", "mid",tears="soft_blink")
    m "Just try to loosen up a little, would you?"
    call her_main("I'm trying!", "angry", "base", "base", "mid",tears="soft")
    m "Ok, what if I do this..?"
    call her_main("Ouch! What are you doing, [genie_name]?", "mad", "worriedCl", "worried", "mid",tears="soft_blink")
    m "Yeah, this won't work either..."
    m "Hm..."
    m "Alright, I think I know what we should do."

    label .choices:
    menu:
        m "..."
        "\"I think I'll spit on it and just force it in!\"":
            call play_music("playful_tension") # SEX THEME.
            call her_main("Force it in, [genie_name]?!", "angry", "wide", "base", "stare",ypos="head")
            $ renpy.play('sounds/spit.mp3') #Sound of spiting.
            g4 "*SPIT!*"
            call her_main("Eeeeeew!", "scream", "worriedCl", "worried", "mid")
            call her_main("No, [genie_name], wait! Maybe if I just relax--", "open", "base", "base", "mid")
            m "No need, here I come!"
            with hpunch
            call her_main("ARGH!", "angry", "base", "base", "mid",tears="soft")
            call her_main("Ouch! Ouch! Ouch!", "mad", "worriedCl", "worried", "mid",tears="soft_blink")
            g4 "Almost in!"
            call her_main("No, you're hurting me! You are hurting me!", "scream", "worriedCl", "worried", "mid")
            g4 "Almost! Almost!"
            call her_main("Ah! It hurts!", "scream", "worriedCl", "worried", "mid")
            g4 "Shut it, [hermione_name]! I'm doing you a favour!"
            g4 "Your anus is so tight it's completely unfuckable!"
            call her_main("Then stop, please!", "mad", "worriedCl", "worried", "mid",tears="soft_blink")
            m "No! We need to loosen up your asshole a little!"
            call her_main("But I don't want you to!", "mad", "worriedCl", "worried", "mid",tears="soft_blink")
            m "Really? How do you expect people to fuck you up your ass then?"
            call her_main("What people?", "shock", "worriedCl", "worried", "mid")
            g4 "You know... people."
            g4 "Argh, dammit... My dick is hurting too now."
            call her_main("Stop then! Stop, [genie_name]!", "open", "worriedCl", "worried", "mid")
            call her_main("I've changed my mind! I don't need these points!")
            g4 "I think I'm almost..."

            $ renpy.play('sounds/gltch.mp3')
            with hpunch
            with kissiris
            call her_main("{size=+5}AAAAAAAAhhhhh!!!{/size}", "scream", "wide", "base", "stare")
            g4 "YES!!!"

            if use_cgs:
                $ face_on_cg = True
                $ ccg_folder = "herm_sex"
                $ ccg1 = "blank"
                $ ccg2 = "blank"
                $ ccg3 = "blank"
                show screen ccg
                call her_main("", "shock", "base", "base", "R",cheeks="blush",tears="soft",ypos="head")
            else:
                call her_chibi_scene("sex_slow", trans=d5)

            call her_main("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!", "scream", "wide", "base", "stare")
            g4 "Let us pump this little asshole full of semen then, shall we?"
            call her_main("Yes... Please, I just want this to end...", "scream", "worriedCl", "worried", "mid",cheeks="blush",tears="crying")
            g4 "Agh... You want this to end sooner?"
            g4 "Help me out then!"
            call her_main("*sob!* How?", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            g4 "You know..."
            call her_main("Oh...", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            #$ ccg2 = 6
            call her_main("I am a whore??", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            g9 "Yes you are!"
            call her_main("*Sob!* I am a whore...", "angry", "squint", "base", "mid",cheeks="blush")
            call her_main("I love to suck cock...")
            call her_main("And now my tiny asshole is getting ripped apart... *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            g4 "Yes! Yes!"
            g4 "Agrh! Yes!"
            call her_main("No! Is it getting bigger?! I'm scared!", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            g4 "ARGH!"

        "\"Suck me off first. Lubricate my cock!\"":
            call her_main("Oh... Alright...", "open", "base", "base", "mid",ypos="head")
            call play_music("playful_tension") # SEX THEME.

            # Blowjob
            call her_chibi_scene("bj", trans=fade)
            call ctc

            call her_main("*Slurp!* *Slurp!* *Slurp!*",ypos="head",flip=False)
            m "Yes... good..."
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Alright, I think that's enough. Back on the desk now."

            # Sex
            call her_chibi_scene("sex_pause", trans=fade)

            call her_main(".............", "open", "base", "base", "mid")
            g4 "Yes! Almost!"
            call her_main("Ouch!", "scream", "worriedCl", "worried", "mid")
            m "Relax. Almost in."

            $ renpy.play('sounds/gltch.mp3')
            with hpunch
            with kissiris
            call her_main("{size=+5}AAAAAAAAhhhhh!!!{/size}", "scream", "wide", "base", "stare")

            if use_cgs:
                $ face_on_cg = True
                $ ccg_folder = "herm_sex"
                $ ccg1 = "blank"
                $ ccg2 = "blank"
                $ ccg3 = "blank"
                show screen ccg
                call her_main("", "shock", "base", "base", "R",cheeks="blush",tears="soft",ypos="head")
            else:
                call her_chibi_scene("sex_slow", trans=d5)

            g4 "YES!!!"
            call her_main("My... my...", "scream", "wide", "base", "stare")
            call her_main("It hurts!", "shock", "worriedCl", "worried", "mid")
            g4 "Let's pump this little asshole full of semen then, shall we?"
            call her_main(".....................", "angry", "squint", "base", "mid",cheeks="blush")
            call ctc

            call her_main(".....................", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "You alright there, slut?"
            call her_main("Ah... You are... stretching me out from the inside... [genie_name].", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            call her_main("And it still hurts...", "angry", "squint", "base", "mid",cheeks="blush")
            m "Hm..."
            m "Maybe not enough lubrication...?"
            m "Come on down, [hermione_name]. Suck my dick some more."
            call her_main("What? But...", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            call her_main("But it's dirty... It's been inside already.", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "Yes, it's been inside, but that doesn't mean it's dirty now."
            m "Come on, [hermione_name]. Suck my cock some more."
            call her_main("...........", "shock", "base", "base", "R",cheeks="blush",tears="soft")

            # Blowjob
            hide screen ccg
            $ face_on_cg = False
            call her_chibi_scene("bj", trans=fade)
            call ctc

            call her_main("*Slurp!* *Slurp!* *Slurp!*",ypos="head",flip=False)
            m "Yes... good..."
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Can you taste your ass on my dick?"
            her "*Slurp!* *Slurp!* *Slurp!*"
            m "Alright, Maybe that's enough."

            # SEX
            if use_cgs:
                $ face_on_cg = True
                $ ccg_folder = "herm_sex"
                $ ccg1 = "blank"
                $ ccg2 = "blank"
                $ ccg3 = "blank"
                show screen ccg
                call her_main("", "shock", "base", "base", "R",cheeks="blush",tears="soft",ypos="head")
            else:
                call her_chibi_scene("sex_slow", trans=fade)
            call ctc

            call her_main("Ah...", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "Better now?"
            call her_main("It still hurts...", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            call her_main("But I think I will be fine...")
            m "I'll take it slow for now..."
            call her_main("Ah... thank you, [genie_name].", "angry", "squint", "base", "mid",cheeks="blush")
            m "Oh... yes... this feels great..."
            call her_main("...........", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "Oh... So tight..."
            call her_main("................", "shock", "narrow", "base", "down",cheeks="blush",tears="crying")
            m "Why are you being so quiet [hermione_name]?"
            call her_main("Because this is painful...", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            call her_main("And I just want you to cum sooner, [genie_name]...")
            m "So you stifle your cries of pain?"
            call her_main("Yes [genie_name]. *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "Don't do that."
            m "Sob, scream and cry as much as you wish!"
            call her_main("B-but--", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            m "That will make me cum sooner."
            call her_main("Really? *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            call her_main("*Sob!* It hurts! *Sob!* It hurts so much! *Sob!*", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "Yes, yes..."
            call her_main("*SOB!*", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            m "You poor little kid..."
            m "A Big, evil man is raping your asshole!"
            call her_main("*SOB!* Yeees! *SOB!*", "scream", "squint", "base", "mid",cheeks="blush",tears="messy")
            g4 "Argh!"
            call her_main("No, I'm scared! *SOB!*", "scream", "worriedCl", "worried", "mid",cheeks="blush",tears="messy")
            
        "{color=[menu_disabled]}\"Lets use some lubrication.\"{size=-2}(Item){/size}{/color}" if anal_lube_ITEM.number <= 0:
            m "(I don't have any lube left. I'm gonna have to be more creative.)"
            jump hg_anal_sex_1.choices
            
        "\"Lets use some lubrication.\"{size=-2}(Item){/size}" if anal_lube_ITEM.number > 0:
            $ anal_lube_ITEM.number -= 1

            call play_music("playful_tension") # SEX THEME.
            call her_chibi_scene("sex_pause", trans=fade)
            call her_main("Lubrication, [genie_name]?!", "angry", "wide", "base", "stare",ypos="head")
            m "*Shhh*... Just stay still."
            "*Squeeze!*"
            call her_main("Ahhh! It's cold!", "scream", "worriedCl", "worried", "mid")
            call nar(">You thoroughly lubricate her asshole.")
            m "That should do it."
            call her_main("No, [genie_name], wait! Maybe--", "angry", "base", "worried", "mid")
            call nar(">You align the tip of your dick with her lubricated winky star and push forward.")
            $ renpy.play('sounds/gltch.mp3')
            with hpunch
            with kissiris
            call her_main("ARGH!", "shock", "base", "base", "mid",tears="soft")
            call nar(">You have applied too much force into your thrust, making you bottom out inside of her.")
            g4 "Holy shit!"
            
            if use_cgs:
                $ face_on_cg = True
                $ ccg_folder = "herm_sex"
                $ ccg1 = "blank"
                $ ccg2 = "blank"
                $ ccg3 = "blank"
                show screen ccg
                call her_main("", "shock", "base", "base", "R",cheeks="blush",tears="soft",ypos="head")
            else:
                call her_chibi_scene("sex_slow", trans=d5)
                
            call her_main("Ouch! Ouch! Ouch!", "mad", "worriedCl", "worried", "mid",tears="soft_blink")
            call her_main("No, you're hurting me! You are hurting me!", "scream", "worriedCl", "worried", "mid")
            g4 "*Argh* Fuck, I can't pull out!"
            call her_main("Ah! It hurts!", "scream", "worriedCl", "worried", "mid")
            g4 "Then stop clenching on me so hard, [hermione_name]!"
            g4 "Your anus is so tight I can't even move!"
            call her_main("Please, do something!", "mad", "worriedCl", "worried", "mid",tears="soft_blink")
            g4 "I'm trying, [hermione_name]!"
            call her_main("Then try harder!", "scream", "base", "angry", "mid",tears="soft")
            call slap_her
            call her_main("..........!", "scream", "wide", "worried", "mid",tears="soft")
            g4 "Shut the hell up, whore!"
            g4 "It's..."
            call slap_her
            g4 "It's...{fast} your..."
            call slap_her
            g4 "It's... your...{fast} bloody..."
            call slap_her
            g4 "It's... your... bloody... {fast}fault!"
            call slap_her
            pause 1.0
            call play_sound("boing") 
            with hpunch
            if not use_cgs:
                call her_chibi_scene("sex_pause", trans=d5)
            pause 1.0
            m "Oh, it worked."
            
            call her_main("*sob!*", "mad", "base", "angry", "down",cheeks="blush",tears="soft")
            call her_main("...my asshole... my poor asshole... *sob*","mad", "base", "angry", "mid",cheeks="blush",tears="soft")
            g9 "In that case, lets try it again."
            call her_main("No! Stop, [genie_name]!", "open", "wide", "worried", "mid",cheeks="blush",tears="soft")
            call her_main("I've changed my mind! I don't need these points!",cheeks="blush",tears="soft")
            m "It will be fine this time, trust me..."

            $ renpy.play('sounds/gltch.mp3')
            with hpunch
            with kissiris
            call her_main("{size=+5}AAAAAAAAhhhhh!!!{/size}", "scream", "wide", "base", "stare")
            g4 "YES!!!"
            
            if not use_cgs:
                call her_chibi_scene("sex_slow", trans=d5)

            call her_main("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!", "scream", "wide", "base", "stare")
            g4 "Let us pump this little asshole full of semen then, shall we?"
            call her_main("Yes... Please, I just want this to end...", "scream", "worriedCl", "worried", "mid",cheeks="blush",tears="crying")
            g4 "Agh... You want this to end sooner?"
            g4 "Help me out then!"
            call her_main("*sob!* How?", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            g4 "You know..."
            call her_main("Oh...", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            #$ ccg2 = 6
            call her_main("I am a whore??", "clench", "base", "worried", "mid", cheeks="blush",tears="soft")
            g9 "Yes you are!"
            call her_main("*Sob!* I am a whore...", "angry", "squint", "base", "mid",cheeks="blush")
            call her_main("I love to suck cock...")
            call her_main("And now my tiny asshole is getting ripped apart... *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            g4 "Yes! Yes!"
            g4 "Agrh! Yes!"
            call her_main("No! Is it getting bigger?! I'm scared!", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            g4 "ARGH!"

    menu:
        "-Fill Hermione up with cum-":
            g4 "Argh!"
            call her_main("No! AH!", "scream", "wide", "base", "stare",ypos="head")
            call cum_block
            g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

            if not use_cgs:
                call her_chibi_scene("sex_cum_in", trans=d5)
            else:
                $ ccg3 = "s1"
            call cum_block
            call ctc

            call her_main("AH! IT'S FILLING ME UP!{heart}{heart}{heart}", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            g4 "Yes, you whore! Yes!"
            call her_main("It hurts, it hurts!", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            g4 "Shut up!"
            with hpunch
            call her_main("No, I am already full! Stop cumming, you bastard!", "scream", "wide", "worried", "stare",cheeks="blush",tears="messy")
            g4 "Shut the fuck up, slut! I am not done yet!"
            call her_main("No! Please! My stomach! I will explode!", "scream", "squint", "base", "mid",cheeks="blush",tears="messy")
            g4 "ARGH!"
            call her_main("No, I think I will throw up...", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            with hpunch
            play sound "sounds/burp.mp3"
            call her_main("{size=+7}*BURP!*!!!!!{/size}", "full", "wide", "worried", "stare",tears="messy")
            call her_main(".......................", "full", "base", "base", "mid",tears="messy")
            call her_main(".............")
            $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
            call her_main("{size=+7}*GULP!*{/size}", "cum", "worriedCl", "worried", "mid")
            call her_main("*SOB!* I HATE YOU...", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            call her_main("{size=+5}I HATE YOU AND YOUR NASTY OLD COCK?{/size}", "scream", "base", "angry", "mid",cheeks="blush",tears="messy")
            call her_main("{size=+5}I HATE YOU! YOU HEAR ME?!{/size}")
            g4 "Agh...Shut it, whore!"
            call her_main("*sob!* *Sob!*...", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            call ctc

            # AFTER CUM INSIDE
            if not use_cgs:
                call her_chibi_scene("sex_cum_in_done", trans=d5)

            call her_main("*Sob!*...", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "Whew!... I think that was the last of it."
            m "You alright?"
            call her_main("Yes... *Sob!*", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "Are You crying?"
            call her_main("My butt hurts, but I am alright, [genie_name]...", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "Well, you took my dick stoically, all things considered..."
            call her_main("Thank you [genie_name]...", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            hide screen bld1
            with d1
            call ctc

            $ face_on_cg = False
            hide screen ccg
            call her_chibi_scene("sex_cum_in_done", trans=d5)
            pause.8

            call her_main("I apologise for saying that I hate you, [genie_name]...", "base", "base", "base", "R",cheeks="blush",tears="mascara",ypos="head",flip=False)
            call her_main("And your cock is not nasty...",cheeks="blush",tears="mascara")
            call her_main("I don't know what's gotten into me...", "grin", "narrow", "worried", "mid_soft",cheeks="blush",tears="mascara")
            g9 "My dick!"
            call her_main("I suppose it's as when you call me a \"whore\". I know you actually don't mean it...", "grin", "narrow", "worried", "mid_soft",cheeks="blush",tears="mascara")
            m "Yeah, sure..."
            m "Does it still hurt?"
            call her_main("A little...", "open", "narrow", "worried", "mid_soft",cheeks="blush",tears="mascara")
            call her_main("I also feel full and warm inside...", "grin", "closed", "base", "mid",cheeks="blush",tears="mascara")
            m "You plan to keep it in? My cum I mean."
            call her_main("Yes...", "grin", "narrow", "base", "mid_soft",cheeks="blush",tears="mascara")

            if daytime:
                call her_main("I hope it won't start leaking during my classes...",cheeks="blush",tears="mascara")
            else:
                call her_main("I hope it won't start leaking before I get to my room...",cheeks="blush",tears="mascara")

            m "Well, good luck on your journey."
            call her_main("Can I get paid now please?", "grin", "closed", "base", "mid",cheeks="blush",tears="mascara")

            return

        "-Pull out and cum on Hermione-":
            if not use_cgs:
                call her_chibi_scene("sex_cum_out", trans=d5)
            else:
                $ ccg3 = "s3"
            call cum_block
            call ctc
            

            call her_main("Ah...{heart}{heart}{heart}", "silly", "narrow", "base", "dead",ypos="head")
            g4 "Yes!!! All over your ass!"
            call her_main("Ah... It's so hot!", "silly", "narrow", "annoyed", "up")
            hide screen bld1
            with d1
            call ctc

            $ face_on_cg = False
            hide screen ccg
            call her_chibi_scene("sex_cum_in_done", trans=d5)
            pause.8

            m "Well, I'm done... You can get off my desk now."
            call her_main("Yes, [genie_name]...", "silly", "base", "worried", "mid", cheeks="blush",tears="soft",ypos="head",flip=False)
            m "You feeling alright?"
            call her_main("Yes, [genie_name]. It still hurts a little, but...", "shock", "base", "base", "R",cheeks="blush",tears="soft")
            m "But what?"
            call her_main("But in a good way... [genie_name].", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
            m "In a good way, huh?"
            g9 "Heh... You cute, little minx."
            call her_main("Can I get paid now, [genie_name]?", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")

            return



### Anal Sex Repeat ###

label hg_anal_sex_2:
    $ hg_pf_sex.change_icon(a="heart_yellow", b="heart_red")

    call her_chibi_scene("lie_on_desk")
    with d3

    call bld
    m "How about another assfuck, [hermione_name]?"
    call her_main("Of course, [genie_name].", "base", "narrow", "base", "up", ypos="head")
    g4 "*Hngh!* You little minx!"

    stop music fadeout 1.0
    hide screen hermione_main
    call blkfade

    call her_main("........", "annoyed", "base", "worried", "R")
    m "Hm..."
    call her_main("...........", "open", "base", "base", "mid")
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_main("Ooooohhhhhhhhhhhh....{heart}", "scream", "wide", "base", "stare")

    # Transition
    if use_cgs:
        $ face_on_cg = True
        $ ccg_folder = "herm_sex"
        $ ccg1 = "blank"
        $ ccg2 = "blank"
        $ ccg3 = "blank"
        show screen ccg
        hide screen blkfade
        call her_main("", "open", "closed", "base", "mid",ypos="head")
    else:
        call her_chibi_scene("sex_slow", trans=d5)

    g4 "Oh, ye-es!"
    call her_main("Ah...", "soft", "narrow", "annoyed", "up")
    m "It seems like your butthole became a bit more welcoming, [hermione_name]."
    call her_main("Ah... It still hurts a little.", "base", "narrow", "base", "mid_soft")
    call her_main("And please, just call me \"whore\", [genie_name].", "base", "squint", "base", "mid")
    g4 "Agh! You slut! You always get me with your words!"

    call play_music("playful_tension") # SEX THEME.
    call her_main("Ah... Ah...", "open", "closed", "base", "mid")
    call her_main("Ah...")
    call her_main("[genie_name]?", "base", "narrow", "base", "mid_soft")
    m "Yes, whore?"
    call her_main("Em...", "angry", "base", "base", "mid")
    call her_main("Would you marry me, [genie_name]?", "angry", "narrow", "base", "down")
    with hpunch
    g4 "{size=+9} WHAT?!{/size}"
    g4 "Don't tell me you're pregnant, [hermione_name]!"
    call her_main("I couldn't get pregnant the way we are doing it, [genie_name]...", "angry", "wink", "base", "mid")
    m "What is this talk of marriage then?"
    call her_main("You misunderstood me [genie_name].", "angry", "base", "base", "mid")
    call her_main("I meant to say, would you marry a girl {size=+5}like{/size} me?", "angry", "narrow", "base", "down")
    call her_main("I would never propose to a man with his cock in my ass, [genie_name]...", "angry", "worriedCl", "worried", "mid",emote="05")
    m "Good. Because I don't think any man would be able to say \"no\" then."
    call her_main("Ah{heart}...", "open", "closed", "base", "mid")
    call her_main("What I meant... ah{heart} {w} ...to say was ah{heart}... {w}...do you think someone would ever ah{heart}... {w} ...want to marry a girl like me?", "angry", "narrow", "base", "down")
    m "Huh?"
    call her_main("I mean, with all that was happening lately... ah{heart}...", "angry", "narrow", "base", "down")
    call her_main("I can't help but feel unclean... damaged even.")
    call her_main("And in a no way innocent...")
    call her_main("Who would want a wife like that?", "angry", "base", "base", "mid")

    menu:
        m "..."
        "\"I would marry you in a heartbeat!\"":
            call her_main("What?", "open", "base", "base", "mid",ypos="head")
            m "Well, hypothetically speaking of course..."
            call her_main("...of course...{heart}", "base", "base", "base", "R")
            call her_main("..............", "base", "happy", "base", "mid")
            call her_main("But why do you say that, [genie_name]?", "soft", "base", "base", "mid")
            m "Huh?"
            m "What do you mean \"why\", whore?"
            m "You are young and attractive..."
            m "Tight asshole, full tits and wet little pussy..."
            call her_main("Ah...{heart}", "open", "closed", "base", "mid")
            m "You will make some lucky guy a very happy man one day, whore."
            m "Ehm, I mean, [hermione_name]."
            call her_main("No, \"whore\" is good. Call me that, [genie_name].", "silly", "narrow", "annoyed", "up")
            m "There, you see? You are a great catch, I'm telling you, whore."
            call her_main("Ah...{heart} Thank you, [genie_name].", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            m "Huh?"
            m "Are you crying?"

        "\"Marriage is out of the picture for you.\"":
            call her_main("That's what I thought...", "shock", "narrow", "base", "down",cheeks="blush",tears="crying",ypos="head")
            m "Oh... I just love that little asshole of yours!"
            call her_main(".....................", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            call her_main("Yes... After all the things I had to do for my house...")
            call her_main("...no one will ever want me...", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            m "Oh, they will want you alright!"
            call her_main("What? But you said...", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            m "Marriage, [hermione_name]. Marriage is impossible for you."
            m "But as a man-pleaser you are a great catch!"
            call her_main("Really?", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            m "Are you kidding me?!"
            m "Young, hot and slutty. You could have any man you want!"
            m "Or a wizard or whatever you are into..."
            call her_main("I think you may be right, [genie_name].", "base", "narrow", "worried", "mid_soft",cheeks="blush",tears="soft")
            m "I know I am right, whore."
            m "Now wiggle that little ass of yours a little."
            call her_main("Like this?", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
            m  "Yes, that's a good whore."
            call her_main("I am a whore, aren't I?", "silly", "narrow", "base", "dead")
            m "You just sold me your asshole for ninety house points. How would you call that?"
            call her_main("Yes, yes...{heart} I am a whore...{heart}", "silly", "base", "worried", "mid", cheeks="blush",tears="soft")
            m "Are you crying?"

    call her_main("Among other things, [genie_name]...{heart}{heart}{heart}", "silly", "narrow", "base", "dead",ypos="head")
    m "Among other things?"
    call her_main("I'm cumming [genie_name]...{heart}{heart}{heart}", "open_wide_tongue", "narrow", "annoyed", "up")
    g4 "Agh! My cock!"
    g4 "Relax your muscles a little, would you?"
    call her_main("BUT I'M CUMMING!{heart}{heart}{heart}", "open", "worriedCl", "worried", "mid")
    g4 "Fine! Have it your way whore!"
    with hpunch
    call her_main("{size=+7}Ah-ah-aha!!! I'm cumming!!!{/size}", "scream", "wide", "base", "stare")
    g4 "{size=+7}Argh!{/size}"

    menu:
        g4 "!!!"
        "-Fill Hermione up with cum-":
            if not use_cgs:
                call her_chibi_scene("sex_cum_in", trans=d5)
            else:
                $ ccg3 = "s1"
            call cum_block
            call ctc

            #
            # TODO: CUM LAYERS
            #

            call her_main("!!!", "scream", "wide", "base", "stare",ypos="head")
            m "Yes! Argh!"
            call her_main("Ah!{heart} It's filling me up!{heart} I can feel it!{heart}", "silly", "narrow", "annoyed", "up")
            m "Shut up, whore!"
            call her_main("Ah! I AM A WHORE!!!!{heart}{heart}{heart}", "scream", "worriedCl", "worried", "mid",cheeks="blush",tears="crying")
            m "Agh!"
            call her_main("Ah...{heart} your cum, [genie_name]...{heart}", "open", "wide", "worried", "stare",cheeks="blush",tears="messy")
            m "Yes, yes..."
            call her_main("Ah...{heart}", "angry", "squint", "base", "mid",cheeks="blush",tears="messy")
            m "......"

        "-Cum all over Hermione-":
            if not use_cgs:
                call her_chibi_scene("sex_cum_out", trans=d5)
            else:
                $ ccg3 = "s3"
            call cum_block
            call ctc

            #
            # TODO: CUM LAYERS
            #

            call her_main("Ah-aha! You're cumming! {heart}{heart}{heart}", "silly", "narrow", "base", "dead",ypos="head")
            g4 "{size=+7}Yes I am, whore!{/size}"
            call her_main("Ah, me too! Me too!", "scream", "worriedCl", "worried", "mid",cheeks="blush",tears="messy")
            g4 "{size=+7}FUCKING SLUT!{/size}"
            call her_main("Ah...{heart} your cum...{heart}", "angry", "narrow", "base", "dead",cheeks="blush",tears="crying")
            call her_main("I'm so full...{heart}{heart}{heart}")
            g4 "Yes!!! All over your ass!"
            call her_main("Ah... It's so hot!", "silly", "narrow", "annoyed", "up")

    #Ending
    call hide_characters
    show screen blkfade
    with d7

    $ face_on_cg = False
    hide screen ccg
    call her_chibi_scene("sex_pause", trans=fade)

    m "Well, this was intense..."
    call her_main("Ah-ha...{heart} ah...{heart}", "grin", "narrow", "base", "dead",cheeks="blush",tears="messy",ypos="head",flip=False)
    m "Are You alright, [hermione_name]?"
    call her_main("I think so... I'm not sure...", "grin", "narrow", "base", "dead",cheeks="blush",tears="messy")
    call her_main("I think I may still be cumming, [genie_name].", "grin", "narrow", "base", "dead",cheeks="blush",tears="messy")
    call her_main("Or maybe not...", "grin", "narrow", "base", "dead",cheeks="blush",tears="messy")
    call her_main("Everything is in a daze... and my legs feel so weak...")
    call her_main("Can I just get paid now, [genie_name]?")

    return

# label hg_pf_anal_sex_old: # Writing not in use
    # m "[hermione_name]?"
    # call her_main("[genie_name]?", "soft", "base", "base", "mid")
    # m "I will be buying another favour from you today..."
    # call her_main(".............", "open", "squint", "base", "mid")
    # m "Care to guess what the favour will be?"
    # m "You have three attempts to find out."
    # call her_main("...........", "annoyed", "squint", "angry", "mid")
    # call her_main("Anal sex?", "disgust", "narrow", "base", "mid_soft")
    # g4 "Wha..........?!"
    # g4 "How did you...?"
    # call her_main("Just a lucky guess, [genie_name]...", "angry", "base", "angry", "mid")
    # m "Sometimes you scare me, [hermione_name]..."