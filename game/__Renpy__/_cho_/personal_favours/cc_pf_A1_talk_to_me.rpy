

### Talk with Cho ###

label cc_pf_A1_Talking:

    # Tier 1
    if cho_whoring in [0,1,2]:

        if cho_whoring == 0:
            # Ask about boyfriends.
            call cc_pf_A1_event1
        else:
            # Ask about boyfriends some more.
            call cc_pf_A1_event2

        if cho_whoring < 3: # Points til 2
            $ cho_whoring += 1
        if cc_pf_A1_Talking_OBJ.level < 2: # Hear 1+2
            $ cc_pf_A1_Talking_OBJ.level += 1

    # Tier 2
    elif cho_whoring in [3,4,5]:

        # Talk with Cho about her Quidditch team.
        call cc_pf_A1_event3
        # Has two branches.
        # Unlocks first public requests favour.

        if cho_whoring < 5: # Points til 5
            $ cho_whoring += 1
        if cc_pf_A1_Talking_OBJ.level < 3: # Heart 3
            $ cc_pf_A1_Talking_OBJ.level += 1

    # Tier 3+4
    else: # Repeatable events # Lewd
        pass

    # Stats
    $ cc_pf_A1_Talking_OBJ.points += 1

    jump end_cho_event



### Tier 1 ###

label cc_pf_A1_event1:

    m "How would you like to have a little chat with me?"
    g9 "Just so we get to know each other a little better."
    cho "Of course, Sir."
    cho "What would you like to talk about with-"
    m "Do you have a boyfriend, Miss Chang?"
    cho "I'm sorry?" # Shocked
    m "I asked if you have boyfriend. Anybody you fool around with?"
    cho "Me? Professor? He- hav- a boyfrind?" # Reluctant, Embarassed
    g9 "Or a girlfriend! That would be even better, now that I think about it!"
    cho "Sir that's-{w} that's not something a headmaster should be concerned about."
    cho "Why would it matter if- {w}Even if I did I'd-"
    g9 "So you don't have one?"
    cho "You are making me nervous, [cho_genie_name]. <3"
    m "(So cute.{w} She's almost making me feel things...)"

    cho "I do not, Sir. I don't have a boyfriend right now."
    g9 "A girlfriend then?"
    cho "No, Sir."

    ### ADD Bridge
    ### Genie needs to convince Cho to tell him about her boyfriends, starting with Cedric.

    # Cedric Diggory
    cho "Cedric was my boyfriend during most of my fifth school year."
    cho "At the time, Hogwarts was hosting the triwizards tournament."
    m "(They host tournaments here? Interesting...)"
    cho "That year was the most fun I've ever had!"
    cho "Sir, we should have this tourney every year, at least if you were to ask me!"
    g9 "(A slut tournament is what this school needs!)"
    m "I'll think about it..."
    m "Now tell me, why did you two end up together?"
    cho "You should know, Professor, I have a huge thing for athletes..."
    cho "Cedric was the representative champion of our school, so of course I had to date him."
    g4 "(Wait until you see me, girl. I'm shredded!)"
    cho "He even put his live at risk during it!"
    m "He surely will be missed."
    cho "Sir?" # Shocked
    m "Died just the way he lived,...{w} as a plot device."
    cho "Cedric isn't dead."
    m "Oh... he isn't?"
    cho "No!"
    m "He died in the books..."
    cho "What books?"
    g9 "And shortly after became a vampire."
    cho "Sir you are making no sense!"
    cho "Please don't joke about him that way. It's so unlike you..."
    cho "He's one of your best students! The best Hufflepuff has ever seen!"
    m "A Hufflepuff? Well, that explains so many things."
    m "If he's such an exceptionally great student, then why aren't you two still together?"
    cho "Things didn't work out, naturally..."
    cho "The tourney ended, and he didn't win, so..."
    m "That's why you two broke up?... Because he didn't win?"
    cho "Sort of. There is of course also the fact that he's on the opposite Quidditch team, as their Seeker."
    cho "It's the last chance to win the Quidditch cup for our house, for the both of us."
    cho "We'd constantly be at each other's throats."
    m "You are missing out, girl."
    g9 "Hatesex is the best!" # Small text
    cho "I didn't quite hear that, Sir."
    m "Yeah yeah, whatever. Who else did you do it with?"
    cho "Do it with?" # Shocked
    m "Smooshing, kissing, or whatever it is you kids do nowadays..."
    cho "With all due respect, Professor, it's very weird that you'd ask me about those sort of things,..."
    cho "But,... you are helping me. So I guess I'm fine with telling you everything."
    g9 "I do like the sound of \"everything\"!"

    # Fleur
    cho "Well, Cedric wasn't the only one I was with during the year the tourney took place..."
    m "You don't say."
    g9 "Please, elaborate!"
    cho "I was sort of dating somebody else. At the same time." # Embarrassed
    m "No{w} way!"
    g4 "You were cheating on that Hufflepuffer?"
    cho "It wasn't cheating, Professor. It wasn't even that serious with Cedric to begin with."
    cho "I was just fooling around a bit with somebody else. Trying out new things..."
    m "New things? Like what?"
    cho "Dating a girl, for example."
    m "(This keeps getting better and better...)"
    cho "She was one of the students from Beauxbaton."
    m "(...)"
    cho "A French girl."
    g4 "You frenched her?"
    cho "Among other things..." # Super embarrassed
    cho "(Why am I telling him this?)"
    cho "You probably know her, since Fleur was also a champion at the tourney."
    g4 "I'm in shock!"

    # Viktor
    cho "Then there also was Viktor Crum who-"
    g4 "Slow down, girl! I'm still not over the fact that you made out with a girl!"
    g9 "I want to hear everything!"

    cho "I'm sorry, Sir. It's just that,..."

    if daytime:
        cho "I'm really late for classes. May we postpone this talk for some other time?"
    else:
        cho "It's getting really late. May we postpone this talk for some other time?"

    ### This part could be fleshed out a bit more.

    m "Okay, girl. You may leave..."
    cho "Thank you, Sir."
    cho "See you next time."

    return





### Second event.
## Asking more questions abour her ex boyfriends and jerking off.

label cc_pf_A1_event2:

    ## Genie wasnts to know more about Cho's ex boyfriends again.
    ## There are 4 choices, two of them are more elaborate.
    ## She'll only have a quick chat with you about Cedric and Harry.
    ## She'll go into more detail with Fleur and Krum.
    ## Genie gets the option to jerk off during the Fleur and Krum talk.

    menu:
        "\"Tell me more about Cedric\"":
            ## Short chat with Cho about Cedric.
            ## No jerk off option for Genie.

            ### Should we make him a stalking kreep, like in the Twilight books?
            cho "There isn't much more to tell, [cho_genie_name]."
            cho "He never seemed to be too interested in me. Always had this dead-pan look in his eyes."
            cho "And he was oddle pale... "
            m "More signs of vampirism." # Small text
            cho "There surely are girls into boys looking like him, but I wasn't one of them."
            cho "But he was a good kisser, at the very least..."
            ## Add end of conversation.
            call nar("End of conversation. Writing not yet added.")

        "\"Tell me more about that Potter boy\"":
            ## Short chat with Cho about Harry.
            ## No jerk off option for Genie.

            cho "Potter?"
            m "Yeah, that boy Snape is always bitching about."
            cho "But I never dated him!"
            m "Wait a minute."
            g4 "Didn't you say you had a relationship with \"all\" of the tourney champions?"
            cho "Yes, with all three of them, Professor."
            cho "Potter wasn't one of the champions."
            m "He wasn't?"
            cho "No. He never threw his name into the Goblet of fire."
            with hpunch
            g4 "He never threw his name into the goblet o' fiya?"
            m "(Wait, why am I getting all riled up? I don't even know what that's supposed to mean.)"
            cho "No, [cho_genie_name]. He wasn't allowed to participate."
            m "So you never did anything with him?"
            cho "I know for a fact that he has a thing for me, but I'm not interested in Harry."
            cho "Plus, he's always surrounded by Granger."
            ## Add end of conversation.
            call nar("End of conversation. Writing not yet added.")


        "\"Tell me more about Fleur\"":
            ## Elaborate chat with Cho about Fleur.
            ## She gets into detail about her and all the kissing the've done.
            ## Maybe even talk about Fleur's sister...
            ## French dirty talk?
            ## Genie gets the option to jerk off or pay attention.
            ## Continue
            call nar("Writing not yet added.")

        "\"Tell me more about Crum\"":
            cho "He was at this school for only the year, so I naturally made the most out of it."
            ## Same options as with Fleur.
            ## They did more than just kissing.
            ## She was jealous when she saw him making out with Hermione, so Cho made it her mission to take him from her.
            ## Cho reluctantly tells you about the BJ she gave him.
            ## (Spoiler, she did even more with him but won't tell you that in this conversation!)
            ## Continue
            call nar("Writing not yet added.")
    return





### Tier 2 ###

# Event 1 & 2
# Has two branches
label cc_pf_A1_event3:

    # Intro
    if cho_whoring < 2:
        cho "Another chat, Professor?"
        cho "Are you going to ask me inappropriate questions again? About my previous relationships?"
        m "Not today. I'd like to hear more about Quiddish."
        cho "Quidditch, [cho_genie_name]."
        m "Are you getting along with your team well?"
        cho "I'd say so."
        cho "It's been difficult for me at first too. A sport so dominated by men."
        cho "Getting accepted into the team as a girl is rare. It's a shame how women are always getting treated unfairly."
        m "(Not this again...)"
        cho "Quidditch at our school has been no exception to this. Very few teams have allowed a female player into their ranks over the years."
        cho "And I've been the only female seeker at this school in over half a century. Can you even believe that, [cho_genie_name]?"
        m "(A century? That's like a coffee brake for me girl...)"
        cho "I don't want to brag, [cho_genie_name], but the role of a seeker is \"the\" most important position in a team by far!"
        cho "If you don't have a good seeker, you have no chance of winning!"
        m "Which is why you need my help so badly..."
        m "Because of your exceptional talents."
        cho "No, [cho_genie_name]! It's not about me!"
        m "So it isn't your fault that you're constantly losing?"
        cho "Of course not! I'm always giving my best."
        cho "It's the other team's fault. They are cheating!"
        cho "Every year it has been the same. And I'm growing more and more desperate with my situation."

    # Third & Repeated Event
    else:
        m "Tell me some more about Quidditch."
        cho "Gladly, [cho_genie_name]."

    m "(...)"

    menu:
        "-Jerk off while she is talking-":
            $ cho_jerk_off_counter += 1
            hide screen cho_chang
            hide screen bld1
            with d5
            pause.8
            call gen_chibi("jerking_off_behind_desk")
            pause.8

        "-Participate in the conversation-":
            pass

    cho "Ever since I was a little girl this has been my dream..."
    cho "[cho_genie_name], can you even believe how \"hard\" it was for me?"
    if masturbating:
        g4 "Yes It's so hard for you, you little slut!!!"
    cho "How difficult it was for me?"
    cho "Being accepted?"
    cho "I'm the only female in my team. The only girl that has made it onto the Ravenclaw team in over a decade!"
    cho "Constantly surrounded by other men."
    if masturbating:
        g4 "And you want to fuck all of them you whore!"
    cho "Even on my own team, I can constantly feel their gazes behind my back."
    cho "If it wasn't for our team leader, I would have been thrown out already, and I know it."
    cho "My own team, [cho_genie_name]. They sometimes treat me like the plague..."
    cho "Anywhere I go with them. Be it the pitch, the dormitories, our classrooms, or the showers..."

    if masturbating:
        pass

       #ADD Jerk off section here.

    else:
        m "Wait a second. You shower \"with\" your team?"
        cho "Of course, [cho_genie_name]. It was after my request, after all."
        cho "They shouldn't exclude me from team activities just because I'm a girl."
        cho "It makes absolutely no difference!"
        m "Just to be clear. You are naked with them, in the shower."
        cho "Of course we are all naked, [cho_genie_name]!"
        cho "Why would anyone take showers with their clothes still on?"

        m "So seeing you naked had nothing to do with the way they act?"
        cho "Of course not. We are all just friends!"
        g9 "I bet some of them would like to be more than \"just friends\" with you!"

        # Cho is shocked
        cho "[cho_genie_name]!"
        cho "But, they are my team. I have known them for years..."
        m "Let me ask you a question."
        m "Do they always have their backs turned to you in the showers? And only to you?"
        cho "May I... May I leave, [cho_genie_name]?"
        m "Yes you may leave now."
        cho "Thank you, [cho_genie_name]."
        # Cho very slowly walks out of your office...

    return



###  Stretching ###

label cho_stretching:

    #If you begin masturbating:
    #Tell me how you get ready for practice...

    #If you don’t masturbate:
    #How about you do some squats for me...

    # Choice to start jerking off
    menu:
        "\"(I will jerk off a little while she talks.)\"":
            $ cho_jerk_off_counter += 1
            $ masturbating = True
        "\"(I’ll ask her to show her flexibility instead.)\"":
            $ masturbating = False
            m "In that case..."

    #Tell me how you get ready for practice:
    if masturbating:
        m "How about you start by telling me a little bit about your Quidditch training. How do you get ready for practice for example?"
        cho "Okay..."
        cho "Well, we usually wake up pretty early in the morning..."
        "You take your cock out and begin stroking it underneath your desk"
        cho "Once I’m up I usually start by doing some stretches to get the blood flowing."
        g4 "\"Keep talking and you’ll get mine going pretty soon.\""
        cho "Sometimes I’ll have to do it in the dark not to wake anyone up..."
        m "\"Wakey wakey..."
        cho "As during later parts of the year the sun hasn’t even risen yet!"
        g9 "\"There we go, it’s risen... Good morning!\""
        cho "When I’m done with stretching I get dressed and make myself down to the great hall for breakfast..."
        g4 "\"Hhng... nude stretching...\""
        cho" As a player on a Quidditch team we get the whole hall to ourselves and a specially protein rich and energy filled filled breakfast."
        m "\"Yes, protein rich... that’s important. I’ll have to remember that one...\""
        cho "And then...{nw}"
        cho "Sir, are you still paying attention?"
        m "What?"
        # Genie stops masturbating
        cho "..."
        g9 "Protein rich breakfast... very important..."
        cho "Quite..."
        cho "Anyway..."



    #How about you do some squats for me:
    else:
        m "How about you start by doing some squats..."
        cho "Squats, sir?"
        m "Yes, squats... You know, bend your knees and stretch your arms forward..."
        cho "I know what squats are..."
        cho "I’m just a bit confused as to why you want me to start doing squats in your office."
        m "Well, I need to see if what you’re claiming is true. I’d like to see for myself if you’re really on par with the rest of your team."
        m "You’re asking a lot of me here if I were to break up any sort of student movement for you."
        cho "I don’t...{nw}"
        m "Unless what you’re saying is just a lie and you’re also just one of those amateur posers that you mentioned..."
        cho "..." # Annoyed, blushing
        cho "I’m not... look! Can a poser do this?"
        # cho squats down (could just be sprite for starter)
        # Later on if we add more chibi positions she’d show off even more here
        m "Impressive..."
        cho "Thank you..."
        m "How about a handstand?"
        cho "A handstand..."
        cho "That hasn’t been part of my training so far..."
        m "I see.."
        cho "But I could...{nw}"




### Old Writing ###

label cho_favor_1:
    $ current_payout = 20

    if cho_whoring <= 0:
        m "{size=-4}(All I'll do is admire her body a bit...){/size}"
        menu:
            "\"(Yes, let's do that.)\"":
                pass
            "\"(Not right now.)\"":
                jump cho_requests

    hide screen cho_chang
    call blkfade
    pause.2
    hide screen blkfade
    call cho_main(xpos="mid",ypos="base",trans="d5")

    if cho_whoring <= 0:
        jump cho_favor_1_1 #First time event.
    elif cho_whoring <= 1:
        jump cho_favor_1_2 #Second time event.
    else:
        jump cho_favor_1_3 #Third time event.



# Favour 1 - First time event.
label cho_favor_1_1:
    menu:
        "\"Take off your top\"":
            m "[cho_name], why don't you take off your top?"
            call cho_main("What, already? Shouldn't we talk a little bit first?","open","wide","sad","L")
            m "Not really..."
            m "Besides, Miss Granger is more than happy to show me her-"
            call cho_main("Fine...","pout","base","angry","R")
            call nar(">Cho quickly removes her tie before starting to undo her shirt.","start")
            call nar(">Her inexperience is obvious and she struggles for a moment.","end")
            $ cho_wear_top = False
            call cho_main("Sorry, about that.","open","base","sad","mid")
            g9 "Don't worry, girl. You're doing great!"
            call cho_main("Thanks.","angry","base","sad","R")
            m "Now take off your skirt..."
            call cho_main("O-okay...","horny","base","sad","down")
            call nar(">Cho takes a deep breath, then swiftly drops her skirt.")
            $ cho_wear_bottom = False
            call ctc
            jump let_cho_strip

        "\"Take off your skirt\"":
            m "[cho_name], why don't you take off your skirt?"
            call cho_main("What, already? Shouldn't we talk a little bit first?","open","wide","sad","L")
            m "Not really..."
            m "Besides, Just thinking about Miss Granger's ass makes me-"
            call cho_main("Fine, I'll do it...","pout","base","angry","R")
            call nar(">Cho takes a deep breath, then swiftly drops her skirt.")
            $ cho_wear_bottom = False
            call cho_main("There, my skirt is gone!","angry","base","sad","down")
            g9 "I can see that, Miss Chang!"
            m "Now take off your shirt..."
            call cho_main("O-okay...","open","base","sad","mid")
            call nar(">Cho quickly removes her tie before starting to undo her shirt.","start")
            call nar(">Her inexperience is obvious and she struggles for a moment.","end")
            $ cho_wear_top = False
            call ctc
            jump let_cho_strip

        "\"Come here and suck my cock!\"":
            m "{size=-5}(Too early for this... It's always too early for this...){/size}"
            jump cho_favor_1_1

        "\"Do you eat ass, Miss Chong?\"":
            call cho_main("Miss... Chong?","open","wide","raised","mid")
            call cho_main("My name Is Chang, [cho_genie_name],... Cho Chang!","open","angry","angry","mid")
            call cho_main("...","pout","suspicious","angry","R")
            m "..."
            m "(She didn't answer my question...)"
            $ cho_mood += 5
            jump cho_favor_1_1


    label let_cho_strip:
        call cho_main("Um, I forgot to ask, but how many points do I get for this?","open","base","sad","mid")
        m "You're a terrible negotiator."
        call cho_main("I know.","smile","base","sad","R")
        call cho_main("What do you pay Hermione?","soft","base","raised","mid")
        m "(Too much if you ask me...)"
        m "A couple of points, maybe..."

        call cho_main("I bet my body is worth more than hers!","open","base","base","mid")
        call cho_main("Does Hermione have abs like this? Of course she doesn't!","horny","base","raised","down")
        if her_whoring < 17:
            call cho_main("That boring book glutton is sitting at the library all day as if it's her home...","open","angry","angry","mid")
        else:
            call cho_main("That stupid slut can't spend even a single day without flirting with somebody that has legs attached...","open","angry","angry","mid")

        call cho_main("I wake up every morning before dawn and run the Quidditch pitch, until the sun rises!","angry","suspicious","angry","mid")
        call cho_main("My body's at the absolute peak of human and wizard conditioning!","open","angry","angry","mid")
        g4 "It is quite impressive, I've got to say!"
        call cho_main("Glad to hear it, [cho_genie_name].","smile","angry","angry","mid")
        call cho_main("Now... How badly do you want me to take off the rest?","soft","angry","base","mid")

        m "(...)"
        m "I will give you..."

        menu:
            "-10 points-":
                call cho_main("(10 points... I hope that's a good price.)","horny","suspicious","sad","downR")
                call cho_main("I guess that's ok, [cho_genie_name].","angry","suspicious","sad","down")
                call blktone
                m "(Really? She'd strip down for barely anything?)"
                m "(Even Hermione gets more points for just her mindless talking...)"
                g4 "(Now she made me feel bad... I should probably pay her a little more.)"
                call hide_blktone
                m "Only the first time, Miss Chang. I will pay you 20 regularily."
                call cho_main("Ok! Thank you, [cho_genie_name].","smile","base","sad","mid")
                $ current_payout = 10
            "-20 points-":
                call cho_main("20 sounds reasonable.","soft","base","base","R")
                m "It sure does..."
                call cho_main("(...)","angry","base","base","R")
                m "(Is it just me, or is the middle choice always the boring one...?)"
                m "Anyway..."
                $ current_payout = 20
            "-100 points-":
                call cho_main("100?","scream","wide","raised","mid")
                call cho_main("Wow, that's a lot!","open","base","raised","L")
                m "(Yeah, it's way too much... what was I thinking?)"
                m "Just today, Miss Chang. I will pay you 20 after this time."
                call cho_main("Thank you so much, [cho_genie_name].","smile","base","base","mid")
                $ current_payout = 100

        g9 "Why don't you thank me by taking off that bra?"
        call cho_main("Of course, sir.","horny","base","sad","down")
        pause.5
        $ cho_wear_bra = False
        call ctc
        call cho_main("I bet my tight body looks way better than Hermione's...","soft","base","raised","mid")

        menu:
            "-Yeah, she's gross-":
                m  "Miss Granger's body is nothing compared to yours."
                call cho_main("Really?","open","wide","raised","mid")
                m  "Her tits sag too much, and her fat hips are disgusting..."
                call blktone
                g4 "(I think something inside me just died saying this.)"
                call hide_blktone
                call cho_main("She really is a...","open","closed","raised","mid")
                call cho_main("...stupid...","angry","closed","angry","mid")
                call cho_main("...fat...","angry","suspicious","angry","mid")
                call cho_main("...cow, isn't she?","quiver","suspicious","angry","mid")
                $ cho_mood = 0
            "-I can't choose-":
                m  "You're both hot."
                call cho_main("I guess.","pout","suspicious","angry","downR")
            "-Nope, you lose-":
                m "I'm afraid, Miss Granger is simply... how shall I put it... sexier!"
                call cho_main("What?","scream","wide","angry","mid")
                m "Besides, jealousy is quite unbecoming of a young witch like yourself..."
                call cho_main("But she doesn't even do work-outs, [cho_genie_name]!","angry","suspicious","angry","downR")
                $ cho_mood +=5

        jump jerk_off_to_cho



# Favour 1 - Second time event.
label cho_favor_1_2:

    m "Miss Chang, how would you like to earn 20 house points the easy way?"
    call cho_main("What do i have to do?","base","suspicious","sad","down")
    m "I want to see your body!"
    call cho_main("You want me to get naked, sir?","open","base","sad","R")
    m "Of course."
    m "If you're not interested, I'm sure Hermione wouldn't mind..."
    call cho_main("!!!","pout","wide","sad","mid",trans="hpunch")
    call cho_main("I'll do it.","horny","base","sad","R")
    $ cho_wear_top = False
    call cho_main("There! How is that?","horny","base","sad","R")

    menu:
        "-Be aggressive-":
            g9 "Nice!"
            m "Now the bottom."
            call cho_main("Yes, uhm... [cho_genie_name].","pout","base","sad","mid")
            $ cho_wear_bottom = False
            call cho_main("(House points...loads of house points...)","horny","closed","sad","mid")
            $ cho_wear_bra = False
            call cho_main("(Am I really doing this?)","angry","base","sad","down")
            $ cho_wear_panties = False
            call cho_main("(Too late now...)","angry","closed","sad","mid")
            call ctc

            m "Very good."
            call cho_main("(...)","upset","closed","sad","mid")
            call cho_main("Uhm... is that enough?","annoyed","wink","sad","mid")

        "-Be nice-":
            m "Go on, girl."
            call cho_main("Yes, sir!","smile","base","sad","R")
            call nar("Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips.")
            $ cho_wear_bottom = False
            m "Nice."
            call cho_main("Thank you, [cho_genie_name].","base","closed","base","mid")
            call nar("Her hands nervously move to her bra.")
            call cho_main("Is this okay?","pout","base","sad","mid")
            $ cho_wear_bra = False
            call cho_main("What do you think?","horny","angry","sad","R")
            m "Simply gorgeous."
            call nar("Finally, she pushes her panties down.")
            $ cho_wear_panties = False
            call cho_main("...","upset","closed","sad","mid")
            g4 "Very nice."
            call cho_main("(...)","pout","base","sad","mid")
            call cho_main("Um...","base","base","sad","R")
            call cho_main("Can I put my clothes back on now?","open","suspicious","sad","down")

    jump jerk_off_to_cho



# Favour 1 - Third time event.
label cho_favor_1_3:

    m "Miss Chang, how would you like to earn 20 house points the easy way?"
    call cho_main("What do i have to do?","base","angry","sad","mid")
    m "I want to see your body again."
    call cho_main("You want me to get naked, sir?","horny","suspicious","sad","down")
    m "Of course."
    m "If you're not interested, I'm sure Hermione wouldn't mind..."
    call cho_main("!!!","scream","wide","sad","mid")
    call cho_main("I'll do it.","smile","base","base","R")
    call cho_main("Only...","open","angry","sad","mid")
    call cho_main("You're not going to...you know...again, are you sir?","horny","angry","sad","mid")
    m "And what would that be, girl?"
    "Cho shifts uncomfortably on her feet."
    call cho_main("Don't make me say it, Professor.","open","angry","sad","R")
    m "Say what, girl?"
    call cho_main("....masturbate.","horny","angry","sad","mid")
    m "What was that?"
    call cho_main("You're not going to jerk off again, are you?","open","base","angry","mid")

    label cho_wants_you_to_jerk_off:
    menu:
        "-Be Aggressive-":
            "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
            m "Get on with it, girl."
            call cho_main("Yes, [cho_genie_name]!","base","base","sad","R")
            $ cho_wear_top = False
            "Cho grits her teeth and removes her top in one swift motion."
            m "That's better. Now the bottoms."
            call cho_main("Yes, [cho_genie_name].","pout","base","sad","mid")
            $ cho_wear_bottom = False
            "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
            call cho_main("(house points...loads of house points....)","smile","base","base","mid")
            "Her hands nervously move to her bra."
            $ cho_wear_bra = False
            "She pulls it up, over her head, and lets it fall to the ground."
            $ cho_wear_panties = False
            "Finally, she pushes her panties over her hips."
            m "Very good."
            call cho_main("........","smile","base","base","mid")

        "-Be Nice-":
            "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
            m "Go on, girl."
            call cho_main("Yes, [cho_genie_name]!","smile","base","sad","R")
            $ cho_wear_top = False
            "Cho flashes a subdued smile and removes her top in one swift motion."
            m "Nice."
            call cho_main("Thank you, [cho_genie_name].","base","closed","base","mid")
            $ cho_wear_bottom = False
            "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
            call cho_main("is this okay?","pout","base","sad","mid")
            "Her hands nervously move to her bra."
            $ cho_wear_bra = False
            "She pulls it up, over her head, and lets it fall to the ground."
            call cho_main("what do you think?","horny","angry","sad","R")
            m "Simply. gorgeous."
            $ cho_wear_panties = False
            "Finally, she pushes her panties over her hips."
            m "Very nice."
            call cho_main("........","upset","closed","sad","mid")

        "-I hadn't planned on it-":
            m "I hadn't planned on it."
            call cho_main("Oh.","pout","base","sad","R")
            call cho_main("Okay then.","base","base","base","mid")
            jump cho_wants_you_to_jerk_off

    jump jerk_off_to_cho



### Jerking off to naked Cho ###
label jerk_off_to_cho:
    menu:
        "-Start jerking off-":
            hide screen cho_chang
            hide screen bld1
            with d3
            pause.2
            call gen_chibi("jerking_off_behind_desk")
            pause.8

            if cho_mood <= 0: #OK with it.
                if cho_whoring in [0]:
                    call cho_main("(!!!)","angry","wide","raised","mid")
                    call cho_main("[cho_genie_name], are you...","horny","suspicious","sad","R")
                    call nar(">Cho's voice is soft and slightly husky. She almost sounds...aroused.")
                    call cho_main("Touching yourself?","quiver","suspicious","angry","down")
                    call cho_main("[cho_genie_name], I didn't agree to this...","angry","suspicious","sad","down")
                elif cho_whoring in [1]:
                    call cho_main("[cho_genie_name]...","horny","suspicious","raised","mid")
                    call cho_main("You are touching yourself.","quiver","suspicious","raised","down")
                else:
                    call cho_main("I knew you would do that...","smile","angry","angry","mid")

                label keep_jerking_off_to_cho:
                menu:
                    "-Keep jerking off-":
                        if cho_whoring in [0]:
                            call nar(">Your eyes continue to drift over the young Quidditch players tight, athletic body.","start")
                            call nar(">You lean back in your chair and begin stroking in earnest.","end")
                        call cho_main("...","quiver","suspicious","raised","downR")
                        call nar(">The young seeker looks mesmerized by your actions.")
                        call cho_main("...","quiver","suspicious","base","down")
                        call nar(">Her eyes glued to your thick cock.")

                        if cho_whoring in [0]: #Not really ok with it.
                            call cho_main("I-I've never seen one before.","open","suspicious","sad","down")
                            call cho_main("Are they always so... BIG?","smile","suspicious","raised","down")
                            m "(Look at the body on that slut!)"
                            call cho_main("(...)","horny","suspicious","sad","downR")
                            call ctc

                            call cho_main("[cho_genie_name], how much longer are you going to-","horny","suspicious","sad","downR")
                            g4 "Here it comes!"
                            call cum_block
                            call gen_chibi("cumming_behind_desk")
                            call cum_block
                            call cho_main("(...)","horny","wide","sad","L")
                            hide screen bld1
                            with d3
                            pause.2
                            call gen_chibi("came_on_desk")
                            pause.8
                            call bld
                            m "I think that was it..."
                            call cho_main("Can I have my points now, [cho_genie_name]?","smile","base","base","R")
                            m "Sure..."

                            if cho_whoring <= 0:
                                $ cho_whoring = 1

                            jump end_cho_favor


                        if cho_whoring >= 1: #Very OK with it!
                            if cho_whoring in [1]:
                                call cho_main("It's so big...","horny","suspicious","raised","down")
                                call cho_main("Does it always get like this??","soft","base","raised","mid")
                            else:
                                call cho_main("Keep stroking your cock, [cho_genie_name].","open","angry","angry","down")

                            menu:
                                "-Tell her to shut up-":
                                    if cho_whoring <= 1:
                                        m "Quiet, girl! Don't ruin this for me."
                                        call cho_main("...","annoyed","angry","angry","mid")
                                        call cho_main("","base","closed","base","mid")
                                        call ctc
                                        g4 "(Is she flexing her muscles?!)"
                                    else:
                                        m "Shut up, [cho_name],... and start flexing those muscles!"
                                        call cho_main("Of course, [cho_genie_name].","horny","base","raised","downR")
                                        call ctc
                                    call nar(">You pump your cock faster and faster...")
                                    g4 "(Look at those fucking abs on that girl!)"
                                    call nar("Cho's athletic, young body has you hard as stone.")
                                    g4 "(I want to play xylophone on it...)"

                                "-Play along-":
                                    if cho_whoring <= 1:
                                        m  "Only when I'm around athletic students like you, Miss Chang."
                                        call cho_main("...","horny","base","raised","R")
                                        call cho_main("I'm glad to hear that, [cho_genie_name].","soft","base","base","mid")
                                        m "Such a nice body you have there..."
                                    else:
                                        m "I can't help it, [cho_name]."
                                        m "When I get to see young girls, with bodies like yours..."
                                        g4 "I always get hard!"
                                    if cho_whoring <= 1:
                                        call cho_main("[cho_genie_name], does Hermione let you grope her?","horny","wink","raised","mid")
                                        g9 "She does!"
                                        call cho_main("Maybe next time, [cho_genie_name], I'll give you something that feels a lot nicer than her disgusting tits!","soft","closed","raised","mid")
                                        call ctc
                                    else:
                                        call cho_main("Is my body that good?","quiver","suspicious","raised","mid")
                                        call ctc
                                        call cho_main("You're' dripping everywhere, professor","horny","suspicious","sad","downR")
                                        call cho_main("oh god...your balls looks so full. There's so much.","horny","base","raised","down")
                                        call nar("The perverse wonder in Cho's voice pushes you over the edge.")
                                    call cho_main("Wouldn't you just love to touch every muscle on my bod-","soft","base","raised","R")

                            g4 "Fuck, here it comes!!!"
                            call cum_block
                            call gen_chibi("cumming_behind_desk")
                            call cho_main("[cho_genie_name]?!","soft","wide","raised","down")
                            call cum_block

                            if cho_whoring <= 1:
                                call cho_main("(Wow. He's cumming so much...)","horny","base","raised","downR")
                                call cho_main("(Just from looking at my body...)","base","base","base","down")
                            else:
                                call cho_main("(Look at all that cum!)","horny","wide","raised","down")
                                call cho_main("......","horny","base","base","downR")
                                call cho_main("(I wonder what it tastes like...)","quiver","suspicious","raised","L")

                            hide screen bld1
                            with d3
                            pause.2
                            call gen_chibi("came_on_desk")
                            pause.8
                            call bld
                            m "Girl, that was amazing!"
                            call cho_main("...","horny","base","raised","mid")

                            if cho_whoring <= 1:
                                call cho_main("(I can't believe I agreed to that...)","horny","suspicious","sad","down")
                                call cho_main("Can I have my points now, [cho_genie_name]?","soft","base","base","mid")
                            else:
                                call cho_main("I'd like to get my points now, [cho_genie_name].","soft","base","base","mid")
                            m "Of course..."

                            if cho_whoring < 2:
                                $ cho_whoring += 1

                            jump end_cho_favor


            else: #Cho is mad! Not OK with it!!!
                if cho_whoring in [0]:
                    call cho_main("(Is he?!)","angry","wide","raised","mid")
                    call cho_main("[cho_genie_name], stop!","scream","closed","angry","mid")
                    call cho_main("I won't let you do that!","open","angry","angry","mid")
                    m "Do what? I'm just scratching my leg..."
                    call cho_main("Don't take me for a fool! I know exactly what you are doing!","angry","closed","angry","mid")
                    call cho_main("Stop!","open","closed","angry","mid",trans="hpunch")
                    call cho_main("Touching!","scream","angry","angry","mid",trans="hpunch")
                    call cho_main("Yourself!!!","angry","angry","angry","mid",trans="hpunch")
                    g4 "Jeeze..., no need to scream like that..."
                    hide screen bld1
                    with d3
                    pause.2
                    call gen_chibi("sit_behind_desk")
                    pause.8
                    call bld
                    m "I will stop..."
                    m "scratching..."
                    m "my leg..."

                elif cho_whoring in [1]:
                    call cho_main("No,[cho_genie_name]! Stop doing that!","horny","wide","sad","L")
                    m "Doing what?"
                    call cho_main("Stop touching yourself!","horny","wide","sad","L")
                    m "Whatever... You ruined the mood anyway..."
                    call gen_chibi("sit_behind_desk")
                    m "Better?"

                else: #OK again!
                    call cho_main("[cho_genie_name]! You are touching yourself again!","horny","wide","sad","L")
                    m "What? Don't you like it?"
                    call cho_main("(...)","horny","wide","sad","L")
                    jump keep_jerking_off_to_cho

                call cho_main("Thank you, [cho_genie_name].","annoyed","angry","angry","R")
                call cho_main("Can I have my points now?","open","closed","raised","mid")
                m "Sure..."
                jump end_cho_favor

        "-Better not-":
            call nar(">You decide not to indulge your baser instincts.")
            m "Alright, Miss [cho_name]."

            if cho_whoring <= 0:
                $ cho_whoring = 1

            else:
                call cho_main("[cho_genie_name], are we done, already?","horny","base","sad","R")
                call cho_main("(I thought he would maybe...)","smile","base","base","R")
                m "Yes. We are done for today."
            jump end_cho_favor



label end_cho_favor:
    #if not first_cho_favor_done:
    #    $ first_cho_favor_done = True

    m "[current_payout] points to Gryffindor!"
    $ gryffindor += current_payout
    call cho_main("[cho_genie_name], I'm from Ravenclaw!","open","wide","raised","mid")
    m "Right, what did I say?"
    $ gryffindor -= current_payout

    m "[current_payout] points to Ravenclaw!"
    $ ravenclaw += current_payout
    $ cho_mood -= 10

    call cho_main("Thank you.","soft","base","base","mid")

    call nar(">Cho quickly puts her clothes on before leaving.")
    call load_cho_clothing_saves
    if daytime:
        call cho_main("Good day, [cho_genie_name].","smile","base","base","mid")
    else:
        call cho_main("Good night, [cho_genie_name].","smile","base","base","mid")
    call play_sound("door")

    jump end_cho_event
