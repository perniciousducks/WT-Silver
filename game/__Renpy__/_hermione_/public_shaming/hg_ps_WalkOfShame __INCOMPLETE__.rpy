

### Walk Of Shame ###

label hg_ps_walk: #This will become more intense as the wear a shorter skirt and wear a sluttier shirt favours are completed

    m "[hermione_name], what classes do you have today?"
    call her_main("What? Since when have you taken an interest in my education?","normal","frown") 
    m "I'm your headmaster, of course I care about your studies."
    call her_main("Hmmmm...","normal","frown") 
    call her_main("Well I have potions class with Professor Snape in the morning and then defence against the dark arts after lunch.","normal","frown") 
    m "So you have Snape as your teacher today?"
    call her_main("Yes [genie_name].","normal","frown") 
    m "That's good. Today I have a task for you to complete."
    call her_main("A task?","normal","frown") 
    m "Yes, I'd like you to attend class."
    call her_main("Is that all?","normal","frown") 
    m "Without your shirt."
    call her_main("WHAT?","normal","frown") 
    call her_main("Why on earth would I do that?","normal","frown") 
    m "Because I asked you to."
    call her_main("...but what about Snape? What about my classmates?","normal","frown") 
    m "Don't worry about Snape, I'm sure that he's used to your behaviour by now."
    m "And as for your classmates, is there anyone that will be surprised?"
    call her_main("Well Ginny would be...","normal","frown") 
    m "What? Shocked to find out that her friend is a massive slut who shows herself off to anyone and everyone any chance she can get?"
    m "Look at your neck [hermione_name], look at what you are wearing. I'd be surprised if there is anyone in the school who doesn't know what a whore you are."
    call her_main("...","normal","frown") 
    ">She holds back tears as she hands you her shirt."
    call her_main("I suppose that you're right [genie_name].","normal","frown") 
    call her_main("Well I best be off... Can't be late for class.","normal","frown") 
    ">She leaves your office reluctantly."
    $ hg_ps_walk.inProgress = True

label hg_ps_walk_complete:#Returns to your office after being made walk around the school with no shirt
    return