#LETTER FROM THE MINISTRY OF MAGIC
#Dear Albus Dubmbledore, as we are sure you are aware,
#an unforgivable curse has been detected within the grounds of Hogwarts.
#While the punishment for such a curse is usually lifetime incarceration in the
#prison, Azkaban, we are allowing you to address this matter at your own discretion.
#This is due to the possible nature of the spell being cast by a minor who has not
#fully grasped the serious nature of the curse. If this is the case we expect no further communication from
#you regarding this unfortunate event. If, however, you believe the curse has been cast by someone other than a student,
#or if any other complications arise we expect direct communication. Lastly, the detection of any further curses will
#result in the immediate dispatchment of an auror to Hogwarts.

#Cornelius Fudge,
#Department Head: Improper Use of Magic Office

#m "That doesn't sound good..."
#m "Perhaps I should tell Snape about this."
#m "Or maybe miss granger?"


#TELL HERMIONE ABOUT THE LETTER #Done
label letter_intro_hermione:
    m "I received a letter not too long ago."
    call her_main("It's from the ministry of magic isn't it?!","shock","wide") #No xpos change.
    call her_main("Did they get wind of my favour trading? Please don't tell me they--","disgust","worriedCl")
    m "No no, the letter isn't about you..."
    m "It \'is\' from the ministry of magic, however."
    m "Apparently they've detected something called an \'unforgivable\' curse at the school."
    call her_main("AN unforgivable CURSE!!!","scream","wide",trans="hpunch")
    call her_main("AT out school?!","shock","wide_stare")
    call her_main("SOMEONE COULD BE DEAD!","scream","wideL")
    call her_main("OR TORTURED!!","disgust","worriedCl")
    call her_main("OR WORSE!!!","disgust","worriedL")
    m "really?"
    call her_main("Those are the only things that can happen with an unforgivable curse, [genie_name]!","angry","worried")
    m "of course... I'm just making sure you were aware of them..."
    call her_main("It's the first lesson we ever received in defense against the dark arts.","open","closed")
    m "Well, one's been cast somewhere on the school."
    m "and I need your help finding out who did it..."
    call her_main("Why do you need my help?","soft","wink")
    call her_main("Surely you're able to detect them?","base","base")
    m "Unfortunately not... I must have been... asleep... when the thing happened..."
    m "I missed my chance, so to speak..."
    call her_main("So how do you expect me to find out who did it?","soft","baseL")
    m "I'm certain that it's the work of another student..."
    m "(or Snape has finally snapped...)"
    m "so I'll need you to go undercover to find out who."
    call her_main("really? You're depending on me to find a criminal student within our school?","soft","down_raised",cheeks="blush")
    m "If it's not too much troub--"
    call her_main("I'd be honored, [genie_name]!","scream","closed")
    call her_main("It's no doubt the work of one of those despicable \'slytherins\'...","open","angryCl")
    call her_main("Nothing would give me greater pleasure than to see scum like that sent to \'Azkaban\'...","angry","angryL")
    m "And what's Azkaban?"
    call her_main("...Is this another test sir?","open","wink")
    m "Sure..."
    call her_main("Of course! I know everything about it!","smile","happy")
    call her_main("It's the prison of the damned... An impenetrable rocky outcrop surrounded by the harsh North Sea...","open","happyCl")
    call her_main("the guards are the deathly eaters of all happy thoughts and emotions known as dementors...","open","angryL")
    call her_main("They endlessly patrol the prison, devouring all hope from the prisoners, driving them mad within a few days...","open","angry")
    call her_main("Tormenting them relentlessly for the rest of their miserable lives...","grin","happyCl")
    call her_main("And the perfect place to house all those dirty \'slytherins\'!","angry","angry")

    menu:
        "(...)"
        "-just tell her to find the student-":
            m "Whatever..."
            m "just find them so we can send them to Azerbaijan..."
            call her_main("Azkaban, sir...","open","wink")
            m "Just go!"
        "-Tell her you're not going to send them to Azkaban-":
            m "By the gods, [hermione_name], what's wrong with you?"
            call her_main("What are you talking about, [genie_name]?","open","baseL",cheeks="blush")
            call her_main("Everyone knows that life in Azkaban is the punishment for casting an unforgivable curse...","open","closed")
            m "I've been given special permission to punish them as I see fit."
            call her_main("Oh...","annoyed","base")
            call her_main("So no Azkaban?","soft","baseL")
            m "Not unless they've killed someone..."
            call her_main("Really? So there's still a chance?","base","glance")
            m "Only if you find a body..."
            call her_main("yay!","smile","happyCl")

    call her_main("Consider it done, [genie_name]!","open","closed")

    call her_walk(action="leave", speed=2)

    if snape_on_the_lookout:
        m "I wonder if she'll find them before Snape..."
    else:
        m "I should probably go tell Snape as well..."

    jump main_room


#TELL SNAPE ABOUT THE LETTER #Done
label letter_intro_snape:
    m "I got some letter from the ministry of magic..."
    call sna_main("Really?","snape_03") #No xpos change.
    call sna_main("Why are you telling me?","snape_04")
    m "Apparently they've detected something called an \'unforgivable\' curse at the school..."
    call play_sound("scratch")
    call sna_main("","snape_11")
    with hpunch
    pause.2
    call sna_main("Shit... this isn't good...","snape_08")
    m "And if they detect another one they're going to send an \'auror\' or something."
    call sna_main("This really isn't good...","snape_07")
    m "Why, are the curses that bad?"
    call sna_main("Forget about the damn curses, if they send an auror here they might find out what we've been doing.","snape_10")
    m "What?"
    call sna_main("THe favour trading! Fucking our students isn't something teachers are supposed to do genie!","snape_25")
    call sna_main("If an auror finds out what's going on here we're both going to Azkaban!","snape_16")
    m "so what are we going to do?"
    call sna_main("We'll just have to make sure that no more curses are cast...","snape_01")
    m "How do we manage that?"
    call sna_main("We have to find out who's been casting them.","snape_24")
    call sna_main("Normally the real Dubmbledore would be able to detect who had cast them, but seeing as how you're here instead...","snape_06")
    call sna_main("We'll have to find them the old fashioned way.","snape_10")
    m "So you want me to launch a manhunt?"
    call sna_main("Are you crazy? We can't let anyone know what's happened. All the students will panic thinking someone's been murdered...","snape_16")
    call sna_main("It's probably just an imperio or crucio that's been cast.","snape_24")
    call sna_main("I'll start the search immediately. In the mean time, just stay here and keep yourself busy.","snape_10")
    m "You don't want my help?"
    call sna_main("Not really... With how potent your magic is you'll probably just attract more attention from the ministry and then they'll definitely send an auror.","snape_03")
    call sna_main("Don't worry Genie, I'll find that student in no time.","snape_02")

    call sna_walk(action="leave", speed=2)

    call bld
    m "Drama queen..."

    jump main_room


#HERMIONE CAPTURED ASTORIA    #Done
label astoria_captured_intro:
    call play_sound("knocking")
    "*knock* *knock* *knock*"

    m "Who is it?"
    her "It's hermione granger, sir, although,... I'm not alone."
    m "Come in."

    call her_walk(xpos="desk", ypos="base", action="enter", speed=2.7)

    call her_main("Hello sir.","normal","happy",xpos="mid",ypos="base")
    m "I thought you said you weren't alone?"
    call her_main("I'm not.","annoyed","glanceL")
    hide screen hermione_main
    hide screen bld1
    with d3
    pause.2

    call her_chibi("stand","desk",flip=True)
    pause.5

    call her_main("Get in here Astoria!","annoyed","angryL",xpos="base",ypos="base")
    ast "{size=+2}{b}No!{/b}{/size}"
    call her_main("Do you want to make this worse?","scream","closed",trans="hpunch")
    ast "no..."
    call nar(">Slowly, a small girl enters your office.")

    call her_chibi("stand","desk",flip=False)
    call her_main("","normal","angry")
    pause.2

    call play_sound("door")
    call ast_main("...","pout","base","worried","R")
    m "..."
    m "Who's this?"
    call ast_main("My name is Astoria Greengrass, sir.","disgust","base","worried","mid",xpos="mid",ypos="base")
    m "And why are you here?"
    call her_main("You asked me to bring you the person who cast the unforgivable curse sir.","soft","annoyed",xpos="close",ypos="base")
    call her_main("Here she is.","grin","angry")
    m "I thought it would be some angsty teen who listens to death metal or something..."
    m "not some little girl..."
    call ast_main("I am not a little girl!","scream","angry","angry","angry")
    m "What are you then, a 600 year old vampire?"
    call ast_main("Vampires aren't real!","pout","angry","angry","R")
    m "..."
    m "So how are you not a little girl then?"
    call ast_main("I'm older than I look!","pout","angry","angry","angry")
    m "I've heard that one before..."
    call her_main("It's true, sir. She was a cursed child, born with a frailty that affects her growth.","normal","concerned")
    call ast_main("Told you!","smile","angry","angry","R")
    m "Whatever... that still doesn't get you out of punishment."
    call ast_main("punishment? for what?","pout","wide","wide","wide")
    call her_main("You know what you did!","angry","angryCl")
    call ast_main("I never cast Imperio on anyone! I swear, sir! Hermione's just being a know-it-all tattle-tail!","pout","wide","worried","R")
    m "Miss Granger..."
    call her_main("I overheard her boasting about it to a group of slytherins in the library.","annoyed","concerned")
    call her_main("By the sounds of it she used Imperio to control another student.","annoyed","base")
    call ast_main("Did not!","worried","angry","worried","angry")
    m "Well, given the severity of the situation, I'm sure there's something we can use to get a clear answer out of you..."
    call her_main("Shall I go fetch a vial of veritaserum from professor snape, sir?","grin","base")
    call ast_main("v-veritaserum? Isn't that against the rules?","scream","wide","worried","wide")
    call her_main("Not when you've been casting unforgivable curses you evil little witch!","grin","angry")
    call ast_main("OK... I'll tell you what happened sir...","pout","closed","base","mid")
    call ast_main("But only if Hermione leaves!","pout","narrow","base","mid")
    call her_main("Not a chance!","scream","angryCl")
    m "Miss granger..."
    call her_main("professor! I think it's only fair, given that I was the one to catch her!","upset","annoyed")
    m "We'll talk about your reward later..."
    call her_main("*hmph*","annoyed","angryL")
    call her_main("Fine...","open","angryCl")
    call her_main("I'll go back to my room then...","annoyed","angryL")
    call her_main("Goodbye sir...","open","angry")
    call her_main("Goodbye Astoria...","angry","closed")


    call her_walk(action="leave", speed=2.7)

    call bld
    m "Right, well now that Hermione's gone, why don't you tell me exactly what--"

    #magic sound effect and screen shake
    call cast_spell("imperio") #Different effects for different spells.
    call ast_main("{size=+10}{b}IMPERIO{/b}{/size}","scream","angry","angry","angry")

    call blktone
    m "..."
    m "What was that?"
    call hide_blktone

    call ast_main("I just cast Imperio on you, professor! Now you have to do everything I say!","grin","narrow","base","mid")
    g4 "Did you just do it again? Another bloody curse... on me?"
    call ast_main("yes... but it should have... why aren't you...","worried","narrow","worried","mid")
    m "Ugh..."
    m "I better get Snape up here."
    call ast_main("professor snape? I command you not to!","scream","angry","angry","angry")
    m "yeah, no. I'm bringing him up here because now we're probably going to have to deal with something called an auror coming to the school."
    call ast_main("An auror?!","worried","wide","wide","wide")
    call ast_main("But they'll send me to Azkaban!","scream","wide","worried","wide")
    m "I'm sure they'll be lenient, you're only a child after all."
    call ast_main("I am not a child!","scream","angry","angry","angry")
    m "ugh... I better get Snape."

    call sna_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call play_music("snape_theme")
    call sna_main("gen- oh, I see you already have a visitor...","snape_03",xpos="base",ypos="base")
    call ast_main("...","pout","base","worried","R")
    call sna_main("Little young isn't she? even for you...","snape_09")
    m "It's not that sort of visit."
    call sna_main("Really? Then what's she doing here.","snape_05")
    m "She's the one who's been casting those curses."
    call sna_main("Truthfully? A slytherin?","snape_05")
    call sna_main("I expect better than this from my students, miss Greengrass...","snape_10")
    call sna_main("The very first lesson I give you is to not--","snape_08")
    call sna_main("get--","snape_08",trans="hpunch")
    call sna_main("caught--!","snape_15",trans="hpunch")
    pause.5
    call sna_main("Do you have anything to say for yourself?","snape_10")
    call ast_main("I-I'm sorry, sir... It won't happen again.","disgust","closed","base","mid")
    call sna_main("Well as long as you only cast it once...","snape_09")
    call ast_main("Twice...","disgust","base","worried","R")

    stop music fadeout 1.0
    call play_sound("scratch")
    call sna_main("","snape_11",trans="hpunch")
    pause.5

    call sna_main("TWICE!?!","snape_15")
    call sna_main("But that means...","snape_08")
    call sna_main("There's probably an auror on the way right now!","snape_07")
    call sna_main("We are so fucked!","snape_29")
    call sna_main("Who did you cast them on you little idiot?","snape_30")
    call sna_main("Who did you curse?","snape_16")
    call ast_main("Well the first time I was just testing it out on Susan Bones...","disgust","closed","base","mid")
    call ast_main("She was being mean to me so I... might have used imperio... to embarrass her a little...","smile","narrow","worried","mid")
    call sna_main("And the second time?","snape_01")
    call ast_main("I just tried to use imperio on professor Dumbledore then, so he wouldn't get me in trouble...","disgust","base","base","R")
    call ast_main("But it didn't work!","pout","base","base","wide")
    call sna_main("Really? It must be because he's a geni--","snape_05")
    call sna_main("Genius wizard!","snape_17",trans="hpunch")
    call sna_main("But this is not good... If they're sending an auror here then they'll want to talk to you... Dumbledore...","snape_16")
    m "me?"
    call sna_main("I'm afraid so...","snape_06")
    m "How long until they get here?"
    call sna_main("I'm not sure, but I don't intend to find out!","snape_16")

    call sna_walk(action="leave", speed=1.5)

    call bld
    g4 "COWARD!"
    call play_music("night_theme")
    call ast_main("So there really is an auror coming?","worried","closed","worried","mid")
    call ast_main("I've heard that they're all trained by madeye moody...","worried","closed","worried","mid")
    call ast_main("PLEASE SIR!","worried","wide","wide","wide",tears="crying")
    call ast_main("YOU CAN'T LET THEM SEND ME TO Azkaban!",tears="crying")
    call ast_main("I promise I'll be good! I won't cast anymore curses!","scream","closed","base","mid")
    call ast_main("I'll do whatever you want!","scream","base","worried","R",tears="crying")
    m "Calm down..."
    call ast_main("b-b-but... I don't want to... go to Azkaban...","worried","closed","worried","mid")
    m "I'm not going to let them take you to Azkaban."
    call ast_main("r-r-r-really? even after I tried to control you?","smile","wink","worried","mid")
    m "(There's not a single being that could possibly control me!)" #4th wall break, lololol
    m "we'll talk about your punishment later. For now, I think it's better for you to go back to your room."
    call ast_main("A-a-alright... but what about the auror?","worried","wink","base","mid")
    m "I'll just explain to them that this was all a simple misunderstanding."
    call ast_main("T-thank you, sir...","smile","narrow","base","mid")
    m "However, I do expect you to come to my office whenever I summon you from now on."
    call ast_main("W-what? Why?","pout","wide","worried","wide")
    m "I might have to call you up here to see the auror. Not to mention we still have the matter of your punishment."
    call ast_main("But I thought it was all just a misunderstanding?","pout","base","narrow","R")
    m "You've committed a very serious offense here young girl. Just because you're not going to Azkaban, doesn't mean you're getting out of punishment."
    call ast_main("Alright sir...","pout","base","worried","R")
    m "Good. Now go back to your room until I summon you."
    g4 "And stop with the bloody curses!"
    call ast_main("yes sir...","pout","closed","base","mid")
    hide screen astoria_main
    with d3

    call nar(">Astoria turns to leave your office, looking slightly dejected at the prospect of future punishment.")
    m "(I feel like I'm actually starting to run this damn school.)"
    m "(This isn't what I signed on for...)"

    $ astoria_unlocked = True
    $ achievement.unlock("unlockast")

    $ astoria_busy = True
    $ hermione_busy = True
    $ snape_busy = True

    jump main_room



#TONKS AUROR INTRO #Done
label tonks_intro_event: #occurs a day or two after the last event
    call play_sound("knocking")
    "*knock* *knock* *knock*"

    m "Ugh..."
    m "Who is it?"
    ton "Tonk-"
    ton "Ugh-"
    ton "(...)"
    ton "Nymphadora Tonks, sir."
    ton "I've been sent by the ministry of magic."
    m "(Shit, another female... Is Snape the only dude on this forsaken planet?)"
    g9 "(Better to just let my charm play...)"
    m "Yes... come in."

    call play_sound("door")
    call ton_main("","base","base","base","mid",xpos="right",ypos="base")
    call ctc

    g4 "(Holy shit!)"
    g9 "(She's hot!)"
    call ton_main("Thank you sir... I assume you know why I'm here then?","open","base","base","mid")
    m "The curses, I'd imagine."
    call ton_main("Yes. As I'm sure you're aware, it's ministry protocol to have an auror investigate every instance of an unforgivable curse being cast.","open","base","raised","R")
    call ton_main("The ministry was willing to ignore one curse given the likelihood that it was just a student playing about...","open","base","worried","down")
    call ton_main("Two curses on the other hand, cannot be ignored.","open","base","raised","mid")
    m "I understand..."
    call ton_main("Well, first things first, do you know who it was that cast the spells?","base","base","raised","mid")
    m "I do."
    call ton_main("Fantastic, that saves me most of the effort involved with divination and location spells.","open","base","base","mid")
    call ton_main("Secondly, are you aware of what spell was cast?","base","base","raised","mid")
    m "(Shit... what was it called again?)"

    menu:
        "\'Imperio\'":
            call ton_main("I thought as much.","base","base","worried","R")
        "\'Imperial\'":
            call ton_main("Do you mean imperio sir?","base","base","raised","mid")
            m "Yes of course, forgive me..."
        "\'Imp Pio?\'":
            call ton_main("...","base","base","raised","mid")
            call ton_main("This is a serious matter sir, I'd prefer if you kept the jokes to a minimum.","open","base","angry","mid")
            m "certainly..."

    call ton_main("Well, I'm not surprised, It usually is Imperio.","open","base","worried","R")
    call ton_main("Most students don't have the guts to cast crucio on another person,...","open","base","worried","mid")
    call ton_main("Let alone Avada Cadavara...","open","wide","wide","wide")
    call ton_main("And lastly, are you aware who the curse was cast on?","open","base","worried","mid")
    m "I am."
    call ton_main("If you wouldn't mind...","base","base","raised","mid")
    m "Susan Bon--"
    call ton_main("Susan Bones!","open","wide","wide","wide",trans="hpunch")
    m "Is there something wrong?"

    show screen blktone
    call ton_main("Of course there's something wrong!","open","wide","angry","wide")
    call ton_main("Susan's my niece!","open","base","angry","mid")
    call ton_main("And you just let her have an unforgivable curse cast on her?","open","base","angry","mid")
    call ton_main("Aren't you supposed to protect your students from these sort of things?","open","base","angry","mid")
    m "There's only so much I can do-"
    call ton_main("Typical! You're just like the ministry, never willing to take responsibility for your failings.","open","base","angry","R")
    call ton_main("At least bring the son of a bitch who cursed my niece up here so I can escort them to Azkaban.","open","base","angry","mid")
    m "Azkaban? I thought that I was being put in charge of their punishment?"
    call ton_main("That was before I found out who it was that had been cursed, Dumbledore!","open","base","base","mid")
    call ton_main("Now they're going to be punished to the full extent of the law.","open","wide","angry","wide")
    call ton_main("Which means a lifetime sentence in Azkaban!","open","base","raised","mid")
    m "..."
    call ton_main("Well are you going to bring them up here or not?","open","base","angry","mid")
    m "I really don't think-"
    call ton_main("I don't care if it was Harry {b}fucking{/b} Potter himself that did it, they're going to Azkaban!","open","base","angry","mid")
    call ton_main("so... Bring. {size=+2}them. {size=+2}up. {size=+2}here!..","open","base","angry","mid")
    call ton_main("{size=+5}now!{/size}","open","base","angry","mid",trans="hpunch")
    m "alright..."
    call blkfade

    ">You summon Astoria up to your office."
    pause.5
    hide screen tonks_main
    hide screen blktone
    hide screen blkfade
    call ast_main("","upset","base","worried","R",xpos="mid",ypos="base",trans="fade")
    pause.8

    call ast_main("Hello professor.","upset","closed","base","mid")
    call ton_main("...","base","base","raised","L",xpos="base",ypos="base")
    call ast_main("Hello, ma'am.","pout","base","worried","R")
    call ton_main("H-hello...","open","base","raised","L")
    call ast_main("You wanted to see me sir?","pout","narrow","base","down")
    m "I'm afraid not, it was actually Miss Tonks here who wanted you brought up here."
    call ast_main("Oh...","upset","base","worried","down")
    call ast_main("Is everything alright?","worried","wink","worried","R")
    call ton_main("You can't be serious, Dumbledore...","open","base","angry","mid")
    call ton_main("Bring the actual caster up here.","open","base","angry","mid")
    m "You're looking at her."
    call ton_main("Honestly?","base","base","wide","L")
    m "Truly."
    call ast_main("Is this about the imperio I cast...","pout","narrow","worried","down")
    call ast_main("I'm really sorry! I promise I won't ever cast it again!","scream","closed","worried","mid")
    call ton_main("Really? It was you who cast the spell?","open","base","worried","L")
    call ton_main("but...","open","base","angry","down")
    call ton_main("but.......","open","base","raised","L")
    call ton_main("But you're so {size=+10}cute!{/size}","open","wide","wide","wide",trans="hpunch")
    call ast_main("...","disgust","wide","wide","wide")
    m "..."
    call ton_main("It couldn't possibly have been someone like you!","open","base","wide","L")
    call ast_main("I'm sorry miss... it was me...","open","closed","base","R")
    call ton_main("Really?","base","base","raised","L")
    call ast_main("Please don't send me to Azkaban!","scream","wide","wide","wide")
    call ast_main("I don't want to go where the dementors are!","scream","closed","worried","mid")
    call ton_main("Don't worry, It won't come to that...","base","base","base","L")
    call ast_main("r-r-r-really?","upset","wink","base","R")
    call ton_main("Of course not!","base","base","raised","mid")
    call ton_main("THe ministry isn't going to lock away a cute little thing like yourself for life over a little...","open","base","base","mid")
    call ton_main("{size=+2}harmless fun.{/size} {image=textheart}","horny","base","wide","L")
    m "..."
    call ton_main("So what did you make susan do anyway?","base","base","raised","L")
    call ton_main("Run around like a chicken?","base","base","raised","mid")
    call ast_main("Not exactly...","upset","closed","base","mid")
    call ton_main("Well come on then, no need to be secretive here.","base","base","base","L")
    call ast_main("I might have made her show her boobs to some second years...","upset","wink","base","mid")
    call ton_main("hahahaha!","base","base","wide","L")
    call ast_main("Just for a second!","pout","base","worried","R")
    m "(what's going on here?)"
    call ton_main("Is that all? You probably did Susan some good then, lord knows she needs to loosen up a bit.","base","base","wide","L")
    call ton_main("She always has been very sensitive about her body for some reason.","base","base","raised","mid")
    call ast_main("So I'm not going to get in trouble?","upset","base","base","mid")
    call ton_main("I didn't say that... You still cast a very serious spell...","open","base","base","L")
    call ton_main("However, given the circumstances, I'm going to leave your punishment in the hands of professor Dumbledore.","open","base","base","mid")
    m "Me?"
    call ton_main("That's not going to be an issue is it, sir?","base","base","raised","mid")
    m "Not at all!"
    call ton_main("Fantastic.","base","base","base","mid")
    call ton_main("Now as part of standard ministry proceedings, I'm going to be staying at the school a little while longer.","open","base","raised","mid")
    call ton_main("Just to ensure that there is nothing else at play.","base","base","base","mid")
    call ton_main("Ever since the imperio recursion event at Beauxbatons last year...","open","base","raised","mid")
    call ton_main("...they've been on edge over dark wizards and these sort of spells...","open","base","angry","R")
    m "Alright..."
    call ton_main("You may leave now, little one.","base","base","base","L")
    call ast_main("Uhm... Ok. Thank you, sir...","upset","closed","base","mid")
    call ast_main("Ma'am...","upset","wink","base","R")
    hide screen astoria_main
    with d3
    pause.8

    call ton_main("So {size=+5}cute!{/size} {image=textheart}","base","base","wide","mid",xpos="right",ypos="base")
    call ton_main("Anyways, I assume that I'll be allowed to sleep in the teachers quarters?","open","base","raised","mid")
    m "Of course, I'll have a bed made up for you immediately."
    call ton_main("Thank you, Dumbledore. Have a nice evening.","base","base","base","mid")
    m "You too..."
    hide screen tonks_main
    with d3
    pause.8

    m "(I didn't even realise we had beds here, I've just been sleeping in this chair...)"
    m "(I really need to clean this thing...)"

    $ astoria_busy = True

    jump main_room



#SNAPE MASKING SPELL #Done
label snape_spell_intro: #Snape tells genie that he has adjusted the magic shield

    call sna_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call play_music("snape_theme")
    call sna_main("I've done it, Genie!","snape_02",xpos="base",ypos="base")
    m "Done what?"
    m "You haven't killed anyone have you?"
    m "I can't bring people back to life Snape! don't expect me to get you out of this one..."
    call sna_main("What? No...","snape_01")
    call sna_main("I've solved our problem with the ministry!","snape_02")
    m "oh... really? How?"
    call sna_main("It was rather ingenious honestly...","snape_23")
    call sna_main("I modified the muggle masking spell to include unforgivable curses!","snape_02")
    m "And this masking spell,... will it work?"
    call sna_main("It's an enormous magical force-field surrounding us, Genie.","snape_24")
    call sna_main("Hiding the castle and all that's in it from all non-magical beings. Making it disappear.","snape_24")
    call sna_main("I was able to modify it to also shroud all unforgivable curses that are cast within it!","snape_23")
    call sna_main("Except for the deadly one, of course. The others are in my opinion quite harmless...","snape_09")
    call sna_main("You should know, magic in this world is closely monitored by the ministry of magic.","snape_01")
    m "And that should stop the ministry from coming here?"
    call sna_main("So long as they don't get wind of the favour trading that's happening, we shouldn't hear anymore from them!","snape_02")
    call sna_main("Can you imagine that? A whole new world of torturing and bending those filthy girls to our wills!","snape_20")
    call sna_main("I have a whole set of slytherin minxes that would willingly let me try those curses out on them!","snape_21")
    call sna_main("Aren't you impressed, Genie?","snape_22")
    m "(this means I could get that little Astoria Greengrass to show me some magic...)"
    m "I suppose..."
    call sna_main("What? Well what's the most impressive thing you've done with magic then?","snape_25")
    m "I once changed the world into a desolate Arabian wasteland..."
    call sna_main("...","snape_09")
    if daytime:
        jump snape_ready
    else:
        call sna_main("Wanna get drunk?","snape_02")
        m "Do I!"

        jump snape_hangout # Snape Genie drinking. Jumps to next day.



#SUSAN INTRO #
label astoria_susan_intro: #have astoria demonstrate the imperio spell for the first time on Susan
    call ast_main("You wanted to see me, sir?","upset","wink","worried","mid",xpos="mid",ypos="base")
    m "Yes. I think it's about time we addressed the issue of your punishment."
    call ast_main("oh... I was hoping you'd forgotten about that.","pout","narrow","narrow","R")
    m "Afraid not."
    call ast_main("What am I going to have to do then?","upset","base","base","mid")
    call ast_main("I won't have to clean the toilets, do I?!","scream","wide","wide","wide")
    m "Don't worry, it's nothing like that."
    call ast_main("Oh...","disgust","narrow","narrow","R")
    call ast_main("Then what will it be?","upset","wink","base","mid")
    m "First things first, I expect you to come to this office whenever I summon you from now on."
    call ast_main("What? Can't we just get this all over with at once?","scream","wide","wide","wide")
    m "Something like an unforgivable curse isn't so easily forgiven, miss Greengrass."
    m "It's in the name!"
    m "You know what the usual punishment is..."
    call ast_main("life in Azkaban...","disgust","closed","worried","mid")
    m "That's right... Now unless you want me to send you away, I think you better agree to this arrangement."
    call ast_main("...","pout","narrow","narrow","R")
    call ast_main("fine... but you better not be up to anything!","open","angry","worried","angry")
    g4 "Me?"
    m "Never..."
    call ast_main("...","pout","base","base","R")
    call ast_main("What's your second request.","upset","base","base","mid")
    m "My second, and last request, is that you cast an unforgivable curse."
    call ast_main("{size=+10}What?{/size}","scream","wide","wide","wide")
    call ast_main("But I don't want to go to Azkaban! You heard what that nasty old lady said!","scream","wide","wide","mid")
    m "Don't worry, you won't go to Azkaban."
    call ast_main("How can you be so sure? Won't she be able to tell if I cast another one?","scream","narrow","narrow","mid")
    m "Not anymore, I've made sure that no one will be any the wiser."
    call ast_main("...","disgust","wide","wide","down")
    call ast_main("But why do you want me to cast unforgivable curses?","open","wink","worried","mid")
    m "Let's just say I'm curious."
    m "(I wanna see someone get mind controlled!)"
    call ast_main("...","pout","angry","angry","angry")
    call ast_main("This isn't a test is it?","pout","angry","angry","R")
    call ast_main("You're just getting me to cast one so that I really do get sent to Azkaban aren't you?","disgust","narrow","narrow","mid")
    call ast_main("Well I won't do it!","scream","closed","base","mid")
    m "I think that you're forgetting that I can already send you to Azkaban."
    call ast_main("Oh...","disgust","base","worried","down")
    call ast_main("But I still don't understand, why would you want to see me cast a curse like that?","open","base","worried","mid")
    m "(Ugh...)"
    m "Because of your exceptional skill! Not everyone can just cast a curse like that!"
    call ast_main("I suppose not... I was pretty angry when I cast it though...","pout","base","base","R")
    call ast_main("I'm not sure if I could do it again...","open","wink","base","mid")
    m "Consider this a test then!"
    call ast_main("...","upset","base","worried","mid")
    call ast_main("Alright...","pout","base","worried","L")
    call ast_main("But I better not end up in Azkaban!","scream","closed","base","mid")
    m "Scout's honor."
    call ast_main("Well who do you want me to cast it on?","worried","base","base","mid")
    call ast_main("It didn't work the last time I tried it on you...","worried","base","base","R")
    m "Who did you say you cast it on last time?"
    call ast_main("Susan Bones, sir.","smile","base","base","mid")
    m "Let's just try that again, seeing as how we know that worked."
    call ast_main("What? You want me to cast a curse on another student? Again?","scream","wide","wide","wide")
    m "They won't remember that we've done it will they?"
    call ast_main("I suppose not...","pout","narrow","narrow","R")
    call ast_main("I just didn't expect you to be OK with us doing something like this...","open","base","base","mid")
    m "Believe me, I've done worse..."
    call ast_main("...","smile","base","base","down")
    call ast_main("Alright... I'll do it.","grin","base","base","mid")
    m "Fantastic!"
    call ctc

    call ast_main("...","pout","base","base","R")
    call ctc

    call ast_main("Are you not going to summon her?","open","wink","base","mid")
    m "I can't."
    call ast_main("Why not?","upset","narrow","narrow","mid")
    m "Because she hasn't visited my office yet. For some reason I can only summon people I've met before."
    call ast_main("That seems stupid.","pout","narrow","narrow","R")
    m "You tell me..."
    call ast_main("Should I go and get her then?","smile","wink","worried","mid")
    m "If you wouldn't mind."
    call ast_main("OK... what should I say to her?","grin","closed","base","mid")
    m "About?"
    call ast_main("To get her to come up here!","open","base","base","down")
    call ast_main("I need to tell her something.","open","base","base","mid")
    m "Just tell her I want to have a word with her."
    call ast_main("Really? Can't it be something a little more fun?","pout","angry","base","R")
    m "Fun?"
    call ast_main("You know, something to make her think she's in trouble so she's all scared and nervous when she gets up here.","open","base","base","L")
    m "You can tell her whatever you want, so long as you get her up here."
    call ast_main("yay!","happy","base","base","mid")
    call ast_main("I'll be right back.","grin","angry","angry","mid")
    hide screen astoria_main
    hide screen bld1
    call blkfade

    ">Astoria leaves your office, skipping and humming as she goes."
    pause.5
    call hide_blkfade
    pause.5

    call bld
    m "..."
    pause.5
    m "This might take a while..."
    pause.5
    g9 "Might as well..."
    hide screen bld1
    with d3
    pause.1

    call gen_chibi("jerking_off_behind_desk")
    with d3
    pause.8

    call play_sound("knocking")
    "*knock* *knock* *knock*"
    call bld
    m "(Damn it...)"
    m "Give me a second..."

    call gen_chibi("hide")
    show screen genie
    with d3
    pause.2

    m "Come in."

    call sus_walk(action="enter", xpos="mid", ypos="base", speed=2.5)
    pause.8

    call sus_main("","upset","base","worried","mid",xpos="mid",ypos="base")
    call ctc

    with hpunch
    g4 "!!!"
    g9 "(LOOK AT THOSE KNOCKERS!)"
    call ast_main("","pout","angry","angry","L",xpos="base",ypos="base")
    pause.8

    m "And Who is this?!?"
    call sus_main("My name is S-Susan Bones, sir...","open","base","worried","L")
    call sus_main("Astoria said you n-needed to see me urgently.","open","narrow","worried","down")
    m "Yes... need to see... them..."
    call sus_main("...","upset","base","worried","mid")
    call sus_main("If you don't mind me asking sir,... what's this about?","open","base","worried","mid")
    m "Oh, um... Did Astoria not tell you?"
    call sus_main("N-no sir...","upset","base","worried","L")
    m "Well, Miss Greengrass and I were discussing how best to further the educat--"

    call ast_main("","grin","angry","angry","angry")
    call cast_spell("imperio")
    call sus_main("","upset","wide","base","wide")
    call ast_main("{size=+10}{b}IMPERIO{/b}{/size}","scream","angry","angry","angry")
    call ast_main("","smile","angry","angry","angry")

    call nar(">A puff of yellow smoke appears in front of Susan's face.","start")
    call sus_main("W-what is thi--","open","narrow","worried","up")
    ">As quick as it appeared, it seems to fly up Susan's nose, her expression relaxing as it moves."
    call sus_main("...","base","base","base","up")
    call nar(">Susan's eye's seem to empty as her body relaxes.","end")

    call ast_main("Yay! It worked!","grin","angry","angry","angry")
    m "Fantastic!"
    call ast_main("So what should we do now?","grin","closed","base","mid")
    call ast_main("Want me to make her dance like a chicken?","grin","angry","angry","L")
    m "Not exactly..."
    call ast_main("What then?","open","wink","base","mid")
    m "Well what did you do to her the first time?"
    call ast_main("...","pout","angry","angry","R")
    call ast_main("I can't say... It's too embarrassing!","pout","narrow","narrow","R")
    g9 "Now I have to know!"
    call ast_main("OK... but you have to promise that you won't get mad at me!","pout","narrow","narrow","mid")
    m "Sure..."
    call ast_main("Well, a few of the other girls have been talking about...","open","base","base","mid")
    call ast_main("...","upset","base","worried","down")
    call ast_main("they were talking about breasts, sir!","disgust","base","base","down",cheeks="blush")
    g9 "(JACKPOT!)"
    m "Go on..."
    call ast_main("They were talking about how boys only like the big ones...","open","narrow","narrow","down",cheeks="blush")
    call ast_main("And that only the girls with big boobs would get asked to the autumn ball...","open","narrow","worried","down",cheeks="blush")
    m "Was Susan one of these girls?"
    call ast_main("No sir. It was just a few of the \'Slytherin\' girls talking in the common room.","open","base","base","mid")
    m "So how did Susan become involved in all this then?"
    call ast_main("It was her own fault!","pout","angry","angry","R")
    m "..."
    call ast_main("What does she expect to happen when she keeps flaunting those disgusting udders of hers around the school!","pout","angry","angry","L")
    call ast_main("It's only fair that someone put her in her place!","pout","angry","angry","mid")
    m "And this someone was you?"
    call ast_main("...","upset","narrow","narrow","mid")
    call ast_main("yes...","worried","narrow","narrow","down",cheeks="blush")
    m "So what did you do?"
    call ast_main("I might have... made her...","worried","angry","angry","R")
    call ast_main("I made her walk around without a shirt on...","pout","angry","angry","R")
    m "What? Really?"
    call ast_main("I'm sorry sir! It was just around the common-room.","open","base","worried","mid")
    call ast_main("I was just so angry about her getting all the attention from the boys.","worried","base","worried","down")
    call ast_main("So I gave her all the attention she could ever ask for!","worried","base","base","L")
    call ast_main("Although it was only around the girls common-room, so it wasn't that big a deal...","open","closed","base","mid")
    call ast_main("And it's not like she can remember it anyway...","open","base","base","R")
    call ast_main("It was just so {b}exciting{/b} to see her taken down a notch...","grin","angry","angry","R")
    m "And what did the other girls do once you started parading her around?"
    call ast_main("They were all shocked at first...","grin","base","base","mid")
    call ast_main("A few of them just told her to stop showing off and put a top on...","open","angry","angry","R")
    call ast_main("So I had to make things a little more embarrassing for her...","grin","angry","angry","mid")
    m "How that?"
    call ast_main("I may have made her do a little dance...","grin","base","base","mid")
    m "A dance?"
    call ast_main("Well... it was sort of just making her shake her boobs for them...","smile","base","base","R")
    m "Can you make her do it again?"
    call ast_main("WHAT!","disgust","wide","wide","wide")
    call ast_main("Professor! I can't do something like that!","scream","closed","base","mid")

    menu:
        "\"Why not?\"":
            call ast_main("Because... because it's wrong!","open","closed","worried","mid")
            call ast_main("You're too old!","scream","wide","wide","mid")
            call ast_main("And you're her teacher!","worried","wide","wide","wide")
            m "So what?"
        "\"Come on...\"":
            call ast_main("...","pout","angry","angry","mid")
            call ast_main("Is this a joke sir?","pout","angry","angry","R")
            m "Maybe..."

    call ast_main("You can't expect me to do something like that!","disgust","closed","worried","mid")
    call ast_main("Unless...","open","wide","wide","wide")
    m "Unless?"
    call ast_main("Maybe if you made it worth my while...","grin","angry","angry","mid")
    call ast_main("Maybe I would be OK...","open","narrow","narrow","mid")
    call ast_main("With making Susan dance for you...","open","narrow","narrow","R")
    m "And what sort of reward would that be?"
    call ast_main("I want points!","scream","closed","angry","mid",trans="hpunch")
    m "(... here we go again...)"
    m "What's your house called?"
    call ast_main("Slytherin! You should know that!","pout","narrow","narrow","R")
    m "How about instead--"
    call ast_main("Not done!","scream","closed","angry","mid",trans="hpunch")
    call ast_main("I also expect you to teach me some new spells!","scream","angry","angry","mid")
    m "What?"
    call ast_main("All the spells I've been learning in class are so {b}boring!{/b}","pout","angry","angry","R")
    call ast_main("Those dumb teachers only want us to learn safe spells...","pout","angry","angry","L")
    call ast_main("that's part of the reason why I cursed Susan in the first place...","pout","angry","angry","mid")
    call ast_main("The unforgivable curses were the first fun spells I learned about!","open","narrow","narrow","mid")
    call ast_main("Well maybe not crucio or avada kadavra...","open","narrow","narrow","down")
    call ast_main("But imperio!","clench","angry","angry","angry")
    call ast_main("It's so much fun!!!","grin","closed","base","mid")
    call ast_main("I wanna learn more spells like this!","grin","angry","angry","mid")
    call ast_main("So I expect you to teach me them, I'm sure you know them all, old man.","open","closed","base","mid")
    m "(I don't know shit.)"
    m "Alright..."
    call ast_main("Yay!","grin","closed","base","mid")
    call ast_main("Well in that case...","smile","base","base","mid")

    #Susan Strips.
    call ast_main("Susan, give professor Dumbledore a nice dance...","scream","closed","base","mid")
    call sus_main("Yes...","base","base","base","mid")
    call nar(">Susan starts moving her hips slowly to the sides, barely moving.")
    call ast_main("That's terrible!","scream","wide","wide","L")
    call sus_main("Oh...","upset","base","worried","mid")
    call ast_main("Take your top off at least...","grin","angry","angry","L")
    call ast_main("Don't worry Dumby, I'll make sure you get a good show!","open","closed","base","mid")
    m "Dumby?"
    call ast_main("Short for Dumbledore!","pout","narrow","narrow","mid")
    m "oh... right..."

    #call set_sus_top("top_2") #ADD Shirt without vest.
    #pause.5

    #call nar(">As the two of you talk, Susan slowly removes her vest.")
    #call ast_main("That's it Susy, one piece at a time.","scream","narrow","base","L")
    call ast_main("That's it Susy, show us those cow tits and take off your vest.","grin","narrow","base","L")
    m "You seemed to have changed your tone..."
    call ast_main("Because now I know this isn't a test.","open","closed","base","mid")

    #call set_sus_top("top_3") #ADD Shirt without vest and tie.
    #pause.5

    #call nar(">Susan quietly removes her tie.")
    call ast_main("Before I was certain you were going to expel me as soon as I cast Imperio.","open","base","base","mid")
    call ast_main("But after you've asked to see Susy's boobs,... well...","open","base","base","L")

    #hide susan_main
    $ susan_wear_top = False
    call update_sus_uniform
    call sus_main("","base","base","base","mid")
    pause.5

    call nar(">Susan peels her stressed shirt off.")
    call ast_main("And now I get to learn some cool new spells!","grin","angry","angry","L")
    call ast_main("...","pout","narrow","narrow","L")
    call ast_main("They better be cool old man!","pout","angry","angry","mid")
    call ast_main("I don't want something boring like fireworks or something.","open","closed","base","mid")
    m "What did you have in mind?"
    call ast_main("Hmmm--","pout","base","base","R")
    call ast_main("Something no one else will know!","grin","angry","angry","mid")
    m "So you want secret spells?"
    call ast_main("Yes! And they have to be fun as well! I don't want a secret spell to find a frog!","open","closed","base","mid")


    call nar(">Susan slowly moves her arms to unclip her bra...")
    m "Ah... sure... whatever you said..."
    call ast_main("...","pout","narrow","narrow","mid")
    call ast_main("Are you excited to see her boobs old man?","open","narrow","narrow","L")
    m "Yeah... it's not every day you get to see a pair like these..."
    call ast_main("Hmph","pout","narrow","narrow","R")
    call ast_main("Typical...","pout","narrow","base","R")
    m "Shh..."
    call ast_main("They're gross...","pout","closed","angry","mid")
    call ast_main("Everyone {size=-2}knows {size=-2}that {size=-2}flat {size=-2}boobs {size=-2}are {size=-2}justice...{/size}","scream","closed","base","mid")
    call ast_main("I think you've seen enough old man!","scream","angry","angry","mid",trans="hpunch")
    m "You can't be serious!"
    call ast_main("[ast_susan_name], I command you to stop!","open","base","base","L")
    call ast_main("Put your clothes on, go back to your room and go to sleep!","grin","base","base","L")
    call sus_main("yes...","base","base","base","up")
    pause.5

    call set_sus_top("top_1") #Normal top.
    with d3
    pause.8

    call sus_walk(action="leave", speed=2.5)

    call play_music("hermione_theme")
    call ast_main("","grin","angry","angry","mid",xpos="mid",ypos="base",trans="fade")
    pause.5

    m "Aw, but we were just getting to the best bit!"
    call ast_main("You can save that for next time old man, I think you've had enough fun today.","open","closed","base","mid")
    call ast_main("Anymore and you're heart will probably give out!","grin","angry","angry","mid")
    call ast_main("In the mean time, I want you to think up some fun and secret spells!","open","base","base","R")
    m "Sure..."
    call ast_main("Alright, well don't bring me up here again until you've got them!","smile","closed","base","mid")
    call ast_main("Good bye, Professor!","open","base","base","mid")
    m "Good bye, child..."
    call ast_main("*hmph*(I'm not a child...)","pout","angry","angry","R")
    hide screen astoria_main
    hide screen bld1
    with d3

    $ susan_unlocked = True
    $ achievement.unlock("unlocksus")

    $ astoria_busy = True
    $ susan_busy = True

    jump main_room



#SNAPE HANDS OVER HIS BOOK #Done
label snape_book_intro: #Have genie ask for a book of sex spells
    m "So to use your magic, you have to say words to cast your spells right?"
    call sna_main("Of course! You don't think we just wiggle our noses do you?","snape_05",xpos="base",ypos="base")
    m "I suppose not..."
    m "Well do you happen to have any secret spells?"
    call sna_main("Secret spells? What for?","snape_04")
    m "It's um..."
    m "It's for a student..."
    call sna_main("What? Miss Granger?","snape_01")
    call sna_main("You can forget all about me giving her anything!","snape_10")
    m "Calm down Severus, it's not Hermione, it's someone else..."
    call sna_main("Oh, you finally got yourself another one did you?","snape_02")
    m "In a way... I'm still trying to get her to come around."
    m "But in exchange she wants me to teach her secret spells or something."
    m "I've got no idea if that's even a thing with your magic."
    call sna_main("It is...","snape_24")
    m "really? So you have some secret spells?"
    call sna_main("I do...","snape_23")
    m "What kind?"
    call sna_main("You may find this hard to believe, but I had a bit of a troubled childhood.","snape_29")
    m "(Shocker...)"
    call sna_main("...","snape_12")
    call sna_main("Anyway, I sort of turned to spell creation as a way to channel my emotions at the time.","snape_24")
    call sna_main("At the age of nine I invented one of my favorite spells, {b}septum sempra{/b}.","snape_02")
    call sna_main("A curse of such terrible power... Even to this day I still see all the faces of-","snape_20")
    m "Yeah yeah yeah, do you have anything fun?"
    call sna_main("Ugh, you could've at least let me finish my story.","snape_29")
    m "Go on then..."
    call sna_main("As I was saying, I used spells as a way to funnel my frustrations. So when I hit puberty, the spells became a little more...","snape_24")
    call sna_main("Sexual in nature...","snape_13")
    m "Really? What did they do."
    call sna_main("It's too embarrassing...","snape_14")
    m "Come on man! Don't hold out on me."
    call sna_main("I'm not going to stand here and explain them all to you.","snape_12")
    call sna_main("Just take the book.","snape_13")

    call sna_walk(xpos="desk", ypos="base", speed=2)

    call nar(">Snape hands you a pink leather book.")
    call sna_main("I've written notes explaining what the spells do as well as how to cast them.","snape_24")
    call sna_main("Keep in mind this sort of magic isn't quite what most students will be used to.","snape_01")
    call sna_main("It's based on a far more primal magic, based off of emotions rather than words.","snape_02")
    call sna_main("It'll take a fair bit of practice before they'll be able to give them a go.","snape_10")
    m "Thanks, even if she can't manage to cast them, the fact you made them should get her off my back."
    call sna_main("Will that be all Genie?","snape_09")
    if daytime:
        m "(...)"
        jump snape_ready
    else:
        m "I guess... Unless you fancy a drink?"
        call sna_main("I thought you'd never ask.","snape_02")

        jump snape_hangout # Snape Genie drinking. Jumps to next day.



#TONKS TEACHER INTRO #Done
label astoria_tonks_intro: #occurs after you get the book from Snape
    call play_sound("knocking")
    "*knock* *Knock* *Thwump*"

    call play_sound("door")
    call ton_main("Sir, I have reason to believe that there is in fact a dark wizard operating somewhere on the grounds.","open","wide","wide","wide",xpos="right",ypos="base")
    m "A dark wizard?"
    m "Surely you meant to say an African American wizard?"
    call ton_main("This isn't the time for your silly jokes, Professor!","open","base","angry","mid")
    call ton_main("I've recently detected another instance of an unforgivable curse being cast in my vicinity.","open","base","raised","R")
    call ton_main("But what's really troubling is that the ministry hasn't contacted me...","open","base","worried","down")
    call ton_main("It must mean that the wizard is concealing themselves to the ministries global detection spell system.","open","base","raised","mid")
    call ton_main("We have to evacuate the school until they're caught... We can't risk the death of a student...","open","base","angry","mid")
    m "Oh... I think those spells you were picking up on might have involved me..."

    stop music fadeout 1.0
    call ton_main("you can't mean...","base","wide","wide","wide")
    call ton_main("You're the dark wizard???","open","wide","wide","wide")
    m "I told you, I don't think you can say that anymore..."

    call play_music("hitman")
    call ton_main("THIS IS NO LAUGHING MATTER!","open","base","angry","mid")
    m "I'm not a \'dark\' wizard! the spells are occurring under my strict supervision."
    call ton_main("You mean you've been letting students cast unforgivable curses? And hiding it from the Ministry?","open","wide","wide","wide")
    call ton_main("What are you thinking?","open","base","angry","mid")
    m "As headmaster of this school, I believe that teaching students is my business, thank you very much."
    call ton_main("Well unforgivable curses are my business, Dumbledore!","open","base","angry","mid")
    call ton_main("I demand you explain what's going on before I Floo back to the ministry and tell them everything!","open","base","angry","R")
    m "(Shit...)"
    m "Alright fine..."
    m "I've been tutoring a student..."
    call ton_main("In the dark arts? Are you crazy?","open","wide","wide","wide")
    m "Don't worry, I'm not letting her kill anyone..."
    call ton_main("Her? Who exactly are you tutoring then?","open","base","angry","mid")
    m "Astoria Greengrass. I believe you've met--"
    call ton_main("Astoria? You mean that cute little lo--{p}lady...","base","base","raised","mid")
    call ton_main("Why on earth are you teaching her curses?","open","base","raised","R")
    m "Miss Greengrass approached me about wanting to learn some more advanced spells."
    call ton_main("So you decided to teach her how to cast Imperio???","open","base","worried","mid")
    call ton_main("And if she's casting imperio under your supervision, then who is the cursee?","open","base","raised","mid")
    call ton_main("I don't suppose you'd let her curse you.","base","base","angry","mid")
    m "Remember your niece?"
    call ton_main("{size=+2}SUSAN?{/size}","open","wide","wide","wide")
    call ton_main("You cannot be serious!!! {p}What sort of school are you running here?","open","base","angry","mid")
    m "A magic one?"
    call ton_main("...","base","base","angry","mid")
    call ton_main("What are you and Astoria making Susan do then?","open","base","angry","mid")
    m "Oh... um..."
    m "Dance like a chicken?"
    call ton_main("You honestly expect me to believe that?","open","base","angry","R")
    m "It was worth a shot."
    call ton_main("So let me get this straight...","base","base","angry","R")
    call ton_main("You've been teaching dark arts to a student, concealing your actions from the ministry of magic...","open","base","angry","mid")
    call ton_main("And controlling my niece to do who knows what?","open","base","angry","mid")
    call ton_main("Do you have any idea how much trouble you're in?","open","base","angry","mid")
    m "Is that a rhetorical question?"
    call ton_main("This probably means that those letters from Miss Granger were actually telling the truth as well.","base","base","raised","R")
    m "What letters?"
    call ton_main("The ministry received a formal complaint from miss granger a few weeks ago about a sexual favour ring at hogwarts.","open","base","raised","mid")
    call ton_main("Obviously the ministry ignored the matter. I mean who could believe that the famous Albus Dumbledore would let something like that happen...","open","base","worried","R")
    call ton_main("But now I'm not so sure...","base","base","angry","mid")
    m "..."
    call ton_main("So is it true then?","open","base","raised","mid")
    call ton_main("Are you fucking your students Dumbledore?","open","base","angry","mid")
    call ton_main("Or are you just covering up for the other teachers here?","base","base","raised","mid")

    menu:
        "-lie-":
            m "I'd never allow--"
        "-tell the truth-":
            m "It all started--"

    call ton_main("I don't care, either way you're going to Azkaban for the rest of your life...","open","base","angry","mid")
    m "*gulp*"
    call ton_main("Unless...","open","base","raised","R")
    m "Unless what?"

    call play_music("hermione_theme")
    call ton_main("Do you have an opening for a defense against the dark arts teacher?","open","base","worried","mid")
    m "..."
    m "What?"
    call ton_main("Ugh... You can't think I like being an auror do you?","base","base","worried","R")
    call ton_main("It's just constant busy work...","open","base","angry","mid")
    call ton_main("Not to mention the hours.","open","base","base","up")
    call ton_main("And the mortality rate...","open","base","worried","down")
    call ton_main("If I'd realized the benefits of being a teacher at hogwarts, I would have signed up straight away!","open","base","angry","mid")
    m "Benefits?"
    m "You mean the favour trading?"
    call ton_main("No, I mean the health care... Of course I mean the favour trading, Dumbledore!","open","base","raised","mid")
    call ton_main("I always assumed that you and Snape wouldn't allow holding hands in the corridors...","open","base","base","mid")
    call ton_main("But if you're playing around with your students...","base","base","base","mid")
    call ton_main("Well let's just say I want in.","horny","base","raised","mid")
    m "(...)"

    g9 "You are hired!"
    m "Consider yourself the new defense of the ancients teacher or whatever..."
    call ton_main("What about Quirrel?","open","base","raised","mid")
    m "Who?"
    call ton_main("The current defense against the dark arts professor...","open","base","base","R")
    m "Oh yeah... I'll get Snape to deal with him..."
    call ton_main("So Snape is in on this too?","open","base","raised","mid")
    m "Yeah..."
    call ton_main("Huh... I didn't think that sad sack even knew what fun was...","base","base","raised","R")
    call ton_main("So what's the going rate around here then?","open","base","base","mid")
    m "Going rate?"
    call ton_main("How much do you pay your students to fool around?","base","base","base","mid")
    m "Oh... It depends on what you want them to do."
    call ton_main("How much for a lap dance?","horny","base","raised","mid")
    m "Again, it depends on the student."
    call ton_main("...","base","base","base","mid")
    m "But if I had to guess, I'd say about 25 points."
    call ton_main("Wait...","open","wide","wide","wide")
    call ton_main("You pay them in points?","open","base","raised","mid")
    m "Most of them."
    call ton_main("So you've managed to convince these girls to offer themselves up for a bunch of imaginary points that don't mean anything?","open","base","angry","mid")
    m "Works for the internet..."
    call ton_main("What?","base","base","angry","mid")
    m "Anyway, you can't just ask for a lap dance straight away, You have to butter them up first."
    call ton_main("How so?","base","base","raised","mid")
    m "Well most of them aren't going to just do whatever you say from the get go..."
    m "You have to slowly earn their trust over time and start out small..."
    call ton_main("Awww really... Can't I just cheat a bit?","open","base","worried","L")
    m "..."
    m "Just take it slow alright, I'm sure you'll find a cute boy who'll be willing to do whatever you want anyway."
    call ton_main("...And what if I want a girl?","horny","base","raised","mid")
    g4 "(...!)"
    m "Whatever floats your boat."
    call ton_main("Well what if I want a specific girl?","base","base","raised","mid")
    m "which one?"
    call ton_main("Astoria Greengrass.","horny","base","angry","mid")
    m "Astoria? Isn't she a little too--"
    call ton_main("She's perfect! She's just so cute and innocent... I can't wait to gobble her up!","horny","base","worried","mid")
    call ton_main("Mmmm... I bet she tastes like heaven...","open_wide_tongue","base","base","up")
    m "..."
    m "I'm not sure if she'd be up for that to be honest--"
    call ton_main("Well you better make her up for it then...","base","base","raised","mid")
    call ton_main("Unless I need to tell the ministry about all this...","open","base","angry","mid")
    m "Fine..."
    call ton_main("Good... I expect her to pay me a little visit soon.","horny","base","raised","mid")
    m "..."
    call ton_main("Now if that's all I'll be off.","base","base","base","mid")
    m "Sure..."
    hide screen tonks_main
    with d3
    call nar(">Tonks turns and leaves your office.")
    m "..."
    m "Did I just become a pimp?"

    $ tonks_unlocked = True
    $ achievement.unlock("unlockton")

    $ tonks_busy = True


    jump main_room



#ASTORIA TONKS FAVOUR INTRO. #Done
label astoria_book_intro: #Tell Astoria that you have a book of spells as well as the pimping with Tonks

    call ast_main("So have you finally managed to remember some cool spells?","grin","angry","angry","mid",xpos="mid",ypos="base",trans="fade")
    call ast_main("Or is remembering stuff too hard for you now?","tongue_silly","angry","angry","mid")
    m "I'll have you know that I've got a whole book full of new spells for you to learn."
    call ast_main("Really?","happy","wide","wide","wide")
    call ast_main("Maybe you're not so such a Dumby after all!","grin","happyCl","base","mid")
    m "Do you want to learn them or not?"
    call ast_main("Of course!","grin","base","base","mid")
    call ast_main("I had to spent the whole day listening to Mcgonagall prattle on about the importance of a transfiguration spell.","pout","angry","angry","R")
    call ast_main("When all it did was turn a stupid rat yellow!","upset","ahegao","ahegao","ahegao")
    call ast_main("I wanna learn something that's actually fun!","pout","narrow","narrow","down")
    m "Well in that case I'll need you to do something for me."
    call ast_main("Should I get Susan up here so you can stare at her stupid fat udders again?","grin","angry","angry","mid")
    call ast_main("I won't send her away this time...","open","base","base","R")
    call ast_main("As long as you behave!","clench","angry","angry","angry")
    m "As tempting as that offer is, that's not it."
    call ast_main("Well what is it then?","open","base","base","L")
    call ast_main("You don't expect me to dance for you do you?","upset","wink","worried","mid")
    m "(Not yet...)"
    m "No, this involves Nymphomaniac Tonks or whatever she was called..."
    call ast_main("The auror!","disgust","wide","wide","wide")
    m "(Well technically she's your teacher now...)"
    call ast_main("You're not going to send me to Azkaban, are you?","scream","closed","worried","mid")
    call ast_main("You promised!","disgust","narrow","worried","down")
    m "No ones sending you to Azkaban."
    call ast_main("Then why does she want to see me?","pout","angry","angry","R")

    menu:
        "-Tell the truth-":
            m "Well, you know how some of the teachers here like to award bonus points to students-"
            call ast_main("You mean the favour trading?","upset","base","base","mid")
            m "You know about that?"
            call ast_main("Of course I know. Half the girls in slytherin earn extra points of Snape.","pout","base","base","R")
            call ast_main("A few have even earned some off of slughorn.","disgust","narrow","base","down")
            with hpunch
            call nar("Astoria shivers at the thought.")
            call ast_main("But I've never done anything like that, Snape gives me the creeps...","pout","angry","angry","L")
            call ast_main("(Plus he only likes girls with big boobs...)","pout","angry","angry","R")
        "-Lie-":
            m "She just wants to ask you a few questions."
            call ast_main("Like what?","upset","wink","worried","mid")
            m "I'm not sure, you'll have to wait and see..."
            call ast_main("I don't wanna!","pout","angry","angry","R")
            m "Come on now... She might even pay you some points afterwards..."
            call ast_main("Some points? You mean...","scream","wide","wide","wide")
            call ast_main("Am I going to have to sell her favours, [ast_genie_name]?!","disgust","wide","wide","mid")
            m "Favours? I have no idea what you're talking about..."
            call ast_main("[ast_genie_name]! Everyone knows about the favour trading here at school.","open","angry","angry","mid")
            call ast_main("I've got three friends who even buy favours from Snape!","disgust","narrow","narrow","R")
            m "Really?"
            call ast_main("Yeah, although they're all huge sluts... I'd never do something like that.","pout","narrow","narrow","R")
            call ast_main("(Plus Snape only likes girls with big boobs...)","pout","ahegao","ahegao","ahegao")

    m "Well we won't be able to practice these new spells without you heading over there."
    call ast_main("Really? You mean I have to go see that creepy old lady...","pout","angry","angry","R")
    m "She's not that old!"
    call ast_main("Maybe for you...!","pout","angry","angry","down")
    call ast_main("She looks ancient!","pout","angry","angry","mid")
    m "You'll look ancient too after 30 years in Alakazam if you don't go over there!\nNOW!"
    call ast_main("What? But you promised! [ast_genie_name]!!!","scream","wide","wide","mid")
    m "I promised you I wouldn't! I've never said that Tonka wouldn't lock you up in Alkatraz instead of me!"
    call ast_main("I don't think that's her name, sir...\n(Nor the right prison...)","worried","narrow","narrow","L")
    m "Whatever, just head over there!"
    m "She won't do anything strange with you. Just talking..."
    call ast_main("Are you sure?","worried","closed","worried","mid")
    m "What's the worst that could happen, really?"
    m "Scared she'll look under your skirt?"
    call ast_main("[ast_genie_name]!","scream","wide","wide","wide")
    m "Just go say hello."
    m "Come back here afterwards and tell me what happened."
    call ast_main("Do I have to?","disgust","closed","worried","mid")
    m "Only if you want to practice cool new spell..."
    call ast_main("Ugh... fine.","pout","angry","angry","R")
    call ast_main("But she better keep her wrinkly old hands to herself.","open","closed","base","mid")
    g9 "I'll show you wrinkly old hands."
    call nar(">You reach out to grab her.")
    call ast_main("Ahhhh!-- Fine, I'm leaving!","scream","closed","worried","mid")
    hide screen astoria_main
    call play_sound("door")
    with d3
    pause.2

    $ astoria_busy = True
    $ tonks_busy = True

    $ astoria_tonks_event_in_progress = True
    call set_ast_map_location("defense_classroom") #Update's Astoria's map location.

    call nar(">Astoria sprints out the door, giggling as she goes.")

    jump main_room
