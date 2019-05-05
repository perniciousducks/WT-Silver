

label hat_intro:
    $ hat_known = True
    who2 "Hey."
    m "What? who said that?"
    menu:
        "-Look behind you-":
            ">You turn around and look in the general direction of the voice."
            m "There's no one there..."
            who2 "..."
            who2 "You're looking straight at me Dumbledore."
        "-Look under the desk-":
            ">You take a quick look under your desk."
            m "There's no one there..."
            who2 "......"
            who2 "Behind you."
            ">You turn around."
            g4 "Who's there?! {p} Show yourself!"
            who2 "You're looking straight at me Dumbledore."
    hat "Or should I say Genie."
    g4 "(The hat is talking!)"
    m "(Wait, is it supposed to talk? Is this normal?)"
    m "What do you want...{p} hat?"
    hat "I'm the {size=+5}sorting{/size} hat, and I Just want to talk."
    m "Well go ahead then, it's not like I've got anything better to do in this room."
    hat "So, about what you've been doing to Hermione Granger..."
    m "Oh, that, Ummmmmm... It's not what it-"
    hat "I want in."
    g4 "What?"
    hat "I want to help you corrupt another girl."
    m "Another girl?"
    hat "Well it wouldn't be much fun messing around with the Granger girl anymore, she's too far gone."
    m "so What's in it for you hat?"
    hat "Entertainment. Do you understand how boring it is to sit in this room all day, staring at the wall with nothing to do..."
    m "..."
    hat "Oh yeah... Well, you should appreciate my offer to fight off the boredom for you then."
    m "And how do you plan to \'corrupt a girl\' from up there on the shelf?"
    hat "I'm the sorting hat, I sort people."
    m "..."
    m "And how does that help?"
    hat "Well, normally I'm placed on student's heads at the beginning of the year."
    hat "I then read their personality using Legilimency to decide what house they go in."
    m "And how does that help us?"
    hat "Well, I can do more than just read personalities, I can alter them as well."
    g9 "Really?"
    hat "Well I mean in theory... The real Dumbledore never let me try it out. Not even on \'him\'."
    g9 "So you're saying if I get a student in here you can turn them into whatever I want?"
    hat "To an extent."
    m "What's that supposed to mean?"
    hat "I can change what house they're in, and their personalities will change to suit that, but I can't completely alter a person's mind."
    m "So I still have to do all the hard work?"
    hat "If you call sexually harassing teens hard work..."
    m "I'll think about it."
    hat "Go ahead, I'm sure you'll have plenty of time to think it over while you sit there by yourself..."
    hat "But... {p}if you want to have some real fun, get that brat Miss Granger to bring one of her slutty little friends up here."
    hat "then you put me on their head and we'll have some fun."
    hat "Until then..."
    m "What?"
    hat "{size=+5}z{/size}{size=+4}z{/size}{size=+3}z{/size}{size=+2}z{/size}{size=+1}z{/size}"
    m "Oh..."
    return


label hat_intro_2: #Bringing in Hermione
    m "[hermione_name], I wanted to talk to you about something."
    call her_main("Whats that [genie_name]?","open","base")
    m "Do you feel that any of your friends are in the wrong house?"
    call her_main("What do you mean In the wrong house?","soft","base")
    m "well, do you know anyone who'd be better suited being in a different house?"
    call her_main("That's a weird question [genie_name].","open","base")
    call her_main("I suppose that Neville Longbottom isn't very courageous, Maybe he'd be better off in \"Hufflepuff\"...","open","suspicious")
    m "(Probably don't want him...)"
    m "Anyone else come to mind?"
    call her_main("I don't think so...","open","worriedL")
    m "Oh well, just-"
    call her_main("Wait, I know! Luna Lovegood!","scream","angryCl")
    m "And why is that?"
    call her_main("Well, surely you've seen her grades [genie_name]...","open","closed")
    call her_main("Suffice to say, she's hardly \"Ravenclaw\" material. She'd probably be better suited to \"Hufflepuff\" as well.","annoyed","suspicious")
    m "Fantastic. Could you please tell her to come to my office later this afternoon?"
    call her_main("Why? You're not going to ask her for favours are you?","annoyed","annoyed")
    m "Nothing of the sort. This is strictly school business."
    call her_main("...","annoyed","annoyed")
    call her_main("Fine... Just don't do anything too bad...","annoyed","suspicious")
    m "Scouts honor!"
    call her_main("Well if that's all then, [genie_name], I better head to class.","open","closed")

    call her_walk(action="leave", speed=2.5)

    jump end_hermione_event


label hat_intro_3: #Luna change scene #DONE
    $ lun_hair_style = "playful"
    call update_lun_uniform

    call play_sound("knocking")
    "*knock* *knock* *knock*"

    lun "It's Luna Lovegood, sir..."
    m "come in, come in..."

    call play_sound("door")
    call lun_walk("door","mid",2)
    pause.5

    call lun_main("Hermione said you wanted to see me?","normal","base","base","R",xpos="right",ypos="base")
    m "Yes. It's about your school house."
    call lun_main("Ravenclaw?","normal","base","raised","mid")
    m "Yes. I've been speaking with the sorting hat recently and I've been worried that he may have gotten a few student's houses wrong over the years."
    call lun_main("Really? So am I going to have to change house?","upset","base","sad","mid")
    m "Of course not!"
    call lun_main("*Phew*!","base","happyCl","base","mid")
    menu:
        "-Let the hat mess with her-(Slytherin Luna Path)":
            pass
        "-Let her go-(Regular Luna Path)":
            $ luna_reverted = True
            m "Actually, on second thought, I better not put the hat on."
            call lun_main("Oh... Why not?","base","wink","sad","mid")
            m "Well, if I let you change house then half the school will probably want a second go."
            m "Better to keep the status quo."
            hat "Wait, I don't get to-"
            ">You slam the hat into a draw in your desk to silence it."
            call lun_main("oh, alright then!","base","base","base","R")
            call lun_main("But seeing as how I'm already here ,sir, I need to talk to you.","base","base","base","mid")
            m "You do?"
            m "(Maybe this won't be a waste of time after-all!)"
            call lun_main("It's about the school being in great danger!","open","wide","angry", "mid")
            m "Oh..."
            m "In that case, you'll have to come speak to me later."
            call lun_main("Oh, um alright then... You must be very busy at the moment!","base","wink","sad","R")
            m "Yeah, busy..."
            m "(Too busy to hear about something that dull.)"
            call lun_main("I'll come back later then, this really is something you nead to hear about!","base","closed","angry","R")
            call lun_walk("mid","leave",2)
            $ luna_busy = True

            $ luna_unlocked = True
            $ achievement.unlock("unlocklun")

            return

    m "I just wanted to put the hat on your head to see if he made the right choice."
    call lun_main("oh, alright then!","base","base","base","R")
    ">You turn around and reach for the hat."
    m "Almost there... Just grab the edge of it..."
    hat "Careful!"
    ">You pull the heavy hat down of the cupboard."
    hat "*Psst*{size=-5}Nice work! Now just put me on her head.{/size}"
    m "Here we are Miss Lovegood..."
    ">You place the hat gingerly on her head."
    call lun_main("...","upset","base","base","R")
    call lun_main("Is it-","upset","base","raised","R")
    hat "{size=+5}HMMMM{/size}yes... {size=-5}yes...{/size} I see. Very interesting... {size=+5}Very{/size}{p} {size=+5}interesting...{/size}"
    call lun_main("What's interesting?","normal","base","raised","mid")
    hat "What? Oh nothing, nothing. Just close your eyes, try and get a bit of sleep..."
    call lun_main("Sleep?","normal","suspicious","raised","R")
    call lun_main("Why would I... want{p} to...","normal","closed","sad","mid")
    call lun_main("...","normal","base","sad","empty")
    m "is she alright?"
    hat "She's fine. Just having a bit of a rest. Now about that personality..."
    hat "Oh yes... Hmmmm, {p}well I suppose that could work..."
    hat "{size=-5}yes... I'm sure salazar would be proud...{/size}"
    hat "Just a little longer..."
    call lun_main("...","normal","base","sad","empty")
    call lun_main("...","normal","base","base","empty")

    # Pupil color change.
    hide screen luna_main
    $ luna_pupil_color = "green"

    call lun_main("...","normal","base","base","empty")
    m "Wait what happened?! Her eyes just changed color!"
    hat "Really? Hmmm... didn't expect that... what color are they?"
    m "Green."
    hat "Well, that seems rather fitting."
    m "Why, what did you do to her personality?"
    hat "Not much, just made it a bit more Snake like..."
    m "What now."
    hat "Well she's going to be a little... out of sorts..."
    hat "It would probably be in your best interests to send her to her room and let her sleep it off."
    m "Will she be able to hear me?"
    hat "Yes, she's in a fairly... lucid state..."
    ">You take the hat off of Luna's head."
    m "Thank you very much Miss Lovegood. I think you better be off to bed now "
    call lun_main("yes... bed...","normal","base","base","empty")

    call lun_walk("mid","leave",2)

    $ luna_wear_accs = False
    $ lun_hair_style = "curly"

    call nar(">You place the hat back on the cupboard")
    m "So what did you do to her personality?"
    hat "Now now... no sense ruining the fun. You'll just have to wait..."
    m "Hmmph"

    $ luna_unlocked = True
    $ achievement.unlock("unlocklun")

    $ luna_busy = True

    return

###Need another intro event here, introducing Luna and setting up the favour selling stuff.




### Luna Reverted Intro ###
# Skip the hat's request to hypnotise her for this event to happen.
# Event also happens when you follow Luna's sub path.

label luna_reverted_greeting_1: #reverted Luna explains the wrackspurt problem

    $ days_to_luna = 3
    $ lun_whoring = -1 #Triggers event during the evening.

    #Reset Luna Model
    call reset_luna_base
    call reset_luna_clothing

    $ lun_hair_style = "playful"
    $ luna_pupil_color = "blue"
    $ luna_l_arm = 1
    $ luna_r_arm = 2

    $ lun_glasses = "spectrespecs"
    $ luna_wear_glasses = True
    $ lun_request_wear_glasses = True

    call reset_luna

    $ lun_genie_name = "Professor" #reset genie's name with Luna
    $ luna_name = "Miss Lovegood" #reset luna's name with genie



    ### Start ###

    call play_sound("knocking")
    "*Knock* *Knock* *Knock*"
    lun "Hello?"
    m "(Sounds like Luna...)"

    menu:
        "-Let her in-":
            m "Come in!"

        "-Tell her to go away-":
            m "(She's probably here because of that thing with the hat!)"
            m "Ugh... I'm not here!"
            lun "..."
            call nar(">Your door opens as Luna walks in.")

    call play_sound("door")
    call lun_walk("door","desk",2.7)
    pause.5

    call lun_main("Hello...","base","base","sad","mid",xpos="mid",ypos="base")
    m "Hello, miss lovegood."

    $ luna_l_arm = 1
    $ luna_r_arm = 1
    call lun_main("...","base","base","sad","R")
    call lun_main("......","normal","base","sad","down")
    call nar(">Luna starts looking around your room.")
    call lun_main("There's such a strange aura in here...","normal","suspicious","angry","R")
    call lun_main("It's like a big hollow tree...","normal","base","sad","R")
    m "..."
    m "(What?)"
    m "Can I help you with anything?"
    call lun_main("Oh... there was something I came here for, wasn't there...","upset","base","sad","down")
    m "(What's going on here?)"
    call lun_main("I remember! The wrackspurt infestation!","base","happyCl","sad","R")

    menu:
        "\"Wrackspurts?... Is that some sort of wizard STD?\"":
            call lun_main("Hahaha, I guess you could say that! ","base","base","sad","R")
            call lun_main("Wrackspurts are invisible creatures which floats into a person’s ear and make their brain go all fuzzy.","normal","base","sad","mid")
            $ luna_l_arm = 2
            call lun_main("You can only view them wearing these spectrespecs!","base","base","base","L")
            $ luna_l_arm = 1
            m "I see... (This bitch really is crazy!)"
            m "(Maybe the hat did some good for her...)"
            m "Well, Miss Lovegood, what can we do about it?"
            call lun_main("I'm not sure, professor... Normally, thinking positive thoughts is enough to remove them, but I am having trouble with these. If my father, Xenophilius-","normal","angry","sad","R")
            "*Genie jumps from the table*"
            g4 "DID YOU JUST CAST A SPELL ON ME?!"
            $ luna_l_arm = 2
            $ luna_r_arm = 2
            call lun_main("Sir?","upset","wide","sad","mid")
            g4 "EXPLAIN YOURSELF!"
            $ luna_l_arm = 1
            $ luna_r_arm = 1
            call lun_main("I am sorry Sir, I am not sure what-","normal","wide","sad","R")
            g4 "XENOFIUS! What does it do?"
            call lun_main("Xenofius? I’ve not heard of that spell before, Sir.","normal","angry","sad","mid")
            m "The spell... That you just... Never mind."
            call lun_main("(A Secret spell?) Sir, your magic is the strongest there is and these wrackspurts are really getting to me.","upset","mad","sad","R")
            m "I see... do go on."
        "\"I am afraid I can’t help you Miss Lovegood.\"":
            call lun_main("Oh please, Sir! You’re the only one powerful enough to help.","open","wide","sad","mid")
            "*You can see Luna is rocking her pelvis as if grinding the air*"
            m "Miss Lovegood, I am afraid I don’t know what a wrackspurt is, let alone how to cure it."
            call lun_main("Well, professor; wrackspurts are detailed on page 6 of The Quibbler! Here!","normal","base","sad","mid")
            "*Luna hands you a Quibbler*"
            m "*Reading* “Rotfang conspiracy... 300 ways to tie up a ghost... “ Ah! Wrackspurts..."
            "\"Invisible creatures which float into a person’s ears, making his/her brain go fuzzy\""
            "*Luna points to her spectrespecs* "
            call lun_main("I can see them, Sir.","base","happyCl","base","mid")
            m "I see...(No wonder Hermione called her Loony Lovegood)."
        "\"What in Agrabah are you wearing?\"":
            call lun_main("Oh! These are my spectrespecs, professor!","base","base","sad","crossed")
            m "(Please don’t be mind-reading, please don’t be mind-reading-)"
            call lun_main("They help me see the wrackspurts.","normal","base","sad","mid")
            m "(Thank the great desert sands!)"
            call lun_main("And these are my plum earrings.","base","base","sad","L")
            m "Ah yes, very nice...{w} Wait, did you say Plumb earrings?"
            call lun_main("Why yes.","normal","base","sad","mid")
            m "I see, I thought I misheard you for a second."
            m "So about these wrecksputs..."

    call lun_main("Yes, Sir, they’re proving to be quite a pain.","normal","closed","sad","mid")

    "*Luna is visibly grinding her pelvis against her thighs.*"
    m "(Is she really?... Ohhh). Miss Lovegood, how exactly do these wickspurts make you feel?"
    call lun_main("They're Just like the quibbler says sir, except...","normal","seductive","sad","R")
    m "Go on..."
    call lun_main("Well, it's not my brain they're making fuzzy.","soft","seductive","sad","down")
    m "Where exactly is fuzzy, Miss Lovegood?"
    call lun_main("Umm... I'm not sure if I can say...","normal","seductive","sad","R")
    m "(YES!)"
    m "Now now, Miss Lovegood, as your headmaster there shouldn't be anything that you can't discuss with me."
    call lun_main("Well, okay...","base","seductive","sad","down")
    call lun_main("the fuzziness is in between my legs, sir...","base","seductive","sad","mid")
    m "Really? That seems quite strange..."
    call lun_main("It is, sir! I've only ever heard of people's brains going fuzzy...","normal","base","sad","mid")
    call lun_main("But this...","normal","angry","sad","mid")
    call lun_main("It's like this unbearable itch I can't scratch...","upset","seductive","sad","down")
    m "(I know that feeling.)"
    call lun_main("And I feel like I can't quite remember what I've been up to over the last few days...","normal","suspicious","sad","R")
    m "Oh um... I wouldn't worry about that at all..."
    m "Let's just focus on this fuzziness of yours."
    call lun_main("... Alright, professor.","normal","seductive","sad","down")
    call lun_main("As I was saying, this fuzziness has really been bothering me the last few days...","normal","seductive","sad","mid")
    m "Hmmm... Has it been affecting your studies at all?"
    call lun_main("Yes it has, sir...","upset","seductive","sad","down")
    m "Well, we can't have that now, can we?"
    call lun_main("No, sir...","base","seductive","sad","mid")
    m "Are you free at the moment?"
    call lun_main("Umm... I'm about to go to divination class, sir...","normal","seductive","sad","down")
    m "In that case, we can address that nasty itch of yours later."
    m "Come to my office later tonight, and we'll see what we can do."
    call lun_main("Oh, thank you, sir!","base","wide","sad","mid")
    call lun_main("I can't wait!","base","seductive","sad","mid")
    call lun_main("Do you think you could possibly stop the nargles stealing my shoes as well?","base","base","sad","down")
    m "(The hell is a nargle?)"
    m "One step at a time, Miss Lovegood."
    call lun_main("Yes, you're right... the nargles wouldn't like it if we were multitasking...","normal","closed","sad","mid")
    m "..."
    call lun_main("Well, I'd best be off... goodbye professor!","base","happyCl","base","mid")
    "*Luna skips out of the room, squeezing her legs together as she prances*"
    m "(This is going to be fun!)"

    jump luna_away



label luna_reverted_greeting_2: #Explaining to Luna what will happen or something #DONE
    $ lun_whoring = 0

    call play_sound("knocking")
    "*knock* *knock* *knock*"
    m "Come in..."

    call play_sound("door")
    call lun_walk("door","mid",2)
    pause.5

    call lun_main("Hello, Sir...","base","happyCl","base","mid",xpos="right",ypos="base")
    m "Miss Lovegood. So, Did the wickerspats leave you alone today?"
    call lun_main("Not at all! They were worse than ever!","upset","base","angry","R")
    m "Really?"
    call lun_main("Really, sir. And I don't think it's just me they're affecting either.","normal","base","sad","mid")
    call lun_main("I fear the whole school is becoming overrun!","normal","wide","sad","mid")
    m "What makes you say that?"
    call lun_main("The way people are acting...","normal","angry","sad","R")
    call lun_main("It's very strange, don't you think sir?","upset","angry","sad","mid")
    m "(Like this crazy bitch can call anyone strange!)"
    m "Strange how?"
    call lun_main("it's Their auras sir!","normal","closed","sad","R")
    m "Oh..."
    call lun_main("They're far too red!","normal","angry","sad","mid")
    m "Too red?"
    call lun_main("I'm afraid so...","upset","angry","sad","R")
    m "And you think these wackspots are to blame?"
    call lun_main("I'm not sure...","normal","seductive","sad","down")
    call lun_main("According to my father's beastiaries, they should only ever produce a grey tinge to an aura...","normal","seductive","sad","R")
    call lun_main("For them to be making auras red...","upset","wide","sad","down")
    call lun_main("It could be very dangerous!","normal","wide","sad","mid")
    m "(Pffft... auras...)"
    m "Yes, I see how that could be dangerous..."
    call nar("*Luna starts grinding her thighs together.*")
    call lun_main("yes...","base","seductive","sad","down")
    call lun_main("So, about this itch, sir...","base","seductive","sad","mid")
    m "Yes."
    call lun_main("Did you say you had some way to get rid of it?","normal","seductive","sad","mid")
    m "I did."
    call lun_main("Well...","upset","seductive","sad","R")
    m "First thing's first, I need something from you, Miss Lovegood."
    call lun_main("Something from me?","pout","wide","sad","mid")
    m "Yes, I need a promise."
    call lun_main("Oh...","normal","base","sad","R")
    call lun_main("Alright then!","base","happyCl","sad","mid")
    m "I haven't even told you what it is yet."
    call lun_main("Don't worry sir, I trust you!","base","wide","base","mid")
    m "(This might be too easy even!)"
    m "Yes... the techniques I'm going to be showing you are proprietary so I'm going to have to make you promise not to talk to anyone about what goes on in this room."
    call lun_main("Techniques...","normal","seductive","sad","R")
    call lun_main("Proprietary...","upset","seductive","sad","down")
    call lun_main("I'm not sure I understand, sir.","normal","seductive","sad","mid")
    m "Well, if what you're saying is correct, even if I use some powerful magic to remove them..."
    m "(I hope she buys this...)"
    m "They'll soon be back, and in greater numbers."
    call lun_main("...","normal","seductive","sad","R")
    m "(Did she buy it?)"
    call lun_main("Yes, You're right, sir.","normal","closed","sad","R")
    m "(YES!)"
    call lun_main("But are there really techniques to dispell them?","normal","seductive","raised","mid")
    m "There are, but as I said, if you want to learn them you'd have to promise not to tell anyone what happens here."
    call lun_main("I suppose that's only fair, This information would be worth more than a snorkack sighting!","base","base","sad","mid")
    m "..."
    m "It's Not just the techniques Miss Lovegood."
    m "You must promise not to tell anyone anything about what happens in this room, no matter what."
    call lun_main("But...","normal","seductive","sad","R")
    call nar("*You can see Luna is awkwardly rocking her pelvis*")
    call lun_main("*Nngh*- Alright then...","base","seductive","sad","mid")
    call lun_main("I solemnly swear that I will tell no one what happens within these hallowed walls...","normal","closed","base","R")
    m "Fantastic!"
    call lun_main("So, can you please teach me the techniques sir?","base","wide","sad","mid")
    call nar(">There's a desperate need in Luna's eyes that excites you to no end.")
    m "Yes, yes. I think I've made you wait long enough."
    call lun_main("Thank you so much!","base","happyCl","base","R")
    m "No need to thank me, Miss Lovegood, I'm simply doing what any good teacher should."
    m "Now, stand in the middle of the room for me."
    hide screen luna_main
    with d3

    call lun_main("Is Here okay?","pout","base","sad","mid",xpos="mid",ypos="base")
    m "Perfect."
    m "Before we begin I have to explain a few things."
    call nar(">Luna stares at you intently.")
    call lun_main("...","normal","angry","sad","mid")
    m "From what I can tell these rockspits seem to have infected an unusual part of your body."
    call lun_main("Yes... Normally they only make your head fuzzy.","pout","angry","sad","R")
    m "And how do you get rid of them in that situation?"
    call lun_main("By thinking positive thoughts, sir...","base","happyCl","sad","R")
    m "Correct."
    m "So, in your current situation, you simply need to focus positive thoughts on the affected area."
    call lun_main("...","normal","base","raised","R")
    call lun_main("How do I do that?","upset","base","sad","mid")
    m "We'll try some self-applied massage to the area to start with."
    call lun_main("So I just start massaging the area that they're making fuzzy?","soft","base","sad","mid")
    m "That's correct, I'll be here to give you some guidance."
    call lun_main("Thank you, Sir!","base","happyCl","sad","R")
    m "You're quite welcome."
    call lun_main("...","base","base","sad","down")
    $ luna_l_arm = 4
    call nar(">Luna quickly puts her hand down her skirt, barely acknowledging the nature of her actions.")
    call lun_main("Ah...","normal","seductive","sad","down")
    m "Is everything alright, Miss Lovegood?"
    call lun_main("Ah...{w=0.3} of course!","base","wide","sad","mid")
    call lun_main("It's just a little sensitive...","base","seductive","sad","down")
    m "That's to be expected. Keep going."
    call lun_main("Ah...{w=0.3} yes sir...","normal","happyCl","sad","R")
    g4 "..."
    call lun_main("Ah...{w=0.3} is this how it should be done?","pout","base","sad","mid")
    m "As long as it's feeling good I'm sure it's working. If you keep this up I'm sure you'll be rid of those nasty wickerspoons."
    call lun_main("That's nice...","base","closed","sad","R")
    call lun_main("...","normal","base","sad","mid")
    call lun_main("Are you sure this will work, sir?","soft","seductive","sad","mid")
    m "Of course I am! Do you dare doubt the powerful Dumbelldoor?"
    call lun_main("Certainly not, sir...","normal","wide","sad","R")
    call lun_main("It's just...","normal","seductive","sad","down")
    call lun_main("I'm not sure this is going to get rid of them...","pout","seductive","sad","mid")
    m "What makes you say that?"
    call lun_main("Do you remember how I said the wickerspats were like a nasty itch, sir?","normal","seductive","sad","R")
    m "I do."
    call lun_main("As nice as this massage feels...","normal","seductive","sad","down")
    call lun_main("It's not really scratching that itch sir...","pout","angry","sad","mid")
    call lun_main("... {p}am I doing it wrong, sir?","normal","seductive","sad","mid")
    m "Certainly not, but this is worse than I feared."
    call lun_main("really?","normal","wide","sad","mid")
    m "Yes. It would seem that those nasty critters are trying to hide."
    call lun_main("Hide? Where?","normal","wide","sad","down")
    m "Well, as long as you're still feeling that itch they can't have gone far."
    m "But this means you'll have to chase them down."
    call lun_main("Chase them down?","normal","seductive","raised","mid")
    m "Don't worry, I'll be here to guide you through it."
    call lun_main("Thank you, sir.","base","base","sad","R")
    m "First things first, close your eyes."
    call lun_main("...","normal","happyCl","sad","R")
    m "Very good. Now I want you to block everything else out."
    call lun_main("Alright, sir...","upset","happyCl","sad","R")
    m "Imagine it's just you, alone in your room."
    call lun_main("Yes...","normal","happyCl","sad","R")
    m "Nice and cozy. Not a care in the world."
    call lun_main("...","base","happyCl","sad","R")
    m "Now, focus on where the itch is strongest."
    call lun_main("Ah...{w=0.3} Alright...","base","happyCl","base","R")
    m "I want you to chase that feeling with your fingers."
    call lun_main("...","normal","happyCl","base","R")
    m "Focus on catching it."
    call lun_main("I can't...","pout","happyCl","sad","R")
    call lun_main("It's like trying to grab rays of sunlight...","normal","happyCl","sad","R")
    m "Don't try to grab a hold of it, just brush against it with the tips of your fingers."
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("...","base","happyCl","base","R")
    call nar(">Luna starts dancing her fingers along under her skirt.")
    call lun_main("Ah...","base","happyCl","sad","R")
    call lun_main("Mmm...","grin","happyCl","sad","R")
    call nar(">Luna starts to softly moan under her breath.")
    call lun_main("I'm close sir...","base","happyCl","sad","R")
    m "Good. Just keep your eyes closed and focus on your fingers."
    call lun_main("{image=textheart}","grin","happyCl","base","R")
    call lun_main("Ah... I think it's working, sir!","base","happyCl","sad","R")
    call lun_main("I think I'm about to catch it!","base","happyCl","base","R")
    m "Shhh, don't speak, just focus..."
    call lun_main("Ok...","normal","happyCl","sad","R")
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("Ah...","grin","happyCl","sad","R")
    call lun_main("{image=textheart}","base","happyCl","sad","R")
    call lun_main("...","upset","happyCl","sad","R")
    call lun_main("Ah...{w=0.3} sir...","normal","seductive","sad","mid")
    call lun_main("I think...","grin","seductive","sad","down")
    call lun_main("Ah...","grin","seductive","sad","R")
    call lun_main("I think I've almost got it...","grin","happyCl","sad","R")
    m "Shhh..."
    call lun_main("Ah...","grin","happyCl","angry","mid")
    call nar(">Luna's fingers start furiously dancing underneath her skirt.")
    call lun_main("Mmmm...","base","happyCl","angry","mid")
    call lun_main("Ah...","grin","happyCl","angry","mid")
    call lun_main("A-ah...","base","seductive","sad","down")
    call lun_main("Yes...","base","seductive","angry","mid")
    m "(I think this is it!)"
    call lun_main("Ah... ah...{image=textheart}","grin","seductive","sad","R")
    call lun_main("{size=+4}Mmm...{w=0.3} yes...{image=textheart}{/size}","base","seductive","sad","down")
    call lun_main("{size=+8}ah...{w=0.3} ah...{/size}","grin","seductive","sad","mid")
    call lun_main("!!!","grin","wide","base","empty")
    call nar(">There's a blur of movement under Luna's skirt.")
    call lun_main("Ah! I think they're attacking me, sir!","base","wide","sad","mid")
    call lun_main("!!!","base","base","sad","empty")
    m "Is everything okay?"
    call lun_main("Ah...{w=0.4} Yes sir...{image=textheart}","normal","seductive","sad","R")
    call lun_main("It's just...","base","seductive","sad","R")
    m "..."
    call lun_main("I-I've never...","normal","seductive","sad","R")
    call lun_main("...","base","seductive","sad","down")
    call lun_main("{size=-5}Ah...{/size}","base","seductive","sad","R")
    m "So, have the wickspots left you alone?"
    call lun_main("I think so, sir...","normal","seductive","sad","mid")
    $ luna_l_arm = 1
    call nar(">Luna slowly pulls her hand out from under her skirt.")
    call lun_main("At least That nasty itch seems to have gone away.","base","base","sad","mid")
    m "Fantastic! will that be all then, Miss Lovegood."
    call lun_main("OH... Did you want me to leave already, sir?","normal","seductive","sad","down")
    m "If there's nothing else I can help you with."
    call lun_main("I suppose not... but what if the feeling comes back, sir?","upset","seductive","sad","R")
    call lun_main("Should I try and get rid of them myself?","normal","seductive","sad","down")
    m "Certainly not!"
    call lun_main("Really? Why not?","normal","wide","sad","mid")
    m "Ss I said earlier miss lovegood, These techniques are to be kept secret."
    m "Not to mention dispelling them in your common room could lead to a school wide outbreak."
    call lun_main("So what can I do if they come back?","normal","base","sad","mid")
    m "If you ever feel like you need to relieve yourself of those pesky little things again, my door is always open."
    call lun_main("Are you sure, sir?","normal","seductive","sad","mid")
    call lun_main("I wouldn't want to bother you...","normal","seductive","sad","R")
    m "You'd be doing no such thing! Besides, I've been meaning to test these sort of techniques for a while now."
    m "If anything you'll be helping me with important research."
    call lun_main("Really? Thank you very much, sir.","base","wide","base","mid")
    call lun_main("Hopefully they leave me alone, but if not I'll come and visit you again.","base","base","sad","R")
    m "I look forward to it."
    call lun_main("...","base","seductive","sad","mid")
    call nar(">Luna gives you one last smile before leaving your office.")

    jump luna_away
