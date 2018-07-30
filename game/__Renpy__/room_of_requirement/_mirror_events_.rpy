screen whose_points_screen:
    add "images/room_of_requirement/whose_points.png"
    
label whose_points:
    show screen bld1
    with Dissolve(.3)
    call hide_room_req
    show screen whose_points_screen

    m "Hello and welcome to whose points is it anyway."
    m "The show where everything is made up but the points doesn't matter."
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
    
    m "Looks like we have our first promt."
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
    m "Any more? On to the next promt then. Hat?"
    
    hat "Sorry, what did you cough call me? That's \n\"Sorting\" Hat to you. (coughs out note.)"
    
    g9 "Things you might do in quidditch... but also with your lover..."
    
    call ast_main( "I'm going first this time! I have a good one!", "grin", "base", "base", "mid") 
    
    m "Go on...."
    
    call ast_main( "Madam Hooch! Get your gross hands off my quidditch robes, you creep!" ,"clench", "angry", "angry", "mid") 
    
    m "Again, I don't think you understand the game..."
    
    call ast_main( "Give me the points!" , "scream", "narrow", "narrow", "mid") 
    
    m "Disquallified!"
    
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
    call luna_main("The whole wizarding world are going see your tits!", "default", "default", "default", "wide_smile")
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
    show screen bld1
    with Dissolve(.3)
    call hide_room_req
    show screen main_room
    show screen genie
    
    "This story takes place in between the introduction of Snape and first meeting Hermione."

    m "\"How does that door work?\""
    m "\"How does the people know I’ve summoned them?\""
    m "\"thoughts: I don’t have a secretary...that I know of anyway.\""
    m "\"Have they been keeping a secretary from me? I should ask Snape.\""

    call sna_walk("door","mid",2) 
    call sna_main("You called? ", "snape_23", xpos="base", ypos="base")

    g11 "How did you, how do you...this door, how does it work?"
    m "\"What is this... this unfamiliar magic.\""
    m "\"I know the ins and outs of the universe. But this world is just so alien to me…\""
    m "\"thoughts: At least I know things about aliens….\""

    call sna_main("Well, you’re the headmaster are you not? ", "snape_23", xpos="base", ypos="base")

    m "What’s that supposed to mean?"

    call sna_main("...", "snape_02", xpos="base", ypos="base")
    call sna_main("I keep forgetting that you don’t know these things.", "snape_01", xpos="base", ypos="base")
    call sna_main("People that were educated here already knows how things work. ", "snape_01", xpos="base", ypos="base")
    call sna_main("The headmaster is in control of the school and its inhabitants.", "snape_24", xpos="base", ypos="base")

    m "I know that, we have schools in my world to..."
    m "But we generally don’t wave wooden sticks around yelling random words."

    call sna_main("...", "snape_08", xpos="base", ypos="base")
    call sna_main("No. You’re literally in control over the school....look.", "snape_01", xpos="base", ypos="base")
    call sna_main("Revelio!", "snape_01", xpos="base", ypos="base")
    call sna_main(remove=True)
    
    call helf_main("Oh, hello there sir!")
    
    g5 "What the hell is that?"
    
    call helf_main(remove=True)
    
    call sna_main("That…", "snape_01", xpos="base", ypos="base")
    call sna_main("Is an house elf.", "snape_01", xpos="base", ypos="base")

    m "An house...elf. Is that like a Santa's elf?"

    call sna_main("Sort of, they don’t get paid so they do have that in common…", "snape_01", xpos="base", ypos="base")
    call sna_main("Ahem, anyway…. The house elf here can send us messages so we’ll go where we are needed.", "snape_01", xpos="base", ypos="base")
    call sna_main("He just sits here invisible during the day and cleans and eat at night.", "snape_01", xpos="base", ypos="base")
    
    m "The house elf cleans? I thought I had some sort of magic self cleaning desk…"
    
    call sna_main(remove=True)
    
    call helf_main("No sir... I see it all, I clean it all....every...last bit of it.")
    call helf_main(remove=True)
    
    call sna_main("...", "snape_08", xpos="base", ypos="base")
    
    m "..."

    
    call sna_walk("mid","door",2) 
    call sna_main("If that is all, I’ll be in the dungeons. I’ve been working on a new cleaning solution.", "snape_01", xpos="base", ypos="base")
    call sna_main("It seems like it might come in handy sooner than I thought.", "snape_01", xpos="base", ypos="base")
    call sna_walk("door","leave",2) 
    
    m "..."

    call sna_main(remove=True)
    
    call helf_main("So, should I turn invisible again sir?")
    call helf_main(remove=True)
    
    m "Yes...yes that will be for the best."

    "The end."
    
    hide screen genie
    hide screen main_room
    jump enter_room_of_req
    
    