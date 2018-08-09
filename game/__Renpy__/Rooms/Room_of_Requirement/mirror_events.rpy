#Regex find h\s+"([ -}]+)"
#Regex replace (call her_main\( "\1", "base", "base" \))

    
    
label a_bad_time_to_disrobe:
    call hide_room_req
    show screen main_room
    show screen genie
    show screen blkfade
    
    n "In this story the genie has found an invisibility cloak."
    n "And with the cloak comes great oportunities"
    n "Title: A bad time to disrobe."
    
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
    n "Later that evening. Hermione returns."
    $ temp_time = daytime
    $ daytime = False
    show screen main_room
    show screen genie
    hide screen day_to_night
    with d3
    
    g9 "I'll take that cloak back if you don't mind."
    
    call her_main( "Certainly.", "base", "base" )
    
    m "Now, spill the beans."
    
    call her_main( "I..I don't have any beans on me sir.", "base", "base" )
    
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
    call her_main( "Pretty badly in fact.", "disgust", "wink" ) 

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
    n "Hermione returns the next morning, looking nervous but more determined than yesterday."
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
    
    call her_main( "I won't dissapoint you sir!", "grin", "base" )
    
    m "I'll be the judge of that..."

    hide screen main_room
    hide screen genie
    hide screen hermione_main
    show screen day_to_night
    with d3
    n "Later that evening a distraught looking Hermione enters the office. "
    $ daytime = False
    show screen main_room
    show screen genie
    hide screen day_to_night
    with d3

    call her_chibi("top_naked", "desk", "base")
    $ hermione_wear_top = False
    $ hermione_breasts_temp = hermione_breasts
    $ hermione_breasts = "characters/hermione/body/breasts/breasts_normal.png"
    #TODO: Remove top
    call her_main( "...", "upset", "base", tears="mascara_soft")
    
    m "What happened? Is there anything wrong?"
    
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

    call her_main( "I think the boy may have seen me.", "soft", "concerned", tears="mascara" ) 
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
    $ hermione_wear_top = True
    $ hermione_breasts = hermione_breasts_temp
    $ daytime = temp_time
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
    
    call her_main("\"I hope I win! I need those housepoints.\"", "base","squintL",xpos="mid")
    
    m "First, let me introduce todays contestants."
    m "The curly haired harlot we all know and love. Give it up for Hermione."
    
    call her_main(" ", "grin","worried",cheeks="blush")
    
    m "Today we're playing scenes from a hat."
    hide screen hermione_main
    
    hat "Stay the fuck away from me."
    
    m "But the notes are already inside you. I put them there last night."
    
    hat "You put notes inside me without my consent? \n*Spits note out*"
    
    m "Looks like we have our first prompt."
    m "Things you might say in potions class... But also in your bedroom."
    
    call her_main("This cauldron hasn't been used for years. It's all moldy and full of muck!", "grin","worried",cheeks="blush")
    
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
    
    call her_main("How's that worth more than my one...", "annoyed","worried")
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
    
    call luna_main(" ", "default", "default", "default", "wide_smile")
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

    call play_music("playful_tension") # SEX THEME.

    call her_chibi("lift_top","mid","base") 
    
    call bld 
    
    g9 "500 points to Gryffindor!"
    call play_sound("applause01")
    
    call luna_main("That's cheating, I didnt even get to finish! ", "mad", "default", "angry", "yell")
    hide screen luna
    
    m "Well, that's all for this episode of whose points is it anyway."
    
    call her_main("I win, all the points for me!", "smile","worried")
    
    call luna_main("Don't end now! This game is rigged!", "mad", "default", "angry", "yell")
    hide screen luna
    
    m "And remember the points doesn't matter!"
    
    call her_main("Wait, they don't?!? I thought they were house points!", "annoyed","worried")
    hide screen hermione_main
    
    call ast_main( "Harlot! Harlot! Harlot!", "grin", "happyCl", "base", "R")
    
    call luna_main("How does those points taste now? ", "default", "default", "default", "grin")
    call luna_main("The whole wizarding world is going see your tits!", "default", "default", "default", "wide_smile")
    hide screen luna
    hide screen astoria_main
    
    call her_main("Oh no, I forgot about that!", "shock","worried", tears="crying")
    
    g9 "Good night!"
    call play_sound("applause01")
    
    "To be continued?"
    
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
    
    n "This story takes place in between the introduction of Snape and first meeting Hermione."
    n "The genie, the desk and the door:"
    n "How does that door work? The genie thought."

    m "\"How do the people know I’ve summoned them? I don’t have a secretary...that I know of anyway.\""

    m "Have they been keeping a secretary from me? I should ask Sn..."
    
    n "Snape then opened the door, his pointy nose protruding under his silky hair."

    call sna_walk("door","mid",2) 
    call sna_main("You called? ", "snape_23", xpos="base", ypos="base")

    n "Snape said with a smirk, doing his best to hide his amusement."
    
    g11 "How did you, how do you..."
    m "This door, how does it work?"
    
    n " The genie said, now even more frustrated. "
    n "The genie wasn’t used to this... this unfamiliar magic."
    n "He was used to knowing the ins and outs of the universe. But this world, it was to alien to him..."
    n "At least he knew things about aliens..."

    call sna_main("Well, you’re the headmaster are you not? ", "snape_06", xpos="base", ypos="base")

    n "Snape said as if that meant anything."

    n "A look of confusion spread across the genies face which only made Snape smirk even more."
    n "He then composed himself after seeing this unusual expression on the headmasters face."

    call sna_main("I keep forgetting that you don’t know these things.", "snape_01", xpos="base", ypos="base")
    call sna_main("students learn it on day one.", "snape_01", xpos="base", ypos="base")
    call sna_main("The headmaster is in control of the school and its inhabitants.", "snape_24", xpos="base", ypos="base")

    n "Snape said in a matter of fact sort of way."
    
    m "I know that, we have schools in my world too."
    m "But generally we don’t wave wooden sticks around yelling random words."

    n "Snape flinched, as if the notion of magic consisting of waving a wand and yelling random words was utterly absurd."
    
    call sna_main("No. You’re literally in control over the school....look.", "snape_08", xpos="base", ypos="base")
    
    n "Snape says, pulling his wand out, waving it."
    
    call sna_main("Revelio!", "snape_01", xpos="base", ypos="base")
    call sna_main(remove=True)
    
    n "After a flash of light and a small pop a house elf appears in the corner of the room."
    
    call helf_main(" ")
    
    g5 "What the hell is that?"
    
    n "The genie said, jumping onto the desk as if things appearing out of thin air was new to him."
    
    call helf_main(remove=True)
    
    call sna_main("That...is a house elf.", "snape_01", xpos="base", ypos="base")
    
    m "A house...elf."
    g10 "Is that like a Santa's elf? "
    
    n "The genie said, now climbing down to sit on his chair."

    call sna_main("Sort of, they don’t get paid so they do have that in common...", "snape_05", xpos="base", ypos="base")
    
    n "Snape muttered under his breath..."  
    
    call sna_main("The houses elves here can send us messages so we can go where we're needed.", "snape_05", xpos="base", ypos="base")
    
    call sna_main("He just sits here invisible during the day and cleans and eats at night.", "snape_01", xpos="base", ypos="base")
    
    m "The house elf cleans?"
    m "I thought I had some sort of magic self cleaning desk..."
    
    n "The genie said sheepishly." 
    call sna_main(remove=True)
    
    call helf_main("No sir...")
    
    n "Said the elf, trying his hardest to bite his tongue but failing."
    
    call helf_main("I see it all, I clean it all....every...last bit of it.")
    call helf_main(remove=True)
    
    call sna_main("...", "snape_08", xpos="base", ypos="base")
    
    n "After a few moments Snape turned around, started walking towards the door and said."
    
    call sna_main("If that is all, I’ll be in the dungeons.", "snape_01", xpos="base", ypos="base")
    call sna_main("I’ve been working on a new cleaning solution.", "snape_01", xpos="base", ypos="base")
    call sna_main("It might come in handy sooner than I thought.", "snape_02", xpos="base", ypos="base")
    call sna_walk("door","leave",2) 
    call sna_main(remove=True)
    
    n "The door shut and silence spread across the room only interrupted after a few minutes by the house elf."
    
    call helf_main("So, should I turn invisible again sir?")
    
    m "Yes...yes that will be for the best."
    call helf_main(remove=True)
    "The end."
    
    hide screen genie
    hide screen main_room
    jump enter_room_of_req
    
    
