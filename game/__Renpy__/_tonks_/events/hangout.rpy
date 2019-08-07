

### Tonks Hangout Event ###

label tonks_hangout:

    call setup_fireplace_hangout(char="tonks")

    $ nt_he_counter += 1
    if firewhisky_ITEM.number >= 1:
        $ firewhisky_ITEM.number -= 1

    $ nt_he_drink.start()

    label tonks_hangout_continue:
        hide sceen bld1
        with fade
        call bld

    # High Priority Events First!

    # Events.
    if hermione_intro.E5_complete and not hang_with_tonks.E1_complete:
        jump hang_with_tonks_E1

    if hermione_intro.E6_complete and her_tier >= 2 and not tonks_requests_unlocked:
        jump hang_with_tonks_E2

    # Tonks Auror Stories.
    $ random_number = renpy.random.randint(1, 3)
    if random_number == 1:
        $ nt_he_story.start()

    label end_tonks_hangout:

        call bld
        if ton_friendship < 100:
            $ renpy.play('sounds/win_04.mp3')
            show screen notes
            ">You spend the evening hanging out with Tonks.\n>Your relationship with her has improved."
            hide screen notes
        else:
            ">You spend the evening hanging out with Tonks."
        call bld("hide")

    if ton_friendship < 100: # max
        if game_difficulty < 2:      #Easy difficulty
            $ ton_friendship += 4
        elif game_difficulty == 2:   #Normal
            $ ton_friendship += 3
        else:                        #Hardcore, larger wine bonus.
            $ ton_friendship += 2

    if ton_friendship > 100:
        $ ton_friendship = 100

    if daytime:
        jump night_start
    else:
        jump day_start



label nt_he_wine_intro:
    call bld
    m "Care for a drink?"
    call ton_main("Of course, [ton_genie_name].","base","base","base","mid", ypos="head")
    call ton_main("Hit me!","horny","base","base","down")
    pause.1

    # Show wine
    call give_reward(">You hand over a bottle of wine you found in the cupboard to Tonks...", gift="interface/icons/item_wine.png", sound=False)

    call ton_main("Wine?","open","base","raised","down")
    call ton_main("Don't you have anything stronger?","upset","base","base","R")
    m "Like what?"
    call ton_main("How about \"firewhisky?\" Got any of that?","open","base","base","mid")
    m "I fear not..."
    call ton_main("What a bummer. I guess wine will do for the day.","upset","base","sad","down")
    m "(Maybe there is some of that stuff stored in that cupboard as well...)"

    $ firewhisky_ITEM.unlocked   = True  # Makes this available in the cupboard.
    $ firewhisky_ITEM.unlockable = False # Makes this available at the shop as a buyable item.

    jump tonks_hangout_continue


label nt_he_firewhisky_intro:
    call bld
    g9 "Look what I've got!"
    pause.1

    # Show firewhisky
    call give_reward(">You hand over a bottle of firewhisky to Tonks...", gift="interface/icons/item_wine.png", sound=False)

    call ton_main("Finally, the good stuff!","horny","base","base","down", ypos="head")
    call ton_main("I'm glad you brought out some firewhisky this time...","base","base","base","down")
    call ton_main("Wine makes me giggly, and lowers my sense of judgment.","base","base","upset","L")
    m "..."
    call ton_main("Got a frog in your throat?","open","base","raised","mid")
    m "No, I was just waiting for an opening."
    call ton_main("Sorry, I guess I talk a lot once I get going...","angry","base","wide","mid")
    call ton_main("Bottoms up.","horny","base","base","down")
    call play_sound("gulp")
    call ton_main("*Gulp*{w=0.6}{nw}","base","closed","sad","mid", trans="hpunch")
    call ton_main("*Cough*-*Cough*","open","closed","sad","mid")
    call ton_main("Yeah, that was a mistake.","angry","base","upset","down")
    m "I don’t drink whisky that often, but even I know not to down it in one..."
    call ton_main("*Mmm*... that's the stuff.","horny","base","base","ahegao")
    m "Are you even listening?"

    jump tonks_hangout_continue


label nt_he_firewhisky_E1:
    call bld
    m "Another glass of firewhisky?"
    call ton_main("Fill er up.","base","base","base","down", ypos="head")
    call ton_main("...","horny","base","base","down")
    call ton_main("A little bit more...","open","base","raised","down")
    call ton_main("A bit more...","horny","base","angry","down")
    call ton_main("That's it, cheers.","base","base","base","mid")
    if daytime:
        m "Boring lessons ahead?"
        call ton_main("Not in particular, why?","open","base","base","mid")
        m "You might regret going back to classes after drinking this much."
        call ton_main("Oh don't you worry, [ton_genie_name].","smile","happyCl","base","mid")
        call ton_main("I could down this entire bottle without anybody being able to notice a thing.","horny","base","base","L")
        m "You're one glass in and swaying like a buoy..."
        call ton_main("*Hick* Oh well-...","open","base","base","ahegao", trans="hpunch")
        call ton_main("No risk, no fun!","horny","base","base","mid")
    else:
        m "Long day?"
        call ton_main("Not in particular, why?","open","base","base","mid")
        m "..."
        m "No reason..."

    jump tonks_hangout_continue


label nt_he_firewhisky_E2:
    call bld
    m "More firewhisky?"
    call ton_main("Thought you’d never ask...","horny","base","base","down", ypos="head")

    jump tonks_hangout_continue


label nt_he_firewhisky_E3:
    call bld
    m "Want to get drunk?"
    call ton_main("Of course.","base","base","base","down", ypos="head")
    if daytime:
        call ton_main("I'm not going to regret this, am I?","angry","base","worried","down")
        call ton_main("Hopefully my students won't notice...","horny","base","base","mid")
    else:
        call ton_main("I'd never say no to that!","horny","base","base","down")

    jump tonks_hangout_continue


label nt_he_firewhisky_E4:
    call ton_main("Bottoms up.","horny","base","base","mid", ypos="head")
    call play_sound("gulp")
    call ton_main("*Gulp*{w=0.8}{nw}","scream","closed","base","mid")
    call play_sound("gulp")
    call ton_main("*Gulp*{w=0.8}{nw}","scream","closed","worried","mid")
    call play_sound("gulp")
    call ton_main("*Gulp*{w=0.8}{nw}","scream","closed","sad","mid")
    call ton_main("*Aaaaaaaahhhh!!!*...","open_wide_tongue","base","base","ahegao", trans="hpunch")
    m "....................."

    jump tonks_hangout_continue



### Events ###

label hang_with_tonks_E1:
    call ton_main("So, that Granger girl is causing you two trouble?","open","base","base","mid", ypos="head")
    m "Quite a bit. She's not too thrilled on the idea of favour trading."
    call ton_main("Maybe I can be of help with her?","base","base","wide","L")
    call ton_main("I can be very convincing.","horny","base","raised","mid")
    m "What are you suggesting?"
    call ton_main("To persuade her having a try of it herself, for a start...","open","base","base","R")
    call ton_main("Convince her that trading favours isn't all bad.","base","base","base","mid")
    m "That would indeed be very helpful. She's stubborn in that regard."
    call ton_main("You don't have to tell me. She's been lecturing me about those \"sexual favours\" since the very day I got here...","open","base","base","R")
    call ton_main("But I shouldn't complain about that...","base","base","base","mid")
    call ton_main("Hearing those naughty words spill out of her gorgeous little mouth really gets me going!","horny","base","base","ahegao")
    g9 "I can imagine so."
    call ton_main("When she describes all the wrong-doings of those filthy \"Slytherin girls\"...","open","base","angry","mid")
    call ton_main("How can I possibly get tired of that!","base","base","base","mid")
    call ton_main("I'm very glad that I've decided to join you two.","open","base","base","down")
    call ton_main("As an Auror It's just constant busy work...","open","base","angry","mid")
    call ton_main("Not to mention the hours.","angry","base","upset","down")
    call ton_main("And the mortality rate...","upset","base","worried","R")
    call ton_main("If I'd realized the benefits of being a teacher at Hogwarts, I would have signed up straight away!","horny","base","base","ahegao")

    ">You spend the evening by conspiring against Hermione with Tonks..."
    ">You feel a faint bond forming between you two..."

    $ hang_with_tonks.E1_complete = True

    if daytime:
        jump night_start
    else:
        jump day_start


label hang_with_tonks_E2:
    call ton_main("So, [ton_genie_name],... what's the going rate around here then?","open","base","base","mid", ypos="head")
    m "Going rate?"
    call ton_main("How much do you pay your students to fool around?","base","base","base","mid")
    m "Oh... It depends on what you want them to do."
    call ton_main("How much for a lap dance?","horny","base","raised","mid")
    m "Again, it depends on the student."
    call ton_main("...","upset","base","base","R")
    m "But if I had to guess, I'd say about 25 points."
    call ton_main("Unbelievable that you've managed to convince these girls to offer themselves up to you, for a bunch of imaginary points...","open","base","angry","R")
    m "Works for the internet..."
    call ton_main("The what?","open","base","raised","mid")
    m "A place you go when you want to procrastinate..."
    m "Or you happen to be sitting on the toilet..."
    m "Anyway, you can't just ask for a lap dance straight away, You have to butter them up first."
    call ton_main("How so?","base","base","raised","mid")
    m "Well most of them aren't going to just do whatever you say from the get go..."
    m "You have to slowly earn their trust over time and start out small..."
    call ton_main("*Awww*... really? Can't I just cheat a bit?","upset","base","worried","L")
    m "..."
    m "Just take it slow all right, I'm sure you'll find a cute boy who'll be willing to do whatever you want anyway."
    call ton_main("...","upset","base","base","R")
    call ton_main("But what if I want a girl?","horny","base","raised","mid")
    g4 "(...!)"
    m "Whatever floats your boat."

    $ tonks_requests_unlocked = True
    call popup("You can now ask Tonks to sell \"Public Requests\" to her students!", "Congratulations!", "interface/icons/head/head_tonks_1.png")

    $ hang_with_tonks.E2_complete = True

    if daytime:
        jump night_start
    else:
        jump day_start



### Discuss Hermione ###

label nt_he_hermione_panties:
    # You tell Tonks zjaz Hermione has shown you her panties.
    #if hg_T1_panties_trigger

    jump end_tonks_hangout


label nt_he_hermione_talk:
    # You tell Tonks about when you got busted jerking off on front of Hermione.
    #if hg_T2_jerk_off_trigger

    jump end_tonks_hangout


label nt_he_hermione_strip:
    # You tell Tonks about Hermione stipping and Snape walking in.
    #if hg_T3_strip_trigger

    jump end_tonks_hangout


label nt_he_hermione_handjob:
    # You tell Tonks about Hermione's attempts to give you a hangjob.
    #if hg_T4_handjob_trigger

    jump end_tonks_hangout


label nt_he_hermione_blowjob:
    # You tell Tonks about the memorable day in which Hermione gave you a blowjob.
    #if hg_T5_blowjob_trigger

    jump end_tonks_hangout


label nt_he_hermione_sex:
    # You tell Tonks about the time you put your p in Hermione's v.
    #if hg_T6_sex_trigger

    jump end_tonks_hangout













### Tonks Auror Stories ###

label nt_he_story_intro_E1:
    call ton_main("Thanks for accepting my job application by the way.","base","base","base","mid", ypos="head")
    m "I didn't really have that much choice in the matter."
    call ton_main("Oh, yeah...","smile","happyCl","base","mid")
    call ton_main("...","angry","base","base","R")
    call ton_main("I'll do well, you'll see.","open","base","base","R")
    call ton_main("After all, I was taught by one of the best aurors there is.","base","base","base","mid")
    call ton_main("And I do wish to teach those students a couple of useful things while I'm here...","open","base","worried","R")
    call ton_main("But teaching a class of beginners should be a breeze.","base","happyCl","base","mid")
    m "I never said I doubted your abilities."
    call ton_main("Maybe I'll give you a demonstration some day...","horny","base","base","mid")
    call ton_main("And I'm not talking about my intellectual abilities...","horny","base","angry","mid")
    g9 "I'm a well for all kinds of knowledge!"
    call ton_main("Anyway, I think I'm gonna go hit the sack.","open","base","base","R")
    m "There's more firewhisky where this came from, so feel free to stop by any time to talk about your progress."
    call ton_main("I'll never say no to a free drink.","base","base","base","down")
    call ton_main("And I'll keep you updated on the academics as usual.","base","base","base","mid")
    m "(That's not the kind of progress I meant...)"

    jump end_tonks_hangout


label nt_he_story_intro_E2:
    call bld
    m "You mentioned an auror last time if I'm not mistaken."
    call ton_main("Moody?","angry","wide","wide","wide", ypos="head")
    m "Not in particular."
    call ton_main("What?","open","base","raised","mid")
    m "..."
    call ton_main("You talking about Madeye?","open","base","angry","mid")
    m "I can see perfectly fine, dear."
    call ton_main("Madeye Moody is the auror that taught me.","open","base","angry","R")
    m "Oh, of course."
    m "(His parents must have hated him...)"
    #m "(What's wrong with a normal name... like Will Smith, or Robin Williams?)"
    m "Anything you'd like to tell me about him?"
    call ton_main("Well, he's a bit of a weirdo, but he knows his stuff.","open","closed","sad","mid")
    call ton_main("I guess if you're as paranoid as him, you'll end up knowing everything there is about the craft...","open","base","sad","R")
    m "Paranoid of what?"
    call ton_main("Dark wizards.","open","base","sad","R")
    m "So he's a racist?"
    call ton_main("No, but he's old... I think he should just retire to be honest.","open","closed","sad","mid")
    call ton_main("His methods have gotten progressively more nefarious...","open","base","sad","R")
    call ton_main("Some would argue he should be locked up himself, for all the unethical things that he did to lock them up...","angry","base","base","mid")
    g9 "And you?"
    call ton_main("Me? What about me?","upset","base","angry","mid")
    m "You wouldn't say what we do is unethical as well?"
    call ton_main("Did you start drinking before I got here?","open","base","angry","mid")
    m "I never stop..."
    call ton_main("...","upset","base","base","up")

    jump end_tonks_hangout


label nt_he_story_intro_E3:
    call ton_main("Do you always happen to have a bottle ready for me?","base","base","raised","mid")
    g9 "For you, always."
    call ton_main("I don't even have to visit the Hogshead to get a drink anymore...","base","base","base","down")
    m "Why go anywhere when you got a magic cupboard that fills itself with alcohol."
    call ton_main("It does?","open","base","raised","mid")
    m "At least I think that’s how it works..."
    m "I may be a Genie, but I can't just turn water into wine...or whisky."
    m "(At least not in this world...)"
    call ton_main("Yeah, that would be impressive.","smile","happyCl","base","mid")
    call ton_main("I haven't found a single wizard that could do that.","open","base","base","mid")
    m "Ah yes. Because all those cunning bachelors are already taken...{w}or gay..."
    call ton_main("No. Single as in...no one can do it.","open","closed","sad","mid")
    call ton_main("It's almost impossible to summon drinks and food out of thin air.","open","base","sad","R")
    call ton_main("Best they can do is conjure water out of the surrounding humidity.","upset","base","base","R")
    m "If only I had my powers...I could do it with a snap of a finger."
    call ton_main("I'm sure you could...","smile","happyCl","base","mid")

    ">You brag about your almighty powers in front of the witch..."
    ">If only you hadn't lost them..."

    #m "(What kind of shit wizard can't even make food...)"
    #m "What about water though, doesn't that count as a drink?"
    #call ton_main("...","base","base","base","mid")
    #call ton_main("You know what, I never thought of that.","base","base","base","mid")
    #m "What even counts as food or drink... sound pretty arbitrary to me."
    #call ton_main("I don't think we're supposed to think about it too hard.","base","base","base","mid")
    #m "Less obvious plot-holes that way I suppose..."
    #call ton_main("Less what, sorry?","base","base","base","mid")
    #m "No matter, just thinking out loud is all."

    jump end_tonks_hangout


label nt_he_story_intro_E4:
    call ton_main("I've been so busy lately... The days here is flying by faster than a Firebolt.","open","closed","sad","mid", ypos="head")
    m "I'm not sure I know that...spell?"
    call ton_main("It's a broom...","base","base","base","mid")
    m "Oh, I see... I'm not into brooms you should know."
    m "Or anything that is inconveniently stiff and long to ride on..."
    call ton_main("Well I don't mind that... Most witches don't.","open","base","base","R")
    g9 "You should ask me about my knowledge of \"flying carpets\" instead!"
    g9 "I can tell you everything about the newest model."
    call ton_main("Do you own one yourself? A carpet?","smile","base","base","mid")
    m "No. But a friend of mine does..."
    m "It's more of a pet, actually."
    m "Technically they are sentient beings..."
    call ton_main("Yes, I've heard of that. How interesting.","smile","happyCl","base","mid")
    call ton_main("Would you like that? Owning a pet?","base","base","angry","mid")
    m "Sure. Why do you ask?"
    call ton_main("Just out of curiosity...","horny","base","base","mid")
    m "(...)"

    ">You keep thinking about what Tonks meant with that, whilst she eyes you up expectantly..."

    jump end_tonks_hangout


label nt_he_story_intro_E5:
    call bld
    m "You still haven't told me anything about your time as an auror..."
    call ton_main("Well, what would you like to know?","open","base","worried","R", ypos="head")
    m "That \"moody guy\" taught you, you said. You could start there."
    call ton_main("Well, the job of an auror is a bit different now than how it was ten-or-so years ago.","open","base","worried","mid")
    call ton_main("I studied to become an auror with the hopes of taking down evil wizards.","angry","base","worried","down")
    m "Sounds like a \"90s B movie\" to me."
    call ton_main("Tell me about it...","upset","base","angry","R")
    call ton_main("But that's not at all how the job is anymore.","open","closed","sad","mid")
    m "Was it ever?"
    call ton_main("That's what they told me...","upset","base","sad","R") #'tell' to 'told'
    call ton_main("But right now, it's mostly droves of paperwork...","open","closed","sad","mid")
    call ton_main("Something they didn't keep up with back in the days...","open","base","sad","mid")
    m "Don’t you have people for that sort of thing?"
    call ton_main("We're our own division, and are supposed to follow strict guidelines set by the ministry...","open","closed","sad","mid")
    call ton_main("There was too much bad stuff happening for anyone to lecture the aurors though...","upset","base","worried","R")
    m "Then why did you stay?"
    call ton_main("I'm here, aren't I?","base","base","angry","mid")
    call ton_main("Why do you think I jumped on the opportunity to teach here?","open","base","base","mid")
    m "(You kind of created that opportunity yourself...)"
    call ton_main("I learned a lot, though. And I always wanted to use that knowledge to teach others...","open","closed","base","mid")
    call ton_main("I just didn't think I was up for it yet. Not until I stepped through these halls again...","open","base","base","mid")
    call ton_main("It made me realise how much I've missed being here.","smile","happyCl","base","mid")

    jump end_tonks_hangout


label nt_he_story_E6:
    call ton_main("Did I ever tell you about the time we arrested a vampire?","smile","happyCl","base","mid", ypos="head")
    m "You haven't even told me about your \"defence against the dark arts\" training yet, but sure, go ahead..."
    call ton_main("Right... Well, there was this vampire guy.","open","base","base","R")
    call ton_main("We spent ages looking for him, and found that he had been disguising himself as a headmaster of a muggle school.","angry","base","base","R")
    m "..."
    call ton_main("It was quite disgusting what he was doing to the students actually...","angry","base","angry","mid")
    call ton_main("He even brought over some of the teachers... they're never going to be the same...","open","base","angry","R")
    m "..."
    call ton_main("Corrupted... Forever...","angry","closed","angry","mid")
    m "(Not sure if I should feel bad at this point...)"
    call ton_main("Kind of hot, though,...don't you think?","horny","base","angry","mid")
    m "(Nevermind...)"
    call ton_main("The power vampires have over their prey.","horny","base","raised","ahegao")
    call ton_main("It's a shame that they're slaves to their own urges.","open","closed","worried","mid")
    m "(Well... there's that bad feeling I felt before.)"
    call ton_main("I get it though. Some aspects of it...","upset","base","base","R")

    jump end_tonks_hangout


label nt_he_story_intro_E7:
    call bld
    m "Now, I'm starting to feel like you've been avoiding the subject of your auror training."
    call ton_main("Is it that obvious?","angry","base","base","R", ypos="head")
    m "You brought up vampires last time without even saying hello."
    call ton_main("Vampires are interesting...","upset","base","worried","up")
    m "..."
    call ton_main("Fine, I didn't want to talk about some of Moody’s teaching methods,...","open","closed","base","mid")
    call ton_main("They tend to be quite...unconventional.","angry","base","worried","R")
    m "Like how?"
    call ton_main("Well...","upset","base","sad","down")
    call ton_main("Moody very much believed in learning by doing.","open","base","sad","mid")
    m "Sounds reasonable enough..."
    call ton_main("This is defence against dark magic we're speaking of...","open","base","raised","mid")
    call ton_main("Some of the spells and situations he put me in are borderline- if not completely- illegal.","open","base","angry","mid")
    m "Surely in a controlled environment where there's no harm to both parties..."
    call ton_main("Well,...most of the time that was the truth...","open","base","sad","R")
    call ton_main("(I can't believe I'm talking about this...)","upset","base","worried","down")
    call ton_main("(The ministry will kick Moody out faster than a blastended newt going off if I'm not careful...)","angry","base","worried","R")

    jump end_tonks_hangout


label nt_he_story_E8:
    call ton_main("I'll tell you about this one time where Moody went a bit too far.","base","base","base","mid", ypos="head")
    m "Where did this sudden urge of sharing come from?"
    call ton_main("Oh, I've been wanting to spill the beans about this for ages. I just didn't want to get anyone in trouble at the ministry...","smile","happyCl","base","mid")
    m "What is there to say I won't get you into trouble?"
    call ton_main("You won't... Would you?","open","base","worried","mid")
    m "No..."
    call ton_main("Right...","base","base","base","R")
    call ton_main("Anyway, he once brought in this werewolf that we had put in custody.","angry","base","base","mid")
    g4 "He did what?!?"
    call ton_main("See, I knew you'd react like that.","base","base","angry","mid")
    m "No, I was just taken by surprise... I didn't know they existed."
    call ton_main("Of course they do, silly!","smile","happyCl","base","mid")
    call ton_main("So he brought in this werewolf... apparently quite harmless comparatively.","open","base","base","R")
    m "Compared to what? A dog?"
    call ton_main("Compared to werewolves like Fenrir Greyback...","upset","base","angry","L")
    m "Oh yeah..."
    m "That... Guy..."
    call ton_main("Moody had worked out a deal with this guy...","open","base","base","mid")
    call ton_main("To see how I would react in a real life situation where he would turn.","base","base","angry","mid")
    m "Turn where?"
    call ton_main("Into a werewolf.","upset","base","angry","mid")
    m "Of course."
    call ton_main("Well... we hadn't taken into account that it was mating season for them...","smile","happyCl","base","mid")
    g9 "You don't say!"
    call ton_main("The guy wasn't that interested in biting me that's for sure.","base","base","base","mid")
    call ton_main("So you can see why I wasn't so keen on reporting it. More of an embarrassing situation sort of thing than anything else.","open","base","base","R")
    call ton_main("And it was totally our fault, I should’ve recognized the signs straight away... when they’re turned they’re largely driven by their instincts.","open","base","sad","down")
    m "I see."
    call ton_main("Dated him for a while...","horny","base","base","R")
    m "You did what?"
    call ton_main("Saturated my need for a dominant male relationship for a couple of months, that's for sure...","open","base","angry","mid")
    m "(That explains a few things...)"

    jump end_tonks_hangout


label nt_he_story_intro_E9:
    call ton_main("Being an auror was quite a stressful job you know.","open","base","sad","R", ypos="head")
    m "I..."
    call ton_main("It did have it's privileges...","upset","base","sad","down")
    call ton_main("The ministry was mostly concerned about the criminals making up for their crimes.","open","base","angry","mid")
    call ton_main("Not necessarily putting them in prison. I had quite a few... more or less successful techniques.","open","closed","base","mid")
    m "Such as?"
    call ton_main("Well, there was this one guy using a love potion...","angry","base","base","R")
    m "A love potion, too bad they aren’t real..."
    call ton_main("Of course they’re real, and quite effective as well.","open","closed","base","mid")
    call ton_main("Also... highly illegal.","base","base","base","mid")
    m "Oh, of course..."
    call ton_main("Anyway...","open","base","base","L")
    call ton_main("He could've ended up in prison at some point... but law isn't black and white like that.","open","base","base","mid")
    m "So you're saying that his intentions were good?"
    m "When is using drugs on people okay in your book?"
    call ton_main("In this instance, the woman in question was in an abusive relationship.","open","base","sad","R")
    call ton_main("And the man in question knew that the boyfriend was quite jealous.","open","base","base","mid")
    m "I see, so he fed her the potion to get her out of it."
    call ton_main("Right, I mean jealousy isn't that bad in a playful relationship. But it wasn't like that.","base","base","base","mid")
    m "How do you know that he was telling the truth?"
    call ton_main("Truth serum.","horny","base","raised","mid")
    m "And those aren't illegal or regulated as well?"
    call ton_main("I did say that I had my own techniques...","open","base","sad","R")
    call ton_main("And as I said... Law is more complicated than that, and in certain instances using a truth serum would be the right thing to do.","angry","base","base","R")
    call ton_main("And to be honest, who was he going to tell... It's not like he had the moral high ground.","base","base","base","mid")
    m "I see, how did the situation end up?"
    call ton_main("The girl got out of the abusive relationship and requested to have her memory adjusted.","open","base","base","mid")
    m "And that's..."
    call ton_main("That's fine if the person in question is okay with it.","open","base","base","R")
    call ton_main("They have to sign a form and all that...","base","base","base","mid")
    m "Obviously..."
    m "(Where do these people draw the line... making someone fall in love with you just like that?)"
    m "(...)"

    jump end_tonks_hangout


label nt_he_story_intro_E10:
    call bld
    m "Settled in okay?"
    call ton_main("Yes, I finally feel like I've found some sort of daily routine.","smile","happyCl","base","mid", ypos="head")
    call ton_main("This school brings back so many memories. I feel like every time I turn a corner I expect to see one of my fellow classmates.","open","base","sad","R")
    m "So, good memories?"
    call ton_main("Mostly, it's a bit different now.","base","base","base","mid")
    m "In what way?"
    call ton_main("We had to redo tasks constantly instead of actually learning new things. I think I brew the same potion a million times.","open","base","sad","R")
    call ton_main("And it was tied to this weird energy system.","upset","base","sad","down")
    m "What's that?"
    call ton_main("The teachers wanted to restrict the amount of enjoyment and fun we had so they gave us a set amount of energy points each day.","open","base","angry","mid")
    call ton_main("So if you ran out of energy points during potions, for example, you couldn't finish the lesson.","upset","base","angry","R")
    m "That doesn't make any sense."
    call ton_main("I know right... I'm glad they got rid of it.","open","base","sad","mid")

    jump end_tonks_hangout


label nt_he_story_E11:
    call bld
    m "Tell me more about your time at Hogwarts, as a student..."
    call ton_main("Of course, [ton_genie_name].","base","base","base","mid", ypos="head")
    call ton_main("Well, as you may or may not know. I'm an metamorphmagi.","open","base","base","R")
    call ton_main("It means I can change my physical appearance at will.","base","base","angry","mid")
    m "Sounds useful."
    call ton_main("It can be.","base","base","base","L")
    call ton_main("Since you can't reprimand me about it, I might as well tell you a bit about it.","open","base","raised","mid")
    m "I'm still your boss."
    call ton_main("You gonna put me in detention?","horny","base","base","mid")
    call ton_main("Or spank me across your knee?","horny","base","angry","mid")
    g9 "Don’t tempt me."
    call ton_main("There was this time where I changed my appearance into professor Snape.","base","base","base","mid")
    m "Why Snape?"
    call ton_main("Well, he was the most likely not to be in the staff room. Which is where I wanted to get in.","open","base","base","R")
    m "Why's that?"
    call ton_main("He never leaves the dungeon does he?","base","base","base","mid")
    call ton_main("Just need to take one look of his pasty face and you'll know that...","open","base","base","R")
    call ton_main("Don't tell him I said that...","upset","base","worried","mid")
    g9 "..." #[Smirk]
    call ton_main("So,...I changed my appearance to professor Snape and went towards the staff room...","open","base","angry","mid")
    m "Isn't the staff room just full of boring old teachers?"
    #call ton_main("Have you used a mirror lately?","open","base","raised","mid")
    call ton_main("My goal wasn't to talk with the teachers...","open","closed","base","mid")
    call ton_main("I was trying to get a key to the prefects bathroom.","base","base","angry","mid")
    m "And you couldn't just turn into a prefect to get in there that way?"
    call ton_main("Well, that would’ve been the clever thing to do...","open","base","sad","R")
    call ton_main("Although like everything else in this school the bathroom has a password and not a key...","open","base","sad","mid")
    call ton_main("Of course I didn't know that... I had just heard rumours about the bathroom.","angry","base","sad","down")
    m "So did you manage to get in there in the end?"
    call ton_main("Oh yeah, it was easy!","smile","happyCl","base","mid")
    call ton_main("Once I knew about the password I just had to pretend to be one of the prefects, and ask another for it.","base","base","base","mid")
    m "Smart..."

    jump end_tonks_hangout


label nt_he_story_E12:
    call bld
    m "Tell me more about that shape-shifting ability of yours..."
    call ton_main("Of course...","base","base","angry","mid", ypos="head")
    call ton_main("Most of my escapades were kind of one trick ponies.","open","base","base","mid")
    m "Sounds pretty fool proof to me..."
    m "I mean how many other students could change their appearance?"
    call ton_main("None, that's why. Process of elimination.","upset","base","sad","R")
    m "So you got punished without any sort of proof?"
    call ton_main("No, but they set up countermeasures after the time when...","open","base","worried","R")
    call ton_main("I shouldn't really talk about it. They never confronted me about it so fessing up now isn't going to do me any good.","angry","base","worried","down")
    m "Not a word leaves this office."
    call ton_main("Do you think I'm weird?","open","base","sad","mid")
    m "Everyone is a bit...weird..."
    call ton_main("Fine, I'll tell you.","angry","base","sad","down")
    call ton_main("You might have noticed but I'm a bit more comfortable with my sexuality than most people.","open","base","base","mid")
    g9 "(Oh, here we go!)"
    call ton_main("I already told you about the whole werewolf thing, and the power play fantasies with the vampire...","open","base","base","R")
    m "Well, you didn't phrase it that bluntly before but I got the gist."
    call ton_main("Well, just like many weird or odd sexual preferences they're often deeply embedded with experiences from your youth.","open","base","worried","L")
    call ton_main("So for me, there was this one time where I pretended to be a teacher...","open","base","worried","mid")
    call ton_main("As in, I literally took over their lesson when they were ill.","angry","base","base","down")
    m "How did you manage that, weren't the students notified of their leave beforehand?"
    call ton_main("No. There was just a note on their door and I ripped it off before the class got there.","open","closed","base","mid")
    m "Seems like a flawed system..."
    call ton_main("Yeah, some of the teachers to this day changed the way they do it because of this reason. Not the new ones though...","angry","base","sad","R")
    m "You haven't told me which class this was, did you turn into Snape and teach potions?"
    call ton_main("Of course not, I wasn't going to make someone hurt themselves... and Snape would've made my life hell.","open","closed","sad","mid")
    call ton_main("It was charms...","angry","base","base","down")
    m "Right..."
    call ton_main("I had been practicing some charms, and taught myself a couple on my own,...like the one for invisibility...","base","base","base","down")
    m "Impressive..."
    call ton_main("Thanks... Normally you wouldn't learn that one until much later, so you'd easily be able to dispel it.","smile","happyCl","base","mid")
    m "But you decided it was a good idea to teach it anyway?"
    call ton_main("I didn't say it was a good idea.","angry","base","base","down")
    call ton_main("It ended up not working anyway...","upset","base","worried","R")
    call ton_main("Instead of the clothes making the students whole body go see through, it just made their clothes vanish!","open","closed","upset","mid")
    call ton_main("Whilst it wasn't intentional, the memory of it still excites me a bit.","base","base","base","down")
    call ton_main("And that's where that particular fetish came from...","base","base","base","mid")
    g4 "Hold on, there's a spell to make only the clothes invisible?"
    call ton_main("That's what you focus on?","open","base","raised","mid")
    m "Well, yeah! Sound to me like you invented a new spell that no one's ever heard off..."
    g4 "And it can make people's clothing invisible?! That's kind of a big deal!"
    call ton_main("It's not a new spell... it was just novice wizards and witches not being powerful enough to cast it properly...","open","base","base","mid")
    call ton_main("Similarly to splinching.","upset","base","worried","R")
    m "(That sounds disgusting...)"
    call ton_main("Anyway, the teachers played it off as an accident... though poor Flitwick had his magical abilities questioned by the students for a while.","upset","base","sad","down")
    call ton_main("And they tried to set up some more countermeasures towards my abilities at that point.","open","base","sad","R")
    call ton_main("Not that they worked that well... I was a bit more selective of my usage, and actually thought about the consequences a bit before using it.","angry","base","sad","R")
    m "Well, you do start thinking more about others as you get older..."
    call ton_main("Yeah well, my sexual drive started to take the upper hand on my decisions from that points on, so it evened out.","smile","happyCl","base","mid")
    m "(...)"

    jump end_tonks_hangout



### Centaur Story ###

# Will be something other than a hangout event as you can't have a jerk-off interaction during them.
# Substitute Teacher for Care for Magical Creatures maybe?

label nt_he_story_centaur: # Not in use.
    call ton_main("...","worried","base","worried","mid")
    call ton_main("Very well, Professor.{w} I think I can make an exception for you.","open","base","base","R")
    g9 "And spare no details."
    call ton_main("I have your word that you will not tell a soul about any of this?","open","base","base","mid")
    g4 "Yes,...now tell me!"

    call ton_main("Very well,...","upset","base","worried","down")
    call ton_main("First you should know, there aren't many witches that could take-on and calm a large group of wild centaurs...","open","base","worried","mid")
    call ton_main("Most would foolishly try to intimidate or threaten them, and rely on their wands and spells to keep them at bay, which would only make matters worse...","open","base","worried","R")
    call ton_main("But that's not how \"I handle\" conflict with those beastly creatures...","base","base","base","mid")
    g9 "Yes?!"
    m "(I like where this is going!)"

    call nar(">*Fap!* *Fap!* *Fap!*")
    call ton_main("Centaurs don't do well with Ministry personnel{w} Even less so with female witches such as myself...","open","base","raised","mid")
    call ton_main("Making them a compelling offer so they'd peacefully return to their assigned territory was quite...{w}challenging {image=textheart}","horny","base","base","R")
    g4 "Go on..."
    call ton_main("All I did was do them a small favour.{w} A little service the Ministry would never even think of providing them with.","angry","base","worried","down")
    call ton_main("But I did it anyway...","base","base","angry","base")
    g4 "*Argh!* What did you do?"
    call ton_main("Well, I simply helped them release some of their stored up tension...","open","base","base","R")
    call ton_main("And stroked their manhood's{w}with my hands...","horny","base","base","mid")

    g9 "Yes! How filthy!"
    call ton_main("*Hmph?!* You believe what I did was filthy, Professor?!","base","wide","wide","wide")
    call ton_main("*Uhm*... I mean, it depends on how you look at it...","upset","base","worried","down")
    call ton_main("It's by far the simplest way to calm down a group of wild centaurs...","open","base","worried","R")
    call ton_main("As far as I could tell, they haven't had any females within their group...","open","base","base","mid")
    call ton_main("You can imagine the amount of tension that gets built up as a result of that...","angry","base","base","mid")
    call ton_main("(Inside those heavy, cum-filled balls!)","horny","base","base","ahegao", hair="horny") # ahegao
    m "So your idea was to jerk them off?"

    call ton_main("Well, yes.{w} They can't easily reach around to do it themselves now, can they?","horny","base","base","mid")
    m "(Those poor bastards!)"

    g4 "Must have been a real...{w}*argh!*- relief for them!"
    call ton_main("I believe so too, Sir.","base","base","base","mid")
    call ton_main("You should know, I never shy away from getting my hands dirty!","horny","base","raised","mid", hair="horny")
    g4 "*Agh!* Fuck! I'm getting close..."
    call ton_main("Most of the Ministry view Centaurs as \"lesser\"... As animals.","open","base","base","R")
    call ton_main("But not me. To me they're all powerful, and magnificent creatures.","base","base","angry","mid")
    call ton_main("And it's known that above all they virtue strength, dominance, and lust...","open","base","base","mid")
    call ton_main("(And they are so{w} fucking{w} hung!!!)","horny","base","base","ahegao", hair="horny") # Ahegao

    #Genie cums
    stop music fadeout 1.0
    g4 "Yes! Here it comes!"

    call cum_block
    call gen_chibi("cumming_behind_desk")
    with d3
    pause 1

    call ton_main("For a Ministry person to submit the way I did was quite the shock to them...","open","base","raised","R", hair="horny")

    call cum_block
    m "*Argh* You horse-cock-loving whore!"
    call ton_main("I have to say, Professor, now that I've told you.{w} I feel quite embarrassed about it!","angry","closed","worried","mid")

    call cum_block
    g4 "You dirty slut!"

    call ton_main("(I'd better not tell him what I had to do for their chieftain...)","angry","base","worried","L", hair="horny")
    call ton_main("(I can still taste him) {image=textheart} {image=textheart} {image=textheart}","horny","base","base","ahegao", hair="horny")

    call hide_characters
    hide screen bld1
    with d3

    call gen_chibi("came_on_desk")
    with d3
    pause.5

    call bld
    g4 "(Fuck me, that felt great!)"

    call ton_main("A remarkable wizard such as yourself would never even consider solutions of such...","open","base","base","mid")
    call ton_main("Depravity...","horny","base","base","R", hair="horny")
    m "Are you asking me whether or not I'd jerk of a Centaur?..."
    m "Because the would be a clear \"no\" from me..."

    call ton_main("Professor, I've never told anybody about my experiences as an Auror...","angry","base","worried","down")
    m "Are there more \"experiences\" you could tell me about?"
    call ton_main("Well...I have been an Auror for quite a while now, so...I do have a couple.","open","base","worried","R")
    g9 "Great! I'd love to hear them!"

    jump end_tonks_hangout
