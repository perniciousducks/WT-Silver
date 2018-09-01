#Regex find h\s+"([ -}]+)"
#Regex replace (call her_main\( "\1", "base", "base" \))

label a_bad_time_to_disrobe:
    call h_equip_temp_outfit(hg_standart_school_OBJ)
    menu:
        "Part 1":
            jump a_bad_time_to_disrobe_part_1
        "Part 2":
            jump a_bad_time_to_disrobe_part_2
    
label a_bad_time_to_disrobe_part_1:
    call hide_room_req
    show screen main_room
    show screen genie
    show screen blkfade
        
    nar "In this story the genie has found an invisibility cloak."
    nar "And with the cloak comes great oportunities"
    nar "Title: A bad time to disrobe."
    
    hide screen blkfade
    with d3
    call her_chibi("stand", "desk")
    m "Miss Granger. Have you ever been excited about the thought of being caught?"
    
    call her_main( "Caught?", "base", "base" ) 
    call her_main( "In what way professor?", "base", "base" )
    
    m "Well, for today's favour I have a prop for you to use."
    
    call her_main( "A prop sir?", "base", "base" )

    m "Yes, I'd like you to put this invisibility cloak on and sneak into one of the boy only areas of the school."
    
    call her_main( "Well, I guess that would be fine...", "base", "base" )
    call her_main( "Seems a bit different than your usual requests.", "base", "base" )

    m "You'd be naked of course."
    
    call her_main( "Naked!?! But what if someone saw me?", "open", "wide" )
    
    m "You'll be wearing the cloak..."
    m "No one would even know you were there."
    
    call her_main( "{size=7}35 points...{/size}", "annoyed", "angryCl" )
    
    m "25 points you said? sounds good to me." 

    call her_walk("desk","door", 2)
    call her_main( "{size=7}You heard what I said...{/size}", "annoyed", "closed" ) 
    call her_chibi("leave")
    
    g9 "\"Some of that bartering skill put to good use...\""  

    
    show screen day_to_night
    with d3
    hide screen main_room
    hide screen genie
    nar "Later that evening. Hermione returns."
    $ temp_time = daytime
    $ daytime = False
    show screen main_room
    show screen genie
    hide screen day_to_night
    with d3
    
    g9 "I'll take that cloak back if you don't mind."
    
    call her_main( "Certainly.", "base", "base" )
    
    m "Now, spill the beans."
    
    call her_main( "I..I don't have any beans on me sir.", "soft", "narrow" )
    
    m "\"Is this girl for real?\""

    m "It's just an expression, tell me... did you complete your assignment?"
    
    call her_main( "I did sir. I snuck into the boys dormitory using the cloak as you suggested.", "soft", "happyCl" )
    
    m "Naked?"
    
    call her_main( "Naked..ish", "disgust", "baseL" )
    
    m "How can you be naked...ish?"
    
    call her_main( "Well, I had my underwear on, I'd be cold otherwise", "base", "base" )
    
    m "Cold? You'd have the cloak on you..."
    m "What happened next then?"
    
    call her_main( "Well, a few of the boys were in there.", "base", "base" )
    call her_main( "They were playing wizards chess...", "base", "base" )
    call her_main( "Pretty poorly in fact.", "disgust", "wink" ) 

    m "..."
    m "I'm sorry miss Granger but you're going to have to do better than this." 
    m "I expect better from you by now."
    
    call her_main( "So, no points then?", "angry", "angry" )
    
    m "No, I know you can do better."
    
    call her_main( "Fine! I'll do better next time. Double points! I'll show you!", "angry", "angryL" )
    
    m "That's the spirit. Your house will thank you when you beat the Slytherins by the end of the year."

    call her_main( "Thank you professor... I'll remember that for next time", "grin", "happy" ) 

    show screen blkfade
    with d3
    hide screen main_room
    hide screen genie
    show screen quistion_pop_up("Hermione will remember that")
    nar "Hermione returns the next morning, looking nervous but more determined than yesterday."
    $ daytime = True
    show screen main_room
    show screen genie
    hide screen quistion_pop_up
    hide screen hermione_main
    hide screen blkfade
    with d3
    
    
    call her_chibi("stand", "desk", "base")
    call her_main( "I see that you have the cloak ready for me sir.", "base", "baseL" )
    
    m "Indeed, I'm expecting better from you today girl."
    
    call her_main( "I won't disappoint you sir!", "grin", "base" )
    
    m "I'll be the judge of that..."

    hide screen main_room
    hide screen genie
    hide screen hermione_main
    show screen day_to_night
    with d3
    nar "Later that evening a distraught looking Hermione enters the office. "
    $ daytime = False
    show screen main_room
    show screen genie
    call her_chibi("top_naked", "desk", "base")
    call h_equip_temp_outfit(hg_standart_school_noshirt_OBJ)
    hide screen day_to_night
    with d3

    call her_main( "...", "upset", "base", tears="mascara_soft")
    
    m "What happened? Where's your shirt?"
    
    call her_main( "What does it look like?", "upset", "base", tears="mascara_soft" ) 
    
    m "Well, I know what it looks like..." 
    
    call her_main( "I didn't want to disappoint, sir, so I did what you asked...", "soft", "base", tears="mascara_soft" )
    call her_main( "I went into the girls changing room at the quidditch pitch and put my clothes in one of the lockers.", "base", "base", tears="mascara_soft" )

    m "Well done. And then?"
    
    call her_main( "I took the cloak and snuck into the boys changing room...", "base", "base", tears="mascara" )
    call her_main( "I stood next to the doorway so that they wouldn't bump into me.", "base", "base", tears="mascara" )
    
    m "Great idea... and no one noticed?" 
    
    call her_main( "Well, at first... This damn cloak is too small.", "angry", "base", tears="mascara" )
    call her_main( "I thought I would be short enough to fit under it...", "base", "base", tears="mascara" ) 
    call her_main( "I didn't notice that my feet were visible...", "upset", "angry", tears="mascara" )
    
    m "\"Well, that's a shame.\""

    call her_main( "One of the boys saw me shuffle and moved to see what it was so I tried to get away but I slipped...and...and.", "upset", "shocked_raised", tears="mascara" )
    
    g11 "And what?" 
    
    call her_main( "And I slipped and my butt fell out!", "scream", "surprised", tears="mascara" )
    
    g9 "{size=18}30 POINTS TO....{/size}" 
    
    call her_main( "I'm not done!", "open", "down", tears="mascara" )
    
    m "Sorry, you carry on my dear!"

    call her_main( "I ran out and grabbed what I could of my clothes... I think the boy may have seen me.", "soft", "concerned", tears="mascara" ) 
    call her_main( "Professor.... I'm beginning to have second thoughts about this cloak idea." , "soft", "concerned", tears="mascara" )
    
    m "The boy didn't see your face, that's what matters."
    m "You could've draped the cloak around your head and it would be enough."
    
    call her_main( "Professor!", "shock", "wide_stare", tears="mascara" )

    m "Just trying to lighten the mood." 
    m "Here's an extra 5 points for a Job well done, miss Granger."
    g9 "35 points to Gryffindor!"
    
    call her_main( "Thank you professor....", "grin", "base", tears="mascara" ) 
    call her_walk ("desk", "door", 2)
    call her_main( "\"He's right, they wouldn't recognize me if I didn't show my face...\"", "base", "base", cheeks="blush", tears="mascara" )
    call her_main( "\"would they?\"", "base", "base", cheeks="blush", tears="mascara" )
    call her_chibi("leave")
    "The End."
    
    hide screen genie
    hide screen main_room
    hide screen hermione_main
    call reset_hermione_main
    call h_unequip_temp_outfit
    jump enter_room_of_req
    
label a_bad_time_to_disrobe_part_2:
    show screen blkfade
    $ temp_time = daytime
    $ daytime = True
    call play_standart_theme
    call hide_room_req
    show screen main_room
    show screen genie   
    call her_chibi("stand", "desk")
    hide screen blkfade
    with d3    
    
    m "Good afternoon miss Granger."
    call her_main( "Good afternoon professor, what can I do for you today?", "base", "base" )
    m "Glad you asked, I've got another task for you."
    call her_main( "And what task may that be professor.", "soft", "baseL" ) 
    m "Well miss Granger, I think somebody owes me a invisibility cloak."
    call her_main( "Oh, do you want me to collect it from somebody?", "open", "base" )
    m "That somebody is you miss Granger..."
    m "You left my cloak at the scene of the crime."
    call her_main( "What crime professor, what have you gotten me into?", "upset", "annoyed" ) 
    m "I'm talking about when you went to visit the boys changing room."
    m "Or have you forgotten already?"
    call her_main( "{size=7}I've tried to.{/size}", "upset", "worriedL" )
    m "Sorry?"
    call her_main( "I said, I do remember.", "normal", "baseL" )
    m "Right, well. Good invisibility cloaks are pretty hard to come by..."
    m "\"I think...\""
    call her_main( "No they're not... they're mass produced as far as I know.", "annoyed", "base" )
    call her_main( "By house elves I bet...", "disgust", "angryCl" )
    m "Hey now, I know they might be small but I wouldn't call them elves."
    m "In any case, the cloak has more of a sentimental value to me... lots of memories."
    g9 "\"Like the time where your butt fell out of it.\""
    g9 "Oh, the memories... you must retrieve it for me." 
    call her_main( "Fine, I'll do it... even though I hold you partly responsible for the situation that lead to me dropping it.", "annoyed", "angryCl" )
    m "Great, let's not dwell on the past then."
    call her_main( "...", "normal", "annoyed" )
    call her_main( "Do you happen to have any idea of where it is?", "open", "base" )
    m "Well, it hasn't been reported as found so unless someone stole it there's only one place it could be."
    call her_main( "The boys changing room?", "base", "down" )
    g9 "The boys changing room."
    call her_main( "And how many house points?", "base", "base" )
    m "For what exactly?"
    call her_main( "Retrieving the cloak of course.", "annoyed", "base" )
    m "You're demanding house points, for your own mistakes miss Granger?"
    call her_main( "But I thought...", "upset", "worried" )
    m "..."
    call her_main( "...", "upset", "down" )
    m "Fine, but only if we continue where we left of."
    call her_main( "With my butt out?!?", "disgust", "surprised" )
    m "With your bu..."
    m "No, well... yes, but this time you'll be prepared."
    call her_main( "But... what if they recognize me sir?", "open", "worried" )
    m "You'd already know if they had recognized you..."
    call her_main( "\"That's true...\"", "soft", "soft", cheeks="blush" ) 
    call her_main( "And then what, you want me to just walk away?", "base", "base", cheeks="blush" )
    m "You can figure it out yourself miss Granger. Once you have the cloak it shouldn't be an issue getting away."
    call her_main( "And I want...", "open", "base" )
    m "I'll give you 40 house points for it."
    call her_main( "\"I was going to ask for 30.\"", "soft", "squintL", cheeks="blush" )
    call her_main( "I'll do it...", "base", "base" )
    g9 "Great, you're doing a great service to your house and making an old man very happy."
    call her_main( "By getting your cloak back right?", "base", "worried" )
    m "Right..."
    call her_walk("desk","door", 2)
    call her_chibi("leave")

    show screen day_to_night
    with d3
    hide screen main_room
    hide screen genie
    nar "Later that evening"
    $ temp_time = daytime
    $ daytime = False
    call play_standart_theme
    show screen main_room
    show screen genie
    call h_unequip_temp_outfit()
    call h_action("covering_uniform")
    hide screen day_to_night
    with d3
    
    

    call her_main( "...", "normal", "dead", cheeks="blush" )
    m "Mission success?"
    call her_main( "...", "normal", "dead", cheeks="blush" )
    m "Miss Granger?"
    call her_main( "Oh, hello professor, yes. Here's your cloak back.", "base", "down" )
    m "..."
    m "And?"
    call her_main( "And what?", "normal", "worriedCl" )
    m "And what about your assignment. How did it go?"
    call her_main( "Oh... yes, it went very well thank you... no hurdles in any way.", "soft", "worriedL", cheeks="blush")
    m "Your face is glowing miss Granger, I can tell when you're being untruthful."
    call her_main( "It is? I didn't even notice...", "normal", "down_raised", cheeks="blush" ) 
    m "You're going to have to elaborate if you'd like those house points."
    call her_main( "Oh... okay, I'l just go ahead then...", "mad", "base" )
    m "Let me get the popcorn."
    call her_main( "popcorn? Where would you get popcorn from in this office?", "annoyed", "base")
    g9 "Magic cupboard."
    call her_main( "Right... well, I'll just start in that case shall I?", "base", "glanceL" )
    call her_main( "...", "base", "base", cheeks="blush")
    call her_main( "So... I went to the boys changing room when they were in quidditch practice.", "open", "down" )
    m "*CRUNCH*"
    call her_main( "It's very messy in there... I thought the girls changing room was bad...", "base", "down_raised" )
    m "*CRUNCH* *Chew* *Chew*"
    m "*CRUNCH*"
    call her_main( "Anyway... so I rumaged around in that mess...", "annoyed", "worried" ) 
    call her_main( "I knew it had to have been somewhere between the showers and the doorway...", "base", "base" )
    call her_main( "After looking around for a while I noticed that the cloak had been pushed under one of the benches lining the wall.", "open", "down" )
    call her_main( "So I grabbed it and I thought I might as well disrobe and hide in the shower room with the cloak on.", "base", "down_raised" )
    call her_main( "But as I was stuffing my clothes in one of the lockers a boy walked in.", "clench", "worried")
    m "*CRUNCH*"
    call her_main( "Professor!", "scream", "angry" )
    g4 "*Cough* *Cough*... sorry."
    call her_main( "It is hard to talk about this as it is without your chewing distracting me.", "annoyed", "angry" )
    call her_main( "Anyhow...", "base", "angryL" )
    call her_main( "I expected the team to be going for at least another 30 minutes.", "open", "base" )
    call her_main( "But that's when the boy walked in...", "normal", "closed" )
    call her_main( "And I panicked and threw the cloak over myself and hid in one of the toilets.", "open", "worriedL")
    m "Smart."
    call her_main( "...", "base", "base", cheeks="blush" )
    call her_main( "Well, it would've been if I had remembered to lock it.", "base", "down_raised" )
    g9 "Not that smart..."
    call her_main( "Do you want me to continue or not?", "annoyed", "annoyed" )
    m "You're the one receiving the points here, I'm just providing the means of earning them."
    call her_main( "...", "normal", "down" ) 
    call her_main( "As I was saying...", "base", "down_raised" )
    call her_main( "I went into one of the toilets and I heard the boy shuffling outside.", "base", "closed" )
    call her_main( "The room was so small so I tried to back into a corner, but as he came in I knew it wasn't going to work...", "base", "down_raised", cheeks="blush")
    call her_main( "So I prayed he wasn't about to sit down and instead I positioned myself above the toilet with my legs around the base.", "clench", "worriedCl" )
    m "And did he sit down or not?"
    call her_main( "No, but he was close enough for me to feel his...", "mad", "ahegao_squint" )
    call her_main( "His...", "base", "ahegao_intense" )
    m "His what? miss Granger..."
    call her_main( "Well... His Penis brushed up against my butt.", "annoyed", "closed", cheeks="blush" )
    m "How did he manage that?"
    call her_main( "The boy wasn't in there to relieve himself in the way I assumed...", "open", "angryCl", cheeks="blush" )
    call her_main( "I guess he wasn't paying attention to what sensation he was feeling on the tip of his...", "normal", "worried", cheeks="blush")
    call her_main( "Anyway...", "open", "worriedL", cheeks="blush" )
    m "..."
    call her_main( "I'd like my points now.", "base", "down")
    m "Certainly miss Granger..."
    m "40 points to Gryffindor!"
    call her_main( "Thank you professor...", "soft", "soft" ) 
    
    call her_walk("desk","door", 2)
    
    call her_main( "\"I'm glad I had time to clean the cloak before walking in here...\"", "base", "dead", cheeks="blush" )
    call her_main( "\"That thing was massive...\"", "normal", "down" )
    call her_main( "\"What am I thinking? snap out of it...\"", "base", "worriedCl", cheeks="blush" ) 

    call her_chibi("leave")

    "The end"
    
    hide screen genie
    hide screen main_room
    hide screen hermione_main
    $ daytime = temp_time
    call play_standart_theme
    call reset_hermione_main
    call h_action("none")
    jump enter_room_of_req
 
label whose_points:
    call hide_room_req
    show screen whose_points_screen
    show screen blkfade
    pause 0.3
    hide screen blkfade
    with d3
    
    
    m "Hello and welcome to whose points is it anyway."
    m "The show where everything is made up but the points don't matter."
    m "Just like at Hogwarts."
    
    call her_main("\"I hope I win! I need those housepoints.\"", "base","squintL",xpos="left")
    
    m "First, let me introduce todays contestants."
    m "The curly haired harlot we all know and love. Give it up for Hermione."
    
    call her_main("...", "grin","worried",cheeks="blush", xpos="left")
    
    m "The ravishing ravenclaw who'll rock your socks off. Luna! "
    call luna_main("heh...hello.", "wink", "default", "default", "default")

    m "And the small girl with a big personality. Astoria!"
    call ast_main( "Hey!","scream" ,"angry" ,"angry" ,"angry", xpos="right" ) 
 
    m "Today we're playing scenes from a hat."
    hide screen hermione_main
    hide screen luna
    hide screen astoria_main
    
    hat "Stay the fuck away from me."
    
    m "But the notes are already inside you. I put them there last night."
    
    hat "You put notes inside me without my consent? \n*Spits note out*"
    
    m "Looks like we have our first prompt."
    m "Things you might say in potions class... But also in your bedroom."
    
    call her_main("This cauldron hasn't been used for years. It's all moldy and full of muck!", "grin","worried",cheeks="blush", xpos="right")
    
    hat "Boo, there's no cauldrons in the bedroom!"
    
    m "Quiet now, it was a good euphemism, 10 points to Gryffindor."
    call play_sound("applause01")
    hide screen hermione_main
    
    call ast_main( "Snape, get your gross hands off my shoulders, you creep!","clench" ,"angry" ,"angry" ,"angry" ) 
    
    m "I'm not sure you got the idea of the game there..."
    
    hide screen astoria_main
    call luna_main("Oops. I was supposed to squeeze the mucus out with my hands and not crush it.", "closed", "default", "raised","wide_smile" )
    
    m "Sounds painful... 15 points to Ravenclaw."
    call play_sound("applause01")
    hide screen luna
    
    call her_main("How's that worth more than mine...", "annoyed","worried")
    hide screen hermione_main
    m "Any more? On to the next prompt then. Hat?"
    
    hat "Sorry, what did you cough call me? That's \n\"Sorting\" Hat to you. (coughs out note.)"
    
    g9 "Things you might do in quidditch... but also with your lover..."
    
    call ast_main( "I'm going first this time! I have a good one!", "grin", "base", "base", "mid") 
    
    m "Go on...."
    
    call ast_main( "Madam Hooch! Get your gross hands off my quidditch robes, you creep!" ,"clench", "angry", "angry", "mid") 
    
    m "Again, I don't think you understand the game..."
    
    call ast_main( "Give me the points!" , "scream", "narrow", "narrow", "mid") 
    
    m "Disqualified!"
    
    call ast_main( "Wait, you can do that?" ,"scream" ,"wide", "wide")
    
    g9 "It's my game, I make the rules."
    
    call ast_main( "\"We'll see about that....\"", "upset", "narrow","narrow")
    hide screen astoria_main
    
    call her_main("My turn.")
    call her_main("I love the feeling of a hard wooden object between my legs. \nI tend to tense up during the climax.", "grin", cheeks="blush")
    
    m "A bit direct but I like it. \n15 points to Gryffindor."
    call play_sound("applause01")
    hide screen hermione_main
    
    call luna_main("It's quite exciting but also a bit hard. You need to make sure not to end up with one of the balls in your throat.", "seductive", "default", "raised","grin")
    
    g9 "\"I don't mind having you end up with one of mine in your throat one day\""
    m "20 points to Ravenclaw"
    call play_sound("applause01")
    hide screen luna
    
    call her_main("\"Seems like pleasing the judge is the way to go. Only one round left...\"", "annoyed","worried")
    hide screen hermione_main
    
    call luna_main("...", "default", "default", "default", "wide_smile")
    hide screen luna
    
    m "Last round ladies. You better make it a good one. It's still all to play for."
    m "The last note if you please!"
    
    hat "I'm all out, looks like you only wrote \ntwo after all!"
    
    m "That can't be right...."
    
    call ast_main( "Let me check professor!", "smile", "base", "base", "mid")
    call ast_main( "I found the last note, it was stuck under one of the folds!")
    hide screen astoria_main
    
    hat "Are you calling me fat young lady?"
    
    call ast_main( "I'll read it for you shall I?")

    m "Go ahead."
    
    call ast_main( "Things that you would not share with your classmates... but would share with dumby.")
    hide screen astoria_main
    
    m "\"I don't remember writing that one...\""
    
    call luna_main("I see invisible creatures... but people don't belie... ", "tired", "down", "sad", "talk")
    hide screen luna
    
    call h_action("lift_top") 

     # SEX THEME.
    call play_sound("scratch")
    stop music
    call her_chibi("lift_top","mid","base") 
    call bld 
    call her_main("...", "smile","worried")
    
    
    g9 "500 points to Gryffindor!"
    hide screen hermione_main
    call play_music("playful_tension")
    
    call luna_main("That's cheating, I didnt even get to finish! ", "mad", "default", "angry", "yell")
    hide screen luna
    
    m "Well, that's all for this episode of whose points is it anyway."
    
    call her_main("I win, all the points for me!", "smile","worried")
    hide screen hermione_main
    
    call luna_main("Don't end now! This game is rigged!", "mad", "default", "angry", "yell")
    hide screen luna
    
    m "And remember the points doesn't matter!"
    
    call her_main("Wait, they don't?!? I thought they were house points!", "annoyed","worried")
    hide screen hermione_main
    
    call ast_main( "Harlot! Harlot! Harlot!", "grin", "happyCl", "base", "R")
    
    call luna_main("How do those points taste now? ", "default", "default", "default", "grin")
    call luna_main("The whole wizarding world is going see your tits!", "default", "default", "default", "wide_smile")
    hide screen luna
    hide screen astoria_main
    
    call her_main("Oh no, I forgot about that!", "shock","worried", tears="crying")
    
    g9 "Good night!"
    call play_sound("applause01")
    
    "To be continued?"
    
    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")
    
    hide screen whose_points_screen
    call h_action() 
    call her_chibi(action="hide")
    hide screen hermione_main
    jump enter_room_of_req
    
label genie_house_elf:
    call hide_room_req
    show screen main_room
    show screen genie
    
    show screen blkfade
    pause 0.3
    hide screen blkfade
    with d3
    
    nar "This story takes place in between the introduction of Snape and first meeting Hermione."
    nar "The genie, the desk and the door:"
    nar "How does that door work? The genie thought."

    m "\"How do the people know I’ve summoned them? I don’t have a secretary...that I know of anyway.\""

    m "Have they been keeping a secretary from me? I should ask Sn..."
    
    nar "Snape then opened the door, his pointy nose protruding under his silky hair."

    call sna_walk("door","mid",2) 
    call sna_main("You called? ", "snape_23", xpos="base", ypos="base")

    nar "Snape said with a smirk, doing his best to hide his amusement."
    
    g11 "How did you, how do you..."
    m "This door, how does it work?"
    
    nar " The genie said, now even more frustrated. "
    nar "The genie wasn’t used to this... this unfamiliar magic."
    nar "He was used to knowing the ins and outs of the universe. But this world, it was to alien to him..."
    nar "At least he knew things about aliens..."

    call sna_main("Well, you’re the headmaster are you not? ", "snape_06", xpos="base", ypos="base")

    nar "Snape said as if that meant anything."

    nar "A look of confusion spread across the genies face which only made Snape smirk even more."
    nar "He then composed himself after seeing this unusual expression on the headmasters face."

    call sna_main("I keep forgetting that you don’t know these things.", "snape_01", xpos="base", ypos="base")
    call sna_main("students learn it on day one.", "snape_01", xpos="base", ypos="base")
    call sna_main("The headmaster is in control of the school and its inhabitants.", "snape_24", xpos="base", ypos="base")

    nar "Snape said in a matter of fact sort of way."
    
    m "I know that, we have schools in my world too."
    m "But generally we don’t wave wooden sticks around yelling random words."

    nar "Snape flinched, as if the notion of magic consisting of waving a wand and yelling random words was utterly absurd."
    
    call sna_main("No. You’re literally in control over the school....look.", "snape_08", xpos="base", ypos="base")
    
    nar "Snape says, pulling his wand out, waving it."
    
    call sna_main("Revelio!", "snape_01", xpos="base", ypos="base")
    call sna_main(remove=True)
    
    nar "After a flash of light and a small pop a house elf appears in the corner of the room."
    
    call helf_main(" ")
    
    g5 "What the hell is that?"
    
    nar "The genie said, jumping onto the desk as if things appearing out of thin air was new to him."
    
    call helf_main(remove=True)
    
    call sna_main("That...is a house elf.", "snape_01", xpos="base", ypos="base")
    
    m "A house...elf."
    g10 "Is that like a Santa's elf? "
    
    nar "The genie said, now climbing down to sit on his chair."

    call sna_main("Sort of, they don’t get paid so they do have that in common...", "snape_05", xpos="base", ypos="base")
    
    nar "Snape muttered under his breath..."  
    
    call sna_main("The houses elves here can send us messages so we can go where we're needed.", "snape_05", xpos="base", ypos="base")
    
    call sna_main("He just sits here invisible during the day and cleans and eats at night.", "snape_01", xpos="base", ypos="base")
    
    m "The house elf cleans?"
    m "I thought I had some sort of magic self cleaning desk..."
    
    nar "The genie said sheepishly." 
    call sna_main(remove=True)
    
    call helf_main("No sir...")
    
    nar "Said the elf, trying its hardest to bite his tongue but failing."
    
    call helf_main("I see it all, I clean it all....every...last bit of it.")
    call helf_main(remove=True)
    
    call sna_main("...", "snape_08", xpos="base", ypos="base")
    
    nar "After a few moments Snape turned around, started walking towards the door and said."
    
    call sna_main("If that is all, I’ll be in the dungeons.", "snape_01", xpos="base", ypos="base")
    call sna_main("I’ve been working on a new cleaning solution.", "snape_01", xpos="base", ypos="base")
    call sna_main("It might come in handy sooner than I thought.", "snape_02", xpos="base", ypos="base")
    call sna_walk("mid","leave",2) 
    call sna_main(remove=True)
    
    nar "The door shut and silence spread across the room only interrupted after a few minutes by the house elf."
    
    call helf_main("So, should I turn invisible again sir?")
    
    m "Yes...yes that will be for the best."
    call helf_main(remove=True)
    "The end."
    
    hide screen genie
    hide screen main_room
    jump enter_room_of_req

label a_spaced_out_conversation:
    $ temp_time = daytime
    $ daytime = False
    
    call hide_room_req
    show screen main_room
    show screen fireplace_fire
    show screen with_snape_animated
    call blkfade 
    call hide_blkfade
    
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

    call sna_main( "So, let me try to understand this,", "snape_05" )
    
    nar "Snape said slowly." 
    
    call sna_main( "You live in a little bottle?", "snape_05" )

    nar "The gray figure nodded."

    call sna_main( "How does that work?", "snape_05" )

    m "I believe it’s based on tessaracted space."
    
    nar "Genie said, his tone becoming akin to a professor lecturing a class."
    
    m "The whole process is very Loki."

    nar "Snape didn’t hear the last words as a flicker and shadow from the flames made Genie appear different."
    nar "Almost as if gleaming golden horns arose from his head."

    call sna_main( "Come again?", "snape_03" )
    
    nar "Snape asked, gaping at the sight before it was gone so fast that he was left unsure he had seen anything."

    m "I said, they keep the whole thing low key."
    
    nar "Genie repeated."
    
    m "Keeps most people from knowing how they make it bigger on the inside."

    call sna_main( "Most people?", "snape_05" )
    nar "Snape asked."

    m "Well, Who knows..."
    nar "Genie answered."

    call sna_main( "Do you know?", "snape_24" )
    
    nar "Snape asked."

    m "Who knows."
    
    nar "Genie repeated."

    call sna_main( "So, who knows?", "snape_08" )
    
    nar "Snape asked again, getting a little irritated."
    nar "Patience was not a trait Snape had ever cared to master."

    m "Yes, Who knows!"
    
    nar "Genie said."
    nar "Snape flicked his hands impatiently and just decided to move on"
    nar "Determining when Genie was serious or not was still beyond his ability."
    nar "Plus, there had been another one of those weird flickers and he could have sworn he had seen a multicolor scarf around Genie’s neck."

    call sna_main( "And, you then grant the summoner three wishes?", "snape_01" )
    
    nar "Snape continued."
    
    call sna_main( "Anything they want? You can make anything come true?", "snape_05" )

    m "Those are the rules of my existence, yes."
    
    nar "Genie replied, thinking, not for the first time, how limited his real life was."

    call sna_main( "That seems stupid.", "snape_09" )
    
    nar "Snape said bluntly."
    nar "Genie smiled. Snape was never much for niceties."
    nar "Genie found it refreshing to talk with someone whose disdain for others so matched his own."

    nar "Snape frowned at that smile. He got along almost perfectly with Genie."
    nar "Their lusts and passions were quite similar..."
    nar "It’s just Genie’s sense of humor that made Snape doubt his seriousness sometimes."

    call sna_main("You’ve got the power of a god,", "snape_06" )
    
    nar "Snape pushed forward."
    
    call sna_main("Can’t you just magic yourself free?", "snape_05" )

    m "It doesn’t work that way,"
    
    nar "Genie said sadly." 
    
    g "I can only grant magic to others."

    nar "Snape shook his head."
    
    call sna_main( "It still seems stupid...", "snape_06" )
    call sna_main( "What if I were to visit you in your world and make one of my wishes that you be free to use your magic however you should please?", "snape_09" )

    nar "Genie stared at Snape with something like wonder."
    nar "It takes quite a bit to make an ageless being like Genie gape in awe."

    g5 "That’s…That’s brilliant!"
    
    nar "Genie shouted."
    
    g6 "Great Gods, man, that could actually work!"

    nar "Snape was taken aback by Genie’s enthusiastic shout, but quickly recovered."
    nar "He was happy for his friend’s excitement, but puzzled."

    call sna_main( "Haven’t you ever thought of that before?", "snape_05" )
    
    nar "Snape asked."

    m "Well, no..."
    
    nar "Said Genie, and if ageless beings could blush, one would assume that’s what Genie would be doing."
    
    m "It’s not something that ever came up."

    call sna_main( "No one suggested it to you?", "snape_01" )
    
    nar "Snape asked, hoping to skip past Genie’s discomfort."

    m "Surprisingly, when given three opportunities at your fondest dreams, helping others doesn’t seem to come up very often."
    
    nar "Genie said with a sarcastic edge that relieved Snape."

    call sna_main( "Well, then...", "snape_01" )
    
    nar "Snape said."
    
    call sna_main( "After we find a way to get you back to your home, maybe I could come visit you and we could work something out.", "snape_28" )

    nar "Genie eyed him curiously and then, with a bit of his usual humor asked," 
    
    g9 "Are you sure you could resist the urge to use all three on yourself?"

    nar "Snape chuckled. He momentarily considered how rarely he chuckled." 
    nar "Not with humor, at least. He hadn’t really done that since…"

    call sna_main( "Yes", "snape_28" )
    
    nar "Snape said with sudden certainty." 
    
    call sna_main( "There is really only one wish I would really want.", "snape_23" )

    nar "Genie raised an eyebrow at that, but let it stand."

    m "What would be your wish, my friend?"
    
    nar "He asked Snape kindly."

    call sna_main( "I wish I could go back and have wooed Lily for my own", "snape_23" )
    
    nar "Snape said dreamily. In his mind’s eye, he remembered the flaming red hair that lit a fire in his own heart."

    call sna_main( "I sometimes wonder if that would have made all the difference.", "snape_29" )
    
    nar "Snape mused."
    
    call sna_main( "If I would have been a better, a kinder man than I am today.", "snape_06" )

    g9 "But would you have been as popular?"
    
    nar "Genie asked."
    
    g10 "you were central in every book and movie. Everyone loves you."

    call sna_main( "What?", "snape_05" )
    
    nar "Snape snapped from his reverie. He looked at Genie in confusion."

    m "I mean, would you have been as powerful."
    
    nar "Genie said hastily."
    
    m "Wasn’t that rejection what drove you to your studies and your mastery?"

    nar "Snape eyed Genie suspiciously, but let the matter pass."

    call sna_main( "Yes, but I would sacrifice all that to be rid of this loneliness.", "snape_06" )
    
    nar "Snape returned to his imaginings."

    m "Well, even if you didn’t stay together,"
    
    nar "Genie said mischievously,"
    
    m "you could at least have had a little fun with her. Maybe even take her on her wedding night."

    nar "Snape’s head snapped up angrily. How dare Genie sully the memory of Lily."
    nar "But then, a wicked thought entered his head."

    call sna_main( "Hmm, what if the boy wasn’t really James’ after all?", "snape_02")
    
    nar "Snape said, and the smile that formed on his face could have frozen the dancing fire beside them."

    call sna_main( "Then, one day, I could reach out to that insipid boy, with his foolish fantasies about Potter and say, ‘Harry, I am your father!’", "snape_28" )

    nar "Genie nodded."
    
    g9 "It could work. You’ve got the black robes already. You just need the helmet."

    nar "Snape cocked an eyebrow in confusion. The flames leapt and danced and Genie flickered once again."

    g9 "No mind pay you." 
    
    nar "Genie said."
    
    g9 "Darkness that path, take you it will."

    call sna_main( "Um?", "snape_29" )
    
    nar "Snape stammered."

    m "What?"
    
    nar "Genie asked."

    call sna_main( "For a moment there, I thought you...", "snape_01" ) 
    
    nar "Snape trailed off, reluctant to go on."

    m "You thought I what?"
    
    nar "Genie prodded."
    
    m "Out with it man!"

    call sna_main( "I thought you looked all shrunken, like a deformed house elf.", "snape_06" )
    
    nar "Snape finally managed to say."
    nar "Genie laughed."
    
    m "Muppet?"

    call sna_main( "No thanks, I’ll just have the wine,", "snape_05")
    
    nar "Snape replied."

    m "I’m afraid that’s the last of it."
    
    nar "Genie said, looking mournfully at the bottle."
    nar "He eyed Snape through the red droppings of wine still remaining in his glass. It looked like Snape was bleeding."
    nar "The image disturbed him and he put his glass down."

    m "So..."
    
    nar "Genie coughed once, cleared his throat and continued."
    
    m "Did you mean it?"

    call sna_main( "About the wishes?", "snape_05" )
    
    nar "Snape asked."

    m "Yes."
    
    nar "Genie said, unable to keep the excitement from his voice."
    
    m "Would you really come to my world and set me free with a wish."

    call sna_main( "Why not?", "snape_06" )
    
    nar "Snape said."
    
    call sna_main( "Assuming we can find a way to send you back.", "snape_09" )

    m "Right."
    
    nar "Genie said, sobering up."
    
    m "There’s that."

    nar "Snape looked at his friend and sensed his growing gloom."

    call sna_main( "Cheer up, Genie.", "snape_23" )
    
    nar "He said, clapping the image of his old wizard master on the shoulder."
    
    call sna_main( "We just need to be careful. We don’t want to make a mistake and send you somewhere crazy.", "snape_05" )

    m "Like a space station?"
    
    nar "Genie asked, his humor returning with his hope."

    call sna_main( "Exactly." , "snape_28" )
    
    nar "Snape replied."
    nar "Not sure what a ‘space station’ was." 
    
    call sna_main( "We don’t want you to end up far, far away.", "snape_24" )

    m "In the final frontier?"
    
    nar "Genie asked, with a wink that to Snape always meant some kind of inside joke Snape never understood."
    nar "He decided to ignore it as he had many other times."

    call sna_main( "Let me continue to research why your powers of transdimensional travel are muted here and we’ll find a way to fix your problem.", "snape_05" )

    m "Both our problems." 
    
    nar "Genie suggested and this time, both of them laughed together."

    call sna_main( "You know, Genie, this could be the start of a beautiful friendship.", "snape_23" )
    
    nar "Snape said, standing to leave."
    hide screen snape_main
    with d3
    
    m "Well, you know what the game devs say."
    
    nar "Genie replied, causing the dark man to pause and look back quizzically."

    m "Play it again, Snape."
    
    "The End"
    
    $ daytime = temp_time
    hide screen main_room
    hide screen fireplace_fire
    hide screen with_snape_animated
    jump enter_room_of_req
