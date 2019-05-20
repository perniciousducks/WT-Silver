

label anal_parit_event: #LV.8 (Whoring = 21 - 23)
    call room("main_room")
    show screen blkfade
    with d3

    call reset_menu_position

    $ gen_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ g_c_u_pic = "sex_slow_ani"

    nar "This story is a rewrite of the \"Time for anal\" Private favour. And the genie is a pirate? Who knows... Enjoy."


    menu:
        "Path 1":
            $ pathvalue = 0
        "Path 2":
            $ pathvalue = 1
        "Path 3":
            $ pathvalue = 2
    call music_block
    call her_chibi("stand","mid","base")
    call hide_blkfade

    #Intro
    if pathvalue == 0:
        m "lass...I'd like you to roleplay with me."
        call her_main("captain..?","annoyed","suspicious")
        m "How familiar ye be wit' th' term \" Swabbing ye poop deck\"?"


        call her_main("90 galleon points...","annoyed","annoyed")
        m "Wha'?"
        call her_main(".............................","disgust","glance")
        m "Ah, well then lass. 90 galleon points 'tis."
        call blkfade
        hide screen hermione_main
        $ renpy.play('sounds/cloth_sound.mp3')
        pause 2
        label lucky_anal_guess:
        call h_equip_temp_outfit(hg_outfit_pirate_ITEM)
        call hide_blkfade

        call her_main("...........","annoyed","worriedL")
        m "Time to get me ole canon out..."
        call her_main(".................","angry","worriedCl",emote="05")
        call blkfade
        call play_sound("climb_desk")
        pause 2
        m "Hm..."
        $ renpy.play('sounds/boing02.mp3')
        call her_main("!!!","angry","wide", ypos="head")
        call play_sound("slap")
        g4 "Blistering barnacles!"
        call her_main("Ouch!","mad","worriedCl",tears="soft_blink")
        m "Jus' try t' loosen up a wee, would ye?"
        call her_main("I be tryin'!","angry","base",tears="soft")
        m "Aye, wha' if I do this..?"
        $ renpy.play('sounds/boing03.mp3')
        call her_main("Ouch! Wha' are ye doin', captain?","mad","worriedCl",tears="soft_blink")
        m "Aye, this won't work either..."
        m "Hm..."
        m "Har har, I reckon I know wha' we should do."
        m "..."
        menu:
            "\"I reckon I'll raise the anchor 'n jus' set sail!\"":
                play music "music/pirate.mp3" fadein 1 fadeout 1
                play bg_sounds "sounds/CreakingShip.mp3"
                call her_main("Just set sail, captain?!","angry","wide",ypos="head")
                $ renpy.play('sounds/spit.mp3') #Sound of spiting.
                g4 "*SPIT!*"
                call her_main("What are ye doing you Seadog!","scream","worriedCl")
                call her_main("No, cap'n, Belay that! Ye're nah in open waters--","open","base")
                m "No needs, raise the anchor! Heave Ho!"
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                call her_main("ARGH!","angry","base",tears="soft")
                call her_main("Ouch! Ouch! Ouch!","mad","worriedCl",tears="soft_blink")
                g4 "Nigh-on in! Me ship has left ye harbour lass!"
                call her_main("No, ye're hurtin' me! Ye be hurtin' me!","scream","worriedCl")
                g4 "Yo Ho Ho!"
                call her_main("Blisterin' Barnacles! It hurts!","scream","worriedCl")
                g4 "Shut it, lass! I be approaching ye secret cavern!"
                g4 "Yer cavern be so tight 'tis completely un-plunderable!"
                call her_main("Then stop, Scallywag!","mad","worriedCl",tears="soft_blink")
                m "Neigh! We needs t' excavate yer cavern a wee!"
                call her_main("But I don't wants ye t'!","mad","worriedCl",tears="soft_blink")
                m "Aye? How do ye expect scallywags t' farrg ye up yer arse then?"
                call her_main("Wha' scallywags?","shock","worriedCl")
                g4 "Ye know... scallywags."
                g4 "Argh, Blimey... Me canon be to wide now."
                call her_main("Stop then! Avast, captain!","open","worriedCl")
                call her_main("Change course captain, I've changed me mind! I don't needs 90 galleon points!")
                g4 "I reckon I be right on course..."

                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                call her_main("{size=+5}AAAAAAAAhhhhh!!!{/size}","scream","wide")
                g4 "Yo Ho Ho!!!"
                call her_main("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!","scream","wide")
                g4 "Let us pump this wee cavern full o' seamen then, savvy?"
                call her_main("Aye... , I jus' wants this t' end...","scream","worriedCl",cheeks="blush",tears="crying")

                call blkfade
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left

                $ gen_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ gen_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u

                if use_cgs:
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_main("","shock","baseL",cheeks="blush",tears="soft",ypos="head")
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
                call her_main("*sob!* How?","shock","baseL",cheeks="blush",tears="soft")
                g4 "Ye know..."
                call her_main("Aye...","shock","baseL",cheeks="blush",tears="soft")
                #$ ccg2 = 6
                call her_main("I be a wench??","clench","worried",cheeks="blush",tears="soft")
                g9 "Yes ye be!"
                call her_main("*Sob!* I be a wench...","angry","suspicious",cheeks="blush")
                call her_main("I love t' suck ye pegleg...")
                call her_main("'n now me wee asshole be gettin' ripped t' pieces... *Sob!*","angry","dead",cheeks="blush",tears="crying")
                g4 "Shiver Me Timbers!"
                g4 "Agrh! Thar She Blows!"
                call her_main("No! Be it gettin' bigger?! I be like a harpoon!","open","surprised",cheeks="blush",tears="messy")
                g4 "ARGH!"

            "\"Lather me canon balls first. Lubricate me pegleg!\"":
                call her_main("Oh... Alright...","open","base",ypos="head")
                play music "music/pirate.mp3" fadein 1 fadeout 1
                play bg_sounds "sounds/CreakingShip.mp3"

                #SUCKING
                call her_chibi("hide")
                hide screen genie
                show screen chair_left

                $ gen_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
                $ gen_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen g_c_u

                hide screen blktone
                hide screen bld1
                call hide_blkfade
                call ctc

                call her_main("*Slurp!* *Slurp!* *Slurp!*")
                m "Aye... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Yarr, I reckon that be enough. Back on th' ship now."
                call blkfade

                #ON THE DESK
                call her_main(".............","open","base")
                g4 "Aye! Sail, Ho!!"
                call her_main("Ouch!","scream","worriedCl")
                m "Relax lass. Approaching harbour."

                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                call her_main("{size=+5}AAAAAAAAhhhhh!!!{/size}","scream","wide")
                g4 "Argh!!!"
                call her_main("Ye... ye...","scream","wide")
                call her_main("Ye ship be to great","shock","worriedCl")
                g4 "Let us pump this wee cavern full o' seamen then, savvy?"
                call her_main(".....................","angry","suspicious",cheeks="blush")


                # SEX
                call her_chibi("hide") #HERMIONE
                hide screen genie
                show screen chair_left

                $ gen_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ gen_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u

                if use_cgs:
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_main("","shock","baseL",cheeks="blush",tears="soft",ypos="head")
                    show screen ccg

                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc

                call her_main(".....................","shock","baseL",cheeks="blush",tears="soft")
                m "Ye be fine thar, wench?"
                call her_main("Blisterin' Barnacles... Ye be... turnin' me folds inside out... captain.","clench","worried",cheeks="blush",tears="soft")
                call her_main("Me stitches be breaking","angry","suspicious",cheeks="blush")
                m "Aye..."
                m "Maybe me canon needs swabbin'...?"
                m "Go below deck, lass. swabb me canon some more."
                call her_main("Wha'? But...","clench","worried",cheeks="blush",tears="soft")
                call her_main("But it be rusty... 'tis been in me bilge.","shock","baseL",cheeks="blush",tears="soft")
                m "Aye, 'tis been abaft, but that's nah nigh ye bilge."
                m "Heave ho landlubber or me ship be sinkin', lass. Swab me canon some more."
                call her_main("...........","shock","baseL",cheeks="blush",tears="soft")
                call blkfade

                #SUCKING
                hide screen ccg
                $ face_on_cg = False
                hide screen hermione_main
                call her_chibi("hide")
                hide screen genie
                show screen chair_left

                $ gen_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
                $ gen_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen g_c_u

                hide screen blktone
                hide screen bld1
                call hide_blkfade
                call ctc

                call her_main("*Slurp!* *Slurp!* *Slurp!*",ypos="head")
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

                $ gen_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
                $ gen_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen g_c_u

                if use_cgs:
                    $ face_on_cg = True
                    $ ccg_folder = "herm_sex"
                    $ ccg1 = "blank"
                    $ ccg2 = "blank"
                    $ ccg3 = "blank"
                    call her_main("","shock","baseL",cheeks="blush",tears="soft",ypos="head")
                    show screen ccg

                hide screen blktone
                hide screen bld1
                hide screen blkfade
                with fade
                call ctc

                call her_main("Ah...","shock","baseL",cheeks="blush",tears="soft")
                m "We be smooth sailing lass?"
                call her_main("It still be hurting...","clench","worried",cheeks="blush",tears="soft")
                call her_main("But th' storm has passed.")
                m "I'll adjust th' sails fer now..."
                call her_main("Ah... I be greatful, captain.","angry","suspicious",cheeks="blush")
                m "Oh... aye... ye secret cavern be great..."
                call her_main("...........","shock","baseL",cheeks="blush",tears="soft")
                m "Oh... Ye cavern be perfect, lass..."
                call her_main("................","shock","down_raised",cheeks="blush",tears="crying")
                m "Why are ye bein' so quiet lass?"
                call her_main("'cause 'tis cavern be too shallow for ye ship...","clench","worried",cheeks="blush",tears="soft")
                call her_main("'n I jus' wants ye t' cum sooner, captain...")
                m "So ye stifle yer cries o' pain?"
                call her_main("Aye captain. *Sob!*","angry","dead",cheeks="blush",tears="crying")
                m "Nah on me ship lass."
                m "Sob, scream 'n cry as much as ye wish!"
                call her_main("B-but--","clench","worried",cheeks="blush",tears="soft")
                m "That shall make me canon ready t' fire in ye broadside."
                call her_main("be this true? *Sob!*","angry","dead",cheeks="blush",tears="crying")
                call her_main("*Sob!* Me hull! *Sob!* It be taking in water! *Sob!*","shock","baseL",cheeks="blush",tears="soft")
                m "Aye, ye ship be sinking... ye booty be mine."
                call her_main("*SOB!*","angry","suspicious",cheeks="blush",tears="messy")
                m "Ye poor wee sprog..."
                m "A grand, wicked pirate be plunderin' yer booty!"
                call her_main("*SOB!* Yeees! *SOB!*","scream","suspicious",cheeks="blush",tears="messy")
                g4 "Take me seamen!"
                call her_main("No, I'm scared! *SOB!*","scream","worriedCl",cheeks="blush",tears="messy")

        menu:
            "-Sink her vessel, fill her up-":
                g4 "Argh!"
                $ renpy.play('sounds/fuse.mp3')
                call her_main("No! AH!","scream","wide",ypos="head")
                $ renpy.play('sounds/cannon.mp3')
                call cum_block
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"

                $ g_c_u_pic = "sex_cum_in_ani"
                hide screen bld1
                with d3
                $ renpy.play('sounds/cannon.mp3')
                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_main("AH! ME BILGE IS FILLING UP! Sink Me!{image=textheart}{image=textheart}{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                g4 "Aye, ye wench! I be shooting me canons!"
                call her_main("Me hull is splintering, spare me Captain!","angry","suspicious",cheeks="blush",tears="messy")
                g4 "Ye're nah sunk yet!"
                $ renpy.play('sounds/cannon.mp3')
                with hpunch
                call her_main("No, I be already full! Stop cummin', ye bastard!","scream","surprised",cheeks="blush",tears="messy")
                g4 "Shut th' farrg up, wench! Ye still be afloat!"
                call her_main("No! Me stomach! Me ship will capsize!","scream","suspicious",cheeks="blush",tears="messy")
                $ renpy.play('sounds/cannon.mp3')
                with hpunch
                g4 "ARGH!"
                call her_main("No! I reckon me bilge be flooded... I must get t' me pumps.","open","surprised",cheeks="blush",tears="messy")
                $ renpy.play('sounds/cannon.mp3')
                with hpunch
                play sound "sounds/burp.mp3"
                call her_main("{size=+7}*BURP!*!!!!!{/size}","full","surprised",tears="messy")
                call her_main(".......................","full","base",tears="messy")
                call her_main(".............")
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                call her_main("{size=+7}*GULP!*{/size}","cum","worriedCl")
                call her_main("*SOB!* I HATE YOU...","angry","suspicious",cheeks="blush",tears="messy")
                call her_main("{size=+5}I HATE YE'N AND YER RUSTY OLE CANON!{/size}","scream","angry",cheeks="blush",tears="messy")
                call her_main("{size=+5}I HATE YE'N! YE HEAR ME?!{/size}")
                g4 "Agh... Dead men tell no tales, wench!"
                call her_main("*sob!* *Sob!*...","angry","suspicious",cheeks="blush",tears="messy")

                # AFTER CUM INSIDE
                hide screen bld1
                with d3
                call ctc

                $ g_c_u_pic = "ani_her_sex_cum_inside_blink"

                call her_main("*Sob!*...","angry","dead",cheeks="blush",tears="crying")
                m "Whew!... I reckon me gunpowder needs restocking in the next harbour.' it be."
                m "Ye afloat lass?"
                call her_main("Aye... *Sob!*","angry","dead",cheeks="blush",tears="crying")
                m "Is that sea water in ye eyes?"
                call her_main("Me bilge is flooded, but me pumps be workin, captain...","angry","dead",cheeks="blush",tears="crying")
                m "Aye, ye took me canonfire broadside, Ye be a well built vessel ..."
                call her_main("Thank ye captain...","angry","dead",cheeks="blush",tears="crying")
                hide screen bld1
                with d3
                call ctc

                call blkfade
                $ face_on_cg = False
                hide screen hermione_main

                call her_main("I apologize for saying that I hate you, captain...","base","baseL",cheeks="blush",tears="mascara",ypos="head")
                call her_main("And your canon is not rusty...",cheeks="blush",tears="mascara")
                call her_main("I don't know what's gotten into me...","grin","concerned",cheeks="blush",tears="mascara")
                g9 "My canonfire!"
                call her_main("I suppose it's when you call me a \"wench\". I know that it's just roleplay...","grin","concerned",cheeks="blush",tears="mascara")
                m "Aye, sure..."
                m "Does it still hurt?"
                call her_main("A little...","open","concerned",cheeks="blush",tears="mascara")
                call her_main("I also feel full and warm inside...","grin","closed",cheeks="blush",tears="mascara")
                m "You plan to keep it in? My cum I mean."
                call her_main("Aye..","grin","glance",cheeks="blush",tears="mascara")

                if daytime:
                    call her_main("I hope I won't spring a leak during my classes...",cheeks="blush",tears="mascara")
                else:
                    call her_main("I hope it won't spring a leak before I get to my cabin...",cheeks="blush",tears="mascara")

                m "Well, good luck on your voyage."
                call her_main("Can I get paid now please?","grin","closed",cheeks="blush",tears="mascara")

            "-Spread yer canon fire o'er er hull-":
                $ renpy.play('sounds/fuse.mp3')
                g4 "*argh*"
                g4 "{size=+6}Fire!{/size}"
                hide screen bld1
                with d3

                call cum_block
                $ renpy.play('sounds/cannon.mp3')
                with hpunch
                $ g_c_u_pic = "sex_cum_out_ani"
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_main("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead",ypos="head")
                g4 "Aye!!! All over yer hold!"
                call her_main("Ah... No, me hull!","silly","ahegao")
                hide screen bld1
                with d3
                $ renpy.play('sounds/cannon.mp3')
                call cum_block 
                with hpunch
                call ctc

                call blkfade

                call blkfade
                $ face_on_cg = False
                hide screen hermione_main

                m "Well, I'm done... You can get off my ship now."
                call her_main("Yes, captain...","silly","worried",cheeks="blush",tears="soft",ypos="head")
                m "You feeling alright?"
                call her_main("Yes, captain. It still hurts a little, but...","shock","baseL",cheeks="blush",tears="soft")
                m "But what?"
                call her_main("But in a good way... captain.","silly","worried",cheeks="blush",tears="soft")
                m "In a good way, huh?"
                g9 "Heh... You naughty, little pirate."
                call her_main("Can I my get my share of the booty now, captain?","silly","worried",cheeks="blush",tears="soft")

    #Second time event.
    elif pathvalue == 1:
        m "lass?"
        call her_main("captain?","soft","base")
        m "I shall be takin' ye on another voyage today..."
        call her_main(".............","open","suspicious")
        m "Care t' guess wha' th' destination will be?"
        m "You have t' guess three times to find out."
        call her_main("...........","annoyed","frown")
        call her_main("Booty plundering?","disgust","glance")
        g4 "Wha..........?!"
        g4 "How did ye...?"
        call her_main("You seem like a booty pirate kind of a man. captain...","angry","angry")
        m "I'm not sure you know what that means, lass..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        jump lucky_anal_guess

    #Third time event.
    elif pathvalue == 2:
        m "How about another booty plunderin, lass?"
        call her_main("Of course, captain.","base","ahegao_raised")
        g9 "Raise anchor, you little tart!"

        hide screen hermione_main
        call h_equip_temp_outfit(hg_outfit_pirate_ITEM)
        call blkfade

        stop music fadeout 1.0

        call her_main("........","annoyed","worriedL",ypos="head")
        m "Hm..."
        call her_main("...........","open","base")
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_main("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide")
        g4 "Oh, ye-es!"
        call her_main("Ah...","soft","ahegao")
        m "It seems like yer cavern be a bit more welcomin', lass."
        call her_main("Ah... It still be a bit tight.","base","glance")
        call her_main("'n , jus' call me \"wench\", captain.","base","suspicious")
        g4 "Agh! Ye wench! Ye always get me wit' yer words!"

        call her_chibi("hide")
        hide screen genie
        show screen chair_left

        $ gen_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
        $ gen_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen g_c_u

        if use_cgs:
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_main("","open","closed",ypos="head")
            show screen ccg

        hide screen blktone
        hide screen bld1
        call hide_blkfade
        call ctc

        play music "music/pirate.mp3" fadein 1 fadeout 1
        play bg_sounds "sounds/CreakingShip.mp3"

        #INSERTION
        call her_main("Ah... Ah...","open","closed")
        call her_main("Ah...")
        call her_main("captain?","base","glance")
        m "Aye, wench?"
        call her_main("Em...","angry","base")
        call her_main("Would ye settle down fer me, captain?","angry","down_raised")
        with hpunch
        g4 "{size=+9} WHAT?!{/size}"
        g4 "Don't tell me ye're expecting cargo, lass!"
        call her_main("Ye seamen don't put no cargo in me bilge, captain...","angry","wink")
        m "Wha' be this natter o' settlin down then?"
        call her_main("Ye misunderstood me captain.","angry","base")
        call her_main("I meant t' say, would ye stop plunderin for a lass {size=+5}like{/size} me?","angry","down_raised")
        call her_main("I would ne'er propose t' a scallywag wit' his pegleg in me arse, captain...","angry","worriedCl",emote="05")
        m "Good. 'cause I don't reckon any scallywag would be able t' say \"neigh\" to you lassie."
        call her_main("Ah{image=textheart}...","open","closed")
        call her_main("Wha' I meant... ah{image=textheart} {w} ...t' say was ah{image=textheart}... {w}...do ye reckon any pirate would ever ah{image=textheart}... {w} ...leave th' sea fer a lass like me?","angry","down_raised")
        m "Huh?"
        call her_main("I mean, wit' all that booty plunderin happenin' lately... ah{image=textheart}...","angry","down_raised")
        call her_main("I can nah help but feel like me hull is scratched... leakin even.")
        call her_main("'n in a no way untarnished...")
        call her_main("Who would wants t' settle fer a lass like that.","angry","base")

        menu:
            m "..."
            "\"I would leave me ship in a heartbeat!\"":
                call her_main("What?","open","base",ypos="head")
                m "Aye, if only a lass like ye would board me ship..."
                call her_main("...Aye...{image=textheart}","base","baseL")
                call her_main("..............","base","squint")
                call her_main("Aye if only a lass like I, cap'n? So, why neigh me?","soft","base")
                m "Huh?"
                m "Wha' do ye mean \"why\", wench?"
                m "Ye be right out of harbour 'n ye only just set sail..."
                m "Tight cabin, shimering tits, 'n wet wee powder pan..."
                call her_main("Ah...{image=textheart}","open","closed")
                m "Ye will make some lucky scallywag a mighty happy one, some day, wench."
                m "Ehm, I mean, lass."
                call her_main("No, \"wench\" be good. you be calling me that more, captain.","silly","ahegao")
                m "Thar, ye see? Ye be a great catch, I be tellin' ye, wench."
                call her_main("Ah...{image=textheart} Thank you, captain.","angry","dead",cheeks="blush",tears="crying")
                m "Huh?"
                m "Ye helm be leakin."
                pass

            "\"A pirate not plunderin t' be wit' ye be o' th' picture\"":
                call her_main("I be thinkin that...","shock","down_raised",cheeks="blush",tears="crying",ypos="head")
                m "Oh... I jus' love that wee cavern o' yers!"
                call her_main(".....................","angry","dead",cheeks="blush",tears="crying")
                call her_main("Aye... Aft all th' thin's I had t' do fer me crew...")
                call her_main("...nah one we pirate would leave th' sea fer me...","angry","suspicious",cheeks="blush",tears="messy")
                m "Oh, they be leavin th's sea fer ye alright!"
                call her_main("Wha'? But ye said...","open","surprised",cheeks="blush",tears="messy")
                m "T' plunder yer cave, lass. But they'd go back t' sea."
                m "But as a canon swabber ye be a great catch!"
                call her_main("Aye?","open","surprised",cheeks="blush",tears="messy")
                m "Ye pullin' me pegleg?!"
                m "Young, hot 'n slutty. Ye could 'ave any scallywag ye wants!"
                m "Or a landlubber or whatever ye be after..."
                call her_main("I reckon ye may be right, captain.","base","concerned",cheeks="blush",tears="soft")
                m "I always be right, wench."
                m "Now wiggle that wee arse o' yers a wee."
                call her_main("Like this?","silly","worried",cheeks="blush",tears="soft")
                m  "Aye, that be a good wench."
                call her_main("I be a wench, aren't I?","silly","dead")
                m "Ye jus' sold me yer asshole fer 90 galleon points. What ye be calling that?"
                call her_main("Yes, yes...{image=textheart} I be nothing but a wench...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
                m "Ye helm be leakin."
                pass

        call her_main("Not only me helm, captain...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
        m "Not just ye helm?"
        call her_main("I'm cumming captain...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
        g4 "Agh! My cock!"
        g4 "Relax your muscles a little, would you?"
        call her_main("BUT I'M CUMMING!{image=textheart}{image=textheart}{image=textheart}","open","worriedCl")
        g4 "Fine! 'ave it yer way wench!"
        with hpunch
        call her_main("{size=+7}Ah-ah-aha!!! I'm cumming!!!{/size}","scream","wide")
        g4 "{size=+7}Argh!{/size}"

        $ renpy.play('sounds/fuse.mp3')
        g4 "!!!"
        menu:
            "-Sink her vessel, fill her up-":
                hide screen bld1
                with d3
                
                $ renpy.play('sounds/cannon.mp3')
                $ g_c_u_pic = "sex_cum_in_ani"
                call cum_block
                with hpunch
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_main("!!!","scream","wide",ypos="head")
                m "Shiver me timbers! Argh!"
                call her_main("Ah!{image=textheart} 'tis fillin' me up!{image=textheart} me bilge is takin in water!{image=textheart}","silly","ahegao")
                m "'tis nah water, wench!"
                $ renpy.play('sounds/cannon.mp3')
                call cum_block
                with hpunch
                call her_main("Ah! I BE A WENCH!!!!{image=textheart}{image=textheart}{image=textheart}","scream","worriedCl",cheeks="blush",tears="crying")
                $ renpy.play('sounds/cannon.mp3')
                with hpunch
                m "Agh!"
                call her_main("Ah...{image=textheart} yer seamen, captain...{image=textheart}","open","surprised",cheeks="blush",tears="messy")
                m "Aye, my semen..."
                call her_main("Ah...{image=textheart}","angry","suspicious",cheeks="blush",tears="messy")
                m "......"
                hide screen bld1
                with d3
                call ctc

                call blkfade

            "-Spread yer canon fire o'er er hull-":
                hide screen bld1
                with d3

                $ renpy.play('sounds/cannon.mp3')
                $ g_c_u_pic = "sex_cum_out_ani"
                call cum_block
                with hpunch
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"

                call her_main("Ah-aha! Ye're cummin'! {image=textheart}{image=textheart}{image=textheart}","silly","dead",ypos="head")
                g4 "{size=+7}Aye I do, wench{/size}"
                call her_main("Blisterin' Barnacles, me too! Me too!","scream","worriedCl",cheeks="blush",tears="messy")
                g4 "{size=+7}FARRRGIN' WENCH!{/size}"
                $ renpy.play('sounds/cannon.mp3')
                call cum_block
                with hpunch
                call her_main("Ah...{image=textheart} yer cum...{image=textheart}","angry","dead",cheeks="blush",tears="crying")
                call her_main("Ye covered me whole deck{image=textheart}{image=textheart}{image=textheart}")
                g4 "Aye!!! All o'er yer hull!"
                $ renpy.play('sounds/cannon.mp3')
                with hpunch
                call her_main("Shiver me timbers... 'tis so hot!","silly","ahegao")
                hide screen bld1
                with d3
                call ctc

                call blkfade

        #Ending
        $ face_on_cg = False

        m "Well, tis been intense..."
        call her_main("Ah-ha...{image=textheart} ah...{image=textheart}","grin","dead",cheeks="blush",tears="messy",ypos="head")
        m "Ye be fine lass?"
        call her_main("I reckon so... I be nah sure...","grin","dead",cheeks="blush",tears="messy")
        call her_main("I reckon I may still be leakin', captain.","grin","dead",cheeks="blush",tears="messy")
        call her_main("Or maybe nah...","grin","dead",cheeks="blush",tears="messy")
        call her_main("Everythin' be in a daze... 'n me legs feel so weak...")
        if her_whoring < 24:
            her "Can I jus' get paid now, captain?"
        stop music fadeout 1.0


    hide screen hermione_main
    show screen blkfade

    stop music fadeout 1.0
    stop bg_sounds

    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.

    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ccg

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    call hide_blkfade


    call her_main("Thank you, captain...","grin","base",xpos="right",ypos="base", cheeks="blush")

    call her_walk(action="leave", speed=2.7)

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    if not hg_outfit_pirate_ITEM.unlocked:
        call unlock_clothing(">Congratulations! You have unlocked a new outfit!",hg_outfit_pirate_ITEM)

    if not card_exist(unlocked_cards, card_maslab):
        if deck_unlocked:
            call give_reward("Ye plundered a special card from 'er cavern.", "images/cardgame/t1/genie_realm/maslab_v1.png")
        $ unlocked_cards += [card_maslab]

    call blkfade
    call h_unequip_temp_outfit
    call her_chibi("hide")
    hide screen main_room

    jump enter_room_of_req
