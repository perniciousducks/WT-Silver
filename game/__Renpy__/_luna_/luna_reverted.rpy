label luna_reverted_events: #MUST BE WEARING GLASSES!
    if luna_corruption == 0:
        jump luna_reverted_event_1
    elif luna_corruption == 1:
        jump luna_reverted_event_2
    elif luna_corruption == 2:
        jump luna_reverted_event_3

    jump day_main_menu

label luna_reverted_event_1: #Masturbate for genie again. 
    $ luna_corruption = 1
    $ days_to_luna = 4
    "*knock* *knock* *knock*"
    m "Come in..."
    call play_sound("door") #Sound of a door opening.
    $ luna_chibi("stand")
    ">Luna stands in front of your desk."
    call luna_main("Hello again Sir...", "closed_happy", "default", "default", "default") 
    m "Miss Lovegood. How have you been?"
    call luna_main("Alright... but the wrackspurts seem to have come back..", "default", "right", "angry", "angry") 
    m "Again? So soon?"
    call luna_main("I'm afraid so sir...", "default", "default", "sad", "upset") 
    call luna_main("Everytime I think about what we did in here...", "wide", "default", "sad", "upset") 
    call luna_main("It just makes them feel so much... stronger...", "angry", "right", "sad", "upset") 
    m "Yes... They must be afraid of my powerful techniques..."
    call luna_main("Do you think so?", "closed", "right", "sad", "upset") 
    m "I do..."
    m "Why else would they attack you when you think about curing them?"
    call luna_main("You're right...", "angry", "default", "sad", "upset") 
    m "So... Are you ready to try and dispel them again?"
    call luna_main("Only if it's not too much trouble sir... I wouldn't want to disturb you...", "angry", "right", "sad", "angry") 
    m "Please, as headmaster it's my duty to make sure my students are safe..."
    call luna_main("You're right...", "seductive", "down", "sad", "upset") 
    call luna_main("I just feel guilty coming up her so often...", "seductive", "right", "sad", "upset") 
    m "don't..."
    "*Luna starts grinding her thighs together.*"
    call luna_main("Ok...", "seductive", "down", "sad", "default") 
    call luna_main("So, is it OK if I start scratching...", "seductive", "default", "sad", "default") 
    m "I don't see why not. Just stand in the middle of the room for me."
    hide screen luna 
    with d3
    $ luna_xpos = 400
    call luna_main("...", "default", "default", "sad", "pout") 
    m "That's it..."
    m "Would you like to start Miss lovegood?"
    $ luna_l_arm = 4
    ">Luna quickly puts her hand down her skirt, barely waiting for you to finish your sentence..."
    call luna_main("ah... thank you sir...", "seductive", "down", "sad", "upset") 
    m "You seem relieved..."
    call luna_main("ah... of course... I've been waiting to come here since yesterday...", "wide", "default", "sad", "default") 
    call luna_main("I think Those slimy wrackspurts have infested the commonroom...", "seductive", "down", "sad", "default") 
    m "That's quite possible..."
    call luna_main("ah... ah...", "closed_happy", "right", "sad", "upset") 
    call luna_main("but getting rid of them... feels... so... good...", "default", "left_stare", "sad", "pout") 
    call luna_main("I'm almost glad I've got them...", "default", "left_stare", "sad", "pout") 
    m "The positive feelings you have are your body reacting to the wickerspats being expelled from your body."
    call luna_main("really?", "closed", "right", "sad", "default") 
    call luna_main("ah...", "default", "left_stare", "sad", "upset") 
    call luna_main("I must... ah... be expelling a lot then...", "seductive", "default", "sad", "talk") 
    call luna_main("in fact...", "wide", "right", "sad", "upset") 
    call luna_main("ah...", "seductive", "down", "sad", "upset") 
    call luna_main("I think... ah... I'm about to... ah...", "seductive", "default", "sad", "pout") 
    call luna_main("Mmmm, it's just like... last time...", "seductive", "right", "sad", "upset") 
    m "Oh, are you cumming already?"
    call luna_main("cumming?", "seductive", "down", "sad", "upset") 
    call luna_main("what's? ah...{image=textheart}", "angry", "left_stare", "sad", "pout") 
    call luna_main("Cumming?{image=textheart}", "seductive", "default", "sad", "upset") 
    call luna_main("Ah... I'm cumming...{image=textheart}{image=textheart}", "wide", "default", "sad", "upset") 
    m "Mmmmm that's it girl..."
    call luna_main("Ah...{image=textheart}", "wide", "down", "sad", "upset")
    ">You see a flush of red roll over Luna's face as her body twitches with the throes of her orgasm." 
    ">However despite this, her fingers remain a flurry of movement under her skirt."
    m "Well, it seems those wickedspots have been giving you a bit of grief now haven't they?"
    label luna_masturbate_again:
        pass
    call luna_main("ah...{image=textheart}yes{image=textheart}", "seductive", "default", "raised", "upset") 
    m "Don't worry, that should sort them out for now..."
    call luna_main("ummm...", "default", "right", "sad", "default") 
    m "What's wrong?"
    call luna_main("...", "closed_happy", "right", "sad", "upset") #eyes closed
    call luna_main("is it...", "closed_happy", "right", "sad", "angry") 
    call luna_main("Ok if I do it once more?", "closed_happy", "right", "sad", "upset") 
    m "What?"
    call luna_main("If you need to do other things I can leave!", "closed_happy", "right", "sad", "default") #smile
    m "There's no need for that! You can stay here as long as you like..."
    m "I was just a little surprised that you needed to go again is all..."
    call luna_main("Ah... well...", "closed_happy", "right", "default", "default") 
    call luna_main("these wrackspurts...", "closed_happy", "right", "default", "upset") 
    call luna_main("ah...", "closed_happy", "right", "sad", "pout") 
    call luna_main("they've been very tiresome...", "closed_happy", "right", "sad", "upset") 
    call luna_main("...", "closed_happy", "right", "sad", "default") 
    call luna_main("besides...", "closed_happy", "right", "default", "default") 
    ">Luna starts dancing her fingers along under her skirt."
    call luna_main("ah...", "closed_happy", "right", "sad", "default") 
    call luna_main("I've been... waiting for this all day...", "closed_happy", "right", "sad", "grin") 
    ">Luna starts to softly moan under her breath."
    call luna_main("standing here...", "closed_happy", "right", "sad", "default") 
    m "..."
    call luna_main("{image=textheart}{image=textheart}{image=textheart}", "closed_happy", "right", "default", "grin") 
    call luna_main("in front of my headmaster...", "closed_happy", "right", "sad", "default") 
    call luna_main("While he helps me to...", "closed_happy", "right", "default", "default") 
    m "Shhh, don't speak, just focus..."
    call luna_main("ok...", "closed_happy", "right", "sad", "upset") 
    call luna_main("...", "closed_happy", "right", "sad", "default") 
    call luna_main("ah...", "closed_happy", "right", "sad", "grin") 
    call luna_main("{image=textheart}", "closed_happy", "right", "sad", "default") 
    call luna_main("...", "closed_happy", "right", "sad", "angry") 
    call luna_main("ah... sir...", "seductive", "default", "sad", "upset") 
    call luna_main("I think...", "seductive", "down", "sad", "grin") 
    call luna_main("ah...", "seductive", "right", "sad", "grin") 
    call luna_main("I think I've almost got them...", "closed_happy", "right", "sad", "grin") 
    m "Shhh..."
    call luna_main("ah...", "closed_happy", "default", "angry", "grin") 
    ">Luna's fingers start furiously dancing underneath her skirt."
    call luna_main("mmmm...", "closed_happy", "default", "angry", "default") 
    call luna_main("ah...", "closed_happy", "default", "angry", "grin") 
    call luna_main("a-ah...", "seductive", "down", "sad", "default") 
    call luna_main("yes...", "seductive", "left_stare", "angry", "default") 
    m "(I think this is it!)"
    call luna_main("Ah... ah...{image=textheart}", "seductive", "right", "sad", "grin") 
    call luna_main("{size=+4}mmm... yes...{image=textheart}{/size}", "seductive", "down", "sad", "default") 
    call luna_main("{size=+8}ah... oh... frickity!!!{/size}", "seductive", "left_stare", "sad", "grin") 
    call luna_main("!!!", "wide", "default", "sad", "grin") #orgasm face
    ">THere's a blur of movement under Luna's skirt."
    call luna_main("ah! thank you sir!", "wide", "left_stare", "sad", "default") 
    call luna_main("!!!", "wide", "default", "sad", "default") #orgasm face
    m "Is everything OK?"
    call luna_main("Ah... yes{image=textheart} thank you{image=textheart} sir...{image=textheart}", "seductive", "right", "sad", "upset") 
    m "so Have the wickspots left you alone now?"
    call luna_main("I think so, sir...", "seductive", "default", "sad", "upset") 
    $ luna_l_arm = 1
    ">Luna slowly pulls her sopping hand out from under her skirt."
    call luna_main("at least That nasty itch seems to have gone away.", "default", "default", "sad", "default") 
    m "Fantastic! will that be all then, Miss Lovegood."
    call luna_main("well I don't suppose I could go-", "seductive", "down", "sad", "upset") 
    call luna_main("No... I better get to bed...", "seductive", "right", "sad", "angry") 
    call luna_main("Thanks again sir!", "seductive", "down", "sad", "upset") 
    ">Luna gives you one last smile before leaving your office."
    m "What an odd girl."
    jump luna_away


label luna_reverted_event_2: #Masturbate for Genie and then Genie cum on Luna's face
    $ luna_corruption = 2
    $ days_to_luna = 3
    "*knock* *knock* *knock*"
    lun "Can I please come in sir..."
    ">There's a desperate twang to Luna's voice."
    menu:
        "-Let her in-":
            m "Of course."
        "-mess with her-":
            m "Who is it?"
            lun "Luna Lovegood sir..."
            lun "May I please come in?"
            m "Luna who?"
            lun "Lovegood sir..."
            m "Oh miss lovegood! Come in..."
    ">Luna quickly enters your office, her face covered in a deep blush."
    $ luna_chibi("stand")
    call luna_main("...", "tired", "right", "sad", "pout") 
    m "Miss Lovegood..."
    m "What can I help you with today?"
    call luna_main("I-I... need...", "seductive", "down", "sad", "talk") 
    $ luna_l_arm = 4
    ">Luna quickly puts her hand down her skirt, not even waiting on your reply..."
    call luna_main("ah... I'm sorry sir... I just... needed... this...{image=textheart}", "seductive", "up", "sad", "default") 
    m "You seem relieved..."
    call luna_main("ah... {image=textheart} yes...", "wide", "left_stare", "sad", "default") 
    call luna_main("these visits are starting to become all I can think about...", "seductive", "down", "sad", "default") 
    m "Hmmm... Do you think that's a bad thing?"
    call luna_main("ah... of course not!", "closed_happy", "right", "sad", "upset") 
    call luna_main("it just... means that it's working...", "default", "left_stare", "sad", "pout") 
    call luna_main("if only I could spend all day up here...", "default", "left_stare", "sad", "default") 
    m "Do you think a full day of treatment would get rid of them?"
    call luna_main("ah...", "default", "left_stare", "sad", "default") 
    call luna_main("probably not...", "seductive", "default", "sad", "talk") 
    call luna_main("but...", "wide", "right", "sad", "default") 
    call luna_main("ah...", "seductive", "down", "sad", "default") 
    call luna_main("I think... it'd probably feel...", "seductive", "default", "sad", "talk") 
    call luna_main("nice...{image=textheart}{image=textheart}{image=textheart}", "seductive", "right", "sad", "default") 
    m "Speaking of feeling nice..."
    call luna_main("Ah... I think I'm... cumming sir...", "seductive", "down", "sad", "open_tongue") 
    call luna_main("ah...{image=textheart}", "seductive", "left_stare", "sad", "default") 
    call luna_main("mmmmm{image=textheart}", "seductive", "default", "sad", "default") 
    call luna_main("Ah... I'm cumming...{image=textheart}{image=textheart}", "wide", "up", "sad", "default") 
    m "Mmmmm that's it girl..."
    call luna_main("Ah...{image=textheart}", "seductive", "down", "sad", "talk")
    $ luna_cheeks = "characters/luna/body/face/cheeks/cheeks_2.png"
    ">You see a flush of red roll over Luna's face as her body twitches with the throes of her orgasm." 
    ">Her fingers keep casually stroking her needy sex..."
    m "Well, it seems those wickedspots have been giving you a bit of grief now haven't they?"
    menu:
        "-Start jerking off-":
            pass
        "-behave-":
            jump luna_masturbate_again
    m "Truth be told they've been starting to affect me as well..."
    call luna_main("What? They got you too?", "angry", "left_stare", "sad", "default") 
    m "I was afraid this might happen with you dispelling all of your personal wrackspurts into this room..."
    m "This is why I didn't want you doing this outside the office..."
    call luna_main("It could have been a disaster sir...", "angry", "left_stare", "sad", "default") 
    call luna_main("But will you be alright?", "wink", "default", "raised", "talk") 
    m "Oh don't worry about me, I'm a {i}master{/i} when it comes to this..."
    call luna_main("Of course... These are your techniques after all...", "closed_happy", "default", "sad", "default") 
    call luna_main("Would it...", "seductive", "right", "sad", "default") 
    call luna_main("Would it be OK if I watched sir?", "tired", "default", "sad", "default") 
    call luna_main("Just as a way to improve my own technique!", "wink", "left_stare", "default", "default")
    m "Mmmm, I see nothing wrong with it..."
    m "Here, I'll come give you a {b}nice{/b} view..."
    show screen blkfade
    with d3
    hide screen luna
    ">With that you slowly rise out of your chair as your cock strains against your robe, brought furiously to life by Luna's own performance."
    ">You then walk around your desk until you stand in front of the pale blonde..."
    m "Here we go..."
    ">As you finally pull your cock from your robe your met with a shocked gasp from Luna."
    lun "It's so..."
    lun "can I..."
    lun "..."
    ">Before you can say anything else, Luna instinctively drops to her knees."
    $ ccg_folder = "luna_facial"
    $ ccg1 = "1"
    $ ccg2 = "genie"
    $ ccg3 = "blank"
    show screen ccg
    hide screen blkfade
    with d3
    lun "wow..."
    m "This is the place that those nasty little whiskersprouts like to hide on me..."
    $ ccg1 = "2"
    lun "It's... big..."
    m "It is..."
    $ ccg1 = "3"
    lun "How often do you have to get rid of them?"
    m "Maybe once or twice a day..."
    $ ccg1 = "4"
    lun "Only twice?"
    m "It depends on the day..."
    ">You start to stroke your cock, the thick stream of precum dripping from the tip more than lubricating your entire length."
    $ ccg1 = "1"
    m "Ugh yeah... that's it..."
    lun "..."
    $ ccg1 = "5"
    lun "Is there anything I should be looking for in particular?"
    m "Nothing in particular... just focus on taking it all in..."
    $ ccg1 = "6"
    lun "Taking it all in..."
    ">Luna stares intently at your cock for a few seconds before suddenly snapping from her reverie."
    $ ccg1 = "7"
    lun "OK sir, I'll take it all in!"
    ">Before you even have time to react, Luna swoops her head in towards your cock, placing her nostrils at the head..."
    $ ccg1 = "8"
    ">Luna takes a huge breath inwards, closing her eyes as she does..."
    $ ccg1 = "9"
    lun "Huh... It doesn't smell like I thought it would..."
    m "What did you think it would smell like?"
    $ ccg1 = "8"
    lun "Spices!"
    m "..."
    m "And what did it smell like?"
    $ ccg1 = "10"
    lun "Hmmm... It reminds me of a certain Bertie Bott's Every-Flavour bean I once had..."
    $ ccg1 = "11"
    lun "It wasn't very good... But it wasn't bad..."
    m "Well now that you've taken it all-"
    ">As if to purposely interrupt you, Luna leans her head in and quickly runs her tongue across the tip of your sensitive cock..."
    $ ccg1 = "12"
    m "What!"
    $ ccg1 = "13"
    lun "I was just hav-"
    m "Argh, you've done it now!"
    m "here it comes You little fucking minx!"
    $ ccg1 = "14"
    lun "Here comes wha-"
    m "ARGH!!!"
    ">As if in retaliation for her previous interruptions, your cock takes it upon itself to interrupt Miss Lovegoods own sentence with a thick deluge of semen."
    $ ccg1 = "15"
    m "There it is you horny little thing... here's what you wanted..."
    $ ccg1 = "16"
    lun "Oh..."
    $ ccg1 = "17"
    lun "What's this?"
    m "Argh..."
    $ ccg1 = "18"
    lun "It smells... so..."
    $ ccg1 = "19"
    lun "Goood...."
    $ ccg1 = "20"
    lun "Can I... Taste it?"
    m "I don't see why not."
    lun "..."
    $ ccg1 = "21"
    $ ccg2 = "blank"
    ">Luna slowly pulls a strand of your thick cum before closely examining it..."
    $ ccg1 = "22"
    lun "(My spectrespecs are detecting so much magic...)"
    lun "I've never seen anything like this before..."
    m "It's called cum."
    lun "Cum..."
    $ ccg1 = "23"
    ">With that, Luna finally decides to taste your essence."
    $ ccg1 = "24"
    lun "..."
    $ ccg1 = "25"
    lun "!!!"
    $ ccg1 = "24"
    lun "..."
    $ ccg1 = "26"
    lun "it's..."
    lun "it's......"
    $ ccg1 = "27"
    lun "it's perfect... it's just the best..."
    m "mmm... that's it... you always know what to say..."
    $ ccg1 = "28"
    lun "I'm not just..."
    $ ccg1 = "29"
    lun "How can you make this?"
    $ ccg1 = "28"
    lun "There's so much magic..."
    $ ccg1 = "30"
    lun "It's incredible..."
    $ ccg1 = "31"
    lun "It's soaking in through my skin... I can't..."
    lun "The wrackspurts... I think this is..."
    $ ccg1 = "32"
    lun "Ah... I think I should... probably leave now sir..."
    m "You're not going to clean yourself up first?"
    $ ccg1 = "33"
    lun "Oh..."
    lun "If it's ok with you sir... I might clean myself up back in my room..."
    m "Whatever suits you miss lovegood..."
    $ ccg1 = "30"
    lun "thank you sir... for... everything..."
    m "Will that be all miss lovegood?"
    lun "Oh, um yes..."
    $ ccg1 = "32"
    lun "I'll see you the next time those wrackspurts come up again..."
    m "See that you do."
    lun "yes sir..."
    show screen blkfade
    with d3
    hide screen ccg
    ">With that Luna stands up off the ground and leaves your office, still covered in cum..."
    hide screen luna
    hide screen luna_chibi
    hide screen blkfade
    with d3
    m "She really is a bit loony..."



    jump luna_away



label luna_reverted_event_3: #Luna gentle BJ where she just happily sucks and lick it like a lollipop for an hour
    $ luna_corruption = 3
    $ days_to_luna = 4
    ">*knock* *knock* *knock*"
    ">Before waiting for a response, your door swings open to reveal Luna Lovegood."
    $ luna_chibi("stand")
    call luna_main("Hello sir! Lovely day today isn't it?", "closed_happy", "default", "default", "default") 
    m "It is now..."
    call luna_main("Awww... that's so nice!", "wink", "default", "sad", "default") 
    m "What brings you up to my office today then Miss Lovegood?"
    m "Those troublesome little wrockspoons giving you grief again?"
    call luna_main("Not exactly...", "seductive", "down", "sad", "talk") 
    m "Oh... Something else I can help you with then?"
    call luna_main("Well... I was just walking past when I remembered how those nasty wrackspurts affected you the other day...", "default", "right", "sad", "open") 
    call luna_main("They aren't by any chance bothering you at the moment are they sir?", "wink", "left_stare", "sad", "default") 
    m "Now that you mention it, they have been giving me a little trouble..."
    m "But I'm much too tired to relieve them myself... I'm such an old man you see..."
    call luna_main("Really? But you look...", "wide", "default", "sad", "talk") 
    call luna_main("so you won't...", "tired", "down", "sad", "pout") 
    call luna_main("...", "tired", "right", "sad", "upset") 
    call luna_main("Is there any way I could help?", "wink", "default", "sad", "default") 
    m "Hmmmm... There is a special technique that I've been developing..."
    m "I'm not sure your ready for it though..."
    call luna_main("Please sir! I know I can handle it!", "wide", "default", "sad", "default") 
    m "Well if you insist..."
    m "Just make sure you don't let anyone else know about this..."
    call luna_main("I wouldn't dare... A cure for wrackspurts would be the talk of the magical world...", "wide", "default", "angry", "default") 
    m "Yes..."
    call luna_main("So what does this technique involve?", "wink", "default", "sad", "default") 
    m "It involves you sucking the nasty things out."
    call luna_main("Sucking them out!", "wide", "default", "mad", "open_wide") 
    m "(I wasn't sure if she'd fall for th-)"
    call luna_main("That's brilliant!", "closed_happy", "default", "default", "open") 
    m "..."
    m "It is?"
    call luna_main("Of course!", "default", "left", "sad", "default") 
    call luna_main("Everyone knows wrackspurts can't survive in someone's stomach!", "closed_happy", "default", "default", "default") 
    m "Very good Miss Lovegood... I see you know your... magic..."
    call luna_main("Mhmm! it also allows you to just sit there and let me take get rid of them!", "seductive", "down", "default", "default") 
    m "You expect me to just sit here while you suck them out?"
    call luna_main("Mhmm!", "closed_happy", "default", "default", "default") 
    m "And you want that?"
    call luna_main("Only if it's not too much trouble sir, I know you must be busy...", "wink", "right", "sad", "upset") 
    m "No trouble at all..."
    call luna_main("Hooray!", "wide", "empty", "default", "default") 
    call luna_main("Now how's this secret technique work?", "wink", "default", "raised", "default") 
    m "Seeing as how you offered to do this while I was sitting, why don't you come over here."
    call luna_main("Can I hide under your desk?", "default", "default", "default", "default") 
    m "You don't have to, I can turn the chair around."
    call luna_main("Oh no, I want to...", "wink", "right", "sad", "default") 
    call luna_main("I've always been rather fond of small spaces like that ever since I was a little girl...", "default", "down", "sad", "default") 
    call luna_main("I used to hide in the roots of a huge Wiggentree near our home...", "seductive", "down", "sad", "talk") 
    call luna_main("I've never felt as safe as I did when was under the roots of that tree...", "closed_happy", "default", "default", "default") 
    call luna_main("It's like the wood wrapped around to hug me when it was cold...", "seductive", "right", "default", "default") 
    call luna_main("...", "seductive", "down", "sad", "default") 
    m "..."
    m "If you want to crawl under the desk feel free..."
    call luna_main("Thank you sir...", "closed_happy", "default", "default", "default") 
    show screen blkfade
    with d3
    hide screen luna
    ">With that, Luna quickly walks around your desk and crawls under your spacious desk..."
    m "Are you ok down there?"
    $ ccg_folder = "luna_desk"
    $ ccg1 = "1"
    $ ccg2 = "blank"
    $ ccg3 = "blank"
    show screen ccg
    hide screen blkfade
    with d3
    lun "My goodness... I've never seen so much..."
    m "Oh yeah... that..."
    $ ccg1 = "2"
    lun "There's more magic in here than under my Wiggentree!"
    m "Wait..."
    m "Magic?"
    $ ccg1 = "3"
    lun "Can't you feel it sir?"
    $ ccg1 = "4"
    lun "It's so heavy in the air... It's {b}all{/b} over the wood..."
    $ ccg1 = "5"
    lun "You can almost taste it..."
    ">With that Luna takes a deep breath in of the air under your soiled desk..."
    $ ccg1 = "6"
    lun "Wow..."
    m "Are you sure you're OK down there? I haven't cleaned it since... well... ever..."
    lun "I'm... great..."
    $ ccg1 = "7"
    lun "Now..."
    ">Luna takes another deep breath..."
    $ ccg1 = "8"
    lun "Are you ready to teach me this new technique?"
    m "(She's gotta be in on this... No one is this oblivious...)"
    m "Certainly!"
    m "(Still, better not to look a gift horse in the mouth...)"
    m "Speaking of mouths, you'll need to open yours..."
    $ ccg1 = "9"
    lun "OK!"
    $ ccg1 = "10"
    lun "Agh..."
    m "..."
    menu:
        "-Take your cock out-":
            ">While the naive young blonde sits under your desk you decide it's finally time for her to get to work."
            ">You slowly pull your hardening cock from out under your robe."
            $ ccg1 = "11"
            lun "..."
            $ ccg1 = "12"
            lun "{size=-7}wow...{/size}"
            m "Now this special technique requires you suck those nasty little critters out of the affected area..."
            m "For me that's right here..."
            ">You give your thick cock a lazy stroke to emphasize."
            $ ccg1 = "13"
            lun "Is there any way in particular that you want me to suck it?"
            m "Imagine it's a tasty lollipop..."
            m "Just don't bite it."
            $ ccg1 = "14"
            lun "Ok then!"
            ">Without any further delay, Luna hops forward to take the head of your cock in her mouth."

        "-Shove it in her mouth!-":
            m "Open wide!"
            $ ccg1 = "15"
            lun "Aghhhh..."
            ">As the naive blonde kneels under your desk with her mouth open wide, you decide to reward her eagerness..."
            ">You quickly slip your hard clock from between your robes and into the girls warm mouth."

        "-Make her take it out-":
            m "Now, seeing as how I'm a little tired..."
            m "Why don't you open my robe and pull out the 'affected area'..."
            $ ccg1 = "9"
            lun "Of course sir..."
            ">Luna reverently opens your robe and softly withdraws your hard cock."
            $ ccg1 = "12"
            lun "What do you..."
            $ ccg1 = "13"
            lun "What now sir?"
            m "Put the tip in your mouth and Imagine it's a tasty lollipop..."
            m "Just don't bite it."
            $ ccg1 = "14"
            lun "Mhmm!"
            $ ccg1 = "15"
            lun "Ok then!"
            ">Without any further delay, Luna hops forward to take the head of your cock in her mouth."
    $ ccg1 = "16"
    ">Luna begins sucking in earnest as her tongue starts darting along the underside of the head of your sensitive cock at a blistering pace."
    $ ccg1 = "17"
    g4 "By the gods girl!"
    $ ccg1 = "18"
    lun "Hee howhng howng? (Is something wrong?)"
    ">Luna somehow manages to form her muffled response without once slowing her tongue."
    g4 "N-no, of course not... You're doing great..."
    $ ccg1 = "19"
    lun "Hi hm? (I am?)"
    g4 "yes..."
    $ ccg1 = "20"
    lun "Hnnk hoo hrr! (Thank you sir!)"
    ">In response to your misguided praise, Luna's tongue seems to increase in speed."
    g4 "Argh..."
    $ ccg1 = "17"
    lun "(Those wrackspurts must really be affecting him...)"
    $ ccg1 = "21"
    lun "(I better try even harder!)"
    g4 "Would you please slow down miss lovegood!"
    $ ccg1 = "13"
    ">Luna takes your cock out of her mouth."
    g4 "Ah...."
    $ ccg1 = "12"
    lun "Was I doing a bad job sir?"
    m "You were just going a little-"
    $ ccg1 = "22"
    lun "I knew I was hurting you!"
    $ ccg1 = "23"
    lun "Maybe we should stop this?"
    m "What? Gods no!"
    $ ccg1 = "24"
    lun "But wasn't I doing it wrong?"
    m "Of course not..."
    $ ccg1 = "25"
    lun "Why did you ask me to slow down then?"
    m "I didn't... It was those nasty wrinklespores!"
    m "They must have made me say it so you'd leave them alone..."
    $ ccg1 = "26"
    lun "Those tricky little..."
    $ ccg1 = "13"
    lun "Don't worry sir, I'll have them out in no time!"
    ">With that, Luna begins her tongue lashing of your cock anew."
    $ ccg1 = "21"
    g4 "A-Ah..."
    g4 "G-good work miss lovegood..."
    $ ccg1 = "27"
    lun "Hnnk hoo hrr! (Thank you sir!)"
    show screen blkfade
    with d3
    $ ccg1 = "28"
    ">Over the next hour, Luna continues to hide under your desk as she relentlessly assaults your cock."
    ">She has an uncanny ability to tell when you're about to cum and slows to a halt every time..."
    hide screen blkfade
    with d3
    g4 "I-I think this is it... again..."
    lun "Hmmmm... (Hmmmm...)"
    $ ccg1 = "17"
    lun "Hhhoohhyyy! (OK!)"
    m "Oh thank-"
    ">Before you can finish your sentence Luna suddenly thrusts her head forward, forcing your cock down the blondes waiting throat."
    $ ccg1 = "29"
    g4 "OH GODS!"
    g4 "HERE IT CUMS!"
    ">You grab the desk to steady yourself as your balls begin to contract and fire out one of the largest loads of your life."
    $ ccg1 = "30"
    lun "!!!"
    g4 "Oh fuck... fuck yes!!!"
    $ ccg1 = "31"
    ">Your cock continues to fire shot after shot down her throat and into her stomach."
    ">Eventually this proves too much for the young girl, forcing her to pull back off until your cock rests in her mouth-"
    $ ccg1 = "32"
    ">Causing your cum to start firing directly into the poor girls mouth, quickly filling her cheeks and firing out her nose..."
    $ ccg1 = "33"
    lun "{size=+10}!!!{/size}" 
    g4 "FUCK YES!!!"
    $ ccg1 = "34"
    ">The sheer force of your orgasm causes white dots to scatter across your vision as it finally dies off..."
    $ ccg1 = "35"
    ">In the afterglow of your titanic enjoyment, all that can be heard is Luna slowly slurping up your cum under the desk."
    show screen blkfade
    with d3
    ">Once done, she Eventually decides to crawl out from underneath your desk..."
    hide screen ccg
    hide screen blkfade
    with d3
    call luna_main("Those nasty wrackspurts sure were giving you trouble weren't they sir?", "seductive", "default", "sad", "default") 
    m "yeah... sure..."
    call luna_main("Well if they bother you again just let me know!", "closed_happy", "default", "default", "default") 
    call luna_main("Getting all of them out was a bit of a struggle...", "doubtful", "right", "sad", "talk") 
    call luna_main("But I think we did it!", "closed_happy", "default", "default", "default") 
    m "You sure did..."
    m "Now if you don't mind Miss granger..."
    call luna_main("Lovegood sir...", "wink", "default", "sad", "pout") 
    m "Right, right... miss love...good..."
    m "This run in with those... things... has left me rather exhausted..."
    call luna_main("Oh...", "wide", "default", "default", "talk") 
    call luna_main("Of course sir! I best be off to divination class anyway...", "default", "right", "sad", "default") 
    call luna_main("Just make sure you let me know if you need any help with those wrackspurts again!", "seductive", "default", "sad", "default") 
    call luna_main("(I can't believe they taste so good...)", "seductive", "empty", "sad", "default") 
    m "You'll be the first to know."
    call luna_main("Thanks sir! Have a nice day!", "closed_happy", "default", "default", "default") 
    ">With that, Luna turns and merrily skips out of your office."
    hide screen luna_chibi
    hide screen luna
    with d3
    m "..."
    jump day_main_menu



    



label luna_reverted_event_4: #Luna gentle BJ for anout 9 hours and 14 orgasms from Genie (Soggy is working on an underdesk background for the Luna BJ CG)

label luna_reverted_event_5: #Luna regular BJ for about 5 hours with Luna masturbating the whole time

label luna_reverted_event_6: #Luna BJ with Hermione interrupting

label luna_reverted_event_7: #Luna sex

label luna_reverted_event_8: #Luna sex with daddy roleplay

label luna_reverted_event_9: #Luna sex with Hermione












