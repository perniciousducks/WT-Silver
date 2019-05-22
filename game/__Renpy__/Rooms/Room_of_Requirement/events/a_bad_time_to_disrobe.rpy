label a_bad_time_to_disrobe:
    show screen blkfade
    call h_equip_temp_outfit(hg_standart_school_ITEM)
    call room("main_room")
    menu:
        "Part 1":
            jump a_bad_time_to_disrobe_part_1
        "Part 2":
            jump a_bad_time_to_disrobe_part_2


label a_bad_time_to_disrobe_part_1:
    $ temp_time = daytime
    $ daytime = True
    $ interface_color = "gold"

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

    $ daytime = False
    $ interface_color = "gray"
    nar "Later that evening. Hermione returns."
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

    show screen quistion_pop_up("{color=#cbcbcb}Hermione will remember that{/color}")
    nar "Hermione returns the next morning, looking nervous but more determined than yesterday."
    $ daytime = True
    $ interface_color = "gold"

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

    $ daytime = False
    $ interface_color = "gray"
    nar "Later that evening a distraught looking Hermione enters the office. "

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

    $ daytime = temp_time
    if daytime:
        $ interface_color = "gold"
    else:
        $ interface_color = "gray"
    call room(hide_screens=True)
    call reset_hermione
    call h_unequip_temp_outfit
    jump enter_room_of_req

label a_bad_time_to_disrobe_part_2:
    $ temp_time = daytime
    $ daytime = True
    call music_block

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
    $ daytime = False
    $ interface_color = "gray"
    call music_block

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
    call blkfade
    centered "{size=+10}{color=#cbcbcb}The end{/color}{/size}"

    call room(hide_screens=True)
    $ daytime = temp_time
    if daytime:
        $ interface_color = "gold"
    else:
        $ interface_color = "gray"
    call music_block
    call reset_hermione
    call set_her_action("none")
    jump enter_room_of_req