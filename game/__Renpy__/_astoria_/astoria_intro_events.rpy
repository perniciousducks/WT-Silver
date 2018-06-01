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
    call her_main("AN unforgivable CURSE!!!","scream","wide")
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
    call her_main("Tormenting them relentlessly for the rest of their miserable lives...","grin","happyCL")
    call her_main("And the perfect place to house all those dirty \'slytherins\'!","angry","angry")
    
    menu:
        "(...)"
        "-just tell her to find the student-":
            m "Whatever..."
            m "just find them so we can send them to Akabur..."
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
    
    call her_walk("mid","leave",2)
    
    if astoria_intro_flag_1 == True:
        m "I wonder if she'll find them before Snape..."
    else:
        m "I should probably go tell Snape as well..."

    jump day_main_menu

    
#TELL SNAPE ABOUT THE LETTER
label letter_intro_snape:
    m "I got some letter from the ministry of magic..."
    call sna_main("Really?","snape_03") #No xpos change.
    call sna_main("Why are you telling me?","snape_04")
    m "Apparently they've detected something called an \'unforgivable\' curse at the school..."
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
    
    call sna_walk("mid","leave",2)
    
    m "Drama queen..."

    jump day_main_menu

    
#HERMIONE CAPTURED ASTORIA    
label astoria_captured_intro:
    call play_sound("knocking")
    "*knock* *knock* *knock*"
    
    m "Who is it?"
    her "It's hermione granger, sir, although,... I'm not alone."
    m "Come in."
    
    call her_walk("door","desk",2.7)
    
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
    ast "No!"
    call her_main("Do you want to make this worse?","scream","closed",trans="hpunch")
    ast "no..."
    call nar(">Slowly, a small girl enters your office.")
    
    call her_chibi("stand","desk",flip=False)
    call her_main("","normal","angry")
    pause.2
    
    call ast_main("...","averted","sad","averted","c_pout")
    m "..."
    m "Who's this?"
    call ast_main("My name is Astoria Greengrass, sir.","averted","sad","averted","c_grimace")
    m "And why are you here?"
    call her_main("You asked me to bring you the person who cast the unforgivable curse sir.","soft","annoyed")
    call her_main("Here she is.","grin","angry")
    m "I thought it would be some angsty teen who listens to death metal or something..."
    m "not some little girl..."
    call ast_main("I am not a little girl!","angry","angry","angry","o_angry")
    m "What are you then, a 600 year old vampire?"
    call ast_main("Vampires aren't real!","angry","angry","averted","c_pout")
    m "..."
    m "So how are you not a little girl then?"
    call ast_main("I'm older than I look!","angry","angry","angry","c_pout")
    m "I've heard that one before..."
    call her_main("It's true, sir. She was a cursed child, born with a frailty that affects her growth.","normal","concerned")
    call ast_main("Told you!","angry","angry","averted","c_smile")
    m "Whatever... that still doesn't get you out of punishment."
    call ast_main("punishment? for what?","surprised","surprised","surprised","c_pout")
    call her_main("You know what you did!","angry","angryCl")
    call ast_main("I never casted Imperio on anyone! I swear, sir! Hermione's just being a know-it-all tattle-tail!","surprised","sad","averted","c_pout")
    m "Miss Granger..."
    call her_main("I overheard her boasting about it to a group of slytherins in the library.","annoyed","concerned")
    call her_main("By the sounds of it she used Imperio to control another student.","annoyed","narrow")
    call ast_main("Did not!","angry","sad","angry","c_worried")
    m "Well, given the severity of the situation, I'm sure there's something we can use to get a clear answer out of you..."
    call her_main("Shall I go fetch a vial of veritaserum from professor snape, sir?","grin","narrow")
    call ast_main("v-veritaserum? Isn't that against the rules?","surprised","sad","surprised","c_worried2")
    call her_main("Not when you've been casting unforgivable curses you evil little witch!","grin","angry")
    call ast_main("OK... I'll tell you what happened sir...","sad","sad","sad","c_pout")
    call ast_main("But only if Hermione leaves!","halflid","halflid","halflid","c_pout")
    call her_main("Not a chance!","scream","angryCl")
    m "Miss granger..."
    call her_main("professor! I think it's only fair, given that I was the one to catch her!","upset","annoyed")
    m "We'll talk about your reward later..."
    call her_main("*hmph*","annoyed","angryL")
    call her_main("Fine...","open","angryCl")
    call her_main("I'll go back to my room then...","annoyed","angryL")
    call her_main("Goodbye sir...","open","angry")
    call her_main("Goodbye Astoria...","angry","closed")
    
    
    call her_walk("desk","leave",2.7)
    
    call bld
    m "Right, well now that Hermione's gone, why don't you tell me exactly what--"
    #magic sound effect and screen shake
    
    stop music fadeout 2.0
    call play_sound("spell")
    show screen white 
    pause.1
    hide screen white
    with hpunch
    
    call ast_main("IMPERIO!!!","angry","angry","angry","o_angry")
    
    call blktone
    m "..."
    m "What was that?"
    call hide_blktone
    
    call ast_main("I just casted Imperio on you, professor! Now you have to do everything I say!","halflid","halflid","halflid","c_grin")
    g4 "Did you just do it again? Another bloody curse... on me?"
    call ast_main("yes... but it should have... why aren't you...","halflid","scared","halflid","c_worried")
    m "Ugh..."
    m "I better get Snape up here."
    call ast_main("professor snape? I command you not to!","angry","angry","angry","c_worried2")
    m "yeah, no. I'm bringing him up here because now we're probably going to have to deal with something called an auror coming to the school."
    call ast_main("An auror?!","surprised","surprised","surprised","c_worried")
    call ast_main("But they'll send me to Azkaban!","sad","scared","sad","c_worried2")
    m "I'm sure they'll be lenient, you're only a child after all."
    call ast_main("I am not a child!","angry","angry","angry","o_angry")
    m "ugh... I better get Snape."
    
    call play_sound("door")
    call sna_walk("door","mid",2)
    
    call sna_main("gen- oh, I see you already have a visitor...","snape_01",xpos="base",ypos="base")
    call ast_main("...","averted","scared","averted","c_pout")
    sna "Little young isn't she? even for you..."
    m "It's not that sort of visit."
    sna "Really? Then what's she doing here."
    m "She's the one who's been casting those curses."
    sna "Truthfully? A slytherin?"
    sna "I expect better than this from my students, miss Greengrass..."
    sna "The very first lesson I give you is to not. get. caught!"
    sna "Do you have anything to say for yourself?"
    call ast_main("I-I'm sorry, sir... It won't happen again.","sad","sad","sad","c_grimace")
    sna "Well as long as you only cast it once..."
    call ast_main("Twice...","averted","sad","averted","c_grimace")
    sna "TWICE!?!"
    sna "But that means..."
    sna "There's probably an auror on the way right now!"
    sna "We are so fucked!"
    pause.5
    sna "Who did you cast them on you little idiot?"
    sna "Who did you curse?"
    call ast_main("Well the first time I was just testing it out on Susan Bones...","sad","sad","sad","c_grimace")
    call ast_main("She was being mean to me so I... might have used imperio... to embarrass her a little...","halflid","sad","halflid","c_smile")
    sna "And the second time?"
    call ast_main("I just tried to use imperio on professor Dumbledore then, so he wouldn't get me in trouble...","averted","averted","averted","c_grimace")
    call ast_main("But it didn't work!","averted","averted","surprised","c_pout")
    sna "Really? It must be because he's a geni-"
    sna "Genius wizard!"
    sna "But this is not good... If they're sending an auror here then they'll want to talk to you... Dumbledore..."
    m "me?"
    sna "I'm afraid so..."
    m "How long until they get here?"
    sna "I'm not sure, but I don't intend to find out!"
    
    call sna_walk("mid","leave",1.5)
    
    g4 "COWARD!"
    call ast_main("So there really is an auror coming?","scared","scared","scared","c_worried")
    call ast_main("I've heard that they're all trained by madeye moody...","scared","scared","scared","c_worried")
    call ast_main("PLEASE SIR!","surprised","surprised","surprised","c_worried",extra_1="tears_1")
    call ast_main("YOU CAN'T LET THEM SEND ME TO Azkaban!")
    call ast_main("I promise I'll be good! I won't cast anymore curses!","sad","sad","sad","c_worried2")
    call ast_main("I'll do whatever you want!","averted","sad","averted","c_worried2")
    m "Calm down..."
    call ast_main("b-b-but... I don't want to... go to Azkaban...","sad","sad","sad","c_worried")
    m "I'm not going to let them take you to Azkaban."
    call ast_main("r-r-r-really? even after I tried to control you?","sad","sad","sad","c_smile")
    m "(There's not a single being that could possibly control me!)" #4th wall break, lololol
    m "we'll talk about your punishment later. For now, I think it's better for you to go back to your room."
    call ast_main("A-a-alright... but what about the auror?","one","one","one","c_worried")
    m "I'll just explain to them that this was all a simple misunderstanding."
    call ast_main("T-thank you, sir...","halflid","halflid","halflid","c_smile")
    m "However, I do expect you to come to my office whenever I summon you from now on."
    call ast_main("W-what? Why?","surprised","sad","surprised","c_pout",extra_1="blank")
    m "I might have to call you up here to see the auror. Not to mention we still have the matter of your punishment."
    call ast_main("But I thought it was all just a misunderstanding?","averted","halflid","averted","c_pout")
    m "You've committed a very serious offense here young girl. Just because you're not going to Azkaban, doesn't mean you're getting out of punishment."
    call ast_main("Alright sir...","averted","sad","averted","c_pout")
    m "Good. Now go back to your room until I summon you."
    g4 "And stop with the bloody curses!"
    call ast_main("yes sir...","sad","sad","sad","c_pout")
    hide screen astoria_greengrass
    
    call nar(">Astoria turns to leave your office, looking slightly dejected at the prospect of future punishment.")
    m "(I feel like I'm actually starting to run this damn school.)"
    m "(This isn't what I signed on for...)"

    jump day_main_menu

label tonks_intro_event: #occurs a day or two after the last event
    call play_sound("knocking")
    "*knock* *knock* *knock*"
    m "Ugh..."
    m "Who is it?"
    ton "Nymphadora Tonks, sir."
    ton "I've been sent by the ministry of magic."
    m "(Shit, another female... Is snape the only dude on this planet?)"
    g9 "(Better to just let my charm play...)"
    m "Yes... come in."
    call ton_main("","standard","standard","center","default")
    call ctc
    g4 "(Holy shit!)"
    g9 "(She's hot!)"
    call ton_main("Thank you sir... I assume you know why I'm here then?","standard","standard","center","open")
    m "The curses, I'd imagine."
    call ton_main("Yes. As I'm sure you're aware, it's ministry protocol to have an auror investigate every instance of an unforgivable curse being cast.","standard","standard","right","default")
    call ton_main("The ministry was willing to ignore one curse given the likelihood that it was just a student playing about...","standard","standard","down","default")
    call ton_main("Two curses on the other hand, cannot be ignored.","standard","concerned","center","default")
    m "I understand..."
    call ton_main("Well, first things first, do you know who it was that cast the spells?","standard","raised","center","default")
    m "I do."
    call ton_main("Fantastic, that saves me most of the effort involved with divination and location spells.","standard","standard","left","default")
    call ton_main("Secondly, are you aware of what spell was cast?","standard","standard","center","default")
    m "(Shit... what was it called again?)"
    menu:
        "\'Imperio\'":
            call ton_main("I thought as much.","standard","standard","right","default")
        "\'Imperial\'":
            call ton_main("Do you mean imperio sir?","standard","raised","center","default")
            m "Yes of course, forgive me..."
        "\'Imp Pio?\'":
            call ton_main("...","standard","raised","center","default")
            call ton_main("This is a serious matter sir, I'd prefer if you kept the jokes to a minimum.","standard","standard","center","default")
            m "certainly..."
    call ton_main("Well, I'm not surprised, It usually is Imperio. Most students don't have the guts to cast crucio on another person, let alone Avada Cadavara...","standard","concerned","right","default")
    call ton_main("And lastly, are you aware who the curse was cast on?","standard","raised","center","default")
    m "I am."
    call ton_main("If you wouldn't mind...","standard","standard","up","default")
    m "Susan Bones."
    m "(Whoever that is...)"
    call ton_main("Susan Bones!","wide","wide","wide","wide")
    m "Is there something wrong?"
    call ton_main("Of course there's something wrong!","wide","angry","wide","wide")
    call ton_main("Susan's my niece!","standard","angry","center","wide")
    call ton_main("and you just let her have an unforgivable curse cast on her?","standard","angry","center","wide")
    call ton_main("Aren't you supposed to protect your students from these sort of things?")
    m "There's only so much I can do-"
    call ton_main("Typical! You're just like the ministry, never willing to take responsibility for your failings.","standard","angry","right","wide")
    call ton_main("At least bring the son of a bitch who cursed my niece up here so I can escort them to Azkaban.","standard","angry","center","wide")
    m "Azkaban? I thought that I was being put in charge of their punishment?"
    call ton_main("That was before I found out who it was that had been cursed, Dumbledore!","standard","angry","center","wide")
    call ton_main("Now they're going to be punished to the full extent of the law.","wide","angry","wide","wide")
    call ton_main("Which means a lifetime sentence in Azkaban!","standard","standard","standard","default")
    m "..."
    call ton_main("Well are you going to bring them up here or not?","standard","standard","standard","default")
    m "I really don't think-"
    call ton_main("I don't care if it was Harry {b}fucking{/b} Potter himself that did it, they're going to Azkaban!","standard","standard","standard","default")
    call ton_main("so... Bring. {size=+2}them. {size=+2}up. {size=+2}here. {size=+2}now!{/size}","standard","standard","standard","default")
    m "alright..."
    ">You summon Astoria up to your office."
    call ast_main("Hello professor.","sad","sad","sad","c_blank")
    call ton_main("...","standard","standard","standard","default")
    call ast_main("Hello mam.","sad","sad","sad","c_blank")
    call ton_main("H-hello...","standard","standard","standard","default")
    call ast_main("You wanted to see me sir?","sad","sad","sad","c_blank")
    m "I'm afraid not, it was actually Miss Tonks here who wanted you brought up here."
    call ast_main("Oh...","sad","sad","sad","c_blank")
    call ast_main("Is everything alright?","sad","sad","sad","c_blank")
    call ton_main("You can't be serious Dumbledore...","standard","standard","standard","default")
    call ton_main("Bring the actual caster up here.","standard","standard","standard","default")
    m "You're looking at her."
    call ton_main("Honestly?","standard","standard","standard","default")
    m "Truly."
    call ast_main("Is this about the imperio I cast...","sad","sad","sad","c_blank")
    call ast_main("I'm really sorry! I promise I won't ever cast it again!","sad","sad","sad","c_blank")
    call ton_main("Really? It was you that cast the spell?","standard","standard","standard","default")
    call ton_main("but...","standard","standard","standard","default")
    call ton_main("but.......","standard","standard","standard","default")
    call ton_main("But you're so {size=+20}cute!{/size}","standard","standard","standard","default")
    m "..."
    call ast_main("...","sad","sad","sad","c_blank")
    call ton_main("It couldn't possibly have been someone like you!","standard","standard","standard","default")
    call ast_main("I'm sorry miss... it was me...","sad","sad","sad","c_blank")
    call ton_main("really?","standard","standard","standard","default")
    call ast_main("please don't send me to Azkaban!","sad","sad","sad","c_blank")
    call ast_main("I don't want to go where the dementors are!","sad","sad","sad","c_blank")
    call ton_main("Don't worry, It won't come to that...","standard","standard","standard","default")
    call ast_main("r-r-r-really?","sad","sad","sad","c_blank")
    call ton_main("Of course not! THe ministry isn't going to lock away a cute little thing like yourself for life over a little harmless fun.","standard","standard","standard","default")
    m "..."
    call ton_main("So what did you make susan do anyway? RUn around like a chicken?","standard","standard","standard","default")
    call ast_main("Not exactly...","sad","sad","sad","c_blank")
    call ton_main("Well come on then, no need to be secretive here.","standard","standard","standard","default")
    call ast_main("I might have made her show her boobs to some second years...","sad","sad","sad","c_blank")
    call ast_main("Just for a second!","sad","sad","sad","c_blank")
    call ton_main("hahahaha!","standard","standard","standard","default")
    m "(what's going on here?)"
    call ton_main("Is that all? You probably did Susan some good then, lord knows she needs to loosen up a bit.","standard","standard","standard","default")
    call ton_main("She always has been very sensitive about her body for some reason.","standard","standard","standard","default")
    call ast_main("So I'm not going to get in trouble?","sad","sad","sad","c_blank")
    call ton_main("I didn't say that... You still cast a very serious spell...","standard","standard","standard","default")
    call ton_main("However, given the circumstances, I'm going to leave your punishment in the hands of professor Dumbledore.","standard","standard","standard","default")
    m "Me?"
    call ton_main("That's not going to be an issue is it sir?","standard","standard","standard","default")
    m "Not at all!"
    call ton_main("fantastic. Now as part of standard ministry proceedings, I'm going to be staying at the school a little while longer just to ensure that there is nothing else at play.","standard","standard","standard","default")
    call ton_main("Ever since the imperio recursion event at Beauxbatons last year they've been on edge over dark wizards and these sort of spells...","standard","standard","standard","default")
    m "Alright..."
    call ton_main("I assume that I'll be allowed to sleep in the teachers quarters?","standard","standard","standard","default")
    m "Of course, I'll have a bed made up for you immediately."
    m "(I didn't even realize we had beds here, I've just been sleeping in this chair...)"
    m "(I really need to clean this thing...)"
    m "asd"



label snape_spell_intro: #Snape tells genie that he has adjusted the magic shield
    ">Snape quickly bursts into your office, his cowl flaring around him as he enters."
    call play_sound("door")
    call sna_walk("door","mid",2)
    
    sna "I've done it, Genie!"
    m "Done what?"
    m "You haven't killed anyone have you?"
    m "I can't bring people back to life Snape! don't expect me to get you out of this one..."
    sna "What? No..."
    sna "I've solved our problem with the ministry!"
    m "oh... really? How?"
    sna "It was rather ingenious honestly. I modified the muggle masking spell to include unforgivable curses!"
    m "The muggle masking spell? That sounds a little suspect..."
    sna "It's an enormous magical force-field surrounding us, Genie."
    sna "Hiding the castle and all that's in it from all non-magical beings. Making it disappear."
    sna "I was able to modify it to also shroud all unforgivable curses that are casted within it!"
    sna "Except for the deadly one, of course. The others are in my opinion quite harmless..."
    sna "You should know, magic in this world is closely monitored by the ministry of magic."
    m "And that should stop the ministry coming here?"
    sna "So long as they don't get wind of the favour trading that's happening, we shouldn't hear anymore from them!"
    sna "Can you imagine that? A whole new world of torturing and bending those filthy girls to our wills!"
    sna "I have a whole set of slytherin minxes that willingly let me to try it out on them..."
    sna "Aren't you impressed, Genie?"
    m "I suppose..."
    m "(this means I could get that little Astoria Greengrass to show me some magic...)"
    sna "What? Well what's the most impressive thing you've done with magic then?"
    m "I once changed the world into a desolate Arabian wasteland..."
    sna "..."
    sna "......"
    sna "........."
    sna "Wanna get drunk?"
    m "Do I!"
    ">You and Snape spend the rest of the evening drinking and reminiscing about past conquests..."
    jump day_main_menu


label astoria_susan_intro: #have astoria demonstrate the imperio spell for the first time on Susan
    ">You summon Astoria to your office."
    call ast_main("You wanted to see me, sir?","sad","sad","sad","c_blank")
    m "Yes. I think it's about time we addressed the issue of your punishment."
    call ast_main("oh... I was hoping you'd forgotten about that.","sad","sad","sad","c_blank")
    m "Afraid not."
    call ast_main("What am I going to have to do then?","sad","sad","sad","c_blank")
    call ast_main("I won't have to clean the toilets will I?","sad","sad","sad","c_blank")
    m "Don't worry, it's nothing like that."
    call ast_main("Oh...","sad","sad","sad","c_blank")
    call ast_main("Then what will it be?","sad","sad","sad","c_blank")
    m "First things first, I expect you to come to this office whenever I summon you from now on."
    call ast_main("What? Can't we just get this all over with at once?","sad","sad","sad","c_blank")
    m "Something like an unforgivable curse isn't so easily forgiven miss Greengrass."
    m "It's in the name!"
    m "You know what the usual punishment is..."
    call ast_main("life in Azkaban...","sad","sad","sad","c_blank")
    m "That's right... Now unless you want me to send you away, I think you better agree to this arrangement."
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("fine... but you better not be up to anything!","sad","sad","sad","c_blank")
    g4 "Me?"
    m "Never..."
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("What's your second request.","sad","sad","sad","c_blank")
    m "My second, and last request, is that you cast an unforgivable curse."
    call ast_main("{size=+10}What?{/size}","sad","sad","sad","c_blank")
    call ast_main("But I don't want to go to Azkaban! You heard what that nasty old lady said!","sad","sad","sad","c_blank")
    m "Don't worry, you won't go to Azkaban."
    call ast_main("How can you be so sure? Won't she be able to tell if I cast another one?","sad","sad","sad","c_blank")
    m "Not anymore, I've made sure that no one will be any the wiser."
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("But why do you want me to cast unforgivable curses?","sad","sad","sad","c_blank")
    m "Let's just say I'm curious."
    m "(I wanna see someone get mind controlled!)"
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("This isn't a test is it?","sad","sad","sad","c_blank")
    call ast_main("You're just getting me to cast one so that I really do get sent to Azkaban aren't you?","sad","sad","sad","c_blank")
    call ast_main("Well I won't do it!","sad","sad","sad","c_blank")
    m "I think that you're forgetting that I can already send you to Azkaban."
    call ast_main("Oh...","sad","sad","sad","c_blank")
    call ast_main("But I still don't understand, why would you want to see me cast a curse like that?","sad","sad","sad","c_blank")
    m "(Ugh...)"
    m "Because of you're exceptional skill! Not everyone can just cast a curse like that!"
    call ast_main("I suppose not... I was pretty angry when I casted it though...","sad","sad","sad","c_blank")
    call ast_main("I'm not sure if I could do it again...","sad","sad","sad","c_blank")
    m "Consider this a test then!"
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("Alright...","sad","sad","sad","c_blank")
    call ast_main("But I better not end up in Azkaban!","sad","sad","sad","c_blank")
    m "Scout's honor."
    call ast_main("Well who do you want me to cast it on?","sad","sad","sad","c_blank")
    call ast_main("It didn't work the last time I tried it on you...","sad","sad","sad","c_blank")
    m "Who did you say you casted it on last time?"
    call ast_main("Susan Bones, sir.","sad","sad","sad","c_blank")
    m "Let's just try that again, seeing as how we know that worked."
    call ast_main("What? You want me to cast a curse on another student?","sad","sad","sad","c_blank")
    m "They won't remember that we've done it will they?"
    call ast_main("I suppose not...","sad","sad","sad","c_blank")
    call ast_main("I just didn't expect you to be OK with us doing something like this...","sad","sad","sad","c_blank")
    m "Believe me, I've done worse..."
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("Alright... I'll do it.","sad","sad","sad","c_blank")
    m "Fantastic!"
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("Are you going to summon her?","sad","sad","sad","c_blank")
    m "I can't."
    call ast_main("Why not?","sad","sad","sad","c_blank")
    m "Because she hasn't visited my office yet. For some reason I can only summon people I've met before."
    call ast_main("That seems stupid.","sad","sad","sad","c_blank")
    m "You're telling me!"
    call ast_main("Should I go and get her then?","sad","sad","sad","c_blank")
    m "If you wouldn't mind."
    call ast_main("OK... what should I say to her?","sad","sad","sad","c_blank")
    m "About?"
    call ast_main("To get her to come up here!","sad","sad","sad","c_blank")
    call ast_main("I need to tell her something.","sad","sad","sad","c_blank")
    m "Just tell her I want to have a word with her."
    call ast_main("Really? Can't it be something a little more fun?","sad","sad","sad","c_blank")
    m "Fun?"
    call ast_main("You know, something to make her think she's in trouble so she's all scared and nervous when she gets up here.","sad","sad","sad","c_blank")
    m "You can tell her whatever you want, so long as you get her up here."
    call ast_main("yay!","sad","sad","sad","c_blank")
    call ast_main("I'll be right back.","sad","sad","sad","c_blank")
    show screen blkfade
    with d3
    ">Astoria leaves your office, skipping and humming as she goes."
    call hide_blkfade
    
    "..."
    pause.5
    "This might take a while"
    pause.5
    "Might as well..."
    hide screen bld1
    call gen_chibi("jerking off behind desk")
    with d3
    pause
    
    call play_sound("knocking")
    "*knock* *knock* *knock*"
    call bld
    m "Damn it. Give me a second..."
    
    call gen_chibi("hide")
    show screen genie
    with d3
    pause.2
    
    m "Come in."
    call nar(">Astoria and Susan slowly enter your office.")
    show screen astoria_greengrass
    show screen susan_bones
    g9 "!!!"
    with hpunch
    g9 "(LOOK AT THOSE KNOCKERS!)"
    m "and Who is this?!?"
    call sus_main("My name is S-Susan Bones, sir...","default","default","default","default")
    call sus_main("Astoria said you n-needed to see me urgently.","default","default","default","default")
    m "Yes... need to see... them..."
    call sus_main("...","default","default","default","default")
    call sus_main("If you don't mind me asking sir... what's this about?","default","default","default","default")
    m "Oh, um... Did Astoria not tell you?"
    call sus_main("N-no sir...","default","default","default","default")
    m "Well, Miss Greengrass and I were discussing how best to further the educat-"
    call ast_main("IMPERIO!!!","sad","sad","sad","c_blank")
    call nar(">A puff of yellow smoke appears in front of Susan's face.")
    call sus_main("W-what is thi-","default","default","default","default")
    call nar(">As quick as it appeared, it seems to fly up Susan's nose, her expression relaxing as it moves.")
    call sus_main("...","default","default","default","default")
    call nar(">Susan's eye's seem to empty as her body relaxes.")
    call ast_main("Yay! It worked!","sad","sad","sad","c_blank")
    m "Fantastic!"
    call ast_main("So what should we do now?","sad","sad","sad","c_blank")
    call ast_main("Want me to make her dance like a chicken?","sad","sad","sad","c_blank")
    m "Not exactly..."
    call ast_main("What then?","sad","sad","sad","c_blank")
    m "Well what did you do to her the first time?"
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("I can't say...","sad","sad","sad","c_blank")
    call ast_main("It's too embarrassing!","sad","sad","sad","c_blank")
    m "embarrassing? Now I have to know!"
    call ast_main("OK... but you have to promise that you won't get mad at me!","sad","sad","sad","c_blank")
    m "Sure."
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("Well a few of the other girls have been talking about...","sad","sad","sad","c_blank")
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("they were talking about breasts, sir!","sad","sad","sad","c_blank")
    g9 "(JACKPOT!)"
    m "go on..."
    call ast_main("they were talking about how boys only like big ones...","sad","sad","sad","c_blank")
    call ast_main("and that only the girls with big boobs would get asked to the autumn ball...","sad","sad","sad","c_blank")
    m "Was Susan one of these girls?"
    call ast_main("No sir. It was just a few of the \'Slytherin\' girls talking in the common room.","sad","sad","sad","c_blank")
    m "So how did Susan become involved in all this then?"
    call ast_main("It was her own fault!","sad","sad","sad","c_blank")
    m "..."
    call ast_main("What does she expect to happen when she keeps flaunting those disgusting udders of hers!","sad","sad","sad","c_blank")
    call ast_main("It's only fair that someone put her in her place!","sad","sad","sad","c_blank")
    m "And this someone was you?"
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("yes...","sad","sad","sad","c_blank")
    m "So what did you do?"
    call ast_main("...","sad","sad","sad","c_blank")
    call ast_main("I might have... made her...","sad","sad","sad","c_blank")
    call ast_main("I made her walk around without a shirt on...","sad","sad","sad","c_blank")
    m "What? Really?"
    call ast_main("I'm sorry sir! It was just around the common-room.","sad","sad","sad","c_blank")
    call ast_main("I was just so angry about her getting all the attention from the boys.","sad","sad","sad","c_blank")
    call ast_main("So I gave her all the attention she could ever ask for!","sad","sad","sad","c_blank")
    call ast_main("Although it was only around the girls common-room so it wasn't that big a deal...","sad","sad","sad","c_blank")
    call ast_main("And it's not like she can remember it anyway...","sad","sad","sad","c_blank")
    call ast_main("It was just so {b}exciting{/b} to see her taken down a notch...","sad","sad","sad","c_blank")
    m "and What did the other girls do once you started parading her around?"
    call ast_main("They were all shocked at first...","sad","sad","sad","c_blank")
    call ast_main("A few of them just told her to stop showing off and put a top on...","sad","sad","sad","c_blank")
    call ast_main("So I had to make things a little more embarrassing for her...","sad","sad","sad","c_blank")
    m "How's that?"
    call ast_main("I may have made her do a little dance...","sad","sad","sad","c_blank")
    m "A dance?"
    call ast_main("Well... it was sort of just making her shake her boobs for them...","sad","sad","sad","c_blank")
    m "Can you make her do it again?"
    call ast_main("WHAT!","sad","sad","sad","c_blank")
    call ast_main("professor! I can't do something like that!","sad","sad","sad","c_blank")
    #menu:
    #    "\"Why not?\"":
    #        call ast_main("Because... because it's wrong!","sad","sad","sad","c_blank")
    #        call ast_main("You're too old!","sad","sad","sad","c_blank")
    #        call ast_main("And you're her teacher!","sad","sad","sad","c_blank")
    #        m "So what?"
    #    "\"Come on...\"":
    #        call ast_main("...","sad","sad","sad","c_blank")
    #        call ast_main("Is this a joke sir?","sad","sad","sad","c_blank")
    #        m "Maybe..."

    call ast_main("You can't expect me to do something like that!","sad","sad","sad","c_blank")
    call ast_main("Unless...","sad","sad","sad","c_blank")
    m "Unless?"
    call ast_main("Maybe if you made it worth my while...","sad","sad","sad","c_blank")
    call ast_main("Maybe I would be OK...","sad","sad","sad","c_blank")
    call ast_main("With making Susan dance with you...","sad","sad","sad","c_blank")
    call ast_main("Maybe!","sad","sad","sad","c_blank")
    m "And what sort of reward would that be?"
    call ast_main("I want points!","sad","sad","sad","c_blank")
    m "What's your house called?"
    call ast_main("Slytherin! You should know that!","sad","sad","sad","c_blank")
    m "of course I do... I was just making sure you knew."
    call ast_main("...","sad","sad","sad","c_blank")
    m "Is that-"
    call ast_main("Not done!","sad","sad","sad","c_blank")
    call ast_main("I also expect you to teach me some new spells!","sad","sad","sad","c_blank")
    m "What?"
    call ast_main("All the spells I've been learning in class are so {b}boring!{/b}","sad","sad","sad","c_blank")
    call ast_main("Those dumb teachers only want us to learn safe spells...","sad","sad","sad","c_blank")
    call ast_main("that's part of the reason why I cursed Susan in the first place...","sad","sad","sad","c_blank")
    call ast_main("The unforgivable curses were the first fun spells I learned about!","sad","sad","sad","c_blank")
    call ast_main("Well maybe not crucio or avada kadavra...","sad","sad","sad","c_blank")
    call ast_main("But imperio!","sad","sad","sad","c_blank")
    call ast_main("It's so much fun!!!","sad","sad","sad","c_blank")
    call ast_main("I wanna learn more spells like this!","sad","sad","sad","c_blank")
    call ast_main("So I expect you to teach me them, I'm sure you know them all, old man.","sad","sad","sad","c_blank")
    m "(I don't know shit.)"
    m "Alright..."
    call ast_main("yay!","sad","sad","sad","c_blank")
    call ast_main("Well in that case...","sad","sad","sad","c_blank")
    call ast_main("Susan, give professor Dumbledore a nice dance...","sad","sad","sad","c_blank")
    call sus_main("yes...","default","default","default","default")
    call nar(">Susan starts moving her hips slowly to the sides, barely moving.")
    call ast_main("That's terrible!","sad","sad","sad","c_blank")
    call sus_main("oh...","default","default","default","default")
    call ast_main("Take your top off at least...","sad","sad","sad","c_blank")
    call ast_main("Don't worry Dumby, I'll make sure you get a good show!","sad","sad","sad","c_blank")
    m "Dumby?"
    call ast_main("short for Dumbledore!","sad","sad","sad","c_blank")
    m "oh... right..."
    call nar(">As the two of you talk Susan slowly removes her vest.")
    call ast_main("That's it Susy, one piece at a time.","sad","sad","sad","c_blank")
    m "You seemed to have changed your tone..."
    call ast_main("Because now know this isn't a test.","sad","sad","sad","c_blank")
    call nar(">Susan quietly removes her tie.")
    call ast_main("Before I was certain you were going to expel me as soon as I cast Imperio.","sad","sad","sad","c_blank")
    call ast_main("but after asking to see Susy's boobs, well...","sad","sad","sad","c_blank")
    call nar(">Susan peels her stressed shirt off.")
    call ast_main("And now I get to learn some cool new spells!","sad","sad","sad","c_blank")
    call ast_main("They better be cool old man!","sad","sad","sad","c_blank")
    call ast_main("I don't want something boring like fireworks or something.","sad","sad","sad","c_blank")
    m "What did you have in mind?"
    call ast_main("Hmmm","sad","sad","sad","c_blank")
    call ast_main("Something no one else will know!","sad","sad","sad","c_blank")
    m "so you want secret spells?"
    call ast_main("Yes! And they have to be fun as well! I don't want a secret spell to find a frog!","sad","sad","sad","c_blank")
    call nar(">Susan slowly moves her arms to unclip her bra...")
    m "ah... sure... whatever you said..."
    call ast_main("Oh...","sad","sad","sad","c_blank")
    call ast_main("Are you excited to see her boobs old man?","sad","sad","sad","c_blank")
    m "Yeah... it's not every day you get to see a pair like these..."
    call ast_main("Hmph","sad","sad","sad","c_blank")
    call ast_main("Typical...","sad","sad","sad","c_blank")
    m "Shh..."
    call ast_main("...","sad","sad","sad","c_blank")
    call nar(">Susan unceremoniously removes her bra, letting it fall to the floor.")
    m "Incredible..."
    call ast_main("They're gross...","sad","sad","sad","c_blank")
    call ast_main("Everyone {size=-2}knows {size=-2}that {size=-2}flat {size=-2}boobs {size=-2}are {size=-2}justice...{/size}","sad","sad","sad","c_blank")
    m "DIdn't you say something about making her dance..."
    call ast_main("Not anymore!","sad","sad","sad","c_blank")
    call ast_main("I think you've seen enough old man!","sad","sad","sad","c_blank")
    m "You can't be serious!"
    call ast_main("Put your clothes on, go back to your room and go to sleep Susan!","sad","sad","sad","c_blank")
    call sus_main("yes...","default","default","default","default")
    m "Aw, but we were just getting to the best bit!"
    call ast_main("You can save that for next time old man, I think you've had enough fun today.","sad","sad","sad","c_blank")
    call ast_main("Any more and you're heart will probably give out!","sad","sad","sad","c_blank")
    call ast_main("In the mean time, I want you to think up fun and secret spells!","sad","sad","sad","c_blank")
    m "Sure..."
    call ast_main("Alright, well don't bring me up here again until you've got them!","sad","sad","sad","c_blank")
    call ast_main("Good bye professor!","sad","sad","sad","c_blank")
    m "Good bye, child..."
    call ast_main("*hmph*(I'm not a child...)","sad","sad","sad","c_blank")
    ">Astoria turns heel and exits your office."
    jump day_main_menu


label snape_book_intro: #Have genie ask for a book of sex spells
    m "So to use your magic, you have to say words to cast your spells right?"
    sna "Of course! You don't think we just wiggle our noses do you?"
    m "I suppose not..."
    m "Well do you happen to have any secret spells?"
    sna "Secret spells? What for?"
    m "It's um..."
    m "It's for a student..."
    sna "What? Miss granger? You can forget all about me giving her anything!"
    m "Calm down Severus, it's not Hermione, it's someone else..."
    sna "Oh, you finally got yourself another one did you?"
    m "in a way... I'm still trying to get her to come around."
    m "But in exchange she wants me to teach her secret spells or something."
    m "I've got no idea if that's even a thing with your magic."
    sna "It is..."
    m "really? So you have some secret spells?"
    sna "I do..."
    m "What kind?"
    sna "You may find this hard to believe, but I had a bit of a troubled childhood."
    m "(Shocker...)"
    sna "..."
    sna "Anyway, I sort of turned to spell creation as a way to channel my emotions at the time."
    sna "At the age of nine I invented one of my favorite spells, {b}septum sempra{/b}."
    sna "A curse of such terrible power... Even to this day I still see all the faces of-"
    m "Yeah yeah yeah, do you have anything fun?"
    sna "Ugh, you could've at least let me finish my story."
    m "go on then..."
    sna "As I was saying, I used spells as a way to funnel my frustrations. So when I hit puberty, the spells became a little more..."
    sna "Sexual in nature..."
    m "Really? What did they do."
    sna "It's too embarrassing..."
    m "Come on man! Don't hold out on me."
    sna "I'm not going to stand here and explain them all to you."
    sna "Just take the book."
    call nar(">Snape hands you a pink leather book.")
    sna "I've written notes explaining what the spells do as well as how to cast them."
    sna "Keep in mind this sort of magic isn't quite what most students will be used to."
    sna "It's based on a far more primal magic, based off of emotions rather than words."
    sna "It'll take a fair bit of practice before they'll be able to give them a go."
    m "Thanks, even if she can't manage to cast them, the fact you made them should get her off my back."
    sna "Will that be all Genie?"
    m "I guess... Unless you fancy a drink?"
    sna "I thought you'd never ask."
    ">You and Snape sit next to the fire, recounting past conquests and enjoying the platonic company."
    jump day_main_menu
    























label astoria_tonks_intro: #occurs after you get the book from Snape
    call play_sound("knocking")
    "*knock* *Knock* *Thwump*"
    
    ">Your door is flung open as Tonks enters the room, a worried look covering her face."
    call ton_main("Sir, I have reason to believe that there is in fact a dark wizard operating somewhere on the grounds.","standard","standard","standard","default")
    m "A dark wizard?"
    m "Surely you meant to say an African American wizard?"
    call ton_main("This isn't the time for your stupid jokes, Professor!","standard","standard","standard","default")
    call ton_main("I've recently detected another instance of an unforgivable curse being cast in my vicinity.","standard","standard","standard","default")
    call ton_main("But what's really troubling is that the ministry hasn't contacted me...","standard","standard","standard","default")
    call ton_main("It must mean that the wizard is concealing themselves to the ministries global detection spell.","standard","standard","standard","default")
    call ton_main("We have to evacuate the school until they're caught... We can't risk the death of a student...","standard","standard","standard","default")
    m "Oh... I think those spells you were picking up on might have involved me..."
    call ton_main("you can't mean...","standard","standard","standard","default")
    call ton_main("You're the dark wizard???","standard","standard","standard","default")
    m "I told you, I don't think you can say that anymore..."
    call ton_main("THIS IS NO LAUGHING MATTER!","standard","standard","standard","default")
    m "I'm not a \'dark\' wizard! the spells are occurring under my strict supervision."
    call ton_main("You mean you've been letting students cast unforgivable curses? And hiding it from the Ministry?","standard","standard","standard","default")
    call ton_main("What are you thinking?","standard","standard","standard","default")
    m "As headmaster of this school, I believe that teaching students is my business, thank you very much."
    call ton_main("Well unforgivable curses are my business, Dumbledore!","standard","standard","standard","default")
    call ton_main("I demand you explain what's going on before I Floo back to the ministry and tell them everything!","standard","standard","standard","default")
    m "(Shit...)"
    m "Alright fine..."
    m "I've been tutoring a student..."
    call ton_main("In the dark arts? Are you crazy?","standard","standard","standard","default")
    m "Don't worry, I'm not letting her kill anyone..."
    call ton_main("Her? Who exactly are you tutoring then?","standard","standard","standard","default")
    m "Astoria Greengrass. I believe you've met--"
    call ton_main("Astoria? You mean that cute little lo--{p}lady...","standard","standard","standard","default")
    call ton_main("Why on earth are you teaching her curses?","standard","standard","standard","default")
    m "Miss Greengrass approached me about wanting to learn some more advanced spells."
    call ton_main("So you decided to teach her how to cast Imperio???","standard","standard","standard","default")
    call ton_main("And if she's casting imperio under your supervision, then who is the cursee?","standard","standard","standard","default")
    call ton_main("I don't suppose you'd let her curse you.","standard","standard","standard","default")
    m "Remember your niece?"
    call ton_main("SUSAN?","standard","standard","standard","default")
    call ton_main("You cannot be serious!!! {p}What sort of school are you running here?","standard","standard","standard","default")
    m "A magic one?"
    call ton_main("...","standard","standard","standard","default")
    call ton_main("What are you and Astoria making Susan do then?","standard","standard","standard","default")
    m "Oh... um..."
    m "Dancing like a chicken?"
    call ton_main("Really...","standard","standard","standard","default")
    call ton_main("You honestly expect me to believe that?","standard","standard","standard","default")
    m "It was worth a shot."
    call ton_main("So let me get this straight...","standard","standard","standard","default")
    call ton_main("You've been teaching dark arts to a student, concealing your actions from the ministry of magic...","standard","standard","standard","default")
    call ton_main("And controlling my niece to do who knows what?","standard","standard","standard","default")
    call ton_main("Do you have any idea how much trouble you're in?","standard","standard","standard","default")
    m "Is that a rhetorical question?"
    call ton_main("...","standard","standard","standard","default")
    call ton_main("This probably means that those letters from Miss Granger were actually telling the truth as well.","standard","standard","standard","default")
    m "What letters?"
    call ton_main("The ministry received a formal complaint from miss granger a few weeks ago about a sexual favour ring at hogwarts.","standard","standard","standard","default")
    call ton_main("Obviously the ministry ignored the matter. I mean who could believe that the famous Albus Dumbledore would let something like that happen...","standard","standard","standard","default")
    call ton_main("But now I'm not so sure...","standard","standard","standard","default")
    m "..."
    call ton_main("So is it true then?","standard","standard","standard","default")
    call ton_main("Are you fucking your students Dumbledore?","standard","standard","standard","default")
    call ton_main("Or are you just covering up for the other teachers here?","standard","standard","standard","default")
    menu:
        "-lie-":
            m "I'd never allow--"
        "-tell the truth-":
            m "It all started--"
    call ton_main("I don't care, either way you're going to Azkaban for the rest of your life...","standard","standard","standard","default")
    m "*gulp*"
    call ton_main("Unless...","standard","standard","standard","default")
    m "Unless what?"
    call ton_main("Do you have an opening for a defense against the dark arts professor?","standard","standard","standard","default")
    m "..."
    m "What?"
    call ton_main("Ugh... You can't think I like being an auror do you?","standard","standard","standard","default")
    call ton_main("It's just constant busy work...","standard","standard","standard","default")
    call ton_main("Not to mention the hours.","standard","standard","standard","default")
    call ton_main("And the mortality rate...","standard","standard","standard","default")
    call ton_main("If I'd realized the benefits of being a teacher at hogwarts, I would have signed up straight away!","standard","standard","standard","default")
    m "benefits?"
    m "You mean the favour trading?"
    call ton_main("no, I mean the health care... Of course I mean the favour trading Dumbledore!","standard","standard","standard","default")
    call ton_main("I always assumed that you and Snape wouldn't allow holding hands in the corridors...","standard","standard","standard","default")
    call ton_main("But if you're playing around with your students...","standard","standard","standard","default")
    call ton_main("Well let's just say I want in.","standard","standard","standard","default")
    m "(...)"
    m "You are hired!"
    m "Consider yourself the new defense of the ancients teacher or whatever..."
    call ton_main("What about Quirrel?","standard","standard","standard","default")
    m "Who?"
    call ton_main("The current defense against the dark arts professor...","standard","standard","standard","default")
    m "Oh yeah... I'll get snape to deal with him..."
    call ton_main("So snape is in on this too?","standard","standard","standard","default")
    m "Yeah..."
    call ton_main("Huh... I didn't think that sad sack even knew what fun was...","standard","standard","standard","default")
    call ton_main("So what's the going rate around here then?","standard","standard","standard","default")
    m "Going rate?"
    call ton_main("How much do you pay your students to fool around?","standard","standard","standard","default")
    m "Oh... It depends on what you want them to do."
    call ton_main("How much for a lap dance?","standard","standard","standard","default")
    m "Again, it depends on the student."
    call ton_main("...","standard","standard","standard","default")
    m "But if I had to guess, I'd say about 25 points."
    call ton_main("Wait...","standard","standard","standard","default")
    call ton_main("You pay them in points?","standard","standard","standard","default")
    m "Most of them."
    call ton_main("So you've managed to convince these girls to offer themselves up for a bunch of imaginary points that don't mean anything?","standard","standard","standard","default")
    m "Works for the internet..."
    call ton_main("what?","standard","standard","standard","default")
    m "Anyway, you can't just ask for a lap dance straight away, You have to butter them up first."
    call ton_main("how so?","standard","standard","standard","default")
    m "Well most of them aren't going to just do whatever you say from the get go..."
    m "You have to slowly earn their trust over time and start out small..."
    call ton_main("Awww really... Can't I just cheat a bit?","standard","standard","standard","default")
    m "..."
    m "Just take it slow alright, I'm sure you'll find a cute boy who'll be willing to do whatever you want anyway."
    call ton_main("...And what if I want a girl?","standard","standard","standard","default")
    m "Whatever floats your boat."
    call ton_main("Well what if I want a specific girl?","standard","standard","standard","default")
    m "which one?"
    call ton_main("Astoria Greengrass.","standard","standard","standard","default")
    m "Astoria? Isn't she a little-"
    call ton_main("She's perfect! She's just so cute and innocent... I can't wait to gobble her up!","standard","standard","standard","default")
    call ton_main("mmm... I bet she tastes like heaven...","standard","standard","standard","default")
    m "..."
    m "I'm not sure if she'd be up for that to be honest-"
    call ton_main("Well you better make her up for it then...","standard","standard","standard","default")
    call ton_main("Unless I need to tell the ministry about all this...","standard","standard","standard","default")
    m "Fine..."
    call ton_main("Good... I expect her to pay me a little visit soon.","standard","standard","standard","default")
    m "..."
    call ton_main("Now if that's all I'll be off.","standard","standard","standard","default")
    m "Sure..."
    ">Tonks turns and leaves your office."
    m "..."
    m "Did I just become a pimp?"

    jump day_main_menu
    







label astoria_book_intro: #Summon Astoria and tell her that you have a book of spells as well as the pimping with Tonks
    #Summon Astoria to your office
    #Tell her you have a book of new spells for her
    #She's very excited, says she can't wait to learn them all
    #Tell her that as payment for her learning these new spells, she'll have to do something for Genie
    #Explain that she will have to go see Tonks now
    #Astoria shocked, upset that she has to go see the Auror, scared about Azkaban
    #Genie tells her not to worry, that she will come back to his office afterwards just to make sure she's alright
    #She reluctantly agrees
    


























































