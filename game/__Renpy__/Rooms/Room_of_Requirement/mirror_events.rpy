#Regex find h\s+"([ -}]+)"
#Regex replace (call her_main\("\1","base","base" \))

label a_bad_time_to_disrobe:
    call h_equip_temp_outfit(hg_standart_school_ITEM)
    menu:
        "Part 1":
            jump a_bad_time_to_disrobe_part_1
        "Part 2":
            jump a_bad_time_to_disrobe_part_2

label a_christmas_tale:
    show screen blkfade
    with d5
    pause 2

    call room(hide_screens=True)

    centered "{size=+7}{color=#cbcbcb}A Christmas tale{/color}{/size}"

    pause 2

    $ temp_time = daytime #Switch 'daytime' back to this at the end of the store.
    $ daytime = False #Night
    $ interface_color = "gray"
    $ room_deco = "_deco_1" #Xmas deco
    $ gen_chibi_stand = "characters/misc/santa/santa_chibi.png"

    call room("main_room")
    hide screen genie
    show screen chair_left
    show screen desk
    show screen fireplace_fire
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    show screen main_room_overlay

    hide screen blkfade
    with d3

    pause 1

    call play_music("anguish")
    show screen bld1
    with d3
    nar "It was the night before Christmas, with excitement at the school."
    nar "But the headmasters room empty, now where is that fool?"
    nar "The stockings were hung by the chimney with care,"
    nar "But no genie to be found. As if he'd never been there."
    hide screen bld1
    with d3
    pause.8

    call play_sound("door")
    call sna_chibi("stand","door","base")
    with d5
    pause.8

    show screen bld1
    with d3
    nar "Severus then entered, all flustered and spent."

    call sna_walk(xpos="mid", ypos="base", speed=2.5)
    pause.2

    call sna_main("Genie? Where are you... I came here, to vent...",face="snape_03",ypos="head")
    nar "He wondered if the genie had found a way home..."
    call sna_main("Seems like a normal Christmas, spent all alone...",face="snape_06")

    nar "But then a crash and a bang from the chimney was heard."
    call play_sound("bump")

    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.2

    call sna_main("What the fuck was that, some kind of bird?",face="snape_14")
    nar "With a snap and a crackle, and a strong blinding light."

    call play_sound("bump")
    hide screen fireplace_fire
    call gen_chibi("stand","620","150")
    call teleport("genie")
    pause.8

    nar "A figure appeared, in the most silent of nights."
    pause.2

    call gen_chibi("stand","620","150",flip=True)
    with d3
    pause.2

    show screen bld1
    with d3
    san_[1] "Oh hello there my friend."
    nar "Said the figure at last."
    san_[1] "I thought you might be here, but where's that genie?"
    call sna_main("...",face="snape_25")
    san_[1] "Blast..."

    call sna_main("Genie...",face="snape_24")
    nar "Said the teacher."
    call sna_main("You're not fooling me.",face="snape_24")
    call sna_main("Have you been drinking again?",face="snape_25")
    call sna_main("And I don't mean drinking tea.",face="snape_29")

    san_[1] "I don't know what you mean."
    nar "Said the large bearded man..."
    san_[2] "I'm santa of course."
    san_[2] "I bring presents...."
    san_[2] "That's the plan!"
    pause.8

    nar "After silence and confusion then Severus said..."
    call sna_main("Well, just get it over with so I can go back to bed.",face="snape_09")
    san_[1] "Now boy where's your spirit, it's Christmas is it not?"
    call sna_main("Now genie, look here...",face="snape_24")
    nar "But then he froze on the spot."

    hide screen bld1
    call gen_chibi("hide")
    call teleport("genie")
    with d3
    pause.5

    show screen bld1
    with d3
    nar "The man had then vanished, without even a trace.."
    hide screen bld1
    with d3

    pause.2
    call sna_chibi("stand","mid","base",flip=False)
    with d3
    pause.5
    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.8

    call sna_main("I thought he couldn't use magic...",face="snape_05")
    nar "You should've seen the look on Snapes face."
    hide screen bld1
    with d3

    call sna_chibi("hide")
    with d3
    call sna_chibi("stand","570","190",flip=True)
    with d3
    pause.5

    show screen bld1
    with d3
    nar "With only a gift left where he had stood, should he open or should he wait?"
    call sna_main("My first present since childhood...",face="snape_04")
    nar "As he peeled back the wrapping he just stood there in shock."
    call sna_main("Where on earth did he get this?",face="snape_03")
    nar "Then suddenly..."
    call play_sound("knocking")
    nar "A knock."

    s "Snape are you in there, I think I lost my keys."
    call sna_main("The door is open, you fool.",face="snape_08",xpos="base",ypos="base")
    nar "His voice... now just a wheeze."

    call play_sound("knocking")
    nar "The genie knocked again. The mutter, he hadn't heard."
    call sna_main("",face="snape_06")
    nar "Now Snape saying nothing, not even a word."
    show screen snape_picture_frame
    with d5
    nar "A picture we then see as it's our time to depart."
    call sna_main("",face="snape_23")
    nar "As sadness turned to joy in the cold teachers heart."
    call ctc

    hide screen snape_picture_frame
    hide screen snape_main
    with d5
    pause.8

    san_[4] "Happy Holidays."

    if not card_exist(unlocked_cards, card_santa):
        if deck_unlocked:
            call give_reward("You have received a special card as a gift!", "images/cardgame/t1/special/santa_v1.png")
        $ unlocked_cards += [card_santa]

    show screen blkfade
    with d9
    pause 2

    call room(hide_screens=True)

    #Reset
    $ daytime = temp_time
    if daytime:
        $ interface_color = "gold"
    else:
        $ interface_color = "gray"
    call update_gen_chibi

    #Unlock Xmas Deco
    $ unlocked_xmas_deco = True

    jump enter_room_of_req



label a_bad_time_to_disrobe_part_1:
    call room("main_room")
    show screen blkfade
    with d3

    nar "In this story the genie has found an invisibility cloak."
    nar "And with the cloak comes great opportunities"
    nar "Title: A bad time to disrobe."

    call her_chibi("stand","desk")

    hide screen blkfade
    with d3

    m "Miss Granger. Have you ever been excited about the thought of being caught?"

    call her_main("Caught?","base","base",xpos="right",ypos="base")
    call her_main("In what way professor?","base","base")

    m "Well, for today's favour I have a prop for you to use."

    call her_main("A prop sir?","base","base")

    m "Yes, I'd like you to put this invisibility cloak on and sneak into one of the boy only areas of the school."

    call her_main("Well, I guess that would be fine...","base","base")
    call her_main("Seems a bit different than your usual requests.","base","base")

    m "You'd be naked of course."

    call her_main("Naked!?! But what if someone saw me?","open","wide")

    m "You'll be wearing the cloak..."
    m "No one would even know you were there."

    call her_main("{size=7}35 points...{/size}","annoyed","angryCl")

    m "25 points you said? sounds good to me."

    call her_walk(xpos="door", ypos="base", speed=2.5)

    call her_main("{size=7}You heard what I said...{/size}","annoyed","closed",ypos="head")
    call her_chibi("leave")

    g9 "\"Some of that bartering skill put to good use...\""

    show screen day_to_night
    with d3

    nar "Later that evening. Hermione returns."
    $ daytime = False
    call her_chibi("stand","desk","base")

    hide screen day_to_night
    with d3

    g9 "I'll take that cloak back if you don't mind."
    call her_main("Certainly.","base","base",xpos="right",ypos="base")
    m "Now, spill the beans."
    call her_main("I..I don't have any beans on me sir.","soft","narrow")
    m "\"Is this girl for real?\""
    m "It's just an expression, tell me... did you complete your assignment?"
    call her_main("I did sir. I snuck into the boys dormitory using the cloak as you suggested.","soft","happyCl")
    m "Naked?"
    call her_main("Naked..ish","disgust","baseL")
    m "How can you be naked...ish?"
    call her_main("Well, I had my underwear on, I'd be cold otherwise","base","base")
    m "Cold? You'd have the cloak on you..."
    m "What happened next then?"
    call her_main("Well, a few of the boys were in there.","base","base")
    call her_main("They were playing wizards chess...","base","base")
    call her_main("Pretty poorly in fact.","disgust","wink")

    m "..."
    m "I'm sorry miss Granger but you're going to have to do better than this."
    m "I expect better from you by now."
    call her_main("So, no points then?", "angry", "annoyed")
    m "No, I know you can do better."
    call her_main("Fine! I'll do better next time. Double points! I'll show you!","angry","angryL")
    m "That's the spirit. Your house will thank you when you beat the Slytherins by the end of the year."
    call her_main("Thank you professor... I'll remember that for next time.", "grin", "happy")

    show screen blkfade
    with d3

    show screen quistion_pop_up("Hermione will remember that")
    nar "Hermione returns the next morning, looking nervous but more determined than yesterday."
    $ daytime = True

    hide screen quistion_pop_up
    call her_chibi("stand","desk","base")

    hide screen blkfade
    with d3

    call her_main("I see that you have the cloak ready for me sir.","base","baseL",xpos="right",ypos="base")
    m "Indeed, I'm expecting better from you today girl."
    call her_main("I won't disappoint you sir!","grin","base")
    m "I'll be the judge of that..."

    show screen day_to_night
    with d3

    nar "Later that evening a distraught looking Hermione enters the office. "
    $ daytime = False

    call her_chibi("top_naked","desk","base")
    call h_equip_temp_outfit(hg_standart_school_noshirt_ITEM)

    hide screen day_to_night
    with d3

    call her_main("...","upset","base", tears="mascara_soft",xpos="right",ypos="base")
    m "What happened? Where's your shirt?"
    call her_main("What does it look like?","upset","base", tears="mascara_soft")
    m "Well, I know what it looks like..."
    call her_main("I didn't want to disappoint, sir, so I did what you asked...","soft","base", tears="mascara_soft")
    call her_main("I went into the girls changing room at the quidditch pitch and put my clothes in one of the lockers.","base","base", tears="mascara_soft")
    m "Well done. And then?"
    call her_main("I took the cloak and snuck into the boys changing room...","base","base", tears="mascara")
    call her_main("I stood next to the doorway so that they wouldn't bump into me.","base","base", tears="mascara")
    m "Great idea... and no one noticed?"
    call her_main("Well, at first... This damn cloak is too small.","angry","base", tears="mascara")
    call her_main("I thought I would be short enough to fit under it...","base","base", tears="mascara")
    call her_main("I didn't notice that my feet were visible...","upset","angry", tears="mascara")
    m "\"Well, that's a shame.\""
    call her_main("One of the boys saw me shuffle and moved to see what it was so I tried to get away but I slipped...and...and.","upset","shocked_raised", tears="mascara")
    g11 "And what?"
    call her_main("And I slipped and my butt fell out!","scream","surprised", tears="mascara")

    g9 "{size=18}30 POINTS TO....{/size}"

    call her_main("I'm not done!","open","down", tears="mascara")
    m "Sorry, you carry on my dear!"
    call her_main("I ran out and grabbed what I could of my clothes... I think the boy may have seen me.","soft","concerned", tears="mascara")
    call her_main("Professor.... I'm beginning to have second thoughts about this cloak idea.","soft","concerned", tears="mascara")
    m "The boy didn't see your face, that's what matters."
    m "You could've draped the cloak around your head and it would be enough."
    call her_main("Professor!","shock","wide_stare", tears="mascara")
    m "Just trying to lighten the mood."
    m "Here's an extra 5 points for a Job well done, miss Granger."
    g9 "35 points to Gryffindor!"
    call her_main("Thank you professor....","grin","base", tears="mascara")

    call her_walk (xpos="door", ypos="base", speed=2.5)

    call her_main("\"He's right, they wouldn't recognize me if I didn't show my face...\"","base","base", cheeks="blush", tears="mascara",ypos="head")
    call her_main("\"would they?\"","base","base", cheeks="blush", tears="mascara",ypos="head")

    call her_chibi("leave")
    "The End."

    call room(hide_screens=True)
    call reset_hermione
    call h_unequip_temp_outfit
    jump enter_room_of_req

label a_bad_time_to_disrobe_part_2:
    show screen blkfade
    $ temp_time = daytime
    $ daytime = True
    call play_standart_theme

    call room("main_room")
    call her_chibi("stand","desk")
    hide screen blkfade
    with d3

    m "Good afternoon miss Granger."
    call her_main("Good afternoon professor, what can I do for you today?","base","base",xpos="right",ypos="base")
    m "Glad you asked, I've got another task for you."
    call her_main("And what task may that be professor.","soft","baseL")
    m "Well miss Granger, I think somebody owes me a invisibility cloak."
    call her_main("Oh, do you want me to collect it from somebody?","open","base")
    m "That somebody is you miss Granger..."
    m "You left my cloak at the scene of the crime."
    call her_main("What crime professor, what have you gotten me into?","upset","annoyed")
    m "I'm talking about when you went to visit the boys changing room."
    m "Or have you forgotten already?"
    call her_main("{size=7}I've tried to.{/size}","upset","worriedL")
    m "Sorry?"
    call her_main("I said, I do remember.","normal","baseL")
    m "Right, well. Good invisibility cloaks are pretty hard to come by..."
    m "\"I think...\""
    call her_main("No they're not... they're mass produced as far as I know.","annoyed","base")
    call her_main("By house elves I bet...","disgust","angryCl")
    m "Hey now, I know they might be small but I wouldn't call them elves."
    m "In any case, the cloak has more of a sentimental value to me... lots of memories."
    g9 "\"Like the time where your butt fell out of it.\""
    g9 "Oh, the memories... you must retrieve it for me."
    call her_main("Fine, I'll do it... even though I hold you partly responsible for the situation that lead to me dropping it.","annoyed","angryCl")
    m "Great, let's not dwell on the past then."
    call her_main("...","normal","annoyed")
    call her_main("Do you happen to have any idea of where it is?","open","base")
    m "Well, it hasn't been reported as found so unless someone stole it there's only one place it could be."
    call her_main("The boys changing room?","base","down")
    g9 "The boys changing room."
    call her_main("And how many house points?","base","base")
    m "For what exactly?"
    call her_main("Retrieving the cloak of course.","annoyed","base")
    m "You're demanding house points, for your own mistakes miss Granger?"
    call her_main("But I thought...","upset","worried")
    m "..."
    call her_main("...","upset","down")
    m "Fine, but only if we continue where we left of."
    call her_main("With my butt out?!?","disgust","surprised")
    m "With your bu..."
    m "No, well... yes, but this time you'll be prepared."
    call her_main("But... what if they recognize me sir?","open","worried")
    m "You'd already know if they had recognized you..."
    call her_main("\"That's true...\"","soft","soft", cheeks="blush")
    call her_main("And then what, you want me to just walk away?","base","base", cheeks="blush")
    m "You can figure it out yourself miss Granger. Once you have the cloak it shouldn't be an issue getting away."
    call her_main("And I want...","open","base")
    m "I'll give you 40 house points for it."
    call her_main("\"I was going to ask for 30.\"","soft","squintL", cheeks="blush")
    call her_main("I'll do it...","base","base")
    g9 "Great, you're doing a great service to your house and making an old man very happy."
    call her_main("By getting your cloak back right?","base","worried")
    m "Right..."

    call her_walk(action="leave", speed=2.5)

    show screen day_to_night
    with d3

    nar "Later that evening"
    $ temp_time = daytime
    $ daytime = False
    call play_standart_theme

    call h_unequip_temp_outfit()
    $ hermione_wear_outfit = False #Otherwise the "action" won't show if she's wearing an outfit.
    call set_her_action("covering_uniform")
    call her_chibi("stand","door","base")

    hide screen day_to_night
    with d3

    call her_walk(xpos="desk", ypos="base", speed=2.5)
    pause.5

    call her_main("...","normal","dead", cheeks="blush",xpos="right",ypos="base")
    m "Mission success?"
    call her_main("...","normal","dead", cheeks="blush")
    m "Miss Granger?"
    call her_main("Oh, hello professor, yes. Here's your cloak back.","base","down")
    m "..."
    m "And?"
    call her_main("And what?","normal","worriedCl")
    m "And what about your assignment. How did it go?"
    call her_main("Oh... yes, it went very well thank you... no hurdles in any way.","soft","worriedL", cheeks="blush")
    m "Your face is glowing miss Granger, I can tell when you're being untruthful."
    call her_main("It is? I didn't even notice...","normal","down_raised", cheeks="blush")
    m "You're going to have to elaborate if you'd like those house points."
    call her_main("Oh... okay, I'l just go ahead then...","mad","base")
    m "Let me get the popcorn."
    call her_main("popcorn? Where would you get popcorn from in this office?","annoyed","base")
    g9 "Magic cupboard."
    call her_main("Right... well, I'll just start in that case shall I?","base","glanceL")
    call her_main("...","base","base", cheeks="blush")
    call her_main("So... I went to the boys changing room when they were in quidditch practice.","open","down")
    m "*CRUNCH*"
    call her_main("It's very messy in there... I thought the girls changing room was bad...","base","down_raised")
    m "*CRUNCH* *Chew* *Chew*"
    m "*CRUNCH*"
    call her_main("Anyway... so I rumaged around in that mess...","annoyed","worried")
    call her_main("I knew it had to have been somewhere between the showers and the doorway...","base","base")
    call her_main("After looking around for a while I noticed that the cloak had been pushed under one of the benches lining the wall.","open","down")
    call her_main("So I grabbed it and I thought I might as well disrobe and hide in the shower room with the cloak on.","base","down_raised")
    call her_main("But as I was stuffing my clothes in one of the lockers a boy walked in.","clench","worried")
    m "*CRUNCH*"
    call her_main("Professor!","scream","angry")
    g4 "*Cough* *Cough*... sorry."
    call her_main("It is hard to talk about this as it is without your chewing distracting me.","annoyed","angry")
    call her_main("Anyhow...","base","angryL")
    call her_main("I expected the team to be going for at least another 30 minutes.","open","base")
    call her_main("But that's when the boy walked in...","normal","closed")
    call her_main("And I panicked and threw the cloak over myself and hid in one of the toilets.","open","worriedL")
    m "Smart."
    call her_main("...","base","base", cheeks="blush")
    call her_main("Well, it would've been if I had remembered to lock it.","base","down_raised")
    g9 "Not that smart..."
    call her_main("Do you want me to continue or not?","annoyed","annoyed")
    m "You're the one receiving the points here, I'm just providing the means of earning them."
    call her_main("...","normal","down")
    call her_main("As I was saying...","base","down_raised")
    call her_main("I went into one of the toilets and I heard the boy shuffling outside.","base","closed")
    call her_main("The room was so small so I tried to back into a corner, but as he came in I knew it wasn't going to work...","base","down_raised", cheeks="blush")
    call her_main("So I prayed he wasn't about to sit down and instead I positioned myself above the toilet with my legs around the base.","clench","worriedCl")
    m "And did he sit down or not?"
    call her_main("No, but he was close enough for me to feel his...","mad","ahegao_squint")
    call her_main("His...","base","ahegao_intense")
    m "His what? miss Granger..."
    call her_main("Well... His Penis brushed up against my butt.","annoyed","closed", cheeks="blush")
    m "How did he manage that?"
    call her_main("The boy wasn't in there to relieve himself in the way I assumed...","open","angryCl", cheeks="blush")
    call her_main("I guess he wasn't paying attention to what sensation he was feeling on the tip of his...","normal","worried", cheeks="blush")
    call her_main("Anyway...","open","worriedL", cheeks="blush")
    m "..."
    call her_main("I'd like my points now.","base","down")
    m "Certainly miss Granger..."
    m "40 points to Gryffindor!"
    call her_main("Thank you professor...","soft","soft")

    call her_walk(xpos="door", ypos="base", speed=2.5)

    call her_main("\"I'm glad I had time to clean the cloak before walking in here...\"","base","dead", cheeks="blush",ypos="head")
    call her_main("\"That thing was massive...\"","normal","down",ypos="head")
    call her_main("\"What am I thinking? snap out of it...\"","base","worriedCl", cheeks="blush",ypos="head")

    call her_chibi("leave")

    "The end"

    call room(hide_screens=True)
    $ daytime = temp_time
    call play_standart_theme
    call reset_hermione
    call set_her_action("none")
    jump enter_room_of_req

label whose_points:
    call room(hide_screens=True)
    show screen whose_points_screen
    show screen blkfade
    with d3
    pause 0.3
    hide screen blkfade
    with d3


    m "Hello and welcome to whose points is it anyway."
    m "The show where everything is made up but the points don't matter."
    m "Just like at Hogwarts."

    call her_main("\"I hope I win! I need those housepoints.\"","base","squintL",ypos="head")

    m "First, let me introduce todays contestants."
    m "The curly haired harlot we all know and love. Give it up for Hermione."
    call play_sound("applause01")
    call her_main("...","grin","worried",cheeks="blush", xpos="left",ypos="base")

    m "The ravishing ravenclaw who'll rock your socks off. Luna! "
    call play_sound("applause01")
    call lun_main("heh...hello.","base","wink","base","mid",xpos="mid",ypos="base")

    m "And the small girl with a big personality. Astoria!"
    call play_sound("applause01")
    call ast_main("Hey!","scream","angry","angry","angry",xpos="right",ypos="base")

    pause.5
    hide screen hermione_main
    hide screen luna_main
    hide screen astoria_main
    with d5
    pause.5

    m "Today we're playing scenes from a hat."

    with hpunch
    hat "Stay the fuck away from me!"

    m "But the notes are already inside you. I put them there last night."

    hat "You put notes inside me without my consent? \n*Spits note out*"

    m "Looks like we have our first prompt."
    m "Things you might say in potions class... But also in your bedroom."

    call her_main("This cauldron hasn't been used for years. It's all moldy and full of muck!","grin","worried",cheeks="blush",xpos="right")

    hat "Boo, there's no cauldrons in the bedroom!"

    m "Quiet now, it was a good euphemism, 10 points to Gryffindor."
    call play_sound("applause01")
    hide screen hermione_main
    with d3

    call ast_main("Snape, get your gross hands off my shoulders, you creep!","clench","angry","angry","angry")

    m "I'm not sure you got the idea of the game there..."
    hide screen astoria_main
    with d3

    call lun_main("Oops. I was supposed to squeeze the mucus out with my hands and not crush it.","silly","closed","raised","mid")

    m "Sounds painful... 15 points to Ravenclaw."
    call play_sound("applause01")
    hide screen luna_main
    with d3

    call her_main("How's that worth more than mine...","annoyed","worried")
    hide screen hermione_main
    with d3

    m "Any more? On to the next prompt then. Hat?"

    hat "Sorry, what did you cough call me? That's \n\"Sorting\" Hat to you. (coughs out note.)"

    g9 "Things you might do in quidditch... but also with your lover..."

    call ast_main("I'm going first this time! I have a good one!","grin","base","base","mid")

    m "Go on...."

    call ast_main("Madam Hooch! Get your gross hands off my quidditch robes, you creep!" ,"clench","angry","angry","mid")

    m "Again, I don't think you understand the game..."

    call ast_main("Give me the points!","scream","narrow","narrow","mid")

    m "Disqualified!"

    call ast_main("Wait, you can do that?" ,"scream" ,"wide","wide")

    g9 "It's my game, I make the rules."

    call ast_main("\"We'll see about that....\"","upset","narrow","narrow")
    hide screen astoria_main
    with d3

    call her_main("My turn.")
    call her_main("I love the feeling of a hard wooden object between my legs. \nI tend to tense up during the climax.","grin", cheeks="blush")

    m "A bit direct but I like it. \n15 points to Gryffindor."
    call play_sound("applause01")
    hide screen hermione_main
    with d3

    call lun_main("It's quite exciting but also a bit hard. You need to make sure not to end up with one of the balls in your throat.","grin","seductive","raised","mid")

    g9 "\"I don't mind having you end up with one of mine in your throat one day\""

    m "20 points to Ravenclaw"
    call play_sound("applause01")
    hide screen luna_main
    with d3

    call her_main("\"Seems like pleasing the judge is the way to go. Only one round left...\"","annoyed","worried")
    hide screen hermione_main
    with d3

    call lun_main("...","grin","base","base","mid")
    hide screen luna_main
    with d3

    m "Last round ladies. You better make it a good one. It's still all to play for."
    m "The last note if you please!"

    hat "I'm all out, looks like you only wrote \ntwo after all!"

    m "That can't be right...."

    call ast_main("Let me check professor!","smile","base","base","mid")
    call ast_main("I found the last note, it was stuck under one of the folds!")
    hide screen astoria_main
    with d3

    hat "Are you calling me fat young lady?"

    call ast_main("I'll read it for you shall I?")

    m "Go ahead."

    call ast_main("Things that you would not share with your classmates... but would share with dumby.")
    hide screen astoria_main
    with d3

    m "\"I don't remember writing that one...\""

    call lun_main("I see invisible creatures... but people don't belie... ","soft","annoyed","sad","down")
    hide screen luna_main
    with d3

    call set_her_action("lift_top")

     # SEX THEME.
    call play_sound("scratch")
    stop music
    call her_chibi("lift_top","mid","base")

    call her_main("...","smile","worried")


    g9 "500 points to Gryffindor!"
    call play_music("playful_tension")
    hide screen hermione_main
    with d3

    call lun_main("That's cheating, I didn't even get to finish! ","scream","mad","angry","mid")
    hide screen luna_main

    m "Well, that's all for this episode of whose points is it anyway."

    call her_main("I win, all the points for me!","smile","worried")
    hide screen hermione_main
    with d3

    call lun_main("Don't end now! This game is rigged!","scream","mad","angry","mid")
    hide screen luna_main
    with d3

    m "And remember the points doesn't matter!"

    call her_main("Wait, they don't?!? I thought they were house points!","annoyed","worried")
    hide screen hermione_main
    with d3

    call ast_main("Harlot! Harlot! Harlot!","grin","happyCl","base","R")

    call lun_main("How do those points taste now? ","grin","base","base","mid")
    call lun_main("The whole wizarding world is going see your tits!","silly","base","base","mid")
    hide screen luna_main
    hide screen astoria_main
    with d3

    call her_main("Oh no, I forgot about that!","shock","worried", tears="crying")

    g9 "Good night!"
    call play_sound("applause01")

    "To be continued?"

    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")

    call room(hide_screens=True)
    call set_her_action("none")
    jump enter_room_of_req

label genie_house_elf:
    show screen blkfade
    call room("main_room")
    with d3

    pause 0.3
    hide screen blkfade
    with d3

    nar "This story takes place in between the introduction of Snape and first meeting Hermione."
    nar "The genie, the desk and the door:"
    nar "How does that door work? The genie thought."

    m "\"How do the people know I’ve summoned them? I don’t have a secretary...that I know of anyway.\""

    m "Have they been keeping a secretary from me? I should ask Sn..."

    nar "Snape then opened the door, his pointy nose protruding under his silky hair."

    call sna_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call sna_main("You called? ","snape_23", xpos="base", ypos="base")

    nar "Snape said with a smirk, doing his best to hide his amusement."

    g11 "How did you, how do you..."
    m "This door, how does it work?"

    nar " The genie said, now even more frustrated. "
    nar "The genie wasn’t used to this... this unfamiliar magic."
    nar "He was used to knowing the ins and outs of the universe. But this world, it was to alien to him..."
    nar "At least he knew things about aliens..."

    call sna_main("Well, you’re the headmaster are you not? ","snape_06", xpos="base", ypos="base")

    nar "Snape said as if that meant anything."

    nar "A look of confusion spread across the genies face which only made Snape smirk even more."
    nar "He then composed himself after seeing this unusual expression on the headmasters face."

    call sna_main("I keep forgetting that you don’t know these things.","snape_01", xpos="base", ypos="base")
    call sna_main("students learn it on day one.","snape_01", xpos="base", ypos="base")
    call sna_main("The headmaster is in control of the school and its inhabitants.","snape_24", xpos="base", ypos="base")

    nar "Snape said in a matter of fact sort of way."

    m "I know that, we have schools in my world too."
    m "But generally we don’t wave wooden sticks around yelling random words."

    nar "Snape flinched, as if the notion of magic consisting of waving a wand and yelling random words was utterly absurd."

    call sna_main("No. You’re literally in control over the school....look.","snape_08", xpos="base", ypos="base")

    nar "Snape says, pulling his wand out, waving it."

    call sna_main("Revelio!","snape_01", xpos="base", ypos="base")
    call sna_main(remove=True)

    nar "After a flash of light and a small pop a house elf appears in the corner of the room."

    call helf_main(" ")

    g5 "What the hell is that?"

    nar "The genie said, jumping onto the desk as if things appearing out of thin air was new to him."

    call helf_main(remove=True)

    call sna_main("That...is a house elf.","snape_01", xpos="base", ypos="base")

    m "A house...elf."
    g10 "Is that like a Santa's elf? "

    nar "The genie said, now climbing down to sit on his chair."

    call sna_main("Sort of, they don’t get paid so they do have that in common...","snape_05", xpos="base", ypos="base")

    nar "Snape muttered under his breath..."

    call sna_main("The houses elves here can send us messages so we can go where we're needed.","snape_05", xpos="base", ypos="base")

    call sna_main("He just sits here invisible during the day and cleans and eats at night.","snape_01", xpos="base", ypos="base")

    m "The house elf cleans?"
    m "I thought I had some sort of magic self cleaning desk..."

    nar "The genie said sheepishly."
    call sna_main(remove=True)

    call helf_main("No sir...")

    nar "Said the elf, trying its hardest to bite his tongue but failing."

    call helf_main("I see it all, I clean it all....every...last bit of it.")
    call helf_main(remove=True)

    call sna_main("...","snape_08", xpos="base", ypos="base")

    nar "After a few moments Snape turned around, started walking towards the door and said."

    call sna_main("If that is all, I’ll be in the dungeons.","snape_01", xpos="base", ypos="base")
    call sna_main("I’ve been working on a new cleaning solution.","snape_01", xpos="base", ypos="base")
    call sna_main("It might come in handy sooner than I thought.","snape_02", xpos="base", ypos="base")

    call sna_walk(action="leave", speed=2)

    nar "The door shut and silence spread across the room only interrupted after a few minutes by the house elf."

    call helf_main("So, should I turn invisible again sir?")

    m "Yes...yes that will be for the best."
    call helf_main(remove=True)
    "The end."

    call room(hide_screens=True)
    jump enter_room_of_req



#Title: Previously, at Hogwarts.
label prev_at_hogwarts:
    #Story Unlock requirements: Finish the first 3 Wizard Cards challenges.

    #Temporarily stored vars
    $ temp_date = day
    $ temp_gold = gold
    $ temp_day = daytime
    $ temp_color = interface_color
    $ temp_weather = weather_gen

    stop weather
    call play_music("stop")
    show screen blkfade
    with d9

    $ day = 1
    $ gold = 0
    $ daytime = True
    $ interface_color = "gold"
    $ weather_gen = 1
    $ show_weather()

    call room("main_room") # Hides all screens too.
    call gen_chibi("hide")
    show screen dumbledore

    pause 2

    centered "{size=+7}{color=#cbcbcb}Previously, at Hogwarts{w} school of Witchcraft and Wizardry...{/color}{/size}"

    pause 2

    call play_music("day_theme")
    hide screen blkfade
    with d9
    call ctc

    call play_sound("knocking")
    pause.8

    dum_[3] "Please, come in..."
    pause.2

    call sna_walk(action="enter", xpos="mid", ypos="base", speed=2.5)
    pause.5

    dum_[1] "Ah, Severus..."
    call sna_main("You called, sir?","snape_01",xpos="base",ypos="base")
    dum_[2] "Indeed, I wanted to talk to you about last night."
    call sna_main("Last night, sir?","snape_03")
    dum_[1] "Yes, last night... Don't think that I had forgotten already..."
    call sna_main("...","snape_04")
    call sna_main("I might have had a few. I hope I didn't say something inappropriate...","snape_05")
    dum_[2] "Quite... Do you remember why I hired you, Severus?"
    call sna_main("For my excellent potion making skills?","snape_25")
    dum_[1] "For your excellent potion making skills..."
    dum_[5] "{size=-6}And your piercing black eyes...{/size}"
    call sna_main("What?","snape_05")
    dum_[4] "What?"
    dum_[2] "I said, you're fierce and wise."
    call sna_main("...","snape_05")
    call sna_main("Why did you call me here again?","snape_03")
    dum_[1] "Ah yes, my apologies.... I got distracted."
    dum_[2] "How much do you remember from our previous discussion?"
    call sna_main("Not a lot... it's all a bit of a haze...","snape_04")
    dum_[1] "..."
    call sna_main("I think I mentioned a students spilling some flobberworm mucus down themselves which halted the whole lesson...","snape_01")
    call sna_main("And that Potter boy...","snape_08")
    dum_[3] "There it is..."
    call sna_main("The Potter boy?","snape_25")
    dum_[1] "Yes, I've noticed you've been quite stressed lately about this... Potter situation of yours for the lack of a better term."
    call sna_main("And your point?","snape_09")
    dum_[2] "Ah yes... my point."
    dum_[1] "Where was I again..."
    dum_[2] "Ah yes, your stress situation..."
    call sna_main("\"You're not really helping old man...\"","snape_08")
    dum_[1] "Have you tried a draught of peace?"
    call sna_main("What?","snape_03")
    dum_[2] "A draught of peace, it's a potion you know..."
    call sna_main("Are you joking with me right now?","snape_04")
    dum_[1] "I'm being quite serious... stress can be quite taxing on your body."
    call sna_main("I...","snape_01")
    call sna_main("I need a moment... I'll talk to you later Albus.","snape_06")
    dum_[1] "I thought we were getting somewhere..."
    call sna_main("...","snape_01")
    hide screen snape_main
    hide screen bld1
    with d3
    pause.2

    call sna_chibi("hide")
    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.2

    call sna_walk(action="leave", speed=2.5)

    call play_music("stop")

    dum_[2] "\"I don't think I'll ever understa-\""

    hide screen dumbledore
    show screen genie
    call teleport("desk")

    pause.8
    call bld
    m "..................?"
    m "Your majesty?"
    pause.2

    show screen blkfade
    with d9
    pause.8

    # Reset vars.
    $ day = temp_date
    $ gold = temp_gold
    $ daytime = temp_day
    $ interface_color = temp_color
    $ weather_gen = temp_weather
    $ show_weather()

    call room(hide_screens=True)
    jump enter_room_of_req



label a_spaced_out_conversation:
    $ temp_time = daytime
    $ daytime = False

    call room("main_room")

    hide screen genie
    hide screen chair_right
    $ fire_in_fireplace = True
    show screen fireplace_fire
    show screen desk
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    show screen blkfade
    with d3
    pause.3
    hide screen blkfade
    with d3

    nar "The flames flickered higher up the fireplace."
    nar "Licking in greedy hunger as if wanting taste the wine the two men sedately drank just out of the fire’s reach."
    nar "The men took no notice of the flames, except to silently acknowledge the warmth it provided."
    nar "They were an odd pair, these two, sitting as they frequently did, beside the old fireplace sipping wine."
    nar "One, dressed all in black, with matching flowing black hair, stared sullenly at his glass."
    nar "Perhaps it was the darkness surrounding him that made his skin look so pale."
    nar "And maybe it was only the voluminous robes wrapped loosely across his body that made him appear gaunt."
    nar "The other was even more mysterious..."
    nar "Draped in gray-white costume, he had a long, flowing beard and a curious aura of both age and vitality."
    nar "Sometimes, if the flames flickered just so, he almost appeared entirely different, as a burly, cowled man with a short curled beard."
    nar "They sat in front of the fire as they did on many nights and talked of worlds upon worlds. And of magic. The dark man was first to speak."

    call sna_main("So, let me try to understand this,","snape_05",ypos="head")

    nar "Snape said slowly."

    call sna_main("You live in a little bottle?","snape_05")

    nar "The gray figure nodded."

    call sna_main("How does that work?","snape_05")

    m "I believe it’s based on tessaracted space."

    nar "Genie said, his tone becoming akin to a professor lecturing a class."

    m "The whole process is very Loki."

    nar "Snape didn’t hear the last words as a flicker and shadow from the flames made Genie appear different."
    nar "Almost as if gleaming golden horns arose from his head."

    call sna_main("Come again?","snape_03")

    nar "Snape asked, gaping at the sight before it was gone so fast that he was left unsure he had seen anything."

    m "I said, they keep the whole thing low key."

    nar "Genie repeated."

    m "Keeps most people from knowing how they make it bigger on the inside."

    call sna_main("Most people?","snape_05")
    nar "Snape asked."

    m "Well, Who knows..."
    nar "Genie answered."

    call sna_main("Do you know?","snape_24")

    nar "Snape asked."

    m "Who knows."

    nar "Genie repeated."

    call sna_main("So, who knows?","snape_08")

    nar "Snape asked again, getting a little irritated."
    nar "Patience was not a trait Snape had ever cared to master."

    m "Yes, Who knows!"

    nar "Genie said."
    nar "Snape flicked his hands impatiently and just decided to move on"
    nar "Determining when Genie was serious or not was still beyond his ability."
    nar "Plus, there had been another one of those weird flickers and he could have sworn he had seen a multicolor scarf around Genie’s neck."

    call sna_main("And, you then grant the summoner three wishes?","snape_01")

    nar "Snape continued."

    call sna_main("Anything they want? You can make anything come true?","snape_05")

    m "Those are the rules of my existence, yes."

    nar "Genie replied, thinking, not for the first time, how limited his real life was."

    call sna_main("That seems stupid.","snape_09")

    nar "Snape said bluntly."
    nar "Genie smiled. Snape was never much for niceties."
    nar "Genie found it refreshing to talk with someone whose disdain for others so matched his own."

    nar "Snape frowned at that smile. He got along almost perfectly with Genie."
    nar "Their lusts and passions were quite similar..."
    nar "It’s just Genie’s sense of humor that made Snape doubt his seriousness sometimes."

    call sna_main("You’ve got the power of a god,","snape_06")

    nar "Snape pushed forward."

    call sna_main("Can’t you just magic yourself free?","snape_05")

    m "It doesn’t work that way,"

    nar "Genie said sadly."

    g "I can only grant magic to others."

    nar "Snape shook his head."

    call sna_main("It still seems stupid...","snape_06")
    call sna_main("What if I were to visit you in your world and make one of my wishes that you be free to use your magic however you should please?","snape_09")

    nar "Genie stared at Snape with something like wonder."
    nar "It takes quite a bit to make an ageless being like Genie gape in awe."

    g5 "That’s...That’s brilliant!"

    nar "Genie shouted."

    g6 "Great Gods, man, that could actually work!"

    nar "Snape was taken aback by Genie’s enthusiastic shout, but quickly recovered."
    nar "He was happy for his friend’s excitement, but puzzled."

    call sna_main("Haven’t you ever thought of that before?","snape_05")

    nar "Snape asked."

    m "Well, no..."

    nar "Said Genie, and if ageless beings could blush, one would assume that’s what Genie would be doing."

    m "It’s not something that ever came up."

    call sna_main("No one suggested it to you?","snape_01")

    nar "Snape asked, hoping to skip past Genie’s discomfort."

    m "Surprisingly, when given three opportunities at your fondest dreams, helping others doesn’t seem to come up very often."

    nar "Genie said with a sarcastic edge that relieved Snape."

    call sna_main("Well, then...","snape_01")

    nar "Snape said."

    call sna_main("After we find a way to get you back to your home, maybe I could come visit you and we could work something out.","snape_28")

    nar "Genie eyed him curiously and then, with a bit of his usual humor asked,"

    g9 "Are you sure you could resist the urge to use all three on yourself?"

    nar "Snape chuckled. He momentarily considered how rarely he chuckled."
    nar "Not with humor, at least. He hadn’t really done that since..."

    call sna_main("Yes","snape_28")

    nar "Snape said with sudden certainty."

    call sna_main("There is really only one wish I would really want.","snape_23")

    nar "Genie raised an eyebrow at that, but let it stand."

    m "What would be your wish, my friend?"

    nar "He asked Snape kindly."

    call sna_main("I wish I could go back and have wooed Lily for my own","snape_23")

    nar "Snape said dreamily. In his mind’s eye, he remembered the flaming red hair that lit a fire in his own heart."

    call sna_main("I sometimes wonder if that would have made all the difference.","snape_29")

    nar "Snape mused."

    call sna_main("If I would have been a better, a kinder man than I am today.","snape_06")

    g9 "But would you have been as popular?"

    nar "Genie asked."

    g10 "you were central in every book and movie. Everyone loves you."

    call sna_main("What?","snape_05")

    nar "Snape snapped from his reverie. He looked at Genie in confusion."

    m "I mean, would you have been as powerful."

    nar "Genie said hastily."

    m "Wasn’t that rejection what drove you to your studies and your mastery?"

    nar "Snape eyed Genie suspiciously, but let the matter pass."

    call sna_main("Yes, but I would sacrifice all that to be rid of this loneliness.","snape_06")

    nar "Snape returned to his imaginings."

    m "Well, even if you didn’t stay together,"

    nar "Genie said mischievously,"

    m "you could at least have had a little fun with her. Maybe even take her on her wedding night."

    nar "Snape’s head snapped up angrily. How dare Genie sully the memory of Lily."
    nar "But then, a wicked thought entered his head."

    call sna_main("Hmm, what if the boy wasn’t really James’ after all?","snape_02")

    nar "Snape said, and the smile that formed on his face could have frozen the dancing fire beside them."

    call sna_main("Then, one day, I could reach out to that insipid boy, with his foolish fantasies about Potter and say, ‘Harry, I am your father!’","snape_28")

    nar "Genie nodded."

    g9 "It could work. You’ve got the black robes already. You just need the helmet."

    nar "Snape cocked an eyebrow in confusion. The flames leapt and danced and Genie flickered once again."

    g9 "No mind pay you."

    nar "Genie said."

    g9 "Darkness that path, take you it will."

    call sna_main("Um?","snape_29")

    nar "Snape stammered."

    m "What?"

    nar "Genie asked."

    call sna_main("For a moment there, I thought you...","snape_01")

    nar "Snape trailed off, reluctant to go on."

    m "You thought I what?"

    nar "Genie prodded."

    m "Out with it man!"

    call sna_main("I thought you looked all shrunken, like a deformed house elf.","snape_06")

    nar "Snape finally managed to say."
    nar "Genie laughed."

    m "Muppet?"

    call sna_main("No thanks, I’ll just have the wine,","snape_05")

    nar "Snape replied."

    m "I’m afraid that’s the last of it."

    nar "Genie said, looking mournfully at the bottle."
    nar "He eyed Snape through the red droppings of wine still remaining in his glass. It looked like Snape was bleeding."
    nar "The image disturbed him and he put his glass down."

    m "So..."

    nar "Genie coughed once, cleared his throat and continued."

    m "Did you mean it?"

    call sna_main("About the wishes?","snape_05")

    nar "Snape asked."

    m "Yes."

    nar "Genie said, unable to keep the excitement from his voice."

    m "Would you really come to my world and set me free with a wish."

    call sna_main("Why not?","snape_06")

    nar "Snape said."

    call sna_main("Assuming we can find a way to send you back.","snape_09")

    m "Right."

    nar "Genie said, sobering up."

    m "There’s that."

    nar "Snape looked at his friend and sensed his growing gloom."

    call sna_main("Cheer up, Genie.","snape_23")

    nar "He said, clapping the image of his old wizard master on the shoulder."

    call sna_main("We just need to be careful. We don’t want to make a mistake and send you somewhere crazy.","snape_05")

    m "Like a space station?"

    nar "Genie asked, his humor returning with his hope."

    call sna_main("Exactly.","snape_28")

    nar "Snape replied."
    nar "Not sure what a ‘space station’ was."

    call sna_main("We don’t want you to end up far, far away.","snape_24")

    m "In the final frontier?"

    nar "Genie asked, with a wink that to Snape always meant some kind of inside joke Snape never understood."
    nar "He decided to ignore it as he had many other times."

    call sna_main("Let me continue to research why your powers of transdimensional travel are muted here and we’ll find a way to fix your problem.","snape_05")

    m "Both our problems."

    nar "Genie suggested and this time, both of them laughed together."

    call sna_main("You know, Genie, this could be the start of a beautiful friendship.","snape_23")

    nar "Snape said, standing to leave."
    hide screen snape_main
    with d3

    m "Well, you know what the game devs say."

    nar "Genie replied, causing the dark man to pause and look back quizzically."

    m "Play it again, Snape."

    "The End"

    $ daytime = temp_time
    call room(hide_screens=True)
    $ fire_in_fireplace = False
    hide screen fireplace_fire
    hide screen with_snape_animated

    call update_snape
    jump enter_room_of_req

label forgotten_lets_have_sex:
    call hide_room_req
    show screen main_room
    show screen fireplace_fire
    show screen genie
    call blkfade
    call hide_blkfade

    hide screen hermione_main
    with d3

    call reset_menu_position
    $ genie_sprite_base = "characters/genie/base_4.png"
    $ genie_sprite_xpos = 550
    $ genie_sprite_ypos = 0
    $ gen_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ g_c_u_pic = "sex_ani"

    call bld
    call her_chibi("stand","desk")
    m "[hermione_name]..."
    m "I have a favour to ask of you..."
    call her_main("Is it sex? {size=-2}Please let it be sex...{/size}","smile","baseL")
    m "You certainly seem eager."
    call her_main(".......","base","glance")
    call her_main("Well I may have made some plans...","base","down")
    her "but I can't tell you what..."
    m "well as long as you bend over my desk I don't really care..."
    call her_main("{image=textheart}{image=textheart}{image=textheart}","base","down")
    stop music fadeout 1.0
    hide screen hermione_main
    call blkfade
    # SEX

    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide") #HERMIONE
    hide screen genie

    $ gen_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ g_c_u_pic = "sex_ani"
    show screen chair_left
    show screen g_c_u

    call her_chibi("hide")
    hide screen blktone
    hide screen bld1
    hide screen blkfade
    with fade
    call ctc

    call play_music("playful_tension") # SEX THEME.
    show screen bld1
    with d3

    call her_head("Ah...{image=textheart}","open","worriedCl")
    m "Your pussy feels drenched today..."
    call her_head("Does it...{image=textheart} ah...{image=textheart}","open","worriedCl")
    call her_head("That's all because of you [genie_name]...{image=textheart}","shock","worriedCl")

    if daytime:
        call her_head("I've been... looking forward to this all morning...{image=textheart}","silly","ahegao")
    else:
        call her_head("I've been... looking forward to this all day...{image=textheart}","silly","ahegao")

    g4 "Agh, you whore!"
    call her_head("Ah...{image=textheart}{image=textheart}","silly","ahegao")
    m "Yes! Do you like it when I fuck you like this?"
    call her_head("Yes, [genie_name]...","base","glance")

    call play_sound("knocking")
    call nar(">You hear a knock at the door.")

    menu:
        "\"Who is it?\"":
            m "(Who would be knocking at a time like this?)"
            lun "It's Luna Lovegood sir."
            m "{size=-3}Who's that again, [hermione_name]?{/size}"
            call her_head("the crazy blonde... ah...{image=textheart}... with the nice breasts...","open","closed")
            m "Come in!"
        "-Tell them to go away.-":
            m "Go aw-!"
            call her_head("no [genie_name]... let them in...","open","worriedCl")
            m "You want to get caught?!"
            call her_head("Ah...{image=textheart} yes...{image=textheart}","shock","worriedCl")
            m "You are a such a little whore, [hermione_name]!"
            call her_head("Ah-ah...{image=textheart} let them in... please...","shock","worriedCl")
            m "You asked for it!"
            call her_head("Ah-a...{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl")
            m "Come in!"

    ">The door opens as Luna Lovegood walks in."
    call play_sound("door") #Sound of a door opening.
    $ luna_chibi("stand", 540, 250)
    call luna_main("Hello Professor!", "seductive", "default", "raised", "smile_large")
    hide screen luna
    #Stop sex
    m "....."
    call her_head("......","shock","worriedCl")

    call luna_main("I wanted to talk to you about the school uniform.", "wink", "default", "default", "talk")
    hide screen luna
    m "The uniform?"
    call luna_main("Yes, I have a few ideas about some necessary changes and I'd like for you to listen.", "closed", "default", "default", "pout")
    hide screen luna
    m "{size=-3}What's going on here, [hermione_name]?{/size}"

    call her_head("I may have given her a suggestibility serum...","silly","ahegao")
    m "{size=-3}A suggestibility serum?{/size}"
    call luna_main("Who are you talking to sir?", "wide", "default", "default", "smile_large")
    hide screen luna
    m "Oh, um.... no one, just ignore me..."
    call luna_main("Ok then, I'll ignore you...", "default", "empty", "default", "default")
    hide screen luna
    call her_head("I may have suggested that she come here...","silly","ahegao")
    call her_head("And that she be unable to see me...","silly","ahegao")
    call luna_main("As I was saying sir, the school uniform simply cannot stay as it is.", "closed", "default", "default", "pout")
    hide screen luna

    show screen blktone
    with d3
    ">You pick up the pace some more."
    $ g_c_u_pic = "sex2_ani"
    ">The room fills up with rhythmical sound of a flesh hitting flesh..."
    call her_head("Ah... ah... ah...","angry","down_raised")
    m "{size=-3}So let me get this straight.{/size}"
    m "{size=-3}You drugged your class mate...{/size}"
    m "{size=-3}Just so she would come in here and watch you have sex with your headmaster.{/size}"
    call her_head("Ah... yes...{image=textheart}{image=textheart}{image=textheart}")
    call luna_main("The girls uniform is far too conservative!", "mad", "default", "mad", "pout")
    hide screen luna
    m "conservative?"
    call luna_main("Indeed! Ms Granger is the only student that is dressing appropriately.", "default", "default", "sad", "talk")
    hide screen luna
    call her_head("ah...","silly","worried",cheeks="blush",tears="soft")
    m "{size=-3}What else did you do to her?{/size}"
    call her_head("I may have told her to... ah...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
    call her_head("act like the biggest slut she knows...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
    m "{size=-3}So you then?{/size}"
    call her_head("yessss...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
    call luna_main("Sir please, pay attention.", "doubtful", "down", "mad", "upset")
    m "Sorry Miss Lovegood, go on."
    call luna_main("Thank you. As I was saying, I think you need to enact several new policies regarding the girls school uniform.", "wink", "default", "default", "talk")
    call luna_main("Everyone should strive to achieve the same level of perfection as Miss granger.", "closed", "default", "default", "grin")
    hide screen luna
    call her_head("{image=textheart}","silly","worried",cheeks="blush",tears="soft")
    call luna_main("I've come up with several rules that will help with this and I'd like you to enforce them.", "closed_happy", "default", "default", "smile_large")
    m "alright..."
    call luna_main("rule number one: shirts must reveal a minimum of 3 inches of cleavage.", "default", "default", "default", "talk")
    hide screen luna
    call her_head("{image=textheart}","silly","worried",cheeks="blush",tears="soft")
    call luna_main("Rule number two: No skirt over 5 inches in length my be worn.", "wink", "default", "default", "smile_large")
    hide screen luna
    call her_head("{image=textheart}{image=textheart}", "silly", "worried", cheeks="blush", tears="soft")
    call luna_main("rule number three: No bras to be worn at anytime.", "closed", "default", "default", "open")
    hide screen luna
    call her_head("{image=textheart}{image=textheart}{image=textheart}", "silly", "worried", cheeks="blush", tears="soft")
    call luna_main("And finally, rule number four: No panties to be worn at anytime.", "mad", "default", "mad", "pout")
    hide screen luna
    call her_head ("{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}", "silly", "worried",cheeks="blush",tears="soft")

    m "Why are your legs shaking, [hermione_name]?"
    m "Are you cumming? In front of your classmate?"
    call her_head("Yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","dead")
    m "Well, I think I will follow your example then."
    call her_head("..............","silly","dead")
    call nar(">You start fucking Hermione with renewed determination!")
    call her_head("Ah! No! I can't...{image=textheart} not in front of...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","shock","baseL",cheeks="blush",tears="soft")
    m "Shut it whore!"
    call luna_main("Yes sir.", "default", "empty", "default", "default")
    g4 "Argh!"
    with hpunch
    g4 "{size=+7}Argh!!!{/size}"
    call cum_block
    g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
    $ g_c_u_pic = "sex_cum_out_ani"
    call cum_block
    call ctc

    $ uni_sperm = True
    $ u_sperm = "characters/hermione/face/auto_08.png"
    hide screen luna
    call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
    g4 "{size=+5}You whore! Take this!{/size}"
    call luna_main ("take what?", "default", "empty", "default", "open")
    hide screen luna
    call her_head("{size=+5}!!!{/size}","silly","worried",cheeks="blush",tears="soft")
    hide screen bld1
    with d3
    call ctc


    $ g_c_u_pic = "sex_cum_out_blink_ani"
    m "Well, that was pretty great..."
    call her_head("Ah...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
    m "You alright there, slut?"
    call her_head("Yes... I...","silly","dead")
    m "Didn't you enjoy this?"
    call her_head("....I think so...","grin","dead")
    call ctc

    call blkfade
    call her_head("I think I came several times, [genie_name]...","soft","ahegao")
    m "Well that'll do for now. You two best head to class."
    call her_head("yes sir...","grin","dead")
    call her_head("Come on Luna let's go.","grin","dead")
    call luna_main("Hermione! When did you get here?", "wide", "right", "default", "pout")
    call luna_main("And what are you covered in?", "default", "down", "default", "talk")
    call her_head("It doesn't matter...","soft","ahegao")
    call her_head("{size=-7}You can lick it off later...{/size}","soft","ahegao")
    hide screen luna

    $ face_on_cg = True
    call h_update_hair

    hide screen ccg
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    if not daytime:
        show screen candlefire

    call her_chibi("stand","desk","base")
    call gen_chibi("hide")
    show screen genie
    pause.1
    hide screen blktone
    hide screen bld1
    call hide_blkfade
    pause.5

    call bld
    stop music fadeout 4.0

    $ hg_pf_sex_OBJ.points += 1

    hide screen luna
    hide screen luna_chibi
    call her_chibi("leave")
    hide screen main_room
    $ uni_sperm = False
    hide screen hermione_main
    hide screen fireplace_fire
    hide screen candlefire
    jump enter_room_of_req
