

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

    jump main_room


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
            $ ll_event_pause += renpy.random.randint(2, 5)
            $ luna_reverted = True
            m "Actually, on second thought, I better not put the hat on."
            call lun_main("Oh... Why not?","base","wink","sad","mid")
            m "Well, if I let you change house then half the school will probably want a second go."
            m "Better to keep the status quo."
            hat "Wait, I don't get to-"
            ">You slam the hat into a drawer in your desk to silence it."
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
            call lun_main("I'll come back later then, this really is something you need to hear about!","base","closed","angry","R")
            call lun_walk("mid","leave",2)
            $ luna_busy = True

            $ luna_unlocked = True
            $ achievement.unlock("unlocklun")

            jump main_room

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

    jump main_room

###Need another intro event here, introducing Luna and setting up the favour selling stuff.




### Luna Reverted Intro ###
# Skip the hat's request to hypnotise her for this event to happen.
# Event also happens when you follow Luna's sub path.

label luna_reverted_greeting_1: #reverted Luna explains the wrackspurt problem

    $ ll_event_pause += renpy.random.randint(2, 5)
    $ lun_whoring = 0 #Triggers event during the evening.

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
    $ lun_name = "Miss Lovegood" #reset luna's name with genie



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

    call lun_walk("desk","leave",2.5)

    call bld
    m "(This is going to be fun!)"

    jump end_luna_event
