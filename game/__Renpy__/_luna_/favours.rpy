###FAVOURS###------------------------------------------------------

label luna_favour_1: ###TALK TO ME
    m "{size=-4}(All I'll do is have a nice little conversation with her...){/size}"
    if luna_corruption == 0: #FIRST TIME
            $ luna_corruption += 1
            call play_music("chipper_doodle")
            m "Ok then..."
            m "Tell me a little about yourself, [luna_name]."
            call luna_main("*hmph* I assume you'll be paying me for this [l_genie_name].", "angry", "default", "angry", "upset")
            menu:
                "-5 gold-":
                    m "How does five gold sound [luna_name]?"
                    call luna_main("five gold! Who do you think I am!", "mad", "default", "angry", "pout")
                    m "A student with no source of income."
                    call luna_main("I am luna lovegood! You should be paying a hundred gold just to look at me!", "doubtful", "right", "mad", "angry")
                    m "How does ten gold sound then?"
                    call luna_main("Perhaps if you'd offered that to being with...", "angry", "default", "angry", "upset")
                    call luna_main("But now I'm far too upset to hold a conversation for such a low amount.", "angry", "right", "angry", "pout")
                    m "would twenty gold calm you down?"
                    call luna_main("well, I suppose it would.", "closed", "down", "default", "default")
                    $ current_payout = 20
                    m "Good, well now that we've got that sorted out..."
                "-10 gold-":
                    m "Will ten gold be enough for a conversation with your headmaster?"
                    call luna_main("I suppose so...", "doubtful", "default", "default", "upset")
                    call luna_main("Just don't try anything funny.", "angry", "right", "angry", "angry")
                    $ current_payout = 10
                    m "Scouts honor. Now..."
                "-50 gold-":
                    $ current_payout = 50
                    m "How does fifty gold sound [luna_name]?"
                    call luna_main("{size=+10}(FIFTY GOLD!){/size}", "wide", "default", "default", "open_wide_tongue")
                    call luna_main("*Hmph* I suppose that's a fair amount.", "closed_happy", "down", "default", "default")
                    call luna_main("Just don't think it buys you anything other than a conversation.", "angry", "default", "angry", "upset")
                    m "Of course not. Speaking of which..."
            call luna_main("Fine, fine, I'll start...", "closed", "down", "default", "upset")
            call luna_main("My school life so far has been painfully dull.", "default", "default", "angry", "angry")
            call luna_main("I've been under appreciated by everyone in this damn place.", "default", "right", "angry", "upset")
            call luna_main("No one seems to take me seriously...", "angry", "down", "angry", "upset")
            menu:
                "-Jerk off while she is talking-": # offended and stops unless you paid her 50 or offer to pay her more
                    hide screen luna
                    hide screen blktone
                    with d3
                    ">You reach under the desk and grab your cock..."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    pause
                    call luna_main("what are you doing [l_genie_name]!?", "doubtful", "default", "raised", "angry")
                    m "What, oh it's nothing. Simply adjusting my robe, that's all."
                    if current_payout < 50:
                        call luna_main("This is exactly what I mean!", "mad", "default", "mad", "angry")
                        call luna_main("Even the headmaster of this damn school thinks he can get away with touching himself in front of me for only [current_payout] gold!", "mad", "right", "mad", "angry")
                        show screen genie
                        with d3
                        "You quickly tuck your cock back into your robe."
                        m "i can assure you I was doing no such thing!"
                        call luna_main("whatever... I'm leaving", "mad", "right", "mad", "angry")
                        m "What! Already?"
                        call luna_main("Would you rather I stay and call the ministry of magic [l_genie_name]?", "mad", "default", "mad", "angry")
                        m "Fair enough."
                        call luna_main("I mean if you're going to try this on you could at least offer a little more than [current_payout] gold...", "doubtful", "default", "angry", "pout")
                        jump luna_away
                    call luna_main("...", "doubtful", "right", "default", "upset")
                    call luna_main("{size=-5}(Well I suppose he did offer fifty gold...){/size}", "doubtful", "right", "default", "default")
                    call luna_main("As I was saying, no one seems to even notice me.", "angry", "default", "angry", "upset")
                    call luna_main("The teachers are too busy playing favourites with the \"gryffindor\" and \"slytherin\" students.", "angry", "right", "angry", "pout")
                    call luna_main("The girls are all self obsessesed.", "angry", "down", "angry", "angry")
                    m "You don't say."
                    call luna_main("and The boys are off chasing anything that shows a little skin...", "mad", "right", "angry", "angry")
                    m "well, maybe you should fight fire with fire."
                    call luna_main("what!? and parade myself around like some tart?", "wide", "right", "angry", "furious")
                    m "{size=-4}(Yes... a nasty, little tart!){/size}"
                    call luna_main("I bet you'd enjoy that wouldn't you [l_genie_name]...", "seductive", "default", "angry", "default")
                    m "{size=-4}(Yes...){/size}"
                    call luna_main("another one of your precious students, dressing like a slut.", "seductive", "right", "default", "default")
                    m "{size=-2}(Yes......){/size}"
                    call luna_main("showing off her body for anyone that will look.", "tired", "right", "angry", "smile_large")
                    m "{size=+2}(Yes.........){/size}"
                    call luna_main("You probably want me to act like those \"slytherin\" sluts too...", "doubtful", "default", "angry", "default")
                    m "{size=+4}(Yes! Yes!){/size}"
                    call luna_main("willing to show it all for a few points...", "doubtful", "default", "angry", "grin")
                    g4 "{size=+4}(almost there...){/size}"
                    call luna_main("is that what you want [l_genie_name]? a nice little slytherin slut?", "doubtful", "default", "angry", "default")
                    g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                    hide screen luna
                    with d3
                    show screen white
                    pause.1
                    hide screen white
                    pause.2
                    show screen white
                    pause .1
                    hide screen white
                    with hpunch
                    g4 "Argh! YES!"
                    hide screen luna
                    with d3
                    hide screen bld1
                    with d3
                    show screen genie_jerking_sperm
                    with d3
                    show screen bld1
                    with d3
                    call luna_main("That's it, [l_genie_name], just let it all out...", "seductive", "default", "default", "default")
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "What? No, I was just... ah, shit, this feels good..."
                    show screen genie
                    hide screen bld1
                    #show screen genie_jerking_off
                    with d3
                    call luna_main("You couldn't help yourself could you?", "seductive", "right", "raised", "default")
                    m "ah... I guess not."
                    call luna_main("Well, I expect a bonus.", "closed_happy", "right", "raised", "upset")
                    m "I'm already paying you fifty gold!"
                    call luna_main("That was just for the conversation. If you expect me to stand here and watch you cum all over yourself, that costs extra.", "mad", "right", "mad", "angry")
                    m "Fine, I'll make it 70 gold."
                    $ current_payout = 70
                    call luna_main("Well I'm glad someone appreciates me.", "seductive", "right", "raised", "default")
                    call luna_main("(Even if it is a filthy old pervert...)", "closed", "right", "raised", "upset")
                "-Participate in the conversation-":
                    m "I can't see why..."
                    call luna_main("Even my father doesn't treat me like he should.", "angry", "right", "angry", "upset")
                    m "And how is that?"
                    call luna_main("Like the princess I am!", "seductive", "default", "default", "pout")
                    m "(Not this again...)"
                    call luna_main("As it is he's barely selling any copies of his newspaper.", "mad", "right", "mad", "angry")
                    call luna_main("It's ridiculous! I should be showered in gifts and gold...", "doubtful", "right", "mad", "upset")
            call luna_main("Speaking of which...", "seductive", "default", "angry", "upset")
            m "Alright, alright. Here's your gold."
            $ gold -= current_payout
            $ luna_gold += current_payout
            ">You hand Luna [current_payout] gold."
            call luna_main("Thank you, [l_genie_name].", "seductive", "right", "default", "default")
            ">Luna leaves your office."



    elif luna_corruption == 1: #SECOND TIME
        if luna_corruption <= 1:
            $ luna_corruption += 1
        call play_music("chipper_doodle")
        m "Alright then..."
        m "How's school going, [luna_name]."
        call luna_main("aren't we going to discuss how much you'll be paying me first, [l_genie_name].", "angry", "default", "angry", "upset")
        menu:
            "-10 gold-": #just conversation (very short)
                $ current_payout = 10
                m "How does 10 gold sound?"
                call luna_main("*Hmph* Fine...", "closed", "down", "default", "upset")
                m "so about your school life..."
                call luna_main("School is boring. All I do is go to classes.", "default", "default", "angry", "angry")
                call luna_main("Can I leave now?", "default", "right", "angry", "upset")
                g9 "What? That was barely a sentence!"
                call luna_main("And ten gold is barely a payment!", "default", "right", "angry", "upset")
                m "I'd say it's a fair payment for a little bit of idle chit chat."
                call luna_main("That's what you got. If you want more, pay more...", "default", "default", "mad", "upset")
            "-20 gold-": #Slightly flirty, still short
                $ current_payout = 20
                m "Will twenty gold be enough for you, [luna_name]?"
                call luna_main("I suppose so...", "doubtful", "default", "default", "upset")
                call luna_main("Just don't expect to get to touch yourself...", "angry", "right", "angry", "angry")
                m "How much would that cost?"
                call luna_main("...{p}More than twenty gold...", "angry", "right", "angry", "angry")
                m "Well I might take you up on that at a later date, For now tell me about school."
                call luna_main("School is boring...", "default", "default", "angry", "angry")
                m "..."
                call luna_main("but there are a few interesting things happening... ", "seductive", "default", "raised", "default")
                m "go on..."
                call luna_main("Well there are some rumours about Peeves the ghost...", "seductive", "right", "raised", "default")
                m "What sort?"
                call luna_main("Well I've heard that he's been touching some of the girls...", "seductive", "default", "sad", "upset")
                m "How haven't I heard a complaint?"
                call luna_main("Well from what I hear... the girls don't have any complaints afterwards...", "seductive", "default", "raised", "default")
                m "Ah... Anything else?"
                call luna_main("Hmmm... nothing comes to mind.", "doubtful", "down", "angry", "upset")
                m "fair enough, well I think that was worth your twenty gold."
            "-100 gold-": #JOI
                $ current_payout = 100
                m "How about one hundred gold?"
                call luna_main("Fine...", "seductive", "right", "angry", "upset")
                call luna_main("...", "doubtful", "default", "angry", "upset")
                call luna_main("......", "doubtful", "default", "raised", "angry")
                call luna_main("Well are you going to start?", "mad", "right", "mad", "angry")
                m "Start what? You're the one who's supposed to be talking."
                call luna_main("Oh please... You expect me to believe you're willing to pay your students 100 gold just to talk?", "angry", "default", "raised", "angry")
                m "Well I suppose that-"
                call luna_main("Just start stroking your cock already [l_genie_name].", "seductive", "default", "default", "upset")
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                call luna_main("Isn't that better?", "seductive", "default", "raised", "default")
                m "..."
                call luna_main("So do you pay anyone else to watch you sit there and jerk your filthy old cock?", "seductive", "default", "angry", "angry")
                m "{size=-4}(I guess I don't really pay hermione...){/size}"
                m "ah... no..."
                call luna_main("good...", "seductive", "right", "default", "default")
                m "Good?"
                call luna_main("Well... we can't have you wasting your money on any of those other little tarts can we?", "mad", "default", "mad", "angry")
                menu:
                    "-Play along-": #act submissive
                        $ luna_dom += 1
                        $ current_payout = 150
                        m "ah... of course not..."
                        call luna_main("That's right... why bother with them when I'm here to talk with you...", "mad", "default", "mad", "default")
                        m "{size=-4}(Yes...){/size}"
                        call luna_main("That's it, keep stroking it for me [l_genie_name].", "doubtful", "default", "angry", "upset")
                        m "{size=-4}(Yes... yes...){/size}"
                        call luna_main("It's probably I good thing that I watch you drain your balls.", "doubtful", "right", "angry", "upset")
                        call luna_main("Otherwise, who knows who you might call up here to watch you do it...", "angry", "default", "angry", "pout")
                        m "{size=-4}(mmmm... yes...){/size}"
                        call luna_main("You'd probably even do it in front of a first year, wouldn't you?", "doubtful", "default", "angry", "default")
                        ">You stop stroking your cock."
                        m "I'd never do any-"
                        call luna_main("Do you even know how old I am?", "doubtful", "default", "raised", "default")
                        m "of course..."
                        call luna_main("*Hmph* Are you sure about that?", "angry", "default", "raised", "talk")
                        m "..."
                        call luna_main("Back to stroking it [l_genie_name]...", "doubtful", "default", "mad", "default")
                        ">You start stroking your cock again."
                        call luna_main("Doesn't that feel better?", "doubtful", "right", "mad", "default")
                        m "{size=-4}(argh... yes...){/size}"
                        call luna_main("Say it outloud.", "mad", "default", "mad", "default")
                        m "{size=-4}yes...{/size}"
                        call luna_main("Good. Now cum for me.", "doubtful", "default", "angry", "default")
                        m "{size=-2}(What?){/size}"
                        call luna_main("come on...", "doubtful", "default", "sad", "default")
                        g4 "{size=+4}(agh... almost there...){/size}"
                        call luna_main("come for your little girl...", "angry", "default", "mad", "talk")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        hide screen luna
                        with d3
                        show screen white
                        pause.1
                        hide screen white
                        pause.2
                        show screen white
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen luna
                        with d3
                        hide screen bld1
                        with d3
                        show screen genie_jerking_sperm
                        with d3
                        show screen bld1
                        with d3
                        call luna_main("That's it, [l_genie_name] just like that...", "seductive", "default", "default", "default")
                        show screen genie_jerking_sperm_02
                        with d3
                        g4 "What? No, I was thinking about... ah, shit, this feels too good..."
                        show screen genie
                        hide screen bld1
                        #show screen genie_jerking_off
                        with d3
                        call luna_main("Your a nasty old man, aren't you.", "seductive", "right", "raised", "default")
                        m "ah..."
                        call luna_main("Don't worry, I won't tell anyone...", "seductive", "default", "raised", "default")
                        m "Thank you..."
                        call luna_main("I expect to be fairly compensated however...", "angry", "right", "angry", "default")
                        m "Don't worry, I'll add an extra 50 gold to your payment."
                        call luna_main("That's the least you could do [l_genie_name]...", "doubtful", "right", "raised", "default")



                    "-Let her know her place-": #note that he could get more for less from those tarts
                        $ luna_sub += 1
                        m "well now that you mention it I'm sure those tarts would probably charge a lot less for a conversation..."
                        call luna_main("*Hmph* You get what you pay for...", "angry", "right", "mad", "angry")
                        m "And what exactly am I getting from you for my payment?"
                        call luna_main("Getting to Look at me while you stroke your filthy old cock should be payment enough.", "angry", "default", "mad", "upset")
                        m "Well you'll have to excuse my old eyes because I can barely see you..."
                        menu:
                            "-Ask her to open her top-":
                                $ luna_sub += 1
                                m "Perhaps you should undo a button or two so I can get a better look."
                                call luna_main("Are you serious? You expect me to flaunt myself like some cheap tart?", "mad", "default", "angry", "upset")
                                m "No, I expect you to flaunt yourself like the princess you claim to be..."
                                call luna_main("...", "angry", "right", "angry", "upset")
                                m "I'm waiting..."
                                call luna_main("... {size=-8}(fine...){/size}", "doubtful", "down", "sad", "angry")
                                ">Luna removes her tie and opens her top slightly..."
                                hide screen luna
                                with d3
                                $ luna_top_level = 2
                                call luna_main("...", "doubtful", "down", "sad", "upset")
                                m "Why don't you keep you're shirt like that from now on..."
                                call luna_main("...", "doubtful", "right", "sad", "angry")
                            "-Ask her to come closer-":
                                m "Perhaps you should come stand a little closer."
                                call luna_main("Really? You want me to come closer while you...?", "doubtful", "default", "mad", "upset")
                                m "Well I am so \"old\"..."
                                call luna_main("...", "angry", "right", "angry", "upset")
                                m "I'm waiting..."
                                call luna_main("... {size=-8}(fine...){/size}", "doubtful", "down", "sad", "angry")
                                hide screen luna_chibi
                                with d3
                                ">Luna walks towards you, standing in front of the table..."
                                $ luna_chibi_xpos = 450
                                show screen luna_chibi
                                with d3
                                m "Very good... Maybe you should stand this close from now on..."
                                call luna_main("...", "doubtful", "right", "sad", "angry")


                        call luna_main("Is this what you want?", "doubtful", "down", "sad", "angry")
                        call luna_main("To humiliate me...", "doubtful", "default", "mad", "angry")
                        m "{size=-4}(mmmm... yes...){/size}"
                        call luna_main("You love this, don't you...", "angry", "default", "angry", "upset")
                        ">You start stroking faster."
                        call luna_main("What I'm forced to do...", "angry", "down", "mad", "upset")
                        call luna_main("Just to survive...", "doubtful", "down", "sad", "angry")
                        m "..."
                        call luna_main("Well don't worry about that...", "mad", "default", "mad", "upset")
                        call luna_main("Just keep stroking it.", "mad", "right", "mad", "default")
                        m "{size=-4}(argh... yes...){/size}"
                        call luna_main("You nasty old man", "mad", "default", "mad", "default")
                        m "{size=-4}yes...{/size}"
                        call luna_main("Get your moneys worth...", "doubtful", "default", "mad", "angry")
                        m "{size=-2}(mmmm...){/size}"
                        call luna_main("come on...", "doubtful", "default", "angry", "default")
                        g4 "{size=+4}(agh... almost there...){/size}"
                        call luna_main("come for your poor student...", "doubtful", "default", "sad", "default")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        hide screen luna
                        with d3
                        show screen white
                        pause.1
                        hide screen white
                        pause.2
                        show screen white
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen luna
                        with d3
                        hide screen bld1
                        with d3
                        show screen genie_jerking_sperm
                        with d3
                        show screen bld1
                        with d3
                        call luna_main("That's it, just let it out...", "mad", "default", "mad", "angry")
                        show screen genie_jerking_sperm_02
                        with d3
                        g4 "good work, slut... ah, shit, this feels so good..."
                        show screen genie
                        hide screen bld1
                        #show screen genie_jerking_off
                        with d3
                        call luna_main("Your a nasty old man, aren't you.", "doubtful", "default", "raised", "default")
                        m "ah..."
                        call luna_main("Forcing me to watch you do this...", "doubtful", "right", "mad", "default")
                        m "Ah... I'm not forcing you to do anything..."
                        call luna_main("Hmph well I expect to be paid now...", "mad", "default", "angry", "upset")
                        m "Don't worry, I'll give you your hundred gold."
                        call luna_main("*Hmph* Fine...{p}(Nothing extra...?)", "mad", "right", "angry", "angry")


        call luna_main("Speaking of which...", "seductive", "default", "angry", "upset")
        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        call luna_main("Thank you, [l_genie_name].", "seductive", "right", "default", "default")
        ">Luna leaves your office."

    elif luna_corruption >= 2 and luna_corruption < 13: #THIRD TIME
        if luna_corruption <= 2:
            $ luna_corruption += 1
        call play_music("chipper_doodle")
        m "Tell me [luna_name]..."
        m "How's you're home life going?"
        call luna_main("My home life?", "angry", "right", "raised", "upset")
        call luna_main("In one word, [l_genie_name], inadequate.", "angry", "default", "angry", "pout")
        m "inadequate?"
        call luna_main("Yes! Someone such as myself should be showered with gifts and gold.", "mad", "right", "angry", "pout")
        call luna_main("Instead I live in a chess piece while my stupid, worthless father struggles to sell 10 copies of his dumb paper!", "mad", "down", "mad", "angry")
        m "Surely he sells more than 10 copies?"
        call luna_main("Barely...", "angry", "right", "angry", "upset")
        call luna_main("He's struggling to get any institutions to stock it these days... ever since the ministry stopped buying it.", "doubtful", "right", "angry", "upset")
        menu:
            "-Say nothing-": #act submissive
                if luna_dom <= 1:
                    $ luna_dom += 1
                $ current_payout = 150
                call luna_main("Wait... that's it!", "seductive", "default", "angry", "default")
                m "what's it?"
                call luna_main("Why don't you start buying the quibbler [l_genie_name]?.", "seductive", "default", "default", "default")
                m "I hardly think one more person is going to turn things around."
                call luna_main("Not you personally [l_genie_name], hogwarts!", "mad", "default", "angry", "upset")
                call luna_main("Just imagine how many copies the entire school would buy!", "default", "right", "angry", "smile_large")
                m "Hmmm, I'll think about it..."
                call luna_main("You'll {size=+4}think{/size} about it?", "doubtful", "default", "mad", "angry")
                call luna_main("*Hmph* Maybe I'll just have to {size=+4}think{/size} about getting my father to write a story...", "doubtful", "right", "mad", "angry")
                call luna_main("involving a perverted old headmaster who likes to lure young girls into his office...", "doubtful", "right", "raised", "angry")
                call luna_main("Just to leer at them while he strokes his filthy old cock...", "doubtful", "default", "angry", "angry")
                m "..."
                call luna_main("I'm sure that would sell some extra copies...", "mad", "right", "raised", "angry")
                call luna_main("Well?", "doubtful", "default", "mad", "upset")
                m "Fine, fine. I'll get someone to start ordering some extra copies for the library."
                call luna_main("There, isn't that easy?", "seductive", "right", "angry", "default")
                m "yes..."
                call luna_main("Good. Now as a reward, I'll let you touch that filthy old cock of yours.", "angry", "default", "angry", "default")
                m "..."
                call luna_main("come on [l_genie_name]...", "doubtful", "default", "sad", "default")
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                call luna_main("That's better isn't it?", "doubtful", "default", "angry", "default")
                call luna_main("Just listen to my voice while you stroke yourself...", "doubtful", "right", "angry", "default")
                m "..."
                call luna_main("Just think about how happy I'll be once father becomes a respectable member of society.", "mad", "default", "mad", "default")
                call luna_main("Think about how much you enjoy making me happy...", "mad", "right", "mad", "default")
                m "{size=-4}(argh... yes...){/size}"
                call luna_main("You love making me happy don't you [l_genie_name]...", "mad", "default", "mad", "default")
                m "{size=-4}yes...{/size}"
                call luna_main("say it louder...", "mad", "default", "mad", "default")
                m "yes..."
                call luna_main("It makes you feel so good doesn't it...", "doubtful", "default", "mad", "default")
                m "{size=-2}(mmmm...){/size}"
                m "{size=+2}yes...{/size}"
                call luna_main("maybe i'll even make you kiss my feet... that would make me very happy", "doubtful", "default", "angry", "default")
                g4 "{size=+4}(agh...){/size}"
                g4 "{size=+4}yes...{/size}"
                call luna_main("that's it [l_genie_name], cum for your princess...", "doubtful", "default", "sad", "default")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("cum...", "angry", "default", "mad", "talk")
                call luna_main("{size=+4}cum!{/size}", "angry", "default", "mad", "talk")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                hide screen luna
                with d3
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                g4 "Argh! YES!"
                hide screen luna
                with d3
                hide screen bld1
                with d3
                show screen genie_jerking_sperm
                with d3
                show screen bld1
                with d3
                call luna_main("That's it, [l_genie_name] just like that...", "mad", "default", "angry", "upset")
                show screen genie_jerking_sperm_02
                with d3
                g4 "ah, shit, why does this feels so good..."
                show screen genie
                hide screen bld1
                #show screen genie_jerking_off
                with d3
                call luna_main("Disgusting...", "seductive", "right", "default", "furious")
                m "ah..."
                call luna_main("...", "mad", "default", "angry", "upset")
                m "Thank you..."
                call luna_main("Thank you...?", "doubtful", "default", "mad", "angry")
                m "Thank you princess..."
                if luna_name == "Miss Lovegood":
                    $ luna_name = "Princess"
                call luna_main("That's better [l_genie_name]...", "angry", "default", "angry", "default")
                call luna_main("Now as a princess I expect a present for having to look at such a filthy act...", "angry", "right", "angry", "default")

            "-Make an offer-": #exchange quibbler purchase
                if luna_sub <= 1:
                    $ luna_sub += 1
                $ current_payout = 50
                m "well I'm sure that I could have a few words with the library staff about stocking it..."
                call luna_main("Really? You'd do that?", "wide", "default", "default", "default")
                m "Of course."
                if l_genie_name == "Old man":
                    $ l_genie_name = "Professor"
                call luna_main("Thank you so much [l_genie_name]!", "closed_happy", "default", "default", "default")
                m "I was thinking you could thank me for my generous offer another way..."
                call luna_main("Oh...{p}", "angry", "right", "mad", "angry")
                m "That's not a problem is it [luna_name]?"
                call luna_main("Of course not... What did you have in mind?", "doubtful", "down", "sad", "upset")
                m "well for starters..."
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                menu:
                    "-Ask her to shorten her skirt-":
                        if luna_sub <= 2:
                            $ luna_sub += 1
                        m "lets talk about that skirt of yours..."
                        call luna_main("What about it?", "mad", "default", "angry", "upset")
                        m "have you ever considered wearing it a little... shorter?"
                        call luna_main("...", "angry", "right", "angry", "upset")
                        m "I'm waiting..."
                        call luna_main("...how short?", "doubtful", "down", "sad", "angry")
                        m "Just an inch or so higher."
                        call luna_main("...", "doubtful", "down", "sad", "angry")
                        call luna_main("(my father better appreciate this...)", "doubtful", "down", "sad", "angry")
                        ">Luna pulls up her skirt slightly and then folds it over at the top..."
                        hide screen luna
                        with d3
                        $ luna_skirt_level = 2
                        call luna_main("...", "doubtful", "down", "sad", "angry")
                        m "{size=-4}(mmmm... yes...){/size}"
                        m "Why don't you wear it like that from now on..."
                        call luna_main("yes, [l_genie_name].", "doubtful", "right", "sad", "angry")

                    "-Make her call you sir-":
                        $ l_genie_name = "Sir"
                        m "How about you start giving me the respect I deserve."
                        call luna_main("...", "doubtful", "default", "mad", "upset")
                        m "I want you to refer to me as sir from now on."
                        call luna_main("...", "angry", "right", "angry", "upset")
                        m "Is that clear?"
                        call luna_main("...Yes...{size=-8}sir{/size}", "doubtful", "down", "sad", "angry")
                        m "Speak up [luna_name]..."
                        call luna_main("Yes sir...", "doubtful", "right", "sad", "angry")
                        m "{size=-4}(yes...){/size}"


                call luna_main("You know this is wrong don't you?", "doubtful", "down", "sad", "angry")
                call luna_main("What you're forcing me to do...", "doubtful", "default", "mad", "angry")
                m "{size=-4}(mmmm... yes...){/size}"
                m "I don't recall forcing you into anything [luna_name]..."
                call luna_main("*hmph*...", "angry", "default", "angry", "upset")
                ">You start stroking faster."
                call luna_main("well...", "angry", "down", "mad", "upset")
                call luna_main("just get it over with...", "doubtful", "down", "sad", "angry")
                m "{size=-4}ah...{/size}"
                call luna_main("Just keep touching yourself in front of me...", "mad", "default", "mad", "upset")
                m "{size=-4}(argh... yes...){/size}"
                call luna_main("let it all out front of me...", "mad", "default", "mad", "grin")
                m "{size=-4}yes...{/size}"
                call luna_main("Your student...", "doubtful", "default", "mad", "angry")
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", "doubtful", "default", "angry", "default")
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little princess...", "doubtful", "default", "sad", "default")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                hide screen luna
                with d3
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                g4 "Argh! YES!"
                hide screen luna
                with d3
                hide screen bld1
                with d3
                show screen genie_jerking_sperm
                with d3
                show screen bld1
                with d3
                call luna_main("ugh... there's so much...", "mad", "default", "mad", "angry")
                show screen genie_jerking_sperm_02
                with d3
                g4 "good work, slut... ah, shit, this feels so good..."
                show screen genie
                hide screen bld1
                #show screen genie_jerking_off
                with d3
                call luna_main("The floor...", "angry", "down", "angry", "upset")
                call luna_main("it's covered...", "angry", "right", "angry", "upset")
                m "Ah... you did good [luna_name]..."
                call luna_main("Hmph well I expect to be paid now...", "mad", "default", "angry", "upset")


        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        call luna_main("Thank you, [l_genie_name].", "seductive", "right", "default", "upset")
        if current_payout <= 50:
            call luna_main("(only [current_payout]?) *hmph*", "mad", "right", "angry", "angry")
        ">Luna leaves your office."

    else: #HERMIONE INVOLVED
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        m "Tell me [luna_name]..."
        m "How's your tutoring with Ms granger going?"
        call luna_main("my lessons with hermione?", "angry", "right", "angry", "upset")
        call luna_main("Honestly... they're fantastic.", "default", "down", "default", "default")
        m "really?"
        call luna_main("Yes... at first I thought that they'd just be a waste of time...", "mad", "right", "sad", "upset")
        call luna_main("but they're actually helping a lot.", "default", "default", "sad", "default")
        m "mmmmm, the way you sucked my cock is proof enough of that..."
        call luna_main("*hmph* I meant my grades...", "angry", "right", "angry", "upset")
        call luna_main("Although she has been a great help with sex as well...", "seductive", "down", "angry", "default")
        call luna_main("in fact... Why don't you bring her up here now?", "seductive", "default", "angry", "default")
        m "why?"
        call luna_main("well I think we both know you only started this conversation so you could stroke your filthy cock of your while I speak...", "angry", "default", "angry", "default")
        m "maybe..."
        call luna_main("why not bring hermione up here for a little more fun?", "mad", "default", "angry", "default")
        call luna_main("we might even give you something to look at...", "seductive", "right", "angry", "default")
        m "done!"
        ">you quickly summon hermione up to your office."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ hermione_SC.chibi.xpos = 600 #Near the desk.
        show screen hermione_blink #Hermione stands still.
        $ luna_flip = -1
        $ luna_r_arm = 2
        $ luna_xpos = 390
        call update_her_uniform
        pause
        call her_main("hello Professor!","base","happyCl")
        call her_main("hi luna! what's he want now? another blowjob.","grin","baseL")
        call luna_main("no, he just wants to talk...", "seductive", "default", "angry", "default")
        call her_main("really?","upset","wink")
        call luna_main("I mean he says talk...", "angry", "right", "mad", "upset")
        call luna_main("but I think we both know he wants to sit there and stroke that filthy old cock of his while we do all the talking.", "seductive", "default", "angry", "default")
        call her_main("typical...","base","down")
        call her_main("so what did you want me here for?","base","glance")
        call luna_main("I figured you could lend a hand... plus this way we both get paid.", "angry", "right", "angry", "upset")
        call her_main("Aw, that's so sweet luna!","base","worriedCl")
        call luna_main("Well, it's more like I want a lesson on dirty talk...", "mad", "right", "sad", "upset")
        call her_main("whatever you say... now I think it's about time you started stroking that cock of yours don't you [genie_name]?","base","glance")
        $ luna_flip = 1
        call luna_main("yeah, come on [l_genie_name]...", "seductive", "default", "sad", "default")
        m "I'm not going to say no to that am I?"
        hide screen blktone
        with d3
        ">You reach under the desk and grab your cock..."
        hide screen blktone8
        with d3
        hide screen genie
        show screen genie_jerking_off
        with d3
        pause
        call luna_main("That's better isn't it?", "angry", "default", "sad", "upset")
        call luna_main("Just listen to our voices while you stroke yourself...", "mad", "default", "angry", "default")
        call her_main("mmmm... he loves it when you tell him a story...","base","suspicious")
        call luna_main("Really? What sort?", "seductive", "right", "sad", "default")
        call her_main("how about the time we nearly got caught during blowjob practice...","base","down")
        $ luna_flip = -1
        call luna_main("What? Not that one!", "wide", "default", "sad", "open")
        m "What happened?"
        $ luna_flip = 1
        call luna_main("It's too embarrassing! I'm not telling him that one!", "wide", "right", "sad", "open")
        call her_main("well I don't mind...","open","baseL")
        $ luna_flip = -1
        call luna_main("please hermione...", "wide", "default", "sad", "upset")
        call her_main("shhh...","open","closed")
        m "go on..."
        ">you speed up your stroking."
        call her_main("the other evening, luna and I were busy studying after class as usual...","soft","squintL")
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
        $ luna_flip = 1
        call luna_main("...", "wide", "down", "sad", "angry")
        m "..."
        call her_main("we'd just finished up basic spells revision so we moved onto blowjobs as usual...","open","baseL")
        call luna_main("...", "wide", "right", "sad", "upset")
        m "{size=-2}(mmmm...){/size}"
        call her_main("it was going well when all of a sudden a few second years came into the common room...","angry","wink")
        call luna_main("you said it was going to be empty!", "wide", "left_stare", "sad", "upset")
        call her_main("it was incredible sir... she swallowed the whole thing...","base","down")
        g4 "{size=+4}(agh...){/size}"
        g4 "{size=+4}yes...{/size}"
        call her_main("she hid all 6 inches of it in her mouth... down her throat...","base","glance")
        call her_main("just so we wouldn't get found out...","base","suspicious")
        $ luna_flip = -1
        call luna_main("well what else was I supposed to do...", "wide", "default", "sad", "open")
        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
        g4 "{size=+4}(agh... almost there...){/size}"
        $ luna_flip = 1
        call her_main("she held it there for nearly a minute...","open","baseL")
        call her_main("a few of them even said hello to us...","soft","squintL")
        call her_main("they didn't suspect a thing...","soft","ahegao")
        call luna_main("not until you started touching me under the desk!", "wide", "right", "angry", "upset")
        g4 "{size=+4}*Argh!* yes you whores!{/size}"
        hide screen luna
        with d3
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "Argh! YES!"
        hide screen luna
        with d3
        hide screen bld1
        with d3
        show screen genie_jerking_sperm
        with d3
        show screen bld1
        with d3
        call luna_main("...", "seductive", "default", "sad", "default")
        call her_main("I told you he liked stories...","base","glance")
        show screen genie_jerking_sperm_02
        with d3
        g4 "ah, shit, why does this feels so good..."
        show screen genie
        hide screen bld1
        #show screen genie_jerking_off
        with d3
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png"
        call luna_main("next time just make one up...", "seductive", "right", "angry", "angry")
        m "ah..."
        call her_main("come on luna, we've got to earn our payment, speaking of...","base","suspicious")

        m "Alright, alright. Here's your gold and points."
        $ gryffindor += 15
        $ ravenclaw += 15
        m "15 points to \"gryffindor\" and \"ravenclaw\"."
        $ gold -= 50
        $ luna_gold += 25
        m "and here's your gold."
        ">You hand Luna and hermione 25 gold each."
        call her_main("Thank you [genie_name]!","base","base")
        call luna_main("...Thank you sir.", "seductive", "right", "sad", "upset")
        ">Luna and hermione leave your office, talking as they go."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen luna
        hide screen luna_chibi
        $ luna_busy = True
        hide screen genie_jerking_sperm_02
        jump end_hg_pf

    hide screen genie_jerking_sperm_02
    jump luna_away










label luna_favour_2: ###SIT ON MY LAP
    m "{size=-4}(I'll just ask her to sit on my lap...){/size}"
    if luna_corruption <= 3: #FIRST TIME
        if luna_corruption <= 3:
            $ luna_corruption += 1
        call play_music("chipper_doodle")
        m "Before we get started, Would you like a seat [luna_name]?"
        call luna_main("I would, but there's no chair [l_genie_name]...", "angry", "default", "raised", "upset")
        m "Well how about you come sit on my lap then?"
        call luna_main("...", "doubtful", "default", "angry", "angry")
        m "Come on, it'll be just like santa claus."
        call luna_main("...", "doubtful", "right", "angry", "angry")
        call luna_main("You better make this worth it [l_genie_name]...", "mad", "right", "angry", "angry")
        m "Don't worry, I'm sure you'll be very happy with your \'reward\'."
        call luna_main("...", "doubtful", "default", "angry", "angry")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."
        #chibi stuff
        $ luna_flip = -1
        $ luna_xpos = 120
        $ luna_chibi_xpos = 300
        hide screen blkfade
        with d3
        menu:
            "-Pull her onto your lap-" if luna_sub >= 2:
                if luna_sub <= 3:
                    $ luna_sub += 1
                $ luna_grope = True
                call luna_main("...", "doubtful", "right", "angry", "angry")
                call luna_main("Actually, I'm not sure if...", "mad", "right", "default", "upset")
                ">You grab Luna around the waist and pull her onto your lap."
                call luna_main("Professor! What are you doing?", "wide", "right", "raised", "angry")
                m "just giving you a helping hand..."
                ">you start slowly rubbing your crouch against her soft ass."
                m "mmm that's it..."
                call luna_main("...", "doubtful", "down", "sad", "upset")
                call luna_main("(this is so humiliating...)", "doubtful", "down", "sad", "angry")

                jump luna_lap_dance

            "-Tell her to sit down-":
                $ luna_grope = False
                m "go on [luna_name]..."
                call luna_main("...", "mad", "right", "angry", "angry")
                call luna_main("Do I really have to do this?", "mad", "right", "angry", "angry")
                m "just Sit down [luna_name]..."
                call luna_main("...", "mad", "right", "angry", "angry")
                ">Luna softly takes a seat on your lap ."
                m "mmmmm..."
                call luna_main("...", "doubtful", "right", "sad", "upset")
                call luna_main("(ugh, he's so hard...)", "doubtful", "down", "sad", "furious")

                label luna_lap_dance:
                    m "That's it, now just start moving your waist."
                ">Luna gradually starts grinding her ass against you."
                m "ughh, that's it."
                call luna_main("...", "mad", "down", "angry", "angry")
                call luna_main("are you happy now?", "mad", "right", "mad", "angry")
                m "Very..."
                call luna_main("Can I leave yet?", "mad", "default", "angry", "angry")
                m "What? We just started!"
                call luna_main("Well I don't have all day.", "mad", "right", "angry", "angry")
                m "Hmmm, well I'll see what I can do to speed this up..."
                menu:
                    "-Grab her waist-":
                        ">You take a hold of her waist."
                        call luna_main("!!!", "wide", "default", "default", "furious")
                        call luna_main("I don't think touching was part of the arrangement [l_genie_name]...", "angry", "right", "mad", "snarl")
                        $ current_payout = 75
                        m "Don't worry [luna_name], you'll be compensated fairly."
                        ">You pull her hard against your crouch, rubbing your cock between her cheeks."
                        call luna_main("...", "doubtful", "down", "sad", "grin")
                        m "That's it [luna_name], not much longer now."
                        call luna_main(".......", "mad", "right", "angry", "angry")
                        m "mmmm, almost there..."
                        call luna_main("What?!!!", "wide", "right", "mad", "angry")
                        show screen blkfade
                        with d3
                        "Luna quickly pulls away from you and stands up."
                        #chibi stuff
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        hide screen blkfade
                        with d3
                        call luna_main("Professor!", "angry", "default", "mad", "talk")
                        m "What on earth did you stop for?"
                        call luna_main("Sitting on your lap is one thing.", "mad", "right", "angry", "angry")
                        call luna_main("But letting you do that...", "doubtful", "default", "mad", "upset")
                        call luna_main("I simply refuse!", "mad", "right", "mad", "furious")
                        m "fine fine."
                        call luna_main("Honestly [l_genie_name], who do you think I am?", "angry", "default", "angry", "upset")
                        call luna_main("I think I'd like to be paid now...", "angry", "right", "angry", "upset")
                    "-Grope her-" if luna_grope:
                        ">You start running your hands along the outside of her thighs, up to her waist and then over her belly."
                        call luna_main("!!!", "wide", "default", "default", "furious")
                        m "mmmm, lovely."
                        ">You keep grinding your cock against her butt checks."
                        m "yes, just like that [luna_name]."
                        $ current_payout = 40
                        call luna_main("......", "doubtful", "down", "sad", "furious")
                        m "gods you've got such a nice ass."
                        ">You Start moving your hands slowly up towards her breasts"
                        call luna_main(".........", "doubtful", "right", "sad", "angry")
                        m "That's it [luna_name], just enjoy it."
                        call luna_main("..................", "doubtful", "right", "sad", "upset")
                        ">your hands are about an inch below her breasts..."
                        m "mmmm, almost there..."
                        call luna_main("..........................", "wide", "right", "sad", "upset")
                        ">Your about to reach her ample tits......"
                        call luna_main("!!!!", "wide", "default", "mad", "furious")
                        show screen blkfade
                        with d3
                        "Luna quickly pulls away from you and stands up."
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        hide screen blkfade
                        with d3
                        call luna_main("Professor!", "wide", "default", "mad", "snarl")
                        m "What on earth did you stop for?"
                        call luna_main("Sitting on your lap is one thing!", "doubtful", "default", "angry", "angry")
                        call luna_main("But letting you touch me there...", "mad", "right", "mad", "upset")
                        call luna_main("I won't do it!", "mad", "right", "angry", "angry")
                        m "alright fine."
                        call luna_main("Honestly [l_genie_name], you really need to learn some self control.", "mad", "default", "mad", "sickened")
                        call luna_main("I think I'd like to be paid now...", "mad", "right", "angry", "angry")



            "-Do nothing-" if luna_dom < 2:
                call luna_main("...", "angry", "right", "angry", "upset")
                call luna_main("......", "mad", "right", "angry", "angry")
                call luna_main("I guess I'll start then...", "doubtful", "right", "angry", "upset")
                ">Luna lightly sits on your lap."
                m "mmmm"
                call luna_main("...", "angry", "default", "angry", "upset")
                call luna_main("......", "mad", "right", "angry", "angry")
                call luna_main(".........", "mad", "right", "mad", "angry")
                call luna_main("Alright, time's up!", "default", "right", "default", "upset")
                ">Luna stands up from your lap"
                m "What, you barely even sat down!"
                call luna_main("*hmph* You should consider yourself lucky you got what you did [l_genie_name]!", "mad", "right", "angry", "angry")
                m "You could have at least moved around a little."
                call luna_main("What? Who do you think I am? Some sort of harlot who'll let you grind yourself against them for as long as you want?", "doubtful", "right", "angry", "furious")
                m "well I expected at least a few minutes."
                call luna_main("Well if your that desperate...", "seductive", "right", "default", "default")
                ">Luna slams her ass into your crouch"
                m "ah..."
                call luna_main("pathetic...", "seductive", "right", "angry", "angry")
                ">She starts rocking back and forward on your lap"
                call luna_main("You really are disgusting [l_genie_name]...", "seductive", "right", "default", "talk")
                m "mmmm"
                call luna_main("begging your students for a lap dance...", "mad", "right", "mad", "angry")
                m "yes, yes..."
                call luna_main("well you better pay extra for this...", "angry", "right", "default", "upset")
                m "of course..."
                call luna_main("...", "seductive", "down", "default", "upset")
                ">luna starts rolling her hips a little faster."
                call luna_main("a lot extra...", "doubtful", "right", "mad", "angry")
                m "of course [luna_name]..."
                call luna_main("that's it [l_genie_name]. just enjoy it...", "seductive", "right", "default", "default")
                m "mmm, just a little more..."
                call luna_main("...", "mad", "down", "raised", "angry")
                m "yes... almost..."
                call luna_main("Times up!", "seductive", "right", "angry", "default")
                show screen blkfade
                with d3
                ">Luna quickly stands up."
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3
                m "What!"
                call luna_main("Times{p}up...", "mad", "default", "angry", "upset")
                m "Ugh, fine."
                call luna_main("Glad you understand,{p} now about my payment...", "mad", "right", "angry", "angry")
                $ current_payout = 120


            "-Do nothing-" if luna_dom >= 2:
                if luna_dom <= 3:
                    $ luna_dom += 1
                call luna_main("...", "angry", "default", "angry", "upset")
                call luna_main("......", "mad", "right", "angry", "angry")
                call luna_main("I guess I'll start then...", "doubtful", "right", "angry", "upset")
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", "seductive", "right", "default", "default")
                call luna_main("You're pathetic...", "seductive", "right", "angry", "angry")
                call luna_main("THe worlds greatest wizard...", "seductive", "right", "default", "default")
                call luna_main("More like the worlds greatest pervert.", "doubtful", "right", "angry", "angry")
                if l_genie_name == "Old man":
                    $ l_genie_name = "Pervert"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call luna_main("*hmph* You're not even ashamed are you?", "seductive", "right", "default", "talk")
                m "of what?"
                call luna_main("What? begging your student for a lap dance.", "mad", "right", "angry", "angry")
                m "I don't recall begging."
                call luna_main("Hmmm...", "angry", "right", "default", "upset")
                ">Luna stands up slowly."
                call luna_main("Well then...", "mad", "right", "angry", "angry")
                m "what?"
                call luna_main("beg...", "seductive", "right", "mad", "angry")
                menu:
                    "-Beg-":
                        pass
                    "-Refuse-":
                        m "I don't think so [luna_name]."
                        call luna_main("*hmph* Fine...", "doubtful", "right", "angry", "pout")
                        show screen blkfade
                        with d3
                        ">Luna walks around to the front of the desk."
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        hide screen blkfade
                        with d3
                        call luna_main("I'd like to be paid now [l_genie_name]...", "mad", "default", "mad", "angry")
                        $ current_payout = 100
                        m "Alright, alright. Here's your gold."
                        $ gold -= current_payout
                        $ luna_gold += current_payout
                        ">You hand Luna [current_payout] gold."
                        call luna_main("Thank you, [l_genie_name].", "angry", "right", "angry", "upset")
                        ">Luna leaves your office."
                m "Please..."
                call luna_main("Please what?", "seductive", "right", "default", "upset")
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."
                call luna_main("That's better isn't it?", "angry", "right", "angry", "default")
                ">She starts rocking back and forward on your lap"
                call luna_main("You're so hard...", "seductive", "down", "default", "upset")
                m "mmmm"
                call luna_main("I bet you'd cum if I kept going wouldn't you...", "seductive", "right", "raised", "upset")
                m "yes..."
                call luna_main("well you better be prepared to pay extra for the privilige...", "angry", "right", "angry", "upset")
                m "of course..."
                call luna_main("...", "mad", "right", "angry", "angry")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call luna_main("a {size=+5}lot{/size} extra...", "seductive", "right", "mad", "angry")
                m "of course [luna_name]..."
                call luna_main("Good. just enjoy yourself then...", "closed_happy", "right", "default", "default")
                m "mmm, just a little more..."
                call luna_main("...[l_genie_name]", "seductive", "right", "angry", "upset")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", "doubtful", "default", "angry", "default")
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little girl...", "doubtful", "default", "sad", "default")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna
                with d3
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                g4 "Argh! YES!"
                call luna_main("ugh... pathetic...", "seductive", "right", "mad", "default")
                call luna_main("...", "mad", "right", "angry", "angry")
                call luna_main("......", "mad", "down", "raised", "upset")
                call luna_main(".........", "mad", "down", "mad", "angry")
                call luna_main("Alright, time's up!", "seductive", "right", "angry", "default")
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3
                call luna_main("*hmph* You [l_genie_name]!", "doubtful", "default", "angry", "upset")
                m "You can hardly blame me for this."
                call luna_main("What? You're the one who begged for it, of course it's your fault.", "angry", "right", "mad", "angry")
                m "well you didn't have to be so good at it."
                call luna_main("I was just making sure that I earned my reward.", "mad", "default", "angry", "angry")
                call luna_main("Speaking of which...", "seductive", "right", "default", "default")
                $ current_payout = 200



        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        if current_payout <= 50:
            call luna_main("(only [current_payout]?) *hmph*", "mad", "right", "angry", "angry")
            call luna_main("Thank you, [l_genie_name].", "doubtful", "right", "angry", "upset")
        else:
            call luna_main("Thank you, [l_genie_name].", "seductive", "right", "default", "default")
        ">Luna leaves your office."

    elif luna_corruption <= 4: #SECOND TIME
        if luna_corruption <= 4:
            $ luna_corruption += 1
        call play_music("chipper_doodle")
        m "Can I offer you another seat [luna_name]?"
        if luna_sub > luna_dom:
            call luna_main("...", "default", "down", "sad", "upset")
            call luna_main("Alright [l_genie_name]...", "default", "right", "sad", "upset")
            m "Good girl."
            call luna_main("...", "default", "down", "sad", "angry")
        else:
            call luna_main("Fine...", "default", "right", "angry", "upset")
            call luna_main("But I expect to be fairly compensated [l_genie_name]...", "angry", "default", "angry", "upset")
            m "yes, yes..."
            call luna_main("...", "angry", "right", "angry", "upset")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."
        #chibi stuff
        $ luna_flip = -1
        $ luna_xpos = 120
        $ luna_chibi_xpos = 300
        hide screen blkfade
        with d3
        menu:
            "-Ask her to remove her skirt first-" if luna_sub >= 2:
                if luna_sub <= 3:
                    $ luna_sub += 1
                $ luna_grope = True
                m "How about you take off your skirt before we start?"
                call luna_main("!!!", "wide", "right", "sad", "upset")
                call luna_main("You're not serious are you?", "doubtful", "right", "sad", "upset")
                m "I am [luna_name], or do you not want hogwarts to keep purchasing new copies of the quibbler?"
                call luna_main("...", "doubtful", "down", "sad", "upset")
                call luna_main("......", "doubtful", "right", "sad", "upset")
                m "I'm waiting."
                call luna_main("Fine...", "doubtful", "down", "sad", "furious")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">Luna slowly removes her skirt, revealing her black silk panties."
                show screen luna
                hide screen blkfade
                with d3
                m "I like your panties..."
                call luna_main("...", "doubtful", "down", "sad", "upset")
                call luna_main("(this is so degrading)", "doubtful", "down", "sad", "furious")
                m "Now take a seat..."
                call luna_main("yes [l_genie_name]...", "doubtful", "right", "sad", "upset")
                ">Luna softly takes a seat on your lap."
                call luna_main("...", "doubtful", "down", "sad", "angry")
                jump luna_lap_dance_2

            "-Tell her to sit down-" if luna_sub >= luna_dom:
                $ luna_grope = False
                m "come on now..."
                call luna_main("...", "mad", "right", "sad", "angry")
                call luna_main("......", "mad", "right", "sad", "angry")
                m "Sit down [luna_name]."
                call luna_main("...", "mad", "right", "sad", "angry")
                ">Luna softly takes a seat on your lap ."
                m "mmmmm..."
                call luna_main("...", "doubtful", "right", "sad", "upset")
                call luna_main("(ugh, he's so hard...)", "doubtful", "down", "sad", "furious")

                label luna_lap_dance_2:
                    m "That's it, now just start moving your ass."
                ">Luna gradually starts grinding her waist against you."
                m "ughh, that's it."
                call luna_main("...", "mad", "down", "sad", "angry")
                call luna_main("is this alright?", "seductive", "right", "sad", "upset")
                m "yes, just keep going..."
                call luna_main("For how long?", "mad", "default", "sad", "angry")
                m "As long as it takes [luna_name]."
                call luna_main("fine...", "mad", "right", "sad", "angry")
                call luna_main("...", "mad", "down", "sad", "angry")
                call luna_main("..........", "doubtful", "down", "sad", "angry")
                call luna_main("Is there anything I can do to speed this up?", "doubtful", "right", "sad", "upset")
                menu:
                    "-enjoy yourself-":
                        $ current_payout = 65
                        m "Just keep doing what you're doing..."
                        call luna_main("...", "doubtful", "down", "sad", "furious")
                        call luna_main("How about this?", "seductive", "right", "sad", "upset")
                        ">Luna starts jiggling her ass slightly as she rocks back and forth."
                        m "Mmmm, yes!"
                        ">You start thrusting into her ever so slightly."
                        call luna_main("...", "doubtful", "down", "sad", "grin")
                        m "That's it [luna_name], not much longer now."
                        call luna_main(".......", "seductive", "right", "sad", "upset")
                        m "mmmm, almost there..."
                        call luna_main("Already?", "wide", "right", "sad", "angry")
                        m "Almost... this is really good..."
                        call luna_main("it is?", "seductive", "right", "sad", "default")
                        m "yeah, just keep moving that perfect little ass of yours..."
                        call luna_main("...", "seductive", "right", "sad", "default")
                        call luna_main("How's this?", "seductive", "down", "sad", "grin")
                        ">She starts rocking back and forward on your lap"
                        m "mmmmm"
                        call luna_main("You're so hard [l_genie_name]...", "seductive", "down", "sad", "default")
                        m "mmmm"
                        call luna_main("are you almost there?", "seductive", "right", "sad", "upset")
                        m "yes..."
                        call luna_main("well I expect to be-", "seductive", "right", "angry", "angry")
                        m "shhh, don't ruin it."
                        call luna_main("...", "mad", "right", "sad", "angry")
                        ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                        m "ah..."
                        call luna_main("...", "seductive", "right", "sad", "angry")
                        m "keep going [luna_name]..."
                        call luna_main("........", "closed", "right", "sad", "default")
                        m "mmm, just a little more..."
                        call luna_main("...[l_genie_name]...", "angry", "down", "sad", "upset")
                        ">Luna starts grinding hard against your lap."
                        m "{size=-2}(mmmm...){/size}"
                        call luna_main("......", "doubtful", "default", "sad", "default")
                        g4 "{size=+4}(agh... almost there...){/size}"
                        $ luna_tears = 1
                        call luna_main("............", "doubtful", "default", "sad", "default")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        ">You start shooting your load against the inside of your cloak."
                        hide screen luna
                        with d3
                        show screen white
                        pause.1
                        hide screen white
                        pause.2
                        show screen white
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        $ luna_tears = 0
                        call luna_main("ugh...", "seductive", "right", "sad", "default")
                        call luna_main("...", "mad", "right", "sad", "angry")
                        call luna_main("......", "mad", "down", "sad", "upset")
                        call luna_main(".........", "seductive", "down", "sad", "angry")
                        call luna_main("Are you finished now [l_genie_name]?", "seductive", "right", "sad", "default")
                        m "Almost... just stay there for a little longer..."
                        call luna_main("......", "seductive", "right", "sad", "default")
                        ">Luna waits for a few seconds before standing up."
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        $ luna_wear_skirt = True
                        hide screen blkfade
                        with d3
                        call luna_main("will that be all [l_genie_name]?", "doubtful", "default", "sad", "upset")
                        m "Yes, thank you [luna_name]."
                        call luna_main("You're welcome [l_genie_name].", "angry", "right", "sad", "angry")
                        call luna_main("Well I better be off to class then.", "mad", "default", "sad", "angry")
                        m "Don't you want your payment first?"
                        call luna_main("Oh right...", "seductive", "right", "sad", "default")
                    "-Grope her-" if luna_grope:
                        $ current_payout = 35
                        ">You start running your hands along the outside of her thighs."
                        call luna_main("...", "wide", "default", "sad", "furious")
                        m "mmmm, lovely."
                        ">You keep grinding your cock against her butt checks."
                        call luna_main("....", "seductive", "right", "sad", "furious")
                        m "yes, just like that [luna_name]."
                        "You move your hands up to her waist"
                        call luna_main("......", "doubtful", "down", "sad", "furious")
                        m "gods you've got such a nice ass."
                        $ luna_tears = 1
                        call luna_main("t-thank you [l_genie_name]...", "closed_happy", "right", "sad", "angry")
                        ">You Start moving your hands slowly up over her smooth stomach."
                        call luna_main(".........", "doubtful", "right", "sad", "angry")
                        m "That's it [luna_name], just enjoy yourself..."
                        $ luna_tears = 0
                        call luna_main("..................", "doubtful", "right", "sad", "upset")
                        ">your hands are about an inch below her breasts..."
                        m "mmmm, almost there..."
                        call luna_main("..........................", "wide", "right", "sad", "upset")
                        ">You quickly move your hands up and grab a hold of her supple breasts over her vest."
                        call luna_main("!!!!", "wide", "default", "mad", "furious")
                        "Luna quickly tries to pull away from you."
                        menu:
                            "-let her up-":
                                $ current_payout = 55
                                ">Luna quickly stands up and moves around to the front of your desk."
                                $ luna_flip = 1
                                $ luna_xpos = 600
                                $ luna_chibi_xpos = 500
                                $ luna_wear_skirt = True
                                hide screen blkfade
                                with d3
                                call luna_main("Professor!", "wide", "default", "mad", "snarl")
                                call luna_main("Grabbing me there wasn't part of the deal!", "mad", "right", "mad", "upset")
                                m "I just couldn't resist..."
                                call luna_main("*hmph*", "mad", "right", "angry", "angry")
                                m "My apologies, [luna_name]."
                                call luna_main("It's alright... just don't let it happen again!", "mad", "default", "mad", "sickened")
                                call luna_main("I think I'd like to be paid now...", "mad", "right", "angry", "angry")
                            "-Hold her down-":
                                if luna_sub <= 4:
                                    $ luna_sub += 1
                                call luna_main("Professor!", "wide", "default", "mad", "snarl")
                                call luna_main("I'd like to leave now!", "mad", "right", "mad", "upset")
                                m "just a bit longer [luna_name]..."
                                ">You start grinding your hard cock between her ample cheeks."
                                call luna_main("!!!", "wide", "down", "sad", "angry")
                                call luna_main("I insist you let me go!", "wide", "right", "mad", "pout")
                                m "If you leave now you can forget about hogwarts purchasing any more of your father's newspaper, [luna_name]."
                                call luna_main("...", "doubtful", "down", "sad", "angry")
                                $ luna_tears = 1
                                call luna_main("you're despicable [l_genie_name]...", "mad", "right", "angry", "angry")
                                ">You give her tits a couple of firm squeezes..."
                                call luna_main("ah{image=textheart}...", "angry", "down", "sad", "angry")
                                call luna_main("this isn't right...", "angry", "right", "sad", "angry")
                                m "I know, I know... But it's hard to resist..."
                                call luna_main(".................", "seductive", "down", "sad", "upset")
                                call luna_main("....................ah...{image=textheart}", "seductive", "down", "sad", "talk")
                                call luna_main("[l_genie_name], you need to stop now...", "angry", "right", "sad", "angry")
                                m "Just a bit longer..."
                                $ luna_tears = 2
                                call luna_main("please...", "angry", "down", "sad", "angry")
                                m "mmmm, I suppose this will have to do..."
                                ">You give her tits a final pinch..."
                                call luna_main("ah...", "angry", "down", "sad", "angry")
                                ">Luna quickly stands up and moves around to the front of your desk."
                                $ luna_flip = 1
                                $ luna_tears = 1
                                $ luna_xpos = 600
                                $ luna_chibi_xpos = 500
                                $ luna_wear_skirt = True
                                hide screen blkfade
                                with d3
                                call luna_main("Professor!", "wide", "default", "mad", "snarl")
                                call luna_main("Grabbing me there wasn't part of the deal!", "mad", "right", "mad", "upset")
                                m "Sorry, [luna_name], I just couldn't help myself..."
                                call luna_main(".......just please try to control yourself next time...", "mad", "default", "mad", "sickened")
                                m "So you want there to be a next time?"
                                call luna_main("as long as I'm getting paid.", "mad", "right", "angry", "angry")
                                call luna_main("speaking of which...", "mad", "default", "angry", "angry")
                                call luna_main("can I please be paid now?", "mad", "down", "sad", "angry")


            "-Do nothing-" if luna_sub <= luna_dom:
                call luna_main("...", "angry", "default", "angry", "upset")
                call luna_main("......", "mad", "right", "angry", "angry")
                call luna_main("I suppose I'll start then...", "doubtful", "right", "angry", "upset")
                ">Luna lightly places herself on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", "seductive", "right", "default", "default")
                call luna_main("You're so pathetic...", "seductive", "right", "angry", "angry")
                call luna_main("THe worlds greatest wizard...", "seductive", "right", "default", "default")
                call luna_main("More like the worlds greatest pervert.", "doubtful", "right", "angry", "angry")
                if luna_name == "Miss Lovegood":
                    $ luna_name = "Princess"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call luna_main("*hmph* You're not even ashamed are you?", "seductive", "right", "mad", "talk")
                m "of what?"
                call luna_main("What? begging your student for a lap dance.", "mad", "right", "angry", "angry")
                m "I don't recall begging."
                call luna_main("Hmmm...", "angry", "right", "default", "upset")
                ">Luna stands up slowly."
                call luna_main("Well then...", "mad", "right", "angry", "angry")
                m "what?"
                call luna_main("beg...", "seductive", "right", "mad", "angry")
                m "Please..."
                call luna_main("Please what?", "seductive", "right", "default", "upset")
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."
                call luna_main("That's better isn't it?", "angry", "right", "angry", "default")
                ">She starts rocking back and forward on your lap"
                call luna_main("ugh, You're so hard...", "doubtful", "down", "mad", "angry")
                m "mmmm"
                call luna_main("I bet you'd cum if I kept going wouldn't you...", "seductive", "right", "angry", "default")
                m "yes..."
                call luna_main("well you better be prepared to pay extra for the privilige...", "angry", "right", "angry", "upset")
                m "of course..."
                call luna_main("...", "mad", "right", "angry", "angry")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call luna_main("a {size=+5}lot{/size} extra...", "seductive", "right", "mad", "default")
                m "of course [luna_name]..."
                call luna_main("Good. just enjoy yourself then...", "closed_happy", "right", "default", "default")
                m "mmm, just a little more..."
                call luna_main("...[l_genie_name]", "seductive", "right", "angry", "default")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", "doubtful", "default", "angry", "default")
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your queen...", "doubtful", "default", "sad", "default")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna
                with d3
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                g4 "Argh! YES!"
                call luna_main("mmmm... pathetic...", "seductive", "right", "mad", "default")
                call luna_main("...", "angry", "right", "angry", "angry")
                call luna_main("......", "mad", "down", "mad", "upset")
                call luna_main(".........", "doubtful", "down", "mad", "angry")
                call luna_main("Alright, time's up!", "seductive", "right", "angry", "default")
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3
                call luna_main("*hmph* You naughty [l_genie_name]!", "doubtful", "default", "angry", "upset")
                m "You can hardly blame me for this."
                call luna_main("What? You're the one who begged for it, of course it's your fault.", "angry", "right", "mad", "angry")
                m "well you didn't have to be so good at it."
                call luna_main("I was just making sure that I earned my reward.", "mad", "default", "angry", "default")
                call luna_main("Speaking of which...", "seductive", "right", "default", "default")
                $ current_payout = 200


            "-Ask Nicely-" if luna_dom >= 2:
                if luna_dom <= 3:
                    $ luna_dom += 1
                m "can you please sit on my lap [luna_name]?"
                call luna_main("...", "seductive", "right", "default", "default")
                call luna_main("......", "mad", "right", "angry", "default")
                call luna_main("well seeing as how you asked so nicely...", "doubtful", "right", "default", "default")
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", "seductive", "down", "angry", "default")
                call luna_main("You're pathetic...", "seductive", "right", "angry", "default")
                call luna_main("THe worlds greatest wizard...", "seductive", "right", "default", "default")
                call luna_main("More like the worlds greatest pervert.", "doubtful", "down", "angry", "default")
                if l_genie_name == "Old man":
                    $ l_genie_name = "Pervert"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call luna_main("*hmph* You're not even ashamed are you?", "seductive", "down", "angry", "talk")
                m "of what?"
                call luna_main("What? begging your student for a lap dance.", "mad", "right", "angry", "default")
                m "I don't recall begging."
                call luna_main("Hmmm...", "seductive", "right", "angry", "default")
                ">Luna stands up slowly."
                call luna_main("Well then...", "mad", "right", "angry", "angry")
                m "what?"
                call luna_main("beg...", "seductive", "right", "mad", "angry")
                m "Please..."
                call luna_main("Please what?", "seductive", "default", "raised", "default")
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."
                call luna_main("That's better isn't it?", "angry", "right", "angry", "default")
                ">She starts rocking back and forward on your lap"
                call luna_main("You're so hard...", "seductive", "down", "mad", "default")
                m "mmmm"
                call luna_main("I bet you'd cum if I kept going wouldn't you...", "seductive", "right", "raised", "default")
                m "yes..."
                call luna_main("well you better be prepared to pay extra for the privilige...", "angry", "right", "angry", "default")
                m "of course..."
                call luna_main("...", "mad", "right", "angry", "default")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call luna_main("a {size=+5}lot{/size} extra...", "seductive", "down", "mad", "default")
                m "of course [luna_name]..."
                call luna_main("Good. just enjoy yourself then...", "closed_happy", "right", "angry", "default")
                m "mmm, just a little more..."
                call luna_main("...[l_genie_name]", "seductive", "right", "default", "default")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", "doubtful", "default", "angry", "default")
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little girl...", "angry", "default", "sad", "talk")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna
                with d3
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                g4 "Argh! YES!"
                call luna_main("ugh... pathetic...", "seductive", "right", "mad", "default")
                call luna_main("...", "angry", "right", "angry", "angry")
                call luna_main("......", "mad", "down", "raised", "default")
                call luna_main(".........", "doubtful", "right", "mad", "default")
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, that's enough now [luna_name]."
                call luna_main("Who says you get to decide when this ends?", "doubtful", "right", "angry", "angry")
                ">Luna starts rolling her hips, focusing on the head of your cock."
                g11 "ah, please, not after I just came."
                call luna_main("really?", "mad", "right", "raised", "default")
                call luna_main("But you sounded so sincere earlier when you were begging for this.", "seductive", "right", "sad", "talk")
                call luna_main("Surely you don't want it to end already?", "seductive", "right", "angry", "default")
                ">she pushes hard against your cock."
                g11 "ah..."
                call luna_main("That's it [l_genie_name], just keep enjoying yourself.", "mad", "down", "angry", "default")
                g11 "I can't, it's too sensitive..."
                call luna_main("I don't see how that's my problem.", "mad", "right", "sad", "default")
                ">She starts moving as fast as she can."
                g11 "{size=-2}ahhh...{/size}"
                call luna_main("come on [l_genie_name]...", "doubtful", "right", "angry", "default")
                g11 "{size=+4}aghhh!{/size}"
                call luna_main("shoot another filthy load...", "doubtful", "right", "mad", "default")
                g4 "{size=+4}*Argh!* It's too much!{/size}"
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "doubtful", "down", "mad", "default")
                ">You start shooting another load against the inside of your sodden cloak."
                hide screen luna
                with d3
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                g4 "Argh!"
                call luna_main("good boy...", "seductive", "right", "mad", "default")
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3
                call luna_main("*hmph* You nasty old [l_genie_name]!", "doubtful", "default", "angry", "default")
                m "ah..."
                call luna_main("Enjoy yourself a little too much did we?", "angry", "right", "mad", "default")
                m "That was too much [luna_name]..."
                call luna_main("Stop complaining. I was just making sure that I earned my reward.", "mad", "default", "angry", "default")
                call luna_main("Speaking of which...", "seductive", "right", "default", "default")
                $ current_payout = 250


        if luna_dom >= luna_sub:
            m "Alright, alright. Here's your gold."
        else:
            m "Here's your payment [luna_name]."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        if current_payout <= 50:
            call luna_main("(only [current_payout]?) *hmph*", "mad", "right", "angry", "angry")
            call luna_main("Thank you, [l_genie_name].", "doubtful", "right", "angry", "upset")
        else:
            call luna_main("Thank you, [l_genie_name].", "seductive", "right", "default", "default")
        ">Luna leaves your office."

    elif luna_corruption >= 5 and luna_corruption < 13: #THIRD TIME
        if luna_corruption <= 5:
            $ luna_corruption += 1
        call play_music("chipper_doodle")
        m "Can I offer you another seat [luna_name]?"
        if luna_sub > luna_dom:
            call luna_main("...", "default", "down", "sad", "upset")
            call luna_main("Alright [l_genie_name]...", "default", "right", "sad", "upset")
            m "Good girl."
            call luna_main("...", "default", "down", "sad", "angry")
        else:
            call luna_main("Fine...", "default", "right", "angry", "upset")
            call luna_main("But I expect to be fairly compensated [l_genie_name]...", "angry", "default", "angry", "upset")
            m "yes, yes..."
            call luna_main("...", "angry", "right", "angry", "upset")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."
        #chibi stuff
        $ luna_flip = -1
        $ luna_xpos = 120
        $ luna_chibi_xpos = 300
        hide screen blkfade
        with d3
        menu:
            "-Pull her onto your lap-" if luna_sub >= 3:
                if luna_sub <= 4:
                    $ luna_sub += 1
                $ luna_grope = True
                ">You grab Luna by the waist and pull her hard onto your lap."
                call luna_main("!!!", "wide", "right", "sad", "upset")
                call luna_main("There's no need to be so forceful [l_genie_name]!", "angry", "right", "sad", "pout")
                m "Sorry, it's hard to help myself when I've got such an eager slut in front of me. You don't mind do you?"
                call luna_main("...", "doubtful", "down", "sad", "default")
                call luna_main("......", "seductive", "right", "sad", "upset")
                m "Do you?..."
                call luna_main("{size=-5}No...{/size}", "doubtful", "down", "sad", "upset")
                call luna_main("...", "doubtful", "right", "sad", "upset")
                m "No what?"
                call luna_main("{size=-5}No... sir...{/size}", "doubtful", "down", "sad", "furious")
                m "Good girl..."
                ">You push your cock hard against her ass."
                call luna_main("ah... thank you [l_genie_name]...", "doubtful", "down", "sad", "default")
                call luna_main("...", "doubtful", "down", "sad", "angry")
                jump luna_lap_dance_3

            "-Tell her to sit down-" if luna_sub >= luna_dom:
                $ luna_grope = False
                if luna_sub <= 3:
                    $ luna_sub += 1
                m "why don-"
                ">Luna quickly sits down on your lap, wriggling around slightly until your cock rests between her cheeks."
                call luna_main("(ah...{image=textheart})", "mad", "down", "sad", "default")
                call luna_main("......", "wide", "right", "sad", "angry")
                m "Some one's eager today..."
                call luna_main("...", "mad", "down", "sad", "angry")
                ">Luna softly starts rocking her hips back and forth."
                m "mmmmm..."
                call luna_main("...", "doubtful", "right", "sad", "upset")
                call luna_main("(he's so hard...{image=textheart})", "doubtful", "down", "sad", "default")

                label luna_lap_dance_3:
                    m "That's it, now just start moving your ass a little more."
                ">Luna starts forcefuly grinding her supple ass against you."
                m "mmmm, that's it."
                call luna_main("...", "mad", "down", "sad", "angry")
                call luna_main("is this good?", "seductive", "right", "sad", "upset")
                m "yes, just keep going..."
                call luna_main("For how long?", "mad", "default", "sad", "angry")
                m "As long as it takes [luna_name]."
                call luna_main("fine...", "mad", "right", "sad", "angry")
                call luna_main("...", "mad", "down", "sad", "angry")
                call luna_main("..........", "doubtful", "down", "sad", "angry")
                call luna_main("Is there anything I can do to speed this up?", "doubtful", "right", "sad", "default")
                call luna_main("Not that I want it to end...", "doubtful", "down", "sad", "default")
                call luna_main("It's just that people will start to ask questions if-", "seductive", "right", "sad", "upset")
                menu:
                    "-enjoy yourself-":
                        $ current_payout = 75
                        m "shhh... Just keep doing what you're doing..."
                        call luna_main("...", "doubtful", "down", "sad", "furious")
                        call luna_main("How about this?", "seductive", "down", "sad", "upset")
                        ">Luna starts jiggling her ass slightly as she rocks back and forth."
                        m "Mmmm, yes!"
                        ">You start thrusting into her ever so slightly."
                        call luna_main("...", "doubtful", "down", "sad", "pout")
                        m "That's it [luna_name], not much longer now."
                        call luna_main(".......", "seductive", "right", "sad", "upset")
                        m "mmmm, almost there..."
                        call luna_main("Already?", "wide", "right", "sad", "angry")
                        m "Almost... this is really good..."
                        call luna_main("it is?", "seductive", "right", "sad", "default")
                        m "yeah, just keep moving that perfect little ass of yours..."
                        call luna_main("...", "seductive", "right", "sad", "default")
                        call luna_main("How's this?", "seductive", "down", "sad", "grin")
                        ">She starts rocking back and forward on your lap"
                        m "mmmmm"
                        call luna_main("You're so hard [l_genie_name]...", "seductive", "down", "sad", "default")
                        m "mmmm"
                        call luna_main("are you almost there?", "seductive", "right", "sad", "default")
                        m "yes..."
                        call luna_main("well I expect to be-", "seductive", "right", "angry", "angry")
                        m "shhh, don't ruin it."
                        call luna_main("...", "mad", "right", "sad", "angry")
                        ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                        m "ah..."
                        call luna_main("...", "seductive", "right", "sad", "angry")
                        m "keep going [luna_name]..."
                        call luna_main("........", "closed", "right", "sad", "default")
                        m "mmm, just a little more..."
                        call luna_main("...[l_genie_name]...", "angry", "down", "sad", "default")
                        ">Luna starts grinding hard against your lap."
                        m "{size=-2}(mmmm...){/size}"
                        call luna_main("......", "doubtful", "default", "sad", "default")
                        g4 "{size=+4}(agh... almost there...){/size}"
                        $ luna_tears = 1
                        call luna_main("............", "doubtful", "default", "sad", "default")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        ">You start shooting your load against the inside of your cloak."
                        hide screen luna
                        with d3
                        show screen white
                        pause.1
                        hide screen white
                        pause.2
                        show screen white
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        $ luna_tears = 0
                        call luna_main("ugh...", "seductive", "right", "sad", "default")
                        call luna_main("...", "mad", "right", "sad", "angry")
                        call luna_main("......", "mad", "down", "sad", "upset")
                        call luna_main(".........", "seductive", "down", "sad", "angry")
                        call luna_main("Are you finished now [l_genie_name]?", "seductive", "right", "sad", "default")
                        m "Almost... just stay there for a little longer..."
                        call luna_main("ok......", "seductive", "down", "sad", "default")
                        ">Luna waits for a few seconds before standing up."
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        $ luna_wear_skirt = True
                        hide screen blkfade
                        with d3
                        call luna_main("will that be all [l_genie_name]?", "doubtful", "default", "sad", "default")
                        m "Yes, thank you [luna_name]."
                        call luna_main("You're welcome [l_genie_name].", "angry", "right", "sad", "angry")
                        call luna_main("Well I better be off to class then.", "mad", "default", "sad", "angry")
                        m "Don't you want your payment first?"
                        call luna_main("Oh right...", "seductive", "right", "sad", "default")
                    "-Grope her-" if luna_grope:
                        $ current_payout = 35
                        ">You start running your hands along the outside of her thighs."
                        call luna_main("ah...{image=textheart}", "wide", "default", "sad", "default")
                        m "mmmm, lovely."
                        ">You keep grinding your cock against her butt checks."
                        call luna_main("....", "seductive", "down", "sad", "furious")
                        m "yes, just like that [luna_name]..."
                        "You move your hands to her knees, just at the edge of her skirt."
                        call luna_main("......", "doubtful", "down", "sad", "default")
                        m "gods you've got such nice legs."
                        $ luna_tears = 1
                        call luna_main("t-thank you [l_genie_name]...", "closed_happy", "right", "sad", "upset")
                        ">You Start slowly moving your hands back towards her waist, pulling up her skirt slightly as you go."
                        call luna_main(".........", "doubtful", "right", "sad", "angry")
                        m "That's it [luna_name], just enjoy yourself..."
                        $ luna_tears = 0
                        call luna_main("..................", "doubtful", "right", "sad", "upset")
                        ">you move your hands to the inside of her thighs..."
                        m "mmmm, that's it..."
                        call luna_main("..........................", "wide", "right", "sad", "upset")
                        ">You start stroking the insides of her thighs, moving closer towards her sex each time."
                        call luna_main("!!!!", "wide", "default", "mad", "furious")
                        $ luna_tears = 1
                        if luna_sub <= 4:
                            $ luna_sub += 1
                        call luna_main("Professor...", "wide", "default", "mad", "snarl")
                        call luna_main("please...", "mad", "right", "mad", "upset")
                        m "just a bit longer [luna_name]..."
                        ">You start grinding your hard cock between her ample cheeks."
                        call luna_main("...", "wide", "down", "sad", "angry")
                        call luna_main("[l_genie_name]...", "mad", "right", "angry", "angry")
                        ">You start lightly running your the tips of your fingers up and down her thighs..."
                        call luna_main("ah{image=textheart}...", "angry", "down", "sad", "angry")
                        $ luna_tears = 2
                        call luna_main("[l_genie_name]... this isn't right...", "angry", "right", "sad", "angry")
                        m "you don't seem to mind..."
                        call luna_main("(I'll let him keep going for a little bit more...)", "seductive", "down", "sad", "upset")
                        call luna_main("(Then I'll make him stop).......ah...{image=textheart}", "seductive", "down", "sad", "talk")
                        call luna_main("[l_genie_name], how much longer do you need?...", "angry", "right", "sad", "angry")
                        m "Just a bit longer..."
                        ">Luna keeps rubbing her ass against your sensitive cock."
                        m "ugh, that's it [luna_name]."
                        call luna_main("p-please hurry [l_genie_name]...", "doubtful", "right", "sad", "angry")
                        m "Well I think I might know a way to speed this up."
                        call luna_main("really?", "mad", "right", "sad", "default")
                        call luna_main("what are-", "seductive", "right", "sad", "talk")
                        ">You quickly move your hands up and grab a hold of her supple breasts through her vest."
                        call luna_main("!!!!", "wide", "default", "mad", "furious")
                        ">Luna's body quivers as her hips roll against you."
                        m "mmm that's it [luna_name]..."
                        call luna_main("...", "mad", "down", "sad", "default")
                        m "I think someone's enjoying herself."
                        call luna_main("What?", "mad", "right", "sad", "default")
                        call luna_main("You think I enjoy this? Feeling your disgusting old cock grind against me?", "mad", "down", "sad", "default")
                        m "{size=-2}ahhh...{/size}"
                        call luna_main("while you paw at me like some filthy old pervert?", "doubtful", "empty", "sad", "default")
                        m "{size=+4}aghhh!{/size}"
                        call luna_main("you really are a filthy old man aren't you...", "doubtful", "right", "sad", "default")
                        g4 "{size=+4}*Argh!* that's is [luna_name]! here it comes!{/size}"
                        call luna_main("!!!!", "wide", "down", "sad", "furious")
                        ">You start shooting a massive load against Luna's ass"
                        hide screen luna
                        with d3
                        show screen white
                        pause.1
                        hide screen white
                        pause.2
                        show screen white
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh!"
                        call luna_main(".....", "mad", "down", "sad", "default")
                        ">Luna stands up from your lap"
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        hide screen blkfade
                        with d3
                        call luna_main("*hmph*", "doubtful", "default", "angry", "default")
                        m "ah... gods that was good"
                        $ luna_tears = 1
                        call luna_main("I think I'd like to leave now [l_genie_name]...", "seductive", "right", "default", "default")

            "-Ask Nicely-" if luna_dom >= luna_sub:
                if luna_dom <= 3:
                    $ luna_dom += 1
                m "can you please sit on my lap [luna_name]?"
                call luna_main("...", "seductive", "right", "default", "default")
                call luna_main("......", "mad", "right", "angry", "default")
                call luna_main("well seeing as how you asked so nicely...", "doubtful", "right", "default", "default")
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", "seductive", "down", "angry", "default")
                call luna_main("You're pathetic...", "seductive", "right", "angry", "default")
                call luna_main("THe worlds greatest wizard...", "seductive", "right", "default", "default")
                call luna_main("More like the worlds greatest pervert.", "doubtful", "down", "angry", "default")
                if l_genie_name == "Old man":
                    $ l_genie_name = "Pervert"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call luna_main("*hmph* You're not even ashamed are you?", "seductive", "down", "angry", "talk")
                m "of what?"
                call luna_main("What? begging your student for a lap dance.", "mad", "right", "angry", "default")
                m "I don't recall begging."
                call luna_main("Hmmm...", "seductive", "right", "angry", "default")
                ">Luna stands up slowly."
                call luna_main("Well then...", "mad", "right", "angry", "angry")
                m "what?"
                call luna_main("beg...", "seductive", "right", "mad", "angry")
                m "Please..."
                call luna_main("Please what?", "seductive", "default", "raised", "default")
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."
                call luna_main("That's better isn't it?", "angry", "right", "angry", "default")
                ">She starts rocking back and forward on your lap"
                call luna_main("You're so hard...", "seductive", "down", "mad", "default")
                m "mmmm"
                call luna_main("I bet you'd cum if I kept going wouldn't you...", "seductive", "right", "raised", "default")
                m "yes..."
                call luna_main("well you better be prepared to pay extra for the privilige...", "angry", "right", "angry", "default")
                m "of course..."
                call luna_main("...", "mad", "right", "angry", "default")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call luna_main("a {size=+5}lot{/size} extra...", "seductive", "down", "mad", "default")
                m "of course [luna_name]..."
                call luna_main("Good. just enjoy yourself then...", "closed_happy", "right", "angry", "default")
                m "mmm, just a little more..."
                call luna_main("...[l_genie_name]", "seductive", "right", "default", "default")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", "doubtful", "default", "angry", "default")
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little girl...", "angry", "default", "sad", "talk")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna
                with d3
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                g4 "Argh! YES!"
                call luna_main("ugh... pathetic...", "seductive", "right", "mad", "default")
                call luna_main("...", "angry", "right", "angry", "angry")
                call luna_main("......", "mad", "down", "raised", "default")
                call luna_main(".........", "doubtful", "right", "mad", "default")
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, that's enough now [luna_name]."
                call luna_main("Who says you get to decide when this ends?", "doubtful", "right", "angry", "angry")
                ">Luna starts rolling her hips, focusing on the head of your cock."
                g11 "ah, please, not after I just came."
                call luna_main("really?", "mad", "right", "raised", "default")
                call luna_main("But you sounded so sincere earlier when you were begging for this.", "seductive", "right", "sad", "talk")
                call luna_main("Surely you don't want it to end already?", "seductive", "right", "angry", "default")
                ">she pushes hard against your cock."
                g11 "ah..."
                call luna_main("That's it [l_genie_name], just keep enjoying yourself.", "mad", "down", "angry", "default")
                g11 "I can't, it's too sensitive..."
                call luna_main("I don't see how that's my problem.", "mad", "right", "sad", "default")
                ">She starts moving as fast as she can."
                g11 "{size=-2}ahhh...{/size}"
                call luna_main("come on [l_genie_name]...", "doubtful", "right", "angry", "default")
                g11 "{size=+4}aghhh!{/size}"
                call luna_main("shoot another filthy load...", "doubtful", "right", "mad", "default")
                g4 "{size=+4}*Argh!* It's too much!{/size}"
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "doubtful", "down", "mad", "default")
                ">You start shooting another load against the inside of your sodden cloak."
                hide screen luna
                with d3
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                g4 "Argh!"
                call luna_main("good boy...", "seductive", "right", "mad", "default")
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3
                call luna_main("*hmph* You nasty old [l_genie_name]!", "doubtful", "default", "angry", "default")
                m "ah..."
                call luna_main("Enjoy yourself a little too much did we?", "angry", "right", "mad", "default")
                m "That was too much [luna_name]..."
                call luna_main("Stop complaining. I was just making sure that I earned my reward.", "mad", "default", "angry", "default")
                call luna_main("Speaking of which...", "seductive", "right", "default", "default")
                $ current_payout = 250


            "-Beg-" if luna_dom >= 3:
                if luna_dom <= 3:
                    $ luna_dom += 1
                m "can you please sit on my lap [luna_name]?"
                call luna_main("...", "seductive", "right", "default", "default")
                call luna_main("......", "mad", "right", "angry", "default")
                call luna_main("keep going...", "doubtful", "right", "default", "default")
                m "please place your perfect little ass on my lap princess..."
                call luna_main("that's better...", "doubtful", "right", "default", "default")
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", "seductive", "down", "angry", "default")
                call luna_main("that's it [l_genie_name]...", "seductive", "right", "default", "default")
                call luna_main("just sit back and enjoy yourself...", "seductive", "right", "default", "default")
                call luna_main("enjoy the feeling of your disgusting old cock rub against me...", "doubtful", "down", "angry", "default")
                ">Luna stands moving her hips backward and forwards..."
                m "ah..."
                call luna_main("*hmph* that's it... tell me how good it feels.", "seductive", "down", "angry", "talk")
                m "w-what?"
                call luna_main("tell me how good it feels to rub that filthy cock of your against me...", "mad", "right", "angry", "default")
                m "..."
                call luna_main("go on... or else.", "seductive", "right", "angry", "default")
                ">Luna goes to stand up slowly."
                m "alright... I'll do it."
                ">Luna sits back down onto your lap"
                call luna_main("good boy...", "seductive", "right", "default", "default")
                m "it's like I'm rubbing up against a ...cloud..."
                call luna_main("a cloud?", "seductive", "right", "raised", "angry")
                m "I mean it's soft..."
                ">Luna slowly grinds against your shaft."
                call luna_main("I suppose that's better than nothing.", "angry", "right", "raised", "default")
                m "mmmm, keep going [luna_name]..."
                call luna_main("pervert...", "doubtful", "right", "mad", "default")
                m "yes..."
                call luna_main("do you even know old I am?", "angry", "right", "angry", "default")
                m "of course..."
                call luna_main("well...", "mad", "right", "angry", "default")
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah... 18?"
                call luna_main("{size=-5}18?{/size} you don't sound so sure about that [l_genie_name]...", "seductive", "down", "mad", "default")
                m "..."
                call luna_main("what if I'm 17?", "doubtful", "right", "sad", "default")
                m "mmm..."
                call luna_main("I bet that'd just make you harder wouldn't it?", "seductive", "right", "default", "upset")
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", "doubtful", "default", "angry", "default")
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little girl...", "angry", "default", "sad", "talk")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
                hide screen luna
                with d3
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                g4 "Argh... YES!"
                call luna_main("ugh... pathetic...", "seductive", "right", "mad", "default")
                call luna_main("...", "angry", "right", "angry", "angry")
                call luna_main("......", "mad", "down", "raised", "default")
                call luna_main(".........", "doubtful", "right", "mad", "default")
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, no more please [luna_name]."
                call luna_main("good boy...", "seductive", "right", "mad", "default")
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3
                call luna_main("*hmph* You're such nasty old [l_genie_name]!", "doubtful", "default", "angry", "default")
                call luna_main("But I suppose I don't mind, as long as I get my reward.", "mad", "default", "angry", "default")
                call luna_main("Speaking of which...", "seductive", "right", "default", "default")
                $ current_payout = 250


        if luna_dom >= luna_sub:
            m "Alright, alright. Here's your gold."
        else:
            m "Here's your payment [luna_name]."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        if current_payout <= 50:
            call luna_main("(only [current_payout]?) *hmph*", "mad", "right", "angry", "angry")
            call luna_main("Thank you, [l_genie_name].", "doubtful", "right", "angry", "upset")
        else:
            call luna_main("Thank you, [l_genie_name].", "seductive", "right", "default", "default")
        ">Luna leaves your office."

    else: #Hermione involved
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        m "Can I offer you another seat [luna_name]?"
        call luna_main("so you want another lapdance...", "seductive", "default", "angry", "upset")
        m "if it's not too much trouble..."
        call luna_main("not at all...", "seductive", "right", "default", "default")
        call luna_main("but just for fun... why don't you get hermione up here?", "angry", "down", "sad", "default")
        m "really?"
        call luna_main("...", "angry", "default", "angry", "upset")
        m "Alright, I'm not going to say no to that!"
        call luna_main("good... let me just get in position first...", "seductive", "default", "angry", "default")
        show screen blkfade
        with d3
        ">Luna walks around the desk and stands in front of you."
        #chibi stuff
        $ luna_flip = -1
        $ luna_xpos = 120
        $ luna_chibi_xpos = 300
        hide screen blkfade
        with d3
        ">Luna lightly sits on your lap."
        m "mmmm"
        ">You start to feel yourself get hard against her ass"
        call luna_main("go on... bring her up here...", "mad", "right", "angry", "angry")
        ">you summon hermione up to your office."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ hermione_SC.chibi.xpos = 600 #Near the desk.
        show screen hermione_blink #Hermione stands still.
        call update_her_uniform
        pause
        call her_main("hello Professor!","base","closed")
        call her_main("hey luna! oh, has he got you on lapdance duty today then?","smile","happyCl",emote="06")
        call luna_main("if you can even call it that...", "seductive", "right", "angry", "upset")
        call luna_main("most of the time he just makes me grind up against him while he creams his robe...", "default", "down", "default", "default")
        call luna_main("I feel bad for the elves who have to clean it up...", "mad", "down", "angry", "default")
        ">Luna starts bouncing slowly on your lap, lifting her weight on and off your crouch."
        call her_main("mmm, so what am I here for then?","base","glance")
        m "ah... ask luna..."
        call luna_main("well I was thinking you could give him a little show while I grind a load out of him...", "wide", "right", "sad", "upset")
        call her_main("mmmm, what did you have in mind?","base","suspicious")
        call luna_main("Playing with those nice tits of your would probably do it...", "default", "right", "sad", "default")
        m "ah... yes..."
        call her_main("probably...","base","down")
        call her_main("but are you sure it's just him who wants a show?","base","suspicious")
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
        call luna_main("what?", "wide", "default", "sad", "open")
        ">Luna starts grinding even faster."
        call luna_main("what are you talking about?", "wide", "down", "sad", "upset")
        call her_main("from the looks of it you don't need any help cranking a nice big load out of [genie_name]...","open","down")
        call her_main("so the only reason you'd bring me up here to show of my tits...","base","glance")
        call her_main("is so you can get a look as well...","base","suspicious")
        call her_main("not that I mind...","smile","baseL")
        call her_main("I just want you to be honest...","base","squint")
        call luna_main("...", "mad", "right", "sad", "upset")
        call luna_main("Fine...", "mad", "down", "sad", "angry")
        call her_main("say it...","base","suspicious")
        call luna_main("I want to look at your boobs alright!", "closed_happy", "default", "sad", "open")
        ">hermione quickly removes her top and bra."
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call update_her_uniform
        call her_main("see, that's not so hard now is it?","base","suspicious")
        call luna_main("no...", "seductive", "default", "sad", "default")
        ">Luna slows down, but starts grinding her mound hard against your cock."
        call her_main("now why don't you too perverts just sit back and relax...","base","down")
        call h_action("lift_breasts")
        call her_main("while I give you something fun to look at ok?","grin","baseL")
        call luna_main("yes hermione...", "default", "default", "sad", "default")
        m "Yes..."
        call luna_main("mmmmm, he's so hard...", "seductive", "down", "sad", "default")
        call h_action("pinch")
        call her_main("I can imagine","grin","dead")
        m "ugh..."
        call luna_main("he's probably going to cum soon...", "mad", "right", "sad", "default")
        m "probably..."
        call her_main("and what about you?","base","glance")
        call h_action("covering")
        call her_main("how do you feel?","base","down")
        call luna_main("so good...", "seductive", "down", "sad", "default")
        call luna_main("...", "mad", "up", "sad", "default")
        ">luna tilts her hips back, grinding as much of her sex against you as possible..."
        ">you swear you can feel her wetness seeping through your robe."
        m "ah..."
        call h_action("pinch")
        call her_main("good...","open","baseL")
        call luna_main("ah...", "angry", "up", "sad", "default")
        ">Luna starts rubbing hard against your lap."
        m "{size=-2}(mmmm...){/size}"
        call luna_main("yes...", "seductive", "up", "sad", "default")
        call h_action("lift_breasts")
        call her_main("why don't you two see if you can cum together?","base","glance")
        g4 "{size=+4}agh... almost there...{/size}"
        call luna_main("m-me too...", "seductive", "up", "sad", "default")
        call h_action("pinch")
        call her_main("cum for me you nasty perverts!","base","suspicious")
        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
        call luna_main("ah...{image=textheart}{image=textheart}{image=textheart}", "angry", "up", "sad", "open")
        ">You start shooting your load against the inside of your cloak as you feel an explosion of wetness from luna's pussy."
        hide screen luna
        with d3
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "Argh! YES!"
        call luna_main("ugh... amazing...", "seductive", "up", "sad", "default")
        call h_action("covering")
        call her_main("mmmm...","base","glance")
        call luna_main("...", "seductive", "up", "sad", "default")
        call luna_main("......", "angry", "down", "sad", "default")
        call luna_main(".........", "seductive", "right", "sad", "default")
        ">Luna slowly keeps rolling her sensitive pussy on your cock..."
        g4 "ugh, that's enough now [luna_name]."
        call luna_main("alright...", "default", "down", "sad", "upset")
        ">Luna stands up from your lap"
        $ luna_flip = 1
        $ luna_xpos = 600
        $ luna_chibi_xpos = 500
        hide screen blkfade
        with d3
        $ hermione_wear_top = True
        $ hermione_wear_bra = True
        call update_her_uniform
        call h_action("none")
        call her_main("feel better you two?","base","glance")
        call luna_main("yes...", "mad", "up", "sad", "default")
        m "ah... you sluts..."
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png"
        call her_main("well come on then luna, we've got some studying to do. Can you pay us now [genie_name]?","base","down")


        m "Alright, alright. Here's your gold and points."
        $ gryffindor += 25
        $ ravenclaw += 25
        m "15 points to \"gryffindor\" and \"ravenclaw\"."
        $ gold -= 80
        $ luna_gold += 40
        m "and here's your gold."
        ">You hand Luna and hermione 40 gold each."
        call her_main("Thank you [genie_name]!","base","base")
        call luna_main("...Thank you sir.", "seductive", "right", "sad", "upset")
        ">Luna and hermione leave your office, talking as they go."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen luna
        hide screen luna_chibi
        $ luna_busy = True
        hide screen genie_jerking_sperm_02
        jump end_hg_pf

    hide screen genie_jerking_sperm_02
    jump luna_away



label luna_favour_3: #STRIP FOR ME - Have this as one favour with three options for each path.
    if luna_corruption <= 8:
        $ luna_corruption += 1
    if luna_corruption >= 13:
        m "how do you feel about stripping?"
        call luna_main("really?", "angry", "default", "angry", "upset")
        call luna_main("Aren't we a little past that?", "mad", "default", "raised", "upset")
        m "What would you rather do then?"
        call luna_main("...", "seductive", "right", "angry", "upset")
        call luna_main("how about another blowjob?", "seductive", "default", "angry", "default")
        m "well then..."
        jump luna_favour_6
    call play_music("chipper_doodle")
    if luna_corruption < 8:
        if luna_sub > luna_dom and luna_corruption < 5:
            m "Have you ever been naked in front of another person [luna_name]?"
            call luna_main("What?", "default", "down", "sad", "upset")
            call luna_main("Well... um... not really, I suppose.", "default", "right", "sad", "upset")
            m "Well then there's a first time for everything!"
            call luna_main("...", "default", "down", "sad", "angry")
        elif luna_sub > luna_dom :
            m "How would you like to step out of those restrictive clothes [luna_name]?"
            call luna_main("...", "default", "down", "sad", "upset")
            call luna_main("Well... {size=-3}they're{/size} {size=-4}not{/size} {size=-5}really{/size} {size=-6}that{/size} {size=-7}restrictive.{/size}", "default", "right", "sad", "upset")
            m "..."
            call luna_main("alright then [l_genie_name]...", "default", "down", "sad", "angry")
            hide screen luna
            with d3
            $ luna_xpos = 270
            ">Luna positions herself directly in front of your desk."
            call luna_main("...", "default", "right", "sad", "angry")
        else:
            m "You don't mind taking some of your clothes of do you [luna_name]?"
            call luna_main("I suppose not...", "default", "right", "angry", "upset")
            call luna_main("So long as your prepared to show some {i}appreciation...{/i}", "angry", "default", "angry", "upset")
            m "yes, [luna_name]..."
            call luna_main("...pervert...", "angry", "right", "angry", "upset")
            hide screen luna
            with d3
            $ luna_xpos = 270
            ">Luna positions herself directly in front of your desk."
            call luna_main("...", "angry", "right", "angry", "upset")
        menu:
            "\"Take off your skirt.\"" if luna_sub >= 5:
                $ luna_choice = 1
                call luna_main("you want me to take of my skirt!", "wide", "default", "sad", "pout")
                m "Yes... You think you could manage that?"
                call luna_main("of course I can manag-", "angry", "right", "sad", "upset")
                m "Fantastic! Why don't you pop it off then so we can take a look..."
                call luna_main("...", "closed", "down", "sad", "upset")
                call luna_main("Fine... (I hope he doesn't expect me to take off my panties as well)", "angry", "down", "sad", "pout")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">Luna slowly starts to unzip her skirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the zipper is undone and she has no choice but to take the skirt off..."
                ">Luna slowly steps out of her skirt and places it on your desk."
                show screen luna
                hide screen blkfade
                with d3
                call luna_main("There... are you happy now [l_genie_name]?", "mad", "down", "sad", "angry")
                m "Almost... take off your shirt next."
                call luna_main("...alright...", "doubtful", "right", "sad", "furious")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_top = False
                ">Luna starts to unbutton her shirt..."
                ">She slowly fumbles with the buttons until Finally the last button is undone..."
                ">Luna begrudgingly takes off her shirt and places it on top of her skirt."
                show screen luna
                hide screen blkfade
                with d3

            "\"Take off your shirt.\"" if luna_sub > luna_dom:
                $ luna_choice = 2
                call luna_main("my shirt?", "angry", "default", "sad", "upset")
                m "Did I stutter [luna_name]?"
                call luna_main("no...", "mad", "right", "sad", "upset")
                m "well Why don't you take it off then so we can take a look..."
                call luna_main("...", "doubtful", "down", "sad", "angry")
                call luna_main("Fine... (I hope he doesn't expect me to take off my bra as well)", "angry", "right", "sad", "upset")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_top = False
                ">Luna starts to unbutton her shirt..."
                ">She slowly fumbles with the buttons until Finally the last button is undone..."
                ">Luna begrudgingly takes off her shirt and places it on top of your desk."
                show screen luna
                hide screen blkfade
                with d3
                pause
                call luna_main("There... are you happy now [l_genie_name]?", "doubtful", "default", "sad", "upset")
                m "Almost... take off your skirt next."
                call luna_main("...fine...", "angry", "right", "sad", "upset")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">Luna slowly starts to unzip her skirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the zipper is undone and she has no choice but to take the skirt off..."
                ">Luna slowly steps out of her skirt and places it on top of her shirt."
                show screen luna
                hide screen blkfade
                with d3

            "\"Please take off your shirt.\"" if luna_dom >= luna_sub:
                $ luna_choice = 3
                call luna_main("...", "seductive", "right", "default", "default")
                call luna_main("......", "mad", "right", "angry", "default")
                call luna_main("well seeing as how you said the magic word I suppose it's only fair...", "doubtful", "right", "default", "default")
                m "thank you [luna_name]."
                call luna_main("(Who'd have thought it'd be the easy...)", "angry", "right", "default", "default")
                call luna_main("close your eyes...", "mad", "default", "angry", "upset")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_top = False
                ">you can hear the soft ruffle of clothes being removed..."
                ">You hear her softly place her shirt and vest on the table..."
                m "..."
                m "Can I open my eyes yet [luna_name]?"
                lun "just a second..."
                lun "Alright, go ahead."
                show screen luna
                hide screen blkfade
                with d3
                pause

            "\"Please take off your skirt [luna_name]...\"" if luna_dom >= 5:
                $ luna_choice = 4
                call luna_main("...", "seductive", "right", "default", "default")
                call luna_main("......", "mad", "right", "angry", "default")
                call luna_main("well seeing as how you said the magic word I suppose it's only fair...", "doubtful", "right", "default", "default")
                m "thank you [luna_name]."
                call luna_main("(Who'd have thought it'd be the easy...)", "angry", "right", "default", "default")
                call luna_main("well... close your eyes...", "angry", "default", "angry", "upset")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">you can hear the soft ruffle of clothes and zips..."
                ">You hear her softly place her skirt on the table..."
                m "..."
                m "Can I open my eyes yet [luna_name]?"
                lun "just a second..."
                lun "Alright, go ahead."
                show screen luna
                hide screen blkfade
                with d3
                pause

        if luna_choice <= 2: #luna sub choices
            if luna_sub <= 5:
                $ luna_sub += 1
            m "Good... now your underwear..."
            call luna_main("!!!", "wide", "default", "sad", "upset")
            call luna_main("You're not serious are you?", "angry", "right", "sad", "upset")
            m "I am. And I expect you to do it now, [luna_name]."
            call luna_main("[l_genie_name]!", "mad", "default", "mad", "angry")
            m "don't you raise your voice at me, [luna_name]!"
            call luna_main(".....!!?", "angry", "right", "sad", "upset")
            m "Nobody is forcing you to do this."
            call luna_main("but-", "seductive", "right", "sad", "upset")
            m "I am doing you and your family a favour!"
            m "so If you don't think your father needs help with his failing magazine, please feel free to leave."
            call luna_main(".....................", "doubtful", "right", "sad", "angry")
            call luna_main(".......................................", "angry", "down", "sad", "upset")
            $ luna_tears = 1
            call luna_main("please [l_genie_name]...", "mad", "default", "sad", "upset")
            call luna_main("isn't there anything else I can do...", "doubtful", "right", "sad", "upset")
            menu:
                "-Make her strip-" if luna_choice == 1:
                    $ current_payout = 40
                    m "Take off your underwear now [luna_name]..."
                    call luna_main("{size=-5}(Should I really do this?){/size}", "doubtful", "down", "sad", "upset")
                    call luna_main("[l_genie_name] I don't know about this... ", "mad", "default", "sad", "upset")
                    if daytime:
                        m "Come on [luna_name], just a little peek and then you'll be off to class."
                    else:
                        m "Come on [luna_name], just a little peek and then you'll be off to bed."
                    call luna_main("Alright [l_genie_name]... ", "doubtful", "down", "sad", "upset")
                    call luna_main("(Stripping for the headmaster...)", "doubtful", "right", "sad", "upset")
                    call luna_main("(imagine if daddy found out...)", "doubtful", "down", "sad", "upset")
                    call luna_main("......", "doubtful", "default", "sad", "upset")
                    hide screen luna
                    show screen blkfade
                    with d3
                    $ luna_wear_bra = False
                    ">Luna slowly unlatches her bra and places it on your desk."
                    show screen luna
                    hide screen blkfade
                    with d3
                    m "Mmmm, very nice [luna_name]."
                    m "Now for your panties..."
                    $ luna_tears = 2
                    call luna_main("yes [l_genie_name]... ", "mad", "right", "sad", "angry")
                    hide screen luna
                    show screen blkfade
                    with d3
                    $ luna_wear_panties = False
                    ">Luna slightly turns to the side so you can't quite make out her crouch..."
                    ">She's very hesitant and takes her time pulling down her panties..."
                    ">Luna slowly steps out of her panties and places them on top of the pile of clothes on your desk."
                    show screen luna
                    hide screen blkfade
                    with d3
                    pause
                    call luna_main("...", "doubtful", "down", "sad", "angry")
                    m "Very nice..."
                    call luna_main("c-can I get dressed now... it's a bit cold in here.", "doubtful", "right", "sad", "upset")
                    m "mmmm... so I can see."
                    call luna_main("!!!", "wide", "default", "angry", "angry")
                    call luna_main("That's enough! I refuse to stand here any longer!", "doubtful", "default", "mad", "upset")

                "-start touching yourself-":
                    $ current_payout = 65
                    m "anything..."
                    hide screen blktone
                    with d3
                    ">You reach under the desk and grab your cock..."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    pause
                    m "Is this better [luna_name]?"
                    call luna_main("{size=-3}I suppose so...{/size}", "doubtful", "down", "sad", "angry")
                    m "Well if it makes you happy..."
                    ">You start stroking faster."
                    call luna_main("...", "doubtful", "down", "sad", "angry")
                    m "Yes... Ah, yes, this is good..."
                    $ luna_tears = 3
                    call luna_main("Fine! Have it your way, [l_genie_name]!", "doubtful", "down", "sad", "angry")
                    call luna_main("enjoy stroking your filthy old cock while you force me stand here...", "doubtful", "default", "mad", "angry")
                    m "{size=-4}(mmmm... yes...){/size}"
                    m "well seeing as how you are standing there... why don't you give those nice little tits of yours a good shake?"
                    call luna_main("*hmph*...", "angry", "default", "angry", "upset")
                    ">Luna sways her chest side to side ever so slightly."
                    call luna_main("well...", "angry", "down", "mad", "upset")
                    ">You keep on wanking while you gaze at Luna's milky tits..."
                    m "just a little bit faster..."
                    call luna_main("*hmph*... just hurry up get it over with [l_genie_name]...", "doubtful", "down", "sad", "angry")
                    ">Luna starts shaking her chest a little faster"
                    m "{size=-4}ah...{/size}"
                    m "that's it slut... keep going..."
                    call luna_main("........", "mad", "default", "mad", "upset")
                    m "{size=-4}(argh... yes...){/size}"
                    call luna_main("(he's going to shoot it all out front of me...)", "angry", "down", "sad", "upset")
                    m "{size=-4}yes...{/size}"
                    call luna_main("(Should I stop.)", "doubtful", "right", "sad", "angry")
                    g4 "{size=+2}mmmm... thats it keep shaking those milky tits...{/size}"
                    call luna_main(".........", "seductive", "default", "sad", "default")
                    g4 "{size=+4}(agh... almost there...){/size}"
                    call luna_main("(too late...)", "doubtful", "down", "sad", "default")
                    g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                    hide screen luna
                    with d3
                    show screen white
                    pause.1
                    hide screen white
                    pause.2
                    show screen white
                    pause .1
                    hide screen white
                    with hpunch
                    g4 "Argh! YES!"
                    hide screen luna
                    with d3
                    hide screen bld1
                    with d3
                    show screen genie_jerking_sperm
                    with d3
                    show screen bld1
                    with d3
                    call luna_main("ugh... there's so much...", "mad", "down", "sad", "upset")
                    call luna_main("{size=-5}(As usual...){/size}", "mad", "right", "sad", "default")
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "good work, slut... ah, shit, this feels so good..."
                    show screen genie
                    hide screen bld1
                    #show screen genie_jerking_off
                    with d3
                    call luna_main("......", "angry", "default", "sad", "upset")
                    m "Ah... you did good [luna_name]..."

            hide screen luna
            show screen blkfade
            with d3
            $ luna_wear_skirt = True
            $ luna_wear_top = True
            $ luna_wear_bra = True
            $ luna_wear_panties = True
            ">Luna quickly picks her clothes up off your desk and gets dressed."
            show screen luna
            hide screen blkfade
            with d3
            call luna_main("I think I'd like to leave now [l_genie_name]...", "angry", "down", "sad", "upset")
            m "You're free to leave whenever you like [luna_name]."
            call luna_main("Well I'm certainly not leaving until you pay me!", "doubtful", "default", "angry", "angry")


        else:
            call luna_main("There... is this what you wanted to see [l_genie_name]?", "angry", "default", "angry", "upset")
            g4 "gods yes!"
            if luna_dom <= 5:
                $ luna_dom += 1
            call luna_main("well... seeing as how you seem to be enjoying yourself so much...", "seductive", "default", "angry", "default")
            m "what?"
            call luna_main("why don't you start ...touching... yourself [l_genie_name]...", "seductive", "down", "angry", "default")
            m "I'm not sure if-"
            call luna_main("that wasn't a question [l_genie_name]...", "mad", "default", "angry", "upset")
            hide screen blktone
            with d3
            ">You reach under the desk and grab your cock..."
            hide screen blktone8
            with d3
            hide screen genie
            show screen genie_jerking_off
            with d3
            pause
            call luna_main("there we are...", "mad", "default", "sad", "default")
            call luna_main("don't you feel better now?", "mad", "right", "sad", "default")
            m "mmmm... yes..."
            call luna_main("Hmmm, I'm not sure if I believe you.", "doubtful", "default", "sad", "angry")
            call luna_main("maybe you need a little encouragement...", "doubtful", "right", "sad", "default")
            m "encouragement?"
            call luna_main("close your eyes [l_genie_name]...", "doubtful", "default", "sad", "default")
            hide screen luna
            show screen blkfade
            with d3
            $ luna_chibi("stand_naked")
            if luna_wear_top:
                $ luna_wear_panties = False
            else:
                $ luna_wear_bra = False
            ">you can hear the soft ruffle of clothes being taken off..."
            ">You feel something light get thrown against your chest..."
            m "???"
            m "Can I open my eyes yet [luna_name]?"
            lun "Go ahead [l_genie_name]..."
            show screen luna
            hide screen blkfade
            with d3
            g9 "!!!"
            call luna_main("like what you see?", "doubtful", "right", "sad", "default")
            g9 "..."
            ">You start stroking your cock with renewed vigor."
            call luna_main("I'll take that as a yes...", "mad", "default", "angry", "default")
            g9 "Aha... Yeah... This feels great..."
            call luna_main("good... just work up a nice big load for me...", "doubtful", "default", "angry", "default")
            if luna_wear_panties:
                call luna_main("if you're a good boy I might even let you shoot it all over my bra...", "mad", "right", "angry", "default")
            else:
                call luna_main("if you're a good boy I might even let you shoot it all over my panties...", "mad", "right", "angry", "default")
            g9 "Yes, [luna_name]!"
            call luna_main("I bet you'd love that wouldn't you?", "angry", "default", "angry", "default")
            m "yes..."
            call luna_main("Shooting your filthy old cum all over my underwear...", "mad", "down", "sad", "default")
            m "..."
            call luna_main("well come on then [l_genie_name]...", "doubtful", "default", "sad", "default")
            call luna_main("keep stroking that disgusting cock of yours...", "doubtful", "default", "angry", "default")
            m "{size=-4}(argh... yes...){/size}"
            call luna_main("do you need a little more encouragement [l_genie_name]...", "mad", "default", "mad", "default")
            m "{size=-4}yes...{/size}"
            call luna_main("say it louder...", "mad", "default", "mad", "default")
            g9 "{size=+4}yes{/size}"
            call luna_main("well close your eyes...", "doubtful", "default", "mad", "default")
            hide screen luna
            show screen blkfade
            with d3
            if luna_wear_panties:
                $ luna_wear_skirt = False
            else:
                $ luna_wear_top = False
            ">you can once more hear the soft ruffle of clothes..."
            m "{size=-2}(mmmm...){/size}"
            lun "open wide [l_genie_name]..."
            show screen luna
            hide screen blkfade
            with d3
            pause
            m "{size=+2}yes...{/size}"
            call luna_main("you love this don't you...", "doubtful", "default", "angry", "default")
            g4 "{size=+4}(agh...){/size}"
            ">you start stroking your cock even faster!"
            g4 "{size=+4}yes...{/size}"
            call luna_main("that's it [l_genie_name], cum for your princess...", "doubtful", "default", "sad", "default")
            g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
            g4 "{size=+4}(agh... almost there...){/size}"
            call luna_main("cum...", "angry", "default", "mad", "talk")
            if luna_wear_panties:
                call luna_main("{size=+4}cum all over my bra!{/size}", "angry", "default", "mad", "talk")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You grab Luna's bra and start stroking your cock into it."
            else:
                call luna_main("{size=+4}cum all over my panties!{/size}", "angry", "default", "mad", "talk")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You grab Luna's panties and start stroking your cock into them."
            hide screen luna
            with d3
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            g4 "Argh! YES!"
            hide screen luna
            with d3
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            show screen bld1
            with d3
            call luna_main("That's it, [l_genie_name], make sure you cover them...", "doubtful", "default", "mad", "default")
            show screen genie_jerking_sperm_02
            with d3
            g4 "ah, shit they're so soft, why does this feels so good..."
            show screen genie
            hide screen bld1
            #show screen genie_jerking_off
            with d3
            call luna_main("mmm...", "mad", "default", "mad", "default")
            m "ah..."
            call luna_main("keep going... make sure you get every last drop out.", "mad", "down", "sad", "default")
            m "ah... Thank you..."
            call luna_main("Thank you...?", "doubtful", "default", "raised", "angry")
            m "Thank you princess..."
            $ luna_name = "Princess"
            call luna_main("*hmph*", "doubtful", "right", "angry", "upset")
            call luna_main("Well seeing as how you've ...finished... I suppose I better get dressed.", "angry", "right", "angry", "upset")

            hide screen luna
            with d3

            if luna_wear_panties:
                ">Luna quickly picks her clothes up off your desk and gets dressed except for her cum covered bra."
            else:
                ">Luna quickly picks her clothes up off your desk and gets dressed except for her cum covered panties."
            $ luna_wear_skirt = True
            $ luna_wear_top = True
            $ luna_wear_bra = True
            $ luna_wear_panties = True
            show screen luna
            with d3
            m "aren't you going to put those on as well?"
            call luna_main("What? and risk contaminating the evidence?", "doubtful", "default", "raised", "angry")
            m "Evidence..."
            call luna_main("Oh don't worry, I just needed some ...insurance...", "angry", "right", "sad", "default")
            m "insurance? Against what?"
            call luna_main("well if I tried to tell the ministry of magic what was going on here I'd get laughed out of the room.", "mad", "default", "raised", "default")
            call luna_main("but this?", "angry", "default", "angry", "default")
            ">She dangles the cum soaked underwear in front of you."
            call luna_main("This says otherwise.", "angry", "down", "angry", "default")
            m "How will they know it's mine? That could be anyone's cum!"
            call luna_main("Please... we're taught identification spells in second year. even neville longbottom would know it's yours.", "doubtful", "default", "mad", "default")
            m "(Shit, if she actually tries that she might work out I'm not really Dumblefore or whatever his name is...)"
            m "So you're going to tell them everything?"
            call luna_main("What? of course not.", "doubtful", "right", "default", "default")
            call luna_main("As long as you behave yourself...", "doubtful", "default", "default", "default")
            m "And what does that entail?"
            call luna_main("Well first things first we're going to talk about how much I'm going to be paid.", "doubtful", "right", "default", "default")
            call luna_main("300 gold sounds fair to me... {p}how about you?", "doubtful", "default", "angry", "default")
            m "It sounds... fair..."
            call luna_main("I'm glad we could come to an agreement.", "mad", "right", "sad", "default")
            m "yes [luna_name]..."
            call luna_main("Good boy... now, speaking of payment...", "doubtful", "default", "angry", "upset")
            $ current_payout = 300


    else: ###THIRD TIME EVENT IS RUN
        if luna_sub > luna_dom :
            m "You don't mind taking your clothes off again, do you, [luna_name]?"
            call luna_main("...", "default", "right", "sad", "upset")
            call luna_main("Well... {size=-3}I {size=-4}mean {size=-2}I {size=-2}do {size=-2}mind.", "default", "down", "sad", "upset")
            m "..."
            call luna_main("...", "default", "default", "sad", "upset")
            call luna_main("alright then, [l_genie_name]...", "default", "right", "sad", "default")
            hide screen luna
            with d3
            $ luna_xpos = 270
            ">Luna positions herself directly in front of your desk."
            call luna_main("(Why can't I stand up for myself?)", "default", "right", "sad", "angry")
            call luna_main("...", "default", "down", "sad", "pout")
        else:
            m "If it's not too much trouble-"
            call luna_main("...", "default", "right", "angry", "upset")
            m "Could you please take your clothes off?"
            call luna_main("*hmph* {p}Well seeing as how you seemed to have learned some manners.", "angry", "default", "angry", "upset")
            m "yes, [luna_name]..."
            call luna_main("I suppose there's no harm in it...", "seductive", "right", "angry", "default")
            hide screen luna
            with d3
            $ luna_xpos = 270
            ">Luna positions herself directly in front of your desk."
            call luna_main("...", "doubtful", "default", "angry", "default")
        menu:
            "\"Take off your skirt.\"" if luna_sub >= 5:
                $ luna_choice = 1
                call luna_main("My skirt?", "wide", "default", "sad", "pout")
                m "Yes..."
                call luna_main("...", "angry", "right", "sad", "upset")
                call luna_main(".......", "angry", "right", "sad", "upset")
                call luna_main("{size=-7}Alright...{/size}", "angry", "right", "sad", "default")
                m "Mmmm, someone's eager today."
                call luna_main("[l_genie_name]...", "closed", "down", "sad", "upset")
                call luna_main("...", "default", "right", "sad", "default")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">Luna slowly starts to unzip her skirt..."
                ">She doesn't hesitate however, quickly placing the skirt on your desk..."
                show screen luna
                hide screen blkfade
                with d3
                call luna_main("There... Is that all [l_genie_name]?", "mad", "right", "sad", "angry")
                m "Not quite..."
                call luna_main("(Surely he doesn't want me to take off my panties?)", "doubtful", "right", "angry", "angry")
                call luna_main("[l_genie_name] please...", "angry", "default", "sad", "upset")
                m "Now now, [luna_name], a deal's a deal..."
                call luna_main("...", "doubtful", "right", "sad", "angry")
                $ luna_tears = 1
                call luna_main("At least close your eyes...", "angry", "default", "sad", "upset")
                m "As you wi- {p}command..."
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_panties = False
                ">You hear the soft rustle of clothes..."
                ">Suddenly something is gently placed on your desk"
                show screen luna
                hide screen blkfade
                with d3
                call luna_main("There... are you happy now!", "seductive", "right", "angry", "upset")
                g9 "Of course!"
                g9 "I only expected you to take your shirt off!"
                call luna_main("What!", "wide", "default", "angry", "open")
                call luna_main("Please! let me put them back on!", "wide", "default", "sad", "upset")
                ">Luna scrambles to pick her panties back up off your desk but you're too fast for her, quickly snatching them up."
                m "Ah ah ah, Miss Lovegood."
                call luna_main("You're so... You're so mean!", "mad", "right", "sad", "upset")
                m "Don't complain too much, I was hoping you'd take those off anyway."
                call luna_main("*hmph*", "doubtful", "default", "default", "angry")
                m "Well, seeing as how we've already crossed this line, how about you take off your top anyway."
                call luna_main("You can't be serious! I think you've seen enough [l_genie_name]!", "angry", "default", "angry", "angry")

            "\"Take off your shirt.\"" if luna_sub > luna_dom:
                $ luna_choice = 2
                call luna_main("my shirt?", "angry", "default", "sad", "upset")
                m "That's not too much is it [luna_name]?"
                call luna_main("no...", "mad", "right", "sad", "upset")
                m "..."
                call luna_main("...", "doubtful", "down", "sad", "angry")
                call luna_main("ugh, Fine... (I hope he doesn't expect me to take off my bra as well)", "angry", "right", "sad", "upset")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_top = False
                ">Luna starts to unbutton her shirt..."
                ">She gently undoes the buttons, letting it slide off her shoulders before placing it on your desk."
                show screen luna
                hide screen blkfade
                with d3
                pause
                call luna_main("There... is that all [l_genie_name]?", "doubtful", "default", "sad", "upset")
                m "Almost... take off your bra next."
                call luna_main("[l_genie_name], I really don't-", "angry", "right", "sad", "upset")
                m "[luna_name]..."
                call luna_main("...{p}fine...", "angry", "right", "sad", "default")
                call luna_main("But you have to close your eyes.", "angry", "default", "sad", "upset")
                m "done."
                call luna_main("...", "doubtful", "down", "sad", "default")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_bra = False
                ">You hear the soft rustle of clothes..."
                ">You can hear something being placed softly onto your desk"
                show screen luna
                hide screen blkfade
                with d3
                m "Very nice..."
                m "Now your skirt."
                call luna_main("You can't be serious! I think you've seen enough [l_genie_name]!", "angry", "default", "angry", "angry")


            "\"Please take off your shirt.\"" if luna_dom >= luna_sub:
                $ luna_choice = 3
                call luna_main("...", "seductive", "right", "default", "default")
                call luna_main("......", "mad", "right", "angry", "default")
                call luna_main("well seeing as how you asked so {i}nicely{/i}...", "doubtful", "default", "default", "default")
                m "thank you [luna_name]."
                call luna_main("(I can't believe people think that this is the greatest wizard ever...)", "angry", "right", "default", "default")
                call luna_main("close your eyes...", "mad", "default", "angry", "default")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_panties = False
                $ luna_wear_bra = False
                $ luna_wear_skirt = False
                $ luna_wear_top = False
                ">you can hear the soft ruffle of clothes being removed..."
                m "..."
                m "Can I open my eyes yet [luna_name]?"
                lun "you can open then when I tell you..."
                ">You hear her softly place something on the table..."
                lun "..."
                m "..."
                lun "Alright, go ahead."
                show screen luna
                hide screen blkfade
                with d3

            "\"Please take off your skirt [luna_name]...\"" if luna_dom >= 5:
                $ luna_choice = 4
                call luna_main("...", "seductive", "right", "default", "default")
                call luna_main("......", "mad", "right", "angry", "default")
                call luna_main("well seeing as how you said the magic word I suppose it's only fair...", "doubtful", "default", "default", "default")
                m "thank you [luna_name]."
                call luna_main("(I've got him wrapped around my finger...)", "angry", "right", "default", "default")
                call luna_main("well... close your eyes...", "angry", "default", "angry", "upset")
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_panties = False
                $ luna_wear_bra = False
                $ luna_wear_skirt = False
                $ luna_wear_top = False
                ">you can hear the soft ruffle of clothes and zips..."
                m "..."
                m "Can I open my eyes yet [luna_name]?"
                lun "wait..."
                m "..."
                ">You hear her softly place something on the table..."
                lun "Alright, you can open them now..."
                show screen luna
                hide screen blkfade
                with d3

        if luna_choice <= 2: #luna sub choices
            if luna_sub <= 6:
                $ luna_sub += 1
            m "I am, and I expect you to do it now, [luna_name]."
            call luna_main("[l_genie_name]... please...", "seductive", "default", "sad", "upset")
            m "Hmmm, well seeing as how I'm in a generous mood, how about we make another deal?"
            call luna_main("...", "angry", "right", "sad", "upset")
            $ luna_tears = 0
            call luna_main("Really? What sort?", "angry", "right", "sad", "upset")
            m "what's the closest school to Howgsmorts?"
            call luna_main("?...{p}Um, probably Beauxbatons Academy of Magic, [l_genie_name]...", "seductive", "right", "sad", "upset")
            m "Well, how about I send a glowing letter of recommendation to them concerning your father's magazine?"
            m "I'm sure that will probably boost sales."
            call luna_main("Really sir? You'd do that?", "wide", "default", "default", "default")
            call luna_main("And all I have to do is stand here and...", "seductive", "right", "sad", "upset")
            if luna_wear_skirt == False:
                call luna_main("take off my top...", "angry", "down", "sad", "upset")
                m "and your bra."
            else:
                call luna_main("take off my skirt...", "angry", "down", "sad", "upset")
                m "and your panties."
            call luna_main("......", "mad", "default", "sad", "upset")
            call luna_main("..........", "doubtful", "right", "sad", "upset")
            call luna_main("Alright... but you have to close your eyes...", "doubtful", "default", "sad", "upset")
            m "Done."
            hide screen luna
            hide screen luna_chibi
            show screen blkfade
            with d3
            $ luna_wear_panties = False
            $ luna_wear_bra = False
            $ luna_wear_skirt = False
            $ luna_wear_top = False
            ">You hear the soft rustle of clothes..."
            ">Suddenly something is gently placed on your desk"
            $ luna_chibi("stand_naked")
            show screen luna
            show screen luna_chibi
            hide screen blkfade
            with d3
            call luna_main("......", "mad", "down", "sad", "upset")
            g9 "looking good, [luna_name]!"
            g9 "So good, in fact, I think I need a closer look!"
            ">You stand up and walk in front of luna, towering over her."
            hide screen bld1
            hide screen genie
            show screen chair_left
            show screen desk
            $ genie_chibi_xpos = -20
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "groping_ass_ani"
            show screen g_c_u
            with fade
            hide screen blktone
            hide screen blkfade
            with d5
            pause
            m "mmmm..."
            call luna_main("......", "mad", "right", "sad", "upset")
            menu:
                "-Grab her tits!-":
                    $ current_payout = 40
                    show screen blkfade
                    hide screen genie
                    $ genie_chibi_xpos = 40
                    $ genie_chibi_ypos = 10
                    $ g_c_u_pic = "groping_ass_ani"
                    show screen g_c_u
                    with fade
                    ">You reach out swiftly and grab both of her creamy tits..."
                    hide screen blkfade
                    call luna_main("!!!", "wide", "default", "mad", "angry")
                    ">YOu start gently kneading her breasts."
                    m "Mmmm... that's it, [luna_name]..."
                    call luna_main("{size=-5}(What is he doing?){/size}", "doubtful", "right", "sad", "upset")
                    call luna_main("[l_genie_name], you really have to stop... ", "mad", "default", "sad", "angry")
                    if daytime:
                        m "Come on [luna_name], just a little more, then you'll be off to class."
                    else:
                        m "Come on [luna_name], just a little more, then you'll be off to bed."
                    $ luna_tears = 2
                    call luna_main("[l_genie_name]... no...", "doubtful", "down", "sad", "upset")
                    call luna_main("(I should stop him...)", "doubtful", "right", "sad", "upset")
                    call luna_main("(before he gets too excited...)", "doubtful", "down", "sad", "upset")
                    ">Luna pushes you back."
                    call luna_main("......", "doubtful", "default", "sad", "upset")
                    ">You let her go and take a step back."
                    $ genie_chibi_xpos = 20
                    call luna_main("...", "doubtful", "down", "sad", "angry")
                    m "Sorry..."
                    call luna_main("It-it's alright [l_genie_name]...", "doubtful", "right", "sad", "upset")
                    call luna_main("You just got a little over-excited...", "doubtful", "down", "sad", "upset")
                    call luna_main("Just, please, try and control yourself next time...", "doubtful", "right", "sad", "default")
                    g9 "With tits like that, I'm not so sure!"
                    call luna_main("...", "doubtful", "right", "sad", "upset")


                "-start touching yourself-"if luna_choice == 1:
                    $ current_payout = 100
                    m "mmmm..."
                    call luna_main("......", "mad", "default", "sad", "upset")
                    hide screen blktone
                    show screen blkfade
                    with d3
                    ">You reach into your robe and pull out your cock..."
                    ">You spit on your hand to lube it before you start stroking..."
                    hide screen genie
                    $ genie_chibi_xpos = -20
                    $ genie_chibi_ypos = 10
                    $ g_c_u_pic = "jerking_off_02_ani"
                    show screen g_c_u
                    hide screen blkfade
                    with fade
                    call luna_main("!!!", "wide", "default", "mad", "angry")
                    call luna_main("(Am I just going to let him do this?)", "doubtful", "right", "angry", "angry")
                    call luna_main("Sir I really thin-", "mad", "default", "angry", "angry")
                    m "Shhhh..."
                    ">You start stroking faster."
                    call luna_main("...", "seductive", "right", "sad", "angry")
                    call luna_main("(I can't just let him...)", "doubtful", "down", "sad", "angry")
                    m "Yes... Ah, yes, this is good..."
                    $ luna_tears = 2
                    call luna_main("sir... please... don't...", "doubtful", "down", "sad", "angry")
                    m "I said \"shhhh\", [luna_name]..."
                    call luna_main("Sir... I-I'll leave if y-you don't stop...", "doubtful", "right", "sad", "angry")
                    m "If you leave, you can say goodbye to the squibbler, or whatever it's called."
                    call luna_main("(I can't do that to daddy...)", "angry", "down", "sad", "angry")
                    call luna_main("Fine! I hope you're happy!", "angry", "default", "sad", "angry")
                    call luna_main("enjoy stroking that filthy old cock while you force me to stand here...", "angry", "down", "sad", "angry")
                    g9 "{size=-4}(mmmm... yes...){/size}"
                    g9 "Oh I am!"
                    call luna_main("*hmph*...", "angry", "default", "angry", "upset")
                    ">Luna tosses her hair over her shoulder in frustration."
                    call luna_main("You're disgusting...", "angry", "down", "mad", "upset")
                    ">You keep on wanking while you gaze at Luna's milky tits..."
                    m "mmmm... that's it, [luna_name]..."
                    $ luna_tears = 3
                    call luna_main("*hmph*... just hurry up get it over with, [l_genie_name]...", "doubtful", "down", "sad", "angry")
                    call luna_main("I'm sick of looking at that... thing...", "angry", "right", "sad", "upset")
                    m "{size=-4}ah...{/size}"
                    m "that's it slut... keep looking..."
                    call luna_main("Professor!", "mad", "down", "angry", "upset")
                    m "{size=-4}(argh... yes...){/size}"
                    call luna_main("I really don't-", "seductive", "down", "sad", "upset")
                    m "{size=-4}yes...{/size}"
                    call luna_main("-think that-", "doubtful", "down", "sad", "angry")
                    g4 "{size=+2}mmmm... thats it keep going...{/size}"
                    call luna_main("-we should be-", "seductive", "down", "sad", "default")
                    g4 "{size=+4}(agh... almost there...){/size}"
                    call luna_main("doing thi-", "doubtful", "down", "sad", "default")
                    g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                    $ genie_cum_chibi_xpos = -20
                    $ genie_cum_chibi_ypos  = 10
                    $ g_c_c_u_pic = "genie_cum_03"
                    show screen g_c_c_u
                    $ luna_wear_cum = True
                    $ luna_cum = 5
                    hide screen luna
                    with d3
                    show screen white
                    pause.1
                    hide screen white
                    pause.2
                    show screen white
                    pause .1
                    hide screen white
                    with hpunch
                    g4 "Argh! YES!"
                    hide screen luna
                    with d3
                    hide screen bld1
                    with d3
                    show screen bld1
                    with d3
                    $ g_c_u_pic = "jerking_off_02_ani"
                    hide screen g_c_c_u
                    call luna_main("ugh... there's so much...", "mad", "down", "sad", "upset")
                    call luna_main("{size=-5}(I can't believe this...){/size}", "mad", "right", "sad", "upset")
                    call luna_main("ugh... {size=-5}(it stinks as well...){/size}", "mad", "down", "angry", "upset")
                    with d3
                    g4 "argh... good work, slut... ah, shit, this feels so good..."
                    show screen genie
                    hide screen bld1
                    hide screen g_c_u
                    #show screen genie_jerking_off
                    with d3
                    call luna_main("......", "angry", "default", "sad", "upset")
                    m "Ah... you did good, [luna_name]..."

            hide screen luna
            show screen blkfade
            with d3
            show screen genie
            hide screen g_c_u
            $ luna_wear_skirt = True
            $ luna_wear_top = True
            $ luna_wear_bra = True
            $ luna_wear_panties = True
            $ luna_cum = 2
            hide screen chair_left
            hide screen desk
            ">Luna quickly picks her clothes up off your desk and gets dressed, putting on her shirt over the cum."
            show screen luna
            hide screen blkfade
            with d3
            call luna_main("I think I'd like to leave now [l_genie_name]...", "angry", "down", "sad", "upset")
            m "You're free to leave whenever you like [luna_name]."
            call luna_main("Well I'm certainly not leaving until you pay me!", "doubtful", "default", "angry", "angry")


        else:
            call luna_main("...", "angry", "default", "default", "default")
            $ luna_chibi("stand_naked")
            pause
            g9 "mmmm"
            if luna_dom <= 5:
                $ luna_dom += 1
            call luna_main("Like what you see [l_genie_name]?", "seductive", "right", "default", "default")
            g9 "Yes... Yes..."
            call luna_main("well... why don't you come take a closer look?...", "seductive", "default", "angry", "default")
            m "what?"
            call luna_main("why don't you stand up and take a good look [l_genie_name]...", "mad", "default", "mad", "default")
            m "I don't think that-"
            call luna_main("shhh...", "angry", "default", "angry", "talk")
            call luna_main("just stand up sir.....", "angry", "default", "angry", "default")
            m "..."
            ">You stand up and walk in front of luna, feeling the pressure of her gaze."
            hide screen bld1
            hide screen genie
            show screen chair_left
            show screen desk
            $ genie_chibi_xpos = -20
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "images/animation/06_groping_01.png"
            show screen g_c_u
            with fade
            hide screen blktone
            hide screen blkfade
            with d5
            pause
            call luna_main("there we are...", "mad", "default", "sad", "default")
            call luna_main("Isn't that better?", "mad", "right", "sad", "default")
            m "mmmm... yes..."
            call luna_main("Hmmm, that's it just keep looking...", "mad", "right", "mad", "default")
            ">Luna gives her tits a little shake."
            g9 "!!!"
            call luna_main("See something you like?...", "doubtful", "right", "sad", "default")
            m "ah, gods yes..."
            call luna_main("mmmmm... why don't you take it out [l_genie_name]...", "doubtful", "default", "sad", "default")
            m "..."
            call luna_main("be a good boy....", "seductive", "default", "sad", "default")
            show screen blkfade
            ">You take your cock out and start stroking it..."
            hide screen genie
            $ genie_chibi_xpos = -20
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "jerking_off_02_ani"
            show screen g_c_u
            hide screen blkfade
            with fade
            call luna_main("that's it [l_genie_name]...", "doubtful", "default", "sad", "default")
            ">you stare at her soft milky tits..."
            m "Mmmm..."
            call luna_main("Mmmm, isn't that better?", "doubtful", "right", "sad", "default")
            g9 "yes..."
            ">You start stroking your cock with renewed vigor."
            call luna_main("Aren't you keen today?", "mad", "default", "angry", "default")
            g9 "Aha... Yeah... This really great..."
            call luna_main("good... make sure you work up a nice big load for me...", "doubtful", "default", "angry", "default")
            call luna_main("if you're a really good boy I might even let you shoot it... on me...", "seductive", "right", "sad", "default")
            g9 "Yes!"
            call luna_main("I bet you'd love that wouldn't you?", "angry", "default", "angry", "default")
            g9 "gods yes..."
            call luna_main("Shooting your filthy old cum all over me...", "doubtful", "down", "angry", "default")
            g9 "!!!"
            call luna_main("come on then [l_genie_name]...", "doubtful", "default", "angry", "default")
            call luna_main("stroke it faster...", "seductive", "default", "sad", "default")
            m "{size=-4}(argh... yes...){/size}"
            call luna_main("get that nasty cum ready for me...", "mad", "default", "mad", "default")
            m "{size=-4}yes...{/size}"
            call luna_main("mmm...", "mad", "default", "mad", "default")
            m "{size=+2}yes...{/size}"
            call luna_main("you really love this don't you...", "doubtful", "default", "angry", "default")
            g4 "{size=+4}(agh...){/size}"
            ">you start stroking your cock even faster!"
            g4 "{size=+4}yes...{/size}"
            call luna_main("Is this why you became a teacher...", "doubtful", "default", "sad", "default")
            call luna_main("Just to cover young students in your filthy cum...", "seductive", "default", "angry", "default")
            g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
            call luna_main("well?", "doubtful", "default", "sad", "default")
            g4 "{size=+4}(agh... almost there...){/size}"
            call luna_main("do it...", "angry", "default", "angry", "default")
            call luna_main("{size=+4}cum all over me!{/size}", "doubtful", "default", "angry", "smile_large")
            g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
            $ genie_cum_chibi_xpos = -20
            $ genie_cum_chibi_ypos  = 10
            $ g_c_c_u_pic = "genie_cum_03"
            show screen g_c_c_u
            $ luna_wear_cum = True
            if luna_addicted:
                $ luna_cum = 11
            else:
                $ luna_cum = 5
            hide screen luna
            with d3
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            call luna_main("...", "seductive", "down", "default", "default")
            g4 "Argh! YES!"
            hide screen luna
            with d3
            hide screen bld1
            with d3
            show screen bld1
            with d3
            $ g_c_u_pic = "jerking_off_02_ani"
            hide screen g_c_c_u
            hide screen bld1
            if luna_addicted:
                call luna_main("That's it, [l_genie_name], make sure you cover me...", "doubtful", "default", "mad", "default")
                show screen genie_jerking_sperm_02
                with d3
                g4 "ah, shit... ah... this is too good..."
                call luna_main("mmm...", "mad", "default", "mad", "default")
                m "ah..."
                call luna_main("keep going... make sure you get every last drop out of that delicous cum out...", "mad", "down", "sad", "default")
                m "ah... Thank you..."
                call luna_main("Good boy...", "seductive", "right", "angry", "default")
                call luna_main("Well seeing as how you've ...finished... I suppose I better clean up.", "angry", "right", "angry", "upset")
                $ luna_cum = 12
                ">Luna collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "seductive", "empty", "sad", "default")
                call luna_main("mmmm{image=textheart}{image=textheart}", "seductive", "left_stare", "sad", "default")
                ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
                $ luna_cum = 13
                call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "seductive", "left_stare", "sad", "default")
                pause
                $ luna_cum = 14
                call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "seductive", "left_stare", "sad", "default")
                $ luna_cum = 15
                call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "seductive", "left_stare", "sad", "default")
                $ luna_wear_cum = False
                call luna_main("ah...", "seductive", "left_stare", "sad", "default")
                call luna_main("amazing...", "seductive", "left", "sad", "default")
                hide screen luna
                with d3
                ">Luna quickly picks her clothes up off your desk and gets dressed."
                $ luna_wear_skirt = True
                $ luna_wear_top = True
                $ luna_wear_bra = True
                $ luna_wear_panties = True
                $ luna_wear_cum = False
                show screen genie
                hide screen chair_left
                hide screen desk
                hide screen g_c_u
                show screen luna
                with d3
                g4 "That was... incredible!"
                call luna_main("I'm glad you enjoyed yourself...", "default", "left_stare", "default", "default")
                m "we need to do this again!"
                call luna_main("mmmm... but before that, I think we need to discuss payment for this time...", "seductive", "right", "angry", "default")
                $ current_payout = 100
            else:
                call luna_main("That's it, [l_genie_name], make sure you cover me...", "doubtful", "default", "mad", "default")
                show screen genie_jerking_sperm_02
                with d3
                g4 "ah, shit... ah... this is too good..."
                call luna_main("mmm...", "mad", "default", "mad", "default")
                m "ah..."
                call luna_main("keep going... make sure you get every last drop out.", "mad", "down", "sad", "default")
                m "ah... Thank you..."
                call luna_main("Good boy...", "seductive", "right", "angry", "default")
                call luna_main("Well seeing as how you've ...finished... I suppose I better get dressed.", "angry", "right", "angry", "upset")

                hide screen luna
                with d3
                ">Luna quickly picks her clothes up off your desk and gets dressed, putting her shirt on over her cum covered chest."
                $ luna_wear_skirt = True
                $ luna_wear_top = True
                $ luna_wear_bra = True
                $ luna_wear_panties = True
                $ luna_cum = 2
                show screen genie
                hide screen chair_left
                hide screen desk
                hide screen g_c_u
                show screen luna
                with d3
                m "That was... amazing"
                call luna_main("I'm glad you enjoyed yourself...", "default", "default", "default", "default")
                m "I have to ask though. why did you-"
                call luna_main("Do this?", "seductive", "right", "angry", "upset")
                m "yes."
                call luna_main("Don't worry about that...", "mad", "default", "angry", "default")
                call luna_main("THe only thing you have to worry about...", "angry", "default", "angry", "default")
                $ luna_l_arm = 2
                ">She runs her finger across the edge of her mouth."
                call luna_main("Is keeping that cock of yours in check...", "angry", "down", "angry", "default")
                m "What?"
                call luna_main("I know you're probably leering after some other students sir...", "doubtful", "default", "mad", "default")
                call luna_main("But if I find out that you've buying favours from other students.", "doubtful", "right", "default", "default")
                call luna_main("well...", "doubtful", "default", "default", "default")
                m "..."
                call luna_main("let's just say I wouldn't let that happen if I were you...", "doubtful", "right", "default", "default")
                call luna_main("Now forget about that, let's discuss payment. 100 gold sounds fair to me... {p}how about you?", "doubtful", "default", "angry", "default")
                m "It sounds fair..."
                call luna_main("I'm glad we could have a happy ending.", "mad", "right", "sad", "default")
                m "yes [luna_name]..."
                call luna_main("Good boy... now, speaking of payment...", "doubtful", "default", "angry", "upset")
                $ current_payout = 100







    hide screen bld1
    if luna_dom >= luna_sub:
        m "Alright, alright. Here's your gold."
    else:
        m "well then, Here's your payment [luna_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    ">You hand Luna [current_payout] gold."
    if current_payout <= 40:
        call luna_main("(only [current_payout]?) *hmph*", "mad", "right", "angry", "angry")
        call luna_main("Thank you, [l_genie_name].", "doubtful", "right", "angry", "upset")
    else:
        call luna_main("Thank you, [l_genie_name].", "seductive", "right", "default", "default")
    ">Luna leaves your office."
    $ luna_wear_cum = False
    hide screen genie_jerking_sperm_02

    jump luna_away




label luna_favour_4: ###Luna handjob
    m "{size=-4}(I'll just ask for a quick tug...){/size}"
    if luna_corruption > 13:
        jump luna_handjob_hermione_call
    if luna_addicted:
        if luna_corruption <= 11:
            $ luna_corruption += 1
        call play_music("chipper_doodle")
        m "[luna_name]?"
        call luna_main("yes [l_genie_name]...", "default", "right", "angry", "upset")
        m "Would it be possible for me to buy another favour..."
        call luna_main("Does it involve me cranking out that delicous cum from your wrinkly old balls?", "angry", "right", "angry", "default")
        call luna_main("Hmmmm?", "seductive", "default", "default", "default")
        m "Possibly..."
        call luna_main("mmmm... good boy...", "mad", "default", "mad", "default")
        call luna_main("well...", "mad", "default", "mad", "default")
        call luna_main("stand up [l_genie_name]...", "mad", "default", "mad", "default")

        show screen blkfade
        ">You stand up and walk around your desk, standing in front of Luna."
        ">You open your cloak and pull out your cock."
        hide screen bld1
        hide screen genie
        show screen chair_left
        show screen desk
        $ genie_chibi_xpos = -20
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen g_c_u
        with fade
        hide screen blktone
        hide screen blkfade
        with d5
        pause
        m "Well..."
        call luna_main("...", "angry", "left_stare", "angry", "angry")
        ">Luna looks down at your cock."
        call luna_main("Mmmm, to think something so disgusting could be so tasty...", "doubtful", "left_stare", "mad", "default")
        ">She takes a firm hold of it with her right hand"
        $ luna_r_arm = 3
        $ genie_sprite_xpos = 300
        $ luna_xpos = 390
        call gen_main("!!!", 4, 2)
        call luna_main("*Hmmph*", "seductive", "left_stare", "angry", "default")
        call luna_main("(It's so warm...)", "seductive", "down", "mad", "default")
        ">Luna slowly starts stroking your cock with her hand, her movements are fast yet stiff."
        m "Why don't you try grabbing it with both hands [luna_name]..."
        call luna_main("Hmph... I don't think so [l_genie_name]!", "mad", "default", "angry", "default")
        m "..."
        ">Luna starts moving her hand back and forth along the length of your cock."
        m "ugh... Yes, that's it..."
        call luna_main("See, one hand's all you need.", "doubtful", "down", "mad", "angry")
        m "Mmmm, yes... just like that [luna_name]..."
        call luna_main("Is this good [l_genie_name]?", "tired", "default", "sad", "talk")
        m "yes, yes, this is amazing..."
        call luna_main("good...", "doubtful", "default", "sad", "default")
        call luna_main("but...", "doubtful", "right", "sad", "upset")
        call luna_main("I think you need a little more encouragement...", "mad", "default", "sad", "default")
        m "What are you thinking?"
        call luna_main("well...", "doubtful", "left_stare", "mad", "default")
        $ luna_wear_skirt = False
        $ luna_wear_bra = False
        $ luna_wear_panties = False
        $ luna_wear_top = False
        ">Luna casually strips, all while keeping a firm grip of your cock."
        g4 "Now that's some encouragement!"
        call luna_main("That's not all sir...", "doubtful", "left_stare", "mad", "default")
        $ genie_sprite_base = "characters/genie/base_4.png"
        $ luna_r_arm = 1
        menu:
            "-Luna teases you with her butt-":
                $ luna_flip = -1
                $ luna_r_arm = 2
                $ luna_l_arm = 2
                $ luna_xpos = 500
                ">Luna slowly turns around, giving a nice view of her pale white cheeks."
                m "Mmmm"
                ">She slowly rolls her hips side to side."
                call luna_main("Enjoying the view...", "mad", "right", "sad", "default")
                m "Very nice [luna_name]!"
                call luna_main("...", "angry", "left_stare", "sad", "upset")
                call luna_main("Thank you sir...", "angry", "right", "sad", "default")
                $ luna_xpos = 390
                pause
                ">She quietly backs into you, just letting the tip of your cock touch her ass, a drop of precum sticks to her cheek."
                call luna_main("Mmm, that's much better...", "seductive", "right", "angry", "default")
                m "Gods yes."
                call luna_main("...", "closed_happy", "right", "angry", "default")
                pause
                $ luna_xpos = 390
                call luna_main("well, I suppose I better get back to work...", "mad", "left_stare", "angry", "default")
                ">Luna slowly turns back around before placing her hand back on your cock."
                $ luna_r_arm = 3
                $ luna_flip = 1
                $ genie_sprite_base = "characters/genie/base_2.png"
                ">Luna starts pumping your cock a little faster."
            "-Luna teases you with her thighs-":
                $ luna_choice = 2
                call luna_main("Come on Professor...", "mad", "right", "sad", "default")
                $ luna_xpos = 350
                ">Luna steps towards you."
                m "mmmm..."
                call luna_main("Get a nice big, tasty load ready for me...", "angry", "left_stare", "sad", "upset")
                m "Ah yes..."
                call luna_main("get ready to cum all for your student.", "angry", "default", "sad", "default")
                $ luna_xpos = 280
                $ luna_ypos = -40
                ">She steps even closer, forcing your cock in between her soft thighs."
                m "Ah..."
                call luna_main("so that I can eat it...", "angry", "down", "angry", "default")
                m "yes..."
                call luna_main("Mmmm, you like that don't you...", "mad", "right", "angry", "default")
                ">Luna starts rolling her thighs around your cock. You can even feel her wet mound grinding against the top of your shaft."
                g4 "Ah! yes!"
                call luna_main("...", "doubtful", "left_stare", "mad", "default")
                g4 "[luna_name]..."
                call luna_main("Hmmm, are you feeling alright now [l_genie_name]?", "seductive", "right", "raised", "default")
                g4 "yes... thank you [luna_name]..."
                call luna_main("Good boy.", "angry", "down", "angry", "default")
                $ luna_xpos = 390
                $ luna_ypos = 0
                call luna_main("*Ptew*", "seductive", "down_left", "angry", "open_tongue")
                $ luna_r_arm = 3
                $ luna_flip = 1
                $ genie_sprite_base = "characters/genie/base_2.png"
                ">Luna spits into her hand before placing it back on your cock."
        g4 "Mmmm, yes that's it [luna_name]..."
        call luna_main("...", "angry", "left_stare", "angry", "default")
        g4 "Just keep pumping that hand up and down."
        call luna_main("......", "mad", "default", "mad", "default")
        if luna_choice == 1:
            ">Luna gently starts shaking her boobs as she jerks you off."
        else:
            call luna_main("*Ptew*", "angry", "down_left", "mad", "open_tongue")
            ">Luna spits into her hand again and places it back on your cock."
        ">She then starts pumping your cock even faster."
        g4 "Gods yes..."
        g4 "(This is it, where should I cum?)"
        menu:
            "-On her cunt!-":
                ">You place your hand on Luna's cheek, trying to hold her in position."

            "-On her tits!-":
                ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

        call luna_main("[l_genie_name]!!!", "angry", "default", "mad", "furious")
        call luna_main("You're not trying to cum on me are you?", "mad", "default", "mad", "angry")
        g4 "Ah [luna_name], I'm almost there!"
        $ genie_sprite_base = "characters/genie/base_4.png"
        $ luna_ypos = 220
        $ luna_xpos = 350
        $ luna_r_arm = 1
        ">Luna gets on her knees before you."
        ">She takes her hand off your cock, leaving you high and dry."
        call luna_main("from now on, the only place you'll be coming is here...", "doubtful", "default", "mad", "angry")
        g4 "Mmmm yes!"
        call luna_main("...", "seductive", "down", "angry", "wide_smile")
        $ luna_xpos = 310
        ">She leans forward, giving your cock a tentative lick."
        call luna_main("...", "doubtful", "down_left", "sad", "wide_smile")
        call luna_main("(This doesn't taste nearly as good...)", "doubtful", "right", "mad", "wide_smile")
        call luna_main("(although it's not the worst...)", "seductive", "down", "sad", "wide_smile")
        g4 "Almost there slut!"
        $ luna_xpos = 350
        ">She moves back slightly from your cock."
        call luna_main("then cum for me...", "angry", "down", "mad", "default")
        call luna_main("cum...", "seductive", "empty", "sad", "default") #hypno eyes
        pause
        g4 "Ah{size=+2} here {size=+2}it {size=+2}is!{/size}"
        menu:
            "Where should you cum?"
            "-Face-":
                $ luna_choice = 1
                $ luna_cum = 11
                $ luna_wear_cum = True
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "closed_happy", "down", "sad", "wide_smile")
                pause
                ">You start shooting your load across her face, coating her in your sticky cum."
                hide screen g_c_c_u
                $ g_c_u_pic = "images/animation/06_jerking_01.png"
                $ luna_r_arm = 2
                $ luna_l_arm = 2
                $ genie_sprite_base = "characters/genie/base_2.png"
                hide screen genie_sprite
                with d3
                $ luna_xpos = 390
                $ luna_ypos = 0
                ">Luna hops to her feet."
                $ luna_cum = 12
                ">Luna then collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "angry", "left_stare", "angry", "default")
                call luna_main("Just give me a moment to clean up sir...", "seductive", "left_stare", "angry", "default")
                m "Sure..."
                ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
                $ luna_cum = 13
                call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "closed_happy", "left_stare", "sad", "default")
                pause
                $ luna_cum = 14
                call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "closed_happy", "left_stare", "sad", "default")
                $ luna_cum = 15
                call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "closed_happy", "left_stare", "sad", "default")
                $ luna_wear_cum = False
                call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
                call luna_main("*gulp*", "closed_happy", "left_stare", "sad", "default")
                call luna_main("ah...", "closed_happy", "left_stare", "sad", "default")
                call luna_main("amazing...", "seductive", "left_stare", "sad", "default")
            "-Mouth-":
                $ luna_choice = 2
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "closed_happy", "down", "sad", "cheeks_full")
                pause
                ">You start firing your load directly into her open mouth. Her eyes glaze over as she struggles to fit it all in."
                g4 "Argh! by the gods {size=+10}YES!{/size}"
                call luna_main("!!!", "seductive", "empty", "sad", "cheeks_full")
                pause
                call luna_main("(It's so good...)", "seductive", "right", "sad", "cheeks_full")
                call luna_main("...", "seductive", "down", "sad", "cheeks_full")
                g4 "{size=+10}TAKE IT ALL YOU big titted sLUT!{/size}"
                g4 "mmmm....."
                hide screen g_c_c_u
                $ g_c_u_pic = "images/animation/06_jerking_01.png"
                $ luna_r_arm = 2
                $ luna_l_arm = 2
                $ genie_sprite_base = "characters/genie/base_2.png"
                hide screen genie_sprite
                with d3
                m "That hit the spot..."
                call luna_main("*gulp*", "closed_happy", "left_stare", "sad", "default")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "seductive", "empty", "sad", "default")
                m "Ahh... that was fantastic slut..."
                call luna_main("[l_genie_name]...", "doubtful", "right", "angry", "default")
        $ g_c_u_pic = "images/animation/06_groping_01.png"
        $ luna_xpos = 390
        $ luna_ypos = 0
        m "well then, Here's your payment [luna_name]."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
        call luna_main("Oh um... yes, Thank you, [l_genie_name].", "seductive", "right", "default", "default")
        call luna_main("let me just get dressed...", "seductive", "right", "default", "default")
        $ luna_wear_skirt = True
        $ luna_wear_bra = True
        $ luna_wear_panties = True
        $ luna_wear_top = True
        ">Luna quickly gets dressed before leaving your office, a streak of embarrassment across her face."
        $ luna_wear_cum = False
        $ luna_wear_cum_under = False
        m "Weird..."

        hide screen g_c_u
        show screen genie
        hide screen chair_left
        hide screen desk

        jump luna_away

    else:
        if luna_corruption <= 10: #FIRST TIME - Change this to 10 when part 2 added
            if luna_corruption <= 10:
                $ luna_corruption += 1
            call play_music("chipper_doodle")
            m "[luna_name]?"
            call luna_main("yes [l_genie_name]...", "default", "right", "angry", "upset")
            m "Would it be possible for me to buy another favour..."
            call luna_main("...", "angry", "right", "angry", "upset")
            call luna_main("Go on...", "angry", "right", "angry", "upset")
            menu:
                "-Ask for a handjob politely-" if luna_sub < luna_dom:
                    $ current_payout = 160
                    if luna_dom <= 8:
                        $ luna_dom += 1
                    $ luna_choice = 3
                    m "Well seeing as how you're so skilled at everything you turn your hand towards..."
                    call luna_main("Mhmmm...", "doubtful", "right", "angry", "angry")
                    m "I was hoping you could turn your hand towards my cock."
                    call luna_main("...", "mad", "right", "default", "upset")
                    m "please..."
                    call luna_main("Really? You want me to stroke that filthy cock of yours?", "mad", "default", "angry", "angry")
                    call luna_main("Isn't it enough that I let you touch yourself...", "doubtful", "right", "mad", "angry")
                    m "There'll be a hefty reward..."
                    call luna_main("...", "mad", "right", "mad", "angry")
                    call luna_main("......", "mad", "default", "angry", "upset")
                    call luna_main("Well seeing as how you asked so nicely...", "mad", "default", "default", "default")
                    m "..."
                    call luna_main("Get over here...", "angry", "default", "mad", "default")
                    m "Fantastic! Let me just stand up."
                    call luna_main("(This couldn't get any easier)", "mad", "right", "angry", "default")
                "-Beg for a handjob-" if luna_dom >= 7:
                    $ current_payout = 200
                    if luna_dom <= 8:
                        $ luna_dom += 1
                    $ luna_choice = 4
                    m "Well if it's not too much trouble..."
                    call luna_main("Mhmmm...", "doubtful", "right", "angry", "angry")
                    m "I was hoping you could..."
                    call luna_main("...", "mad", "right", "default", "upset")
                    m "give me a handjob..."
                    call luna_main("Really? You want me to stroke that filthy cock of yours?", "mad", "default", "angry", "angry")
                    m "If it's not too much trouble..."
                    call luna_main("Well I suppose I probably should.", "seductive", "right", "default", "default")
                    call luna_main("Who knows who you'll call up here if I don't...", "mad", "default", "mad", "default")
                    m "Thank you..."
                    call luna_main("...", "mad", "right", "mad", "angry")
                    call luna_main("......", "mad", "default", "angry", "upset")
                    call luna_main("However I do expect to be fairly compensated...", "mad", "default", "default", "default")
                    m "Of course."
                    call luna_main("Good. Now Get over here...", "angry", "default", "mad", "default")
                    m "Fantastic! Let me just stand up."
                    call luna_main("(This couldn't get any easier...)", "mad", "right", "angry", "default")
                    call luna_main("(I'll be the only person in his will by the end of the month at this rate...)", "doubtful", "default", "mad", "default")

            show screen blkfade
            ">You stand up and walk around your desk, standing in front of Luna."
            ">You open your cloak and pull out your cock."
            hide screen bld1
            hide screen genie
            show screen chair_left
            show screen desk
            $ genie_chibi_xpos = -20
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "jerking_off_02_ani"
            show screen g_c_u
            with fade
            hide screen blktone
            hide screen blkfade
            with d5
            pause
            m "Well..."
            call luna_main("...", "angry", "left_stare", "angry", "angry")
            ">Luna looks down at your cock."
            call luna_main("Disgusting...", "doubtful", "left_stare", "mad", "default")
            ">She takes a firm hold of it with her right hand"
            $ luna_r_arm = 3
            $ genie_sprite_xpos = 300
            $ luna_xpos = 390
            call gen_main("!!!", 4, 4)
            call luna_main("*Hmmph* At least it isn't small...", "seductive", "left_stare", "angry", "default")
            call luna_main("(I can't even fit my hand around it.)", "seductive", "down", "mad", "default")
            ">Luna slowly starts stroking your cock with her hand, her movements are rough and inexperienced."
            m "Why don't you try grabbing it with both hands [luna_name]..."
            call luna_main("Hmph... you wish!", "mad", "default", "angry", "default")
            m "..."
            ">Luna starts moving her hand back and forth along the length of your cock."
            m "ugh... Yes, that's it..."
            call luna_main("(Men really are the worst)", "doubtful", "down", "mad", "angry")
            m "Mmmm, yes... just like that [luna_name]..."
            call luna_main("Is this good [l_genie_name]?", "tired", "default", "sad", "talk")
            m "yes, yes, this is amazing..."
            call luna_main("good...", "doubtful", "default", "sad", "default")
            call luna_main("but...", "doubtful", "right", "sad", "upset")
            call luna_main("Do you need a little more encouragement?", "mad", "default", "sad", "default")
            m "What are you thinking?"
            call luna_main("......", "doubtful", "left_stare", "mad", "default")
            menu:
                "-Luna takes her top off-":
                    ">Luna slowly removes her vest and starts to unbutton her top."
                    m "Mmmm"
                    $ luna_wear_top = False
                    $ luna_choice = 1
                    $ luna_r_arm = 2
                    ">She takes her shirt off and places it onto the floor."
                    call luna_main("There...", "mad", "right", "sad", "default")
                    m "Very nice [luna_name]!"
                    call luna_main("...", "angry", "left_stare", "sad", "upset")
                    call luna_main("Thank you sir...", "angry", "default", "sad", "default")
                    $ luna_r_arm = 3
                    ">She places her hands back around your cock."
                    call luna_main("Mmm, much better...", "seductive", "left_stare", "angry", "default")
                    m "Gods yes."
                    call luna_main("...", "seductive", "default", "angry", "default")
                    call luna_main("I'd take my bra off as well...", "seductive", "right", "sad", "upset")
                    call luna_main("But I don't think you'd be able to stop yourself from cumming on the spot, would you?", "mad", "default", "mad", "default")
                    g4 "probably not!"
                    call luna_main("...", "doubtful", "left_stare", "angry", "default")
                    ">Luna starts pumping your cock a little faster."
                "-Luna teases you-":
                    $ luna_choice = 2
                    call luna_main("Come on Professor...", "mad", "right", "sad", "default")
                    ">Luna starts moving her hands up and down your cock a little faster."
                    m "mmmm..."
                    call luna_main("Get a nice big load ready for me...", "angry", "left_stare", "sad", "upset")
                    m "Ah yes..."
                    call luna_main("get ready to cum all over your student.", "angry", "default", "sad", "default")
                    ">She speeds up the pace."
                    m "Ah..."
                    call luna_main("What's wrong?", "angry", "default", "raised", "upset")
                    m "Well if you go that fast the friction's a little painful."
                    call luna_main("Really?...", "mad", "default", "angry", "default")
                    ">Luna doesn't slow down. If anything she speeds up slightly."
                    g9 "Ah!"
                    call luna_main("...", "doubtful", "default", "mad", "default")
                    g9 "[luna_name]..."
                    call luna_main("Hmmm, do You want me to spit on your cock then?", "seductive", "default", "raised", "default")
                    g9 "Just a little bit..."
                    call luna_main("...", "seductive", "default", "angry", "default")
                    call luna_main("......", "seductive", "default", "mad", "default")
                    g9 "Please..."
                    call luna_main("Good boy.", "angry", "default", "angry", "default")
                    call luna_main("*Ptew*", "seductive", "down_left", "angry", "open_tongue")
                    ">Luna spits into her hand before placing it back on your cock."
            g4 "Mmmm, yes that's it [luna_name]..."
            call luna_main("...", "angry", "left_stare", "angry", "default")
            g4 "Just keep pumping those hands up and down."
            call luna_main("......", "mad", "default", "mad", "default")
            if luna_choice == 1:
                ">Luna gently starts shaking her boobs as she jerks you off."
            else:
                call luna_main("*Ptew*", "angry", "down_left", "mad", "open_tongue")
                ">Luna spits into her hand again and places it back on your cock."
            ">She then starts pumping your cock even faster."
            g4 "Gods yes..."
            g4 "(This is it, where should I cum?)"
            menu:
                "-On her face-":
                    ">You place your hand on the top of Luna's head and slowly try to force it down to be level with your crouch."

                "-On her tits-":
                    ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

            call luna_main("[l_genie_name]!!!", "angry", "default", "mad", "furious")
            call luna_main("You're not trying to cum on me are you?", "mad", "default", "mad", "angry")
            g4 "Ah [luna_name], I'm almost there."
            call luna_main("Well...", "doubtful", "left_stare", "mad", "angry")
            $ luna_wear_skirt = False
            ">Luna quickly pulls down her skirt."
            g4 "!!!"
            call luna_main("You cum...", "mad", "default", "mad", "angry")
            g4 "Ah..."
            ">Luna slowly pulls her panties forward, exposing her pussy to the air."
            ">Her right hand is still wrapped around your cock as she pumps it with blinding speed."
            call luna_main("Where I tell you...", "doubtful", "default", "mad", "angry")
            g4 "mmmm"
            call luna_main("Now...", "mad", "default", "mad", "upset")
            call luna_main("Cum.", "seductive", "default", "angry", "default")
            $ g_c_c_u_pic = "jerking_off_cum_ani"
            show screen g_c_c_u
            $ luna_wear_cum_under = True
            $ luna_cum = 10
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            ">You start shooting your load directly into Luna's panties, coating her pussy in cum."
            g4 "Argh! by the gods {size=+10}YES!{/size}"
            call luna_main("...", "seductive", "down", "default", "default")
            call luna_main("(It's so warm...)", "seductive", "right", "sad", "default")
            g4 "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
            g4 "mmmm....."
            hide screen g_c_c_u
            $ g_c_u_pic = "images/animation/06_jerking_01.png"
            $ luna_r_arm = 2
            hide screen genie_sprite
            with d3
            m "That hit the spot..."
            call luna_main("({image=textheart}{image=textheart}{image=textheart})", "seductive", "left_stare", "sad", "default")
            call luna_main("[l_genie_name]!", "mad", "default", "mad", "default")
            call luna_main("How could you! Cumming on your students {size=-10}pussy{/size}...", "angry", "left_stare", "angry", "default")
            m "Ahh... that was fantastic slut..."
            $ g_c_u_pic = "images/animation/06_groping_01.png"
            call luna_main("[l_genie_name]...", "doubtful", "right", "angry", "default")

        else: #last time event is run before cum addict variant
            if luna_corruption <= 11:
                $ luna_corruption += 1
            call play_music("chipper_doodle")
            m "[luna_name]?"
            call luna_main("yes [l_genie_name]...", "default", "right", "angry", "upset")
            m "Would it be possible for me to buy another favour..."
            call luna_main("I think I know what you want...", "angry", "right", "angry", "default")
            call luna_main("but why don't you ask me anyway...", "seductive", "default", "default", "default")
            call luna_main("you know I like to hear you beg.", "mad", "default", "mad", "default")
            menu:
                "-Ask for a handjob politely-" if luna_sub < luna_dom:
                    $ current_payout = 160
                    if luna_dom <= 8:
                        $ luna_dom += 1
                    $ luna_choice = 3
                    m "Well seeing as how you're so skilled at everything you turn your hand towards..."
                    call luna_main("Mhmmm...", "doubtful", "right", "angry", "angry")
                    m "I was hoping you could turn your hand towards my cock."
                    call luna_main("...", "mad", "right", "default", "upset")
                    m "please..."
                    call luna_main("Really? You want me to stroke that filthy cock of yours?", "mad", "default", "angry", "angry")
                    call luna_main("Isn't it enough that I let you touch yourself...", "doubtful", "right", "mad", "angry")
                    m "There'll be a hefty reward..."
                    call luna_main("...", "mad", "right", "mad", "angry")
                    call luna_main("......", "mad", "default", "angry", "upset")
                    call luna_main("Well seeing as how you asked so nicely...", "mad", "default", "default", "default")
                    m "..."
                    call luna_main("Get over here...", "angry", "default", "mad", "default")
                    m "Fantastic! Let me just stand up."
                    call luna_main("(This couldn't get any easier)", "mad", "right", "angry", "default")
                "-Beg for a handjob-" if luna_dom >= 7:
                    $ current_payout = 200
                    if luna_dom <= 8:
                        $ luna_dom += 1
                    $ luna_choice = 4
                    m "Well if it's not too much trouble..."
                    call luna_main("Mhmmm...", "doubtful", "right", "angry", "angry")
                    m "I was hoping you could..."
                    call luna_main("...", "mad", "right", "default", "upset")
                    m "give me a handjob..."
                    call luna_main("Really? You want me to stroke that filthy cock of yours?", "mad", "default", "angry", "angry")
                    m "If it's not too much trouble..."
                    call luna_main("Well I suppose I probably should.", "seductive", "right", "default", "default")
                    call luna_main("Who knows who you'll call up here if I don't...", "mad", "default", "mad", "default")
                    m "Thank you..."
                    call luna_main("...", "mad", "right", "mad", "angry")
                    call luna_main("......", "mad", "default", "angry", "upset")
                    call luna_main("However I do expect to be fairly compensated...", "mad", "default", "default", "default")
                    m "Of course."
                    call luna_main("Good. Now Get over here...", "angry", "default", "mad", "default")
                    m "Fantastic! Let me just stand up."
                    call luna_main("(This couldn't get any easier...)", "mad", "right", "angry", "default")
                    call luna_main("(I'll be the only person in his will by the end of the month at this rate...)", "doubtful", "default", "mad", "default")

            show screen blkfade
            ">You stand up and walk around your desk, standing in front of Luna."
            ">You open your cloak and pull out your cock."
            hide screen bld1
            hide screen genie
            show screen chair_left
            show screen desk
            $ genie_chibi_xpos = -20
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "jerking_off_02_ani"
            show screen g_c_u
            with fade
            hide screen blktone
            hide screen blkfade
            with d5
            pause
            m "Well..."
            call luna_main("...", "angry", "left_stare", "angry", "angry")
            ">Luna looks down at your cock."
            call luna_main("Disgusting...", "doubtful", "left_stare", "mad", "default")
            ">She takes a firm hold of it with her right hand"
            $ luna_r_arm = 3
            $ genie_sprite_xpos = 300
            $ luna_xpos = 390
            call gen_main("!!!", 4, 4)
            call luna_main("*Hmmph* At least it isn't small...", "seductive", "left_stare", "angry", "default")
            call luna_main("(I can't even fit my hand around it.)", "seductive", "down", "mad", "default")
            ">Luna slowly starts stroking your cock with her hand, her movements are rough and inexperienced."
            m "Why don't you try grabbing it with both hands [luna_name]..."
            call luna_main("Hmph... you wish [l_genie_name]!", "mad", "default", "angry", "upset")
            m "..."
            ">Luna starts moving her hand back and forth along the length of your cock."
            m "ugh... Yes, that's it..."
            call luna_main("(He loves this...)", "doubtful", "down", "mad", "default")
            m "Mmmm, yes... just like that [luna_name]..."
            call luna_main("Is this good [l_genie_name]?", "tired", "default", "sad", "talk")
            m "yes, yes, this is amazing..."
            call luna_main("good...", "doubtful", "default", "sad", "default")
            call luna_main("but...", "doubtful", "right", "sad", "upset")
            call luna_main("Do you need a little more encouragement?", "mad", "default", "sad", "default")
            m "What are you thinking?"
            call luna_main("......", "doubtful", "left_stare", "mad", "default")
            menu:
                "-Luna takes her top off-":
                    ">Luna slowly removes her vest and starts to unbutton her top."
                    m "Mmmm"
                    $ luna_wear_top = False
                    $ luna_choice = 1
                    ">She takes her shirt off and places it onto the floor."
                    call luna_main("There...", "mad", "right", "sad", "default")
                    $ luna_r_arm = 2
                    m "Very nice [luna_name]!"
                    call luna_main("...", "angry", "left_stare", "sad", "upset")
                    call luna_main("Thank you sir...", "angry", "default", "sad", "default")
                    $ luna_r_arm = 3
                    ">She places her hands back around your cock."
                    call luna_main("Mmm, much better...", "seductive", "left_stare", "angry", "default")
                    m "Gods yes."
                    call luna_main("...", "seductive", "default", "angry", "default")
                    call luna_main("well, seeing as how you're being such a good boy...", "mad", "down", "angry", "default")
                    $ luna_wear_bra = False
                    $ luna_r_arm = 2
                    $ luna_l_arm = 2
                    ">Luna slowly removes her bra before placing her hand back on your cock."
                    $ luna_r_arm = 3
                    $ luna_l_arm = 1
                    ">Luna starts pumping your cock a little faster."
                "-Luna teases you-":
                    $ luna_choice = 2
                    call luna_main("Come on Professor...", "mad", "right", "sad", "default")
                    ">Luna starts moving her hands up and down your cock a little faster."
                    m "mmmm..."
                    call luna_main("Get a nice big load ready for me...", "angry", "left_stare", "sad", "upset")
                    m "Ah yes..."
                    call luna_main("get ready to cum all over your student.", "angry", "default", "sad", "default")
                    ">She speeds up the pace."
                    m "Ah..."
                    call luna_main("mmmm, hurts doesn't it.", "angry", "down", "angry", "default")
                    m "yes..."
                    call luna_main("Really?...", "mad", "default", "angry", "default")
                    ">Luna doesn't slow down. If anything she speeds up slightly."
                    g9 "Ah! yes!"
                    call luna_main("...", "doubtful", "default", "mad", "default")
                    g9 "[luna_name]..."
                    call luna_main("Hmmm, do You want me to spit on your cock then?", "seductive", "default", "raised", "default")
                    g9 "yes... please [luna_name]..."
                    call luna_main("Good boy.", "angry", "default", "angry", "default")
                    call luna_main("*Ptew*", "seductive", "down_left", "angry", "open_tongue")
                    ">Luna spits into her hand before placing it back on your cock."
            g4 "Mmmm, yes that's it [luna_name]..."
            call luna_main("...", "angry", "left_stare", "angry", "default")
            g4 "Just keep pumping those hands up and down."
            call luna_main("......", "mad", "default", "mad", "default")
            if luna_choice == 1:
                ">Luna gently starts shaking her boobs as she jerks you off."
                call luna_main("......", "seductive", "left_stare", "angry", "default")
            else:
                call luna_main("*Ptew*", "angry", "down_left", "mad", "open_tongue")
                ">Luna spits into her hand again and places it back on your cock."
            ">She then starts pumping your cock even faster."
            g4 "Gods yes..."
            g4 "(This is it, where should I cum?)"
            menu:
                "-On her face-":
                    ">You place your hand on the top of Luna's head and slowly try to force it down to be level with your crouch."

                "-On her tits-":
                    ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

            call luna_main("[l_genie_name]!!!", "angry", "default", "mad", "furious")
            call luna_main("You're not trying to cum on me are you?", "mad", "default", "mad", "angry")
            g4 "Ah [luna_name], I'm almost there!"
            call luna_main("hmmm... (Might as well make some more money from the [l_genie_name]...)", "doubtful", "left_stare", "mad", "angry")
            $ luna_wear_skirt = False
            $ luna_wear_bra = False
            $ luna_wear_panties = False
            $ luna_wear_top = False
            ">Luna quickly strips, all while keeping a firm grip of your cock.."
            g4 "hurry up! You'll ruin the damn moment!"
            call luna_main("well then, pick...", "seductive", "default", "sad", "upset")
            g4 "you mean..."
            ">Leans forward slowly while ever so slightly jiggling her milky boobs."
            ">Her right hand is still wrapped around your cock as she pumps slowly, keeping you at firmly at the edge."
            call luna_main("pick where you want to cum...", "seductive", "left_stare", "mad", "default")
            g4 "Ah yes!"
            call luna_main("you can pick my boobs...", "mad", "right", "sad", "upset")
            ">She gives them another shake."
            call luna_main("or my thighs...", "seductive", "default", "angry", "default")
            ">She rubs them together as she rotates on the balls of her feet."
            call luna_main("boobs are an extra 100...", "angry", "default", "mad", "default")
            call luna_main("thighs are 50...", "angry", "right", "angry", "upset")
            g4 "Ah{size=+2} here {size=+2}it {size=+2}is!{/size}"
            menu:
                "-boobs-":
                    $ current_payout += 100
                    show screen g_c_c_u
                    $ luna_cum = 5
                    $ luna_wear_cum = True
                    show screen white
                    pause.1
                    hide screen white
                    pause.2
                    show screen white
                    pause .1
                    hide screen white
                    with hpunch
                    ">You start shooting your load across her chest, coating her tits in cum."

                "-thighs-":
                    $ current_payout += 50
                    show screen g_c_c_u
                    $ luna_cum = 10
                    $ luna_wear_cum = True
                    show screen white
                    pause.1
                    hide screen white
                    pause.2
                    show screen white
                    pause .1
                    hide screen white
                    with hpunch
                    ">You start spurting over Luna's soft thighs, coating her pussy in cum."

                "-{size=+10}FACE!{/size}-":
                    jump luna_cum_addict_event
            g4 "Argh! by the gods {size=+10}YES!{/size}"
            call luna_main("...", "seductive", "down", "default", "default")
            call luna_main("(It's so warm...)", "seductive", "right", "sad", "default")
            g4 "{size=+10}TAKE IT ALL YOU big titted sLUT!{/size}"
            g4 "mmmm....."
            hide screen g_c_c_u
            $ g_c_u_pic = "images/animation/06_jerking_01.png"
            $ luna_r_arm = 2
            hide screen genie_sprite
            with d3
            m "That hit the spot..."
            call luna_main("({image=textheart}{image=textheart}{image=textheart})", "seductive", "left_stare", "sad", "default")
            if luna_choice == 1:
                $ luna_cum = 12
                ">Luna collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "seductive", "left_stare", "sad", "default")
                call luna_main("{size=+4}It's {size=+4}amazing!!!!!{image=textheart}{image=textheart}{/size}", "seductive", "left_stare", "sad", "default")
                call luna_main("but please just shoot it into my mouth next time?", "seductive", "left_stare", "sad", "default")
                m "Sure..."
                ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
                $ luna_cum = 13
                call luna_main("...", "seductive", "left_stare", "sad", "default")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "seductive", "left_stare", "sad", "default")
                pause
                $ luna_cum = 14
                call luna_main("...", "seductive", "left_stare", "sad", "default")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "seductive", "left_stare", "sad", "default")
                $ luna_cum = 15
                call luna_main("...", "seductive", "left_stare", "sad", "default")
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", "seductive", "left_stare", "sad", "default")
                $ luna_wear_cum = False
                call luna_main("ah...", "seductive", "left_stare", "sad", "default")
                call luna_main("amazing...", "seductive", "left_stare", "sad", "default")
            m "Ahh... that was fantastic slut..."
            $ g_c_u_pic = "images/animation/06_groping_01.png"
            call luna_main("[l_genie_name]...", "doubtful", "right", "angry", "default")

    $ luna_wear_skirt = True
    $ luna_wear_bra = True
    $ luna_wear_panties = True
    $ luna_wear_top = True
    $ luna_wear_cum = False
    hide screen bld1
    with d3
    m "well then, Here's your payment [luna_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    ">You hand Luna [current_payout] gold."
    call luna_main("Thank you, [l_genie_name].", "seductive", "right", "default", "default")
    ">Luna leaves your office."
    $ luna_wear_cum = False
    $ luna_wear_cum_under = False

    hide screen g_c_u
    show screen genie
    hide screen chair_left
    hide screen desk

    jump luna_away








label luna_favour_5: #Luna jerks Genie off onto Hermione's face

    if luna_corruption <= 11:
        $ luna_corruption += 1
        m "[luna_name], how would you feel about selling another favour?"
        call luna_main("...", "seductive", "default", "angry", "default")
        call luna_main("What is it this time [l_genie_name]?", "angry", "right", "angry", "default")
        m "Well, do you remember how we had a little fun with miss granger the other day?"
        call luna_main("...", "seductive", "default", "angry", "default")
        call luna_main("go on...", "doubtful", "right", "angry", "default")
        m "how would you feel about bringing her up her for a little more fun?"
        call luna_main("You really are a disgusting pervert aren't you?", "angry", "default", "mad", "default")
        m "..."
        call luna_main("Aren't you...", "doubtful", "default", "angry", "upset")
        m "Yes..."
        call luna_main("at least you're honest about it...", "mad", "right", "sad", "default")
        call luna_main("Which is more than I can say for that two-faced slut hermione...", "wide", "left_stare", "mad", "angry")
        m "So you're OK with having a little fun with her?"
        call luna_main("on one condition.", "angry", "default", "mad", "default")
        m "Name it."
        call luna_main("I'm in control. No matter what.", "mad", "right", "angry", "upset")
        call luna_main("Even if you think what's happening is too mean...", "mad", "default", "angry", "angry")
        call luna_main("I am in control... got it?", "doubtful", "default", "mad", "upset")
        m "Done."
        call luna_main("alright then...", "closed_happy", "default", "sad", "default")
        call luna_main("I also expect to be paid 150 gold for my troubles...", "angry", "default", "sad", "upset")
        m "Certainly."
        call luna_main("...", "seductive", "right", "angry", "default")
        call luna_main("Now [l_genie_name]...", "angry", "default", "mad", "angry")
        m "Alright then..."
        ">You pay Luna 150 gold."
        $ gold -=150
        $ luna_gold += 150
        call luna_main("thank you [l_genie_name]...", "angry", "right", "sad", "upset")
        call luna_main("...", "angry", "default", "raised", "upset")
        call luna_main("Well come on then, summon her...", "mad", "default", "angry", "pout")
        ">You summon Hermione. Somehow..."
        call play_sound("door") #Sound of a door opening.
        $ hermione_SC.chibi.xpos = 600 #Near the desk.
        show screen hermione_blink #Hermione stands still.
        $ luna_flip = -1
        $ luna_r_arm = 2
        $ luna_xpos = 390
        call update_her_uniform
        pause
        call her_main("hello Prof-","soft","baseL")
        call her_main("Luna! what are you doing here?","angry","wide")
        call luna_main("same thing as you...", "seductive", "default", "angry", "default")
        call her_main("Oh, um... you must be here to... help Professor dumbledore then...","open","worriedL")
        call luna_main("Mhmmm...", "angry", "default", "sad", "default")
        call her_main("So, ugh... what does dumbledore need our help with?","open","worried")
        call luna_main("Probably emptying those nasty balls of his...", "mad", "default", "angry", "angry")
        call her_main("!!!","angry","wide")
        call her_main("Luna! what are you talking about?","angry","worried")
        call her_main("are you feeling ok?","annoyed","worriedL")
        call luna_main("come on now hermione... it wouldn't be the first time you've helped old dumbledore like this?", "angry", "right", "angry", "default")
        call luna_main("would it...?", "angry", "default", "angry", "upset")
        call her_main("I have no idea what you're talking about!","scream","angryCl")
        call her_main("Professor dumbledore must be mistaken...","scream","angryCl")
        call her_main("M-Maybe he needs to go to the nurses and have his mind checked...","scream","angryCl")
        call luna_main("So you're not selling favours to dumbledore in exchange for points?", "doubtful", "default", "raised", "upset")
        call her_main("certainly not! I'd never do something so underhanded!","scream","worriedCl")
        call luna_main("Really?", "angry", "default", "raised", "angry")
        call her_main("Of course not! I'm shocked you even have to ask!","annoyed","worriedL")
        call luna_main("So you're comfortable saying that after you've had a sip of some veritaserum?", "mad", "default", "mad", "upset")
        call her_main("!!!","angry","wide")
        call her_main("O-O-Of course... but as you know, that potion's banned...","open","closed")
        call luna_main("Not for the illustrious Professor dumbledore!", "seductive", "right", "sad", "default")
        call luna_main("Isn't that right sir?", "angry", "right", "mad", "angry")
        m "Oh, um yes of course I can get that easily..."
        m "(What the hell is veribatium?)"
        call her_main("!!!","annoyed","frown") #angry face
        call her_main("surely you know there's no need for that sir!","normal","frown") #angry face
        m "..."
        call her_main("...","annoyed","frown")
        call luna_main("...", "angry", "default", "default", "default")
        call her_main("Fine! I admit it!","scream","worriedCl")
        call luna_main("See... Isn't it better to tell the truth?", "mad", "default", "sad", "default")
        call her_main("...","normal","worriedCl")
        call her_main("So is that why I've been brought here? To be ridiculed!?","angry","angry")
        call her_main("I'm not ashamed of what I've done for my house!","annoyed","annoyed")
        call luna_main("No, you've been brought here to sell dumbledore one of those favours.", "seductive", "default", "angry", "default")
        call her_main("What?","upset","wink")
        call her_main("Why are you here then?","soft","base")
        call luna_main("To help you.", "angry", "default", "sad", "default")
        call her_main("...","annoyed","angry")
        call her_main("Help how?","disgust","glance")
        call luna_main("Why don't you take your clothes off and I'll show you...", "mad", "left_stare", "sad", "default")
        call her_main("[genie_name]... please...","scream","worriedCl")
        m "I'm sorry [hermione_name], my hands are tied..."
        call her_main("...","normal","worriedCl")
        call her_main("Do I have to?","angry","worriedCl",emote="05")
        call luna_main("Of course not... So long as you don't mind me telling your precious \"MRM\" what's been going on.", "mad", "default", "mad", "default")
        call her_main("...","mad","worried",tears="soft")
        call her_main("FINE!","mad","worriedCl",tears="soft_blink")
        call her_main("I see how it is!","annoyed","annoyed",tears="crying")
        ">Hermione pulls off her top in a huff."
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call her_main("Feel free to humiliate me!","angry","angry",tears="crying")
        ">Hermione angrly removes her skirt."
        $ hermione_wear_skirt = False
        $ hermione_wear_panties = False
        call her_main("for trying to do what's right!","annoyed","annoyed",tears="crying")
        ">Hermione stands naked before you and Luna. Her face is contorted in what seems like an equal mix of rage and embarrassment."
        call her_main("there! are you happy now you two?","annoyed","annoyed")
        m "Ye-"
        call luna_main("almost...", "seductive", "down", "sad", "default")
        call luna_main("now why don't you get on your knees...", "angry", "default", "angry", "angry")
        call her_main("!!!","angry","wide",tears="crying")
        call her_main("please, luna... I'm {size=-2}sorry {size=-2}about {size=-2}what I said to you the other day...{/size}","annoyed","down",tears="crying")
        call luna_main("then kneel...", "doubtful", "default", "sad", "upset")
        hide screen hermione_main
        $ hermione_SC.chibi.xpos = 40 #40 = Near Luna
        $ hermione_SC.chibi.ypos = 60
        $ h_c_u_pic = "characters/hermione/chibis/dance/08_sits.png"
        $ hermione_head_xpos=590
        show screen h_c_u
        with d3
        call her_kneel("...","annoyed","ahegao")
        call luna_main("there... isn't this simpler? Is this not your natural state?", "default", "down", "angry", "upset")
        call her_kneel("...","annoyed","down")
        call luna_main("now... I'll need your help for this next bit Professor.", "seductive", "right", "sad", "default")
        m "What do I need to do?"
        call luna_main("come and stand before your star student.", "angry", "down", "angry", "default")
        ">You get up out of your chair and walk over to the two girls."
        show screen blktone
        show screen blkfade
        hide screen bld1
        hide screen genie
        show screen chair_left
        show screen desk
        $ genie_chibi_xpos = -20
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "images/animation/06_jerking_01.png"
        show screen g_c_u
        with fade
        hide screen blktone
        hide screen blkfade
        with d5
        pause
        ">Hermione looks up at you with a pleading expression."
        call her_kneel("[genie_name]... please... what's going on?","mad","worried",tears="soft")
        call luna_main("I said that you're here to sell a favour.", "angry", "down", "angry", "upset")
        call luna_main("Isn't that you want? To sell favours to dumbledore?", "seductive", "left_stare", "sad", "default")
        call her_kneel("I want... I want \"gryffindor\" to win the house cup...","open","down")
        if gryffindor > slytherin:
            call luna_main("But \"gryffindor\" is already ahead by [gryffindor-slytherin] points...", "angry", "down", "raised", "pout")
            call luna_main("do you really think that they need any more points to win?", "angry", "down", "sad", "default")
            call her_kneel("...","soft","squintL")
        else:
            call luna_main("do you really think it's fair for you to win by selling your body?", "mad", "down", "angry", "upset")
            call luna_main("*tch* *tch* *tch* what would your parents think?", "angry", "down", "angry", "pout")
            call her_kneel("they wouldn't understand...","annoyed","angryL")
        ">Luna puts her hand in your robes and quickly pulls out your hardening cock."
        $ luna_r_arm = 3
        $ luna_flip = 1
        $ luna_xpos = 640
        $ hermione_head_xpos = 590
        $ hermione_head_ypos = 390
        $ genie_sprite_xpos = 550
        call gen_main("!!!", 4, 2)
        call luna_main("Just admit it...", "mad", "left_stare", "sad", "default")
        call luna_main("you're a slut...", "doubtful", "left_stare", "default", "default")
        call her_kneel("{size=-5}no... I'm... a good student...{/size}","open","baseL")
        pause
        ">Luna starts sliding her smooth hand up and down your cock."
        call luna_main("hmmmm... I'm not so sure a good student would do this...", "seductive", "right", "sad", "pout")
        call her_kneel("...","soft","squintL")
        call luna_main("kneel willingly in front of their headmaster..", "angry", "down", "angry", "default")
        call her_kneel("...","grin","ahegao")
        call luna_main("naked...", "mad", "left_stare", "angry", "default")
        call her_kneel("...","angry","down_raised")
        call luna_main("While another student jerks him off...", "seductive", "right", "sad", "default")
        call her_kneel("...","soft","ahegao")
        call luna_main("Waiting patiently to be covered in cum...", "mad", "down", "sad", "grin")
        call her_kneel("{image=textheart}{image=textheart}{image=textheart}","grin","dead")
        pause
        call luna_main("in fact, I can think of only one sort of student who'd do that...", "seductive", "down", "angry", "default")
        call luna_main("do you know what sort of student that is hermione?", "angry", "left_stare", "sad", "default")
        call her_kneel("ah...{image=textheart} a...","soft","squintL")
        call luna_main("Mhmmm, go on...", "seductive", "down", "angry", "default")
        call her_kneel("ah... {p}a slut...{image=textheart}","open","baseL")
        call luna_main("good girl...", "seductive", "down", "sad", "default")
        call her_kneel("{image=textheart}{image=textheart}{image=textheart}","grin","dead")
        m "Ah... almost there [luna_name]..."
        ">Luna gives your cock a hard squeeze."
        g9 "Ah!"
        call luna_main("not yet old man!", "mad", "default", "mad", "angry")
        call luna_main("she hasn't learnt her lesson yet!", "mad", "down", "mad", "default")
        m "What else does she need to do?"
        call luna_main("...", "angry", "right", "angry", "pout")
        call luna_main("Lick it...", "mad", "down", "sad", "angry")
        call her_kneel("...","shock","wide")
        call her_kneel("OK...","soft","squintL")
        ">Hermione opens her mouth and puts out her tongue."
        call her_kneel("ah...","open_wide_tongue","squintL")
        call luna_main("...", "angry", "left_stare", "angry", "angry")
        call luna_main("seems like I have to do everything then...", "doubtful", "right", "angry", "upset")
        ">Luna pulls you forward, harshly, by your cock into Hermione's open mouth."
        g4 "!!!"
        $ luna_xpos += 45
        $ genie_sprite_xpos += 45
        $ luna_xpos += 10
        $ genie_sprite_xpos += 10
        $ hermione_kneel_cock = True
        call her_kneel("...","open_wide_tongue","ahegao")
        ">Hermione starts running her tongue along the length of your cock, lubricating it while Luna continues to stroke."
        g4 "Ah!!!"
        g4 "This is it sluts!"
        call luna_main("do it...", "seductive", "default", "sad", "default")
        call her_kneel("mmmm...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
        call luna_main("cover the slut...", "angry", "down", "mad", "default")
        g9  "Argh! by the gods {size=+10}YES!{/size}"
        $ luna_xpos -= 45
        $ genie_sprite_xpos -= 45
        $ luna_xpos -= 10
        $ genie_sprite_xpos -= 10
        $ hermione_kneel_cock = False
        g9  "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
        show screen white
        pause.1
        $ luna_r_arm = 4
        hide screen white
        pause.2
        $ uni_sperm = True
        $ u_sperm = "characters/hermione/face/auto_07.png"
        show screen white
        pause .1
        hide screen white
        with hpunch
        $ luna_r_arm = 3
        ">You erupt over Hermione's face, coating her in a thick layer of spunk."
        call her_kneel("!!!!","silly","ahegao_raised",cheeks="blush")
        g9 "{size=+10}YES!{/size}"
        call luna_main("mmmm, good girl...", "seductive", "down", "sad", "default")
        ">Luna's hand slowly continues to stroke your cock, jerking out the last couple of drops of sperm onto Hermione's nose."
        pause
        call luna_main("perfect...", "default", "down", "sad", "default")
        call her_kneel("...","grin","dead")
        m "that was fantastic!"
        $ luna_r_arm = 1
        hide screen genie_sprite
        with d3
        hide screen bld1
        show screen genie
        hide screen chair_left
        hide screen desk
        hide screen g_c_u
        call luna_main("...", "seductive", "left_stare", "sad", "default")
        $ luna_flip = -1
        $ luna_xpos = 300
        if luna_addicted == True:
            call luna_main("well it's not over yet...", "seductive", "right", "sad", "default")
            call her_kneel("...what?","mad","wide",cheeks="blush")
            call her_kneel("why?","open","baseL",cheeks="blush")
            call luna_main("Just look at you!", "wide", "down", "sad", "grin")
            call luna_main("Covered in the [l_genie_name]s delicous cum!", "seductive", "down", "sad", "default")
            call her_kneel("delicous...","disgust","down_raised")
            call her_kneel("Do you want me to clean myself up?","upset","wink")
            call luna_main("And waste all that perfectly good cum one some tart like you?!", "wide", "down", "angry", "angry")
            call luna_main("No, I think I'll have to clean this mess up myself...", "wide", "down", "sad", "default")
            ">You notice a hunger in Luna's eyes..."
            call her_kneel("does that mean...","disgust","glance")
            call luna_main("come on hermione, we don't have all day...", "angry", "right", "angry", "upset")
            call luna_main("tranfiguration starts in 5 minutes...", "angry", "right", "mad", "angry")
            call luna_main("so hurry up...", "angry", "down", "angry", "upset")
            call her_kneel("(I can't be late to mcgonagall's class...)","annoyed","down")
            call her_kneel("I'm not sure what you want me to do...","annoyed","angryL")
            call luna_main("stand up now slut...", "doubtful", "down", "mad", "upset")
            call her_kneel("...","annoyed","angry")
            hide screen hermione_kneel
            $ hermione_xpos = 480
            show screen hermione_main
            with d3
            ">Hermione slowly stands up, her face still covered in cum..."
            $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
            call luna_main("mmmmm... look at you... you smell so good...", "default", "empty", "sad", "default")
            $ luna_xpos = 600
            $ luna_r_arm = 2
            ">Luna moves closer to Hermione before picking up a strand of cum with her finger and moving it to her mouth."
            call her_main("!!!","angry","wide")
            m "(woah...)"
            $ luna_xpos = 630
            call luna_main("mmmmm... you taste even better...", "closed_happy", "default", "sad", "default")
            call her_main("...","open","worriedCl")
            ">Hermione stands still, letting luna slowly wipe the cum from her face..."
            $ u_sperm = "characters/hermione/face/auto_08.png"
            call her_main("...","shock","worriedCl")
            call luna_main("mmmmm...", "closed_happy", "default", "sad", "cheeks_full")
            ">Luna slowly fills her mouth with cum before eventually swallowing."
            call luna_main("*gulp*", "seductive", "empty", "sad", "default")
            ">Eventually she finally gets the last strand into her mouth."
            $ uni_sperm = False
            call her_main("...","disgust","down_raised")
            call luna_main("...", "closed_happy", "default", "sad", "cheeks_full")
            call luna_main("*gulp*", "seductive", "empty", "sad", "default")
            call her_main("...","annoyed","worriedL")
            $ luna_l_arm = 2
            $ luna_flip = 1
            $ luna_xpos = 300
            call luna_main("Well, I better be off to... class...", "default", "right", "angry", "default")
            call luna_main("Good bye [l_genie_name]...", "seductive", "default", "sad", "default")
            call luna_main("Good bye slut...", "angry", "right", "angry", "upset")
            ">Luna quietly exits the room."
            hide screen luna_chibi
            hide screen luna
            call luna_reset
            $ luna_busy = True
            with d3
            ">Hermione quietly gets dressed, a shocked look on her face..."
        else:
            call luna_main("well it's not over yet...", "doubtful", "right", "angry", "default")
            call her_kneel("...what?","mad","wide",cheeks="blush")
            call her_kneel("why?","open","baseL",cheeks="blush")
            call luna_main("Just look at the mess you made!", "angry", "down", "angry", "upset")
            call luna_main("You'll have to clean that up before you can go to class!", "angry", "down", "mad", "default")
            call her_kneel("well normally I just go the prefect bathroom...","annoyed","worriedL")
            call her_kneel("or I use a towel...","annoyed","down")
            call her_kneel("{size=-5}but never scourgify for some reason...{/size}","annoyed","angryL")
            call luna_main("And waste all that perfectly good cum the Professor gave you?!", "wide", "down", "angry", "angry")
            call luna_main("No, I think I'll have to stay here and make sure you dispose of it properly...", "angry", "down", "angry", "default")
            call her_kneel("does that mean...","angry","wide")
            call luna_main("come on hermione, we don't have all day...", "seductive", "down", "sad", "default")
            call luna_main("tranfiguration starts in 5 minutes...", "angry", "down", "angry", "upset")
            call her_kneel("(I can't be late to mcgonagall's class...)","angry","down_raised")
            call luna_main("now dispose of that cum like a good little slut...", "mad", "down", "sad", "default")
            call her_kneel("...","soft","ahegao")
            ">Hermione slowly starts using her fingers to push your cum into her mouth."
            $ luna_l_arm = 4
            $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
            call luna_main("mmmmm... that's it... make sure you get it all slut...", "seductive", "down", "sad", "default")
            m "(woah...)"
            ">Hermione slowly continues to clear her face of cum."
            $ u_sperm = "characters/hermione/face/auto_08.png"
            call her_kneel("...","full_cum","dead") #Cheek full
            ">She fills her mouth with cum before eventually swallowing."
            call her_kneel("*gulp*","cum","worriedCl")
            ">Eventually she finally gets the last strand into her mouth."
            $ uni_sperm = False
            call her_kneel("...","full_cum","dead") #Cheek full
            call luna_main("see, good sluts don't waste anyting do they?", "seductive", "down", "sad", "grin")
            call her_kneel("...","full_cum","dead") #Cheek full
            $ luna_l_arm = 2
            call luna_main("Well, I better be off to... class...", "default", "right", "angry", "default")
            call luna_main("Good bye [l_genie_name]...", "seductive", "default", "sad", "default")
            call luna_main("Good bye slut...", "angry", "right", "angry", "upset")
            ">Luna quietly exits the room."
            hide screen luna_chibi
            hide screen luna
            with d3
            ">Hermione swallows the last mouthful of your cum."
            call her_kneel("*gulp*","cum","worriedCl")
            call her_kneel("mmmm...{image=textheart}{image=textheart}{image=textheart}","grin","dead")
            ">She picks herself up from the floor gracefully. Getting dressed before turning to address you."
        $ hermione_wear_panties = True
        $ hermione_wear_skirt = True
        $ hermione_wear_top = True
        $ hermione_wear_bra = True
        $ hermione_SC.chibi.xpos = 500 #Near the desk: 400. (210 - standing on desk.)
        $ hermione_SC.chibi.ypos = 260#Default: 250. (180- standing on desk.)
        show screen hermione_blink #Hermione stands still.
        call update_her_uniform
        hide screen hermione_kneel
        with d3
        call her_main("[genie_name], what on earth was that all about?!","scream","angryCl")
        call her_main("Why on earth was Luna in here?","annoyed","angryL")
        call her_main("how on earth does she know about me selling favours?","angry","angry")
        if luna_addicted == True:
            call her_main("And {size=+5}why on earth{/size} does she love the taste of your cum?","angry","angry",emote="01")
        m "I can explain everything..."
        call her_main("Please do...","annoyed","annoyed")
        m "do you remember how you yourself described Luna lovegood as crazy?"
        call her_main("Of course. Everyone knows she's Loony Luna.","annoyed","angryL")
        m "Well I was testing out some new magic..."
        m "And I'm attempting to cure her of her previous condition..."
        m "(I hope she believes this schlock...)"
        call her_main("Really?","shock","wide")
        call her_main("But isn't messing around with her mind a little...","soft","squintL")
        call her_main("unethical?","angry","down_raised")
        m "Yes, well normally you'd be right, but this is more of a curing of an existing mental condition."
        m "Think about it like I'm trying to cure her of Aspergers disease."
        call her_main("Actually sir, Aspergers has been reclassified as part of the autism spectrum and is no longer considered it's own disease.","open","closed")
        m "..."
        m "(Of course she'd know that...)"
        m "Well anyway, my point is there's nothing untoward happening."
        call her_main("...","annoyed","angryL")
        call her_main("Alright then...","open","closed")
        call her_main("But why is she so mean?","open","worriedCl")
        m "I'm not sure. Maybe that's the true her."
        call her_main("I guess that's not impossible...","annoyed","down")
        call her_main("But why was she jerking you off?","open","down")
        m "Oh um..."
        m "Well that sort of just happened during my evaluation..."
        m "She wanted to help her fathers magazine anyway possible, and one thing led to another..."
        if luna_addicted == True:
            call her_main("what about the her loving the taste of your sperm?","angry","suspicious",cheeks="blush")
            m "Honestly I'm not really sure about that."
            m "I think that's just her being weird..."
        call her_main("...","annoyed","angry")
        call her_main("ugh, fine...","annoyed","baseL")
        call her_main("I guess...","annoyed","angryL",cheeks="blush")
        m "So you don't mind helping out with her in the future?"
        call her_main("What? I have to spend more time with her?","soft","wide")
        call her_main("But she's weird...","open","worriedCl",cheeks="blush")
        m "We can work on that. Besides, don't you want to help out one of your friends?"
        call her_main("Hmmm, I suppose that you're right [genie_name].","annoyed","closed")
        call her_main("I can't imagine that the daydreaming Luna would do too well in the real world.","open","squint",cheeks="blush")
        call her_main("and as her friend It's my responsibility to try and save her from that!","open","baseL",cheeks="blush")
        call her_main("!!!","soft","wide")
        call her_main("Maybe we could even have study sessions together!","grin","baseL")
        call her_main("I've always wanted someone to study with! Normally it's only ever Harry and I'm pretty sure he's just there to stare at my boobs...","annoyed","annoyed")
        call her_main("(Not that I mind...)","open","baseL")
        menu:
            "-Encourage friendship-":
                $ luna_friendship = 1
                $ luna_hatred = 0
                m "I'm sure she'd be happy to spend some more time with you."
                call her_main("Do you think so sir? She seemed pretty mean today.","open","down")
                m "She'll come around, just give it time."
                call her_main("I hope so sir! A ravenclaw study buddy would be great!","smile","happyCl",emote="06")
                m "(more like fuck buddy...)"
                call her_main("...","base","happyCl")
            "-discourage friendship-":
                $ luna_friendship = 0
                $ luna_hatred = 1
                m "I'm not so sure about that. She seemed pretty harsh today."
                call her_main("hmmm, you're probably right.","annoyed","base")
                m "Maybe you should fight fire with fire?"
                call her_main("And be mean in return?","disgust","down_raised")
                call her_main("I don't know [genie_name]... She is my friend...","clench","down_raised")
        m "Anyway, thanks for your help today."
        call her_main("anything for my friends [genie_name]...","soft","squintL")
        m "(Does that mean me?)"
        m "Yes, well, 60 points to \"gryffindor\"!"
        $ gryffindor += 60
        call her_main("Thank you [genie_name]...","open","baseL")
        $ luna_busy = True
        jump end_hg_pf

    elif luna_corruption <= 12: #second time
        $ luna_corruption += 1
        $ luna_payout = 150
        $ hermione_payout = 40
        m "How would you feel about another handjob involving Miss Granger?"
        call luna_main("Really?", "angry", "default", "raised", "upset")
        call luna_main("You want to bring her into this again?", "mad", "default", "angry", "angry")
        m "If it's not too much of an issue..."
        call luna_main("*Hmph* so long as you pay me I don't care about you dragging that little hussie up here...", "doubtful", "right", "angry", "upset")
        m "Fantastic! I'll summon her now."
        call luna_main("...", "doubtful", "right", "angry", "angry")
        ">You summon Hermione to your office."
        call play_sound("door") #Sound of a door opening.
        $ hermione_SC.chibi.xpos = 600 #Near the desk.
        show screen hermione_blink #Hermione stands still.
        $ luna_flip = -1
        $ luna_r_arm = 2
        $ luna_xpos = 390
        call update_her_uniform
        pause
        call her_main("Hello [genie_name]...","base","base")
        call her_main("Hello Luna...","open","suspicious")
        call luna_main("Hermione...", "doubtful", "default", "angry", "upset")
        call her_main("What are you doing here?","annoyed","angryL")
        call luna_main("Getting ready to Jerk dumbledore off onto your face...", "seductive", "default", "angry", "default")
        call her_main("Oh...","annoyed","base")
        call her_main("again?","upset","wink")
        m "Can you blame me?"
        call her_main("I suppose not...","grin","baseL")
        call luna_main("well then...", "mad", "default", "angry", "upset")
        call her_main("what?","annoyed","angry")
        call luna_main("hurry up and strip so we can get this over with...", "doubtful", "right", "angry", "upset")
        call her_main("Why do I always have to strip?","scream","angryCl")
        call luna_main("because I said so...", "doubtful", "default", "default", "angry")
        call luna_main("unless you don't want to...", "angry", "right", "default", "upset")
        call her_main("I suppose I don't mind. It just seems a little unfair that it's only me though...","annoyed","ahegao")
        call luna_main("tough.", "doubtful", "default", "mad", "angry")
        menu:
            "-make luna strip-":
                m "Now, now, Miss Granger is right. It seems only fair for both of you to go nude."
                call luna_main("...", "wide", "right", "angry", "upset")
                call her_main("Come on Luna... we're both girls, there's no need to be embarrassed.","grin","baseL")
                call luna_main("embarrassed? hardly.", "doubtful", "right", "angry", "upset")
                call her_main("well hurry up and strip then. I thought you wanted to get this over with?","smile","baseL")
                call luna_main(".........", "angry", "default", "mad", "upset")
                call luna_main("Fine... But I expect extra for this [l_genie_name]!", "default", "right", "angry", "upset")
            "-agree with Luna-":
                m "Now, now, Listen to luna [hermione_name]."
                call her_main("What? Why?","angry","angry")
                m "Well, if we're being honest, it's mainly because I want to see your naked body again..."
                call her_main("oh... well alright then.","base","squint")
                call luna_main("and you don't want to see me naked?", "mad", "default", "angry", "upset")
                m "I didn't mean it like-"
                call luna_main("*hmph* I suppose I'll strip then [l_genie_name]... Just so you remember who has the better body.", "seductive", "default", "angry", "upset")
                call luna_main("But I expect extra for this [l_genie_name]!", "angry", "right", "angry", "angry")
        m "sure. I'll add another 40 gold."
        $ luna_payout += 40
        call her_main("If she's getting extra then I want some more points!","scream","angryCl")
        m "whatever. An extra 20 points for gryffindor then."
        $ hermione_payout += 20
        call her_main("yay!","smile","baseL")
        call luna_main("I still can't believe you get excited over points.", "doubtful", "up", "angry", "upset")
        call her_main("Why? Don't you want to see that look of excitement on your friends faces when they win the house cup?","base","squint")
        call her_main("and the look of dissapointment on those nasty slytherins faces when they lose!","base","ahegao_raised")
        call luna_main("pfft, friends...", "default", "right", "mad", "upset")
        call her_main("aww... Luna...","open","worried")
        call luna_main("Just shut up and strip slut.", "mad", "default", "mad", "angry")
        call her_main("fine...","annoyed","down")
        show screen blkfade
        with d3
        ">Luna and Hermione both strip in front of you."
        ">You can hardly believe your eyes as they slowly strip down in front of each other."
        ">As they're putting their clothes in a pile you slowly get up from your desk and whip your cock out from in between your robes."
        call luna_main("On your knees then, slut...", "seductive", "left_stare", "angry", "default")
        hide screen hermione_main
        $ hermione_SC.chibi.xpos = 40 #40 = Near Luna
        $ hermione_SC.chibi.ypos = 60
        $ h_c_u_pic = "characters/hermione/chibis/dance/08_sits.png"
        $ hermione_head_xpos=590
        show screen h_c_u
        with d3
        hide screen bld1
        hide screen genie
        show screen chair_left
        show screen desk
        $ genie_chibi_xpos = -20
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "images/animation/06_jerking_01.png"
        show screen g_c_u
        with fade
        $ luna_r_arm = 3
        $ luna_flip = 1
        $ luna_xpos = 640
        $ hermione_head_xpos = 590
        $ hermione_head_ypos = 390
        $ genie_sprite_xpos = 550
        show screen genie_sprite

        $ luna_wear_top = False
        $ luna_wear_bra = False
        $ luna_wear_skirt = False
        $ luna_wear_panties = False
        hide screen blkfade
        with d3
        call her_kneel("...","base","closed")
        ">Luna slowly starts jerking your cock in front of Hermione's face."
        ">Her technique is rough and inexperienced, but decent enough."
        $ luna_r_arm = 3
        call luna_main("mmmm, that's it [l_genie_name]...", "seductive", "left_stare", "angry", "default")
        call her_kneel("...","annoyed","worriedL")
        call her_kneel("......","annoyed","angry")
        call her_kneel(".........","annoyed","annoyed")
        call luna_main("something wrong hermione?", "angry", "down", "angry", "upset")
        call her_kneel("no...","annoyed","down")
        call luna_main("good. maybe you sh-", "seductive", "down", "angry", "default")
        call her_kneel("You're doing it all wrong!","scream","angry",emote="01")
        call luna_main("What?", "wide", "down", "default", "upset")
        call her_kneel("that's not how he likes it.","annoyed","angryL")
        call luna_main("are you sure? He seems to be enjoying it to me...", "angry", "down", "angry", "angry")
        call her_kneel("he's just being nice. You need to focus on the tip with the palm of your hand more.","annoyed","angry")
        call her_kneel("otherwise he doesn't shoot nearly as much...","annoyed","annoyed")
        call luna_main("*hmph*", "angry", "right", "angry", "upset")
        call luna_main("Why don't we ask the old pervert who he prefers then...", "mad", "down", "mad", "upset")
        call her_kneel("alright. Who do you prefer [genie_name]?","annoyed","base")
        menu:
            "-Luna-":
                call her_kneel("What!","angry","angry",emote="01")
                call her_kneel("That's ridiculous! I'm much better than her at giving handjobs!","annoyed","annoyed")
                call luna_main("It's about more than just jerking his cock hermione.", "angry", "left_stare", "default", "default")
                call her_kneel("like what?","annoyed","angryL")
                call luna_main("it's about excitement...", "seductive", "left_stare", "angry", "default")
                ">Luna gives your cock light squeeze."
                m "Ah..."
                call her_kneel("*hmph* at least let me show you how it's done...","disgust","glance")
                call her_kneel("i'm sure you'll find plenty of ways to \'excite\' him from the floor.","annoyed","annoyed")
            "-Hermione-":
                call luna_main("WHAT?", "wide", "default", "mad", "angry")
                ">Luna gives your cock a painful squeeze, bordering on bruising it."
                call gen_main("AH!", 2, 4)
                call her_kneel("Don't take it too hard Luna, I just have a \'little\' more experience.","base","happyCl")
                ">Luna lets go of your cock."
                $ genie_sprite_exp = "characters/genie/exp_1.png"
                $ luna_r_arm = 1
                call luna_main("*hmph*, I suppose you're right. You've probably spent all year with your hands wrapped around any cock you could find.", "doubtful", "left_stare", "mad", "angry")
                call her_kneel("Hey!","annoyed","annoyed")
                call luna_main("Am I wrong?", "angry", "left_stare", "angry", "default")
                call her_kneel("...","disgust","down_raised")
                call her_kneel("at least let me show you how it's done...","annoyed","annoyed")
        call luna_main("whatever...", "doubtful", "right", "angry", "upset")
        call her_kneel("...","base","baseL")
        show screen blkfade
        with d3
        $ hermione_zorder = 4 #CHANGE BACK TO 5 AFTER THIS
        hide screen hermione_kneel
        ">Hermione grabs a hold of your cock as she and Luna switch places."
        ">You're unable to deny that she's much more experienced that Luna, quickly bringing you to the edge."
        $ luna_ypos = 250
        $ hermione_right_arm = "characters/hermione/body/arms/right/dick.png"
        $ genie_sprite_base = "characters/genie/base_2.png"
        $ genie_sprite_exp = "characters/genie/exp_4.png"
        $ hermione_xpos = 590

        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        $ hermione_wear_skirt = False
        $ hermione_wear_panties = False
        call update_her_uniform

        show screen hermione_main

        hide screen blkfade
        with d3
        m "Ah... this is it [hermione_name]... not long now."
        call her_main("mmm, that's it [genie_name]. just enjoy yourself.","open","baseL")
        call luna_main("as if he could...", "angry", "right", "angry", "upset")
        g9 "ah..."
        call luna_main("go on [l_genie_name], tell her i'm better.", "mad", "up", "angry", "upset")
        ">you can barely mutter more than a guttural moan in response."
        g9 "Ugh..."
        call luna_main("...", "doubtful", "up", "angry", "upset")
        call luna_main("tell her i'm better!", "doubtful", "up", "mad", "angry")
        g9 "mmmm"
        call her_main("I'm not sure he can hear you... He must be enjoying himself too much.","open","down")
        call her_main("speaking of which... are you ready [genie_name]?","soft","squintL")
        g9 "Ugh... yes... here it comes sluts!"
        call her_main("well why don't I show Luna here how to give a proper handjob.","base","down")
        call luna_main("...", "seductive", "right", "sad", "upset")
        call her_main("See, he likes it when you do this with your palm...","base","suspicious")
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        $ luna_cum = 12
        $ luna_wear_cum = True
        g4 "{size=+5}ARGH! by the gods YES!!!{/size}"
        g4 "{size=+5}WHAT ARE YOU DOING GIRL!?!?!{/size}"
        ">Your cock explodes over Luna's face, covering her until you can barely make out her features."
        $ luna_cum = 12
        $ luna_wear_cum = True
        call luna_main("mmmmm...", "wide", "default", "sad", "default")
        call her_main("that's it, just let out all that {b}nasty{/b} cum.","grin","ahegao")
        $ g_c_u_pic = "images/animation/06_jerking_01.png"
        $ genie_sprite_base = "characters/genie/base_2.png"
        $ luna_cum = 12
        ">Luna then collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
        call luna_main("{image=textheart}{image=textheart}{image=textheart}", "angry", "left_stare", "angry", "default")
        call luna_main("it's not nasty!", "seductive", "left_stare", "angry", "default")
        call her_main("oh that's right... I almost forgot how much of a cumslut you are.","angry","down_raised")
        call luna_main("I am not!", "angry", "up", "angry", "upset")
        call her_main("so you're not going to eat all of that \'delicous\' cum on your face then?","base","suspicious")
        call luna_main("...", "seductive", "left_stare", "angry", "default")
        ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
        $ luna_cum = 13
        call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
        call her_main("that's it Cumslut...","base","glance")
        call luna_main("{image=textheart}{image=textheart}{image=textheart}", "closed_happy", "left_stare", "sad", "default")
        pause
        $ luna_cum = 14
        call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
        call her_main("keep going...","base","down")
        call luna_main("{image=textheart}{image=textheart}{image=textheart}", "closed_happy", "left_stare", "sad", "default")
        $ luna_cum = 15
        call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
        call her_main("mmmm...","grin","baseL")
        call luna_main("{image=textheart}{image=textheart}{image=textheart}", "closed_happy", "left_stare", "sad", "default")
        $ luna_wear_cum = False
        call luna_main("...", "seductive", "empty", "sad", "cheeks_full")
        call luna_main("*gulp*", "closed_happy", "left_stare", "sad", "default")
        call luna_main("ah...", "closed_happy", "left_stare", "sad", "default")
        call luna_main("amazing...", "seductive", "up", "sad", "default")
        call luna_main("I didn't know it was possible for someone to cum so much...", "default", "up", "sad", "default")
        call her_main("well of course you didn't. I'm surprised you were able to make [genie_name] cum at all!","open","closed")
        call her_main("what with that shoddy technique of yours...","annoyed","suspicious")
        call luna_main("it's not that bad...", "angry", "up", "sad", "upset")
        call her_main("whatever you have to tell yourself...","open","closed")
        call luna_main("...", "mad", "up", "angry", "upset")
        call luna_main("fine... i'm not as good at giving hand jobs as you...", "doubtful", "right", "default", "upset")
        call luna_main("but that's only because you've spent the entire year in here whoring yourself out to our headmaster!", "doubtful", "up", "mad", "upset")
        call her_main("well I can teach you a few things if you'd like.","smile","baseL")
        call luna_main("what?", "angry", "up", "default", "pout")
        call luna_main("why would you help me?", "angry", "up", "sad", "upset")
        call her_main("I wouldn't be doing it for free...","open","baseL")
        call luna_main("...", "seductive", "left_stare", "angry", "upset")
        call luna_main("what do you want?", "doubtful", "up", "sad", "angry")
        call her_main("before I tell you, you have to answer one question...","open","baseL")
        m "(ugh... I need to sit down after all that.)"
        show screen blkfade
        with d3
        ">You slowly move back to your desk and sit down while hermione and luna continue talking."
        $ hermione_xpos = 550
        $ luna_ypos = 0
        $ luna_xpos = 450
        $ luna_flip = -1
        $ hermione_right_arm = "characters/hermione/body/arms/right/right_1.png"
        $ hermione_zorder = 5
        hide screen genie_sprite
        show screen genie
        hide screen chair_left
        hide screen desk
        hide screen g_c_u
        $ hermione_SC.chibi.xpos = 600 #Near the desk: 400. (210 - standing on desk.)
        $ hermione_SC.chibi.ypos = 260#Default: 250. (180- standing on desk.)
        show screen hermione_blink #Hermione stands still.
        call update_her_uniform
        hide screen blkfade
        with d3
        call luna_main("alright...", "doubtful", "default", "angry", "upset")
        call her_main("how are your grades?","base","base")
        call luna_main("WHAT?", "wide", "default", "sad", "open")
        call luna_main("my grades? why do you care?", "angry", "default", "angry", "pout")
        call her_main("it's a simple question...","base","down")
        call luna_main("well I'm not going to answer it...", "mad", "default", "mad", "angry")
        call her_main("if you don't want to answer, I'm sure dumbledore would be more than happy to...","base","glance")
        call luna_main("...", "doubtful", "default", "mad", "angry")
        call luna_main("......", "mad", "default", "angry", "angry")
        call luna_main(".........", "angry", "default", "angry", "upset")
        call luna_main(".............", "doubtful", "right", "angry", "upset")
        call luna_main("fine...", "doubtful", "right", "sad", "upset")
        ">Luna slowly lists her marks across all subjects, most of them bordering on a pass and fail with the exception of divination."
        call her_main("what? so low? How do you expect to get a job at the ministry of magic with marks like that?","scream","wide_stare")
        call luna_main("...", "doubtful", "down", "sad", "upset")
        call her_main("at this rate you'll have to get a job in the muggle world.","disgust","down_raised")
        call luna_main("you think I don't know that? why do you think I agreed to all this in the first place...", "angry", "default", "angry", "angry")
        call luna_main("Just stop humiliating me and list your stupid demand!", "mad", "default", "angry", "angry")
        call luna_main("What is it anyway? Do you expect me to walk around the school half naked?", "doubtful", "right", "angry", "angry")
        call her_main("Of course not...","open","worried")
        call luna_main("then what?", "angry", "default", "mad", "upset")
        call her_main("In exchange for me teaching you how to be a better lover, I want you to be my study buddy.","open","closed")
        call luna_main("...", "doubtful", "default", "angry", "angry")
        call luna_main("what?", "wide", "default", "sad", "upset")
        call luna_main("why would you of all people need a study buddy? Aren't your grades perfect?", "doubtful", "default", "angry", "upset")
        call her_main("of course... but that's not why I want a study buddy.","soft","baseL")
        call her_main("It gets lonely in the library sometimes...","annoyed","angryL")
        call her_main("Plus I've always wanted a ravenclaw to study with, but all the other girls refuse to even talk to me.","open","worried")
        call her_main("and harry and ron have just started staring at my tits the whole time.","open","angryCl")
        call her_main("{size=-5}not that I really mind...{/size}","base","ahegao_raised")
        call her_main("but think about all the fun we can have! you can even quiz me on advanced transmogrification spells!","smile","happyCl")
        call luna_main("...", "angry", "default", "angry", "upset")
        call her_main("not to mention we can work on your grades as well!","base","happyCl")
        call her_main("If you work hard we can probably get them up before the O.W.L.s!","grin","baseL")
        call luna_main("whatever... as long as you teach me how to wring as much gold out of the old mans balls as possible I don't care...", "doubtful", "right", "angry", "pout")
        call her_main("YAY!","grin","worriedCl")
        m "I'm still here you know!"
        call her_main("of course Professor...","grin","baseL")
        call luna_main("...", "doubtful", "right", "default", "upset")
        call her_main("well come on then luna, we've still got a bit of time before classes, let's head to the library!","smile","baseL")
        call luna_main("you want to start now?", "wide", "default", "angry", "upset")
        call her_main("no offense, but with your grades the way they are...","grin","worriedCl",emote="05")
        call her_main("well we don't have much time to spare...","base","worriedCl")
        m "This isn't going to impact our \"lessons\" is it [hermione_name]?"
        call her_main("of course not [genie_name]...","grin","baseL")
        call luna_main("it better not...", "angry", "default", "angry", "upset")
        m "alright then, in that case, here's your payment."
        $ gryffindor += hermione_payout
        m "[hermione_payout] points to \'gryffindor\'!"
        call her_main("thank you [genie_name].","base","closed")
        $ luna_gold += luna_payout
        $ gold -= luna_payout
        m "And [luna_payout] gold for Luna."
        ">You hand Luna the pile of coins."
        $ luna_flip = 1
        call luna_main("Thank you [l_genie_name]...", "closed", "right", "mad", "upset")
        ">Luna and hermione quickly get dressed before quickly leaving the room together."
        $ luna_wear_skirt = True
        $ luna_wear_top = True
        $ luna_wear_panties = True
        $ luna_wear_bra = True
        $ hermione_wear_skirt = True
        $ hermione_wear_top = True
        $ hermione_wear_panties = True
        $ hermione_wear_bra = True
        call update_her_uniform
        call her_main("this is going to be so much FUN!","grin","ahegao")
        call luna_main("(What have I agreed to)", "doubtful", "down", "sad", "upset")
        hide screen luna
        hide screen luna_chibi
        $ luna_busy = True
        jump end_hg_pf
        # end scene

    else: #third handjob event, needs to be repeatable
        if luna_corruption <= 13:
            $ luna_corruption += 1
        label luna_handjob_hermione_call:
            pass
        m "How about another handjob [luna_name]?"
        call luna_main("sure... do you want hermione here as well?", "doubtful", "right", "angry", "upset")
        m "You read my mind!"
        call luna_main("alright. but I expect to be the one doing the... job.", "angry", "right", "default", "upset")
        m "if you insist."
        call luna_main("...", "seductive", "default", "default", "upset")
        call luna_main("just hurry up and bring her up here...", "seductive", "right", "default", "upset")
        ">You summon hermione to your office."
        call play_sound("door") #Sound of a door opening.
        $ hermione_SC.chibi.xpos = 600 #Near the desk.
        show screen hermione_blink #Hermione stands still.
        $ luna_flip = -1
        $ luna_r_arm = 2
        $ luna_xpos = 390
        call update_her_uniform
        pause
        call her_main("hello [genie_name]!","base","happyCl")
        call her_main("hello luna!","smile","happyCl")
        m "You seem cheerful."
        call her_main("why wouldn't I be? are we going to work on handjobs today?","open","baseL")
        call luna_main("just hurry up and get on your knees slut...", "seductive", "default", "angry", "angry")
        call her_main("someone's eager!","smile","happyCl",emote="06")
        call luna_main("...", "doubtful", "default", "angry", "upset")
        ">You stand up from your desk while hermione slowly strips and kneels in front of you."
        hide screen hermione_main
        $ hermione_SC.chibi.xpos = 40 #40 = Near Luna
        $ hermione_SC.chibi.ypos = 60
        $ h_c_u_pic = "characters/hermione/chibis/dance/08_sits.png"
        $ hermione_head_xpos=390
        show screen h_c_u
        with d3
        hide screen bld1
        hide screen genie
        show screen chair_left
        show screen desk
        $ genie_chibi_xpos = -20
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "images/animation/06_jerking_01.png"
        $ genie_sprite_base = "characters/genie/base_4.png"
        show screen g_c_u
        with fade
        $ luna_r_arm = 2
        $ luna_flip = 1
        $ luna_xpos = 640
        $ hermione_head_xpos = 590
        $ hermione_head_ypos = 390
        $ genie_sprite_xpos = 550
        $ hermione_wear_skirt = False
        $ hermione_wear_top = False
        $ hermione_wear_panties = False
        $ hermione_wear_bra = False
        call update_her_uniform
        show screen genie_sprite
        call her_kneel("Aren't you going to get naked as well Luna?","annoyed","angryL")
        call luna_main("I don't see why I should have to...", "angry", "right", "mad", "upset")
        call her_kneel("I told you before, he like's it better if you're naked while you stroke it.","annoyed","angryL")
        call luna_main("...", "angry", "left_stare", "angry", "upset")
        call luna_main("fine...", "doubtful", "right", "sad", "upset")
        call her_kneel("good.","base","base")
        call luna_main("but I expect extra for this [l_genie_name]!", "seductive", "right", "angry", "upset")
        m "that seems fair."
        call luna_main("...", "doubtful", "default", "angry", "upset")
        show screen blkfade
        with d3
        ">Luna slowly strips as well, carefully putting her clothes in a pile next to hermione's."
        $ luna_wear_skirt = False
        $ luna_wear_top = False
        $ luna_wear_panties = False
        $ luna_wear_bra = False
        hide screen blkfade
        with d3
        call luna_main("happy now?", "angry", "default", "angry", "upset")
        m "Very."
        call luna_main("good... let's just get this over with.", "angry", "right", "mad", "upset")
        call her_kneel("...","annoyed","frown")
        call luna_main("what is it now hermione?", "doubtful", "left_stare", "angry", "upset")
        call her_kneel("Just try and act like you like it a little more, ok?","open","suspicious")
        call luna_main("whatever...", "doubtful", "right", "angry", "upset")
        call her_kneel("great!","base","down")
        $ luna_r_arm = 3
        ">Luna spits into her hand before wrapping it around your cock."
        ">She's barely started to stroke it yet you can already tell her technique has improves significantly."
        m "Mmmm, yes that's it slut."
        m "just like that."
        call luna_main("...", "seductive", "left_stare", "angry", "default")
        call her_kneel("that's good luna... now try focusing on the tip a little more, like we talked about.","base","glance")
        call luna_main("like this?", "seductive", "left_stare", "sad", "upset")
        ">Luna wraps her hand around the head of your cock, rotating her hand slightly as she pumps her hand."
        m "Ugh... yes..."
        call her_kneel("good work. now go back to the rest of the shaft.","open","closed")
        call her_kneel("try no to focus on one area too long...","open","closed")
        call luna_main("ok...", "angry", "left_stare", "sad", "default")
        ">This continues for a while longer, Luna listening intently to hermione's instructions."
        g9 "Ugh... I'm getting close!"
        call her_kneel("alright, when this happens you need to slow down a little...","base","down")
        call luna_main("really? but isn't he about to cum?", "wide", "left_stare", "sad", "angry")
        g9 "Don't slow down now!"
        call her_kneel("shhh [genie_name], I'm trying to give a lesson here!","upset","closed")
        g9 "..."
        ">Luna slows her hand back down, bringing you almost painfully back from the edge of orgasm."
        call her_kneel("he {b}was{/b} about to cum, but if you build him up and then bring him back down he'll eventually cum much harder.","grin","dead")
        call her_kneel("I read about this technique in witches weekly... it's called edging!","base","down")
        call luna_main("hmmm, and you're sure it feels better?", "seductive", "left_stare", "raised", "upset")
        call luna_main("he almost seems like he's in pain...", "seductive", "left_stare", "angry", "default")
        ">luna gives your cock a hard squeeze as she looks sadistically at your cock."
        $ genie_sprite_exp = "characters/genie/exp_2.png"
        g4 "ah!"
        $ genie_sprite_exp = "characters/genie/exp_4.png"
        call her_kneel("believe me, he'll like this much more...","open","closed")
        call her_kneel("just wait to you see how much he'll shoot once you finally {i}let{/i} him cum.","grin","ahegao")
        call luna_main("mmmmm... I like the sound of that.", "mad", "left_stare", "mad", "default")
        call luna_main("so how much longer should I do this...", "seductive", "left_stare", "default", "default")
        $ genie_sprite_exp = "characters/genie/exp_2.png"
        g4 "I can't take much more of this!"
        call her_kneel("probably not too much longer...","angry","wink")
        call her_kneel("it can get a little... frustrating if you do it for too long.","base","down")
        call luna_main("really? I don't mind that...", "mad", "left_stare", "mad", "default")
        g4 "I do!"
        call luna_main("alright then... how should I finish him off?", "seductive", "down", "angry", "default")
        call her_kneel("hmmm...","base","suspicious")
        show screen blkfade
        with d3
        $ genie_sprite_exp = "characters/genie/exp_1.png"
        ">Hermione slowly stands up and whispers something into Luna's ear before kneeling back down."
        hide screen blkfade
        with d3
        call luna_main("are you sure he'll like that?", "wide", "left_stare", "sad", "default")
        call her_kneel("trust me, he'll love it...","grin","baseL")
        m "like what?"
        call luna_main("quiet [l_genie_name]!", "mad", "default", "angry", "upset")
        ">luna gives your cock another painful squeeze before resuming stroking the length of it."
        $ genie_sprite_exp = "characters/genie/exp_2.png"
        g4 "Ah!"
        $ genie_sprite_exp = "characters/genie/exp_3.png"
        m "can you stop that?"
        call luna_main("I'll stop it once you learn to be quiet.", "doubtful", "default", "angry", "pout")
        $ genie_sprite_exp = "characters/genie/exp_1.png"
        m "..."
        call her_kneel("mmmm... that's it Luna...","soft","ahegao")
        call her_kneel("he's almost there... do it now.","grin","dead")
        call her_kneel("ah...","open_wide_tongue","squintL")
        ">Hermione opens her mouth as wide as she can while luna pulls you forward by your cock into her eager hole."
        $ luna_xpos += 45
        $ genie_sprite_xpos += 55
        $ hermione_kneel_cock = True
        $ genie_sprite_exp = "characters/genie/exp_2.png"
        g4 "!!!"
        call her_kneel("mmm...","open_wide_tongue","ahegao")
        call luna_main("there we go...", "seductive", "left_stare", "sad", "default")
        $ hermione_head_xpos -= 10
        $ hermione_head_ypos -= 5
        ">Hermione starts eagerly lapping at the head of your cock while luna starts furiously stroking your shaft."
        g4 "{size=+5}FUCK YES!!!{/size}"
        g4 "{size=+5}here it comes sluts!{/size}"
        ">Luna continues stroking your cock at a blistering pace while hermione moves backwards slightly, leaving her mouth open and waiting."
        $ luna_xpos -= 55
        $ genie_sprite_xpos -= 55
        $ hermione_head_xpos += 10
        $ hermione_head_ypos += 5
        $ hermione_kneel_cock = False
        g4 "{size=+10}ARGHHH!!!!{/size}"
        show screen white
        pause.1
        $ uni_sperm = True
        $ u_sperm = "characters/hermione/face/auto_16.png"
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+5}ugh! YES!!!{/size}"
        call luna_main("so much...", "wide", "left_stare", "sad", "default")
        call her_kneel("...","full_cum","dead")
        call her_kneel("*gulp*","cum","worriedCl")
        call her_kneel("mmm... I told you it would make him cum more...","grin","dead")
        call luna_main("even so...", "seductive", "left_stare", "sad", "default")
        ">Luna stares at hermione with a fierce hunger in her eyes."
        call luna_main("stand up... please...", "seductive", "left_stare", "sad", "upset")
        ">Exhausted after the marathon handjob you decide to take a seat while hermione and luna clean up."
        call her_kneel("only because you asked nicely...","open","baseL")
        $ hermione_xpos = 550
        $ luna_ypos = 0
        $ luna_xpos = 450
        $ luna_flip = -1
        $ hermione_right_arm = "characters/hermione/body/arms/right/right_1.png"
        $ genie_sprite_base = "characters/genie/base_1.png"
        $ hermione_zorder = 5
        $ luna_r_arm = 1
        hide screen hermione_kneel
        show screen hermione_main
        hide screen genie_sprite
        show screen genie
        hide screen chair_left
        hide screen desk
        hide screen g_c_u
        $ hermione_SC.chibi.xpos = 600 #Near the desk: 400. (210 - standing on desk.)
        $ hermione_SC.chibi.ypos = 260#Default: 250. (180- standing on desk.)
        show screen hermione_blink #Hermione stands still.
        call update_her_uniform
        hide screen blkfade
        with d3
        ">Hermione slowly stands up, her face simply drenched in cum..."
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
        call luna_main("mmmmm... just look at you... you look so... delicous...", "default", "empty", "sad", "default")
        call her_main("...","open","baseL")
        $ luna_xpos = 500
        $ luna_r_arm = 2
        ">Luna moves closer to Hermione before picking up a strand of cum with her finger and moving it to her mouth."
        call her_main("go on...","soft","ahegao")
        m "(mmmm...)"
        $ luna_xpos = 530
        call luna_main("mmmmm... you taste even better...", "closed_happy", "default", "sad", "default")
        call her_main("...","grin","dead")
        ">Hermione stands still, letting luna slowly wipe the cum from her face..."
        $ u_sperm = "characters/hermione/face/auto_08.png"
        call her_main("that's it... make sure you get it all...","base","down")
        call luna_main("mmmmm...", "closed_happy", "default", "sad", "cheeks_full")
        ">Luna slowly fills her mouth with cum before eventually swallowing."
        call luna_main("*gulp*", "seductive", "empty", "sad", "default")
        ">Eventually she finally gets the last strand into her mouth."
        $ uni_sperm = False
        call her_main("better?","base","glance")
        call luna_main("...", "closed_happy", "default", "sad", "cheeks_full")
        call luna_main("*gulp*", "seductive", "empty", "sad", "default")
        call luna_main("much.", "seductive", "empty", "sad", "default")
        call her_main("good.","base","suspicious")

        menu:
            "-Ask about study sessions-":
                m "So how have your recent study sessions been going?"
                $ luna_l_arm = 2
                $ luna_flip = 1
                $ luna_xpos = 300
                call luna_main("they've been OK...", "doubtful", "right", "sad", "upset")
                call her_main("stop being such a negative nancy luna, they have been amazing [genie_name]!","smile","happyCl",emote="06")
                call luna_main("...", "doubtful", "down", "sad", "upset")
                call her_main("Luna quizzed me on advanced transmogrification spells, advanced potion recipes and even complex herbology!","smile","happyCl")
                call luna_main("I don't even thinks she needs quizzing, she got everything right...", "angry", "right", "angry", "angry")
                call her_main("well the tutoring was even better!","base","happyCl")
                call her_main("we studied transfiguration, D.A.D.A, handjobs, potions, titjobs, spells, dirty talk and herbology!","grin","baseL")
                m "sounds like quite the lesson..."
                call luna_main("......", "seductive", "right", "sad", "upset")
                call her_main("If we keep these sessions up I'm sure Luna will pass her o.w.l.s with flying colours!","base","squint")
                call luna_main(".........", "seductive", "down", "sad", "default")
                if not luna_herm_talk:
                    $ luna_herm_talk = True
                    call her_main("I can't wait to see what mark she gets when she has to do them!","smile","happyCl",emote="06")
                    $ luna_flip = -1
                    call luna_main("I think you mean when {b}we{/b} have to do them...", "doubtful", "default", "angry", "upset")
                    call her_main("Oh, I don't have to do my o.w.l.s anymore...","base","happyCl")
                    call luna_main("What? Why not?", "wide", "default", "sad", "upset")
                    call her_main("Do you want to tell her or should I?","base","down")
                    m "(I have no idea what she's talking about.)"
                    m "Why don't you fill her in."
                    call her_main("alright then...","base","glance")
                    call her_main("I already did my o.w.l.s last year.","grin","worriedCl",emote="05")
                    call luna_main("Really? How?", "angry", "default", "sad", "upset")
                    call her_main("Well, I'd already been testing myself on past years exams since I was a 3rd year.","grin","worriedCl")
                    call her_main("Last year I finally felt that I was ready for the real thing. So I spoke to Professor dumbledore and Professor McGonagal.","base","baseL")
                    call her_main("I explained my situation and they agreed to test me early.","base","baseL")
                    call her_main("I got the highest mark since dumbledore himself took them!","smile","happyCl",emote="06")
                    call luna_main("Wait... If you've already completed your o.w.l.s, why are you still at school?", "doubtful", "default", "angry", "angry")
                    call her_main("I didn't want to miss out on school work or spending time with my friends...","base","happyCl")
                    call her_main("So I've just been doing additional study in the library after classes in exhchange for a special reccomendation from the school.","smile","happyCl")
                    call her_main("although recently I've been spending most of my free time in here...","base","down")
                    call luna_main("but why did you want to study with me then? Surely you don't need the quizzing anymore?", "mad", "default", "raised", "upset")
                    call her_main("I've always wanted to practice teaching and I get to help out my friend while I do it!","grin","baseL")
                    call luna_main("Friend?", "doubtful", "default", "sad", "upset")
                    call her_main("of course we're friends luna! Maybe even best friends after all this...","base","squint")
                    call luna_main("...", "seductive", "default", "sad", "upset")
                    $ luna_tears = 1
                    call luna_main("whatever...", "angry", "right", "angry", "upset")
                    $ luna_flip = 1
                    call luna_main("if you two are done talking I'm going to class...", "mad", "default", "angry", "upset")
                    ">Luna quickly gets dressed before leaving, not saying a word to you or hermione."
                    $ luna_wear_skirt = True
                    $ luna_wear_top = True
                    $ luna_wear_panties = True
                    $ luna_wear_bra = True
                    hide screen luna_chibi
                    hide screen luna
                    with d3
                    call her_main("...","annoyed","worriedL")
                    call her_main("did she seem ok to you sir?","annoyed","worriedL")
                    m "I think so. She's probably just not used to you being nice to her."
                    call her_main("maybe... If it's alright with you I might go check up on her.","angry","worried")
                    m "Suit yourself. I'm getting pretty sleepy anyway."
                    call her_main("thank you [genie_name].","base","worriedCl")
                    $ hermione_wear_skirt = True
                    $ hermione_wear_top = True
                    $ hermione_wear_panties = True
                    $ hermione_wear_bra = True
                    call update_her_uniform
                    ">Hermione quickly gets dressed before chasing after Luna."
                else:
                    jump luna_her_hj_end

            "-let them go-":
                label luna_her_hj_end:
                    m "Alright, you two can go now."
                    $ luna_l_arm = 2
                    $ luna_flip = 1
                    $ luna_xpos = 300
                    call luna_main("*hmph*, not before you pay us!", "angry", "default", "angry", "upset")
                    m "Right, nearly forgot."
                    call her_main("...","annoyed","suspicious")
                    $ gryffindor += 50
                    m "50 points to \'gryffindor\'!"
                    call her_main("thank you [genie_name]...","base","closed")
                    call luna_main("...", "seductive", "right", "default", "upset")
                    $ luna_gold += 150
                    $ gold -= 150
                    m "150 gold for Luna."
                    call luna_main("thanks [l_genie_name]...", "seductive", "right", "default", "upset")
                    call her_main("...","annoyed","angryL")
                    m "if that's all, I think I need a nap."
                    call her_main("alright then...","base","base")
                    ">Hermione and Luna get dressed before leaving your office together."
                    $ luna_wear_skirt = True
                    $ luna_wear_top = True
                    $ luna_wear_panties = True
                    $ luna_wear_bra = True
                    $ hermione_wear_skirt = True
                    $ hermione_wear_top = True
                    $ hermione_wear_panties = True
                    $ hermione_wear_bra = True
                    call update_her_uniform
                    ">You can hear them talking and laughing together as they shut your door."

    call play_sound("door") #Sound of a door opening.
    hide screen luna
    hide screen luna_chibi
    $ luna_busy = True
    jump end_hg_pf


label luna_favour_6: #luna and hermione blowjob
    if luna_corruption == 14: #first time
        $ luna_corruption += 1
        m "I have a new favour for you to complete today [luna_name]!"
        call luna_main("...", "angry", "default", "angry", "upset")
        m "If it's not too much trouble."
        call luna_main("save your begging [l_genie_name]... I'm fairly certain I know what you want.", "seductive", "right", "angry", "default")
        m "You do?"
        call luna_main("Mhmmm... unless I'm mistaken, you probably want me to wrap my lips around that filthy old cock of yours...", "angry", "default", "mad", "default")
        call luna_main("Am I mistaken sir?", "seductive", "right", "angry", "default")
        m "Certainly not! let's get started then shall we?"
        call luna_main("Not just yet... I have one condition.", "seductive", "default", "angry", "default")
        m "Name it."
        call luna_main("I want you to summon hermione.", "doubtful", "right", "sad", "default")
        m "Miss granger? Why?"
        call luna_main("well seeing as how this is my first time doing something like this, it only makes sense to have her here to offer her... experience.", "seductive", "right", "default", "default")
        call luna_main("heaven knows how many times she's sucked that disgusting cock of yours.", "mad", "default", "angry", "angry")
        m "I've lost count myself."
        call luna_main("In that case I suggest you summon her.", "angry", "default", "mad", "angry")
        m "Hey, I'm not going to say no to that!"
        ">You summon hermione to your office."
        call play_sound("door") #Sound of a door opening.
        $ hermione_SC.chibi.xpos = 600 #Near the desk.
        show screen hermione_blink #Hermione stands still.
        $ luna_flip = -1
        $ luna_r_arm = 2
        $ luna_xpos = 390
        call update_her_uniform
        pause
        call her_main("hello Professor...","base","closed")
        call her_main("oh, hi luna! what's he got you up here for today? Another handjob?","base","suspicious")
        call luna_main("not quite...", "angry", "right", "default", "default")
        call her_main("so he's finally asked for a blowjob then?","base","down")
        call luna_main("Mhmmm.", "seductive", "default", "default", "default")
        call her_main("great! I was hoping he'd ask for one soon. practicing on a dildo is one thing, but there's no subsitute for the real deal!","soft","ahegao")
        m "You've been practicing?"
        call her_main("of course! {p}although she still has a lot to learn...","upset","closed")
        call luna_main("It wasn't that bad...", "angry", "default", "sad", "pout")
        call her_main("ugh... let's just say you'll be glad she's had the practice.","angry","base")
        call her_main("My dildo still has bite marks on it from her first attempt.","angry","down_raised")
        call luna_main("Well how was I supposed to know the teeth aren't supposed to touch...", "angry", "right", "angry", "angry")
        call her_main("I told you that was the rule number one! Besides, you nearly bit it clean in half...","angry","wide")
        g4 "!!!"
        m "you know what, I think I'll be fine without one..."
        call her_main("oh no... you already asked for one. besides, she needs the experience.","annoyed","frown")
        m "Can't she have a little more practice?"
        $ luna_flip = 1
        call luna_main("stop complaining... I don't bite hard anymore.", "angry", "right", "mad", "upset")
        m "You're still biting?!?"
        call luna_main("I just said not hard!", "mad", "default", "angry", "pout")
        m "You shouldn't be biting at all!"
        call her_main("Don't worry [genie_name], I'll be standing right beside her. I'll make sure she doesn't do anything she shouldn't.","grin","worriedCl")
        m "Alright then..."
        g4 "But if you bite my cock off you're both getting expelled!"
        call luna_main("Pffft... as if you could have us expelled for failing to give a good blowjob...", "angry", "right", "angry", "default")
        m "Watch me..."
        call her_main("can we just get started?","base","down")
        m "..."
        call her_main("good... now take off your clothes luna.","open","closed")
        call luna_main("do I have to?", "seductive", "right", "sad", "pout")
        call her_main("I told you that appearance is everything, remember?","annoyed","closed")
        call luna_main("ugh... fine.", "seductive", "down", "sad", "upset")
        call her_main("Good! I'll get naked as well then, just to make it fair!","soft","squintL")
        m "(I think the two of them might be getting a little too friendly...)"
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
        call luna_main("...", "default", "right", "default", "default")
        show screen blkfade
        with d3
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png"
        ">hermione and luna slowly strip together, slowly placing their clothes in matching piles on your desk."
        ">Eventually Luna kneels before you, gazing up into your eyes while hermione stands behind her, examining her actions."
        call her_main("that's it... eye contact is very important.","disgust","down_raised")
        $ ccg_folder = "luna_bj"
        $ ccg1 = "herm"
        $ ccg3 = "gene"
        $ ccg2 = 1
        show screen ccg
        hide screen luna_chibi
        hide screen luna
        hide screen hermione_blink
        hide screen hermione_main
        hide screen blkfade
        with d3
        lun "..."
        $ ccg2 = 2
        lun "what now?"
        her "stick out your tongue..."
        lun "..."
        $ ccg2 = 3
        lun "ah..."
        her "good... now give the tip a little lick."
        lun "..."
        $ ccg2 = 4
        ">Luna leans forwards, giving the tip of your cock a tentative lick."
        m "Ugh... that's it slut."
        her "mmm... now another one. more tongue this time..."
        lun "..."
        $ ccg2 = 5
        ">Luna leans forward again, giving your cock another lick, this time starting further down the shaft."
        m "yes..."
        her "now just keep doing that until you can taste precum."
        $ ccg2 = 6
        lun "ok..."
        $ ccg2 = 7
        ">luna continues licking the head of your cock, running her tongue around the helmet and occasionally running her tongue down the entire length of it."
        her "just pretend it's a big lollipop..."
        lun "..."
        $ ccg2 = 8
        lun "when should I start sucking it?"
        her "not yet... I'll tell you when."
        $ ccg2 = 7
        lun "..."
        ">Luna keeps going, licking at an even faster pace, eventually focusing entirely on the head of your cock."
        m "mmmm... keep going..."
        $ ccg2 = 8
        lun "I think I can taste it hermione..."
        her "alright then... now, just like we practiced. Open wide."
        lun "..."
        $ ccg2 = 9
        ">Luna opens her mouth wide, eagerly presenting her young mouth."
        lun "ah..."
        her "good work... now put the tip in your mouth..."
        $ ccg2 = 10
        lun "..."
        ">A worried, almost scared, look appears over Luna's face."
        pause
        $ ccg2 = 8
        lun "it's so big... I'm not sure I can-?"
        her "shhh... it's alright. I'm here..."
        ">Hermione places a hand on the top of Luna's head."
        $ ccg2 = 11
        lun "hey! what do you think-"
        ">Before luna has a chance to complain, hermione pushes her head forward into your waiting cock."
        $ ccg2 = 12
        pause
        lun "!!!"
        her "there we go!"
        ">However, instead of entering her mouth, the head of your cock instead gets caught at the entrance, grating against her top row of teeth."
        g9 "Ahh... I said no teeth!"
        $ ccg2 = 13
        lun "!!!"
        ">Hermione tries to push Luna's head forward again..."
        her "come on luna... open wide!"
        $ ccg2 = 14
        lun "..."
        ">You can feel luna trying to stretch her mouth over the head of your enormous cock, managing to get a little more in."
        $ ccg2 = 15
        lun "......"
        her "hmmm... I guess the dildo we practiced on wasn't large enough..."
        m "Ugh... maybe we should try again later..."
        her "and stop now? I don't think so [genie_name]. Besides, once she gets the head in her mouth she'll be ok."
        her "she probably just needs one more push-"
        ">Hermione punctuates the end of her sentence with a forceful shove of Luna's head."
        $ ccg2 = 14
        pause
        lun "!!!"
        ">You can feel Luna's jaw stretch open a little further, barely failing to let the tip of your cock in. "
        m "I really don't think this is going to-"
        ">Before you can finish your sentence hermione gives one last shove, forcing the head of your cock into luna's straining mouth."
        $ ccg2 = 16
        lun "!!!"
        her "There we are! I told you she could do it [genie_name]!"
        $ ccg2 = 17
        lun "............."
        her "although we might need to give her a little bit of a rest, just to get used to it..."
        $ ccg2 = 18
        pause
        lun "...................."
        her "remember to breathe through your nose!"
        lun "............................."
        $ ccg2 = 19
        m "Are you sure she'll be OK?"
        her "She'll be fine sir! Besides, I didn't think you were one to worry about this sort of thing..."
        $ ccg2 = 18
        m "Well I don't remember nearly breaking your jaw when you gave your first blowjob..."
        her "Luna just has a smaller mouth..."
        $ ccg2 = 19
        pause
        her "She'll get used to it!"
        her "speaking of which, that's probably enough time..."
        $ ccg2 = 17
        lun "*nhihtsnoo*!!!"
        ">You feel Luna try to shout a complaint while her mouth is gagged by your cock."
        m "mmmm, that's good."
        her "well then, Time for part two of the lesson!"
        ">You see hermione's hand strengthen her grip on luna's hair."
        her "Now the tip to giving a good blowjob, according to witches weekly anyway, is to try and emulate the feeling of a vagina."
        $ ccg2 = 19
        her "So I just want you to keep your tongue straight, while I worry about the back and forth motions, ok luna?"
        $ ccg2 = 18
        lun "*mmmghh*..."
        her "great! here we go!"
        ">Hermione starts pushing Luna's head back and forward as deep as it will go."
        $ ccg2 = 23
        ">Eventually she settles into a rhythm of moving her head forward until about half your cock is in her mouth and then backwards until the head catches on her jaw."
        $ ccg2 = 16
        m "Mmmm... yes... just like that you little sluts..."
        $ ccg2 = 23
        pause
        her "how's she going [genie_name]? Is she keeping her tongue nice and straight?"
        $ ccg2 = 16
        m "Yeah... she's doing... great..."
        $ ccg2 = 20
        lun "..."
        $ ccg2 = 17
        her "fantastic! SHe's not letting her teeth touch anymore is she?"
        $ ccg2 = 21
        m "No... it's fine..."
        $ ccg2 = 18
        her "good work Luna! now just make sure you keep up a nice suction when I move your head forwards."
        $ ccg2 = 20
        lun "*mmmKyyy*..."
        $ ccg2 = 17
        ">This continues for a few more minutes. Luna continuing to suck your cock tirelessly while hermione gives her constant instruction."
        $ ccg2 = 22
        ">Thanks to hermione's instructions you're ready to blow in no time."
        $ ccg2 = 20
        her "mmm... where do you want to blow your load [genie_name]?"
        $ ccg2 = 19
        ">Hermione keeps forcefully moving Luna's head back and forth while talking."
        $ ccg2 = 21
        her "do you want to shoot it all down her slutty little throat?"
        $ ccg2 = 19
        pause
        lun "*mmmmm*...{image=textheart}"
        $ ccg2 = 21
        ">Luna's mouth vibrate pleasantly around your cock."
        $ ccg2 = 17
        her "or would you prefer to cum all over her face?"
        $ ccg2 = 20
        m "Ugh..."
        $ ccg2 = 17
        her "I know what she wants..."
        $ ccg2 = 21
        her "she wants you to shoot it all into her mouth and down her throat..."
        $ ccg2 = 19
        lun "{image=textheart}{image=textheart}{image=textheart}"
        $ ccg2 = 20
        her "she even made me promise before we came here..."
        $ ccg2 = 21
        lun "..."
        $ ccg2 = 19
        g9 "Ugh... I can't take it anymore!"
        $ ccg2 = 23
        pause
        g9 "HERE IT COMES SLUTS!!!"
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+5}ARGH! YES!!!{/size}"
        pause
        $ ccg2 = 24
        lun "!!!!!!!!!!!!"
        her "mmmm, that's it [genie_name]... let it all out..."
        g4 "{size=+5}AH...{/size}"
        ">Your load fills Luna's mouth to the brim while hermione holds her head firmly in place."
        $ ccg2 = 24
        pause
        lun "..."
        lun "......"
        $ ccg2 = 25
        pause
        lun "........."
        $ ccg2 = 26
        pause
        lun "............."
        $ ccg2 = 24
        lun "*gulp*"
        $ ccg2 = 27
        pause
        lun "ah... {image=textheart}{image=textheart}{image=textheart}"
        #fade to black.
        hide screen ccg
        with fade
        ">Luna and Hermione both get dressed while you sit in your chair, enjoying the show."
        call her_main("So what did you think luna? Not so bad now was it?","grin","baseL")
        call luna_main("I suppose not. although next time I think I should be able to move my head on my own!", "seductive", "right", "default", "upset")
        call her_main("Hmmm, I'm not sure if you're ready for that just yet...","grin","worriedCl")
        call luna_main("Whatever... now about our payment [l_genie_name]...", "doubtful", "right", "angry", "upset")
        m "Yes, yes. How does 60 points to \"gryffindor\" for Hermione and 150 gold for you sound?"
        call her_main("Actually we wanted to talk to you about that [genie_name]...","base","down")
        call her_main("Luna and I have been talking, and we're not sure it's fair that we both are paid in seperate currencies.","base","worriedCl")
        call her_main("We think it would be more fair if we're both paid points and gold.","base","closed")
        m "Really? I'm surprised miss lovegood would agree to that."
        call luna_main("Well I didn't want to-", "angry", "right", "mad", "upset")
        call her_main("...","annoyed","suspicious")
        call luna_main("But... hermione convinced me.", "doubtful", "right", "sad", "default")
        m "Alright then..."
        m "(It's not like I care who gets these worthless points)"
        $ ravenclaw += 30
        $ gryffindor += 30
        m "30 points to \"gryffindor\" and \"ravenclaw\"!"
        $ luna_gold += 75
        $ gold -= 150
        m "And here's 75 gold each."
        call her_main("Thank you [genie_name]!","base","base")
        call luna_main("...", "angry", "right", "angry", "upset")
        call her_main("Luna! Don't be rude.","angry","angry")
        call luna_main("...Thanks [l_genie_name].", "seductive", "right", "sad", "upset")
        call her_main("...","disgust","down_raised")
        call her_main("Well, we better be off sir, we still have a lot of studying to do!","grin","baseL")
        call her_main("(Not to mention more practice with the dildo...)","soft","squintL")
        call her_main("Come on Luna!","open","baseL")
        call luna_main("...", "default", "right", "default", "default")
        ">Luna and hermione leave the office together, chattering happily as the door closes."

    elif luna_corruption == 15: #second time
        $ luna_corruption += 1
        m "how do you feel about another blowjob?"
        call luna_main("...", "angry", "default", "angry", "upset")
        m "Come on, you seemed to like the last one..."
        call luna_main("*hmph* only because of your magic cum...", "seductive", "right", "angry", "default")
        m "well then I've got a fresh load ready for you!"
        call luna_main("Alright then... hurry up and summon hermione", "doubtful", "right", "sad", "default")
        m "Again? I thought you only wanted her here for the first time?"
        call luna_main("I don't remember having to explain myself to you...", "angry", "default", "angry", "upset")
        m "..."
        call luna_main("besides, you can't expect me to learn everything just from one lesson.", "seductive", "right", "default", "default")
        m "Fair enough, besides, you won't hear me complaining."
        call luna_main("good...", "seductive", "default", "angry", "default")
        ">You summon hermione to your office."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ hermione_SC.chibi.xpos = 600 #Near the desk.
        show screen hermione_blink #Hermione stands still.
        $ luna_flip = -1
        $ luna_r_arm = 2
        $ luna_xpos = 390
        call update_her_uniform
        pause
        call her_main("hello Professor!","base","closed")
        call her_main("hey luna! what's he want this time? Another blowjob?","base","suspicious")
        call luna_main("Mhmmm...", "seductive", "default", "default", "default")
        call her_main("great!!!","base","down")
        call her_main("You're going to love it [genie_name], she's been practicing every chance she could since last time!","soft","ahegao")
        m "really? I didn't expect her to be so enthusiastic..."
        call luna_main("*hmph* it's not like I'm excited about this...", "seductive", "right", "angry", "upset")
        call her_main("I told you to stop acting so cold Luna!","grin","baseL")
        call her_main("You should have heard her [genie_name]... She was practically begging for more lessons...","open","baseL")
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
        call luna_main("...", "seductive", "down", "sad", "default")
        call her_main("she insisted I spend all of our last study session teaching her about proper tongue work...","base","squint")
        call her_main("I made sure she studied tranfiguration and herbology first though...","grin","worriedCl",emote="05")
        $ luna_flip = 1
        call luna_main("can we stop talking and get started already!", "angry", "right", "mad", "upset")
        call her_main("See, I told you she was eager!","soft","squintL")
        m "I can hardly believe it..."
        call luna_main("shut up! both of you!", "wide", "right", "angry", "upset")
        m "..."
        call her_main("Alright... let's get started then.","base","down")
        call luna_main("finally...", "seductive", "down", "sad", "default")
        show screen blkfade
        with d3
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png"
        ">hermione and luna slowly strip together, slowly placing their clothes in matching piles on your desk."
        ">Eventually Luna kneels before you, gazing up into your eyes while hermione stands behind her, examining her actions."
        her "remember to look him in the eye... he loves that."
        $ ccg_folder = "luna_bj"
        $ ccg1 = "herm"
        $ ccg3 = "gene"
        $ ccg2 = 1
        show screen ccg
        hide screen luna_chibi
        hide screen luna
        hide screen hermione_blink
        hide screen hermione_main
        hide screen blkfade
        with d3
        lun "..."
        $ ccg2 = 2
        lun "should I stick my tongue out now?"
        her "yes, very good..."
        lun "..."
        $ ccg2 = 3
        lun "ah..."
        her "good... now you know what to do."
        lun "..."
        $ ccg2 = 4
        ">Luna leans forwards, giving the tip of your cock a loving lick."
        m "Ugh... that's it slut."
        her "mmm... just like we talked about. remember to work the shaft..."
        lun "..."
        $ ccg2 = 5
        ">Luna leans forward again, giving your cock another lick, this time starting further down the shaft."
        m "yes..."
        her "don't be afraid to lick the balls either."
        $ ccg2 = 6
        lun "ok..."
        $ ccg2 = 7
        ">luna continues licking the head of your cock, running her tongue around the helmet and occasionally running her tongue down the entire length of it and onto your balls."
        her "just like we practiced..."
        lun "..."
        $ ccg2 = 8
        lun "should I start sucking it?"
        her "you are eager, aren't you..."
        $ ccg2 = 7
        lun "..."
        her "Well, if you want to suck it, ask him..."
        lun "!!!"
        lun "Do I have to?"
        her "You do. We talked about this..."
        $ ccg2 = 1
        lun "can I... suck your cock..."
        menu:
            "-make her beg-":
                $ luna_dom -= 1
                $ luna_sub += 1
                m "I don't know... maybe if you asked a little nicer..."
                lun "..."
                her "go on..."
                lun "fine..."
                $ ccg2 = 2
                lun "can I suck your cock sir?"
                m "Hmmm, I'm not sure... that wasn't very convincing."
                $ ccg2 = 28
                lun "how dare you make-"
                her "LUNA!"
                $ ccg2 = 8
                lun "..."
                $ ccg2 = 2
                lun "Please... can I suck you big cock..."
                m "keep going..."
                lun "please..."
                $ ccg2 = 29
                lun "I just want to taste it..."
                lun "Feel it in my slutty little mouth..."
                m "Seeing as how you asked so nicely!"
            "-let her-":
                m "Go ahead slut."
        $ ccg2 = 30
        lun "*hmph*"
        her "Say thank you..."
        $ ccg2 = 28
        lun "..."
        $ ccg2 = 2
        lun "thank you sir..."

        $ ccg2 = 9
        ">Luna opens her mouth wide, eagerly presenting her young mouth."
        lun "ah..."
        her "good work... now put it in your mouth..."
        $ ccg2 = 10
        lun "..."
        pause
        $ ccg2 = 8
        lun "Are you sure-"
        her "shhh... it's alright. I'm here..."
        ">Hermione places a hand on the top of Luna's head."
        $ ccg2 = 11
        lun "hey! I think I can manage on my own this-"
        ">Before luna has any further chance to complain, hermione gives her a forceful shove into your waiting cock."
        $ ccg2 = 16
        lun "!!!"
        her "There we are! look at how much progress you're making, you got it in first time!"
        $ ccg2 = 17
        lun "............."
        her "although I still think you might need a little break just to let your mouth get used to this..."
        $ ccg2 = 18
        pause
        lun "...................."
        her "remember to breathe through your nose!"
        lun "............................."
        $ ccg2 = 19
        m "mmmm, her tongues moving around like crazy..."
        her "good... we practiced tongue work for a few hours last night..."
        $ ccg2 = 18
        m "well that practice is paying off!"
        her "hear that luna?"
        $ ccg2 = 31
        lun "{image=textheart}{image=textheart}{image=textheart}"
        pause
        her "She was a little worried you wouldn't like it..."
        her "anyway, time to start the real thing!"
        $ ccg2 = 17
        lun "*whhttahhhkkkooonn*!!!"
        ">You feel Luna try to shout a complaint while her mouth is gagged by your cock."
        m "mmmm, that's good."
        her "alright luna, we're going to go a little bit faster than last time!"
        ">You see hermione's hand strengthen her grip on luna's hair."
        her "Now just let me worry about the speed, you just focus on the tongue work, OK?"
        lun "*oohhhhkkk*"
        $ ccg2 = 19
        her "good girl..."
        $ ccg2 = 18
        lun "*mmmghh*..."
        her "here... we... go!"
        ">Hermione starts pushing Luna's head back and forward as deep as it will go."
        $ ccg2 = 23
        ">Eventually she settles into a quick rhythm of moving her head forward until about half your cock is in her mouth and then backwards until the head catches on her jaw."
        $ ccg2 = 16
        m "Mmmm... yes... just like that you little sluts..."
        $ ccg2 = 23
        pause
        her "how's she going [genie_name]? how's her tongue feel?"
        $ ccg2 = 16
        m "Yeah... it feels... amazing..."
        $ ccg2 = 20
        lun "..."
        $ ccg2 = 17
        her "fantastic! she's not moving it too fast is she?"
        $ ccg2 = 21
        m "No... it's fine..."
        ">All while hermione is talking to you her hand is firmly wrapped around Luna's hair, forcing her head backwards and forwards at a blistering pace."
        $ ccg2 = 18
        her "now make sure you suck hard when I push your head forward OK Luna..."
        $ ccg2 = 20
        lun "*mmmKyyy*..."
        $ ccg2 = 17
        ">This continues for a few more minutes. Luna continuing to suck your cock tirelessly while hermione gives her constant instruction."
        $ ccg2 = 22
        m "Ugh... get ready sluts... not much longer..."
        $ ccg2 = 20
        her "mmm... where do you want to blow your load [genie_name]?"
        $ ccg2 = 19
        ">Hermione keeps forcefully moving Luna's head back and forth while talking."
        $ ccg2 = 21
        her "do you want to shoot it all down her slutty little throat?"
        $ ccg2 = 32
        pause
        lun "*mmmmm*...{image=textheart}"
        $ ccg2 = 21
        ">Luna's mouth vibrate pleasantly around your cock."
        $ ccg2 = 17
        her "or would you prefer to cum all over her face?"
        $ ccg2 = 20
        m "Ugh..."
        $ ccg2 = 17
        her "I know what she wants..."
        $ ccg2 = 21
        her "she wants you to shoot it all into her mouth and down her throat again..."
        $ ccg2 = 32
        lun "{image=textheart}{image=textheart}{image=textheart}"
        $ ccg2 = 20
        her "but this isn't about making her happy..."
        $ ccg2 = 21
        lun "!!!"
        $ ccg2 = 19
        her "so why don't you coat the bitch..."
        g9 "Ugh... I can't take it anymore!"
        ">Just as you reach your orgasm, hermione pulls luna's head off your cock."
        $ ccg2 = 33
        lun "Hey!"
        g9 "HERE IT COMES SLUTS!!!"
        $ ccg2 = 35
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+5}ARGH! YES!!!{/size}"
        pause
        $ ccg2 = 35
        lun "!!!!!!!!!!!!"
        her "mmmm, that's it [genie_name]... let it all out..."
        her "coat her in it..."
        g4 "{size=+5}AH...{/size}"
        ">Your cum erupts over luna's face, hitting her eyes and coating her face, all while hermione holds her head firmly in place as she tries to turn away."
        $ ccg2 = 36
        pause
        lun "..."
        lun "......"
        $ ccg2 = 37
        pause
        lun "........."
        $ ccg2 = 38
        pause
        lun "............."
        $ ccg2 = 39
        lun "Hermione! You promised!"
        her "tough. Now just stay still and look up into his eyes like we talked about..."
        $ ccg2 = 40
        lun "I can't... They're covered in cum..."
        her "Too bad."
        lun "..."
        $ ccg2 = 41
        pause
        lun "......."
        $ ccg2 = 42
        her "good girl..."
        #fade to black.
        hide screen ccg
        with fade
        ">Luna and Hermione both get dressed while you sit in your chair, enjoying the show."
        call her_main("There we are Luna, how was that?","grin","baseL")
        call luna_main("It was OK...", "seductive", "right", "default", "upset")
        call luna_main("although I prefer it when he shoots into my mouth...", "seductive", "right", "default", "upset")
        call her_main("I know... but it's not about how you like it.","grin","worriedCl")
        call luna_main("why not?", "doubtful", "right", "angry", "upset")
        call her_main("because a good blowjob is all about making him feel good.","grin","worriedCl")
        call her_main("I can see we're still going to have another lesson after we get paid. speaking of which...","grin","worriedCl")
        $ ravenclaw += 30
        $ gryffindor += 30
        m "30 points to \"gryffindor\" and \"ravenclaw\"!"
        $ luna_gold += 75
        $ gold -= 150
        m "And here's 75 gold each."
        call her_main("Thank you [genie_name]!","base","base")
        call luna_main("...", "angry", "right", "angry", "upset")
        call her_main("...","disgust","down_raised")
        call luna_main("...Thank you sir.", "seductive", "right", "sad", "upset")
        call her_main("Well, we better be off sir, we still have a lot of studying to do!","grin","baseL")
        call her_main("(Not to mention more practice with the dildo...)","soft","squintL")
        call her_main("Come on Luna!","open","baseL")
        call luna_main("...", "default", "right", "default", "default")
        ">Luna and hermione leave the office together, chattering happily as the door closes."

    else: #third time (repeatable)
        if luna_corruption <= 16:
            $ luna_corruption += 1
        m "how about another lesson in blowjobs?"
        call luna_main("...", "seductive", "right", "angry", "default")
        call luna_main("alright...", "seductive", "right", "sad", "default")
        call luna_main("just hurry up and summon hermione", "seductive", "default", "default", "default")
        m "if you insist..."
        ">You summon hermione to your office."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ hermione_SC.chibi.xpos = 600 #Near the desk.
        show screen hermione_blink #Hermione stands still.
        $ luna_flip = -1
        $ luna_r_arm = 2
        $ luna_xpos = 390
        call update_her_uniform
        pause
        call her_main("hello Professor!","base","closed")
        call her_main("hey luna! another blowjob?","base","suspicious")
        call luna_main("Mhmmm...", "angry", "right", "default", "default")
        call her_main("yay!!!","grin","worriedCl")
        call her_main("we can finally practice deepthroating!","base","glance")
        m "really? are you sure she's ready for that?"
        call luna_main("*hmph* of course I am...", "angry", "right", "angry", "pout")
        call her_main("believe me sir, she's been practicing really hard!","open","baseL")
        call her_main("You should have seen her genie... she almost got my 7 inch dildo in all the way...","grin","ahegao")
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
        call luna_main("...", "angry", "right", "sad", "upset")
        call her_main("well half of the way...","soft","squintL")
        call her_main("but I'm sure she'll manage with the real thing...","grin","baseL")
        $ luna_flip = 1
        call luna_main("can we stop talking and get started already!", "angry", "right", "angry", "default")
        call her_main("See, I told you she was ready!","grin","worriedCl")
        m "I can hardly believe it..."
        call her_main("Alright... let's get started then.","grin","ahegao")
        call luna_main("finally...", "seductive", "right", "sad", "default")
        show screen blkfade
        with d3
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png"
        ">hermione and luna slowly strip together, slowly placing their clothes in matching piles on your desk."
        ">Eventually Luna kneels before you, gazing up into your eyes while hermione stands behind her, examining her actions."
        her "remember to look him in the eye... he loves that."
        $ ccg_folder = "luna_bj"
        $ ccg1 = "herm"
        $ ccg3 = "gene"
        $ ccg2 = 1
        show screen ccg
        hide screen luna_chibi
        hide screen luna
        hide screen hermione_blink
        hide screen hermione_main
        hide screen blkfade
        with d3
        lun "..."
        $ ccg2 = 43
        lun "ah..."
        her "nice work luna..."
        $ ccg2 = 44
        lun "thank you..."
        her "good... now you know what to do."
        lun "..."
        $ ccg2 = 5
        ">Luna leans forwards, giving the tip of your cock a loving lick."
        m "Ugh... that's it slut."
        her "mmm... remember the dirty talk..."
        lun "..."
        $ ccg2 = 45
        ">Luna leans forward again, giving your cock another lick, this time starting further down the shaft."
        m "yes..."
        $ ccg2 = 5
        lun "it tastes strange..."
        $ ccg2 = 7
        ">luna continues licking the head of your cock, alternating between licking and gently sucking the tip..."
        her "it's nice isn't it..."
        lun "yes..."
        $ ccg2 = 9
        lun "can I start sucking it sir?"
        her "you are eager, aren't you..."
        $ ccg2 = 6
        lun "yes..."
        $ ccg2 = 46
        lun "I can't wait for him to shoot his sticky load all over me..."
        her "very good... now tell him what you are"
        lun "..."
        $ ccg2 = 47
        lun "i'm a slut sir..."
        her "More."
        $ ccg2 = 48
        lun "I'm a slut for your cum..."
        $ ccg2 = 49
        lun "I'm a nasty little cumslut who's addicted to her headmasters cum..."
        her "Well time for you to earn it then cumslut... open wide!"

        $ ccg2 = 9
        ">Luna opens her mouth wide, eagerly presenting her young mouth."
        lun "ah..."
        her "good work... here we go!"
        ">Hermione grabs the back of luna's head and gives her a violent shove, forcing your cock down her mouth, resting on the entrance to her throat."
        $ ccg2 = 23
        lun "!!!"
        her "There we go! now dumbledore's cock is a little thicker than the dildo we practiced with so you need to make sure you relax your throat..."
        $ ccg2 = 20
        lun "............."
        her "how's she going [genie_name]? is she getting it down all the way?"
        m "Almost, she's not really deepthroating it though..."
        $ ccg2 = 21
        pause
        her "OK, the secret here is to try and swallow it."
        her "Now I'm going to give another push, and I want you to swallow when I do OK?"
        lun "*mmmkkkyyy*"
        her "here... we..."
        $ ccg2 = 17
        ">hermione pulls luna's head back on your cock."
        her "GO!"
        $ ccg2 = 50
        ">Hermione gives another harsh shove, this time forcing your cock completely down luna's throat."
        lun "*gluck*"
        m "ugh... that's it..."
        her "good work Luna! I knew you could do it!"
        $ ccg2 = 51
        lun "*glllkkk*"
        ">hermione pulls luna's head back."
        $ ccg2 = 52
        m "gods that feels good..."
        her "mmmm, I bet... now the make sure you breathe through your nose when I pull your head back, you won't be able to breathe when he's in your throat OK?"
        $ ccg2 = 53
        lun "mmmkkkyyy"
        ">hermione shoves luna forward again."
        $ ccg2 = 54
        pause
        her "see..."
        her "it's a balancing game... now get ready, we're going to speed up the pace a bit."
        $ ccg2 = 51
        lun "*whhttahhhkkkooonn*!!!"
        ">You feel Luna try to shout a complaint while her mouth is gagged by your cock."
        m "mmmm, i love it when she does that..."
        ">You see hermione's hand strengthen her grip on luna's hair."
        her "remember to breathe on the back stroke."
        $ ccg2 = 55
        lun "*oohhhhkkk*"
        her "good girl..."
        $ ccg2 = 52
        lun "*glckk*glckk*glckk*..."
        her "that's it!"
        ">hermione starts forcefully fucking luna's face on your cock."
        $ ccg2 = 54
        lun "*glckk*agh*glckk*..."
        $ ccg2 = 52
        m "Mmmm... yes... just like that you little sluts..."
        $ ccg2 = 54
        pause
        her "now this is a bit faster and harder than what you'd normally do when giving a blowjob by yourself."
        $ ccg2 = 52
        her "but it feels amazing doesn't it?"
        $ ccg2 = 54
        m "Yeah... it feels... incredible..."
        $ ccg2 = 52
        her "I was talking to Luna, [genie_name]."
        $ ccg2 = 56
        lun "...*glckk*{image=textheart}*glckk*..."
        $ ccg2 = 52
        her "mmm, I knew you'd love it."
        $ ccg2 = 54
        ">hermione starts relentlessly making you fuck luna's throat."
        $ ccg2 = 52
        lun "*glckk*glckk*glckk*"
        $ ccg2 = 56
        lun "*glckk*{image=textheart}*glckk*{image=textheart}*glckk*"
        $ ccg2 = 52
        ">This continues for a few more minutes. Luna mindlessly having her throat impaled while hermione gives her further instructions."
        $ ccg2 = 57
        m "Ugh... get ready sluts... not much longer..."
        $ ccg2 = 58
        her "mmm... that's it [genie_name]..."
        $ ccg2 = 54
        ">Hermione keeps forcefully shoving Luna's head back and forth while talking."
        $ ccg2 = 52
        her "I think she wants it shot down her slutty little throat again..."
        $ ccg2 = 56
        pause
        lun "*mmmmm*...{image=textheart}"
        $ ccg2 = 58
        ">Luna's mouth vibrate pleasantly around your cock."
        $ ccg2 = 54
        her "but we can't have that can we?"
        $ ccg2 = 52
        m "Ugh..."
        $ ccg2 = 51
        her "sluts like her don't deserve to get what they want..."
        $ ccg2 = 57
        her "she doesn't deserve all of that yummy cum to herself does she?"
        $ ccg2 = 52
        lun "{image=textheart}{image=textheart}{image=textheart}"
        $ ccg2 = 54
        her "she needs to learn to share..."
        $ ccg2 = 52
        lun "..."
        $ ccg2 = 54
        her "so why don't you coat the filthy {b}cum{/b}slut..."
        g9 "Ugh... I can't take it anymore!"
        ">Just as you reach your orgasm, hermione yanks luna's head off your cock."
        $ ccg2 = 59
        lun "hhhhyyy!"
        pause
        g9 "HERE IT COMES SLUTS!!!"
        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+5}ARGH! YES!!!{/size}"
        pause
        $ ccg2 = 60
        lun "!!!!!!!!!!!!"
        her "mmmm, that's it [genie_name]... let it all out..."
        her "coat her in it..."
        g4 "{size=+5}AH...{/size}"
        ">Your cum erupts over luna's face, hitting her eyes and coating her face, all while hermione holds her head firmly in place as she tries to turn away."
        $ ccg2 = 61
        pause
        lun "..."
        lun "......"
        $ ccg2 = 62
        pause
        lun "........."
        $ ccg2 = 63
        pause
        lun "............."
        $ ccg2 = 64
        lun "ugh....."
        her "I don't even think she can speak..."
        lun "*grbbble*"
        her "you must have fucked her throat to hard [genie_name]..."
        her "oh well!"
        lun "..."
        $ ccg2 = 65
        pause
        show screen blkfade
        with d3
        ">Hermione leans down in front of Luna and starts to lick the cum from her face."
        $ ccg1 = "blank"
        $ ccg3 = "blank"
        $ ccg2 = 66
        hide screen blkfade
        with d3
        her "mmmm, I told you that we need to share what he pays us didn't I?"
        lun "y-yes..."
        $ ccg2 = 67
        her "mmmm... {size=-5}good girl...{/size}"
        show screen blkfade
        with d3
        hide screen ccg
        with fade
        ">Luna and Hermione both get dressed while you sit in your chair, enjoying the show."
        hide screen blkfade
        with d3
        call her_main("There we are Luna, how was that?","grin","baseL")
        $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
        $ luna_tears = 3
        call luna_main("......", "seductive", "down", "sad", "upset")
        call luna_main("incredible...", "seductive", "right", "sad", "default")
        call her_main("I told you you'd love it didn't I?","grin","worriedCl")
        call luna_main("yes hermione...", "mad", "down", "sad", "default")
        call her_main("good, now I think we need to go do some actual study, could you please pay us [genie_name]?","grin","worriedCl")
        $ ravenclaw += 30
        $ gryffindor += 30
        m "30 points to \"gryffindor\" and \"ravenclaw\"!"
        $ luna_gold += 75
        $ gold -= 150
        m "And here's 75 gold each."
        call her_main("Thank you [genie_name]! Anytime you want luna's to fuck luna's slutty little throat again just let us know!","base","base")
        call luna_main("...Thank you sir.", "seductive", "down", "sad", "default")
        call her_main("Well, we better be off sir, we still have a lot of studying to do!","grin","baseL")
        call her_main("(Not to mention more practice with the {b}big{/b} dildo...)","soft","squintL")
        call her_main("Come on Luna!","open","baseL")
        call luna_main("...", "default", "down", "sad", "default")
        ">Luna and hermione leave the office together, chattering happily as the door closes."

    call play_sound("door") #Sound of a door opening.
    hide screen luna
    hide screen luna_chibi
    $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_1.png"
    $ luna_tears = 0
    $ luna_busy = True
    jump end_hg_pf


    jump luna_away
label luna_favour_7:
    m "Luna."
    call luna_main("yes sir...", "default", "default", "sad", "default")
    m "Today I have a new type of favour for you."
    call luna_main("really?", "wide", "default", "default", "default")
    m "Today, we'll be-"
    call luna_main("Wait!", "wide", "default", "angry", "default")
    call luna_main("Before you ask me...", "seductive", "right", "sad", "default")
    call luna_main("can you please summon Hermione?", "seductive", "default", "sad", "upset")
    m "You don't even know what I'm going to ask you yet!"
    call luna_main("I have a fair idea sir...", "angry", "default", "angry", "default")
    call luna_main("And if it's alright with you, I'd prefer that Hermione be here as well.", "seductive", "right", "sad", "default")
    m "well I'm not going to say no to that!"
    call luna_main("Thank you sir...", "closed_happy", "default", "sad", "default")
    ">You summon Hermione up to your office."
    $ luna_xpos = 300
    $ luna_flip = -1
    call her_main("Hey Luna!!!","grin","wink")
    call her_main("[genie_name].","normal","happyCl")
    call her_main("So what's he want from us today?","smile","glance")
    call her_main("Another blowjob?","grin","baseL")
    call luna_main("He hasn't even asked yet.", "seductive", "right", "sad", "default")
    call luna_main("I wanted you to be here for it.", "doubtful", "left_stare", "sad", "default")
    call her_main("you mean...","shock","happy")
    call her_main("Awww that's so sweet Luna.","grin","soft")
    call her_main("You better ask her nicely sir!","mad","narrow")
    m "You don't even know what-"
    call her_main("Everyone knows what you're going to ask for next sir.","open","closed")
    call her_main("At least try and make it a little romantic for her...","smile","soft")
    m "Romantic?"
    call her_main("Work something out!","open","angry")
    call luna_main("You really don't need to worry about it [l_genie_name]...", "default", "down", "sad", "upset")
    call her_main("Shh! You're first time needs to be at least a little bit special Luna!","upset","angryL")
    m "..."
    m "Luna Lovegood."
    m "Would you do me the honor?"
    $ luna_flip = 1
    call luna_main("...", "wide", "default", "sad", "default")
    call her_main("(That's the corniest thing I've ever heard...)","open","wink")
    call luna_main("I...", "wide", "right", "sad", "default")
    call luna_main("I......", "wide", "right", "sad", "upset")
    call luna_main("I can't!", "wide", "down", "sad", "angry")
    call her_main("What?","shock","wide")
    call her_main("Why not Luna? We've talked about this...","soft","worried")
    call her_main("We even spent all last weekend \'practicing\'...","normal","worriedL")
    call luna_main("I know...", "default", "right", "mad", "pout")
    call luna_main("It's just...", "default", "down", "sad", "talk")
    call luna_main("I don't think I can handle it...", "default", "right", "sad", "angry")
    call luna_main("I'm not like you... I can't be good at everything...", "closed_happy", "default", "sad", "open") 
    show screen blkfade
    "*SLAP*"
    ">You close your eyes and recoil, expecting the stinging in your face to start any moment, however it never comes."
    $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
    hide screen blkfade
    with d3
    ">Instead, you notice a bright red mark starting to form across Luna's face."
    call her_main("You need to stop thinking that right now!","open","angry")
    call luna_main("but I'm not as-", "default", "right", "sad", "pout")
    call her_main("Luna... you have to Stop measuring yourself against other people.","open","wink")
    call her_main("You're the cutest, nicest, zaniest girl at this school and I don't know what's happened to you recently but you need to just calm down and enjoy your life.","open","wink")
    $ luna_tears = 2
    call luna_main("but...", "wide", "down", "sad", "upset")
    call her_main("Shhh... It's ok...","soft","soft")
    call her_main("Why don't we start by enjoying our headmasters big cock, hmmm?","grin","happy")
    call her_main("Would that make you feel a little better?","smile","wink")
    call luna_main("y-yes...", "seductive", "right", "sad", "default")
    show screen blkfade
    with d3
    hide screen luna
    hide screen hermione_main
    $ luna_tears = 0
    her "Good... Now let's take our clothes off and hop up onto [genie_name]'s desk!"
    lun "Hermione... I'm still not so sure about this..."
    lun "I don't know if I'm ready..."
    her "Shhh, It's alright... I'll go first OK?"
    lun "Really? You'd do that for me?"
    her "Of course! Besides, I don't really mind doing it..."
    her "I'm sure you'll love it as well!"
    lun "I hope so..."
    her "Are you ready [genie_name]?"
    $ ccg_folder = "luna_sex"
    $ ccg1 = "luna_1"
    $ ccg2 = "herm_1"
    $ ccg3 = "blank"
    show screen ccg
    hide screen bld1
    hide screen blkfade
    with d3
    m "Am I!"
    pause
    menu:
        "-Be gentle...-":
            ">You take a hold of Hermione's legs, slowly parting them as you the head of your cock up with her tender sex."
            $ ccg2 = "herm_2"
            her "Now just take it slowly [genie_name], so Luna can get a good idea of what she's-"
            ">You sneak the head of your cock softly into her waiting pussy."
            $ ccg2 = "herm_3"
            her "{image=textheart}ah{image=textheart}"
            m "Mmmm, that's it slut... we can take it nice and slow..."
            ">You slide the rest of your cock into her needy hole."
            $ ccg2 = "herm_4"
            her "ah{image=textheart}{image=textheart}{image=textheart}..."
            pause
            her "So {image=textheart}gooood{image=textheart}..."
            $ ccg1 = "luna_2"
            lun "mmm..."
            g4 "{size=+10}Here we go!{/size}"
            ">You start thrusting your hips in and out of hermione, her pussy spasming around your hard member."
            $ ccg2 = "herm_5"
            her "ah{image=textheart}... ah{image=textheart}... ah{image=textheart}..."
            her "{size=-15}harder...{/size}"
            $ ccg1 = "luna_3"
            lun "What's that Hermione?"
            her "{size=-10}harder...{/size}"
            $ ccg1 = "luna_4"
            lun "I think you better stop sir... I think you might be hurting her!"
            $ ccg2 = "herm_6"
            her "HARDER!!!"
            g4 "Ugh... take this you filthy whore."
            $ ccg1 = "luna_5"
            lun "..."
            her "Yes, yes!"
            her "I'm a nasty little whore..."
            $ ccg2 = "herm_7"
            her "Getting {image=textheart}fucked{image=textheart} silly in front of their best friend..."
            $ ccg1 = "luna_6"
            lun "(best?...)"
            $ ccg2 = "herm_8"
            her "I'm even going to cum in front of her!"
            $ ccg2 = "herm_5"
            her "ah... here I..."
            $ ccg1 = "luna_7"
            lun "Already?"
            her "Y-y-yes... {size=+5}I'm{image=textheart}{image=textheart}{image=textheart}{/size}"
            $ ccg2 = "herm_9"
            her "{size=+5}CUMMING!!!{/size}"
        "-Be rough!-":
            ">You take a hold of Hermione's legs, lining the head of your cock up with her tender sex."
            her "Now just take it slowly, so Luna can get an idea of-"
            ">You slam into her, burying your cock to the hilt."
            her "!!!"
            g4 "Mmmm, that's it slut... You're still so tight."
            her "ah{image=textheart}{image=textheart}{image=textheart}... this is..."
            pause
            her "So {image=textheart}gooood{image=textheart}..."
            $ ccg1 = "luna_5"
            lun "mmm..."
            g4 "{size=+10}Here we go!{/size}"
            ">You start thrusting your hips in and out of hermione, her pussy spasming around your hard member."
            $ ccg2 = "herm_5"
            her "ah{image=textheart}... ah{image=textheart}... ah{image=textheart}..."
            her "{size=-15}harder...{/size}"
            $ ccg1 = "luna_3"
            lun "What's that Hermione?"
            her "{size=-10}harder...{/size}"
            $ ccg1 = "luna_4"
            lun "I think you better stop sir... I think you might be hurting her!"
            $ ccg2 = "herm_6"
            her "HARDER!!!"
            g4 "Ugh... take this you filthy whore."
            $ ccg1 = "luna_5"
            lun "..."
            her "Yes, yes!"
            her "I'm a nasty little whore..."
            $ ccg2 = "herm_7"
            her "Getting {image=textheart}fucked{image=textheart} silly in front of their best friend..."
            $ ccg1 = "luna_6"
            lun "(best?...)"
            $ ccg2 = "herm_8"
            her "I'm even going to cum in front of her!"
            $ ccg2 = "herm_5"
            her "ah... here I..."
            $ ccg1 = "luna_7"
            lun "Already?"
            her "Y-y-yes... {size=+5}I'm{image=textheart}{image=textheart}{image=textheart}{/size}"
            $ ccg2 = "herm_9"
            her "{size=+5}CUMMING!!!{/size}"
    ">Hermione's cunt shakes violently as her eyes roll back into her head..."
    pause
    $ ccg2 = "herm_10"
    m "Ugh... that's it girl..."
    $ ccg2 = "herm_11"
    her "so{image=textheart}{image=textheart}{image=textheart} goooooooooooood...{image=textheart}"
    $ ccg1 = "luna_8"
    lun "wow..."
    ">You pull your rock hard cock out of Hermione's needy hole, despite her best efforts to wrap her legs around your torso."
    $ ccg2 = "herm_12"
    her "Just... a little longer [genie_name]..."
    m "Now, now, [hermione_name]... don't be greedy..."
    $ ccg2 = "herm_13"
    her "..."
    her "You're right sir..."
    $ ccg2 = "herm_14"
    her "Sorry Luna..."
    $ ccg2 = "herm_15"
    her "I'm just such a greedy little cockslut..."
    pause
    $ ccg1 = "luna_9"
    lun "I know..."
    $ ccg2 = "herm_14"
    her "..."
    ">You move away from Hermione's sweaty body, over to Luna's milky white form."
    $ ccg1 = "luna_10"
    ">You grab a hold of her legs, lining your cock up with her dripping cunt."
    m "Are you ready [luna_name]?"
    $ ccg1 = "luna_11"
    lun "I... I think so..."
    $ ccg1 = "luna_12"
    lun "Are you sure everything will be fine, Hermione?"
    $ ccg2 = "herm_16"
    $ ccg1 = "luna_13"
    ">Hermione gently takes Luna's hand in her own."
    pause
    her "I promise."
    $ ccg1 = "luna_14"
    lun "Thanks Hermioneeeeehhhh"
    ">You decide to interrupt the cute moment by slowly forcing the head of your cock into Luna's soft pussy."
    $ ccg1 = "luna_15"
    lun "ah... it's... so hot..."
    $ ccg2 = "herm_17"
    her "mmmmm, yeah it is..."
    $ ccg1 = "luna_16"
    lun "ah...{image=textheart}{image=textheart}{image=textheart}"
    her "Mmmm it seems like she likes it [genie_name]..."
    $ ccg1 = "luna_17"
    ">Luna barely muffles a timid little moan in response."
    $ ccg2 = "herm_18"
    her "Maybe she's ready for a little more?"
    $ ccg1 = "luna_18"
    lun "ah... yes..."
    lun "Just please... go slowly sir..."
    her "Hmmm, I'm not sure he'll be able to control himself."
    show screen blkfade
    with d3
    ">Hermione leans over and whispers into Luna's ear."
    $ ccg_folder = "luna_kiss"
    $ ccg1 = "1"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    hide screen blkfade
    with d3
    her "I know I wouldn't."
    pause
    show screen blkfade
    with d3
    $ ccg_folder = "luna_sex"
    $ ccg1 = "luna_18"
    $ ccg2 = "herm_18"
    $ ccg3 = "blank"
    hide screen blkfade
    with d3
    ">As if to punctuate the end of Hermione's sentence, you slowly thrust the rest of your length into Luna's tight fuckhole."
    hide screen blkfade
    with hpunch
    $ ccg1 = "luna_19"
    lun "{size=+10}!!!{/size}"
    $ ccg1 = "luna_20"
    lun "Ahhhhhhh"
    $ ccg2 = "herm_19"
    her "Mmmm, maybe that was a little too much sir..."
    m "ugh... I couldn't help myself."
    ">You slowly pull your cock out of her, until only the tip remains, before thrusting forward, reburying it in it's newfound home."
    g4 "Fuck she's so tight..."
    g4 "I can barely move..."
    $ ccg1 = "luna_20"
    lun "a-a-ahhhhh..."
    ">You slowly start to settle into a deep, rhythmic motion with your hips. Each thrust eliciting a gentle moan from Luna's lips."
    $ ccg2 = "herm_20"
    her "How is she [genie_name]?"
    m "incredible..."
    $ ccg1 = "luna_21"
    lun "thank you sir..."
    $ ccg1 = "luna_22"
    ">You begin to notice tears start to form in the corners of Luna's eyes."
    $ ccg2 = "herm_16"
    her "Is everything alright Luna?"
    $ ccg2 = "herm_18"
    her "It's not hurting too much is it?"
    $ ccg1 = "luna_23"
    lun "I-It's nothing!"
    $ ccg2 = "herm_17"
    her "Are you sure? If it's too much we can stop..."
    $ ccg1 = "luna_24"
    lun "No!"
    lun "It's just... I'm... just..."
    lun "So..."
    $ ccg1 = "luna_25"
    lun "Happy..."
    ">You start to notice Luna and Hermione's hands tremble as Hermione squeezes tightly around Luna's."
    $ ccg2 = "herm_21"
    her "So you like it?"
    $ ccg1 = "luna_26"
    lun "Ah..."
    lun "yes... I think so..."
    $ ccg1 = "luna_27"
    lun "It's a little painful... but it's..."
    $ ccg1 = "luna_26"
    lun "ah...{image=textheart}{image=textheart}{image=textheart}"
    $ ccg1 = "luna_25"
    lun "Still nice..."
    $ ccg2 = "herm_19"
    her "Yay!!! I knew you'd love it! This is going to be so much fun from now on!"
    $ ccg1 = "luna_29"
    lun "From... now on?"
    her "Duh... You don't think Dumbledore's going to be happy with only fucking that yummy pussy once do you?"
    $ ccg1 = "luna_24"
    lun "ah...{image=textheart}{image=textheart}{image=textheart} I guess n-not..."
    $ ccg2 = "herm_18"
    her "I know I wouldn't..."
    $ ccg1 = "luna_29"
    lun "w-what?"
    $ ccg2 = "herm_17"
    her "shhh... just enjoy yourself."
    $ ccg1 = "luna_26"
    lun "a-alright...{image=textheart}"
    g4 "Gods your tight..."
    $ ccg1 = "luna_25"
    lun "Ah... thank you... sir..."
    $ ccg2 = "herm_21"
    her "Good girl, he likes it when you call him that."
    $ ccg1 = "luna_18"
    lun "Really?"
    $ ccg2 = "herm_18"
    her "Mhmmm... He likes it even more when you describe what you feel to him."
    $ ccg1 = "luna_23"
    lun "I-I don't know... ah...{image=textheart} if I could do that..."
    lun "It's too embarrassing!"
    $ ccg2 = "herm_17"
    her "I'd like it too..."
    $ ccg1 = "luna_18"
    lun "..."
    lun "well Alright..."
    $ ccg1 = "luna_21"
    lun "It's... ah...{image=textheart} it's like he's scratching an itch I never knew I had."
    her "mmmmm, I know that itch..."
    lun "ah...{image=textheart} does it go away?"
    $ ccg2 = "herm_18"
    her "eventually... but not for long..."
    $ ccg1 = "luna_17"
    lun "ah...{image=textheart}"
    $ ccg1 = "luna_20"
    lun "You mean?"
    $ ccg2 = "herm_19"
    her "Mhmmm... Don't worry, I'm sure dumbledore will be more than happy to scratch it for you..."
    $ ccg2 = "herm_18"
    her "Or if he's too busy... well... you could always come to my room..."
    $ ccg1 = "luna_17"
    lun "{image=textheart}{image=textheart}{image=textheart}"
    $ ccg1 = "luna_18"
    lun "a-alright..."
    $ ccg_folder = "luna_kiss"
    $ ccg1 = "2"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    hide screen blkfade
    with d3
    her "{size=-5}good girl{/size}"
    pause
    ">As hermione whispers to Luna, you feel her pussy squeeze around your cock."
    show screen blkfade
    with d3
    $ ccg_folder = "luna_sex"
    $ ccg1 = "luna_18"
    $ ccg2 = "herm_18"
    $ ccg3 = "blank"
    hide screen blkfade
    with d3
    g9 "Mmmm yes!"
    g9 "Do that again [hermione_name]!"
    $ ccg2 = "herm_22"
    her "Do what?"
    g9 "call her a good girl!"
    $ ccg1 = "luna_16"
    lun "{image=textheart}{image=textheart}{image=textheart}"
    g9 "Ugh... by the gods! Her cunt goes wild every time!"
    $ ccg1 = "luna_30"
    lun "d-don't... {image=textheart}ah...{image=textheart}"
    $ ccg2 = "herm_17"
    her "Ohhh..."
    $ ccg2 = "herm_19"
    her "Someone's got a nasty little fetish don't they?"
    $ ccg1 = "luna_24"
    lun "No... it's not like that!"
    $ ccg1 = "luna_22"
    lun "It's just... mmmm...{image=textheart}{image=textheart}"
    lun "That's what... ah...{image=textheart}"
    $ ccg1 = "luna_21"
    lun "That's what {image=textheart}daddy{image=textheart} used to call me..."
    $ ccg2 = "herm_18"
    her "And hearing us call you a {b}good girl...{/b}"
    $ ccg1 = "luna_16"
    lun "mmmmm{image=textheart}{image=textheart}"
    g9 "Fuck yes..."
    $ ccg2 = "herm_17"
    her "Makes your pussy feel good?"
    $ ccg1 = "luna_20"
    lun "Y-y-yes...{image=textheart}"
    $ ccg1 = "luna_24"
    lun "Is that wrong?"
    $ ccg2 = "herm_23"
    her "no!"
    $ ccg2 = "herm_24"
    her "It's perfectly natural for you to get turned on by us calling you a good girl-"
    $ ccg1 = "luna_17"
    lun "a{image=textheart}a{image=textheart}ahhhhh{image=textheart}"
    $ ccg2 = "herm_25"
    her "just like your {b}daddy{/b} used to..."
    $ ccg1 = "luna_31"
    lun "{size=+10}!!!{/size}"
    $ ccg1 = "luna_32"
    lun "mmmm I think I'm getting close Hermione!"
    g9 "argh!!! Me too!"
    menu:
        "-Cum inside-":
            g9 "GET READY SLUTS!"
            $ ccg1 = "luna_33"
            lun "W-w-what?"
            $ ccg2 = "herm_26"
            her "Aren't you going to pull out [genie_name]?"
            g9 "HERE IT COMES!!!"
            $ ccg2 = "herm_27"
            her "I guess not then..."
            $ ccg1 = "luna_34"
            lun "You don't mean..."
            g9 "ARGH!!!"
            ">Your cock explodes inside Luna, unleashing an avalanche of your thick seed into her tight little pussy."
            g9 "BY THE NINE DIVINES!"
            $ ccg1 = "luna_35"
            lun "it's{image=textheart}Ican't{image=textheart}what{image=textheart}ahhhhhhhhh{image=textheart}{image=textheart}{image=textheart}"
            $ ccg1 = "luna_36"
            lun "..."
            $ ccg2 = "herm_25"
            her "Mmmm, just enjoy it Luna..."
            $ ccg2 = "herm_24"
            her "Be a {b}good girl{/b} for daddy and just let him pump you full of cum..."
            $ ccg1 = "luna_37"
            lun "{image=textheart}ah{image=textheart}"
            $ ccg2 = "herm_26"
            her "mmmm"
            her "{b}good{/b}"
            $ ccg1 = "luna_36"
            lun "mmm{image=textheart}{image=textheart}"
            $ ccg2 = "herm_25"
            her "{b}girl{/b}"
            $ ccg1 = "luna_38"
            lun "ah...{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
            pause
            show screen blkfade
            with d3
            ">It all proves too much for Luna, who passes out on your desk, cum still seeping out of her well used sex."

        "-Cum all over her-":
            g9 "GET READY SLUTS!"
            $ ccg1 = "luna_33"
            lun "W-w-what?"
            g9 "HERE CUMS DADDY!!!"
            $ ccg2 = "herm_24"
            her "mmm... do it [genie_name]!"
            $ ccg1 = "luna_39"
            lun "ah-ah-ah..."
            g9 "ARGH!!!"
            ">You pull your cock out at the last second, jerking it furiously as you shoot rope after rope of thick cum."
            g9 "BY THE NINE DIVINES!"
            $ ccg1 = "luna_40"
            lun "it's{image=textheart}Ican't{image=textheart}what{image=textheart}ahhhhhhhhh{image=textheart}{image=textheart}{image=textheart}"
            $ ccg1 = "luna_41"
            lun "..."
            $ ccg2 = "herm_25"
            her "Mmmm, just enjoy it Luna..."
            $ ccg2 = "herm_24"
            her "Be a {b}good girl{/b} for daddy and just let him coat you with his nasty cum..."
            $ ccg1 = "luna_42"
            lun "{image=textheart}ah{image=textheart}don't{image=textheart}call{image=textheart}it{image=textheart}nasty...{image=textheart}{image=textheart}{image=textheart}"
            $ ccg2 = "herm_26"
            her "mmmm"
            her "{b}good{/b}"
            $ ccg1 = "luna_43"
            lun "mmm{image=textheart}{image=textheart}"
            $ ccg2 = "herm_25"
            her "{b}girl{/b}"
            $ ccg1 = "luna_44"
            lun "ah...{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
            pause
            show screen blkfade
            with d3
            ">It all proves too much for Luna, who passes out on your desk, coated in a thick layer of your cum."
    hide screen ccg
    hide screen blkfade
    with d3
    call her_main("I think you broke her...","grin","wink")
    m "She's fine..."
    m "If I remember correctly, you had a similar response on your first time as well..."
    call her_main("[genie_name]!","shock","happy")
    m "Anyway, are you able to take call her back to her room?"
    call her_main("I'm not allowed in the Ravenclaw common room...","base","glanceL")
    call her_main("I guess I'll just have to take her back to my room...","grin","down_raised")
    m "I'm sure that's the only reason why..."
    call her_main("I don't have any idea what you're talking about sir...","base","glanceL")
    ">With a flick of Hermione's wand, Luna's clothes slither back onto her naked form."
    call her_main("Wingardium Leviosaaaaa!","open","happyCl")
    ">Luna's body lifts gently into the air, as if she was the star of a magic show."
    call her_main("Well I better be off [genie_name], it's getting a little late.","grin","happy")
    m "Goodnight [hermione_name]."
    call her_main("Goodnight {size=-5}daddy{/size}...","grin","narrow")
    ">Hermione turns and leaves your office, Luna's unconscious form floating through the air after her."

    jump luna_away
label luna_favour_8:
    jump luna_away
label luna_favour_9:
    jump luna_away
label luna_favour_10:
    jump luna_away
label luna_favour_11:
    jump luna_away
label luna_favour_12:
    jump luna_away
label luna_favour_13:
    jump luna_away
