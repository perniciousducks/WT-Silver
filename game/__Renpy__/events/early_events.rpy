

### EVENT 0 ###

#First event in the game. Gennie finds himself at the desk.
label event_01:
    call bld
    m "..................?"
    m "Your majesty?"
    m "......................................................."
    g4 "I did it again, didn't I?"
    g4 "Teleported myself to who knows where..."
    m "What's with those ingredients?"
    m "They seem to be way more potent than I thought."
    m "Well, whatever this place is I have no business here..."
    m "Better undo the spell and return to the shop before the princess gets angry with me again..."
    m "....................."
    m "Although..."
    m "There is something odd about this place... it's..."
    m "It's almost brimming with...."
    g4 "{size=+5}MAGIC?!{/size}"
    m "Yes... magic, I can feel it. So powerful and yet somehow..."
    m "....alien."
    m "Interesting..."
    m "I think I will stick around for a little bit..."
    $ achievement.unlock("start")
    hide screen bld1
    with d3
    return


# Owl intro.
label owl_intro:
    call play_sound("owl")
    show screen owl
    call bld
    m "What? An owl?"
    hide screen bld1
    with d3

    return


# First time genie meets snape
label event_00:
    call play_music("dark_fog")
    call play_sound("door")

    call sna_chibi("stand","door","base")
    with d3
    pause.3

    call bld
    g4 "{size=-3}(An Indigenous life form!?){/size}"
    hide screen bld1

    $ tt_xpos=650
    $ tt_ypos=180
    show screen thought
    with d3
    pause 1

    call bld
    m "{size=-3}(looks human enough...){/size}"
    m "{size=-3}(Maybe if I just act cool he'll leave...?){/size}"
    hide screen bld1
    hide screen thought
    with d3

    call sna_walk("door","mid",4)
    pause.2

    show screen bld1
    call sna_main("","snape_01",xpos="base",ypos="base")
    call ctc

    who2 "Albus... Do you have a moment?"
    hide screen snape_main

    menu:
        m "..."
        "\"Actually I'm a bit busy.\"":
            call sna_main("","snape_04")
            who2 "Well, aren't you always, Albus?"
        "\"Of course. What is it?\"":
            pass
        "\"And Albus to you too.\"":
            call sna_main("","snape_05")
            who2 "What?"
            call sna_main("","snape_04")
            who2 "Albus I'm not in the mood for your... shenanigans."
        "\"Take me to your leader.\"":
            call sna_main("","snape_01")
            who2 "What?"
            who2 "Hm...?"
            who2 "You mean the minster of magic?"
            call sna_main("","snape_03")
            who2 "I would rather avoid having to deal with that bureaucrat..."
            hide screen snape_main
            with d3
            m "Fine, never mind... How can I be of help?"

    call sna_main("","snape_06")
    who2 "I have something important I need to discuss with you..."
    who2 "I think we need to revise our admittance policy."
    hide screen snape_main
    with d3
    m "................?"
    call sna_main("","snape_03")
    who2 "Half of my... so-called \"pupils\" are nothing but annoying maggots that make my life miserable on a daily basis."
    hide screen snape_main
    with d3
    m "................"
    call sna_main("","snape_06")
    who2 "Most of them belong to your precious \"gryffindor\" house of course..."
    hide screen snape_main
    with d3
    m "......?"
    call sna_main("","snape_03")
    who2 "The wretched Weasley family, that noisy Granger girl and of course the hero of all the juvenile delinquents around the globe...."
    call sna_main("","snape_08")
    who2 "{size=+3}The Potter boy!{/size}"
    call sna_main("","snape_01")
    who2 "Mark my words, Albus. The \"gryffindor house\" will become this school's undoing!"
    hide screen snape_main
    with d3
    m "...................."
    call sna_main("","snape_01")
    who2 "Nothing but annoying maggots, the lot of them!"
    call sna_main("","snape_06")
    who2 "And if that wasn't enough, now they spread all sorts of nasty rumours about the teachers!"
    who2 "Particularly about yours truly..."
    hide screen snape_main
    with d3
    m "......................"
    call sna_main("","snape_05")
    who2 "You don't believe those rumours, do you Albus?"
    hide screen snape_main
    with d3

    menu:
        m ".............."
        "\"Well, of course not!\"":
            call sna_main("","snape_09")
            who2 "Good..."
            who2 "You know me better than that. I wouldn't care for such things..."
        "\"Where there's smoke, there's fire.\"":
            call sna_main("","snape_10")
            who2 "Albus?! You can't be serious!"
            who2 "Those are nothing but filthy lies, I'm telling you!"

    hide screen snape_main
    with d3
    m "........................."
    call sna_main("","snape_04")
    who2 "Well, those wretched kids left me completely exhausted. I think I will retire for today."
    call sna_main("","snape_09")
    who2 "................"

    stop music fadeout 1.0

    hide screen snape_main
    with d3
    hide screen bld1

    call sna_walk("mid","leave",3)
    call bld

    m "Hm..."
    m "So that tall, broody dude mistook me for someone else...?"
    m "Which means I must be shrouded in a concealment spell..."
    m "........."
    m "So basically, I'm a genie disguised as a human, who is in turn disguised as another human..."
    m "No, that's not stupid at all..."

    $ days_without_an_event = 0

    jump day_start




### EVENT 3 ###

#Sanpe talks to genie about hermione, snape becomes suspicious
label event_03:
    call play_music("dark_fog")
    call play_sound("door")

    call sna_walk("door","mid",2)
    call bld

    m "{size=-3}(That broody guy again...){/size}"
    call sna_main("","snape_01",xpos="base",ypos="base")
    who2 "Albus!"
    m "Hey.......... you..."
    who2 "You need to do something about that Granger girl..."
    call sna_main("","snape_06")
    who2 "Honestly... I'm running out of ways to punish that... that..."
    call sna_main("","snape_04")
    who2 "That little witch!"

    menu:
        m "..."
        "\"Granger? Hermione Granger, right?\"":
            who2 "Yes, her..."
            who2 " She also happens to be a part of the \"Potter gang\"."
        "\"I got your back, Jack, witches be crazy!\"":
            who2 "What...? Albus you behave oddly lately."
            who2 "Is everything alright?"
            menu:
                m "..."
                "\"Yes, I'm fine. Go on.\"":
                    who2 "If you say so..."
                "\"You know me. I love my shenanigans.\"":
                    who2 "Hm....."

        "\".....................................................\"":
            pass

    who2 "Remember how back in the days they used to publicly flog the students?"
    who2 "I swear if we could bring that back all of our problems would be solved..."
    who2 "Yes... I would gladly tie that girl to a flogging pole in front of the entire school..."
    call sna_main("","snape_20")
    who2 "Then lift her skirt up, and..."
    call sna_main("","snape_12")
    who2 "*Khem!* Sadly, nowadays we teachers are severely limited in the disciplinary measures we have at our disposal..."
    who2 "I know you are just as powerless as I am in this matter, but I'm telling you, that girl had better stop testing my patience."

    menu:
        m "..."
        "\"I'll take care of that little whore!\"":
            call sna_main("","snape_05")
            who2 "...?!"
            who2 "Albus..."
            who2 "You are acting strange lately..."
        "\"Nobody ever said this job would be easy.\"":
            call sna_main("","snape_06")
            who2 "Sometimes I feel like I would rather deal with a classroom full of Dementors..."
        "\"You will feel better tomorrow.\"":
            call sna_main("","snape_06")
            who2 "You are probably right..."

    who2 "Hm..."
    call sna_main("","snape_06")
    who2 "Perhaps I'd better go get some sleep."
    who2 "I need to be in my top shape every morning..."
    who2 "You can't show weakness to those kids or they will swallow you whole..."
    call sna_main("","snape_24")
    who2 "Good night, Albus."


    hide screen snape_main
    hide screen bld1
    with d3

    call sna_walk("mid","door",3)
    pause.2

    who2 "................."

    call sna_chibi("stand","door","base",flip=False)
    with d3
    pause.2

    who2 "One more thing..."
    show screen bld1
    show screen snape_main
    with d3
    who2 "You should ignore any lies you hear about me and those slytherin girls..."
    hide screen snape_main
    with d3
    m "Got it."

    hide screen bld1
    call sna_chibi("stand","door","base",flip=True)
    with d3
    pause.2

    call sna_chibi("leave")

    jump day_start


#NOT IN USE
label event_04:
    return

### EVENT 5 ###

#Snape comes in, has a talk with Genie, then the duel starts.
label event_05:
    call play_music("dark_fog")
    call play_sound("door")

    call sna_walk("door","mid",2)
    call bld

    call sna_main("","snape_01",xpos="base",ypos="base")
    call ctc

    who2 "Good evening, Albus."
    who2 "I want to talk to you about those damn kids again..."
    who2 "But first I want to ask you something..."
    call sna_main("","snape_05")
    who2 "Have you noticed anything strange going on around here lately?"

    menu:
        m "..."
        "{size=-2}\"Like you being especially whiny?\"{/size}":
            who2 "What? B-but... Those kids..."
            call sna_main("","snape_06")
            who2 "Well, perhaps you are right..."
        "{size=-2}\"That owl is fetching my mail, man!\"{/size}":
            who2 "An owl? What about it?"
            call sna_main("","snape_25")
            who2 "That's not what I mean..."
            call sna_main("","snape_29")
            who2 "Well, never mind..."
        "{size=-2}\"No, not really. It's just business as usual.\"{/size}":
            who2 "Hm... Maybe I'm just being paranoid..."

    call sna_main("","snape_24")
    who2 "The reason why I'm here today is the \"Potter Gang\""
    call sna_main("","snape_01")
    who2 "There are only so many points I can subtract from the Gryffindor house, you know..."
    who2 "And the Granger girl became the worst of them lately..."
    call sna_main("","snape_06")
    who2 "She practically leads the onslaught."
    call sna_main("","snape_05")
    who2 "Speaking of which, has she been sending you any letters lately?"

    menu:
        m "..."
        "\"Hermione Granger? No, Nothing from her.\"":
            who2 "I see... So she's been bluffing then."
            call sna_main("","snape_16")
            who2 "What an annoying young witch."
        "\"Yes... Every damn day...\"":
            who2 "Really now?"
            who2 "Any lies about me in particular?"
            who2 "I hope you know better than to listen to the likes of her..."

    call sna_main("","snape_03")
    who2 "She would never admit it, but I know she's been spreading those nasty rumours about me around the school..."
    call sna_main("","snape_29")
    who2 "Tsk... Noisy little...... witch."
    call sna_main("","snape_09")
    who2 "I would never stoop so low as to trade house points in exchange for sexual favours..."
    who2 "I mean, sure, we use house points to motivate students, but that's completely different..."
    who2 "I can't speak for the rest of the staff though..."
    call sna_main("","snape_13")
    who2 "The stories I hear about Minerva McGonagall and those poor Gryffindor freshmen may be true..."
    call sna_main("","snape_01")
    who2 "Well, I just wanted to make sure that you take those rumours about me for what they are..."
    who2 "Nasty lies made up by a bunch of spoiled kids."


    who2 "Oh.... Before I go..."
    who2 "There is one thing I meant to ask you for a while now..."
    call sna_main("","snape_09")
    who2 "........................."
    call sna_main("","snape_05")
    who2 "What is my name?"

    menu:
        m "..."
        "\"What? What kind of question is that?\"":
            call sna_main("","snape_06")
            who2 "You are right..."
            who2 "Forgive me... I'm just being paranoid I suppose..."
            call sna_main("","snape_05")
            who2 "But you can never be too cautious with rumours about  \"you know who\" still being alive and all..."
        "\"Tall broody guy?\"":
            call sna_main("","snape_06")
            who2 "Albus, lately you adopted a peculiar sense of humor, that I do not care for in a slightest..."
            who2 "Maybe you should spend a little less time in the company of that big oaf Hagrid."
        "-\{Use magic to get the right answer\}-":
            $ d_flag_01 = True
            hide screen snape_main
            with d3
            call blktone
            ">You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer."
            call hide_blktone
            call sna_main("","snape_03") #SNAPE
            who2 "!!?"
            m "What kind of question is this, Severus?"
            who2 "Forgive me... I'm just being paranoid I suppose..."

    call sna_main("","snape_06")
    who2 "Well, good night, Albus."
    hide screen snape_main
    hide screen bld1

    call sna_walk("mid","door",3)
    pause.2

    stop music fadeout 1.0
    who2 "........................"

    call sna_chibi("leave")
    hide screen bld1
    hide screen snape_main

    show screen blkfade
    with d3

    $ renpy.play('sounds/07_run.mp3')
    pause 2
    g4 "???"

    show screen snape_defends
    call hide_blkfade
    show screen ctc

    call play_music("hitman") #TENSE THEME

    call ctc

    call bld

    if d_flag_01:
        sna_[6] "Who are you, scum!"
        g4 "What? It's me... uhm... Abius! I mean, Albus!"
        sna_[4] "You cannot fool me."
        sna_[4] "Just now, you used some sort of alien magic!"
        sna_[6] "Reveal your true self to me now, fiend! Who are you?!"
    else:
        sna_[1] "My name is Severus Snape!"
        sna_[1] "Now, who might you be...?"

    g4 "!!!"
    sna_[1] "Easy now... Just answer my question."
    m "Alright, alright. Just calm down, would you?"
    sna_[1] "........"

    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False

    label no_wait:
    menu:
        m "..."
        "\"I am not your enemy.\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna_[1] "That the first thing an enemy would say."
        "\"I'm just a tourist. I'll be leaving now.\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_[1] "You are not going anywhere."
        "\"I work for Albis Doombldore!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_[1] "It's Albus Dumbledore, you moron!"

    if d_points == 2:
        pass
    else:
        jump no_wait

    sna_[1] "Who sent you here? What did you do with the real Albus?"
    sna_[1] "Shed your disguise and reveal your true self at once, this is your last warning!"

    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False

    label no_wait_2:
    menu:
        m "..."
        "\"I can't. It's hard to explain...\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna_[1] "I have no interest in your explanations. I wouldn't believe a single word you'd say anyway!"
        "\"Stop threatening me, human!\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_[1] "\"Human\"?"
            sna_[1] "Are you implying that you are {size=+5}not{/size} one?"
            sna_[1] "What are you then?! Dispell your cloaking charm immediately or else!"
        "\"I mean you no harm, I swear!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_[1] "Is that so?"
            sna_[1] "Prove it then. Dispel your cloaking charm now!"

    if d_points == 2:
        pass
    else:
        jump no_wait_2

    sna_[1] "I've heard enough!"
    g4 "By the great desert sands! Would you let me explain, human?!"
    sna_[1] "There is nothing left to explain!"
    sna_[1] "Since you refuse to cooperate, I'll be taking you into custody by force!"
    g4 "What?! Wait!"

    if skip_duel == True:
        jump snape_lost

    stop music
    call play_music("boss_theme")
    call play_sound("glass_break")

    pause.1


    show screen snape_glass
    pause 3

    hide screen genie
    hide screen snape_defends

    jump duel



### EVENT 6 ###

#THE TALK AFTER THE DUEL ENDS.
label event_06:
    $ potions = 0 #Makes sure there are no potions left in the possessions.

    stop music fadeout 2.0

    g4 "*Panting*"
    g4 "Ready to talk now?!"
    sna_[8] "(...i-impossible...)"

    call play_music("dark_fog")

    hide ch_gen
    show image "images/dueling/snape/no_magic.png" at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")

    m "I told you that you're no match for me..."
    call bld

    m "You did give me a good run for my money though..."
    sna_[1] "The way you conjure the spells with your bare hands..."
    sna_[1] "No human could do that... who--"
    sna_[4] "{size=+5}What are you?{/size}"
    sna_[1] "Some sort of shape-shifting demon summoned by \"you know who\"?"
    m "Summoned by whom?"
    sna_[2] "By \"you know who\"!"
    m "What?"
    sna_[7] "......................"
    m "............................"
    m "Listen, I'm not a demon..."
    m "And I sure as heck don't work for \"I don't know who\"!"
    sna_[1] "............................."
    m "I've been ehm..."
    m "...Conducting an experiment back in my world, during which something went wrong and I ended up here."
    m "That's all..."
    sna_[1] ".........................."
    sna_[1] "What became of the real Albus Dumbledore then?"
    m "I'm sure he is fine."
    m "He's Probably feeling as surprised about finding himself in my world as I am about finding myself here..."
    sna_[1] "...................................."
    sna_[1] "When did this happen?"
    m "Four days ago..."
    sna_[1] "Can you go back?"
    m "I think so..."
    sna_[2] "Why didn't you then?"
    m "Not sure..."
    m "The Magic of this world is so bizarre... Perhaps I just got curious."
    sna_[1] "..................."
    sna_[1] "You need to fix this..."
    m "Fix what?"
    sna_[4] "Everything. You need to bring back Albus and leave our world."

    menu:
        m "..."
        "\"Yes, yes, I know. Off I go then.\"":
            m "Yes, yes, I know..."
            m "Well, off I go then. Sorry for the ruckus."
            sna_[1] "No harm done..."
        "\"But I like it here! Can't I stay?\"":
            sna_[1] "Absolutely not."
            sna_[1] "Whoever you are, you are not from this plane of existence."
            sna_[1] "Your very presence here upsets the natural order of things."
            sna_[1] "And these days this school needs a proper headmaster more than ever."

    sna_[1] "Have a safe trip home now."
    m "Ehm... Thank you, mr. Severus. Good luck with your students and the \"potter gang\"."
    sna_[1] "\"The potter gang\"?"
    sna_[7] "Oh, right, those buggers..."

    menu:
        "-Undo the spell-":
            pass
    menu:
        "-Undo the spell-":
            pass
    menu:
        "-Undo the spell-":
            pass

    sna_[1] "Did it work? Albus, is that really you?"

    menu:
        m "..."
        "\"Yeah, that's me. So good to be back!\"":
            sna_[1] "Glad to have you back, old friend. Are you alright?"
            m "I'm fine, Severus, thank you."
            sna_[1] "How was it, in that other world?"
            m "A lot of sand and very hot, but other than that quite pleasant."
            sna_[1] "I see... Did you miss your brother?"
            menu:
                m "..."
                "\"Yes, I missed you so much!\"":
                    sna_[1] "......................."
                    sna_[1] "Yeah, right...."
                "\"I don't have a brother, Severus.\"":
                     sna_[1] "........................"
                     sna_[1] "You may not have one, but the real Albus Dumbledore does."
                "-Use magic to get the right answer-":
                    call bld
                    ">You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer."
                    hide screen bld1
                    with d3
                    m "My little brother Aberforth? Why would I miss him?"
                    sna_[1] "I can feel it whenever you use your alien magic..."

        "\"Nope. It's still me. The non-human guy.\"":
            pass

    sna_[1] "Why are you still here, creature?"
    m "I'm not sure... I tried to undo the spell but nothing happened..."
    sna_[7] "Marvelous..."
    sna_[1] "What does this mean? So You're staying here for good?"
    m "Of course not..."
    m "Me being here at all is only possible because the spell is compensating for the unbalance caused by itself..."
    m "said spell will wear off eventually and I shall be pulled back into my world."
    m "Likewise, your Dumbledore-friend shall be pulled back here."
    sna_[1] "I see..."
    sna_[1] "How long until the spell wears off?"

    menu:
        m "..."
        "\"A couple of days.\"":
            sna_[1] "I see..."
        "\"A week or so...\"":
            sna_[1] "Hm.... A week, huh..."
        "\"Could be months...\"":
             sna_[1] "That long?"
             sna_[1] "Now isn't that just \"perfect\"?"
        "\"I have no clue...\"":
            sna_[1] "....................."
            sna_[2] "Splendid..."

    m "Alright, to be honest I'm not sure where to go from here..."
    m "All this time I thought I could undo the spell whenever I wanted to..."
    sna_[1] "..................................................."
    sna_[1] ".................................."
    sna_[1] "..................."
    m "Snape?"
    sna_[1] "..................................................."
    m "Severus?"
    sna_[6] "Yes, yes..."
    sna_[1] "Listen, it's very late, and too much has happened already..."
    sna_[7] "I need to process all of this."
    sna_[1] "I will come to see you tomorrow, after my classes."
    sna_[6] "Until then, keep your true identity and our conversation a secret, alright?"
    m "Not a problem."
    sna_[1] "Alright then..."
    sna_[1] "But before I go, I have one more question..."
    m "I'm listening..."
    sna_[2] "........"
    sna_[1] "If you are not a human, then..."
    sna_[7] "What are you?"
    m "...I'm a genie."
    sna_[1] "A genie?"
    m "Yes, I possess phenomenal cosmic powers and all that..."
    sna_[1] "Seriously?"
    m "Oh, yes."
    sna_[1] "Unbelievable..."
    sna_[1] "Well, I'll see you tomorrow.... genie."
    m "I'll be here..."

    sna_[7] "(A genie? Now that's new...)"

    hide screen duel

    jump day_start



#THE TALK WITH SNAPE THE DAY AFTER THE DUEL.
label event_07:
    call play_music("dark_fog")
    call play_sound("door")

    call sna_walk("door","mid",2)
    call bld

    call sna_main("","snape_01",xpos="base",ypos="base")
    show screen ctc
    with d3

    sna "..................."
    hide screen snape_main
    with d3
    m "Good evening..."
    show screen snape_main
    with d3
    sna "Is the spell still in effect?"
    hide screen snape_main
    with d3
    m "Yes. very much so."
    show screen snape_main
    with d3

    sna "I see..."
    sna "Last night I gave our little.... conundrum some thought."
    sna "And I think I came up with a solution..."
    m "Really? Great! I'm listening."
    hide screen snape_main
    with d3

    call sna_main("Let's just roll with it...","snape_29")
    m "Excuse me?"
    call sna_main("Well what else could we do?","snape_06")
    sna "Normally I would alert the ministry of magic and let them take care of this mess..."
    sna "But I'd rather avoid any dealings with those rotten bureaucrats this time..."
    call sna_main("Also, losing a headmaster, even temporarily, could hurt the school's reputation...","snape_10")
    sna "And what if your spell wears off tomorrow, or even tonight?"
    call sna_main("I see no reason to start a commotion...","snape_09")
    m "Hm..."
    call sna_main("So we shall keep the charade going for now...","snape_03")

    m "By doing what exactly?"
    call sna_main("Just act like Albus always does: never leave this tower and try to avoid any human contact...","snape_05")
    m "That...."
    m "Sounds..."
    g4 "Incredibly boring!"
    g4 "What am I supposed to do here?"
    call sna_main("You are a Genie. Conjure up some sort of entertainment for yourself.","snape_01")
    m "My magic doesn't seem to be working properly here for some reason..."
    m "And my lamp is literally worlds away..."
    call sna_main("Well, what do you expect me to do about that?","snape_03")
    sna "Send you a couple of girls from Slytherin maybe?"
    g9 "I have no idea what \"Slytherin\" is, but I think that would work..."
    call sna_main("That was a joke, obviously.","snape_04")
    call sna_main("Although...","snape_09")
    sna "Hm..."
    call sna_main("Well, in any case, I don't see how entertaining {size=+7}you{/size} is {size=+7}my{/size} problem.","snape_01")
    m "Oh, but it is!"
    m "I'm immortal and all-powerful..."
    m "Being bored is one of the worst things that could happen to me!"
    g4 "And I have a thing against being cooped up in small spaces with nothing to do!"
    g4 "I may lose my mind..."
    g4 "Oh! Ah! I think it's happening already!"
    call sna_main(".......","snape_03")
    g4 "I'm losing my mind! It's getting hard to breathe!"
    call sna_main("....","snape_04")
    g4 "It's so dark..."
    g4 "Are you still here?"
    call sna_main("....","snape_03")
    m "........."
    call sna_main("Are you done?","snape_10")
    m "Yes..."
    m "Seriously though, I don't see how this whole affair benefits me at all."
    call sna_main("Do you have any choice?","snape_01")
    m "I do..."
    m "Instead of sitting here on my ass all day and being quiet I could explore your world..."
    call sna_main("Hm...","snape_03")
    call sna_main("Well, alright, what do you want?","snape_01")
    m "Teach me your magic..."
    call sna_main("My magic?","snape_05")
    m "Yes... The way you conjure up your spells is..."
    m "Intriguing..."
    call sna_main("Hm...","snape_04")
    call sna_main("Agreed.","snape_06")
    m "Oh, and send me some of those \"Slytherin\" girls as well.."
    call sna_main("...............","snape_05")
    sna "........................."
    call sna_main("Ha-ha-ha!!!","snape_28")
    m "What? What did I say?"
    call sna_main("A-ha-ha-ha-ha...","snape_28")
    call sna_main("No, no, my apologies...","snape_02")
    sna "It's just that to me you still look and sound like Albus..."
    sna "To hear Professor Dumbledore say things like \"Send me some of those girls\"..."
    call sna_main("It's hysterical... ","snape_22")
    call sna_main("But you wouldn't understand...","snape_09")
    m "Heh..."
    g9 "Send those whores up, Severus. I'm feeling lonely tonight."
    call sna_main("Ha-ha-ha! Stop it, you're killing me!","snape_28")
    sna "A-Ha-ha-ha!"
    m "No, I'm serious... Is it possible?"
    call sna_main("Hm...","snape_02")
    sna "We'll see..."
    sna "You being our new headmaster presents me with interesting possibilities..."
    sna "I need some time to figure out how to use this situation to my advantage."
    m "You mean {size=+7}our{/size} advantage, right?"
    call sna_main("Oh, yes. Yes, of course...","snape_06")
    sna "Well, I think we are done for today..."
    call sna_main("Good night... genie.","snape_24")
    m "Yes. Good night, Severus."

    hide screen snape_main
    hide screen ctc
    hide screen bld1
    with d3

    call sna_walk("mid","door",3)
    pause.2

    call sna_head(".................","snape_06",xpos="base",ypos="base")
    call sna_head("\"Send those whores up, Severus!\" Ha-ha-ha..","snape_28")
    $ renpy.play('sounds/door.mp3')
    call sna_chibi("leave")

    m "Hm... "
    m "I Suppose I'll just curl up in a ball on top of this desk as usual..."
    pause.2

    call give_reward(">You've unlocked the ability to summon Severus Snape to your office.","interface/icons/head/head_snape_1.png")
    $ achievement.unlock("unlocksna", True)
    $ snape_unlocked = True

    jump day_start



### EVENT 8 ###

#HERMONE SHOWS UP FOR THE FIRST TIME. IN USE.
label event_08:
    stop music fadeout 1.0
    pause 1

    call play_sound("knocking") #Sound someone knocking on the door.
    "*Knock-knock-knock*"
    m "Huh?"

    call play_sound("knocking") #Sound someone knocking on the door.
    "*Knock-knock-knock*"
    pause.7

    m "Somebody is knocking on the door..."
    m "Crap... I'm supposed to avoid any human contact!"
    m "Hm... What are the chances that the thing knocking on my door is not human?"
    m "Yeah, quite slim..."

    call play_sound("knocking") #Sound someone knocking on the door.
    "*Knock-knock-knock*"
    m "Persistent little bastard..."

    $ d_flag_01 = False #When False Genie doesn't know Hermione's name.
    $ d_flag_02 = False #When TRUE Genie knows it's a girl knocking on the door.

    menu:
        m "..."
        "\"Who is it?\"":
            $ d_flag_01 = True
            who "It's me, professor..."
            who "Hermione Granger. Can I come in?"
            m "{size=-4}(It's that wretched woman who's been harassing me with her letters lately...){/size}"

            menu:
                m "..."
                "\"Go away, please. I'm busy.\"":
                    her "But, professor, I really need to talk to you..."
                    m "..........................................."
                    her "Professor? I'm coming in!"
                    m "{size=-4}(Crap...){/size}"
                "\"Yes, yes, you can come in.\"":
                    pass

        "\"Come in!\"":
            pass
        "\"Go away!\"":
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            who "But, professor, I really need to talk to you..."
            m "..........................................."
            who "Professor? I'm coming in!"
            m "{size=-4}(Crap...){/size}"
        "\"................\"":
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            who "Professor, are you there?"
            m "{size=-4}(Go away...){/size}"
            who "Professor, I really need to talk to you..."
            m "..........................................."
            her "Professor? I'm coming in!"
            m "{size=-4}(Crap...){/size}"

    pause.2
    call play_sound("door") #Sound of a door opening.

    call her_chibi("stand","door","base")
    with d3
    pause.5

    if not d_flag_01:
        m "?!!"
    if not d_flag_02: #When TRUE Genie knows it's a girl knocking on the door.
        m "{size=-3}(A girl?){/size}"

    call play_music("chipper_doodle")

    call her_walk("door","mid",3)
    pause.5

    show screen bld1
    show screen ctc

    call her_main("","base","base",xpos="base",ypos="base")
    call ctc

    call her_main("Good morning, professor.","normal","base")

    menu:
        "\"Good morning... girl.\"":
            her "{size=-4}(\"Girl\"?){/size}"
            pass
        "\"Good morning, Hermione.\"" if d_flag_01:
            pass
        "\"Good morning, Child.\"":
            her "{size=-4}(\"Child\"...?){/size}"
        "\"................................\"":
            pass

    her "I am very busy with my class schedule, but I kept my morning free today so that I could see you, professor."
    her "You probably know why I am here too."
    call her_main("The issue I have been fruitlessly trying to bring to your attention lately.","open","angryCl")
    her "I cannot understand why you are not acting to stop that nonsense, professor!"
    her "This simply cannot continue!"
    call her_main("The inequality is starting to affect all of the houses...","open","base")
    her "Simply because Gryffindor has more integrity than the rest..."
    her "Do you think it's fair that the people who deserve to be in the lead are being pushed back instead?"
    her "Do you think that's fair, professor? Do you?"
    call her_main("","normal","base")
    m "{size=-4}(Would you look at that pretty little thing?){/size}"
    m "{size=-4}(Look at her going on and on about something... She's adorable.){/size}"
    m "{size=-4}(Damn, I haven't seen a woman in weeks.){/size}"

    menu:
        "\"(I will jerk off a little while she talks.)\"":
            call hide_characters
            hide screen bld1
            with d3
            pause.2

            call gen_chibi("jerking_off_behind_desk")
            with d3
            pause.5

            show screen bld1
            call nar(">You reach under the desk and grab your cock...")

            $ her_jerk_off_counter += 1
            $ jerked_off_during_hermione_intro = True #Affects next conversation with Snape.

            $ masturbating = True

        "\"(No, that's stupid! I Need to behave!)\"":

            $ masturbating = False

    m "Yes, keep on going, dear."
    call her_main("\"Yes\"?! So you think it's fair?","angry","angry")
    m "Oh, of course not, I meant \"no\". But keep on going anyway..."
    call her_main("That's a relief. I'm glad that you agree with me, professor...","normal","base")
    call her_main("As I was saying, the whole issue is simply ridiculous and I cannot believe that it is taking place in our day and age!","open","angryCl")

    if masturbating:
        call nar(">*Fap!* *Fap!* *Fap!*","start")
        call nar(">You keep on stroking your cock...","end")
    else:
        m "I see..."

    call her_main("I mean, I would understand if something like this were to occur during the middle ages...")
    her "But we left the middle ages behind a long time ago, did we not?"

    if masturbating:
        g9 "{size=-4}(Would you look at those rosy cheeks? I want to poke 'em with my cock.){/size}"
        call nar(">You keep stroking your cock...")
    else:
        m "Ehm... I suppose you did. I mean, we did."

    call her_main("So it hurts the whole house-point-distribution system.")
    her "But it doesn't even stop there!"
    her "It hurts our entire educational system as well..."
    her "And more importantly, the motivation among students is steadily decreasing due to it!"

    if masturbating:
        m "{size=-4}(Look at those huge knockers on you, girl!){/size}"
        m "{size=-4}(Yes... I want to squeeze my dick between them...){/size}"

    her "As you can see, the situation is dire..."
    call her_main("But we can still set everything right...","open","base")
    her "As the president of our school's Student Representative Body..."
    her "I have a few suggestions on how to do that more efficiently."

    if not masturbating:
        m ".............."

    her "First of all, the house point system needs to be maintained!"
    call her_main("You need to control the point distribution better, sir.","normal","base")

    if masturbating:
        g4 "{size=-4}(Yes, you are a whore... A nasty little whore... I bet you love to suck cocks... Don't you? Yes, I bet you do...){/size}"
        call nar(">You stroke your rock-hard cock ferociously!")

    her "Of course you agree with me on this, professor, do you not?"

    if masturbating:
        g4 "{size=-4}*Panting heavily*{/size}"
        call her_main("Professor...?","normal","frown")
        g4 "{size=-4}(Crap. What does she want now?){/size}"
        g4 "Yes, it's all true. Please keep going..."
        her "Ehm... So, as I was saying..."
        m "{size=-4}(Oh... That was a good jerkoff session, but I'm getting dangerously close to the \"grand finale\".){/size}"
        m "{size=-4}(Maybe I should stop before I get myself into trouble.){/size}"

        menu:
            "\"(Yes, time to actually listen to her.)\"":
                call hide_characters
                hide screen bld1
                with d3

                call gen_chibi("sit_behind_desk")
                with d3
                pause.5

                $ masturbating = False

            "\"(No! I want to keep on jerking off!)\"":

                $ masturbating = True

    else:
        m "{size=-4}(Do I? I honestly don't give a damn...){/size}"
        m "Uhm... I suppose I do..."
        her "{size=-4}(\"Suppose\"?){/size}"
        her "{size=-4}(When did Professor Dumbledore become so... apathetic?){/size}"

    call her_main("Another measure you could take into consideration is tightening your control over the staff...","open","angryCl")
    her "Especially the teachers..."
    call her_main("I hope I'm not stepping out of line here, sir, but some of the teachers really do require supervision...","normal","base")

    if masturbating:
        g4 "{size=-4}(Yes! You little whore! You little fucking whore!) *Panting*{/size}"
    else:
        m "......................."

    call her_main("I understand that you may not have time for this, professor. After all, you are the headmaster of our school, and a very busy man.","open","angryCl")
    her "Being a top student is hard on me as well, sometimes..."

    if masturbating:
        g4 "{size=-4}(She said \"hard-on\"!) *Panting*{/size}"

    her "But you could delegate that task to me..."
    her "Just put your faith in me, professor."

    if masturbating:
        call her_main("Yes, you can do it! Just put it in me, sir!","base","base")
        stop music fadeout 1.0

        g4 "{size=-4}(Oh crap, that did it!) *Argh!*{/size}"
        hide screen hermione_main
        hide screen bld1
        with d3
        pause.2

        call cum_block

        call gen_chibi("cumming_behind_desk")
        with d3
        pause 3

        call her_main("Professor?! What is going on...?","angry","wide")

        g4 "Ah... YESSSSS.....!"
        her "???"
        g4 "*breathing heavily* Yes! yes...."

        call gen_chibi("came_on_desk")
        with d3
        pause.5

        m "Yes, girl. It's all exactly as you say and I will.... take care of it all."
    else:
        m "Alright... I will think about your proposal, I promise."

    call her_main("Really?","normal","frown")
    her "hm..........."

    call play_music("chipper_doodle")

    call her_main("That's a relief! Thank you, professor.","open","angryCl")

    if masturbating:
        m "No, no, thank you..."
        call her_main("Hm...","normal","frown")

    call her_main("My classes are about to start, so I'd better go now.","open","angryCl")
    her "Thank you for your time..."

    call her_walk("mid","leave",2)

    if masturbating:
        m "{size=-4}(This was awesome...) *Panting*{/size}"
        m "{size=-4}(My trousers are ruined though...){/size}"
    else:
        m "................."
        m "(She is cute, but quite a piece of work...)"

    hide screen genie_jerking_sperm_02
    with d3

    $ snape_against_hermione = True #Turns True after event_08. Activates special date with Snape # 01.
    $ event08_happened = True

    call play_music("brittle_rille")

    return



### EVENT 9 ###

#Second visit from Hermione. Says she sent a letter to the Minestry.
#Takes place after first special event with Snape, where he just complains about Hermione.
label event_09:
    stop music fadeout 3.0
    call play_sound("knocking") #Sound someone knocking on the door.
    "*Knock-knock-knock!*"

    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger."
            m "(It's that young witch again...)"
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    $ achievement.unlock("knock")
                    return
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well alright..."
            $ achievement.unlock("knock")
            return
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            call play_sound("knocking") #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    $ event09 = True #You let Hermione in. This event will stop looping now.

    call play_sound("door") #Sound of a door opening.

    call her_walk("door","mid",3)
    pause.5
    call bld

    call play_music("chipper_doodle")

    call her_main("","normal","base",xpos="base",ypos="base")
    call ctc

    call her_main("Good morning, professor Dumbledore.","open","angryCl")

    menu:

        "\"Good morning, child.\"":
            call her_main("{size=-4}(Again with the \"child\"...){/size}","annoyed","frown")
            call her_main("Sir, I would appreciate it if you would treat me as an equal...","open","angryCl")
            m "{size=-4}(I'm literally millions of years older than you, witch. We are anything but equal.){/size}"
            m "...................."
            call her_main("................","annoyed","frown")
        "\"Good morning, miss Granger.\"":
            her "Ehm... so, about the reason of me being here today then..."
        "\"Yeah, yeah, whatever...\"":
            pass

    her "I see that no matter what I do I simply cannot get through to you, sir."
    call her_main("So in light of your negligence, I decided to take the initiative myself!","open","angryCl")
    m "Did you now...?"
    her "Yes! We, the proud students of Hogwarts, detest sexism..."
    her "No individual shall be treated differently based on his or her gender."
    m "But--"
    call her_main("Please, let me finish, professor!","angry","angry")
    call her_main("I'm organizing the \"Men's rights movement\" in our school!","open","angryCl")
    g4 "Oh boy, this is just so typical!"
    g4 "Blame everything on--"
    stop music fadeout 1.0
    m "Wait, did you say {size=+5}MEN'S{/size} rights movement?"
    call play_music("chipper_doodle")
    call her_main("You have no idea how hard it is to be a boy in our school these days...","open","worried")
    menu:
        "\"Didn't see this one coming...\"":
            call her_main("No, you did not, because you, refuse to listen to us, sir!","open","angryCl")
            her "But we will make you hear us..."
        "{size=-3}\"That's literally the dumbest idea I've ever heard.\"{/size}":
            call her_main("I knew you would say something like that...","normal","frown")

    call her_main("Did you know that some of the girls in this school are now selling favours for house points...?","annoyed","frown")
    her "Sometimes even for good grades..."
    m "Really?"
    call her_main("Nobody from the \"Gryffindor\" house of course...","open","angryCl")
    her "And that's what puts us at a disadvantage - our integrity!"
    her "As for the boys - they have to work ten times harder than the girls simply to pass a test..."
    her "Or, if they are lucky enough, to get one meagre house-point..."
    call her_main("This is sexism in its purest form!","open","base")
    menu:
        m "..."
        "\"What do you want me to do?\"":
            call her_main("Nothing!","normal","base")
            m "Great. I'm good at that."
        "\"I'm not sure what to say...\"":
            call her_main("You do not need to say anything anymore, professor.","normal","base")
        "\"You are being ridiculous!\"":
            call her_main("Am I? Well, we'll see...","normal","frown")

    call her_main("I already sent a letter to the ministry of magic.","open","angryCl")
    with hpunch
    g4 "{size=+7}You did what?!{/size}"
    m "{size=-4}(Wait, do I really give a damn about that?){/size}"
    her "I'm sorry, but you left me no choice, professor."

    her "Now, if you'll excuse me, I must get to my classes..."

    call her_walk("mid","leave",2)

    m "...................."

    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.

    call play_music("brittle_rille")

    return



### EVENT 11 ###

#Third visit, after second special date with Snape. Hermione complains that she almost failed a test. (EVENING EVENT!)
label event_11:
    stop music fadeout 1.0
    call play_sound("knocking") #Sound someone knocking on the door.
    "*Knock-knock-knock!*"

    her "Professor, I'm coming in!"
    m "...."

    call play_music("chipper_doodle")
    call play_sound("door") #Sound of a door opening.

    $ hermione_wear_robe = True
    call update_her_uniform

    call her_walk("door","mid",2.1) #Hermione Chibi stands still after.

    call bld
    pause.5

    call her_main("","annoyed","frown",xpos="base",ypos="base")
    call ctc

    call her_main("Good evening, professor.","annoyed","angryL")

    menu:
        "\"-stare full of hatred-\"":
            call her_main("You can stare at me all you want, sir.","normal","frown")
            her "It will not make the problems of this school go away."
        "*sigh of exasperation*":
            call her_main("Is this a bad time?","normal","base")
            call her_main("Well, since I'm already here...","open","base")
        "\"....................................\"":
            call her_main("Professor?","open","base")
            m "Yes, yes..."

    call her_main("Something... bizarre has happened today...","open","angryCl")
    call her_main("I'm Not sure how to describe this...","normal","frown")
    call her_main("................................","annoyed","frown")
    call her_main("I think I almost failed a test...","annoyed","angryL")

    menu:
        "\"That happens to students sometimes.\"":
            call her_main("To other students, yes. But not to me, sir!","annoyed","angryL")
            call her_main("Never to me...","soft","baseL")
        "\"(Way to go, Snape!)\"":
            call her_main("Excuse me?","normal","base")
            m "What?"
            m "Oh, I said, that's too bad. How are you holding up?"
            call her_main(".................","normal","frown")
        "\"So why tell me?\"":
            her "Because... this is not an ordinary event!"

    her "I'm not sure what is going on here..."
    m "An evil scheme against you, miss Granger?"
    call her_main("This is not a laughing matter, sir.","normal","base")
    call her_main("You should consider me a \"measuring stick\" for our educational system.","open","angryCl")
    her "If I \"almost\" fail a test, the rest of the students will definitely fail it."
    m "Is that so...?"
    call her_main("Yes, professor. Something went terribly wrong today...","normal","frown")
    call her_main(".................................","annoyed","angryL")
    call her_main("But what if it didn't?","open","worried")
    her "What if all the tests will be this difficult from now on?"
    call her_main("I need to study harder!","open","worriedL")

    label cant_say:
    menu:
        "\"I could tutor you, miss Granger.\"":
            call her_main("You, professor?","open","base")
            call her_main("Oh, thank you for your offer but I don't think that would be necessary, sir.","soft","base")
            call her_main("The best tutor is a book, and I have the entire Hogwarts library at my disposal.","open","closed")
        "\"A wise decision, miss Granger.\"":
            call her_main("Thank you, professor.","soft","base")
        "\"You need to put my cock in your mouth.\"":
            m "You need to put my co--"
            call her_main("Huh?","soft","base")
            m "{size=-4}(No, I can't actually say that...){/size}"
            call her_main("......?","annoyed","suspicious")
            jump cant_say

    m "............"
    call her_main("Well, if there is nothing else, I have a studying schedule to keep.","open","closed")
    m "By all means..."

    call her_walk("mid","leave",2)

    $ hermione_wear_robe = False

    $ event11_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.

    call play_music("night_theme")

    return



### EVENT 12 ###

#Hermione complains that she might have failed a test. (EVENING EVENT!)
label event_12:
    call play_sound("door")

    call her_walk("door","desk",2.8)

    call play_music("chipper_doodle")

    her "Professor! I need to talk to you!"
    m "(So She doesn't even bother to knock anymore?)"
    call bld

    call her_main("Professor, something awful happened today!","open","worried",xpos="right",ypos="base")
    her "I failed a test today..."
    her "I cannot believe this is happening!"
    call her_main("How is this even possible?!","angry","wide")

    menu:
        "\"You should study more, girl!\"":
            call her_main("But I studied all night for this test!","soft","base",tears="soft")
        "\"There, there... It'll be alright.\"":
            call her_main("No it won't! This is a catastrophe!","mad","worriedCl",tears="soft_blink")

    call her_main("And the worst part is that I think I might be the only one who failed...","angry","base",tears="soft")
    call her_main("How will this make me look?","angry","base",tears="soft")
    call her_main("I will know for sure when we get the results though...","normal","baseL",tears="soft")
    call her_main("Yes, I'm sure everyone else failed as well...","soft","baseL")
    call her_main("I mean, they must have, right?","open","worried")
    call her_main(".....................","soft","baseL")
    call her_main("....right?","open","worried")

    menu:
        "{size=-3}\"Of course. You are a top student after all.\"{/size}":
            call her_main("Exactly...","annoyed","frown")
            her "Or at least I used to be until today..."
            call her_main("I cannot believe this is happening!","mad","worriedCl",tears="soft_blink")
        "{size=-3}\"You could prepare better if I were to tutor you.\"{/size}":
            $ tutoring_offer_made = True #Affects conversation in the next event.
            call her_main("hm...","annoyed","suspicious")
            call her_main("Yes, that could help I suppose...","soft","baseL")
            call her_main("I appreciate your offer, professor, but...","open","base")
            her "May I think about it?"
            m "Don't take too long..."
        "{size=-3}\"I suppose we'll know soon enough.\"{/size}":
            call her_main("Yes, I suppose we will...","soft","base")

    call her_main("I'm sorry, professor, I'm probably just overreacting anyway...","grin","worriedCl",emote="05")
    call her_main("But you must understand that my reputation is at stake here!","open","base")
    call her_main("There's gotta be something wrong with the test...","annoyed","angryL")
    her "And although I failed, I probably still got the most points on the test..."
    her "As usual..."
    call her_main("Well, I'd better go now. We have another \"MRM\" meeting today.","open","angryCl")
    her "I will let you know about the new ideas we come up with tonight."
    m "I can hardly wait..."

    call her_walk("desk","leave",3)

    $ event12_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.

    jump day_start



### EVENT 13 ###

#Hermione complains that she did fail the test. (EVENING EVENT!)
label event_13:
    call play_sound("door")

    call her_walk("door","mid",2)

    her "....................."
    m "???"

    call her_walk("mid","desk",1.6)

    her "............"
    m "Miss Granger?"
    her "..............................."
    m "Miss Granger?!!"
    call bld

    call her_main("","upset","dead",tears="mascara",xpos="right",ypos="base")
    call ctc

    her "Huh?"
    her "Oh, I'm already here?"
    her "I'm sorry, sir... I..."
    her ".................."
    her "It seems that I did..."
    her "I did... uhm..."
    her "... I failed that test after all."
    her "I..."
    call her_main("I'm sorry, professor...","upset","worriedCl",tears="mascara_soft_blink")
    her "I'm not sure why I'm here..."
    her "I think I'd better go..."
    m "..................."

    call her_walk("desk","leave",1,action="run")

    pause.3
    m "............."
    m "She will be alright..."
    m "I think..."

    $ event13_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.

    jump day_start



### EVENT 14 ###

#Hermione comes after her breakdown (when she failed the test). She is asking for tutoring. Tutoring unlocked.
label event_14:
    call play_music("chipper_doodle")
    call play_sound("door")

    call her_walk("door","mid",2)
    call bld

    call her_main("Good morning, Professor.","base","base",xpos="base",ypos="base")
    m "How can I help you today, miss Granger?"
    call her_main("Well, first of all, I am terribly sorry about yesterday's display, sir...","open","angryCl")
    call her_main("I've never failed a test in my life, so I wasn't sure how to react...","open","suspicious")
    call her_main("But I'm all better now...","open","angryCl")
    m "I see..."
    her "I will not take much of your time, I promise..."

    if tutoring_offer_made:
        her "I am here to take you up on your offer."

        menu:
            "\"What offer?\"":
                her "A while back you offered to tutor me, sir..."
                menu:
                    "\"Oh... That offer has expired.\"":
                        call her_main("It...","open","base")
                        her "Expired, sir?"
                        her "B-but...."
                        call her_main("But I require tutoring, and you are the smartest wizard I know...","open","worried")
                        call her_main("Please, sir. I really need your help.","angry","worried")
                        menu:
                            "\"Show me your tits and it's a deal!\"":
                                call her_main("m-my...?","angry","wide")
                                call her_main("............","annoyed","worriedL")
                                her "....."
                                with hpunch
                                call her_main("{size=+5}Professor Dumbledore!!!{/size}","scream","angryCl")
                                m "{size=-5}(Well, at least I tried...){/size}"
                                her "I am not some \"Slytherin\" floozy!"
                                m "Of course not, miss Granger."
                                m "It was a test... You passed. Good job."
                                call her_main("What...?","open","base")
                                call her_main("Oh, of course. I'm so silly sometimes. Sorry about the yelling, sir.","grin","worriedCl",emote="05")
                                m "My offer is still valid. If you want me to then I can tutor you."
                                call her_main("..............","annoyed","worriedL")
                            "\"Well, alright, alright...\"":
                                pass
                    "\"Oh, that's right. Great.\"":
                        pass

            "\"Splendid! Starting today?\"":
                pass

    else:
        call her_main("I... uhm...","normal","frown")
        her "Sir, I hope this is not too much to ask..."
        m "Yes?"
        her "Ehm... would it be alright if..."
        her "..............."
        call her_main("do You think you could tutor me a little, sir?","annoyed","frown")
        menu:
            "\"I suppose that is possible.\"":
                pass
            "\"Hm... I'm quite busy actually.\"":
                call her_main("Sir, please, you are the smartest wizard I know!","open","worried")
                m "{size=-4}(You have no idea, little witch.){/size}"
                m "Well, it could be arranged, I suppose..."

    call her_main("Thank you, sir. I am very grateful.","base","base")
    call her_main("Just let me know when, and I will bring my books!","open","closed")
    call her_main("I must study even harder from now on...","annoyed","frown")
    call her_main("And I'll be taking private lessons from you, sir, as often as possible.","base","base")
    call her_main("But that's not all...","normal","frown")
    her "The \"MRM\" shall investigate our education system much closer now..."
    her "I think some sort of foul play might be taking place..."
    m "No way!"
    her "I have a list of suspects already but I will get back to you on this later...."
    m "Ehm... alright..."
    call her_main("Oh, my classes are about to start. I'd better go...","open","worriedL")

    call her_walk("mid","leave",2)

    stop music fadeout 1.0

    call give_reward(">You've unlocked the ability to summon Hermione to your office.","interface/icons/head/head_hermione_1.png")
    $ achievement.unlock("unlockher", True)
    $ hermione_unlocked = True #Unlocks after event_14. Adds "Summon Hermione" button to the door.
    $ hermione_busy = True
    $ tutoring_hermione_unlocked = True

    $ event14_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.

    call play_music("brittle_rille")

    return



### EVENT 15 ###

#Hermione comes and asks to buy a favour from her.
label event_15:
    call play_sound("knocking")

    "*Knock-knock-knock!*"

    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger."
            m "(It's that young witch again...)"
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    $ achievement.unlock("knock")
                    return
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well, alright..."
            $ achievement.unlock("knock")
            return
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            call play_sound("knocking")
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    call play_sound("door")

    call her_walk("door","mid",3)

    call her_main("Good evening, professor...","soft","baseL",xpos="base",ypos="base")
    her "........................"
    call her_main("........................","annoyed","worriedL")
    her "........................"
    call her_main("Ehm......","open","base")
    call her_main(".................","annoyed","worriedL")
    m "What is it, miss Granger?"
    call her_main("Well, ehm...","open","base")
    her "You see... The \"Gryffindor\" house is not in the lead anymore..."
    call her_main("And... everyone is working so hard...","annoyed","worriedL")
    her "And they look up to me for help but I don't know what to do..."
    m "............................"
    her "Professor Dumbledore...."
    stop music fadeout 2.0
    call her_main("I want you to buy a favour from me!","scream","worriedCl")
    call her_main("","normal","worriedCl")

    menu:
        "\"You mean like a sexual favour?\"":
            call her_main("Ehm... I'm not sure...","angry","worriedCl",emote="05")
            her "The kind that would gain our house additional points..."
            call her_main("I could write an essay for you or...","open","base")
            call her_main("Or maybe clean your tower..?","angry","worriedCl",emote="05")
            m "{size=-4}(Clean my tower? Heh... There's gotta be dirty joke in there somewhere...){/size}"
            m "Well, alright then, I think we can figure something out."
        "\"Well, if you insist...\"":
            pass
        "\"I don't think so, miss Granger.\"":
            call her_main("B-but... We need the points...","open","base")
            her "Professor, please, I am really desperate..."
            m "Desperate you say..?"
            m "Well, alright..."

    call play_music("chipper_doodle")
    call her_main("Thank you, professor...","base","base")

    label choose_favor_agagin:
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    her "So... What will it be?"

    menu:
        "\"Show me your tongue...\"":
            $ d_flag_01 = True
            pass
        "\"Stand there. Let me look at you.\"":
            $ d_flag_02 = True
            pass
        "\"Make a silly face...\"":
            $ d_flag_03 = True
            pass
        "\"Say \"I've been a bad girl\".\"":
            $ d_flag_04 = True
            pass

    her "Em..."
    her "How many house points will I get for that...?"
    $ d_flag_05 = False # 20 Points.
    $ d_flag_06 = False # 40 Points.
    $ d_flag_07 = False # 10 Points.
    $ d_flag_08 = False # 1 Point.

    menu:
        "\"1 point.\"":
            if d_flag_02: #Stand there.
                $ d_flag_08 = True # 1 Point.
                pass
            else:
                her "I don't think it's worth it then..."
                jump choose_favor_agagin
        "\"10 points.\"":
            if d_flag_02: #Stand there.
                $ d_flag_07 = True # 10 Points.
                pass
            else:
                her "I don't think it's worth it then..."
                jump choose_favor_agagin
        "\"20 points.\"":
            $ d_flag_05 = True
            her "So little...?"
            pass
        "\"40 points.\"":
            $ d_flag_06 = True
            pass

    call her_main("Em, alright...",xpos="mid",ypos="base",trans="fade")

    if d_flag_01: #Show me your tongue.
        call her_main("M-my... tongue, sir?","grin","worriedCl",emote="05")
        m "Yes, girl. Open your mouth, and show me your tongue."
        call her_main("{size=-7}(What a weirdo...){/size}","annoyed","angryL")
        call her_main("Ehm... well, alright then...","normal","frown")
        call her_main("Here...","open","suspicious")
        call her_main(".............","open_tongue","glance")
        her "............."
        call her_main(".................","open_tongue","angryL")
        call ctc

        menu:
            "\"Very good. Here are your points.\"":
                pass
            "\"Not good enough. You can do better\"":
                call her_main("...............","annoyed","angryL")
                her "Alright, I will try to do better, sir..."
                call her_main("How about this?","open","worried")
                call her_main("A-a-ah..................","scream","baseL")
                call her_main("............................","open_wide_tongue","squintL")
                call her_main("......................................","open_wide_tongue","down_raised")
                her "..................................................."
                her "...................................................................."
                call her_main(".......................................................................................................","open_wide_tongue","angryCl")

    if d_flag_02: #Stand still...
        call her_main("So, I just have to stand here then...?","base","base")
        m "Good... Now turn around... slowly."
        her "uhm... alright..."
        hide screen hermione_main
        hide screen bld1
        pause.5

        show screen hermione_stand_f #Hermione stands still.
        with d7

        call her_main(".................................","annoyed","baseL",flip=True)

        menu:
            m "Hm..."
            "\"The uniform suits you, miss Granger...\"":
                call her_main("............","soft","baseL",cheeks="blush")
                call her_main("Thank you, professor Dumbledore...","open","baseL",cheeks="blush")
            "\"You have a nice body, miss Granger...\"":
                call her_main("!!?","soft","wide")
                call her_main("..............","annoyed","angryL",cheeks="blush")
                call her_main("Thank you, professor...")
            "\"That's enough. Here are your points...\"":
                show screen hermione_stand #Hermione stands still.
                with d7
                pause.5
                show screen bld1
                with d3
                jump stupid_enogh

        m "Very good, you can turn back now..."
        show screen hermione_stand #Hermione stands still.
        with d7
        pause.7

        show screen hermione_main
        call bld
        her "................."

    if d_flag_03: #STUPID FACE
        call her_main("A silly face then...","grin","worriedCl",emote="05")
        her "Let's see..."
        label stupid_faces:
        call her_main("How about this one?","silly","silly")

        menu:
            "\"Good! Very stupid! I mean, silly.\"":
                jump stupid_enogh
            "\"Not stupid enough.\"":
                pass

        call her_main(".........","annoyed","angryL")
        call her_main("What about this one then?","disgust","narrow")

        menu:
            "\"Ha-ha! You look like an idiot!\"":
                jump stupid_enogh
            "\"No, not stupid enough.\"":
                pass

        call her_main(".........","annoyed","angryL")
        call her_main("What if I do it like this?","full","ahegao_intense")

        menu:
            "\"Good! Very stupid.\"":
                jump stupid_enogh
            "\"Not stupid enough.\"":
                jump stupid_faces

    if d_flag_04: #BAD GIRL
        call her_main("I...","normal","frown")
        her "I have been a very bad girl..."
        g9 "Have you been a very, very, very bad girl?"
        her "Yes, sir..."
        her "I have been very, very, very, very bad..."

        label to_early_for_sucking_cocks:
        menu:
            g9 "..."
            "\"Do you need to be punished?\"":
                call her_main("Do I need to... be punished?","open","worried")
                call her_main("Ehm...","soft","baseL")
                her "....................."
                call her_main("Well, I am not perfect, if that's what you mean, sir...","annoyed","angryL")
                call her_main("But do I need to be punished... hm?","soft","baseL")
                call her_main("Is this really for me to decide...? I mean...","normal","frown")
                her "What does this have to do with anything?"
                m "You are overanalyzing this, girl."
                m "Just say that you need to be punished!"
                call her_main("Fine. I need to be punished!","angry","angry")
                call her_main("{size=-5}(And I truly do think so sometimes...){/size}","normal","worriedCl")
                m "That's a good girl."
                call her_main("................??","upset","wink")
                m "Now that wasn't hard at all, was it?"
                call her_main("n-no , sir...","annoyed","worriedL")
                m "Alrighty, then..."
            "\"Do you want to get spanked?\"":
                call her_main("Do I want to...","open","worried")
                call her_main("Get s-spanked??","angry","wide")
                call her_main("Tsk!","angry","angry")
                call her_main("Professor, I don't think I'm comfortable with--","open","angryCl")
                m "Apologies, let me rephrase the question..."
                m "How badly do you need those points?"
                call her_main("..................","annoyed","frown")
                call her_main("Yes, sir. I do need to get spanked.","open","angryCl")
                m "Alright, that's good enough for now..."
                call her_main("{size=-4}(For now?){/size}","normal","frown")
            "\"Come here and suck my cock!\"":
                m "{size=-5}(Too early for this... I need to reel her in first.){/size}"
                jump to_early_for_sucking_cocks

    label stupid_enogh:
    if d_flag_05:
        m "20 points to the \"Gryffindor\" house."
        $ gryffindor +=20
    elif d_flag_06:
        m "40 points to the \"Gryffindor\" house."
        $ gryffindor +=40
    elif d_flag_07:
        m "10 points to the \"Gryffindor\" house."
        $ gryffindor +=10
    elif d_flag_08:
        m "1 point to the \"Gryffindor\" house."
        $ gryffindor +=1

    call her_main("Yay!..............","grin","worriedCl",emote="05",xpos="base",ypos="base",flip=False,trans="fade")
    her "This was quite easy..."
    her "Do you think you could buy some more favours from me in the future, professor?"

    menu:
        "\"I don't think that's a good idea.\"":
            call her_main("Please, professor...","angry","worried")
            her "We really need those points..."
            m "......."
            call her_main("You are an esteemed wizard and to be honest...","annoyed","worriedL")
            her "The only person in this school whom I don't mind asking for this..."
            m "Well, when you put it that way..."
        "\"That's a possibility...\"":
            pass

    call her_main("Thank you, professor. Thank you so much.","base","base")
    call her_main("Well... I suppose I'd better go now...","base","base")
    m "............"

    call her_walk("mid","door",2)
    pause.3

    if d_flag_01: #Show me your tongue
        her "{size=-4}(Hm...){/size}"
        her "{size=-4}(Students show teachers their tongues all the time...){/size}"
        her "{size=-4}(Although that's usually when the teacher is not looking...){/size}"
        her "{size=-4}(But there is nothing wrong with what I did today...){/size}"
        her "{size=-4}(I earned my house extra points...){/size}"

    if d_flag_02: #Stand still...
        her "{size=-4}(I can just stand there and let the professor look at me...){/size}"
        her "{size=-4}(There is nothing wrong with that... nothing at all...){/size}"

    if d_flag_03:
        her "{size=-4}(Stupid face...){/size}"
        her "{size=-4}(Stupid face...){/size}"
        her "{size=-4}(I need to practice this.){/size}"

    if d_flag_04:
        her "{size=-4}(I'm a bad girl...){/size}"
        her "{size=-4}(I am very bad...){/size}"
        her "{size=-4}(Yes, I can say things like that easily...){/size}"
        her "{size=-4}(There is nothing wrong with that... nothing at all...){/size}"

    call her_chibi("leave")

    stop music fadeout 1.0

    call give_reward(">You unlocked the ability to buy sexual favours from Hermione.","interface/icons/head/head_hermione_2.png")

    $ hermione_favors = True

    $ event15_happened = True #Turns TRUE after event_15
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $ hermione_busy = True

    return



init python:
    class wt_silver_event(object):
        day_wait = 0
        completed = False
