label luna_reverted_greeting_1: #reverted Luna explains the wrackspurt problem #DONE

    $ days_to_luna = 3
    $ lun_corruption = -1 #Triggers event during the evening.

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

    $ lun_genie_name = "Sir" #reset genie's name with Luna
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
            m "(SHe's probably here because of that thing with the hat!)"
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
    call lun_main("it's like a big hollow tree...","normal","base","sad","R")
    m "..."
    m "(What?)"
    m "Can I help you with something?"
    call lun_main("oh... there was something I came here for, wasn't there...","upset","base","sad","down")
    m "(What's going on here? I thought the hat wiped her mind!)"
    call lun_main("I remember! The wrackspurt infestation!","base","happyCl","sad","R")

    menu:
        "\"Wrackspurts?... Is that some sort of wizard STD?\"":
            call lun_main("Hahaha, I guess you could say that! ","base","base","sad","R")
            call lun_main("Wrackspurts are invisible creatures which float into a person’s ear and make their brain go all fuzzy.","normal","base","sad","mid")
            $ luna_l_arm = 2
            call lun_main("You can only view them wearing these spectrespecs!","base","base","base","L")
            $ luna_l_arm = 1
            m "I see... (This bitch really is crazy!)"
            m "(Maybe the hat was good for her...)"
            m "Well, Miss Lovegood, what can we do about it?"
            call lun_main("I am not sure, professor... normally thinking positive thoughts is enough to remove them, but I am having trouble with these. If my father, Xenophilius-","normal","angry","sad","R")
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
            "*You can see Luna is rocking her pelvis as though she were grinding the air*"
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
            m "Ah yes, very nice..."
            m "So about these wrecksputs..."

    call lun_main("Yes, Sir, they’re proving to be quite a pain.","normal","closed","sad","mid")

    "*Luna is visibly grinding her pelvis against her thighs.*"
    m "(Is she really?... Ohhh). Miss Lovegood, how exactly do these wickspurts make you feel?"
    call lun_main("they're Just like the quibbler says sir, except...","normal","seductive","sad","R")
    m "Go on..."
    call lun_main("Well, it's not my brain they're making fuzzy.","soft","seductive","sad","down")
    m "Where exactly is fuzzy, Miss Lovegood?"
    call lun_main("Umm... I'm not sure if I can say...","normal","seductive","sad","R")
    m "(YES!)"
    m "Now now, Miss Lovegood, as your headmaster there shouldn't be anything that you can't say to me."
    call lun_main("Well alright...","base","seductive","sad","down")
    call lun_main("the fuzziness is in between my legs, sir...","base","seductive","sad","mid")
    m "Really? That seems quite strange..."
    call lun_main("It is sir! I've only ever heard of people's brains going fuzzy...","normal","base","sad","mid")
    call lun_main("but this...","normal","angry","sad","mid")
    call lun_main("it's like this unbearable itch I can't scratch...","upset","seductive","sad","down")
    m "(I know that feeling.)"
    call lun_main("and I feel like I can't quite remember what I've been up to over the last few days...","normal","suspicious","sad","R")
    m "Oh um... I wouldn't worry about that at all..."
    m "Let's just focus on this fuzziness of yours."
    call lun_main("Alright, professor...","normal","seductive","sad","down")
    call lun_main("As I was saying, this fuzziness has really been bothering me the last few days...","normal","seductive","sad","mid")
    m "Hmmm, has it been affecting your studies at all?"
    call lun_main("yes, it has, sir...","upset","seductive","sad","down")
    m "Well, we can't have that now, can we?"
    call lun_main("no, sir...","base","seductive","sad","mid")
    m "Are you free at the moment?"
    call lun_main("Umm... I'm about to go to divination class, sir...","normal","seductive","sad","down")
    m "Well, in that case, we'll address that nasty itch of yours later on."
    m "Come to my office later tonight, and we'll see what we can do."
    call lun_main("Oh, thank you, sir!","base","wide","sad","mid")
    call lun_main("I can't wait!","base","seductive","sad","mid")
    call lun_main("Do you think you could possibly stop the nargles stealing my shoes as well?","base","base","sad","down")
    m "(What the hell is a nargle?)"
    m "One step at a time, Miss Lovegood."
    call lun_main("yes, you're right... the nargles wouldn't like it if we were multitasking...","normal","closed","sad","mid")
    m "..."
    call lun_main("well, I'd best be off... goodbye professor!","base","happyCl","base","mid")
    "*Luna skips out of the room, squeezing her legs together as she prances*"
    m "(This is going to be fun!)"

    jump luna_away

label luna_reverted_greeting_2: #Explaining to Luna what will happen or something #DONE
    $ lun_corruption = 0

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
    m "yes, I see how that could be dangerous..."
    call nar("*Luna starts grinding her thighs together.*")
    call lun_main("yes...","base","seductive","sad","down")
    call lun_main("So, about this itch, sir...","base","seductive","sad","mid")
    m "Yes."
    call lun_main("Did you say you had some way to get rid of it?","normal","seductive","sad","mid")
    m "I did."
    call lun_main("well...","upset","seductive","sad","R")
    m "well, the first thing's first I need something from you, Miss Lovegood."
    call lun_main("Something from me?","pout","wide","sad","mid")
    m "Yes, I need a promise."
    call lun_main("oh...","normal","base","sad","R")
    call lun_main("alright then!","base","happyCl","sad","mid")
    m "I haven't even told you what it is yet."
    call lun_main("Don't worry sir, I trust you!","base","wide","base","mid")
    m "(this might be too easy!)"
    m "Yes well, the techniques I'm going to be showing you are proprietary so I'm going to have to make you promise not to talk to anyone about what goes on in this room."
    call lun_main("techniques...","normal","seductive","sad","R")
    call lun_main("proprietary...","upset","seductive","sad","down")
    call lun_main("I'm not sure I understand, sir.","normal","seductive","sad","mid")
    m "Well, if what you're saying is correct, even if I use some powerful magic to remove them..."
    m "(I hope she buys this...)"
    m "They'll soon be back, and in greater numbers."
    call lun_main("...","normal","seductive","sad","R")
    m "(Did she buy it?)"
    call lun_main("yes, You're right, sir.","normal","closed","sad","R")
    m "(YES!)"
    call lun_main("But are there really techniques to dispell them?","normal","seductive","raised","mid")
    m "There are, but as I said, if you want to learn them you have to promise not to tell anyone what happens here."
    call lun_main("I suppose that's only fair, This information would be worth more than a snorkack sighting!","base","base","sad","mid")
    m "..."
    m "well, it's Not just the techniques Miss Lovegood."
    m "You must promise to tell anyone anything that happens in this room, no matter what."
    call lun_main("well...","normal","seductive","sad","R")
    call nar("*You can see Luna is awkwardly rocking her pelvis*")
    call lun_main("alright then...","base","seductive","sad","mid")
    call lun_main("I solemnly swear that I will tell no one what happens within these hallowed walls...","normal","closed","base","R")
    m "Fantastic!"
    call lun_main("so can you please teach me the techniques sir?","base","wide","sad","mid")
    call nar(">There's a desperate need in Luna's eyes that excites you to no end.")
    m "yes, yes. I think I've made you wait long enough."
    call lun_main("Thank you so much!","base","happyCl","base","R")
    m "No need to thank me, Miss Lovegood, I'm simply doing what any good teacher should."
    m "Now, stand in the middle of the room for me."
    hide screen luna_main
    with d3

    call lun_main("is Here ok?","pout","base","sad","mid",xpos="mid",ypos="base")
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
    call lun_main("thank you, Sir!","base","happyCl","sad","R")
    m "You're quite welcome."
    call lun_main("...","base","base","sad","down")
    $ luna_l_arm = 4
    call nar(">Luna quickly puts her hand down her skirt, barely acknowledging the nature of her actions.")
    call lun_main("ah...","normal","seductive","sad","down")
    m "Is everything alright, Miss Lovegood?"
    call lun_main("ah... of course!","base","wide","sad","mid")
    call lun_main("It's just a little sensitive...","base","seductive","sad","down")
    m "That's to be expected. Keep going."
    call lun_main("ah... yes sir...","normal","happyCl","sad","R")
    g4 "..."
    call lun_main("ah... is this how it should be done?","pout","base","sad","mid")
    m "As long as it's feeling good I'm sure it's working. If you keep this up I'm sure you'll be rid of those nasty wickerspoons."
    call lun_main("that's nice...","base","closed","sad","R")
    call lun_main("...","normal","base","sad","mid")
    call lun_main("are you sure this will work, sir?","soft","seductive","sad","mid")
    m "Of course I am! Do you dare doubt the powerful Dumbelldoor?"
    call lun_main("certainly not, sir...","normal","wide","sad","R")
    call lun_main("it's just...","normal","seductive","sad","down")
    call lun_main("I'm not sure this is going to get rid of them...","pout","seductive","sad","mid")
    m "What makes you say that?"
    call lun_main("do you remember how I said the wickerspats were like a nasty itch, sir?","normal","seductive","sad","R")
    m "I do."
    call lun_main("well... as nice as this massage feels...","normal","seductive","sad","down")
    call lun_main("it's not really scratching that itch sir...","pout","angry","sad","mid")
    call lun_main("... {p}am I doing it wrong, sir?","normal","seductive","sad","mid")
    m "Certainly not, but this is worse than I feared."
    call lun_main("really?","normal","wide","sad","mid")
    m "Yes. It would seem that those nasty critters are trying to hide."
    call lun_main("Hide? Where?","normal","wide","sad","down")
    m "Well, as long as you're still feeling that itch they can't have gone far."
    m "But this means you'll have to chase them down."
    call lun_main("chase them down?","normal","seductive","raised","mid")
    m "Don't worry, I'll be here to guide you through it."
    call lun_main("thank you, sir.","base","base","sad","R")
    m "First things first, close your eyes."
    call lun_main("...","normal","happyCl","sad","R")
    m "Very good. Now I want you to block everything else out."
    call lun_main("alright, sir...","upset","happyCl","sad","R")
    m "Imagine it's just you alone in your room."
    call lun_main("yes...","normal","happyCl","sad","R")
    m "Nice and cozy. Not a care in the world."
    call lun_main("...","base","happyCl","sad","R")
    m "Now, focus on where the itch is strongest."
    call lun_main("Ah... alright...","base","happyCl","base","R")
    m "I want you to chase that feeling with your fingers."
    call lun_main("...","normal","happyCl","base","R")
    m "Focus on catching it."
    call lun_main("I can't...","pout","happyCl","sad","R")
    call lun_main("It's like trying to grab rays of sunlight...","normal","happyCl","sad","R")
    m "Don't try and grab a hold of it, just brush against it with the tips of your fingers."
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("...","base","happyCl","base","R")
    call nar(">Luna starts dancing her fingers along under her skirt.")
    call lun_main("ah...","base","happyCl","sad","R")
    call lun_main("mmm...","grin","happyCl","sad","R")
    call nar(">Luna starts to softly moan under her breath.")
    call lun_main("I'm close sir...","base","happyCl","sad","R")
    m "Good. Just keep your eyes closed and focus on your fingers."
    call lun_main("{image=textheart}","grin","happyCl","base","R")
    call lun_main("ah... I think it's working, sir!","base","happyCl","sad","R")
    call lun_main("I think I'm about to catch it!","base","happyCl","base","R")
    m "Shhh, don't speak, just focus..."
    call lun_main("ok...","normal","happyCl","sad","R")
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("ah...","grin","happyCl","sad","R")
    call lun_main("{image=textheart}","base","happyCl","sad","R")
    call lun_main("...","upset","happyCl","sad","R")
    call lun_main("ah... sir...","normal","seductive","sad","mid")
    call lun_main("I think...","grin","seductive","sad","down")
    call lun_main("ah...","grin","seductive","sad","R")
    call lun_main("I think I've almost got it...","grin","happyCl","sad","R")
    m "Shhh..."
    call lun_main("ah...","grin","happyCl","angry","mid")
    call nar(">Luna's fingers start furiously dancing underneath her skirt.")
    call lun_main("mmmm...","base","happyCl","angry","mid")
    call lun_main("ah...","grin","happyCl","angry","mid")
    call lun_main("a-ah...","base","seductive","sad","down")
    call lun_main("yes...","base","seductive","angry","mid")
    m "(I think this is it!)"
    call lun_main("Ah... ah...{image=textheart}","grin","seductive","sad","R")
    call lun_main("{size=+4}mmm... yes...{image=textheart}{/size}","base","seductive","sad","down")
    call lun_main("{size=+8}ah... ah...{/size}","grin","seductive","sad","mid")
    call lun_main("!!!","grin","wide","base","empty")
    call nar(">There's a blur of movement under Luna's skirt.")
    call lun_main("ah! I think they're attacking me, sir!","base","wide","sad","mid")
    call lun_main("!!!","base","base","sad","empty")
    m "Is everything OK?"
    call lun_main("Ah... yes sir...{image=textheart}","normal","seductive","sad","R")
    call lun_main("it's just...","base","seductive","sad","R")
    m "..."
    call lun_main("I-I've never...","normal","seductive","sad","R")
    call lun_main("...","base","seductive","sad","down")
    call lun_main("{size=-5}Ah...{/size}","base","seductive","sad","R")
    m "so Have the wickspots left you alone?"
    call lun_main("I think so, sir...","normal","seductive","sad","mid")
    $ luna_l_arm = 1
    call nar(">Luna slowly pulls her hand out from under her skirt.")
    call lun_main("at least That nasty itch seems to have gone away.","base","base","sad","mid")
    m "Fantastic! will that be all then, Miss Lovegood."
    call lun_main("OH... did you want me to leave already, sir?","normal","seductive","sad","down")
    m "If there's nothing else I can help you with."
    call lun_main("I suppose not... but what if the feeling comes back, sir?","upset","seductive","sad","R")
    call lun_main("Should I try and get rid of them myself?","normal","seductive","sad","down")
    m "Certainly not!"
    call lun_main("Really? Why not?","normal","wide","sad","mid")
    m "as I said earlier miss lovegood, These techniques are to be kept secret."
    m "Not to mention dispelling them in your common room could lead to a school wide outbreak."
    call lun_main("So what can I do if they come back?","normal","base","sad","mid")
    m "If you ever feel like you need to relieve yourself of those pesky little things again, my door is always open."
    call lun_main("Are you sure, sir?","normal","seductive","sad","mid")
    call lun_main("I wouldn't want to bother you...","normal","seductive","sad","R")
    m "You'd be doing no such thing! besides, I've been meaning to test these sort of techniques for a while now."
    m "If anything you'll be helping me with important research."
    call lun_main("Really? thank you very much, sir.","base","wide","base","mid")
    call lun_main("Hopefully they leave me alone, but if not I'll come and visit you again.","base","base","sad","R")
    m "I look forward to it."
    call lun_main("...","base","seductive","sad","mid")
    call nar(">Luna gives you one last smile before leaving your office.")

    jump luna_away

label luna_cum_addict_event:
    $ luna_addicted = True #luna is now a cum addict. I'm a bit undecided about the whole thing tbh, might ruin the dom path but idk, we can work it in, make her a dommy cumslut or whatever........
    ">You put your arms on Luna's shoulders forcing her to her knees."
    $ luna_l_arm = 2
    $ luna_r_arm = 2
    $ genie_base = "characters/genie/base/hard.png"
    call gen_main("Down we go!","grin")
    $ luna_ypos = 225
    $ luna_xpos = 350
    call lun_main("Stop right now! This wasn't an option [lun_genie_name]!","open","wide","mad","mid")
    g4 "Argh, too late slut!"
    call lun_main("!!!","upset","closed","mad","mid")
    $ luna_cum = 11
    call cum_block

    $ luna_wear_cum = True
    ">You coat Luna's furious expression in a wave of hot cum!"
    pause
    g4 "Argh! by the gods {size=+10}YES!{/size}"
    call lun_main("...","normal","seductive","base","crossed")
    call lun_main("(What's this smell?)","pout","seductive","sad","downL")
    g4 "{size=+10}TAKE IT ALL YOU big titted sLUT!{/size}"
    g4 "mmmm....."
    hide screen g_c_c_u
    $ g_c_u_pic = "images/animation/06_jerking_01.png"
    $ luna_r_arm = 2
    hide screen genie_main
    $ genie_base = "characters/genie/base/open.png"
    with d3
    m "That hit the spot..."
    call lun_main("...","pout","mad","mad","L")
    call lun_main("......","normal","angry","angry","downL")
    call lun_main(".........","base","seductive","sad","empty")
    m "Ahh... that was fantastic slut..."
    $ g_c_u_pic = "images/animation/06_groping_01.png"
    call lun_main("What {size=+4}is {size=+4}this {size=+4}smell?{/size}","base","wide","sad","mid")
    m "Cum?"
    ">Luna gets up from her knees"
    $ luna_ypos = 0
    call lun_main("{size=+4}it{/size}","upset","suspicious","mad","L")
    call lun_main("{size=+8}smells{/size}","normal","mad","angry","downL")
    call lun_main("{size=+12}incredible!!!{/size}","base","wide","sad","empty")
    m "..."
    m "What?"
    call lun_main("my god!!! there's so much magical energy in it!","base","wide","sad","mid")
    call lun_main("I've never sensed anything this powerful before!","base","wide","sad","down")
    m "Ah yes, well I am the great fumblemore!"
    call lun_main("...","pout","angry","angry","mid")
    call lun_main("This smell... it's too much for a mortal to make...","base","angry","base","mid")
    m "(Shit...)"
    call lun_main("can I...","normal","base","sad","mid")
    call lun_main("taste it?","normal","seductive","sad","R")
    m "What sort of question is that?"
    call lun_main("If it's too much...","normal","wide","sad","mid")
    g9 "Of course you can taste my cum girl!"
    call lun_main("thank you sir...","base","wide","sad","mid")
    m "(She seems different...)"
    $ luna_cum = 12
    ">Luna collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","full","seductive","sad","empty")
    call lun_main("{size=+4}It's {size=+4}amazing!!!!!{image=textheart}{image=textheart}{/size}","base","happyCl","sad","mid")
    call lun_main("can I have the rest? Please sir?","base","wide","sad","mid")
    m "Sure..."
    ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
    $ luna_cum = 13
    call lun_main("...","full","seductive","sad","empty")
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
    pause
    $ luna_cum = 14
    call lun_main("...","full","seductive","sad","empty")
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
    $ luna_cum = 15
    call lun_main("...","full","seductive","sad","empty")
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
    $ luna_wear_cum = False
    call lun_main("ah...","base","happyCl","sad","mid")
    call lun_main("amazing...","base","seductive","sad","mid")
    m "Enjoy yourself did we?"
    call lun_main("How could I not?","pout","angry","angry","R")
    m "(What is going on here? SHe seems all bitchy again...)"
    call lun_main("You have to tell me how you did that!","normal","mad","angry","mid")
    m "Cum? I'm pretty sure you've got that all worked out..."
    call lun_main("Not that, idiot!","normal","suspicious","mad","mid")
    call lun_main("why did it contain so much magical energy?","normal","angry","angry","mid")
    call lun_main("we lovegoods are sensitive to magic, but The only thing I've ever experienced like this was when I was allowed in the same room as some essence of Djinn...","pout","angry","mad","R")
    call lun_main("But everyone knows the Djinn were hunted to extinction millenia ago...","normal","mad","angry","mid")
    g4 "(!!!)"
    m "oh, um..."
    m "Trade secret..."
    call lun_main("Fine! Be that way then [lun_genie_name]...","pout","suspicious","angry","R")
    ">Luna gets dressed in front of you in a huff."

    call load_luna_clothing_saves

    call lun_main("Just don't expect me to let you get away with wasting that spunk anymore [lun_genie_name]!","normal","mad","angry","mid")

    m "well... anyway, Here's your payment, [luna_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    ">You hand Luna [current_payout] gold."
    call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")

    jump luna_away #DONE

label luna_reverted_event_1: #Masturbate for genie again. #DONE
    $ lun_corruption = 1
    $ days_to_luna = 4

    call play_sound("knocking")
    "*knock* *knock* *knock*"
    m "Come in..."

    call play_sound("door")
    call lun_walk("door","mid",2.5)
    pause.5

    call lun_main("Hello again, [lun_genie_name]...","base","happyCl","base","mid",xpos="right",ypos="base")
    m "Miss Lovegood. How have you been?"
    call lun_main("Alright... but the wrackspurts seem to have come back..","upset","base","angry","R")
    m "Again? So soon?"
    call lun_main("I'm afraid so [lun_genie_name]...","normal","base","sad","mid")
    call lun_main("Everytime I think about what we did in here...","normal","wide","sad","mid")
    call lun_main("It just makes them feel so much... stronger...","normal","angry","sad","R")
    m "Yes... They must be afraid of my powerful techniques..."
    call lun_main("Do you think so?","normal","closed","sad","R")
    m "I do..."
    m "Why else would they attack you when you think about curing them?"
    call lun_main("You're right...","normal","angry","sad","mid")
    m "So... Are you ready to try and dispel them again?"
    call lun_main("Only if it's not too much trouble [lun_genie_name]... I wouldn't want to disturb you...","upset","angry","sad","R")
    m "Please, as headmaster it's my duty to make sure my students are safe..."
    call lun_main("You're right...","normal","seductive","sad","down")
    call lun_main("I just feel guilty coming up her so often...","normal","seductive","sad","R")
    m "don't..."
    "*Luna starts grinding her thighs together.*"
    call lun_main("Ok...","base","seductive","sad","down")
    call lun_main("So, is it OK if I start scratching...","base","seductive","sad","mid")
    m "I don't see why not. Just stand in the middle of the room for me."
    hide screen luna_main
    with d3

    call lun_main("...","pout","base","sad","mid",xpos="mid",ypos="base")
    m "That's it..."
    m "Would you like to start Miss lovegood?"
    $ luna_l_arm = 4
    call nar(">Luna quickly puts her hand down her skirt, barely waiting for you to finish your sentence...")
    call lun_main("ah... thank you [lun_genie_name]...","normal","seductive","sad","down")
    m "You seem relieved..."
    call lun_main("ah... of course... I've been waiting to come here since yesterday...","base","wide","sad","mid")
    call lun_main("I think Those slimy wrackspurts have infested the commonroom...","base","seductive","sad","down")
    m "That's quite possible..."
    call lun_main("ah... ah...","normal","happyCl","sad","R")
    call lun_main("but getting rid of them... feels... so... good...","pout","base","sad","mid")
    call lun_main("I'm almost glad I've got them...","pout","base","sad","mid")
    m "The positive feelings you have are your body reacting to the wickerspats being expelled from your body."
    call lun_main("really?","base","closed","sad","R")
    call lun_main("ah...","normal","base","sad","mid")
    call lun_main("I must... ah... be expelling a lot then...","soft","seductive","sad","mid")
    call lun_main("in fact...","normal","wide","sad","R")
    call lun_main("ah...","normal","seductive","sad","down")
    call lun_main("I think... ah... I'm about to... ah...","pout","seductive","sad","mid")
    call lun_main("Mmmm, it's just like... last time...","normal","seductive","sad","R")
    m "Oh, are you cumming already?"
    call lun_main("cumming?","normal","seductive","sad","down")
    call lun_main("what's? ah...{image=textheart}","pout","angry","sad","mid")
    call lun_main("Cumming?{image=textheart}","normal","seductive","sad","mid")
    call lun_main("Ah... I'm cumming...{image=textheart}{image=textheart}","normal","wide","sad","mid")
    m "Mmmmm that's it girl..."
    call lun_main("Ah...{image=textheart}","normal","wide","sad","down")
    call nar(">You see a flush of red roll over Luna's face as her body twitches with the throes of her orgasm.","start")
    call nar(">However despite this, her fingers remain a flurry of movement under her skirt.","end")
    m "Well, it seems those wickedspots have been giving you a bit of grief now haven't they?"
    label luna_masturbate_again:
        pass
    call lun_main("ah...{image=textheart}yes{image=textheart}","normal","seductive","raised","mid")
    m "Don't worry, that should sort them out for now..."
    call lun_main("ummm...","base","base","sad","R")
    m "What's wrong?"
    call lun_main("...","normal","happyCl","sad","R")
    call lun_main("is it...","upset","happyCl","sad","R")
    call lun_main("Ok if I do it once more?","normal","happyCl","sad","R")
    m "What?"
    call lun_main("If you need to do other things I can leave!","base","happyCl","sad","R")
    m "There's no need for that! You can stay here as long as you like..."
    m "I was just a little surprised that you needed to go again is all..."
    call lun_main("Ah... well...","base","happyCl","base","R")
    call lun_main("these wrackspurts...","normal","happyCl","base","R")
    call lun_main("ah...","pout","happyCl","sad","R")
    call lun_main("they've been very tiresome...","normal","happyCl","sad","R")
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("besides...","base","happyCl","base","R")
    call nar(">Luna starts dancing her fingers along under her skirt.")
    call lun_main("ah...","base","happyCl","sad","R")
    call lun_main("I've been... waiting for this all day...","grin","happyCl","sad","R")
    call nar(">Luna starts to softly moan under her breath.")
    call lun_main("standing here...","base","happyCl","sad","R")
    m "..."
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","grin","happyCl","base","R")
    call lun_main("in front of my headmaster...","base","happyCl","sad","R")
    call lun_main("While he helps me to...","base","happyCl","base","R")
    m "Shhh, don't speak, just focus..."
    call lun_main("ok...","normal","happyCl","sad","R")
    call lun_main("...","base","happyCl","sad","R")
    call lun_main("ah...","grin","happyCl","sad","R")
    call lun_main("{image=textheart}","base","happyCl","sad","R")
    call lun_main("...","upset","happyCl","sad","R")
    call lun_main("ah... [lun_genie_name]...","normal","seductive","sad","mid")
    call lun_main("I think...","grin","seductive","sad","down")
    call lun_main("ah...","grin","seductive","sad","R")
    call lun_main("I think I've almost got them...","grin","happyCl","sad","R")
    m "Shhh..."
    call lun_main("ah...","grin","happyCl","angry","mid")
    call nar(">Luna's fingers start furiously dancing underneath her skirt.")
    call lun_main("mmmm...","base","happyCl","angry","mid")
    call lun_main("ah...","grin","happyCl","angry","mid")
    call lun_main("a-ah...","base","seductive","sad","down")
    call lun_main("yes...","base","seductive","angry","mid")
    m "(I think this is it!)"
    call lun_main("Ah... ah...{image=textheart}","grin","seductive","sad","R")
    call lun_main("{size=+4}mmm... yes...{image=textheart}{/size}","base","seductive","sad","down")
    call lun_main("{size=+8}ah... oh... frickity!!!{/size}","grin","seductive","sad","mid")
    call lun_main("!!!","grin","wide","sad","mid")
    call nar(">THere's a blur of movement under Luna's skirt.")
    call lun_main("ah! thank you, [lun_genie_name]!","base","wide","sad","mid")
    call lun_main("!!!","base","wide","sad","mid")
    m "Is everything OK?"
    call lun_main("Ah... yes{image=textheart} thank you{image=textheart} [lun_genie_name]...{image=textheart}","normal","seductive","sad","R")
    m "so Have the wickspots left you alone now?"
    call lun_main("I think so, [lun_genie_name]...","normal","seductive","sad","mid")
    $ luna_l_arm = 1
    call nar(">Luna slowly pulls her sopping hand out from under her skirt.")
    call lun_main("at least That nasty itch seems to have gone away.","base","base","sad","mid")
    m "Fantastic! will that be all then, Miss Lovegood."
    call lun_main("well I don't suppose I could go-","normal","seductive","sad","down")
    call lun_main("No... I better get to bed...","upset","seductive","sad","R")
    call lun_main("Thanks again, [lun_genie_name]!","normal","seductive","sad","down")
    m "(What an odd girl.)"
    call nar(">Luna gives you one last smile before leaving your office.")

    jump luna_away

label luna_reverted_event_2: #Masturbate for Genie and then Genie cum on Luna's face #DONE
    $ lun_corruption = 2
    $ days_to_luna = 3

    call play_sound("knocking")
    "*knock* *knock* *knock*"
    lun "Can I please come in, [lun_genie_name]?"
    call nar(">There's a desperate twang to Luna's voice.")

    menu:
        "-Let her in-":
            m "Of course."
        "-mess with her-":
            m "Who is it?"
            lun "Luna Lovegood, [lun_genie_name]..."
            lun "May I please come in?"
            m "Luna who?"
            lun "Lovegood, [lun_genie_name]..."
            m "Oh miss lovegood! Come in..."

    call play_sound("door")
    call lun_walk("door","mid",2.5)
    pause.5

    call lun_main("...","pout","annoyed","sad","R",cheeks="blush",xpos="right",ypos="base")
    m "Miss Lovegood..."
    m "What can I help you with today?"
    call lun_main("I-I... need...","soft","seductive","sad","down")
    $ luna_l_arm = 4
    call nar(">Luna quickly puts her hand down her skirt, not even waiting on your reply...")
    call lun_main("ah... I'm sorry [lun_genie_name]... I just... needed... this...{image=textheart}","base","seductive","sad","up")
    m "You seem relieved..."
    call lun_main("ah... {image=textheart} yes...","base","wide","sad","mid")
    call lun_main("these visits are starting to become all I can think about...","base","seductive","sad","down")
    m "Hmmm... Do you think that's a bad thing?"
    call lun_main("ah... of course not!","normal","happyCl","sad","R")
    call lun_main("it just... means that it's working...","pout","base","sad","mid")
    call lun_main("if only I could spend all day up here...","base","base","sad","mid")
    m "Do you think a full day of treatment would get rid of them?"
    call lun_main("ah...","base","base","sad","mid")
    call lun_main("probably not...","soft","seductive","sad","mid")
    call lun_main("but...","base","wide","sad","R")
    call lun_main("ah...","base","seductive","sad","down")
    call lun_main("I think... it'd probably feel...","soft","seductive","sad","mid")
    call lun_main("nice...{image=textheart}{image=textheart}{image=textheart}","base","seductive","sad","R")
    m "Speaking of feeling nice..."
    call lun_main("Ah... I think I'm... cumming [lun_genie_name]...","open_tongue","seductive","sad","down")
    call lun_main("ah...{image=textheart}","base","seductive","sad","mid")
    call lun_main("mmmmm{image=textheart}","base","seductive","sad","mid")
    call lun_main("Ah... I'm cumming...{image=textheart}{image=textheart}","base","wide","sad","up")
    m "Mmmmm that's it girl..."
    call lun_main("Ah...{image=textheart}","soft","seductive","sad","down", cheeks="blush")
    call nar(">You see a flush of red roll over Luna's face as her body twitches with the throes of her orgasm.","start")
    call nar(">Her fingers keep casually stroking her needy sex...","end")
    m "It seems those wickedspots have been giving you a bit of grief now haven't they?"

    menu:
        "-Start jerking off-":
            pass
        "-behave-":
            jump luna_masturbate_again

    m "Truth be told they've been starting to affect me as well..."
    call lun_main("What? They got you too?","base","angry","sad","mid")
    m "I was afraid this might happen with you dispelling all of your personal wrackspurts into this room..."
    m "This is why I didn't want you doing this outside the office..."
    call lun_main("It could have been a disaster [lun_genie_name]...","base","angry","sad","mid")
    call lun_main("But will you be alright?","soft","wink","raised","mid")
    m "Oh don't worry about me, I'm a {i}master{/i} when it comes to this..."
    call lun_main("Of course... These are your techniques after all...","base","happyCl","sad","mid")
    call lun_main("Would it...","base","seductive","sad","R")
    call lun_main("Would it be OK if I watched [lun_genie_name]?","base","annoyed","sad","mid")
    call lun_main("Just as a way to improve my own technique!","base","wink","base","mid")
    m "Mmmm, I see nothing wrong with it..."
    m "Here, I'll come give you a {b}nice{/b} view..."
    show screen blkfade
    hide screen luna_main
    with d3

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
    lun "OK [lun_genie_name], I'll take it all in!"
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
    lun "Ah... I think I should... probably leave now [lun_genie_name]..."
    m "You're not going to clean yourself up first?"
    $ ccg1 = "33"
    lun "Oh..."
    lun "If it's ok with you [lun_genie_name]... I might clean myself up back in my room..."
    m "Whatever suits you miss lovegood..."
    $ ccg1 = "30"
    lun "thank you [lun_genie_name]... for... everything..."
    m "Will that be all miss lovegood?"
    lun "Oh, um yes..."
    $ ccg1 = "32"
    lun "I'll see you the next time those wrackspurts come up again..."
    m "See that you do."
    lun "yes, [lun_genie_name]..."
    show screen blkfade
    hide screen luna_main
    hide screen ccg
    with d3

    call lun_chibi("stand","mid","base")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade
    with d3

    call lun_walk("mid","leave",2)

    $ luna_busy = True

    m "She really is a bit loony..."

    jump main_room

label luna_reverted_event_3: #Luna gentle BJ where she just happily sucks and lick it like a lollipop for an hour #DONE
    $ lun_corruption = 3
    $ days_to_luna = 4

    call play_sound("knocking")
    ">*knock* *knock* *knock*"
    call nar(">Before waiting for a response, your door swings open to reveal Luna Lovegood.")

    call play_sound("door")
    call lun_walk("door","mid",2)
    pause.5

    call lun_main("Hello, [lun_genie_name]! Lovely day today isn't it?","base","happyCl","base","mid",xpos="right",ypos="base")
    m "It is now..."
    call lun_main("Awww... that's so nice!","base","wink","sad","mid")
    m "What brings you up to my office today then Miss Lovegood?"
    m "Those troublesome little wrockspoons giving you grief again?"
    call lun_main("Not exactly...","soft","seductive","sad","down")
    m "Oh... Something else I can help you with then?"
    call lun_main("Well... I was just walking past when I remembered how those nasty wrackspurts affected you the other day...","open","base","sad","R")
    call lun_main("They aren't by any chance bothering you at the moment are they [lun_genie_name]?","base","wink","sad","mid")
    m "Now that you mention it, they have been giving me a little trouble..."
    m "But I'm much too tired to relieve them myself... I'm such an old man you see..."
    call lun_main("Really? But you look...","soft","wide","sad","mid")
    call lun_main("so you won't...","pout","annoyed","sad","down")
    call lun_main("...","normal","annoyed","sad","R")
    call lun_main("Is there any way I could help?","base","wink","sad","mid")
    m "Hmmmm... There is a special technique that I've been developing..."
    m "I'm not sure your ready for it though..."
    call lun_main("Please, [lun_genie_name]! I know I can handle it!","base","wide","sad","mid")
    m "Well if you insist..."
    m "Just make sure you don't let anyone else know about this..."
    call lun_main("I wouldn't dare... A cure for wrackspurts would be the talk of the magical world...","base","wide","angry","mid")
    m "Yes..."
    call lun_main("So what does this technique involve?","base","wink","sad","mid")
    m "It involves you sucking the nasty things out."
    call lun_main("Sucking them out!","scream","wide","mad","mid")
    m "(I wasn't sure if she'd fall for th-)"
    call lun_main("That's brilliant!","open","happyCl","base","mid")
    m "..."
    m "It is?"
    call lun_main("Of course!","base","base","sad","L")
    call lun_main("Everyone knows wrackspurts can't survive in someone's stomach!","base","happyCl","base","mid")
    m "Very good Miss Lovegood... I see you know your... magic..."
    call lun_main("Mhmm! it also allows you to just sit there and let me take get rid of them!","base","seductive","base","down")
    m "You expect me to just sit here while you suck them out?"
    call lun_main("Mhmm!","base","happyCl","base","mid")
    m "And you want that?"
    call lun_main("Only if it's not too much trouble, [lun_genie_name], I know you must be busy...","normal","wink","sad","R")
    m "No trouble at all..."
    call lun_main("Hooray!","base","wide","base","empty")
    call lun_main("Now how's this secret technique work?","base","wink","raised","mid")
    m "Seeing as how you offered to do this while I was sitting, why don't you come over here."
    call lun_main("Can I hide under your desk?","base","base","base","mid")
    m "You don't have to, I can turn the chair around."
    call lun_main("Oh no, I want to...","base","wink","sad","R")
    call lun_main("I've always been rather fond of small spaces like that ever since I was a little girl...","base","base","sad","down")
    call lun_main("I used to hide in the roots of a huge Wiggentree near our home...","soft","seductive","sad","down")
    call lun_main("I've never felt as safe as I did when was under the roots of that tree...","base","happyCl","base","mid")
    call lun_main("It's like the wood wrapped around to hug me when it was cold...","base","seductive","base","R")
    call lun_main("...","base","seductive","sad","down")
    m "..."
    m "If you want to crawl under the desk feel free..."
    call lun_main("Thank you, [lun_genie_name]...","base","happyCl","base","mid")

    label luna_blowjob_under_desk:
        pass
    show screen blkfade
    hide screen luna_main
    with d3

    ">Luna quickly walks around your desk and crawls under your spacious desk..."
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
    lun "Can't you feel it, [lun_genie_name]?"
    $ ccg1 = "4"
    lun "It's so heavy in the air... It's {b}all{/b} over the wood..."
    $ ccg1 = "5"
    lun "You can almost taste it..."
    ">Luna takes a deep breath in of the air under your soiled desk..."
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
            lun "Of course, [lun_genie_name]..."
            ">Luna reverently opens your robe and softly withdraws your hard cock."
            $ ccg1 = "12"
            lun "What do you..."
            $ ccg1 = "13"
            lun "What now, [lun_genie_name]?"
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
    lun "Hnnk hoo hrr! (Thank you, [lun_genie_name]!)"
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
    lun "Was I doing a bad job, [lun_genie_name]?"
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
    lun "Don't worry, [lun_genie_name], I'll have them out in no time!"
    ">With that, Luna begins her tongue lashing of your cock anew."
    $ ccg1 = "21"
    g4 "A-Ah..."
    g4 "G-good work miss lovegood..."
    $ ccg1 = "27"
    lun "Hnnk hoo hrr! (Thank you, [lun_genie_name]!)"
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
    ">Before you can finish your sentence Luna suddenly thrusts her head forward, forcing your cock down the young girl's throat."
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
    hide screen ccg
    with d3

    ">Once done, she Eventually decides to crawl out from underneath your desk..."

    call lun_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade
    with d3
    pause.5

    call lun_main("Those nasty wrackspurts sure were giving you trouble weren't they [lun_genie_name]?","base","seductive","sad","mid",xpos="right",ypos="base")
    m "yeah... sure..."
    call lun_main("Well if they bother you again just let me know!","base","happyCl","base","mid")
    call lun_main("Getting all of them out was a bit of a struggle...","soft","suspicious","sad","R")
    call lun_main("But I think we did it!","base","happyCl","base","mid")
    m "You sure did..."
    m "Now if you don't mind Miss granger..."
    call lun_main("Lovegood, [lun_genie_name]...","pout","wink","sad","mid")
    m "Right, right... miss love...good..."
    m "This run in with those... things... has left me rather exhausted..."
    call lun_main("Oh...","soft","wide","base","mid")
    call lun_main("Of course, [lun_genie_name]! I best be off to divination class anyway...","base","base","sad","R")
    call lun_main("Just make sure you let me know if you need any help with those wrackspurts again!","base","seductive","sad","mid")
    call lun_main("(I can't believe they taste so good...)","base","seductive","sad","empty")
    m "You'll be the first to know."
    call lun_main("Thanks, [lun_genie_name]! Have a nice day!","base","happyCl","base","mid")

    call lun_walk("desk","leave",2.7)

    $ luna_busy = True

    m "..."

    jump main_room

label luna_reverted_event_4: #Luna gentle BJ for anout 9 hours and 14 orgasms from Genie #NEEDS TESTING
    $ lun_corruption = 4
    $ days_to_luna = 6

    call play_sound("knocking")
    ">*knock* *knock* *knock* *knock* *knock* {b}*knock* *knock*{/b}"

    call play_sound("door")
    call lun_walk("door","mid",2)
    pause.2

    call nar(">Your door swings wide as the ever cheerful Luna Lovegood strolls in.")

    call lun_main("Hello, [lun_genie_name]!","base","happyCl","base","mid",xpos="right",ypos="base")
    m "Miss Lovegood, to what do I owe the {i}pleasure{/i}?"
    call lun_main("Well...","base","wink","sad","mid")
    call lun_main("today is a sunday...","base","seductive","sad","mid")
    m "It is?"
    call lun_main("Of course! Can't you tell how happy the sun is?","base","wide","base","mid")
    m "..."
    call lun_main("anyway... seeing as how it's Mr Sun's happy day...","base","seductive","base","mid")
    call lun_main("and I don't have any classes!","base","seductive","sad","R")
    call lun_main("So I was wondering... what are you up to today [lun_genie_name]?","base","seductive","mad","mid")
    m "Probably just working on some reports for the ministry..."
    m "Why?"
    call lun_main("Well if you wouldn't mind...","base","seductive","sad","mid")
    call lun_main("Maybe I could get a few more of my nasty wrackspurts out for you?","base","wink","angry","mid")
    call lun_main("I just feel so bad knowing that I gave them to you...","pout","wide","sad","mid")
    m "I wouldn't blame yourself-"
    call lun_main("But I do!","open","wide","sad","mid")
    call lun_main("The idea of all those nasty things being trapped in there...","base","seductive","sad","empty",cheeks="blush")
    call lun_main("Causing so much discomfort...","upset","seductive","sad","downL",cheeks="blush")
    call lun_main("It's all I've been able to think about!","base","angry","angry","empty",cheeks="blush")
    m "I suppose if it's bothering you so much I can let you get a few out."
    call lun_main("oh thank you, thank you, thank you!","open","happyCl","base","mid",cheeks="blush")
    call lun_main("You don't know how much better I'll feel once I get them {b}all{/b} out!","base","angry","angry","empty",cheeks="blush")
    m "I don't think yo-"
    show screen blkfade
    with d3
    ">Luna quickly hops over to her favourite place in the room, your cum-soaked desk, and kneels before you."
    hide screen luna_main
    hide screen blkfade
    with d3
    $ ccg_folder = "luna_desk"
    $ ccg("38","blank","blank")
    lun "Hmmmm... you don't know how heavy this has been on my mind sir..."
    $ ccg1 = "37"
    lun "All those nasty wrackspurts churning around in you..."
    $ ccg1 = "38"
    lun "But don't worry sir! I've got a foolproof plan to drag every single one off them out!"
    m "Oh really? And what does this master plan involve?"
    $ ccg1 = "39"
    lun "The first part was the hardest... Gillyweed isn't an easy thing to get..."
    $ ccg1 = "40"
    lun "But being able to breathe without using my throat will be worth it!"
    m "I'm liking the sound of this plan already!"
    m "What's part two?"
    $ ccg1 = "39"
    lun "It's the easiest part! All I need is my wand!"
    m "What's that fo-"
    $ ccg1 = "15"
    show screen white
    lun "PETRIFICUS TOTALUS!"
    ">Your body cements itself in place as you lose complete control from the neck down."
    hide screen white
    $ ccg1 = "39"
    m "What have you done!? I can't move my legs!"
    $ ccg1 = "41"
    lun "Calm down sir, I'm not going to hurt you."
    m "Then why can't I move!?"
    $ ccg1 = "36"
    lun "I was just a little worried that those nasty wrackspurts would try to make us stop before we were finished..."
    m "(Oh no...)"
    m "What do you mean by... finished?"
    $ ccg1 = "37"
    lun "I already told you that I'm going to get {b}ALL{/b} of those tast- nasty wrackspurts out didn't I?"
    $ ccg1 = "39"
    lun "The petrification charm is just so you don't hurt yourself."
    m "Lun-"
    ">Before your able to protest anymore, your jaw locks in place..."
    lun "Shh... that's it... Just imagine that your under the Wiggentree..."
    $ ccg1 = "36"
    lun "We've got the whole day to look forward to..."
    m "(oh... no...)"
    $ ccg1 = "37"
    lun "Well, let's get started shall we?"
    show screen blkfade
    with d3
    pause 0.5

    #3 hours later
    pause 0.5
    $ ccg("blank","blank","blank", "luna_bj_loop_1")
    hide screen blkfade
    with d3
    #have loop here

    m "Please Luna... you have to stop now..."
    g4 "four times is enough..."
    $ ccg("42","blank","blank")
    lun "Those tasty wrackspurts really have a hold on you don't they?"
    ">Luna gives your stressed balls a playful squeeze."
    $ ccg1 = "43"
    lun "Mmmm... I can still feel so much magic in here..."
    $ ccg1 = "44"
    lun "well, back to work!"
    $ ccg("blank","blank","blank", "luna_bj_loop_1")
    ">Luna's head dives forward as she gleefully impales your cock on her soft, magically smooth throat. "
    lun "*glck*glck*glck*"
    ">Once more, the room falls into silence, save for the melodic sound of Luna's constant and unyielding throat-fucking..."
    show screen blkfade
    with d3
    pause 0.5

    #3 hours later
    $ ccg("blank","blank","blank", "luna_bj_loop_2")
    pause 0.5
    hide screen blkfade
    with d3
    lun "*glck*glck*glck*"
    g4 "Please... I'm..."
    lun "*glck*glck*glck*"
    g4 "ARGH!!!"
    lun "*glck*glck*glck*"
    ">Luna doesn't even acknowledge your cries for help, deciding to start humming a merry tune instead..."
    lun "*glck*hm-ha*glck*huu*glck*"
    g4 "NO!!!"
    ">The vibrations from her humming push you over the edge, earning an excited chirp from Luna as you fire another painful load into her stomach."
    g4 "Arghhhhhh..."
    m "Don't you... need to stop..."
    m "for lunch... or something..."
    lun "Slrp-*pop*"
    $ ccg("45","blank","blank")
    lun "After swallowing all these wrackspurts? I don't think I'll need dinner sir, let alone lunch!"
    m "please..."
    $ ccg1 = "46"
    lun "Shhhh, it's okay sir... Just let me get rid of these tasty little wrackspurts and then you can have a nice night sleep..."
    $ ccg1 = "47"
    lun "Goodness knows they haven't been letting me get a good nights sleep..."
    $ ccg1 = "48"
    lun "I've been plotting out my revenge on them all week..."
    lun "Now..."
    $ ccg("blank","blank","blank", "luna_bj_loop_2")
    lun "*glck*glck*glck*"
    ">Luna renews her attack on your cock, lashing her tongue along the underside as she slams the tip down her throat..."
    m "ARGHHH-"
    show screen blkfade
    with d3
    pause 0.5

    #one eternity later
    pause 0.5
    hide screen blkfade
    with d3
    g4 "Please... i can't... not any more... i'll die..."
    lun "*glck*glck*glck*"
    g4 "PLEASE"
    lun "*glck*glck*glck*"
    g4 "ARGHH!!! FUCKING UGH ARGHHHHHH!!!"
    $ ccg("53","blank","blank")
    lun "*glck*glck*glck*"
    g4 "!!!!!!!"
    lun "*glck*glck*glck*"
    $ ccg1 = "45"
    lun "Slrp-*pop*"
    ">Luna Finally pulls away from your cock..."
    lun "I think that's probably enough..."
    $ ccg1 = "47"
    lun "Even if I do think there were still a few too many wrackspurts in that last load..."
    $ ccg1 = "45"
    lun "Don't worry though, we can get them later!"
    m "No... not again... I can't..."
    $ ccg1 = "49"
    lun "Of course you can! How else are we going to rid the school of them?"
    m "I... suppose so..."
    m "But... at least give me a few days to recover..."
    $ ccg1 = "50"
    lun "A few days?!"
    m "At least..."
    $ ccg1 = "51"
    lun "Alright..."
    lun "I might not have been so thorough today if I knew you'd take so long to recover!"
    m "Well, at least you've learned a valuable lesson."
    $ ccg1 = "45"
    lun "I suppose i did! I think five hours probably the limit from now on."
    m "Five!- just hurry up and get yourself cleaned up, I'm about to pass out..."
    $ ccg1 = "52"
    lun "Clean up? Why?"
    show screen blkfade 
    with d3
    show screen luna_main
    hide screen ccg
    $ luna_cum = 11
    $ genie_base = "characters/genie/base/base.png"
    $ luna_wear_cum = True
    hide screen blkfade
    with d3
    m "You don't intend to walk to your dorm like that do you?"
    call lun_main("Of course! I intend to wear these wrackspurt corpses with pride!","base","happyCl","base","mid",cheeks="blush")
    call lun_main("it should serve as a warning to the other wrackspurts around the school!","base","angry","angry","mid",cheeks="blush")
    m "Don't let me stop you then."
    call lun_main("plus, I think I'll be able to make a lovely perfume out of it...","base","wink","sad","mid",cheeks="blush")
    m "..."
    ">Luna takes in a deep breath."
    call lun_main("agh.... it reminds me of my old Wiggentree... and my new friend!","base","happyCl","sad","mid",cheeks="blush")
    ">With that, Luna skips merrily out of your office, drenched head to toe in a thick layer of cum..."
    call lun_walk("desk","leave",2.7)
    $ luna_busy = True
    $ luna_wear_cum = False
    m "..."
    m "I still can't move..."
    m "eh..."
    m "Zzzz..."
    jump main_room

label luna_reverted_event_5: #Luna regular BJ for about 5 hours with Luna masturbating the whole time #NEEDS POSING
    ">*knock* *knock* *knock* *knock* *knock* {b}*knock* *knock*{/b}"
    ">Your door swings wide as the effervescent Luna Lovegood strolls in."
    $ luna_chibi("stand")
    call lun_main("Hello [lun_genie_name]!", "base", "happyCl", "sad", "default")
    m "..."
    m "You're not going to paralyse me again are you?"
    call lun_main("Oh... not if you don't want me too...", "pout", "default", "sad", "R")
    m "I do not."
    call lun_main("Sorry... I thought you'd like it... Is there anything I can do to make it up to you?", "upset", "seductive", "sad", "down")
    m "Hoping under the desk would be a good start."
    call lun_main("Really? I was worried you'd be mad at me!", "base", "wide", "default", "default")
    m "Well so long as you do a good job making it up to me..."
    call lun_main("Don't worry sir, I'll do my best!", "base", "happyCl", "default", "default")
    m "About that..."
    show screen blkfade
    with d3

    menu:
        "Facefuck her to teach her a lesson!":
            jump luna_reverted_facefuck
        "Let her do her own thing...":
            pass

    ">You quickly take out your hard cock and slap it against Luna's naive nose a few times."
    $ ccg_folder = "luna_desk"
    $ ccg("36","blank","blank")
    show screen ccg
    hide screen blkfade
    with d3

    m "I expect you to make it up to my cock miss lovegood."
    $ ccg1 = "38"
    lun "Oh no, is he upset with me?"
    m "very... I think he'll need a lot of attention before he's feeling any better."
    $ ccg1 = "39"
    lun "Mmmm, what sort of attention?"
    $ ccg1 = "54"
    ">You place the tip of your cock against the air-headed girl's lips."
    m "Shhhh..."
    $ ccg1 = "55"
    ">You slowly start rubbing the tip over her soft lips, a drop of precum smearing across them like lip-gloss."
    m "Why don't you start with a nice kiss..."
    lun "..."
    $ ccg1 = "56"
    ">Luna doesn't even acknowledge you with a response, instead preferring to lose herself in the act of making out with your cock..."
    m "Ughhh, that's it..."
    $ ccg1 = "57"
    ">Luna's eyes drift up as she slowly envelops the tip of your cock, her tongue rushing to find the tip and start lashing it..."
    m "Mmmm... That's a good start... He might forgive you after all..."
    $ ccg1 = "58"
    lun "Hyyy!"
    $ ccg1 = "56"
    ">In her moment of joy, luna takes your cock from her mouth before unleashing a flurry of kisses on the tip..."
    $ ccg1 = "38"
    lun "thank you, thank you, thank you!"
    m "If you really want him to forgive you, maybe put him back in your mouth..."
    lun "OK!"
    $ ccg1 = "58"
    ">Luna thrusts her head forward, swallowing half your cock before running her tongue along the underside."
    m "mmmm"
    $ ccg1 = "59"
    m "Ughhh... that's it... keep going... just like that..."
    lun "hhhkkyyy..."
    $ ccg("blank","blank","blank", "luna_bj_loop_3")
    #bunch of pauses to allow for motion
    ">You feel your load slowly start to build as Luna lovingly works your shaft."

    menu:
        "Blow it on her face":
            g9 "Alright slut, here it comes!"
            pass
        "Shoot it down her throat":
            g9 "Ugh... You are just to good at this..."
            g9 "I don't think I can help myself..."
            ">With that you put your hand on the back of Luna's head, grabbing a handful of her blonde locks before pulling her forward, impaling your cock into her neck."
            lun "!!!"
            g9 "Ughh that's the fucking spot!"
            lun "..."
            g9 "This is what you deserve after what you did last time!"
            lun "..."
            g9 "Not that you'll mind, you nasty little freak..."
            g9 "I bet you're loving this aren't you..."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            g9 "Little cumslut that you are..."
            g9 "well, here's your reward!"
            ">With that, you unleash a colossal load down her throat!"
            lun "!!!"
            g9 "Ughh... my balls have been aching ever since you drained them you little semen demon!"
            g9 "This should be a good chance to empty them..."
            ">Your tighten your grip on her hair, pulling her head back until just the tip of your cock rests in her mouth."
            g9 "Mmmm, this way you should get to taste it too..."
            ">Almost instantly you fill Luna's cheeks to the brim..."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            g9 "This isn't too much is it?"
            ">You pull her head forward viciously forcing all the cum pooled in her mouth to come flying out the poor girls nose..."
            g9 "Mmmm, I love it when this happens..."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            g9 "The best part of this is..."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            m "I know that I know this is all you'll be smelling for the next week..."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            m "It'll find it's way into every nook and cranny of your nose..."
            m "And be all you'll be able to think about..."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            m "Is how much of a dirty little cumslut you really are!"
            lun "{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
            ">With that, you feel Luna's body start to violently shudder as her hips spasm, her thighs dripping onto the floor..."
            g9 "Alright slut, here it comes again{b}{/b}!"

    menu:
        "\"Shutup and take this!!!\"(Coat her)":
            ">You begin firing off one of the largest loads of your life, taking care to make sure every square inch of the girls receives a thick coating of spunk."
            g9 "Ugh... this is what you deserve after the other day."
            lun "Why?"
            g9 "You know why!"
            g9 "If you act like a filthy cumslut then you should expect to be treated like one..."
            lun "..."
            ">Your orgasm comes to a close..."
            g9 "Mmmm... I think i might have treated you more like a cumrag if I'm being honest..."
        "\"Do an ahegao face!\"":
            lun "A what face?"
            g9 "Just stick your tongue out and look up like your doing a silly face!"
            lun "?"
            lun "Ah..."
            g9 "Oh that's it, here it comes you hungry little cumslut!"
            lun "{image=textheart}{image=textheart}{image=textheart}"
            ">With that you begin to fire off a huge load, coating the poor girl in a thick layer of cum..."
            g9 "ugh yes... take this slut..."
            lun "Ah..."
        "\"Cry!\"":
            lun "Why?"
            g9 "Do you want to get covered in cum or not?"
            lun "You mean if I don't cry..."
            lun "You won't cover me in wrackspurts?"
            g9 "Well-"
            lun "*sob* That's so mean sir! *sob*"
            lun "*sob* You'd make me go to class without...*sob*you'd have so many left in you!*sob*"
            g9 "Ugh that's it slut! Here it comes!"
            lun "*sob*O-o-oK*sob*"
            ">With that you begin to fire off a huge load, coating the poor girl in a thick layer of cum..."
            lun "*sob*{image=textheart}*sob*{image=textheart}*sob*{image=textheart}*sob*"
            g9 "ugh yes... take this slut..."
            lun "*sob*mmmm...*sob*"
            g9 "OH fuck... That shouldn't feel so good..."
            lun "why not?"
            m "Shhh..."
            ">You place the tip of your cock against her lips to silence the cum soaked girl..."
    lun "wow..."
    lun "You're..."
    lun "You're just the best..."
    ">Luna leans forward, placing a kiss on the end of your cock before whispering something quietly to it..."
    lun "{size=-5}Thank you...{/size}"
    lun "Now, I think I better be going sir..."
    lun "Unless you had anymore wrackspurts that you needed me to take care of?"
    m "For goodness sake girl!"
    lun "..."
    m "You can go now..."
    lun "Yes sir..."
    ">Luna picks herself up from under your desk and goes to leave."
    m "Aren't you forgetting something?"
    lun "Probably! I'm not the best when it comes to that."
    m "Don't you think you should clean yourself off a little before you head back to your room?"
    lun "Oh don't worry sir, I'm not going to my room, I'm going to the potions lab."
    lun "Oh, I {b}did{/b} forget something!"
    m "What's that?"
    lun "What's a slut sir?"
    m "A slut?"
    lun "Mhmm, you called me one when I was getting rid of the wrackspurts!"
    m "Oh, ugh... It's someone who loves... doing what we're doing..."
    lun "Really? So does that mean a cumslut is someone who loves cum?"
    m "Mhmm."
    lun "Then I must be the worlds biggest cumslut!"
    m "..."
    lun "Well, toodaloo sir!"
    ">With that, Luna hops out of your office, even more of a spring in her step than when she entered."
    m "..."
    m "(Am I playing around with a disabled chick?)"
    m "Eh, who cares..."
    jump main_room #NEEDS POSING

label luna_reverted_event_5_1: #Luna facefuck transitional part #NEEDS POSING
    ">You put your hand on the back of the unsuspecting girls head..."
    m "I was thinking we could have another lesson today..."
    lun "Really? What sort?"
    m "Well, today I'll be teaching you what happens when you decide to paralyse your headmaster and suck their cock for hours on end..."
    lun "Oh... and what's that?"
    m "This happens miss lovegood, this happens..."
    ">With no more warning, you grab a handful of the blonde's locks and pull her head forward into your stomach, forcing your cock down Luna's neck."
    m "You see, I wasn't the biggest fan having you come in..."
    ">You begin pumping luna's head backwards and forwards, impaling the back of her throat each time."
    lun "*glck**glck**glck*"
    m "paralyse me..."
    lun "*glck**glck**glck*"
    m "AND THEN PROCEED TO SUCK ME OFF FOR AN ENTIRE DAY!"
    lun "*glck*{image=textheart}*glck*{image=textheart}*glck*{image=textheart}"
    m "And if you want cum so much, just beg like a normal cumslut!"
    lun "*glck*{image=textheart}*glck*{image=textheart}*glck*{image=textheart}"
    m "Speaking of, ready for your first load slut?"
    lun "*glck*{image=textheart}*glck*mmmhhmmmm*glck*{image=textheart}"
    m "Good girl! Here it comes!!!"
    ">You start shooting the first of many loads down Luna's throat."
    m "Ughhh... here you are slut... here's your favourite meal!"
    lun "*glck*{image=textheart}*glck*{image=textheart}mmmmm{image=textheart}*glck*{image=textheart}*glck*"
    ">After the first three shots, you feel your orgasm start to subside..."
    m "Ughh... I don't think that's going to be enough of a load to satisfy a nasty little cumslut like you now is it?"
    lun "*glck*{image=textheart}*glck*{image=textheart}*glck*{image=textheart}"
    ">You muster what little genie magic you can and focus it on your empty balls..."
    lun "*glck*{image=textheart}*glck*!!!*Gulp*{image=textheart}*glck*{image=textheart}"
    ">Allowing your withering cock to come back to life, firing a inhumane volley of cum into the girls stomach."
    m "That's better! This is what a cumslut like you deserves!"
    ">Luna's hands have both managed to sneak under her skirt and are now a blur of movement..."
    lun "*Gulp*{image=textheart}*glck*{image=textheart}*Gulp*{image=textheart}*glck*{image=textheart}"
    m "Ughhh... If you'd just asked..."
    lun "*Gulp*{image=textheart}*glck*{image=textheart}*Gulp*{image=textheart}*glck*{image=textheart}"
    m "Instead I have to teach you a lesson."
    ">You pull luna's limp head off your cock as it continues to fire off round after round..."
    lun "*GASP* *cough* *cough* *cough*"
    m "Mmmmm that's it just let me cover you..."
    lun "..."
    m "Anything to say for yourself cumslut?"
    lun "..."
    lun "{size=-5}T-Thank you...{/size}"
    m "What was that? I don't think I could hear you through all that cum..."
    lun "Thank you sir..."
    m "(what?)"
    lun "You're the only person who has taken me seriously with the wrackspurts..."
    lun "And you've been so nice..."
    lun "And taught me so many things..."
    lun "And this cum..."
    lun "It's so good! It's like it's made of pure magic!"
    lun "Thank you, thank you, thank you!"
    lun "You're the best genie ever!"
    ">With that, luna willing impales her head on your cock, shamelessly slobbering over every inch of it..."
    m "ugh... I'm glad you've learned your lesson."
    m "I am the best genie ever..."
    play sound "scratch.mp3"
    m "DID YOU JUST SAY GENIE?"
    lun "*Slrp*POP*!"
    lun "Mhmmm. I mean you are a genie aren't you?"
    m "Well, yes..."
    m "But how do you know that? I thought I looked like dumbydoo or whoever..."
    lun "ONly when I'm not wearing my spectrespecs!"
    m "Those glasses?... So you've known the whole time?"
    lun "Well, I didn't know you were a genie until I tasted this..."
    ">She gives the end of your dick a quick lick."
    lun "I don't think any other creature could make something so tasty..."
    lun "Not even a unicorn..."
    m "So you don't care I'm a genie?"
    lun "Nope! Not unless it bothers you..."
    m "As long as you keep sucking cock like that, you can think I'm the prince of persia..."
    m "Just don't expect any wishes."
    lun "Hmph... Why not?"
    m "You have to rub my lamp to get wishes and I'm pretty sure that thing is all the way back in Agrabah."
    lun "Awww... rubbing this doesn't count?"
    ">Luna gives your cock a playful few strokes."
    m "Afraid not."
    lun "Oh well... I guess that your yummy cummy will just have to do."
    lun "Speaking of..."
    ">Luna goes to throw her head onto your cock again..."
    m "Steady on there girl... Don't you think you've had enough cum for one day?"
    lun "What? Already? But there's still so much magic..."
    lun "{image=textheart}{image=textheart}{image=textheart}"
    lun "Can't we keep going? There must be so many wrackspurts left in you..."
    m "(Oh right... those things...)"
    m "Quite right... it seems that you're bringing in more wookiesports than I can deal with..."
    m "I'll have to teach you an advanced method for getting rid of them in both of us at once."
    lun "Really? You have something like that?"
    lun "That could solve the school's wrackspurt infestation in no time!"
    lun "could you teach it to me now? Pleeeease..."
    m "Ugh... I think I need a bit of a nap after that... not to mention you could use a shower..."
    lun "And waste this? I told you that I'm using it to make a perfume to ward off those wrackspurts."
    lun "I'm even thinking of selling it to the other students to help slow down those nasty things..."
    m "Whatever... just do it somewhere else... I need a nap..."
    lun "OK Mr Genie, sir!"
    m "Genie is fine."
    lun "Have a nice nap, Genie!"
    ">With that a cum-soaked Luna prances out of your office and into the wide world..."
    m "..."
    $ lun_genie_name = "genie"

    jump main_room

label luna_reverted_event_6: #Repeatable Luna BJ for whole day #NEEDS POSING
    #Invite Luna to your office, ask what she's doing
    #Offer to give her a note to excuse her from class
    #Have her hop under the desk
    #Get the idea to have someone come up and visit while this is happening
    #Summon up hermione for some entertainment
    #menu options between show tits/pussy
    #hermione catches on when you cum in front of her with your hands above the desk
    #demands extra points for playing your sick game
    #gets into it
    #hermione starts to tease whoever's under the desk (calling a cumslut)
    #only serves to turn luna on more and make her believe the room is infected with wrackspurts
    ">The bubbly Luna Lovegood strolls in through your door."
    lun "Good morning, [lun_genie_name]!"
    m "Miss Lovegood."
    lun "Is there {i}anything{/i} I can help you with today?"
    m "well... Now that you mention it... What's your class schedule like for today?"
    lun "Hmmmm... not too busy. I have divination at eleven and... um... herbology at two!"
    m "I think I might need to write you a note explaining your absence from class then."
    lun "really? Why's that?"
    m "Those nasty wickerspoons are bothering me again, quite badly I'm afraid."
    lun "They are?!"
    m "Indeed. I'm thinking you'll need to spend the whole day seeing to them."
    lun "the {b}whole{/b} day?..."
    m "Unless, of course, you'd prefer to go to your classes?"
    lun "No, no, no! I'll help you!"
    m "Fantastic... Shall we begin then?"
    lun "{b}yes{/b}... thank you [lun_genie_name]..."
    show screen blkfade
    with d3
    pause
    hide screen blkfade
    with d3
    #No CG, just Genie at his desk...
    g4 "{size=+5}You greedy little slut! Take this!{/size}"
    lun "*gulp* *gulp* *gulp*"
    ">You fire your third load of the day into Luna's hungry mouth."
    lun "*gulp*{image=textheart}*gulp*{image=textheart}*gulp*"
    m "Fuck that's good... Ugh..."
    ">Sensing that your orgasm has ended, Luna begins to slow down and focus suckling the end of your cock to nurse it back to health..."
    lun "*glck*{image=textheart}*slrp*{image=textheart}*glck*"
    m "Ugh... I should... mmmm... do some work... or something..."
    lun "*glck*{image=textheart}*slrp*{image=textheart}*glck*"
    menu: 
        "-Try and do some paperwork-":
            ">Intent on not losing the entire day to Luna's mouth you begin to write out a report for the ministry."
            m "Yes... school activities..."
            lun "*glck*{image=textheart}*slrp*{image=textheart}*glck*"
            m "..."
            show screen blkfade
            with d3
            pause 
            hide screen blkfade
            with d3
            m "There, all done!"
            lun "*glck*{image=textheart}*slrp*{image=textheart}*glck*"
            m "(It only took three hours and twice as many orgasms)"
            lun "*glck* *slrp* *glck*"
            m "Just a quick read through before I send this off to the ministry..."
            m "..."
            lun "*glck* *slrp* *glck*"
            m "......"
            lun "*Slrp* *pop*"
            lun "How's the report, [lun_genie_name]?"
            m "Unless you consider a three page report about how you suck cock useful..."
            m "Then it's garbage..."
            lun "Wait... You wrote a report on how I..."
            lun "Can I have it? Please, [lun_genie_name]!"
            m "Sure, it's not like I can send it to the ministry anyway."
            lun "Oh thank you, thank you, thank you! I can't wait to read it tonight."
            m "Until then..."
            lun "Oh, right!"
            lun "*glck*{image=textheart}*slrp*{image=textheart}*glck*"
            m "Ugh... that's it slut..."
        "-Summon someone-":
            pass
    m "(Maybe I should bring someone up here while this is going on...)"
    menu :
        "-Hermione-":
            pass

    #First time Hermione is brought up
    m "(That slut will probably get off on it.)"
    ">Without further ado, you summon Hermione up to your office to take your mind off of Luna's endless cocksucking."
    her "You wanted to see me [genie_name]?"
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    m "Mmmmm... That I did..."
    her "Ugh... This room reeks of cum! Open a window or something..."
    m "The window doesn't shut."
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    her "Then maybe try cumming a bit less..."
    m "If I do that I'm not sure you'll' be able to win the house cup..."
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    m "Speaking of..."
    her "oh..."
    her "What will it be today then [genie_name]?"
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    her "Do you want me to suck your cock?"
    her "Or maybe you want to bend me over your desk again{image=textheart}{image=textheart}{image=textheart}..."
    m "I love your enthusiasm but lets just start with a nice look at your tits..."
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    her "Oh... alright then..."
    #Hermione shows her tits
    m "Ugh... that's it slut..."
    lun "{size=-5}*glck* *slrp* *glck*{/size}"
    her "..."
    m "Mmmm... Make them jiggle!"
    ">You start bucking your hips to facefuck Luna while Hermione unknowingly encourages you on..."
    lun "*glck* *slrp* *glck*"
    m "Oh fuck yes... just like that..."
    her "Is something going-"
    m "Shut-up and get naked [hermione_name]!"
    lun "*glck* *slrp* *glck*"
    her "..."
    ">Hermione stares at your desk while stripping down to nothing."
    her "So... who's hiding under the desk?"
    lun "*glck* *slrp* *glck*"
    m "Ugh... what do you mean?"
    her "Please, I can hear them sucking you off from here."
    lun "*glck* *slrp* *glck*"
    her "I'm just curious who you managed to get..."
    lun "*glck* *slrp* *glck*"
    her "Anyone I know?"
    m "I believe... argh... you've met..."
    her "Hmmmm... It's not a slytherin is it?"
    m "What colour are they again?"
    her "The green ones you decrepit old perv!"
    lun "*glck* *slrp* *glck*"
    m "Mmmm... she's not a slytherin then..."
    her "Hmmm... She certainly doesn't have any shame by the sounds of it, so she's not a hufflepuff..."
    lun "*glck* *slrp* *glck*"
    her "It has to be a Gryffindor! They're the only ones brave enough to try this..."
    lun "*glck* *slrp* *glck*"
    her "Ginny, is that you?! I told you to stay away from Dumbledore!"
    m "Wrong, they're in the blue house."
    her "A ravenclaw? But which ravenclaw girl would be stupid enough to-"
    her "..."
    lun "*glck* *slrp* *glck*"
    her "It's Luna again isn't it?"
    m "..."
    her "That hat better not have been involved!"
    m "Scout's honor."
    her "We'll see about that..."
    ">Before you can say anything Hermione walks around your desk to check on Luna."
    lun "*slrp* *pop*"
    lun "Hi Hermione! Nice work guessing that it was me!"
    her "..."
    her "What are you doing Luna?"
    lun "Getting rid of wrackspurts! There's so many!"
    her "..."
    her "God your stupid... well, At least I know why the room stinks of cum now..."
    lun "Isn't it great? I'm thinking about using it to make a perfume!"
    her "(Idiot)"
    her "At least I know this is the real you..."
    lun "You do? Thanks for checking, sometimes I'm not so sure myself!"
    her "..."
    lun "Now if it's OK Hermione, I think I better get back to work, I've only gotten six rounds out so far."
    ">Without any hesitation, Luna shamelessly returns to sucking your cock in front of Hermione."
    lun "*glck* *slrp* *glck*"
    her "Six times already? How long does she stay under there?"
    m "She'd live under there if she could..."
    lun "*glck* *slrp* *glck*"
    her "So what? You called me up here to give you a little show while Luna Lovegood sucks you off all day?"
    m "Pretty much... It was getting a little boring with just the two of us..."
    her "Ugh... You're such a pig!"
    m "So you don't want to earn some points for your house?"
    her "I didn't say no... I just wanted to make sure you know how perverted this is!"
    lun "*glck* *slrp* *glck*"
    her "You hadn't even locked your door!"
    #Hermione starts touching herself
    her "What if someone else walked in while this was going on?"
    lun "*glck* *slrp* *glck*"
    her "Do you think they wouldn't be able to heart it?"
    her "To {b}smell{/b} it?"
    lun "*glck* *slrp* *glck*"
    her "But maybe that's what you two want..."
    her "Maybe you were waiting for someone else to walk in and catch you..."
    lun "*glck* *slrp* *glck*"
    her "Is that what you wanted [genie_name]? Some cute little thing to walk in and unknowingly be forced into watching you cum in front of them..."
    her "To be forced into breathing in this thick musk..."
    lun "*glck* *slrp* *glck*"
    her "Imagine if it was a first year? What would you do then?"
    her "Would you do the right thing and send them away?"
    lun "*glck* *slrp* *glck*"
    her "Or would you make them stay..." 
    g4 "Mmmm...."
    lun "*glck* *slrp* *glck*"
    her "Make them watch while you bust your seventh load of the day down Luna's throat!"
    g4 "ARGHH, this is it you sluts!"
    ">With that you fire another gargantuan load into Luna's mouth."
    lun "*glp* *glp* *glp*"
    g4 "Mmmm...."
    lun "*glp* *glp* *glp*"
    her "I guess that answers that..."
    her "I think I better be going then."
    m "Ugh... yes... good... bye..."
    lun "*glck* *slrp* *glck*"
    her "Have a nice day you two!"
    ">With that your vision starts to fade to black as Luna suckles your wilting cock back to health..."
    show screen blkfade 
    with d3
    ">By the time you wake up Luna is gone and the sun has set."
    ">All that's left is a puddle of cum under the desk and an aching in your balls..."
    hide screen blkfade 
    with d3

    jump main_room

    #repeatable Hermione summon event 
    #Hermione immediately comments about Luna being under the desk due to the smell
    #Talks about how perverted this is 
    #Starts calling Luna names as she strips and starts to play with herself
    #Genie asks her why she's stripping and also criticising Luna
    #Asks what she's expected to do when the room reeks like cum so badly
    #Hermione says it's too much
    #insists on spending the rest of the day watching Luna under your desk
    #FTB as both Luna and Hermione spend the rest of the day under your desk

label luna_reverted_event_7: #Luna sex with Genie #NEEDS TESTING
    #Luna is desperate to learn Genie's new techniques
    #Have genie explain some bullshit about how the technique will work
    #explain she'll have to get naked
    #have Luna get more and more excited by the idea of what is going to happen
    #start sex
    #Luna starts babbling about how good it's feeling
    #starts crying over the idea of losing the wrackspurts and not being able to do this anymore
    #Have genie explain that she's just a needy little slut and that her lust isn't going to go away
    #Luna extatic at the idea of being able to continuosly being able to fuck/suck genie
    #Cries as she begs for Genie to dump his load in her
    #ahegao face
    #asks genie to come to her room to cuddle
    m "Ready to learn a new technique?"
    call lun_main("Truly?! Oh, I've been waiting for this since you first mentioned it!","base","base","sad","mid")
    call lun_main("A way for both of us to get rid of our wrackspurts at once!","base","base","sad","mid")
    call lun_main("When do you think you'll approach the rest of the wizarding world with this knowledge?","base","base","sad","mid")
    call lun_main("Everyone deserves to hear about it, we can finally get rid of this scourge once and for all!","base","base","sad","mid")
    m "It's not quite ready for the masses just yet..."
    m "I was hoping you'd be able to help me iron out a few kinks to perfect it..."
    call lun_main("Kinks? What sort of kinks?","base","base","sad","mid")
    m "Well, doing it in public has always done it for me... why don't we go for a walk?"
    call lun_main("okay! Want me to give you a tour of the school while we're at it, [lun_genie_name]?","base","base","sad","mid")
    m "Why not..."
    show screen blkfade
    with d3
    ">Together you and Luna gently meander around the grounds, all the while Luna happily explains the history of it all..."
    call lun_main("And this is the school library...","base","base","sad","mid")
    m "This place is huge! We could definitely find somewhere to do it in here!"
    call lun_main("I wouldn't recommend it... If we accidentally get cum on any of the books they'll probably attack us...","base","base","sad","mid")
    m "(Is she being serious?)"
    m "Well, where do you suggest?"
    call lun_main("hmmm, we need somewhere we don't have to worry about being found...","base","base","sad","mid")
    call lun_main("And also somewhere the wrackspurts we expel won't bother anyone...","base","base","sad","mid")
    call lun_main("...","base","base","sad","mid")
    call lun_main("I know, let's go to the lake! Wrackspurts hate cold water!","base","base","sad","mid")
    m "They do?"
    call lun_main("Of course! Just think about how much a cold shower gets rid of them.","base","base","sad","mid")
    m "You're a clever one."
    call lun_main("Thank you, [lun_genie_name]!","base","base","sad","mid")
    ">With that, Luna grabs your hand and leads you down to the lakeside, out into the open moonlight."
    $ ccg_folder = "luna_fucking"
    $ ccg("lake_1","blank","blank")
    hide screen blkfade
    with d3
    call lun_main("Is this alright, [lun_genie_name]?","base","base","sad","mid")
    m "This seems like as good a place as any."
    call lun_main("So can you finally teach me?","base","base","sad","mid")
    m "Oh, alright then... Seeing as how you asked so nicely..."
    call lun_main("Oh thank you, thank you, thank you!","base","base","sad","mid")
    call lun_main("So how does it work?","base","base","sad","mid")
    m "You'll need to take your top off."
    call lun_main("Okay!","base","base","sad","mid")
    ">Without even the slightest bit of hesitation, Luna rips off her top and throws it to the ground."
    call lun_main("What's next?","base","base","sad","mid")
    m "Bend over."
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","base","sad","mid")
    show screen blkfade
    with d3
    hide screen luna_main
    ">Without saying anything, Luna goes to bend over, desperate to give herself to you..."
    m "Now pull down your skirt..."
    lun "{image=textheart}!!!{image=textheart}"
    ">Luna enthusiastically yanks down her skirt and pants, revealing her sopping pussy."
    lun "Please, [lun_genie_name]..."
    menu:
        "-Tease her-":
            ">You step forward and gently start rubbing the head of your cock against her wet entrance."
            lun "a-ah..."
            ">Luna desperately starts thrusting towards you, begging for penetration."
            lun "Please, [lun_genie_name], I need it..."
            m "Need what?"
            lun "Your cock... please, I need it... The wrackspurts..."
            ">Luna's hips continue to buck in the air almost pathetically..."
            lun "I-I-I-"
            pass
        "-Slam it in!-":
            pass

    $ ccg("lake_2","1","blank")
    hide screen blkfade
    with d3
    ">Tired of talking, you decide to end the poor girl's suffering by slamming into her needy little fuckhole."
    lun "{size=+10}{image=textheart}!!!{image=textheart}{/size}"
    m "That's it you little slut!"
    $ ccg2 = 2
    lun "{size=-5}{image=textheart}wow...{image=textheart}{/size}"
    $ ccg2 = 3
    ">Before you're able to even start a steady pace of fucking the girl her hips start violently slamming to you..."
    m "Ugh... steady on there, [luna_name], we've only just started!"
    $ ccg2 = 4
    lun "{image=textheart}a-ah... i can't... [lun_genie_name]... it's just... too... {image=textheart}{b}goood{/b}...{image=textheart}"
    $ ccg2 = 5
    ">All you can do is stand there as Luna fucks herself senseless on your cock..."
    lun "{image=textheart}ah...{image=textheart}the wrackspurts...{image=textheart} they're going...{image=textheart}aaaahhh..."
    $ ccg2 = 4
    lun "I'm almost... sad to lose... them...{image=textheart}{image=textheart}"
    $ ccg("lake_2","2","fade")
    lun "They feel {image=textheart}{b}amazing{/b}...{image=textheart}"
    m "About that..."
    $ ccg2 = 6
    lun "W-what?"
    m "This isn't wickspots or whatever you call them..."
    $ ccg2 = 4
    lun "It isn't?... then... ah...{image=textheart} what's this feeling..."
    m "This is sex..."
    $ ccg2 = 7
    ">Luna's hips slam into your stomach and hold there."
    lun "Oh..."
    m "..."
    lun "Hmmm..."
    $ ccg2 = 8
    lun "So sex forces us to eject the wrackspurts... but the feeling good is normal?"
    m "..."
    m "You got it."
    $ ccg2 = 5
    ">Luna's hips resume their assault, desperate to make up for the lost time."
    $ ccg2 = 6
    lun "So we're... using {b}sex{/b}... to eject them..."
    m "..."
    $ ccg2 = 9
    lun "That... would explain... the red tint... to their aura..."
    m "(Does this bitch ever shut up?)"
    ">Weary of her analysis you begin to take matters into your own hands."
    $ ccg2 = 5
    ">Grabbing a hold of her hips, you start to fuck the witch in earnest."
    g4 "take this, slut!"
    $ ccg2 = 1
    lun "{size=+10}{image=textheart}!!!{image=textheart}{/size}"
    $ ccg2 = 10
    lun "a-ahhhhh..."
    ">You keep pounding her from behind. Luna's lovely breasts jiggle a little with every thrust."
    ">You turn your attention to her butt... It's so milky and... pert... she's such a needy little girl...."
    $ ccg2 = 11
    $ renpy.play('sounds/slap.mp3')
    lun "ah...{image=textheart}{image=textheart}{image=textheart}"
    ">You give her buttocks another loud slap."
    $ ccg2 = 12
    $ renpy.play('sounds/slap.mp3')
    lun "Thank you, [lun_genie_name]."
    ">You pick up the pace and feel you're getting close..."
    $ ccg2 = 13
    lun "Yes! Yes! Thank you! Thank you! I'm almost... almost...{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 14
    ">You feel Luna's tight cunt start to spasm and grip down hard on your cock..." 
    m "Argh! You dirty little slut! Who said you could cum yet!"
    $ ccg2 = 15
    lun "I had too, [lun_genie_name]."
    ">Her hips refuse to slow as she speaks..."
    $ ccg2 = 13
    lun "I {b}need{/b} it..."
    $ ccg2 = 16
    ">You let out a roar and start cumming uncontrollably right into her pussy..."
    lun "ahh!{image=textheart} Yes!{image=textheart} ah...{image=textheart} it's so {b}hot{/b}...{image=textheart}"
    $ ccg2 = 17
    lun "Your cum is {b}filling{/b} me up..."
    $ ccg2 = 18
    lun "{size=-3}It's...{/size}{w} {size=-7}i...{/size}{w} {size=-9}I'm cumming...{image=textheart}{image=textheart}again...{image=textheart}{/size}"
    ">You keep firing cum deep inside her pussy until the last drop..."
    $ ccg2 = 19
    ">You can see that Luna is still trying to thrust into you, but her legs refuse to listen to her with multiple orgasms taking over her body..."
    show screen blkfade
    with d3
    ">Luna tries to keep going but collapses on the ground with a thump after you pull out of her..." 
    m "Ugh... I suppose I better carry her back, she'll freeze out here otherwise."
    menu:
        "-Carry her back to her room-":
            ">You softly pick the statuesque young girl up off the cold grass, cradling her in your arms as you take her to her dorm."
            lun "..."
            lun "{size=-5}you really are a genie, aren't you?{/size}"
            pass
        "-Wipe your cock on her first-":
            m "(Should I?)"
            m "(Eh, why not?)"
            ">With that, you take your softening cock and start smearing the end of it across her nose and face."
            lun "..."
            lun "{size=-5}thank you...{/size}"
            ">You softly pick the cum coated young girl up off the cold grass, cradling her in your arms as you take her to her dorm."
            pass
    ">You return to your office."

    jump main_room  

label luna_reverted_event_8: #Luna sex repeatable (in the office)#NEEDS POSING
    #Luna already in the office
    #Ask her if she's ready for a bit of sex
    #Say she was hoping he'd ask about this again
    #ask if he wants to go down to the lake again
    #Says can't be bothered, offers to have sex here
    #Adamant that no one will bother them
    #Moments after they start there's a knock on the door
    #Option to choose who it is
    m "How are you feeling today, [luna_name]?"
    lun "Happier now that I'm in here!"
    m "Fantastic... Now, would you be interested in expelling a few more wookspoons together?"
    lun "You mean..."
    lun "Oh, thank you, thank you, thank you, [lun_genie_name]!"
    show screen blkfade
    with d3
    hide screen luna_main
    ">Before you can say anymore, Luna throws her clothes to the floor and starts desperately thrusting her ass towards you."
    m "Gods, you're a needy little whore, aren't you?"
    lun "yes..."
    m "Mmmm"
    ">Unable to wait any longer, you drive yourself into her tight hole."
    $ ccg_folder = "luna_fucking_2"
    $ ccg("1","blank","blank")
    hide screen blkfade
    with d3
    lun "!!!"
    menu:
        "Astoria":
            jump luna_reverted_event_8_ast_1
        "Tonks":
            jump luna_reverted_event_8_ton_1
        "Hermione":
            jump luna_reverted_event_8_her_1

label luna_reverted_event_8_ast_1: #Astoria part 1#NEEDS POSING
    call ast_main("Ready to practice ano-","smile","happyCl","base","mid",xpos=600)
    m "!!!"
    lun "!!!"
    ast "Dumby! What are you doing?"
    lun "Oh... hello, Astoria..."
    ast "I wasn't speaking to you, Lovegood! I thought we were only going to practice Imperio when we were together Dumby!"
    ast "It's no fair if you get to play around with other students on your own!"
    m "It's not what you think, Astoria..."
    ast "What, so I'm supposed to think that Loony Luna just bent over and begged you to screw her?!"
    ast "Speaking of which..."
    ast "{size+=3}Why {size+=3}haven't {size+=3}you {size+=3}two {size+=3}{b}stopped{/b}!!!{/size}"
    lun "Sorry... Astoria... but this... is an emergency..."
    lun "I had a wrackspurt attack and needed help to purge them..."
    ast "Wrackspurt?..."
    ast "Ugh... I always knew you \"ravenclaw\" girls were {b}special{/b}..."
    ast "But you really do take the cake, Luna..."
    lun "Thank you, Astoria!"
    ast "So, is she just like this then Dumby?"
    m "Pretty much..."
    ast "Well, I guess this is OK then..."
    ast "So long as you clean this room afterwards, it reeks in here!"
    lun "Isn't it {b}great{/b}..."
    ast "No! It smells gross, Dumby! I can hardly breathe!"
    lun "Those are probably the wrackspurts... We can teach you how to get rid of them if you'd like."
    ast "No. thanks."
    lun "At least watch us finish then..."
    ast "What? Why?"
    lun "You should know... how to expel them..."
    lun "It's just... the {b}best{/b}..."
    ast "You want me to watch while Dumby-"
    g4 "Argh... This is it whores!"
    ast "!!!"
    lun "Yes!"
    g4 "ARGH!!!"
    ">You grab a tight hold of Luna's hips as you start to wildly fill her up with your cum."
    ast "..."
    ">Luna slumps forwards onto your desk, drooling as her legs shake uncontrollably."
    lun "{image=textheart}{image=textheart}{image=textheart}"
    ">You slump back into your chair, leaving Luna on your desk, leaking cum."
    m "Like the show?"
    ">You look around but can't find any trace of the small witch..."
    lun "ah... y-y-yea..."
    m "Awesome, I'm just gonna... take a nap..."
    ">With that the two of you doze off..."
    ">When you wake you find only a Luna shaped cumstain on your desk."
    jump main_room

label luna_reverted_event_8_ast_2: #Astoria repeatable part
    #Upset at Dumby for banging Luna again
    #Comes in after Luna is covered in cum
    #Starts shaming Luna about the smell of the room and her being a cumslut
    #Complains about all big boobed girls being sluts
    #Cum all over her as Astoria watches

    jump main_room

label luna_reverted_event_8_her_1: #Hermione part 1#NEEDS POSING
    call her_main("[genie_name], I hope you're not too busy to ben-","smile","happyCl")
    her "[genie_name], Luna! What are you two doing?!"
    m "ah... Isn't it obvious?"
    her "Ugh... Why are you two fucking then?"
    lun "Mmmm... we're getting rid... of some nasty wrackspurts!"
    her "You're still going on about that? I told you before, you're just horny!"
    lun "Stop... ah... being closed... minded hermione..."
    lun "I bet you... didn't even realise that... Dumbledore was a genie at first!"
    her "My goodness, you're such an {b}idiot{/b}!"
    lun "Don't be mean Hermione... is it the wrackspurts that are bothering you?"
    lun "I'm sure that we can teach you how to get rid of them by yourself!"
    her "I know how to play with myself, idiot!"
    lun "oh..."
    lun "Well if you just want to watch us, I don't mind..."
    her "Don't you have any shame!?"
    lun "mmmm... why should I be ashamed... this feels so {b}good{/b}..."
    her "I know it feels good... but you shouldn't let other people watch you do it..."
    her "Imagine if the whole school found out!"
    lun "Oh, that would be {b}fantastic{/b}!"
    lun "Imagine me... being the person to teach the world how the dispel wrackspurts!"
    her "So you'd be okay with everyone knowing you've had Dumbledore's cock in you?"
    lun "I'd give the school a demonstration if I was allowed!"
    ">Hermione's hands drift in between her legs..."
    her "Ugh... you're so fucking {b}dirty{/b} aren't you..."
    her "I just thought you were an idiot..."
    her "But now... I see you've been a bimbo this whole time without even realizing..."
    lun "A bimbo?"
    her "Uh-huh... You've become Dumbledore's new blonde bimbo..."
    lun "..."
    her "Well, I think I better give you two some alone time..."
    lun "You don't want to stay?"
    her "I need to take care of something... Until then..."
    her "Why don't you just let [genie_name] empty his balls in you..."
    ">With that, Hermione runs her pussy-drenched hand down Luna's face before turning and leaving the room."
    lun "I'm glad I've got a good friend like hermione..."
    m "..."
    lun "I wish... she could have stayed though..."
    lun "Maybe... I should have asked if... she wanted to take turns..."
    lun "That was probably... rude of me..."
    m "You'd take turns?"
    lun "Of course, sharing is w-what friends do."
    g4 "You filthy slut!"
    ">You start slamming into Luna at full pace."
    g4 "Here it comes you bimbo!"
    ">With that, you start unloading into Luna's pussy."
    lun "a-a-ahh..... soo... goooood..."
    m "..."
    ">Luna slumps forwards onto your desk, drooling as her legs shake uncontrollably."
    lun "{image=textheart}{image=textheart}{image=textheart}"
    ">You slump back into your chair, leaving Luna on your desk, leaking cum."
    m "Are you good to make your own way back?"
    lun "ah... y-y-yea..."
    m "Awesome, I'm just gonna... take a nap..."
    show screen blkfade
    with d3
    ">With that the two of you doze off..."
    ">When you wake you find only a Luna shaped cumstain on your desk."
    hide screen blkfade 
    with d3
    jump main_room

label luna_reverted_event_8_her_2: #Hermione repeatable part
    call her_main("[genie_name], I really need a good-","smile","happyCl")
    her "Oh... Hello, Luna."
    lun "H-hello Hermione."
    her "I think I'll leave you two alone..."
    ">Hermione turns to leave."
    lun "W-wait. Don't go..."
    her "..."
    lun "We can share... if you like..."
    her "Share? Share what?"
    lun "{b}Him{/b}."
    her "..."
    her "Do you really think I'm going to share with you?"
    her "Just get naked... and let him take turns..."
    her "Fucking us both... senseless..."
    her "..."
    her "Fine! But only because that's what I came here for anyway."
    ">With that, Hermione starts to strip, eager to join the fun."
    m "Don't I get a say in this?"
    her "Oh, shut it. You're hardly going to say no to this are you?"
    m "Fair point..."
    ">With that, Hermione hops up onto your desk, her eyes begging for your cock."
    her "My turn."
    #Fade to cg with Hermione and Luna fucking

    #Have Luna offer to share
    #Genie objects to not being asked before being told to shut up by Hermione
    #Change to desk CG with both of them on it
    #Take turns fucking both 
    #Luna excited to have someone to talk with wrackspurts about
    #Starts talking about how they could pleasure each other
    #Hermione cums at the idea of it
    #Send both home covered in cum

    jump main_room

label luna_reverted_event_8_ton_1: #Tonks part 1#NEEDS POSING
    call ton_main("Professor Dumbledore!","horny","base","raised","L")
    lun "!!!"
    m "!!!"
    ton "I didn't think you'd be able to land a grade-a bird like this you old horndog!"
    ton "How'd you manage this one then? Love potion? Points? Gold?"
    lun "He's helping me... ah... get rid of... my wrackspurts!"
    ton "..."
    ton "Mind control?"
    m "Nope."
    ton "Then should I ask what the hell a \"wrackspurt\" is?"
    m "Ugh... Luna can explain them..."
    lun "ah... they're nasty little... mmmm... creatures that make... ah... you want... mmm... to {b}fuck{/b}."
    ton "..."
    lun "You should... ah... be careful, Ms Tonks... {image=textheart} we're expelling a lot... {image=textheart} of them..."
    ton "Really? And how will I know If these \"wrackspurts\" are after me...?"
    lun "You'll feel... ah... hot...{image=textheart} down there..."
    ton "Oh... I see..."
    ton "You know, you should come visit me after hours Miss Lovegood, I think I might also be able to help you out..."
    m "Hey!"
    lun "Ah... thank you... {image=textheart} Ms tonks... but I don't think... ah... you'll {b}taste{/b} as good..."
    ton "Now, now, you don't know that... I taste like {b}heaven{/b}..."
    lun "There's just... ah{image=textheart} no way... your cum can...{image=textheart} taste half as good..."
    ">Tonks hand disappears down the front of her pants..."
    ton "Oh I see how it is..."
    lun "Ah... you do?"
    ton "Uh-huh... You're just Dumbledore's little cumslut... aren't you?"
    lun "That's it!"
    ton "So you admit it then?"
    lun "Of course! I'm proud... to be a cumslut!"
    lun "As an auror you should... ah{image=textheart} know the importance of... mmm{image=textheart} warding off evil magic!"
    ton "There's warding..."
    ton "And then there's just being covered in cum..."
    lun "Oh..."
    lun "Well, they're both fun!"
    ton "Fuck... you've really done a number on this her, haven't you, Dumbledore..."
    m "She was like this from the start..."
    lun "Mhmm!"
    ton "Then you've lucked out on finding the horniest little nymph to ever live..."
    lun "I am not... a nymph!"
    m "more like Nympho."
    ton "Anyway... all this talk of how much you love your headmasters yummy cum..."
    ton "I want to see it..."
    m "See what?"
    ton "Her covered in it..."
    lun "You do?"
    ton "Ugh... you bet... nothing like seeing your students soaking in their headmasters spunk..."
    lun "{image=textheart}{image=textheart}{image=textheart}"
    menu:
        "Where should you cum?"
        "-On her face-":
            m "On your knees slut!"
            lun "Mhmm!"
            ">Luna quickly hops off the desk and smiles in front of your cock..."
            lun "Need me to-"
            g4 "Shutup!"
            lun "..."
            g4 "Ugh... here it is you little whore!"
            ton "..."
            ">Eager to show off to your audience you fire off a colossal load over cum over luna's waiting face."
            lun "{image=textheart}{image=textheart}{image=textheart}"
            lun "{size=-5}thank you...{/size}"
            ">Tonk's fingers noticeably begin to speed up."
            ton "Mmmm, damn... where were all the sluts like this when I was in school..."
        "-Fire it in her-":
            g4 "ARGH!!! TAKE IT ALL YOU LITTLE WHORE!"
            ">You start filling up poor Luna as her hungry pussy does it's best to milk you dry."
            lun "Oh thank you! thank you! thank you!"
            ton "Wow..."
            lun "Ugh...{image=textheart} it's like he's... pumped me full of magic..."
            ">Tonk's fingers noticeably begin to speed up."
            ton "Mmmm, damn... where were all the sluts like this when I was in school..."
    ton "ah... this has certainly been...{p}fun."
    ton "But I think I best be on my way... I need to take care of some \"rockspoons\" of my own..."
    lun "Ugh... You don't want to see us go again?"
    ">With that slips your softening cock back into her tight hole..."
    m "Ugh... can't we have a break first?"
    lun "..."
    ">Luna simply looks back at you with the eyes of a puppy dog begging for a treat."
    m "Fine... just start off slowly this time!"
    lun "That's no fun..."
    ton "Wow... you two really are going to go again, aren't you?"
    lun "You don't have to... a-ah...{image=textheart} stay if you don't want to..."
    ton "Oh...{p}I may as well stick around for a little bit longer..."
    ">Tonks' angrily fingers her cunt while she stares hungrily at Luna's bouncing boobs."
    show screen blkfade 
    with d3
    pause 2
    hide screen blkfade
    with d3
    g9 "NO! MORE!"
    lun "Pleaaaaaase!"
    ton "Yeah, you can make it one more round Dumbledore!"
    g9 "I've already gone four rounds!"
    lun "But there are still so many-"
    g9 "Well, too bad, I'm about to pass out."
    ton "Hmmm, he's probably right, Luna... He is pretty old."
    lun "That shouldn't matter!"
    ton "It's also getting rather late. As your teacher, it is my responsibility to make sure you follow curfew."
    m "The whole cum bath thing is OK though?"
    ton "Surprisingly, there's nothing about a \"cum bath\" in the teachers handbook..."
    m "Fair enough. You two going to bed suits me anyway."
    ton "Well, come on then, Luna, hurry up and get dressed, I'll walk you home."
    lun "Alright then Miss Tonks..."
    ">With an airy smile, Luna picks up her clothes and places them on over her cum soaked form."
    ton "Aren't you going to scourgify yourself before we go?"
    lun "What, Why?"
    ton "No offence honey, but you reek... I'm feeling light headed just standing next to you."
    lun "Oh that's just the wrackspurts! They're corpses can have that affect on people."
    lun "I {b}love{/b} the smell myself... Besides, I need to wear them to act as a warning to the other wrackspurts while I sleep!"
    ton "You mean you expect me to walk you back to your room covered head to toe in cum?"
    lun "You don't have to... I can make my own way home."
    ton "I wouldn't miss this for the world... All we need is a leash and we can cross a line off my bucket list."
    lun "What?"
    ton "Never mind, let's just go before the prefects start whining about curfew."
    ">With that, tonks walks off with the cum-soaked Luna..."
    m "Finally... I thought they'd never leave..."
    ">You collapse into your chair and doze off seconds later."
    jump main_room


label luna_reverted_event_8_ton_2: #Tonks repeatable part
    #shocked to see that they're going at it again
    #Immediately starts touching herself
    #Starts talking about how excited she is to take Luna home covered in cum again
    #Talks about how wet she was during it
    #Tonks starts talking about how she wishes she could be so brazen
    #Cum all over Luna and Tonks excitedely takes her home while offering to lick her clean

    jump main_room













