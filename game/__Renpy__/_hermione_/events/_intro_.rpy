

### Hermione Intro ###

label hermione_intro_E1:
    stop music fadeout 1.0
    pause 1

    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"
    m "Huh?"

    call play_sound("knocking")
    "*Knock-knock-knock*"
    pause.7

    m "Somebody is knocking on the door..."
    m "Crap... I'm supposed to avoid any human contact!"
    m "Hm... What are the chances that the thing knocking on my door is not human?"
    m "Yeah, quite slim..."

    call play_sound("knocking")
    "*Knock-knock-knock*"
    m "Persistent little bastard..."

    $ d_flag_01 = False #When False Genie doesn't know Hermione's name.

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
            who "But, professor, I really need to talk to you..."
            m "..........................................."
            who "Professor? I'm coming in!"
            m "{size=-4}(Crap...){/size}"
        "\"................\"":
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

    if d_flag_01:
        m "{size=-3}(A girl?){/size}"
    else:
        m "?!!"

    call her_walk(xpos="mid", ypos="base", speed=3)
    pause.5

    call her_main("","base","base", xpos="base", ypos="base")
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
        m "{size=-4}(Oh... That was a good jerk-off session, but I'm getting dangerously close to the \"grand finale\".){/size}"
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

    call her_walk(action="leave", speed=2)

    if masturbating:
        m "{size=-4}(This was awesome...) *Panting*{/size}"
        m "{size=-4}(My trousers are ruined though...){/size}"
    else:
        m "................."
        m "(She is cute, but quite a piece of work...)"

    hide screen genie_jerking_sperm_02
    with d3

    $ snape_busy = True # No point in calling him during the day.

    $ hermione_intro.E1_complete = True

    jump main_room


# Event 2

# Second visit from Hermione. Says she sent a letter to the Minestry.
# Takes place after first special event with Snape, where he just complains about Hermione.

label hermione_intro_E2:
    stop music fadeout 3.0
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
                    pass

                "\"Of course. Come on in.\"":
                    jump hermione_intro_E2_continue

        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well alright..."
            pass

        "\"Yes, come in.\"":
            jump hermione_intro_E2_continue

        "\"...................................\"":
            call play_sound("knocking")
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"
            jump hermione_intro_E2_continue

    # Don't let Hermione in.
    $ achievement.unlock("knock")
    $ hg_event_pause += 1
    jump main_room

    # Let Hermione in.
    label hermione_intro_E2_continue:
        pass

    call her_walk(action="enter", xpos="mid", ypos="base", speed=3)
    pause.5

    call play_music("chipper_doodle")
    call her_main("","normal","base", xpos="base", ypos="base")
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

    call her_walk(action="leave", speed=2)

    call bld
    m "...................."

    $ snape_busy = True # No point in calling him during the day.

    $ hermione_intro.E2_complete = True
    $ hg_event_pause += 1

    jump main_room



# Event 3

# Third visit, after second special date with Snape.
# Hermione complains that she almost failed a test. (EVENING EVENT!)

label hermione_intro_E3:
    stop music fadeout 1.0
    call play_sound("knocking")
    "*Knock-knock-knock!*"

    her "Professor, I'm coming in!"
    m "...."

    call play_music("chipper_doodle")

    $ hermione_wear_robe = True
    call update_her_uniform

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)
    pause.5

    call her_main("","annoyed","frown", xpos="base", ypos="base")
    call ctc

    call her_main("Good evening, Professor.","annoyed","angryL")

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
    call her_main("I'm not sure how to describe this...","normal","frown")
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
    call her_main("This is not a laughing matter, Sir.","normal","base")
    call her_main("You should consider me a \"measuring stick\" for our educational system.","open","angryCl")
    her "If I \"almost\" fail a test, the rest of the students will definitely fail it."
    m "Is that so...?"
    call her_main("Yes, professor. Something went terribly wrong today...","normal","frown")
    call her_main(".................................","annoyed","angryL")
    call her_main("But what if it didn't?","open","worried")
    her "What if all the tests will be this difficult from now on?"

    menu:
        "\"You should study more, girl!\"":
            call her_main("But I studied all night for this test!","soft","base", tears="soft")
        "\"There, there... It'll be alright.\"":
            call her_main("No it won't! This is a catastrophe!","mad","worriedCl", tears="soft_blink")

    call her_main("And the worst part is that I think I might be the only one who failed...","angry","base", tears="soft")
    call her_main("How will this make me look?","angry","base", tears="soft")
    call her_main("I will know for sure when we get the results though...","normal","baseL", tears="soft")
    call her_main("Yes, I'm sure everyone else failed as well...","soft","baseL")
    call her_main("I mean, they must have, right?","open","worried")
    call her_main(".....................","soft","baseL")
    call her_main("....right?","open","worried")

    label cant_say:
    menu:
        "{size=-3}\"Of course. You are a top student after all.\"{/size}":
            call her_main("Exactly...","annoyed","frown")
            her "Or at least I used to be until today..."
            call her_main("I cannot believe this is happening!","mad","worriedCl", tears="soft_blink")
        "{size=-3}\"You could prepare better if I were to tutor you.\"{/size}":
            $ tutoring_offer_made = True
            call her_main("hm...","annoyed","suspicious")
            call her_main("Yes, that could help I suppose...","soft","baseL")
            call her_main("I appreciate your offer, professor, but...","open","base")
            call her_main("The best tutor is a book, and I have the entire Hogwarts library at my disposal.","open","closed")
            call her_main("I don't think it would be necessary, sir. But...","soft","base")
            her "May I think about it?"
            m "Don't take too long..."
        "{size=-3}\"I suppose we'll know soon enough.\"{/size}":
            call her_main("Yes, I suppose we will...","soft","base")
        "{size=-3}\"You need to put my cock in your mouth.\"{/size}":
            m "You need to put my co-"
            call her_main("Huh?","soft","base")
            m "{size=-4}(No, I can't actually say that...){/size}"
            call her_main("......?","annoyed","suspicious")
            jump cant_say

    m "............"
    call her_main("I'm sorry, professor, I'm probably just overreacting anyway...","grin","worriedCl", emote="05")
    call her_main("But you must understand that my reputation is at stake here!","open","base")
    call her_main("There's gotta be something wrong with the test...","annoyed","angryL")
    her "And although the entire class might have failed, I probably still got the most points on the test..."
    her "As usual..."
    call her_main("Well, I'd better go now. We have another \"MRM\" meeting today.","open","angryCl")
    her "I will let you know about the new ideas we come up with."
    m "I can hardly wait..."
    call her_main("Well, if there is nothing else, I have a studying schedule to keep.","open","closed")
    m "By all means..."

    call her_walk(action="leave", speed=2)

    $ hermione_wear_robe = False
    $ snape_busy = False

    $ hermione_intro.E3_complete = True
    $ hg_event_pause += 1

    jump main_room



# Event 4

# Hermione complains that she did fail the test. (EVENING EVENT!)

label hermione_intro_E4:
    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call bld
    her "....................."
    m "???"

    call her_walk(xpos="desk", ypos="base", speed=1.6)

    call bld
    her "............"
    m "Miss Granger?"
    her "..............................."
    m "Miss Granger?!!"

    call her_main("","upset","dead", tears="mascara", xpos="right", ypos="base")
    call ctc

    her "Huh?"
    her "Oh, I'm already here?"
    her "I'm sorry, sir... I..."
    her ".................."
    her "It seems that I did..."
    her "I did... uhm..."
    her "... I failed that test after all."
    her "I..."
    call her_main("I'm sorry, professor...","upset","worriedCl", tears="mascara_soft_blink")
    her "I'm not sure why I'm here..."
    her "I think I'd better go..."
    m "..................."

    call her_walk(action="run", xpos="door", ypos="base", speed=1, loiter=False)
    call play_sound("door")
    pause.3

    call bld
    m "............."
    m "She will be alright..."
    m "I think..."

    $ hermione_intro.E4_complete = True
    $ hg_event_pause += 1

    jump day_start


# Event 5

# Hermione comes after her breakdown (when she failed the test).
# She is asking for tutoring.
# Tutoring unlocked!

label hermione_intro_E5:
    call her_walk(action="enter", xpos="desk", ypos="base", speed=2.8)

    call play_music("chipper_doodle")
    call her_main("Good morning, Professor.","base","base", xpos="right", ypos="base")
    m "(So She doesn't even bother to knock anymore?)"

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
                                call her_main("Oh, of course. I'm so silly sometimes. Sorry about the yelling, sir.","grin","worriedCl", emote="05")
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

    call her_walk(action="leave", speed=2)

    stop music fadeout 1.0

    $ hermione_unlocked = True
    $ achievement.unlock("unlockher")

    $ hermione_busy = True
    $ tutoring_hermione_unlocked = True

    $ hermione_intro.E5_complete = True #Allows next event to start.
    $ hg_event_pause += 2

    jump main_room


# Event 6

# Hermione comes and asks to buy a favour from her.

label hermione_intro_E6:
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
                    pass

                "\"Of course. Come on in.\"":
                    jump hermione_intro_E6_continue

        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well, alright..."
            pass

        "\"Yes, come in.\"":
            jump hermione_intro_E6_continue

        "\"...................................\"":
            call play_sound("knocking")
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"
            jump hermione_intro_E6_continue

    # Don't let Hermione in.
    $ achievement.unlock("knock")
    $ hg_event_pause += 1
    jump main_room

    # Let Hermione in.
    label hermione_intro_E6_continue:
        pass

    call her_walk(action="enter", xpos="mid", ypos="base", speed=3)

    call her_main("Good day, professor...","soft","baseL", xpos="base", ypos="base")
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
            call her_main("Ehm... I'm not sure...","angry","worriedCl", emote="05")
            her "The kind that would gain our house additional points..."
            call her_main("I could write an essay for you or...","open","base")
            call her_main("Or maybe clean your tower..?","angry","worriedCl", emote="05")
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

    label choose_favor_again:
    $ current_favor = ""
    her "So... What will it be?"

    menu:
        "\"Show me your tongue...\"":
            $ current_favor = "show_tongue"
        "\"Stand there. Let me look at you.\"":
            $ current_favor = "stand_there"
        "\"Make a silly face...\"":
            $ current_favor = "silly_face"
        "\"Say \"I've been a bad girl\".\"":
            $ current_favor = "bad_girl"

    her "Em..."
    her "How many house points will I get for that...?"
    $ current_payout = 0

    menu:
        "\"1 point.\"":
            if not current_favor in ["stand_there"]:
                her "I don't think it's worth it then..."
                jump choose_favor_again
            $ current_payout = 1
        "\"10 points.\"":
            if not current_favor in ["stand_there","silly_face"]:
                her "I don't think it's worth it then..."
                jump choose_favor_again
            $ current_payout = 10
        "\"20 points.\"":
            her "So little...?"
            $ current_payout = 20
        "\"40 points.\"":
            her "(Wow. That's quite a lot...)"
            $ current_payout = 40

    call her_main("Em, alright...", xpos="mid", ypos="base", trans="fade")

    if current_favor == "show_tongue":
        call her_main("M-my... tongue, sir?","grin","worriedCl", emote="05")
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

    if current_favor == "stand_there":
        call her_main("So, I just have to stand here then...?","base","base")
        m "Good... Now turn around... slowly."
        her "uhm... alright..."
        hide screen hermione_main
        hide screen bld1
        pause.5

        #show screen hermione_stand_f <- screen does not exist
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

    if current_favor == "silly_face":
        call her_main("A silly face then...","grin","worriedCl", emote="05")
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

    if current_favor == "bad_girl":
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
                m "You are overanalysing this, girl."
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
        if current_payout == 1:
            m "[current_payout] point to the \"Gryffindor\" house."
        else:
            m "[current_payout] points to the \"Gryffindor\" house."
        $ gryffindor += current_payout

    call her_main("Yay!..............","grin","worriedCl", emote="05", xpos="base", ypos="base", flip=False, trans="fade")
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

    call her_walk(xpos="door", ypos="base", speed=2)
    pause.3

    if current_favor == "show_tongue":
        call her_main("{size=-4}(Hm...){/size}","annoyed","down", ypos="head")
        call her_main("{size=-4}(Students show teachers their tongues all the time...){/size}","soft","baseL")
        call her_main("{size=-4}(Although that's usually when the teacher is not looking...){/size}","base","glanceL")
        call her_main("{size=-4}(But there is nothing wrong with what I did today...){/size}","disgust","down")
        call her_main("{size=-4}(I earned my house extra points...){/size}","smile","happyCl")

    if current_favor == "stand_there":
        call her_main("{size=-4}(I can just stand there and let the professor look at me...){/size}","annoyed","baseL", ypos="head")
        call her_main("{size=-4}(There is nothing wrong with that... nothing at all...){/size}","open","closed")

    if current_favor == "silly_face":
        call her_main("{size=-4}(Stupid face...){/size}","silly","silly", ypos="head")
        call her_main("{size=-4}(Stupid face...){/size}","silly","happy")
        call her_main("{size=-4}(I need to practice this.){/size}","base","happyCl")

    if current_favor == "bad_girl":
        call her_main("{size=-4}(I'm a bad girl...){/size}","angry","angry", ypos="head")
        call her_main("{size=-4}(I am very bad...){/size}","soft","angry")
        call her_main("{size=-4}(Yes, I can say things like that easily...){/size}","smile","happyCl")
        call her_main("{size=-4}(There is nothing wrong with that... nothing at all...){/size}","base","happyCl")

    call her_chibi("leave")

    stop music fadeout 1.0

    call popup("You unlocked the ability to buy sexual favours from Hermione.", "Congratulations!", "interface/icons/head/head_hermione_2.png")

    $ hermione_favors = True
    $ hermione_busy = True

    $ hermione_intro.E6_complete = True
    $ hg_event_pause += 1

    jump main_room
