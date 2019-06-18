

# Collar Event

label collar_scene:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call nar(">Hermione bursts into the room crying")

    call her_main("[genie_name], am I a slut?","angry","base",tears="soft",xpos="right",ypos="base")
    m "What are you talking about?"
    call her_main("Susan Bones is telling everyone in the school that I'm a slut!","open","angryCl")
    m "Why is this Miss Bones calling you a slut?"
    call her_main("Because she found out what we are doing! She's telling everyone that I'm your slut!","soft","base",tears="soft")
    call her_main("My reputation is ruined! What will people think when they find out what I've been doing with my ninety year old Professor?","mad","worriedCl",tears="soft_blink")
    call her_main("I'll be known as a slut for the the rest of my life!","scream","worriedCl")
    her "I'll never be able to get a good job..."
    her "My friends will hate me..."
    call her_main("Please, You don't think I'm a slut do you [genie_name]?","open","base")

    menu:
        "-You are a slut-":
            jump slut_scene
        "-You're a whore-" if her_reputation >= 21:
            jump whore_scene
        "-No, you're a slave-" if her_whoring >= 21:
            jump slave_scene
        "-Of course not, you're a good girl-":
            jump good_girl_scene

label slut_scene: #Locked to her being your slut

    m "Of course you're a slut."
    call her_main("!!!","angry","base",tears="soft")
    m "You come here nearly every day and do unspeakable things. A normal girl doesn't let her headmaster fuck her in the ass."
    call her_main("I knew it... How will I be able to live this down?","mad","worried",tears="soft")
    m "You won't. You'll have to embrace it."
    call her_main("What?","angry","base",tears="soft")
    m "There's no coming back for a slut like this. Even if I leave you'll just find some other cock to please."
    call her_main("Sir... please.","angry","worriedCl",emote="05")
    m "Don't act like you don't already know this. You know that deep down you're a filthy slut."
    call her_main("I am not!","scream","worriedCl")
    m "Suck my cock."
    call her_main("...What?","open","base")
    m "I said suck. My. Cock. Slut."
    call her_main("...","annoyed","worriedL")
    hide screen hermione_main
    with d3

    call her_walk_desk_blkfade #Hides her_main, her_chibi, screen-tones, calls blkfade.

    ">Hermione walks over and kneels before you as you pull out your cock from your robes."

    call play_music("playful_tension") #HERMIONE
    hide screen genie
    $ gen_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ her_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ her_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    $ h_c_u_pic = "hand_ani"
    show screen chair_left
    show screen h_c_u

    hide screen hermione_stand #Hermione stands still.
    hide screen blktone
    hide screen bld1
    call hide_blkfade
    call ctc

    call bld
    $ hermione_zorder = 8
    m "That's a good little slut. Now if you want to suck my cock I expect you to ask nicely."
    call her_main("What? This is bad enough, just let me suck \nyour cock.","upset","wink")
    hide screen hermione_main
    m "Sluts beg for cock. And seeing as how you're a slut, I expect you to beg."
    call her_main("...","normal","worriedCl")
    hide screen hermione_main
    call her_main("Please [genie_name], let me suck your cock.","open","base")
    hide screen hermione_main
    m "Hmmm that was almost good enough. Try again, a little harder."
    call her_main("Pretty please [genie_name], please let me suck\nyour big beautiful cock.","scream","worriedCl")
    hide screen hermione_main
    m "Good girl."

    menu:
        "-Throat fuck-":
            m "Here's you reward slut!"
            ">You grab the back of her head and force your cock into her mouth and to the entrance of her throat."
            show screen g_c_u
            hide screen h_c_u
            with d3
            call her_main("!!!","shock","wide")
            hide screen hermione_main
            ">You feel her push back against your legs."
            m "Now, now [hermione_name] good sluts know how to deepthroat. Just relax your throat."
            call her_main("eeettsss hhooooo hhhhggggg!","open_wide_tongue","down_raised")
            hide screen hermione_main
            m "Come on [hermione_name] you are a good slut aren't you."
            call her_main("...","open_wide_tongue","angryCl")
            hide screen hermione_main
            ">Hermiones throat relaxes and allows you to enter."
            m "Ughhh! Your throat is so tight. You're such a filthy little slut aren't you?"
            call her_main("*Slurp!* *Gltch!* *Gulp!*","open_wide_tongue","base")
            hide screen hermione_main
            m "I asked you a question slut."
            call her_main("hhyyym aaaa hhhhtttt","open_wide_tongue","angry")
            hide screen hermione_main
            ">You increase the speed in her throat."
            m "What was that [hermione_name]? I couldn't hear you over you sucking my cock. Try speaking a little louder."
            call her_main("hhhhyyyyyym aaaaaaa hhhhhhhhttttttt!","shock","wide")
            hide screen hermione_main
            ">The vibration from her throat on your penis is amazing."
            m "Once more, so that I can hear you."
            ">You pull her head off your cock."
            show screen h_c_u
            hide screen g_c_u
            with d3
            call her_main("{size=+10}I'm a slut!{/size}","scream","worriedCl")
            hide screen hermione_main
            m "Yes you are."
            ">You impale her back into your cock."
            show screen g_c_u
            hide screen h_c_u
            with d3
        "-Let her suck you-":
            m "Well if you insist [hermione_name]."
            ">Hermione takes you into her waiting mouth."
            show screen g_c_u
            hide screen h_c_u
            with d3
            m "See, don't you feel better now that you have a cock in your mouth?"
            call her_main("mmmmmmm","open_tongue","glance")
            hide screen hermione_main
            m "Admit it, you love this."
            call her_main("*Slurp!* *Gulp!* *Slurp!*","open_wide_tongue","down_raised")
            hide screen hermione_main
            m "You love being used as someone else's plaything."
            call her_main("*Gulp!* *Gobble!* *Gobble!*","open_wide_tongue","angryCl")
            hide screen hermione_main
            m "You might act upset that people will find out what you are."
            call her_main("*Gulp!* *Gobble!* *Slurp!*","open_tongue","glance")
            hide screen hermione_main
            m "But deep down, you're just glad that you don't have to act like you're not a massive slut."
            call her_main("*Slurp!* *Gobble!*","open_wide_tongue","angryCl")
            hide screen hermione_main
            m "Aren't you"
            call her_main("...","open_wide_tongue","down_raised")
            hide screen hermione_main
            m "I asked you a question slut."
            show screen h_c_u
            hide screen g_c_u
            with d3
            ">She takes you out of her mouth."
            call her_main("...yes. I am a massive slut.","normal","worriedCl")
            hide screen hermione_main
            m "Good to hear you finally admit it. Now, back in the mouth."
            call her_main("Yes [genie_name]","smile","glance")
            hide screen hermione_main
            ">Hermione takes you back into her mouth with renewed effort."
            show screen g_c_u
            hide screen h_c_u
            with d3

    m "Ughhh, I'm getting close girl."
    m "Get ready."
    ">Hermione starts focusing on the tip of your cock, licking your slit."
    m "That did it. Here it comes!"
    ">You pull out of her mouth and start pumping your cock."
    $ g_c_u_pic = "cum_on_face_ani"
    $ u_sperm = "characters/hermione/face/auto_07.png"
    $ uni_sperm = True
    m "Here's your reward you filthy fucking cumslut!"
    ">You explode across her face."
    ">One string of your cum even goes up her nostril."
    m "Who's a slut?"
    $ g_c_u_pic = "cum_on_face_blink_ani"
    call her_main("I am...","grin","baseL")
    hide screen hermione_main
    m "Good, well now that we've established that I have a present for you."
    call her_main("A present? What is it?","base","down")
    hide screen hermione_main
    m "It's a lovely necklace to help remember who you are."

    #sQuest "slave" collar reward
    call give_reward(">You present her the \"slut\" collar.\n \"slut\" collar added to your wardrobe.")

    call her_main("This isn't a necklace, this is a collar with slut \nwritten on it! I can't wear this!","angry","wide")
    hide screen hermione_main
    m "You can and will wear this."
    m "You are MY slut and you will do well to remember it. Now put it on and get out of my office."
    call her_main("...Fine","angry","down_raised")
    hide screen hermione_main
    ">She tightens the collar around the neck."

    $ h_neckwear = "collar_slave_shackle"
    $ h_request_wear_neckwear = True
    $ hermione_wear_neckwear = True
    $ collar = 2
    call update_her_uniform

    call her_main("Can I at least get a towel or something to \nclean my face?","angry","base")
    hide screen hermione_main
    m "Why? Everyone already knows what a slut you are, walking back to your room with a bit of cum on your face is hardly going to change that."
    call her_main("You can't be serious?!","upset","closed")
    hide screen hermione_main
    m "I am, and if you ever want to suck my cock again you will do as I say."
    call her_main("...yes [genie_name].","open","closed")
    hide screen hermione_main
    m "Well get going."
    call her_main("Good night [genie_name].","base","glance")
    hide screen hermione_main
    m "Good night. {w}Slut."
    call her_main("...","base","down")

    call her_walk(action="leave", speed=2.5)

    $ hermione_zorder = 5

    jump end_hermione_event


label whore_scene: #(locked behind the public her_whoring flag)

    #sex scene where she begs genie to cum inside her
    #genie yells at her and makes her admit she is a whore
    #he cums inside her
    #she then comes back later that night after Ginny makes the quidditch team use her

    m "You're not a slut [hermione_name]."
    call her_main("Thank you si-","mad","worried",tears="soft")
    m "You're worse than a slut, you're a whore."
    call her_main("What? What's the difference?","angry","base")
    m "A slut is someone who enjoys sex. A whore is someone who's addicted to it."
    m "You don't care where you get it do you? As long as someone uses you couldn't care less."
    call her_main("I-I-I-","open","worriedCl")
    m "You even fucked your best friends didn't you?"
    m "I bet you begged them to do it as well."
    m "Look at what you've become, nothing more than the school toy. Willing to give everyone a go."
    call her_main("Sir please, you're being too mean...","shock","worriedCl")
    m "Oh is the little whore getting upset? Don't worry, I'll make you feel all better."
    her "How?"
    m "Come over here and bend over."
    call her_main("You can't be serious? After what you just said?","angry","base")
    m "I am serious, now be a good little whore and bend over my desk and I'll give you what you want."
    call her_main("...","angry","down_raised")

    call her_walk_desk_blkfade
                                                                                                                                                                                  #HERMIONE
    hide screen genie
    $ gen_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ g_c_u_pic = "pause_sex"
    show screen chair_left
    show screen g_c_u
    call hide_blkfade

    $ hermione_zorder = 8

    ">Hermione walks over to your desk silently, bends over and presents herself."
    m "See what a good little whore you are. Now if you ask nicely I'll fuck you."
    call her_main("...","angry","down_raised")
    hide screen hermione_main
    call her_main("Please [genie_name].","open","down")
    hide screen hermione_main
    m "Please what?"
    call her_main("Please fuck me...","mad","worried",tears="soft")
    hide screen hermione_main
    m "I'm not sure I quite heard that. You'll have to speak up."
    call her_main("{size=+5}Please fuck my cunt{/size}","scream","wide")
    hide screen hermione_main
    m "Seeing as how you asked nicely."
    $ g_c_u_pic = "sex_ani"
    ">You take a firm grip of her hips and thrust into her sopping pussy."
    m "Ugh you're still so tight."
    m "I thought that you would have loosened up after all the guys you've fucked."
    call her_main("[genie_name]...","open","worriedCl")
    hide screen hermione_main
    m "Don't try and act innocent with me [hermione_name]. I know what you do in the dormitories after dark."
    m "Just admit what you are."
    call her_main("{size=-5}I'm a whore.{/size}","grin","ahegao")
    hide screen hermione_main
    m "What was that, I couldn't hear you ever the sound of me fucking you."
    call her_main("I'm a whore.","silly","ahegao")
    hide screen hermione_main
    m "Very good, now beg me."
    call her_main("Beg you to what?","silly","dead")
    hide screen hermione_main
    m "Beg me to cum inside your pussy, whore."
    call her_main("Please fill my little pussy with your thick cum.","grin","dead")
    hide screen hermione_main
    m "That's a good little whore, who else have you told that to?"
    m "Is it just me or do you beg every other boy you meet to cum inside you?"
    call her_main("...","angry","wink")
    hide screen hermione_main
    m "Tell me girl."
    call her_main("I beg every boy that fucks me to cum inside!","shock","worriedCl")
    hide screen hermione_main
    m "What a fucking whore."
    call her_main("I-I'm cumming.","open","surprised",cheeks="blush",tears="messy")
    hide screen hermione_main
    m "Well I think I might join you then."
    ">You increase your pumping of her pussy."
    m "Here's your cum, whore. You earned it."
    ">You push yourself all the way in and start shooting off into her womb."
    $ g_c_u_pic = "sex_cum_in_ani"
    call her_main("!!!","scream","surprised",cheeks="blush",tears="messy")
    hide screen hermione_main
    m "That's it, take it all you fucking slut."
    call her_main("...","grin","dead",cheeks="blush",tears="messy")
    hide screen hermione_main
    m "Well aren't you going to at least be grateful."
    call her_main("...Thank you [genie_name].","base","concerned",cheeks="blush",tears="soft")
    hide screen hermione_main
    m "Thank you for what?"
    call her_main("Thank you for ... cumming in my pussy.","grin","dead",cheeks="blush",tears="messy")
    hide screen hermione_main
    m "You're welcome girl. A good whore should always be grateful."
    call her_main("Yes [genie_name].","grin","closed",cheeks="blush",tears="mascara")
    hide screen hermione_main
    call blkfade

    show screen genie
    hide screen chair_left
    hide screen g_c_u
    call her_chibi("stand","desk","base")
    hide screen blkfade
    with d3
    $ hermione_zorder = 5
    ">Hermione gets to her feet"
    m "Well seeing as how you said thank you I have a present for you."
    call her_main("A present?","open","concerned",cheeks="blush",tears="mascara")
    m "Yes, it's a lovely piece of jewelery to commemorate your self-acceptance."

    #sQuest "whore" collar reward
    call give_reward(">You present her the \"whore\" collar.\n \"whore\" collar added to your wardrobe.")

    call her_main("A collar? That says whore?","open","squint",cheeks="blush")
    call her_main("How is this a piece of jewelery?","open","annoyed",cheeks="blush")
    m "Well I expect you to wear it all the time, like a ring, so I guess that qualifies it as jewelery."
    call her_main("You expect me to wear this all the time? Not just in your office.","scream","angry",cheeks="blush",tears="messy")
    m "Of course. I already know what a whore you are, this is so that everyone else will know."
    call her_main("What will people think of me?","scream","worriedCl",cheeks="blush",tears="messy")
    m "They'll think the truth, that you're a shameless whore."
    call her_main("...Hmmph","angry","suspicious",cheeks="blush")
    m "Well whatever you think, I expect you to put it on and then get out of my office."
    call her_main("...Fine","shock","down_raised",cheeks="blush",tears="crying")
    ">She places the collar around her neck and tightens it."

    $ h_neckwear = "collar_whore_shackle"
    $ h_request_wear_neckwear = True
    $ hermione_wear_neckwear = True
    $ collar = 3
    call update_her_uniform

    call her_main("Goodbye [genie_name].","angry","dead",cheeks="blush",tears="crying")
    m "Goodbye whore."

    call her_walk(action="leave", speed=2.5)

    $ hermione_zorder = 5

    jump end_hermione_event


label slave_scene:

    m "Don't be silly [hermione_name], you're not a slut."
    call her_main("Thank yo-","base","base")
    m "You're a slave."
    call her_main("I'm a what?","upset","wink")
    m "You're a slave Miss Granger. Specifically, my slave."
    call her_main("What are you talking about? I'm not your slave.","angry","angry")
    m "Are you sure? You come in here whenever I summon you, eager to do whatever I say."
    m "Just begging to do anything to please me."
    m "When was the last time you even said no to me?"
    call her_main("Well, I...","annoyed","worriedL")
    m "Exactly, you've become my slave and you didn't even realise it."
    call her_main("Just because I care about my house doesn't mean that-","angry","worriedCl",emote="05")
    m "Please, when was the last time you even cared about getting your points?"
    m "You just want to please me. Those points are an excuse you tell yourself so you don't have to acknowledge what you are."
    m "Now be a good girl and bend over the desk."
    call her_main("...","angry","base")

    call her_walk_desk_blkfade

    hide screen genie
    $ gen_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ g_c_u_pic = "pause_sex"
    show screen chair_left
    show screen g_c_u
    hide screen hermione_stand #Hermione stands still.
    call hide_blkfade

    $ hermione_zorder = 8
    ">Hermione walks over to your desk, bends over it and then lifts her skirt up."
    call her_main("Yes [genie_name].","angry","down_raised")
    hide screen hermione_main
    m "That's a good little slave girl."
    m "Now ask me nicely to fuck that little ass of yours."
    call her_main("Please [genie_name], please fuck my slutty ass.","open","closed")
    hide screen hermione_main
    m "Good girl."
    ">You thrust your full length into her in one motion."
    $ g_c_u_pic = "sex_ani"
    m "You're very tight today, are you enjoying this?"
    call her_main("Yes [genie_name], I'm loving this.","base","ahegao_raised")
    hide screen hermione_main
    m "Good, make sure you keep your ass nice and tight for me."
    ">You pick up speed and begin to fuck her ass in earnest."
    m "Now tell me girl. Who do you belong to?"
    call her_main("You.","open","down")
    hide screen hermione_main
    m "Good, and who am I?"
    call her_main("Professor Dumbledore.","grin","baseL")
    hide screen hermione_main

    call slap_her

    "You unleash a firm slap across her buttocks."
    m "That's not who I am to you [hermione_name]. To you I am your master."
    m "Do you understand now?"
    call her_main("Yes.","angry","base",tears="soft")
    hide screen hermione_main

    call slap_her

    " You give her another powerful slap that leaves a bright red mark."
    m "Yes what?"
    call her_main("Yes master.","angry","base",tears="soft")

    $ genie_name = "Master"

    hide screen hermione_main
    m "Good, you're a fast learner."
    m "Now if I'm your master then what does that make you?"
    call her_main("{size=-7}a slave{/size}","soft","base",tears="soft")
    m "What was that, I couldn't quite make that out."
    call her_main("A slave.","mad","worried",tears="soft")

    $ hermione_name = "Slave"

    hide screen hermione_main

    call slap_her

    ">You give her yet another strong slap across her buttocks."
    m "You aren't just some common slave [hermione_name]."
    call her_main("I'm not?","annoyed","annoyed")
    hide screen hermione_main
    m "No, of course not."
    m "You're my personal slave."
    call her_main("I think I'm about to cum master.","angry","down_raised")
    hide screen hermione_main

    call slap_her

    ">You give her a fierce slap to her left buttock."
    m "You will come when I give you permission and not a second sooner."
    call her_main("Please master, may I cum?","angry","wide")
    hide screen hermione_main
    m "Not until I do."
    call her_main("Please hurry.","open","worriedCl")
    hide screen hermione_main
    m "Well put some effort in then girl. If you want me to cum then you better start acting like it."
    ">Hermione starts pushing back against you and rotating her hips as you thrust into her."
    m "That's it girl. Almost there, just a little more..."
    ">You grab her hips and impale her on your throbbing member."
    m "Ughhh"
    $ g_c_u_pic = "sex_cum_in_ani"
    ">You roar as you cum inside her tight hole."
    call her_main("I'm cumming!","scream","wide")
    hide screen hermione_main
    ">You continue to shoot ropes of cum into her asshole."
    call her_main("Thank you sir.","soft","ahegao")
    hide screen hermione_main

    call slap_her

    ">Slap!"
    m "What was that girl? It almost sounded like you didn't call me master."
    call her_main("Thank you master, thank you master.","grin","dead")
    hide screen hermione_main
    m "That's it girl."
    ">Hermione closes her eyes as she rides out the last of her orgasm."
    m "On your knees girl."
    call her_main("W-w-what? Why?","angry","base")
    hide screen hermione_main
    m "Because I said so. Now get off the table and on to your knees."
    call her_main("Yes master.","angry","down_raised")
    hide screen hermione_main
    $ gen_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ her_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ her_chibi_ypos = 10
    $ h_c_u_pic = "hand_ani"
    hide screen g_c_u
    show screen h_c_u
    ">Hermione pulls herself of the table and kneels in front of you."
    m "Tell me what you are."
    call her_main("Master's slave.","base","down")
    hide screen hermione_main
    m "That's a good answer. And because you are such a good girl I'm going to give you a present."

    #sQuest "slave" collar reward
    call give_reward(">You present her the \"slave\" collar.\n \"slave\" collar added to your wardrobe.")

    call her_main("What's this?","base","glance")
    hide screen hermione_main
    m "This is a collar, so that everyone will know that you're my slut."
    call her_main("Do I have to wear this all the time?","base","suspicious")
    hide screen hermione_main
    m "Yes you do."
    call her_main("...","angry","down_raised")
    pause       ###new
    call her_main("Yes master...","angry","wink")
    hide screen hermione_main
    ">She tightens the collar around her neck."

    $ h_neckwear = "collar_slut_shackle"
    $ h_request_wear_neckwear = True
    $ hermione_wear_neckwear = True
    $ collar = 1
    call update_her_uniform

    m "That look suits you girl."
    call her_main("Thank you master. Will I be getting any points \ntoday?","base","down")
    hide screen hermione_main
    m "Hahaha, of course not. Slaves aren't paid girl, that's what makes them slaves."
    call her_main("I suppose your right.","base","glance")

    hide screen hermione_main
    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","mid","base")
    #call fade <- label does not exist

    call her_walk(action="leave", speed=2.5)

    $ hermione_zorder = 5

    jump end_hermione_event


label good_girl_scene:

    m "Of course you aren't Miss Granger."
    m "You're just doing everything you can to help your friends."
    call her_main("*sob* Really [genie_name]?","open","worriedCl")
    m "Really. You wouldn't have done any of this if the point system was fair would you?"
    call her_main("*sob* I guess not...","angry","base")
    m "I'm sure once Miss Bones realizes what you are doing this for she will understand."
    call her_main("Do you really think so [genie_name]?","angry","down_raised")
    m "I do, you're a good girl Miss Granger."
    call her_main("Thank you [genie_name].","base","base")
    m "Once Gryffindor wins the house cup no one will even remember what they said about you they'll be so grateful."
    call her_main("Yes, you're right [genie_name]. I suppose that I was just overreacting.","base","happyCl")
    m "Don't worry about it."
    call her_main("Before I go...","grin","baseL")
    call her_main("Do you think that you could buy a favour off of me?","smile","glance")
    m "Sure, what would you like to do?"
    call her_main("Well I suppose that I could show you my breasts.","base","down")
    call her_main("For 50 points of course...","angry","wink")
    m "That seems fair."
    call her_main("Thank you [genie_name].","base","glance")
    ">Hermione slowly lifts her top."

    call set_her_action("lift_top")
    call ctc

    call her_main("Do you like them [genie_name]","annoyed","base")
    m "Of course I do, they're lovely."
    call her_main("Thank you [genie_name], you're always so kind.","base","closed")
    ">She lowers her top."

    call set_her_action("none")
    pause.5

    m "50 points to Gryffindor."
    $ gryffindor += 50
    call her_main("Thank you [genie_name]. Have a nice night.","smile","angry")
    m "You too [hermione_name]."

    $ collar = 4

    call her_walk(action="leave", speed=2.5)

    $ hermione_zorder = 5

    jump end_hermione_event
