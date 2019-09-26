

### Astoria Intro ###

### Event 1 ###
# Tonks tells you about a student that has used the Imperius curse at school.
# You need to ask Snape and Hermione to help find the student.

label astoria_intro_E1:
    if "poster_1_store" not in tonks_mail_list:
        $ tonks_mail_list.append("poster_1_store")

    stop music fadeout 1.0
    call play_sound("knocking")
    "*knock-knock-knock*"

    ton "[ton_genie_name], may I come in?"
    ton "We have to talk about some recent events that happened..."
    ton "It's quite urgent..."

    menu:
        m "(...)"
        "\"Yes, come in!\"":
            ton "Thank you..."

        "\"Not now!\"":
            ton "I'm sorry Sir, but I'm afraid this can't wait."
            ton "I'm coming in..."

    # Tonks walks in.
    call ton_walk(action="enter", xpos="desk", ypos="base", speed=2.8)

    call play_music("tonks_theme")
    call ton_main("Good evening, [ton_genie_name].","base","base","base","mid", xpos="mid", ypos="base")
    m "[tonks_name]..."
    call ton_main("I'm terribly sorry for bursting in like this!","open","base","worried","R")
    m "What in the world got you so flustered?"
    call ton_main("We might be in big trouble, [ton_genie_name]!","upset","base","worried","mid")

    call play_music("playful")
    g9 "Miss Tonks... Have you been a bad girl?"
    call ton_main("I'm not joking, [ton_genie_name]!","angry","base","angry","mid")
    call ton_main("Something terrible has happened at school today!","open","base","angry","R")
    call ton_main("I believe one of our students has conducted some highly illegal activities against another student!","upset","base","worried","R")
    call ton_main("We have to take action!{p=0.6}The last thing we need is for this to reach the Ministry's attention!","open","base","angry","mid")
    m "So? Isn't it your task to cover that sort of stuff?"
    call ton_main("Yes, but...","upset","base","worried","down")
    call ton_main("Please, [ton_genie_name]! I can't cover this up all on my own!","open","base","worried","mid")
    call ton_main("I require your help...","upset","base","sad","mid")
    m "My help, you say?"
    call ton_main("Yes...","base","base","worried","down")

    menu:
        m "(...)"
        "\"How exactly can I help you?\"":
            pass

        "\"I'm busy right now...\"":
            call ton_main("Busy with what exactly?","open","base","raised","mid")
            m "...................."
            call ton_main("[ton_genie_name]?","angry","base","angry","mid")
            m "Please give me a minute... I'm still thinking..."
            call ton_main("We don't have time for this!","angry","base","angry","mid")
            m "I have all the time in the world, darling..."
            m "I'm immortal..."
            call ton_main("Could you please just listen to me?","angry","closed","angry","mid")

        "\"What's in it for me?\"":
            call ton_main("Are you seriously asking me that?","open","wide","wide","wide")
            call ton_main("If this doesn't get dealt with immediately, they'll have us both locked up in a cell in Azkaban, do you hear me?!","angry","base","angry","mid")
            m "Loud and clear..."
            m "I'll be locked up in a cell - together with you..."
            g9 "I can think of many fates worse than that, if I'm honest."
            call ton_main("Weren't you so scared of that very thing before?","open","base","raised","mid")
            g9 "Not when I'm accompanied by someone as lovely as you!"
            call ton_main("................","upset","base","worried","R")
            call ton_main("You are clearly insane!","open","base","angry","mid") # Annoyed
            call ton_main("Fine... Tell me what you want so we can continue...","upset","base","worried","mid")
            m "Hmm..."

            $ d_flag_01 = False

            label astoria_intro_E1_choices:

            menu:
                m "How about you..."
                "\"Pull on my finger...\"" if d_flag_01 == False:
                    $ d_flag_01 = True
                    call ton_main("I'm sorry?","open","base","raised","mid")
                    g9 "Come on. It's an old trick we Genies like to do!"
                    m "It's harmless, I swear..."
                    call ton_main(".............","upset","base","angry","R")
                    call ton_main("Very well...","open","closed","base","mid")
                    pause.2

                    # Tonks walks over.
                    call hide_characters
                    hide screen bld1
                    show screen blkfade
                    with d3

                    # Genie and Tonks stand behind the desk.
                    $ gen_chibi_zorder = 1
                    $ ton_chibi_zorder = 1
                    call ton_chibi("stand","275","behind_desk")
                    call gen_chibi("stand","190","behind_desk")
                    show screen chair_left
                    show screen desk
                    hide screen blkfade
                    with fade
                    pause.8

                    call bld
                    g9 "Now pull it."
                    call ton_main("..................................","upset","base","worried","down", ypos="head")
                    m "Try a bit harder..."
                    call ton_main("..............................................","angry","base","angry","down")
                    call bld("hide")
                    pause.2
                    with hpunch
                    pause.5

                    call bld
                    g4 "Why isn't this working?!"
                    m "(Oh, that's right...)"
                    m "(I forgot we Genies are unable to fart...)"
                    call ton_main("Are we done here?","open","closed","base","mid")
                    m "Want to give it one more try?"
                    call ton_main("I think not...","open","base","base","R")
                    call ton_main("I expected a bit more from a Genie... A magic trick, perhaps?","upset","base","sad","down")
                    m "I've told you, I can't do magic anymore..."
                    call ton_main("How very disappointing...","open","closed","base","mid")
                    call ton_main("I'm starting to have my doubts that you ever were a Genie...","angry","base","worried","R")
                    m "Sorry about that..."
                    m "Can I ask you for something else?"
                    call ton_main("Still? Even after disappointing me like this?","upset","base","angry","mid")
                    m "Please?"
                    call ton_main("*Ugh*... Fine...","upset","base","angry","R")
                    show screen blkfade
                    hide screen bld1
                    with d3

                    $ gen_chibi_zorder = 2 # Default
                    $ ton_chibi_zorder = 3 # Default
                    call gen_chibi("sit_behind_desk")
                    call ton_chibi("stand","desk","base")

                    hide screen blkfade
                    call ton_main("","upset","base","base","mid", xpos="mid", ypos="base", trans="fade")

                    jump astoria_intro_E1_choices

                #"\"Blow me!\"":
                #    call ton_main("Blow you? With my mouth?","base","base","base","mid")
                #    m "Yes, please."
                #    call ton_main("On your dick, I imagine?","base","base","base","mid")
                #    g9 "Yes, if you would..."
                #    call ton_main("Very well...","base","base","base","mid")
                #    call ton_main("Get it out for me, would you...","base","base","base","mid") # Naughty look
                #    g9 "!!!"
                    # Tonks walks over.
                    # Blkfade.
                    # Genie and Tonks stand behind the desk.
                    # Genie has his dick in hand, jerking off.

                #    call nar("To your surprise, Tonks \"blows\" a gust of wind over \"your cock\"...")
                #    call ton_main("There, all done.","base","base","base","mid")
                #    m ".............."
                #    call ton_main("What? I did what you asked for... I blew your cock...","base","base","base","mid")
                #    m "......................"
                #    call ton_main("Now, could we get back to discuss what I came here for in the first place?","base","base","base","mid")
                #    m "Fine. I know when I'm outwitted..."
                #    call ton_main("I will suck your delicious cock some other time, [ton_genie_name]... I promise!","base","base","base","mid")
                #    call ton_main("But now, we simply don't have time to fool around, I'm afraid...","base","base","base","mid")

                "\"Send Nudes.\"":
                    call ton_main("Nudes, [ton_genie_name]?","upset","base","raised","mid")
                    g9 "Yes! Send me some nude pictures of yourself!"
                    g9 "A poster, maybe?"
                    call ton_main("*Oh*...","upset","base","base","down")
                    call ton_main("A poster, you say?...","horny","base","base","mid")
                    call ton_main("What are you gonna do with it? Put it on your wall and fap to it?","horny","base","angry","mid")
                    g9 "You can count on that!"
                    call ton_main("Hold on!{w} Are you going to hang it up here? In your office?!","open","wide","wide","wide")
                    m "Sure... It's not like there are that many other rooms I can go to..."
                    call ton_main("(Oh my... So everyone would be able to see it...)","upset","base","worried","R", hair="horny")
                    call ton_main("(All those girls that come in here...)","upset","base","base","ahegao")
                    call ton_main("(As long as my face isn't on it, this shouldn't be too bad...)","angry","base","worried","down")
                    call ton_main("...","upset","base","worried","R")
                    call ton_main("Very well, I shall send you an owl with it tomorrow morning, [ton_genie_name].","base","base","base","mid")
                    g9 "Sweet!"
                    call ton_main("Now, here is what I'll require your help with...","open","closed","base","mid")

                    if "poster_1_gift" not in tonks_mail_list:
                        $ tonks_mail_list.append("poster_1_gift")
                        $ tonks_mail_list.remove("poster_1_store")

    call ton_main("This girl I've told you about, Susan Bones?","open","base","base","mid")
    call ton_main("The one with-","open","base","base","R")
    g9 "With the giant tits!"
    call ton_main("...The one with the unfortunate luck of being a constant target of bullying and harassment!","angry","closed","angry","mid") # Annoyed
    m "Yes, that too..."
    call ton_main("That poor girl! She cried the entire time when she told me about what happened...","open","base","sad","down")
    call ton_main("I can't believe she got hit by a curse!","angry","base","angry","down") # Angry
    m "At least she isn't dead..."
    call ton_main("No, of course not!","open","base","angry","mid")
    m  "Or Injured?"
    call ton_main("Thankfully not...","upset","base","base","R")
    m "And nobody tried to shrink her tits?"
    call ton_main("Don't be silly...","open","closed","base","mid")
    m "Then what are you concerned about exactly?"

    call ton_main("This is something quite serious!","angry","base","sad","mid")
    call ton_main("If we don't find the culprit of this, and find them quickly, the Ministry will be on our toes by tomorrow!","open","base","angry","mid")
    m "That bad, huh?"
    call ton_main("Yes, I'm afraid...","upset","base","worried","down")
    call ton_main("She was the target of an \"unforgivable curse!\"","open","base","worried","mid")
    m "A curse?..."
    m "Like...{w=0.5} The c-word?"
    call ton_main("No! A magical curse!{w} not an insult...","angry","closed","angry","mid")
    call ton_main("Those curses are a major transgression of Ministry laws!","open","base","angry","mid")
    call ton_main("If you are caught having cast even one of them, they will put you in Azkaban for the rest of your life!","open","closed","worried","mid")
    call ton_main("Sharing a room with a whole bunch of Dementors!","upset","base","angry","mid")
    m "Dement-{w=0.6}ors?"
    m "Is it like a nursing home or something?"
    call ton_main("No, I've told you before!","angry","closed","angry","mid")
    call ton_main("Azkaban is a prison! With Dementors roaming all over it...","open","base","angry","mid")
    call ton_main("Believe me, you wouldn't want to be around them, I tell you that much...","open","base","angry","R")
    m "(Does she hate old people as well now?)"

    call ton_main("Should the Ministry find out about what happened to... Miss Bones.","upset","base","worried","R")
    g9 "*He-he-he!*..."
    call ton_main("Which they most certainly will, as her aunt is head of the Ministry's department for \"Magical Law Enforcement\"...","open","base","worried","mid")
    call ton_main("Our whole operation would be busted! And we'd get locked up once and for all!","upset","base","sad","mid")

    m "So, are we in trouble?"
    call ton_main("Not yet...","open","closed","sad","mid")
    call ton_main("I could luckily erase Susan's memory of the ordeal - with the obliviate spell.","angry","base","sad","mid")
    m "You can do that? Neat..."
    call ton_main("But, if this should happen to her again, I doubt there is much I could do to prevent her from telling her aunt right away...","open","base","worried","R")
    m "So what do you suggest we do?"
    call ton_main("Find the student who cursed her, and then talk some sense into her - to never do it again...","open","closed","base","mid")
    m "Find{w=0.2}.{w=0.2}.{w=0.2}.{w=0.8} her?"
    call ton_main("Yes! She heard a girl's voice in her head - while she was under the influence of the imperius curse...","open","base","angry","mid")
    call ton_main("Who told her{w=0.2}.{w=0.2}.{w=0.2}.{w=0.8}to lift up her top.","upset","base","worried","R")
    g9 "Oh yes?"
    call ton_main("The imperius curse can make people do {b}unspeakable things{/b} against their will!","open","closed","angry","mid")
    call ton_main("I have no doubt that someone as sweet and good-hearted as Susan wouldn't know how to defend herself against it...","open","base","sad","mid")
    call ton_main("So... She showed her breasts to a bunch of other students...{w=1.4} unfortunately...","upset","base","sad","R")
    g9 "I wish I could have been there to stop it!"
    call ton_main("Of course you do...","open","closed","base","mid")
    call ton_main("That's sadly all the information I can share...","upset","base","worried","down")
    call ton_main("Nobody that stood with her saw who might have cursed her...","open","base","worried","mid")

    m "Should we get some help finding them?"
    call ton_main("*Hmmm*... That wouldn't be such a bad idea.","base","base","base","R")
    m "Shall I ask Snape? Maybe even Miss Granger?"
    call ton_main("Yes. Professor Snape might prove himself useful for once...","open","base","base","down")
    call ton_main("I don't know about Granger... She'd need to keep quiet at all cost!","angry","base","worried","mid")
    call ton_main("The Ministry can't know about this!","open","base","angry","mid")
    m "Yes. Yes..."
    call ton_main("Well, I should get going... there are a couple of students I'd like to question.","open","base","worried","R")
    m "Good luck, then."
    call ton_main("Talk to you soon, [ton_genie_name].","base","base","worried","mid")

    # Tonks leaves.
    call ton_walk(action="leave", speed=2.5)

    call bld
    m "I should definitely get Snape on this..."
    m "And Granger..."
    g9 "Or I could jerk off instead!" # Achievement if you do, maybe?
    g9 "Yes that seems like a good idea right now!"

    # TODO: Add hidden achievement called "Follow the script!" and unlock it if you jerk off after this scene. Maybe add some Susan smut writing for the jerk-off session?

    $ tonks_busy = True
    $ astoria_intro.E1_complete = True

    jump main_room


### Event 2 - Hermione ###
# You astk Hermione to find the student.

label astoria_intro_E2_hermione:
    m "I require your help with something."
    m "Tonks came by earlier and informed me about a student making a ruckus."
    m "I- *uhm*...{w} She thought maybe you could be of help finding them?"
    call her_main("Of course, Sir.","base","happyCl")
    m "Apparently a student got hit by an \"unforgivable curse\" here at the school."
    call her_main("AN unforgivable CURSE!!!","scream","wide", trans="hpunch")
    call her_main("AT our school?!","shock","wide_stare")
    call her_main("SOMEONE COULD BE DEAD!","scream","wideL")
    call her_main("OR TORTURED!!","disgust","worriedCl")
    call her_main("OR WORSE!!!","disgust","worriedL")
    m "really?"
    call her_main("Those are the only things that can happen with an unforgivable curse, [genie_name]!","angry","worried")
    m "of course... I'm just making sure you were aware of them..."
    call her_main("It's the first lesson we ever received in defence against the dark arts.","open","closed")
    m "Well, one's been cast somewhere on the school."
    m "and I need your help finding out who did it..."
    call her_main("Why do you need my help?","soft","wink")
    call her_main("Surely you're able to detect them?","base","base")
    m "Unfortunately not... I must have been... asleep... when the thing happened..."
    m "I missed my chance, so to speak..."
    call her_main("So how do you expect me to find out who did it?","soft","baseL")
    m "I'm certain that it's the work of another student..."
    m "(or Snape has finally snapped...)"
    m "so I'll need you to go undercover to find out who."
    call her_main("really? You're depending on me to find a criminal student within our school?","soft","down_raised",cheeks="blush")
    m "If it's not too much troub--"
    call her_main("I'd be honoured, [genie_name]!","scream","closed")
    call her_main("It's no doubt the work of one of those despicable \'slytherins\'...","open","angryCl")
    call her_main("Nothing would give me greater pleasure than to see scum like that sent to \'Azkaban\'...","angry","angryL")

    # Genie already knows about Azkaban.
    #m "And what's Azkaban?"
    #call her_main("...Is this another test sir?","open","wink")
    #m "Sure..."
    #call her_main("Of course! I know everything about it!","smile","happy")
    #call her_main("It's the prison of the damned... An impenetrable rocky outcrop surrounded by the harsh North Sea...","open","happyCl")
    #call her_main("the guards are the deathly eaters of all happy thoughts and emotions known as dementors...","open","angryL")
    #call her_main("They endlessly patrol the prison, devouring all hope from the prisoners, driving them mad within a few days...","open","angry")
    #call her_main("Tormenting them relentlessly for the rest of their miserable lives...","grin","happyCl")
    #call her_main("And the perfect place to house all those dirty \'slytherins\'!","angry","angry")

    menu:
        m "(...)"
        "\"just find her...\"":
            call her_main("Very well, Sir...","soft","baseL")

        "\"No one's getting sent to Azkaban...\"":
            m "By the gods, [hermione_name], what's wrong with you?"
            call her_main("What are you talking about, [genie_name]?","open","baseL",cheeks="blush")
            call her_main("Everyone knows that life in Azkaban is the punishment for casting an unforgivable curse...","open","closed")
            m "I've been given special permission to punish them as I see fit."
            call her_main("Oh...","annoyed","base")
            call her_main("So no Azkaban?","soft","baseL")
            m "Not unless they've killed someone..."
            call her_main("Really? So there's still a chance?","base","glance")
            m "Only if you find a body..."
            call her_main("yay!","smile","happyCl")

    call her_main("Consider it done, [genie_name]!","open","closed")

    call her_walk(action="leave", speed=2)

    call bld
    if astoria_intro.E2_snape:
        m "I wonder if she'll find her before Snape..."
    else:
        m "I should probably go tell Snape as well..."

    $ hermione_busy = True
    $ astoria_intro.E2_hermione = True

    jump main_room


### Event 2 - Snape ###
# You ask Snape to find the student.

label astoria_intro_E2_snape:
    m "Tonks came by earlier and informed me about one of your students causing trouble."
    call sna_main("Really?","snape_03") #No xpos change.
    call sna_main("Why are you telling me?","snape_04")
    m "Apparently somebody got hit by something called an \"unforgivable\" curse at the school..."
    call play_sound("scratch")
    call sna_main("","snape_11")
    with hpunch
    pause.2

    call sna_main("Shit... this isn't good...","snape_08")
    m "She worries that the ministry might find out about it if we don't do anything."
    call sna_main("This really isn't good...","snape_07")
    call sna_main("If they send an auror here they might find out what we've been doing!","snape_10")

    m "Didn't they already do that?"
    call sna_main("We've got lucky with Tonks, but if they were to send another Auror investigating the curses.","snape_03")
    call sna_main("They might get wind of all the favour trading that we've been doing as well.","snape_10")
    call sna_main("Fucking our students isn't something teachers are supposed to do genie!","snape_25")
    sna "We can't risk receiving any more attention on the matter."
    call sna_main("If an auror finds out what's going on here we're both going to Azkaban!","snape_16")
    m "so what are we going to do?"
    call sna_main("We'll just have to make sure that no more curses are cast...","snape_01")
    m "How do we manage that?"
    call sna_main("We have to find out who's been casting them.","snape_24")
    call sna_main("Normally the real Dumbledore would be able to detect who had cast them, but seeing as how you're here instead...","snape_06")
    call sna_main("We'll have to find them the old-fashioned way.","snape_10")
    m "So you want me to launch a manhunt?"
    call sna_main("Are you crazy? We can't let anyone know what's happened. All the students will panic thinking someone's been murdered...","snape_16")
    call sna_main("It's probably just an imperio or crucio that's been cast.","snape_24")
    call sna_main("I'll start the search immediately. In the meantime, just stay here and keep yourself busy.","snape_10")
    m "You don't want my help?"
    call sna_main("Not really... me and Tonks should be able to find that student in no time.","snape_02")
    if astoria_intro.E2_hermione:
        m "And Granger..."
        call sna_main("Have you told her about this?!","snape_03")
        m "Sure... She seemed eager to help."
        call sna_main("Of course she did...","snape_06")
        call sna_main("(You bloody fool...)","snape_35")

    call sna_main("Don't worry, I'll find that student in no time. You shall see...","snape_02")

    call sna_walk(action="leave", speed=2)

    call bld
    m "What a drama queen..."

    $ snape_busy = True
    $ astoria_intro.E2_snape = True

    jump main_room


### Event 3 ###
# Hermione brings Astoria to you.
# Snape scolds her and Tonks gives her detention.

label astoria_intro_E3:
    stop music fadeout 1.0
    call play_sound("knocking")
    call bld
    "*knock* *knock* *knock*"
    m "(...)"

    call play_sound("knocking")
    "*knock* *knock* *knock*"

    menu:
        m "..."
        "\"What?\"":
            pass
        "\"Not now...\"":
            pass

    with hpunch
    who "Stop pulling me!"
    her "Shut it already!"
    who "Why did you drag me here?"
    her "You know very well why I brought you!"
    who "Let me go you filthy mudbl-"
    call play_sound("thump")

    m "Who's there?"
    her "*Shhhhh*- now!"
    m "..."
    her "It's Hermione Granger, Sir."
    her "Although... I'm not alone."
    m "Come in."

    call her_walk(action="enter", xpos="desk", ypos="base", speed=2.7)

    call her_main("Hello sir.","normal","happy", xpos="mid", ypos="base")
    m "I thought you said you weren't alone?"
    call her_main("I'm not.","annoyed","glanceL")
    hide screen hermione_main
    hide screen bld1
    with d3
    pause.2

    call her_chibi("stand","desk",flip=True)
    pause.5

    call her_main("Get in here, Astoria!","annoyed","angryL", ypos="head", flip=True)
    ast "{size=+2}{b}No!{/b}{/size}"
    call her_main("Do you want to make this worse?","scream","closed", trans="hpunch")
    ast "no..."
    hide screen bld1
    with d3
    pause.1

    call her_chibi("stand","desk","base", flip=False)
    pause.2

    call play_sound("door")
    call ast_chibi("stand","door","base")
    with d3
    pause.8

    # Astoria enters.
    call ast_walk("mid","base", speed=2.5)

    call her_main("","base","base", xpos="base", ypos="base", flip=False)
    call ast_main("...","annoyed","base","worried", "R", xpos="mid", ypos="base")

    m "..."
    m "And who's this?"
    call her_main("Astoria Greengrass, Sir.","base","base", xpos="right", ypos="base")
    call her_main("You asked me to bring you the person who cast the unforgivable curse, Sir.","soft","annoyed",xpos="close",ypos="base")
    call her_main("And here she is.","grin","angry")
    m "I thought it would be some angsty teen who listens to death metal - or something..."
    m "Not some little girl..."
    call ast_main("I am not a little girl!","clench","narrow","angry","mid")
    call ast_main("You're just ancient!", "annoyed","narrow","angry","R")
    m "(Oh, you have no idea...)"

    call her_main("What's going to be her punishment, Sir?","grin","angry")
    call ast_main("Punishment? I didn't do anything!", "annoyed", "wide","wide", "wide")
    call her_main("You know very well what you did!","angry","angryCl")
    call her_main("Sir, I overheard her boasting about it in the library - to a group of \"Slytherins.\"","annoyed","concerned")
    call her_main("By the sounds of it, she used Imperio to control another student!","annoyed","base")
    call ast_main("I did not!","annoyed", "base","worried","L")

    call her_main("Shall I go fetch a vial of veritaserum from Professor Snape, sir?","grin","base")
    call ast_main("V-veritaserum?!","clench","base","worried","mid")
    call ast_main("That's illegal!","clench","base","base","mid")
    call her_main("Not when you've been casting unforgivable curses - you evil little witch!","grin","angry")
    call ast_main("Fine!", "clench", "closed","angry", "mid")
    call ast_main("I'll tell you what happened sir...", "open", "narrow","base", "mid")
    call ast_main("But only if this Gryffindor leaves!", "annoyed", "narrow","base", "mid")
    call her_main("Not a chance!","scream","angryCl")

    $ d_flag_01 = False

    menu:
        m "(...)"
        "You're dismissed, Miss Granger!":
            her "What?!"
            pass

        "Go and fetch Snape!":
            $ d_flag_01 = True
            pass

    her "But Sir, I'd really like to know what her punishment is going to be!"
    m "That is of no concern to you."
    #m "That's none of your concern." - either one works, pick your favourite
    her "Yes it is! And I demand to be rewarded!"
    her "Given that I was the one who caught her, I think it's only fair!"

    m "(...)"
    menu:
        "\"Not now, Miss Granger...\"":
            m "We'll talk about your reward later..."
            her "But!"
            m "No butts..." #is this deliberate?
            call her_main("*hmph*","annoyed","angryL")
            call her_main("Fine...","open","angryCl")
            $ her_mood += 12

        "\"How about some house points instead?\"":
            her "*Hmm*..."
            her "How many house points?"

            menu:
                m "(...)"
                "\"How about 10?\"":
                    her "..."
                    her "I expected more for this, Professor!"
                    m "Take 'em or leave 'em..."
                    her "Very well..."
                    $ her_mood += 6
                    $ gryffindor += 10

                "\"You'll get 20.\"":
                    her "..."
                    her "I suppose that's fair."
                    $ her_mood = 0
                    $ gryffindor += 20

    her "In a few days, everyone at Hogwarts will know what happened to her..."
    her "When she's sent to Azkaban!"
    m "Nobody's going anywhere, except for you, Miss Granger..."

    if d_flag_01:
        m "Now go and fetch Snape for me."
    else:
        m "You may leave..."

    her "..."
    ast "*cough*... mudblood..." # Small text
    her "*Tzzzs!*..."
    call her_main("I'll go back to class then...","annoyed","angryL")
    her "Good day, Professor."

    call her_walk(action="leave", speed=2.5)

    ast "..."
    m "..."

    if d_flag_01:
        ast "Sir, weren't you going to summon Professor Snape?"
        m "Oh, that's right!"
        m "Give me a second..."
        ast "..."
        ast "(Better him than any of the other teachers...)"

    call sna_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call play_music("snape_theme")
    call sna_main("You wanted to see me?","snape_03",xpos="base",ypos="base")
    call ast_main("...", "annoyed", "base","worried", "R")
    call sna_main("Astoria?!","snape_09")
    call sna_main("Why is one of my students in your office? Don't tell me you...","snape_09")
    m "It's not that sort of visit."
    call sna_main("Really? Then what's she doing here?","snape_05")
    m "She's the one who's been casting those curses."
    call sna_main("Truthfully? A Slytherin?","snape_05")
    call sna_main("I expect better than this from my students, Miss Greengrass...","snape_10")

    call sna_main("The very first lesson I give you is don't-","snape_08")
    call sna_main("get-","snape_08",trans="hpunch")
    call sna_main("caught!","snape_15",trans="hpunch")
    pause.5

    call sna_main("Do you have anything to say for yourself?","snape_10")
    call ast_main("I-I'm sorry, sir... It won't happen again.", "upset","closed","base","mid")
    call sna_main("Who did you cast them on, you little idiot?","snape_30")
    ast "Susan Bones, Sir..."
    sna "The \"Hufflepuff\" cow-"
    sna "*Ahem*..."
    m "..."
    sna "That cowardly \"Hufflepuff\" girl?"
    ast "Yes."
    call ast_main("I... might have used Imperio to embarrass her a little...","smile","narrow","worried","mid")
    call sna_main("Well as long as you only cast it once...","snape_09")
    sna "We have to make sure this stays under wraps."
    sna "Miss Greengrass, you will not mention this incident to any other student or teacher, am I clear?"
    ast "Yes Sir, I promise..."
    sna "You should count yourself lucky the ministry hasn't been notified..."
    sna "Miss Tonks has been kind enough to wipe the c...{w=0.3} Susan's memory of the event."
    sna "You owe her big time...."
    ast "Of course..."
    sna "I'll leave her punishment to the two of you..."
    sna "I have someone-..."
    sna "*Uhm*... I've got an appointment to attend to in my office."
    m "Naturally..."
    sna "Until next time... Albus."
    m "And Albus to you t..."
    g4 "I mean..."
    g9 "Until next time!"
    sna "..."
    m "..."

    # Snape leaves and runs into Tonks.
    call sna_walk("door","base", speed=2.8)

    call play_sound("door")
    call ton_chibi("stand","door","base")
    with d3
    pause.5

    ton "Snape. How good to see you!"
    sna "Save your compliments for someone else... I'm in a bit of a hurry."
    ton "Still mad at me for taking your post?"
    ton "I'd be willing to compensate you for it, you know..."
    sna "..." # Blush

    menu: #what's the point of having a menu here, it doesn't change anything
        m "..."
        "-Cough-":
            m "*Ahem*..."
        "-...-":
            pass

    sna "Would you mind?"
    ton "Sure...{image=textheart}"
    sna "Stepping aside."
    ton "Oh, okay..."

    call play_sound("door")
    hide screen bld1
    call sna_chibi("hide")
    with d3
    pause.5

    call ton_walk("desk","base", speed=2.8)
    pause.2

    ton "Hello, Professor."
    ton "Astoria? What are you doing here?" # horny
    ton "You didn't cause any mischief, I hope."
    ast "Of course not."
    call ton_main("Wait, is she the one who's cursed Susan?","open","base","raised","L")
    m "Yep."
    ast "..."
    call ton_main("(Oh shit!)","open","base","raised","L")

    call ast_main("I'm really sorry! I promise I won't ever cast it again!","clench","closed","worried","mid")
    call ton_main("Really? It was you who cast the spell?","open","base","worried","L")
    m "..."
    call ton_main("It couldn't possibly have been someone as cute as you!","open","base","wide","L")
    ast "..." # Embarrassed, stares down.
    call ast_main("Please don't send me to Azkaban!","scream","wide","wide","wide")
    call ton_main("Don't worry, It won't come to that...","base","base","base","L")
    call ton_main("The ministry isn't going to lock away such a cute little thing like yourself...","open","base","base","mid")
    call ton_main("{size=+2}Over a little harmless fun.{/size} {image=textheart}","horny","base","wide","L")

    call ton_main("It's just the Imperius curse.","open","base","worried","R")
    call ton_main("Most students don't have the guts to cast crucio on another person...","open","base","worried","mid")
    call ton_main("Let alone Avada Kedavra...","open","wide","wide","wide")

    m "..."
    call ton_main("So, you had some fun with Susan, I gather?","base","base","raised","L")
    call ton_main("Want to tell me what you made her do?","base","base","base","L")
    m "(Doesn't she already know that?)"
    call ast_main("I might have made her show her boobs to some second years...","upset","wink","base","mid")
    call ton_main("*ha-ha-ha-ha!*","base","base","wide","L")
    call ast_main("Just for a second!", "annoyed", "base","worried", "R")
    m "(what's going on here?)"
    call ton_main("Is that all?","base","base","wide","L")
    call ton_main("You probably did Susan some good then...","base","base","wide","L")
    call ton_main("She sure needs to loosen up a bit.","base","base","wide","L")

    call ton_main("She always has been very sensitive about her body for some reason.","base","base","raised","mid")
    call ast_main("So I'm not going to get in trouble?","upset","base","base","mid")
    call ton_main("I didn't say that... You still cast a very serious spell...","open","base","base","L")
    ton "A couple of hours of detention with me should be a sufficient enough punishment for casting an unforgivable curse."
    ton "Wouldn't you agree, Professor?"

    $ d_flag_01 = False

    menu:
        m "(...)"
        "\"Seems reasonable to me.\"":
            ast "Really? Only detention?"
            ton "I'm very much looking forward to it."
            ast "Wicked!"

        "\"Why don't you just reward her at this point...\"":
            $ d_flag_01 = True

            ast "What?"
            ton "*Hmm*... I agree."
            m "Miss Tonks, I was being sarcastic..."
            ton "But you're right though, Professor!"
            ton "Casting the Imperius curse at her age is no easy task!"
            ton "A girl with that type of...{w=0.3} talent, is a rare thing." # Horny
            ton "I would say, 50 points for \"Slytherin\" should be appropriate."
            ast "!!!"
            g4 "(If Hermione hears about this - she'll Abra Kadabra my head off!)"
            g4 "(And not the one on my shoulders...)"
            ton "But you'll still have to visit me for detention."
            ast "I guess I can do that..."
            ton "Wonderful."
            $ slytherin += 50

    ton "That should be all for now, Astoria."
    ast "..."
    ton "Have a good night, cutie."
    ast "*Uhm*...{w=0.3} Good night then."

    # Astoria leaves.

    call ton_main("She's {size=+5}so cute!{/size} Isn't she? {image=textheart}","base","base","wide","mid")

    if d_flag_01:
        m "You gave her 50 house points..."
        g4 "For what you previously described as a serious crime?"
        ton "I know! I shouldn't have rewarded her, but..."
        ton "Did you see how her face lit up!" # Horny
        ton "I thought we were supposed to encourage our students, [ton_genie_name]."
        m "Don't put this one me..."
        ton "Fine, maybe I got a bit too excited..."

    else:
        m "A couple of hours of detention..."
        m "For what you previously described as a serious crime?"
        ton "Did I go too soft on her?"
        #m "Oh, don't you think I suddenly started to care about this school."
        m "Oh, don't get me wrong. I couldn't care less about this school."
        m "I'm not even supposed to be here..."
        ton "Fair enough..."

    m "We should have a chat about Astoria again..."
    m "Discuss the severity of her... \"detention.\""
    ton "Of course, [ton_genie_name]."
    ton "I'm glad we're on the same page...{image=textheart}"
    m "Until next time, [tonks_name]."
    ton "Bye.{image=textheart}"

    call bld
    m "(...)"
    m "(I feel like I'm actually starting to run this damn school.)"
    m "(This isn't what I signed up for...)"

    $ astoria_busy = True
    $ hermione_busy = True
    $ snape_busy = True
    $ tonks_busy = True

    $ astoria_intro.E3_complete = True

    jump main_room


### Tonks Hangout Event 1 ###
# Tonks wantes to teach Astoria the Imperius curse.

label nt_he_astoria_E1:
    ton "So about this girl."
    m "You're going to have to be more specific."
    ton "Astoria Greengrass."
    m "Ah yes, the hot-headed one."
    ton "Yes, she's pretty cute isn't she..."
    ton "I wouldn't mind giving her a thorough robe inspection if you know what I'm saying."
    ton "This girl...{w} she's special...{w} different..."
    m "You got the hots for this girl?"
    ton "She's a Slytherin!"
    m "People keep saying that as if I'd know what the problem is."
    ton "Oh yes... I guess I'm a teacher now so I should be more impartial..."
    ton "Old habits I suppose."
    ton "But no, it's not that."
    ton "This girl is cursed... and it's quite a problem."
    m "Don't you mean this cursed girl {i}is{/i} a problem?"
    ton "No, she's cursed. Quite a hefty curse at that!"
    m "..."
    ton "Her family - the Greengrass family - is quite infamous in the wizarding world."
    ton "They're known for being a very high class family of witches and wizards..."
    ton "Some of them are very stuck-up and spoiled, for that reason."
    ton "It's quite the norm for most pure blood families, actually."
    m "Get to the point..."
    ton "*Sigh*"
    ton "One of Astoria's ancestors was put under a blood curse - and I fear that parts of this curse has trickled down the generations - and surfaced in Astoria."
    m "And what did this accursed curse do exactly?"
    ton "Originally, its purpose was to bring down the family, and make them appear weak in the eyes of the wizarding community."
    ton "Every now and then one of the family members would become frail and live a short life."
    m "Oh shit..."
    ton "Yeah..."
    m "Hey, at least it's not the other way round, am I right..."
    m "Immortality can be quite the curse too you know..."
    ton "Yes, I can see how much you're hurting inside..."
    ton "The opportunity to have sex with some of the most attractive women in all of history must really suck."
    m "I'll live with it..."
    ton "Fortunately, this curse has faded after many generations, but in turn appears to have evolved into something else..."
    m "How would you know?"
    ton "I'm an auror..."
    m "Is that your answer for everything now?"
    ton "Just trust me..."
    ton "The nature of it is quite familiar to me."
    ton "I have strong reasons to believe that this girl is..."
    ton "She's..."
    m "She's what?"
    ton "She's asexual!"
    m "..."
    ton "You don't believe me?"
    m "Oh no, I do believe you."
    m "..."
    m "Mind explaining to me what asexual's supposed to mean?"
    ton "You don't know?"
    ton "Well that's not too surprising - all things considered..."
    ton "It means she feels no sexual feeling or attraction, to anything!"
    g4 "WHAT?!"
    ton "I know!"
    m "By the great desert sands... That's a curse worse than death."
    m "I thought the effect was supposed to have got weaker?"
    ton "The curse has seemingly gone from killing off random members of their family, to preventing new members from being born."
    m "That doesn't make any sense..."
    m "But since when has magic made any fucking sense in this universe..."
    ton "Hey, it makes perfect sense!"
    ton "..."
    ton "In any case, I'd like to keep an eye on her - if you don't mind."
    m "Go right ahea-{w=0.8}{nw}"
    ton "Maybe even teach her how to cast Imperio properly."
    m "..."
    g4 "Hold on a second...{w=0.8} what?!"
    g4 "You want to teach this {b}sadist{/b} how to cast those illegal curses?"
    m "That's what got us in all this trouble in the first place!"
    ton "Don't worry, I'm just gonna teach her the basics..."
    ton "She won't go out and curse students at random anymore... I won't allow that."
    ton "But... Maybe this can help ignite that \"sexual urge\" - deep inside of her..."
    ton "She clearly isn't ready to do it with some boy..."
    ton "Or you, for that matter."
    m "If she's really cursed with \"Asexuality\" - then I don't want to have her anywhere close to me."
    ton "It's not contagious, you numpty!"
    ton "Have you not been paying attention? It's a family curse!"
    m "..."
    ton "That being said, I'd rather have her do it with me..."
    m "Are we still talking about the curse thingy?"
    ton "Yes..."
    m "So your goal is to somehow awaken her sexuality, and get rid of this curse?"
    ton "It might not be that easy, but I think it would be a good start."
    ton "I must at least know if my theory is correct..."
    m "I don't see how this Imperio thing plays into it, but if you say so..."
    #m "But hold on... won't the ministry be down our necks again if an illegal curse is repeatedly cast at Hogwash?"
    #ton "No, the ministry doesn't track magic inside the school walls illegal or not, curses are no different."
    #ton "They rely on these things being reported by the school administration... or lately... by yours truly."
    #ton "And to be frank... This place could blow up and I wouldn't care enough to report it to those assholes anymore."
    #m "I hope that's not part of your plan..."
    #ton "Not unless it's a pleasure explosion."
    ton "I'll speak to Miss Greengrass."
    ton "I doubt she'll have many objections..."

    jump main_room


### Event 4 ###
# Astoria summon unlock.
# If you pick the wrong choice Astoria won't return for a week and ignores you.

label astoria_intro_E4:
    stop music fadeout 1.0
    call play_sound("knocking")
    call bld
    "*knock* *knock* *knock*"
    m "(...)"

    call play_sound("knocking")
    "*knock* *knock* *knock*"

    menu:
        m "..."
        "\"Who is it?\"":
            ast "Professor, may I come in?"
            g4 "It's that accursed, cursed girl!"
            ast "Sir?"

        "\"Not now...\"":
            ast "But, Professor Tonks told me you wanted to speak with me."
            m "She did?"
            ast "Yes."

    menu:
        m "..."
        "\"Come in.\"":
            ast "..."
            pass

        "\"I'm busy.\"":
            ast "*Uhm*..."
            ast "Very well, Sir."
            ast "I shall be back tomorrow..."
            m "..."

            $ ag_event_pause += 1
            $ astoria_busy = True

            jump main_room


    ast "Hello, Professor."
    ast "Professor Tonks told me to talk to you, Sir."
    m "....................."
    m "She did?"
    ast "Yes, Sir..."
    m "(Shit, was I supposed to do anything with her?)"
    ast "...................."
    m  "(Oh that's right. Freeing her from her curse...)"
    ast "Sir, If there is nothing you need of me, then I'd like to leave..."

    menu:
        m "..."
        "\"What about your detention?\"":
            ast "Oh..."
            m "If I recall correctly, we have yet to discuss your punishment."
            ast "So you didn't forget about that..."
            pass

        "\"You still need to be punished!\"":
            ast "Punished?!"
            ast "I thought I was only going to get detention?"
            m "Yes, detention."
            pass

        "\"Fine by me...\"":
            ast "I'll head back to the dungeons, then..."
            m "See ya."

            # Astoria leaves

            call bld
            m "I'd better not mention this to Tonks..."
            m "I'm sure she'll come back for her punishment."

            $ ag_event_pause += 7 # Returns a week later.
            $ astoria_busy = True

            jump main_room

    m "It's just a couple of hours with your teacher."
    g9 "I'm sure you'll enjoy it!"
    ast "If you say so, Sir."
    ast "..."
    ast "Would it be ok if I go there some other time?"
    m "Are you trying to weasel yourself out of your punishment?"
    ast "No?"
    ast "It's just that... I really don't have time right now..."
    m "..."
    m "I'll allow it. But just this once!"
    ast "Thank you!"
    m "You're dismissed..."
    ast "..."

    # Astoria leaves.
    call ast_walk(action="leave", speed=2.5)

    $ astoria_busy = True
    $ ag_event_pause  += 2
    $ ag_summon_pause += 2 # You can't summon Astoria for a couple of days.

    $ astoria_unlocked = True
    $ achievement.unlock("unlockast", True)
    call popup("{size=-4}You can now summon Astoria into your office.{/size}", "Character unlocked!", "interface/icons/head/head_astoria_1.png")

    jump main_room
