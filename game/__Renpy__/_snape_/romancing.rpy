

label date_with_snape_01:
    call bld 
    m "Alright. Teach me your wand-based magic now."
    call sna_head("Sure, I could do that...","snape_23",xpos="base",ypos="base") 
    call sna_head("Or I could tell you some more about those teenage \"slytherin\" sluts...","snape_02") 
    g9 "The latter, please."
    call sna_head("Great... Get a load of this then...","snape_13") 
    pause.1
    call blktone 

    ">You spend the evening by discussing all sorts of inappropriate things with Porfessor Snape."
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">You feel a faint bond forming between you two..."
    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return
    
    
label date_with_snape_02:
    call bld 
    m "For our little enterprise to succeed..."
    m "You need to be more generous with these house point things..."
    call sna_head("Right, of course...","snape_09",xpos="base",ypos="base") 
    sna "Miss Granger will require a strong incentive..."
    sna "So putting my house in the lead is essential..."
    call sna_head("Could take time though...","snape_06") 
    m "Take time?"
    m "Why not just award a couple of hundred points to \"Slytherin\" and be done with it?"
    call sna_head("No, we need to be discreet with this...","snape_24") 
    call sna_head("Awarding a whole bunch of points to my house without any reason could draw in unnecessary attention...","snape_05") 
    m "Hm... I see your point..."
    call blktone 

    ">You spend the evening by conspiring against Hermone with professor Snape..."
    ">The faint bond of friendship between you two strengthens."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return
    

label date_with_snape_03:
    call bld 
    call sna_head("Have you heard of that \"men's rights movement\" nonsense?","snape_01",xpos="base",ypos="base") 
    sna "She is smart, popular and has a will of iron..."
    $ s_sprite = "characters/snape/main/snape_06.png"
    call sna_head("Lately I am starting to feel very doubtful about our whole plan...","snape_06") 
    m "You shouldn't though..."
    call sna_head("Is that so...","snape_26") 
    m "It may take some time, but I {size=+5}will{/size} break her."
    m "Just trust me."
    sna "Alright..."
    call sna_head("What choice do I have but to hope for the best...?","snape_06") 
    call blktone 

    ">You spend the evening by dreading the uncertain future with professor Snape."
    ">A faint bond of trust is forming between you two."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how many points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
  
    return
    

label date_with_snape_04:
    call bld 
    call sna_head("Tell me something, Genie...","snape_24",xpos="base",ypos="base") 
    m "Yes?"        
    call sna_head("Do you believe in the theory of parallel worlds?","snape_25") 
    m "Well, it's hard not to. All things considered."
    call sna_head("True...","snape_23") 
    call sna_head("So, you think somewhere out there is another version of me?","snape_05") 
    m "Probably..."
    call sna_head("Hm...","snape_23") 
    sna "Severus Snape - the ever cheerful white mage..."
    m "Sure, why not?"
    call sna_head("What unsettling imagery you put into my mind...","snape_03") 
    m "How about another version of that Granger girl?"
    call sna_head("Yes! Hermione Granger - the repulsive slut without any dignity! Yes, I like it!","snape_02") 
    m "And what if in that other world the cheerful Severus teams up with some bizarre version of me?"
    m "And maybe together we train the slut Hermione to be a proper girl and a good student?"
    call sna_head("Ha-ha-ha! That's hilarious!","snape_28") 
    pause.1
    call blktone 

    ">You spend the evening by discussing science, metaphysics, philosophy and sluts."
    ">the bond of friendship between you and Professor Snape strengthens."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return

    
    
label date_with_snape_05:
    call bld 
    call sna_head("So... How is our little plan coming along?","snape_05",xpos="base",ypos="base") 
    sna "Is that wretched girl giving you trouble?"

    menu:
        "\"Yeah. She's stubborn.\"":
            call sna_head("No surprise there...","snape_06") 
        "\"No, not really...\"":
            call sna_head("Seriously?","snape_05") 
            sna "Interesting..."
    call sna_head("But you are positive you will be able to break her?","snape_01") 
    m "Oh, absolutely."
    m "It may take some time though..."
    call sna_head("Well, we do have time...","snape_06") 
    call sna_head("You are still pretty much powerless, right?","snape_05") 
    m "Yeah, pretty much..."
    call sna_head("Splendid!","snape_02") 
    m "......................."
    call sna_head("I mean, it is bad for {size=+5}you{/size}, but good for {size=+5}us{/size}, right?","snape_29") 
    m "Right..."
    call blktone 

    ">Professor Snape seems to feel awkward about benefitting from your misery..."
    ">The bond of friendship between you two strengthens slightly..."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return
    

label date_with_snape_06:
    call bld 
    m "So, tell me about those \"slytherin\" sluts some more!"
    call sna_head("What can I say? Life's been good to me lately, my friend.","snape_23",xpos="base",ypos="base") 
    call sna_head("These days I have a whole harem of skimpy students to choose from.","snape_22") 
    g9 "Nice!"
    call sna_head("Yes. Thanks to you, I can do whatever the bloody hell I want!","snape_02") 
    sna "And more importantly..."
    call sna_head("Whoever the hell I want!","snape_13") 
    m "Seriously?"
    call sna_head("Well, sort of...","snape_09") 
    sna "Obviously I don't actually walk around and \"do whoever I want\"..."
    call sna_head("But you wouldn't believe what some of those girls are willing to do in exchange for house points!","snape_13") 
    call sna_head("Or even for the mere promise of good grades...","snape_22") 
    pause.1
    call blktone 

    ">Professor Snape's usual cold exterior disintegrates before your eyes..."
    ">The bond of your friendship strengthens yet again..."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return
    
    
label date_with_snape_07:
    call bld 
    call sna_head("So, back in your world you are some kind of all-powerful being?","snape_05",xpos="base",ypos="base") 
    m "Yeah, sort of..."
    call sna_head("Then how come you do the bidding of that Jasmine woman?","snape_05") 
    m "Oh... Well..."
    m "...she is a princess."
    call sna_head("So?","snape_05") 
    sna "Is she your princess? You are not even human."
    sna "Did you swear your loyalty to her?"
    hide screen s_head2  
    m "Not really..."
    call sna_head("Why do you even bother then?","snape_06") 
    call sna_head("The way I see it, you are an all-powerful being and she is just some muggle...","snape_09") 
    m "She's a what?"
    call sna_head("A human... She's just a human...","snape_25") 
    call sna_head("So why bother trying to please her?","snape_05") 
    m "Well it's complicated..."
    call sna_head("..............","snape_05") 
    m ".................."
    call sna_head("She's hot, isn't she?","snape_02") 
    m "Smoking..."
    call sna_head("Gotcha.","snape_23") 
    pause.1
    call blktone 

    ">You and professor Snape share a bitter-sweet moment of complete male solidarity."
    ">The bond of your friendship strengthens."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return
    
    
label date_with_snape_08:
    call bld 
    call sna_head("Do you think if we wanted to...","snape_05",xpos="base",ypos="base") 
    sna "We could bring the public flogging back?"
    m "What do you mean?"
    call sna_head("Well, years ago flogging was a completely acceptable measure of punishment for the students.","snape_06") 
    sna "*Sigh* Simpler times..."
    call sna_head("These days students just completely lack discipline...","snape_16") 
    sna "I would like nothing more than to publicly flog every single one of them..."
    call sna_head("Especially the girls...","snape_22") 
    m "Hm... Fine by me..."
    m "But won't a reform like that attract unnecessary attention towards us?"
    call sna_head("Yes. You are right of course.","snape_29") 
    sna "I am getting greedy..."
    call sna_head("I'm getting drunk with power, my friend!","snape_28") 
    sna "And this exquisite wine does not improve my judgment in the slightest either!"
    pause.1
    call blktone 

    ">Professor Snape seems to be completely at ease around you now."
    ">The bond of male friendship between you twe strengthens even more.\n>\"Slytherin\" house point payouts have increased formidably..."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_09:
    call bld 
    call sna_head("...so, after that I return back to Russia, right?","snape_24",xpos="base",ypos="base") 
    g4 "Back to Russia?"
    call sna_head("But wait, it gets worse.","snape_01") 
    call sna_head("Apparently I am fluent in Russian now.","snape_05") 
    g4 "Wait, what?"
    call sna_head("And I am this miserable muggle guy who lives in this shithole of a town full of rundown buildings.","snape_06") 
    sna "I try to make a living by drawing comics and creating games with \"Ren'Py\"..."
    call sna_head("And that is so bizarre because I don't even know what a \"Ren'Py\" is!","snape_24") 
    m "Hm... Then what happened?"
    call sna_head("Not much... Mostly worked my ass off for months...","snape_05") 
    sna "Then managed to create a relatively successful game somehow..."
    call sna_head("Eventually began to make decent money with my craft...","snape_24") 
    call sna_head("And then, just when I was about to allow myself to feel hopeful about the future...","snape_06") 
    call sna_head("I woke up...","snape_04") 
    call sna_head("....................","snape_09") 
    m "......................"
    call sna_head("What do you think all of that means?","snape_05") 
    m "Sounds like another one of Akabur's self-inserts."
    call sna_head("What?","snape_05") 
    m "Just ignore the whole thing."
    m "A silly dream, nothing more."
    call sna_head("Felt more like a nightmare...","snape_29") 
    pause.1
    call blktone 

    ">Professor Snape trusts you more than he used to..."
    ">(To the point where he doesn't think twice about sharing his weird-ass dreams with you)."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return
    
    
label date_with_snape_10:
    call bld 
    call sna_head("What is the meaning of life, Genie?","snape_29",xpos="base",ypos="base") 
    g4 "What?"
    call sna_head("Since you are an all-powerful being, you've got to know things like that, right?","snape_05") 
    m "Maybe..."
    call sna_head("Great. Tell me then.","snape_06") 
    m "Hm... You sure you're ready for this?"
    call sna_head("Yes. Lay it on me, friend.","snape_05") 
    m "Alright then..."
    call sna_head("................!","snape_01") 
    m "It's plastic..."
    call sna_head("I beg your pardon?","snape_05") 
    m "it's plastic..."
    call sna_head("I don't get it...","snape_25") 
    m "This planet plans to evolve into something else in a million years or so..."
    m "In order to do that it needs a special kind of material that it can't produce on it's own."
    m "So it spawns a new form of life - humans."
    call sna_head("..............","snape_11") 
    m "You wanted to know the purpose of your existence?"
    m "It's to produce plastic. Simple as that."
    call sna_head("Are you fucking kidding me?!","snape_30") 
    call sna_head("No, no... That can't be it...","snape_26") 
    g9 "He-he..."
    call sna_head("Are you pulling my leg?","snape_25") 
    g9 "You should've seen your face."
    call sna_head("You really got me worried there, you bloody non-human bastard!","snape_15") 
    g9 "I know! It was hard to resist..."
    call blktone 

    ">You spend the evening by skillfully avoiding a whole variety of similar questions."
    ">Despite your refusal to cooperate the bond of friendship between you two strengthens yet again."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return


label date_with_snape_11:
    call bld 
    call sna_head("So... Back in your world, do you people have a country named England?","snape_05",xpos="base",ypos="base") 
    m "We used to..."
    call sna_head("What happened?","snape_26") 
    m "\"The great catastrophe\"..."
    m "It incinerated most of the worlds population in a matter of hours..."
    call sna_head("................","snape_26") 
    m "Turning about eighty percent of the planet's surface into a scorching desert..."
    m "And the remaining twenty percent into an icy wasteland..."
    m "............."
    call sna_head("That is...","snape_26") 
    call sna_head("Horrible...","snape_06") 
    call sna_head("Are you sure that you want to return to that place?","snape_25") 
    m "Of course."
    m "It may be a bit barbaric, but hey... it's home."
    call blktone 

    ">Professor Snape finds a new level of respect for you..."
    ">The bond of friendship between you two solidifies."

    call sly_plus 
    call hide_blktone 
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return

    
label date_with_snape_12:
    call bld 
    call sna_head("I've been thinking about what you've said the other day...","snape_09",xpos="base",ypos="base") 
    sna "About your home world being nothing but a scorched desert and all..."
    m "Yes?"
    call sna_head("Do you think Albus will be alright there?","snape_06") 
    m "Oh, absolutely!"
    m "Since I quite literally replaced him in his chair..."
    m "He probably replaced me in exactly the same place back in Agrabah."
    call sna_head("Agrabah?","snape_05") 
    m "Yes... A very big city."
    m "One of the few that rose after the great catastrophe."
    m "Probably the biggest of them all as well..."
    m "the heart of the human civilization if you will."
    call sna_head("I am relieved to hear that...","snape_23") 
    m "Sure..."
    m "Although if your Albus friend really materialized in exactly the same spot I occupied before I casted the spell..."
    m "I suppose the princess could have him beheaded..."
    call sna_head("WHAT?!","snape_01") 
    m "But the probabilty of that happening is very slim..."
    m "About five percent... Maybe ten... Twenty percent tops."
    call sna_head(".......................................................","snape_03") 
    pause.1
    call blktone 

    ">Professor Snape seems grateful to you for (sort of) putting his concerns about Albus Dumbledore's well-being to rest..."
    ">The bond of your friendship strengthens yet again..."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return

    
label date_with_snape_13:
    call bld 
    call sna_head("You know what?","snape_01",xpos="base",ypos="base") 
    m "What?"
    call sna_head("For the first time in a very long time...","snape_01") 
    call sna_head("I think...","snape_03") 
    call sna_head("I am actually content with the way my life is going.","snape_25") # 0_0
    call sna_head("What an unsettling feeling...","snape_26") 
    m "Are you sure that this is not some euphoric trance state caused by all the sex you've been having lately?"
    call sna_head("Could be.","snape_22") 
    call sna_head("Nonetheless, you may only be training just one girl...","snape_09") 
    call sna_head("But it has a great impact on my life...","snape_24") 
    sna "And even the school itself..."
    m "In other words you are getting less broody and you blame me."
    call sna_head("Something like that...","snape_23") 
    call sna_head("I'm losing my dark presence, man.","snape_28") # :)
    pause.1
    call blktone 

    ">Professor Snape really did become a little more cheerful lately..."
    ">He even looks younger now than back when you first met him..."
    ">Professor Snape's feeling of gratitude fortifies the bond of your friendship."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return

    
label date_with_snape_14:
    call bld 
    call sna_head("...so she says: \"Sir, could you choke me a little, please!\".","snape_02",xpos="base",ypos="base") 
    call sna_head("And I am happy to oblige of course!","snape_13") 
    call sna_head("So, I choke that little bitch while I'm fucking her, right?","snape_19") 
    sna "And she rolls her eyes up to the point where I can't even see her pupils anymore!"
    sna "Her face turns to a cute tint of purple and she's barely breathing."
    call sna_head("So I think that maybe I should loosen up my grip a little...","snape_14") 
    call sna_head("And that's when the bitch starts to cum!","snape_21") 
    m "Sweet! And then you woke up?"
    call sna_head("What? No, it actually happened.","snape_05") 
    call sna_head("I finally nailed that blond witch from \"Slytherin\".","snape_13") 
    g9 "Nice!"
    call sna_head("I know.","snape_13") 
    call sna_head("She is pretty twisted though...","snape_25") 
    call sna_head("And I mean really fucking messed up.","snape_26") 
    g9 "Our type of girl!"
    call sna_head("Exactly!","snape_22") 
    pause.1
    call blktone 

    ">You and professor Snape bond over the similarities of your taste in women."
    ">The bond of your friendship has never been stronger."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.

    return

    
label date_with_snape_15:
    call sna_head("It's been a while now...","snape_05",xpos="base",ypos="base") 
    m "What do you mean?"
    call sna_head("The spell that brought you here...","snape_24") 
    sna "You said it would wear off in time..."
    call sna_head("Do you feel any different?","snape_05") 
    m "No... Not really..."
    m "Maybe it needs more time?"
    call sna_head("Could be...","snape_01") 
    sna "Or there could be something else..."
    m "Like what?"
    call sna_head("No idea...","snape_09") 
    sna "But I shall give this some more thought..."
    call sna_head("Oh, and one more thing...","snape_24") 
    m "Hm...?"
    call sna_head("This time of the year is usually pretty busy...","snape_24") 
    sna "Even more so now when I need to constantly cover up for Albus' absence."
    hide screen s_head2
    m "..................."
    call sna_head("I'm not sure if I will be able to spend my evenings with leisurely drinking wine anymore...","snape_06") 
    m "Really?"
    call sna_head("Yes...","snape_06") 
    sna "I'll  still be around for a quick chat from time to time, but that's about it."
    hide screen s_head2
    m "I see..."
    m "I will have to find another way of spending my evenings from now on then..."
    call sna_head("I'm sure miss granger will be happy to help.","snape_02") 
    m "Yes, for as long as \"slytherin\" is in the lead."
    call sna_head("Seriously? She still cares about that?","snape_05") 
    m "Very much so."
    call sna_head("Well in that case I shall personally ensure that \"slytherin\" house gets as many house points as possible.","snape_23") 
    pause.1
    call blktone 

    ">Your friendship level with professor Snape reached itss maximum value."
    ">Congratulations. If this were a \"dating-sim\" you would be getting the ending with Severus Snape."
    ">The \"Slytherin\" house point payout has increased greatly and reached it's maximum level as well."

    call sly_plus 
    call hide_blktone 

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    $ sfmax = True # Turns TRUE when friendship with Snape been maxed out.

    return

    
label sly_plus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">The \"Slytherin\" house point payout has increased..."
    return



