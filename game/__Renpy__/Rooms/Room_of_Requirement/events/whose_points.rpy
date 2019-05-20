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