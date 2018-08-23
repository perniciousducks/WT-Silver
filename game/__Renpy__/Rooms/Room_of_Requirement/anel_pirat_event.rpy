label anal_parit_event: #LV.8 (Whoring = 21 - 23)
    call hide_room_req
    show screen main_room
    show screen genie
    show screen blkfade

    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.
    
    $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "sex_slow_ani"
    
    nar "This story is a rewrite of the \"Time for anal\" Private favour. And the genie is a pirate? Who knows... Enjoy."
    
    menu:
        "Path 1":
            $ pathvalue = 0 
        "Path 2":
            $ pathvalue = 1
        "Path 3":
            $ pathvalue = 2
            
    call hide_blkfade
    
    #Intro
    if pathvalue == 0:
        m "[hermione_name]...I'd like you to roleplay with me."
        call her_main("[genie_name]..?","annoyed","suspicious")
        m "How familiar ye be wit' th' term \" Swabbing ye poop deck\"?"


        call her_main("90 galleon points...","annoyed","annoyed")
        m "Wha'?"
        call her_main(".............................","disgust","glance")
        m "Ah, well then lass. 90 galleon points 'tis."
        hide screen hermione_main

        label lucky_anal_guess:
        call set_hermione_outfit(hg_pirate_OBJ)
        call blkfade
        stop music fadeout 1.0
        call hide_blkfade
        
        call her_head("...........","annoyed","worriedL")
        m "Time to get me ole canon out..."
        call her_head(".................","angry","worriedCl",emote="05")
        m "Hm..."
        call her_head("!!!","angry","wide")
        g4 "Blistering barnacles"
        call her_head("Ouch!","mad","worriedCl",tears="soft_blink")
        m "Jus' try t' loosen up a wee, would ye?"
        call her_head("I be tryin'!","angry","base",tears="soft")
        m "Aye, wha' if I do this..?"
        call her_head("Ouch! Wha' are ye doin', [genie_name]?","mad","worriedCl",tears="soft_blink")
        m "Aye, this won't work either..."
        m "Hm..."
        m "Har har, I reckon I know wha' we should do."
        m "..."
        menu:
            "\"I reckon I'll raise the anchor 'n jus' set sail!\"":
                call play_music("playful_tension") # SEX THEME.
                call her_head("Just set sail, [genie_name]?!","angry","wide")
                $ renpy.play('sounds/spit.mp3') #Sound of spiting.
                g4 "*SPIT!*"
                call her_head("What are ye doing you Seadog!","scream","worriedCl")
                call her_head("No, [genie_name], Belay that! You're not in open waters--","open","base")
                m "No needs, raise the anchor! Heave Ho!"
                with hpunch
                call her_head("ARGH!","angry","base",tears="soft")
                call her_head("Ouch! Ouch! Ouch!","mad","worriedCl",tears="soft_blink")
                g4 "Nigh-on in! Me ship has left ye harbour lass!"
                call her_head("No, ye're hurtin' me! Ye be hurtin' me!","scream","worriedCl")
                g4 "Yo Ho Ho!"
                call her_head("Blisterin' Barnacles! It hurts!","scream","worriedCl")
                g4 "Shut it, [hermione_name]! I be approaching ye cavern!"
                g4 "Yer cavern be so tight 'tis completely un-plunderable!"
                call her_head("Then stop, Scallywag!","mad","worriedCl",tears="soft_blink")
                m "Neigh! We needs t' excavate yer cavern a wee!"
                call her_head("But I don't wants ye t'!","mad","worriedCl",tears="soft_blink")
                m "Aye? How do ye expect scallywags t' farrg ye up yer arse then?"
                call her_head("Wha' scallywags?shock","worriedCl")
                g4 "Ye know... scallywags."
                g4 "Argh, Blimey... Me canon be to wide now."
                call her_head("Stop then! Avast, [genie_name]!","open","worriedCl")
                call her_head("Change course captain, I've changed me mind! I don't needs 90 galleon points!")
                g4 "I reckon I be nigh-on..."

                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                call her_head("{size=+5}AAAAAAAAhhhhh!!!{/size}","scream","wide")
                g4 "Yo Ho Ho!!!"
                call her_head("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!","scream","wide")
                g4 "Let us pump this wee cavern full o' seamen then, savvy?"
                call her_head("Aye... , I jus' wants this t' end...","scream","worriedCl",cheeks="blush",tears="crying")

                call blkfade
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u

                if use_cgs:
                    hide screen candlefire
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_head("","shock","baseL",cheeks="blush",tears="soft")
                    show screen ccg

                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc
                call hide_blkfade

                #SCHUSH!
                g4 "Agh... Ye wants this voyage t' end sooner?"
                g4 "I smell mutiny, do ye want to walk the plank?"
                call her_head("*sob!* How?","shock","baseL",cheeks="blush",tears="soft")
                g4 "Ye know..."
                call her_head("Aye...","shock","baseL",cheeks="blush",tears="soft")
                #$ ccg2 = 6
                call her_head("I be a wench??","clench","worried",cheeks="blush",tears="soft")
                g9 "Yes ye be!"
                call her_head("*Sob!* I be a wench...","angry","suspicious",cheeks="blush")
                call her_head("I love t' suck ye pegleg...")
                call her_head("'n now me wee asshole be gettin' ripped t' pieces... *Sob!*","angry","dead",cheeks="blush",tears="crying")
                g4 "Shiver Me Timbers!"
                g4 "Agrh! Thar She Blows!"
                call her_head("No! Be it gettin' bigger?! I be like a harpoon!","open","surprised",cheeks="blush",tears="messy")
                g4 "ARGH!"

            "\"Lather me canon balls first. Lubricate me pegleg!\"":
                call her_head("Oh... Alright...","open","base")
                call play_music("playful_tension") # SEX THEME.

                #SUCKING
                call her_chibi("hide")
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen g_c_u

                hide screen blktone
                hide screen bld1
                call hide_blkfade
                call ctc

                call her_head("*Slurp!* *Slurp!* *Slurp!*")
                m "Aye... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Yarr, I reckon that be enough. Back on th' ship now."
                call blkfade

                #ON THE DESK
                call her_head(".............","open","base")
                g4 "Aye! Sail, Ho!!"
                call her_head("Ouch!","scream","worriedCl")
                m "Relax lass. Approaching harbour."

                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                call her_head("{size=+5}AAAAAAAAhhhhh!!!{/size}","scream","wide")
                g4 "Argh!!!"
                call her_head("Ye... ye...","scream","wide")
                call her_head("Ye ship is to vast","shock","worriedCl")
                g4 "Let us pump this wee cavern full o' seamen then, savvy?"
                call her_head(".....................","angry","suspicious",cheeks="blush")
                
                
                # SEX
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u

                if use_cgs:
                    hide screen candlefire
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_head("","shock","baseL",cheeks="blush",tears="soft")
                    show screen ccg

                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc

                call her_head(".....................","shock","baseL",cheeks="blush",tears="soft")
                m "Ye be fine thar, wench?"
                call her_head("Blisterin' Barnacles... Ye be... turnin' me folds inside out... [genie_name].","clench","worried",cheeks="blush",tears="soft")
                call her_head("Me stitches be breaking","angry","suspicious",cheeks="blush")
                m "Aye..."
                m "Maybe me canon needs swabbin'...?"
                m "Go below deck, [hermione_name]. swabb me canon some more."
                call her_head("Wha'? But...","clench","worried",cheeks="blush",tears="soft")
                call her_head("But it be rusty... 'tis been in me bilge.","shock","baseL",cheeks="blush",tears="soft")
                m "Aye, 'tis been abaft, but that's nah nigh ye bilge."
                m "Heave ho landlubber or me ship be sinkin', [hermione_name]. Swab me canon some more."
                call her_head("...........","shock","baseL",cheeks="blush",tears="soft")
                call blkfade

                #SUCKING
                hide screen ccg
                $ face_on_cg = False
                hide screen hermione_face
                call h_update_hair
                call her_chibi("hide")
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen g_c_u

                hide screen blktone
                hide screen bld1
                call hide_blkfade
                call ctc

                call her_head("*Slurp!* *Slurp!* *Slurp!*",xpos="base",ypos="base")
                m "Aye... good lass..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Can ye taste yer arse on me canon?"
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Aye, Maybe that be enough."
                call blkfade

                # SEX
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left

                $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u

                if use_cgs:
                    hide screen candlefire
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_head("","shock","baseL",cheeks="blush",tears="soft")
                    show screen ccg

                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc

                call her_head("Ah...","shock","baseL",cheeks="blush",tears="soft")
                m "We be smooth sailing lass?"
                call her_head("It still be hurting...","clench","worried",cheeks="blush",tears="soft")
                call her_head("But th' storm has passed.")
                m "I'll adjust th' sails fer now..."
                call her_head("Ah... I be greatful, [genie_name].","angry","suspicious",cheeks="blush")
                m "Oh... aye... this cavern be great..."
                call her_head("...........","shock","baseL",cheeks="blush",tears="soft")
                m "Oh... Ye cavern be perfect, lass..."
                call her_head("................","shock","down_raised",cheeks="blush",tears="crying")
                m "Why are ye bein' so quiet [hermione_name]?"
                call her_head("'cause 'tis cavern be to small for ye ship...","clench","worried",cheeks="blush",tears="soft")
                call her_head("'N I jus' wants ye t' cum sooner, [genie_name]...")
                m "So ye stifle yer cries o' pain?"
                call her_head("Aye [genie_name]. *Sob!*","angry","dead",cheeks="blush",tears="crying")
                m "Nah on me ship lass."
                m "Sob, scream 'n cry as much as ye wish!"
                call her_head("B-but--","clench","worried",cheeks="blush",tears="soft")
                m "That shall make me canon ready t' fire in ye broadside."
                call her_head("be this true? *Sob!*","angry","dead",cheeks="blush",tears="crying")
                call her_head("*Sob!* Me hull! *Sob!* It be taking in water! *Sob!*","shock","baseL",cheeks="blush",tears="soft")
                m "Aye, ye ship be sinking... ye booty be mine."
                call her_head("*SOB!*","angry","suspicious",cheeks="blush",tears="messy")
                m "Ye poor wee sprog..."
                m "A grand, wicked pirate be plunderin' yer booty!"
                call her_head("*SOB!* Yeees! *SOB!*","scream","suspicious",cheeks="blush",tears="messy")
                g4 "Take my booty!"
                call her_head("No, I'm scared! *SOB!*","scream","worriedCl",cheeks="blush",tears="messy")

        menu:
            "-Fill Hermione up with cum-":
                g4 "Argh!"
                call her_head("No! AH!","scream","wide")
                call cum_block
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

                $ g_c_u_pic = "sex_cum_in_ani"
                hide screen bld1
                with d3

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_head("AH! ME BILGE IS FILLING UP! Sink Me!{image=textheart}{image=textheart}{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                g4 "Aye, ye wench! I be shooting me canons!"
                call her_head("Me hull is splintering, spare me Captain!","angry","suspicious",cheeks="blush",tears="messy")
                g4 "Ye're nah sunk yet!"
                with hpunch
                call her_head("No, I be already full! Stop cummin', ye bastard!","scream","surprised",cheeks="blush",tears="messy")
                g4 "Shut th' farrg up, wench! Ye still be afloat!"
                call her_head("No! Me stomach! Me ship will capsize!","scream","suspicious",cheeks="blush",tears="messy")
                g4 "ARGH!"
                call her_head("No! I reckon me bilge be flooded... I must get t' me pumps.","open","surprised",cheeks="blush",tears="messy")
                with hpunch
                play sound "sounds/burp.mp3"
                call her_head("{size=+7}*BURP!*!!!!!{/size}","full","surprised",tears="messy")
                call her_head(".......................","full","base",tears="messy")
                call her_head(".............")
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                call her_head("{size=+7}*GULP!*{/size}","cum","worriedCl")
                call her_head("*SOB!* I HATE YOU...","angry","suspicious",cheeks="blush",tears="messy")
                call her_head("{size=+5}I HATE YE'N AND YER RUSTY OLE CANON!{/size}","scream","angry",cheeks="blush",tears="messy")
                call her_head("{size=+5}I HATE YE'N! YE HEAR ME?!{/size}")
                g4 "Agh... Dead men tell no tales, wench!"
                call her_head("*sob!* *Sob!*...","angry","suspicious",cheeks="blush",tears="messy")

                # AFTER CUM INSIDE
                hide screen bld1
                with d3
                call ctc

                $ g_c_u_pic = "ani_her_sex_cum_inside_blink"

                call her_head("*Sob!*...","angry","dead",cheeks="blush",tears="crying")
                m "Whew!... I reckon me gunpowder needs restocking in the next harbour.' it be."
                m "Ye afloat lass?"
                call her_head("Aye... *Sob!*","angry","dead",cheeks="blush",tears="crying")
                m "Is that sea water in ye eyes?"
                call her_head("Me bilge is flooded, but me pumps be workin, [genie_name]...","angry","dead",cheeks="blush",tears="crying")
                m "Aye, ye took me canonfire broadside, Ye be a well built vessel ..."
                call her_head("Thank ye captain...","angry","dead",cheeks="blush",tears="crying")
                hide screen bld1
                with d3
                call ctc

                call blkfade
                $ face_on_cg = False
                hide screen hermione_face
                call h_update
                call h_update_hair

                call her_head("I apologize for saying that I hate you, [genie_name]...","base","baseL",cheeks="blush",tears="mascara",xpos="base",ypos="base")
                call her_head("And your canon is not rusty...",cheeks="blush",tears="mascara")
                call her_head("I don't know what's gotten into me...","grin","concerned",cheeks="blush",tears="mascara")
                g9 "My canonfire!"
                call her_head("I suppose it's when you call me a \"wench\". I know that it's just roleplay...","grin","concerned",cheeks="blush",tears="mascara")
                m "Aye, sure..."
                m "Does it still hurt?"
                call her_head("A little...","open","concerned",cheeks="blush",tears="mascara")
                call her_head("I also feel full and warm inside...","grin","closed",cheeks="blush",tears="mascara")
                m "You plan to keep it in? My cum I mean."
                call her_head("Aye..","grin","glance",cheeks="blush",tears="mascara")

                if daytime:
                    call her_head("I hope I won't spring a leak during my classes...",cheeks="blush",tears="mascara")
                else:
                    call her_head("I hope it won't spring a leak before I get to my cabin...",cheeks="blush",tears="mascara")

                m "Well, good luck on your voyage."
                call her_head("Can I get paid now please?","grin","closed",cheeks="blush",tears="mascara")

            "-Pull out and cum on Hermione-":
                $ g_c_u_pic = "sex_cum_out_ani"
                hide screen bld1
                with d3

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                g4 "Aye!!! Allover yer hold!"
                call her_head("Ah... No, me cargo!","silly","ahegao")
                hide screen bld1
                with d3
                call ctc

                call blkfade

                call blkfade
                $ face_on_cg = False
                hide screen hermione_face
                call h_update
                call h_update_hair

                m "Well, I'm done... You can get off my ship now."
                call her_head("Yes, [genie_name]...","silly","worried",cheeks="blush",tears="soft",xpos="base",ypos="base")
                m "You feeling alright?"
                call her_head("Yes, [genie_name]. It still hurts a little, but...","shock","baseL",cheeks="blush",tears="soft")
                m "But what?"
                call her_head("But in a good way... [genie_name].","silly","worried",cheeks="blush",tears="soft")
                m "In a good way, huh?"
                g9 "Heh... You naughty, little pirate."
                call her_head("Can I my share of the booty now, [genie_name]?","silly","worried",cheeks="blush",tears="soft")

    #Second time event.
    elif pathvalue == 1:
        m "[hermione_name]?"
        call her_main("[genie_name]?","soft","base")
        m "I shall be takin' ye on another voyage today..."
        call her_main(".............","open","suspicious")
        m "Care t' guess wha' th' destination will be?"
        m "You have t' guess three times to find out."
        call her_main("...........","annoyed","frown")
        call her_main("Booty plundering?","disgust","glance")
        g4 "Wha..........?!"
        g4 "How did ye...?"
        call her_main("You seem like a butt pirate sort of a man. [genie_name]...","angry","angry")
        m "I'm not sure you know what that means, [hermione_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        jump lucky_anal_guess

    #Third time event.
    elif pathvalue == 2:
        m "How about another booty plunderin, [hermione_name]?"
        call her_main("Of course, [genie_name].","base","ahegao_raised")
        g9 "Raise anchor, you little mynx!"
        
        hide screen hermione_main
        call set_hermione_outfit(hg_pirate_OBJ)
        call blkfade
        
        stop music fadeout 1.0

        call her_head("........","annoyed","worriedL")
        m "Hm..."
        call her_head("...........","open","base")
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide")
        g4 "Oh, ye-es!"
        call her_head("Ah...","soft","ahegao")
        m "It seems like yer cavern be a bit more welcomin', [hermione_name]."
        call her_head("Ah... It still be a bit tight.","base","glance")
        call her_head("'n , jus' call me \"wench\", [genie_name].","base","suspicious")
        g4 "Agh! Ye wench! Ye always get me wit' yer words!"

        call her_chibi("hide")
        hide screen genie
        show screen chair_left

        $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen g_c_u

        if use_cgs:
            hide screen candlefire
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_head("","open","closed")
            show screen ccg

        hide screen blktone
        hide screen bld1
        call hide_blkfade
        call ctc

        call play_music("playful_tension") # SEX THEME.

        #INSERTION
        call her_head("Ah... Ah...","open","closed")
        call her_head("Ah...")
        call her_head("[genie_name]?","base","glance")
        m "Aye, wench?"
        call her_head("Em...","angry","base")
        call her_head("Would ye settle down for me, [genie_name]?","angry","down_raised")
        with hpunch
        g4 "{size=+9} WHAT?!{/size}"
        g4 "Don't tell me ye're expecting cargo, [hermione_name]!"
        call her_head("Ye seamen don't put no cargo in me bilge, [genie_name]...","angry","wink")
        m "Wha' be this natter o' settlin down then?"
        call her_head("Ye misunderstood me [genie_name].","angry","base")
        call her_head("I meant t' say, would ye stop plunderin for a lass {size=+5}like{/size} me?","angry","down_raised")
        call her_head("I would ne'er propose t' a scallywag wit' his pegleg in me arse, [genie_name]...","angry","worriedCl",emote="05")
        m "Good. 'cause I don't reckon any scallywag would be able t' say \"neigh\" to you lassie."
        call her_head("Ah{image=textheart}...","open","closed")
        call her_head("Wha' I meant... ah{image=textheart} {w} ...t' say was ah{image=textheart}... {w}...do ye reckon any pirate would ever ah{image=textheart}... {w} ...leave th' sea fer a lass like me?","angry","down_raised")
        m "Huh?"
        call her_head("I mean, wit' all that plunderin happenin' lately... ah{image=textheart}...","angry","down_raised")
        call her_head("I can nah help but feel like me hull is scratched... leakin even.")
        call her_head("'n in a no way untarnished...")
        call her_head("Who would wants t' settle fer a lass like that.","angry","base")

        menu:
            m "..."
            "\"I would leave me ship in a heartbeat!\"":
                call her_head("What?","open","base")
                m "Aye, if only a lass like ye would board me ship..."
                call her_head("...Aye...{image=textheart}","base","baseL")
                call her_head("..............","base","squint")
                call her_head("Aye if only a lass like I, [genie_name]?","soft","base")
                m "Huh?"
                m "Wha' do ye mean \"why\", wench?"
                m "Ye be right out of harbour 'n ye only just set sail..."
                m "Tight cabin, shimering tits, 'n wet wee powder pan..."
                call her_head("Ah...{image=textheart}","open","closed")
                m "Ye will make some lucky scallywag a mighty happy one, some day, wench."
                m "Ehm, I mean, [hermione_name]."
                call her_head("No, \"wench\" be good. you be calling me that more, [genie_name].","silly","ahegao")
                m "Thar, ye see? Ye be a great catch, I be tellin' ye, wench."
                call her_head("Ah...{image=textheart} Thank you, [genie_name].","angry","dead",cheeks="blush",tears="crying")
                m "Huh?"
                m "Ye helm be leakin."
                label among_anal_other_things:
                call her_head("Not only me helm, [genie_name]...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                m "Not just ye helm?"
                call her_head("I'm cumming [genie_name]...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
                g4 "Agh! My cock!"
                g4 "Relax your muscles a little, would you?"
                call her_head("BUT I'M CUMMING!{image=textheart}{image=textheart}{image=textheart}","open","worriedCl")
                g4 "Fine! 'ave it yer way wench!"
                with hpunch
                call her_head("{size=+7}Ah-ah-aha!!! I'm cumming!!!{/size}","scream","wide")
                g4 "{size=+7}Argh!{/size}"

            "\"A pirate nah plunderin t' be wit' ye be o' th' picture\"":
                call her_head("I be thinkin that...","shock","down_raised",cheeks="blush",tears="crying")
                m "Oh... I jus' love that wee cavern o' yers!"
                call her_head(".....................","angry","dead",cheeks="blush",tears="crying")
                call her_head("Aye... Aft all th' thin's I had t' do fer me ship...")
                call her_head("...nah one we pirate would leave th' sea fer me...","angry","suspicious",cheeks="blush",tears="messy")
                m "Oh, they be leavin th's sea fer ye alright!"
                call her_head("Wha'? But ye said...","open","surprised",cheeks="blush",tears="messy")
                m "T' plunder yer cave, [hermione_name]. But they'd go back t' sea."
                m "But as a canon swabber ye be a great catch!"
                call her_head("Aye?","open","surprised",cheeks="blush",tears="messy")
                m "Ye pullin' me peglet?!"
                m "Young, hot 'n slutty. Ye could 'ave any scallywag ye wants!"
                m "Or a landlubber or whatever ye be into..."
                call her_head("I reckon ye may be right, [genie_name].","base","concerned",cheeks="blush",tears="soft")
                m "I always be right, wench."
                m "Now wiggle that wee arse o' yers a wee."
                call her_head("Like this?","silly","worried",cheeks="blush",tears="soft")
                m  "Aye, that be a good wench."
                call her_head("I be a wench, aren't I?","silly","dead")
                m "Ye jus' sold me yer asshole fer 90 galleon points. What ye be calling that?"
                call her_head("Yes, yes...{image=textheart} I be nothing but a wench...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
                m "Ye helm be leakin."
                jump among_anal_other_things

        menu:
            g4 "!!!"
            "-Fill Hermione up with cum-":
                hide screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_in_ani"

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_head("!!!","scream","wide")
                m "Shiver me timbers! Argh!"
                call her_head("Ah!{image=textheart} 'tis fillin' me up!{image=textheart} me bilge is takin in water!{image=textheart}","silly","ahegao")
                m "'tis nah water, wench!"
                call her_head("Ah! I BE A WENCH!!!!{image=textheart}{image=textheart}{image=textheart}","scream","worriedCl",cheeks="blush",tears="crying")
                m "Agh!"
                call her_head("Ah...{image=textheart} yer seamen, [genie_name]...{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                m "Aye, my semen..."
                call her_head("Ah...{image=textheart}","angry","suspicious",cheeks="blush",tears="messy")
                m "......"
                hide screen bld1
                with d3
                call ctc

                call blkfade

            "-Cum all over Hermione-":
                hide screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_ani"

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_head("Ah-aha! Ye're cummin'! {image=textheart}{image=textheart}{image=textheart}","silly","dead")
                g4 "{size=+7}Aye I do, wench{/size}"
                call her_head("Blisterin' Barnacles, me too! Me too!","scream","worriedCl",cheeks="blush",tears="messy")
                g4 "{size=+7}FARRRGIN' WENCH!{/size}"
                call her_head("Ah...{image=textheart} yer cum...{image=textheart}","angry","dead",cheeks="blush",tears="crying")
                call her_head("Ye covered me whole deck{image=textheart}{image=textheart}{image=textheart}")
                g4 "Aye!!! All o'er yer hull!"
                call her_head("Shiver me timbers... 'tis so hot!","silly","ahegao")
                hide screen bld1
                with d3
                call ctc

                call blkfade

        #Ending
        $ face_on_cg = False
        call h_update_hair

        m "Well, tis been intense..."
        call her_head("Ah-ha...{image=textheart} ah...{image=textheart}","grin","dead",cheeks="blush",tears="messy",xpos="base",ypos="base")
        m "Ye be fine lass?"
        call her_head("I reckon so... I be nah sure...","grin","dead",cheeks="blush",tears="messy")
        call her_head("I reckon I may still be leakin', [genie_name].","grin","dead",cheeks="blush",tears="messy")
        call her_head("Or maybe nah...","grin","dead",cheeks="blush",tears="messy")
        call her_head("Everythin' be in a daze... 'n me legs feel so weak...")
        if whoring < 24:
            her "Can I jus' get paid now, [genie_name]?"
        stop music fadeout 1.0


    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    hide screen ccg
    if not daytime:
        show screen candlefire

    call her_chibi("stand","desk","base")
    show screen genie
    call hide_blkfade


    call her_main("Thank you, [genie_name]...","angry","suspicious",cheeks="blush",xpos="right",ypos="base")

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    $ custom_outfit_old = temp_outfit

    hide screen main_room
    jump enter_room_of_req