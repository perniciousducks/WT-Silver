

label luna_reverted_greeting_1: #reverted Luna explains the wrackspurt problem #DONE
    $ days_to_luna = 3
    $ luna_corruption = -1 #Triggers event during the evening.

    $ luna_pupil_color = "blue"
    $ luna_l_arm = 1
    $ luna_r_arm = 2

    $ lun_hair_style = "A"

    $ lun_request_wear_top = True
    $ lun_request_wear_bottom = True
    $ lun_request_wear_glasses = True
    $ lun_request_wear_stockings = False
    $ lun_top = "top_1"
    $ lun_bottom = "skirt_1"
    $ lun_glasses = "spectrespecs"

    call luna_reset

    $ lun_genie_name = "Sir" #reset genie's name with Luna
    $ luna_name = "Miss Lovegood" #reset luna's name with genie

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
    $ luna_corruption = 0

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
    call lun_main("ah... is this how it should be done?","pout","base","sad","stareL")
    m "As long as it's feeling good I'm sure it's working. If you keep this up I'm sure you'll be rid of those nasty wickerspoons."
    call lun_main("that's nice...","base","closed","sad","R")
    call lun_main("...","normal","base","sad","stareL")
    call lun_main("are you sure this will work, sir?","soft","seductive","sad","mid")
    m "Of course I am! Do you dare doubt the powerful Dumbelldoor?"
    call lun_main("certainly not, sir...","normal","wide","sad","R")
    call lun_main("it's just...","normal","seductive","sad","down")
    call lun_main("I'm not sure this is going to get rid of them...","pout","seductive","sad","mid")
    m "What makes you say that?"
    call lun_main("do you remember how I said the wickerspats were like a nasty itch, sir?","normal","seductive","sad","R")
    m "I do."
    call lun_main("well... as nice as this massage feels...","normal","seductive","sad","down")
    call lun_main("it's not really scratching that itch sir...","pout","angry","sad","stareL")
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
    call lun_main("yes...","base","seductive","angry","stareL")
    m "(I think this is it!)"
    call lun_main("Ah... ah...{image=textheart}","grin","seductive","sad","R")
    call lun_main("{size=+4}mmm... yes...{image=textheart}{/size}","base","seductive","sad","down")
    call lun_main("{size=+8}ah... ah...{/size}","grin","seductive","sad","stareL")
    call lun_main("!!!","grin","wide","base","empty")
    call nar(">There's a blur of movement under Luna's skirt.")
    call lun_main("ah! I think they're attacking me, sir!","base","wide","sad","stareL")
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
    call lun_main("my god!!! there's so much magical energy in it!","base","wide","sad","stareL")
    call lun_main("I've never sensed anything this powerful before!","base","wide","sad","down")
    m "Ah yes, well I am the great fumblemore!"
    call lun_main("even so sir...","pout","angry","angry","mid")
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
    call lun_main("{size=+4}It's {size=+4}amazing!!!!!{image=textheart}{image=textheart}{/size}","base","happyCl","sad","stareL")
    call lun_main("can I have the rest? Please sir?","base","wide","sad","mid")
    m "Sure..."
    ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
    $ luna_cum = 13
    call lun_main("...","full","seductive","sad","empty")
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","stareL")
    pause
    $ luna_cum = 14
    call lun_main("...","full","seductive","sad","empty")
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","stareL")
    $ luna_cum = 15
    call lun_main("...","full","seductive","sad","empty")
    call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","stareL")
    $ luna_wear_cum = False
    call lun_main("ah...","base","happyCl","sad","stareL")
    call lun_main("amazing...","base","seductive","sad","stareL")
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

    jump luna_away



label luna_reverted_event_1: #Masturbate for genie again. #DONE
    $ luna_corruption = 1
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
    call lun_main("but getting rid of them... feels... so... good...","pout","base","sad","stareL")
    call lun_main("I'm almost glad I've got them...","pout","base","sad","stareL")
    m "The positive feelings you have are your body reacting to the wickerspats being expelled from your body."
    call lun_main("really?","base","closed","sad","R")
    call lun_main("ah...","normal","base","sad","stareL")
    call lun_main("I must... ah... be expelling a lot then...","soft","seductive","sad","mid")
    call lun_main("in fact...","normal","wide","sad","R")
    call lun_main("ah...","normal","seductive","sad","down")
    call lun_main("I think... ah... I'm about to... ah...","pout","seductive","sad","mid")
    call lun_main("Mmmm, it's just like... last time...","normal","seductive","sad","R")
    m "Oh, are you cumming already?"
    call lun_main("cumming?","normal","seductive","sad","down")
    call lun_main("what's? ah...{image=textheart}","pout","angry","sad","stareL")
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
    call lun_main("yes...","base","seductive","angry","stareL")
    m "(I think this is it!)"
    call lun_main("Ah... ah...{image=textheart}","grin","seductive","sad","R")
    call lun_main("{size=+4}mmm... yes...{image=textheart}{/size}","base","seductive","sad","down")
    call lun_main("{size=+8}ah... oh... frickity!!!{/size}","grin","seductive","sad","stareL")
    call lun_main("!!!","grin","wide","sad","mid")
    call nar(">THere's a blur of movement under Luna's skirt.")
    call lun_main("ah! thank you, [lun_genie_name]!","base","wide","sad","stareL")
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
    $ luna_corruption = 2
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
    call lun_main("ah... {image=textheart} yes...","base","wide","sad","stareL")
    call lun_main("these visits are starting to become all I can think about...","base","seductive","sad","down")
    m "Hmmm... Do you think that's a bad thing?"
    call lun_main("ah... of course not!","normal","happyCl","sad","R")
    call lun_main("it just... means that it's working...","pout","base","sad","stareL")
    call lun_main("if only I could spend all day up here...","base","base","sad","stareL")
    m "Do you think a full day of treatment would get rid of them?"
    call lun_main("ah...","base","base","sad","stareL")
    call lun_main("probably not...","soft","seductive","sad","mid")
    call lun_main("but...","base","wide","sad","R")
    call lun_main("ah...","base","seductive","sad","down")
    call lun_main("I think... it'd probably feel...","soft","seductive","sad","mid")
    call lun_main("nice...{image=textheart}{image=textheart}{image=textheart}","base","seductive","sad","R")
    m "Speaking of feeling nice..."
    call lun_main("Ah... I think I'm... cumming [lun_genie_name]...","open_tongue","seductive","sad","down")
    call lun_main("ah...{image=textheart}","base","seductive","sad","stareL")
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
    call lun_main("What? They got you too?","base","angry","sad","stareL")
    m "I was afraid this might happen with you dispelling all of your personal wrackspurts into this room..."
    m "This is why I didn't want you doing this outside the office..."
    call lun_main("It could have been a disaster [lun_genie_name]...","base","angry","sad","stareL")
    call lun_main("But will you be alright?","soft","wink","raised","mid")
    m "Oh don't worry about me, I'm a {i}master{/i} when it comes to this..."
    call lun_main("Of course... These are your techniques after all...","base","happyCl","sad","mid")
    call lun_main("Would it...","base","seductive","sad","R")
    call lun_main("Would it be OK if I watched [lun_genie_name]?","base","annoyed","sad","mid")
    call lun_main("Just as a way to improve my own technique!","base","wink","base","stareL")
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
    $ luna_corruption = 3
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
    call lun_main("They aren't by any chance bothering you at the moment are they [lun_genie_name]?","base","wink","sad","stareL")
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






# UNFINISHED!!!
label luna_reverted_event_4: #Luna gentle BJ for anout 9 hours and 14 orgasms from Genie
    $ luna_corruption = 4
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
    call lun_main("today is a sunday...","base","wink","sad","mid")
    m "It is?"
    call lun_main("Of course! Can't you tell how happy the sun is?","base","wink","sad","mid")
    m "..."
    call lun_main("anyway... seeing as how it's Mr Sun's happy day...","base","wink","sad","mid")
    call lun_main("I don't have any classes!","base","wink","sad","mid")
    call lun_main("So I was wondering... what are you up to today [lun_genie_name]?","base","wink","sad","mid")
    m "Probably just working on some reports for the ministry..."
    m "Why?"
    call lun_main("Well if you wouldn't mind...","base","wink","sad","mid")
    call lun_main("Maybe I could get a few more of my nasty wrackspurts out for you?","base","wink","sad","mid")
    call lun_main("I just feel so bad knowing that I gave them to you...","base","wink","sad","mid")
    m "I wouldn't blame yourself-"
    call lun_main("But I do!","base","wink","sad","mid")
    call lun_main("The idea of all those nasty things being trapped in there...","base","wink","sad","mid")
    call lun_main("Causing so much discomfort...","base","wink","sad","mid")
    call lun_main("It's all I've been able to think about!","base","wink","sad","mid")
    m "I suppose if it's bothering you so much I can let you get a few out."
    call lun_main("oh thank you, thank you, thank you!","base","base","sad","mid")
    call lun_main("You don't know how much better I'll feel once I get them {b}all{/b} out!","base","base","sad","mid")
    m "I don't think yo-"
    show screen blkfade
    with d3


label luna_reverted_event_5: #Luna regular BJ for about 5 hours with Luna masturbating the whole time

label luna_reverted_event_6: #Luna BJ with Hermione interrupting

label luna_reverted_event_7: #Luna sex

label luna_reverted_event_8: #Luna sex with daddy roleplay

label luna_reverted_event_9: #Luna sex with Hermione
