#Public tentacle scene
label tentacle_scene_intro:
    with d3 # Transition from inventory
    show screen bld1
    m "(Okay... so...{w=0.3} What was this scroll supposed to do again?)"
    m "(Ah, that's it... it's supposed to turn me into some sort of magical tentacle plant...)"
    m "(Let's see...)"
    if not tentacle_sample:
        m "(I'm still missing the plant sample.)"
        m "(Well... I have the key so I guess I need to find where that highest point is...)"

        label .riddle:
        m "\"At the highest point is where I'm hidden-\""
        m "\"A place where you will need this key-\""
        m "\"To use this scroll that is forbidden-\""
        m "\"You'll need to take a piece of me...\""

        menu:
            m "..."
            "-Continue-":
                pass
            "-Repeat the riddle-":
                jump tentacle_scene_intro.riddle

        m "(The highest point, huh... I wonder where that could be.)"
        jump main_room_menu
    else:
        m "(I have everything I need to perform the ritual.)"
        if not daytime:
            m "(It's too late for me to use it now, I better try again at dusk.)"
            jump main_room_menu
        elif hermione_busy:
            m "(Though Hermione is busy at the moment, I should postpone using the scroll until tomorrow.)"
            jump main_room_menu

    m "(I better write miss Granger a note first so she can carry me with her to class...)"
    call gen_chibi("paperwork")
    with d3
    pause 1.0

    # Setup
    $ hermione_busy = True
    $ d_flag_01 = []
    $ d_flag_02 = False

    menu:
        m "(Hmm... how should I start?)"
        "Dear Hermione, ...":
            $ d_flag_01.append("Dear Hermione,\n\n")
        "Dear [hermione_name], ...":
            $ d_flag_01.append("Dear [hermione_name],\n\n")
        "You, the bimbo, ...":
            $ d_flag_01.append("You, the bimbo,\n\n")

    "*Scribble* *Scribble*"

    menu:
        m "....mhmm...."
        "...I had very important business matter to attend to...":
            $ d_flag_01.append("I had very important business matter to attend to,")
        "...I went out to visit a brothel...":
            $ d_flag_01.append("I went out to visit a brothel,")
        "...I have turned myself into a plant...":
            $ d_flag_01.append("I have turned myself into a plant,")
            $ d_flag_02 = True

    "*Scribble* *Scribble*"

    menu:
        m "..."
        "...I ask you kindly...":
            $ d_flag_01.append("I ask you kindly,")
        "...Just listen for once...":
            $ d_flag_01.append("just listen for once and")

    "*Scribble* *Scribble*"

    menu:
        m "...and now..."
        "...take this plant with you to your class..." if not d_flag_02:
            $ d_flag_01.append("take this plant with you to your class.\n\n")
        "...take this plant then shove it up your ass..." if not d_flag_02:
            $ d_flag_01.append("take this plant then {b}{s}shove it up yo{/s}{/b} bring it to class.\n\n")
            g9 "Shove it up yo-..."
            call gen_chibi("sit_behind_desk")
            with d3
            g4 "I can't write that!"
            m "What if she does listen and I get shat on... No, no, no, let me change that."
            call gen_chibi("paperwork")
            with d3
        "...take me to class..." if d_flag_02:
            $ d_flag_01.append("take me to class.\n\n")

        "...shove me up your ass..." if d_flag_02:
            $ d_flag_01.append("{b}{s}shove me up yo{/s}{/b} take me to class.\n\n")
            g9 "Shove me up yo-..."
            call gen_chibi("sit_behind_desk")
            with d3
            g4 "I can't write that!"
            m "What if she does listen and I get shat on... No, no, no, let me change that."
            call gen_chibi("paperwork")
            with d3

    "*Scribble* *Scribble*"

    menu:
        m "..."
        "...Sincerely, Dombledure.":
            $ d_flag_01.append("Sincerely,\nDombledure.")
        "...Yours truly, [genie_name].":
            $ d_flag_01.append("Yours trully,\n[genie_name].")

    $ d_flag_01 = " ".join(d_flag_01)

    call gen_chibi("sit_behind_desk")
    with d3
    pause 1.0
    m "Yes...{w=0.5} that should do it... now to call her up here and use that scroll..."
    stop music fadeout 3.0
    show screen blkfade
    with d5
    centered "{size=+7}{color=#cbcbcb}Few moments later...{/color}{/size}"
    call gen_chibi("hide")
    show screen desk
    show screen chair_left
    show screen letter_on_desk
    show screen plant_on_desk
    hide screen blkfade
    with d5

    pause 3.0
    call her_walk(action="enter")
    with d3
    pause 1
    call her_main("[genie_name], my class is about to-", "open", "base", "worried", "L", trans=d3)
    call her_main("[genie_name]?", "open", "squint", "base", "L")
    call her_walk(xpos="mid", ypos="base")
    pause 1.0
    call chibi_emote("thought","hermione")
    pause 2.0
    call chibi_emote("hide", "hermione")
    call her_main("Are we playing hide and seek??", "annoyed", "base", "angry", "R", trans=d3)
    call her_main("[genie_name], I really don't have the-", "annoyed", "narrow", "angry", "stare")
    hide screen hermione_main
    hide screen bld1
    with d3
    pause 1.0
    call chibi_emote("exclaim","hermione")
    pause 1.0
    call chibi_emote("hide", "hermione")
    her "..."
    call her_walk(xpos="desk", ypos="base")
    m "(Yes... she's seen me...)"
    m "(Take the note!)"
    call her_main("What's with this ugly plant...", "disgust", "narrow", "angry", "stare", trans=d3)
    with vpunch
    g4 "(I'm not ugly!)"
    m "(...Just haven't blossomed yet...)"
    pause 1.0
    call her_chibi("stand", flip=True)
    with d3
    call her_main("Professo-......?", "open", "base", "worried", "L", flip=True, trans=d3)
    call her_main("I thought I heard him for a second...", "annoyed", "narrow", "worried", "R")
    m "(Read the note already, would you..)"
    pause 1.0
    call her_chibi("stand", flip=False)
    with d3
    call her_main("Oh, there's also a note, I better read it...", "open", "base", "base", "down", flip=False, trans=d3)

    m "(Can't help herself but snoop in other peoples business can she...)"
    hide screen letter_on_desk
    with d3
    $ renpy.play("sounds/pageflip.mp3")
    call her_main("Oh... It's actually addressed to me...", "soft", "base", "base", "stare")

    # Read letter from Genie
    $ letter = Letter(text=d_flag_01)

    $ menu_x = 0.5
    $ menu_y = 0.9

    show screen letter
    hide screen hermione_main
    with d5

    menu:
        "-Done reading-":
            pass

    call reset_menu_position

    hide screen letter
    call her_main("....................................", "disgust", "narrow", "angry", "mid", trans=d3)
    call her_main("So I'm a delivery girl as well now?", "annoyed", "narrow", "angry", "stare")
    call her_main("Well.. I suppose I'm already headed that way...", "annoyed", "closed", "angry", "stare")
    call her_main("Guess he must've checked my schedule for once...", "annoyed", "narrow", "worried", "R")
    g9 "(Herbology class, here I come!)"

    hide screen hermione_main
    hide screen plant_on_desk
    call her_chibi("hide")
    show screen blkfade
    with d9

    pause 1.5
    call play_sound("door")
    pause 1
    centered "{size=+7}{color=#cbcbcb}Herbology{/color}{/size}"
    pause 1

    call play_music("agenda")
    play bg_sounds "sounds/murmur.mp3" fadein 2 fadeout 2

    spo "In today's class, we will be learning about a plant called Devil's Snare."
    spo "Hermione Granger was kind enough to bring us a pot with an underdeveloped Devil's Snare."
    spo "It's kind of witty and looks weak but..."
    g4 "(Oh fuck you, bitch!)"
    her "Actually, professor that wa-..."
    spo "Miss Granger, please don't interrupt me."
    her "Sorry..."
    spo "Now then..."
    spo "This is an incredibly dangerous plant, known to constrict and kill its prey with its fast and powerful tendrils."
    spo "They are found naturally in caves and swamps as they like dark and damp places and hate sunlight."
    her "Isn't Devil's Snare extremely dangerous?"
    spo "Thank you for stating the obvious, Miss Granger, now please, sit down."
    # TODO: sound class laughs
    her "..........."
    spo "They're barely one week old, they would barely be able to stroke you with their tendrils, let alone constrict you."
    spo "Now everyone, pass the samples around so that you all can get a good look."
    her "Professor Sprout, are they supposed to have mouths?"
    spo "Yes Miss Granger, it's how they eat their prey once they have asphyxiated them."
    her "Okay, well what are the eyes for? I thought they sensed their prey by touch?"
    spo "What are you talking about, Devil's Snare don't have eyes."
    her "This one do-..."
    # TODO: sound crowd gasps
    # TODO: sound grab (?)
    with vpunch
    ">All of a sudden, you explode outwards in a flash of thick green tentacles"
    her "What's happening?!?"
    ">You quickly bind her wrists and stomach..."
    her "I can't move!"
    ">then lift her into the air with your powerful appendages."
    spo "Stay calm Miss Granger, Devil's Snare will let you go if you don't move!"
    ">Slinking your slimy tentacles under her top and skirt."
    if not hermione.is_worn("panties"):
        mal "Hey, look, look! She doesn't have panties on!"
        fem "That's, like, sooo insulting, y'know."
        mal2 "And she brought her own plant sample, I bet she planned this out, what a total slut!"
    her "Oh no..."
    # TODO: sound cloth rip
    ">You rip her top of in a flurry of buttons and cotton."
    her "Ahhhh"
    # TODO: sound Old squeeky door sound being opened. (No, don't add that XD)
    ">Sliding your tentacles up her legs and slowly pull them apart"
    ">Hermione struggles against you but her effort is in vain."
    her "Please no... Not here."
    if hermione.is_worn("panties"):
        ">The tentacles slowly pull up her panties, revealing her to the class"
    mal "Wow..."
    fem "This is horrible, someone should do something"
    mal2 "Professor Sprout says as long as she doesn't move she'll be released."
    ">You position a large, flowered tentacle above Hermione's head"
    her "What is that?"
    ">It suddenly opens to reveal a long slender appendage with an engorged base"
    her "What the hell is that? It looks like a..."
    ">While she is focused on the dangling limb above her you move six smaller tentacles towards her waist"
    her "Oh god no, someone please help me! Professor Sprout do something!"
    spo "Ok students, stand back!"
    ">Professor Sprout casts an impressive-looking spell at the mass of writhing tentacles"
    # TODO: sound Spell
    spo "Confringo!"
    ">It strikes the plant forcefully but does nothing."
    spo "What? That should have killed it. It must be magically protected."
    ">You move three tentacles to her vagina and start teasing the opening."
    her "Please Professor Sprout, do something! Anything!"
    spo "I'm not sure I can, it has a powerful magical spell protecting it"
    spo "If I try anything more powerful than the spell I just cast I might hurt you."
    ">You move two smaller tentacles to her asshole and start teasing the entrance, slowly prying it open"
    her "Well then what am I supposed to do?"
    spo "Just stay as still as possible and it should eventually let you go..."
    ">You move a tentacle with a mouth on the end of it to her right breast and latch onto it."
    her "Please, I'm not going to be able to stay still if this keeps going"
    ">The three tentacles at the entrance of her vagina suddenly thrust into her"

    # TODO: sound RIGHT INTO HER VAGENE

    if her_reputation > 15:
        call tentacle_1
    else:
        call tentacle_2

    stop bg_sounds fadeout 3.0

    "> After everyone leaves the room your body starts to turn back to normal..."
    gen "That was hot!"
    "> You notice that something is amiss..."
    gen "What happened to my clothes?!"
    gen "...I was expecting this other-wordly magic to cover the basics of transmutations at the very least."
    gen "Guess I was wrong..."
    gen "I must get out of here before anyone spots me."

    call play_sound("running")

    "> You dash through the castle in a flash and get back to your office to grab a new pair of pants."

    hide screen blkfade
    with d5

    jump main_room

label tentacle_1: #Public path
    call cg_scene(folder="", layer="p1")
    hide screen blkfade
    with d9
    call ctc

    her "!!!"
    her "What on earth is going on?"
    ">You start pumping the tentacles in her vagina slowly"
    call cg_scene("p2")
    her "Oh..."
    ">You move a small tentacle with a mouth on the end to her ear so that only she can hear you."
    gen "Enjoying yourself slut?"
    her "Professor!"
    gen "Shhh... Just relax dear. I'll let you go eventually."
    gen "Thaaaat's right, do as your [genie_name] says, just relax."
    her "How am I supposed to relax?!"
    gen "Well if you're not going to relax, at least try to enjoy it..."
    ">You start rotating the tentacles in her vagina."
    # TODO: masturbating sound?
    call cg_scene("p3")
    her "..."
    spo "If you keep thrashing about so much it won't let you go, stay still girl!"
    her "I-I'm trying!"
    gen "Are you sure you're trying enough? Judging by how much you're moving I'd say that's quite the opposite."
    gen "Someone might even think that you are enjoying this."
    her "They wouldn't..."
    mal "Who's she talking to?"
    mal2 "I've got no idea, bitches be crazy man."
    gen "Are you sure? Do you think you'll be able to stifle every moan?"
    # TODO: masturbating sound?
    ">You push deeply into her with the 3 tentacles."
    her "!!!"
    call cg_scene("p4")
    gen "Do you think you'll be able to stop your hips from bucking?"
    ">You give her another powerful thrust."
    her "{size=-6}{heart}*ah*{/size}"
    gen "Do you really think that you'll be able to stop yourself from begging me for more?"
    ">You increase the speed of the tentacles"
    her "{size=-3}mmmmmmm{/size}"
    gen "I don't think you will. In fact I know that you won't."
    gen "Because I know what you are. A slut."
    gen "A slut who can only think about getting off when she's being fucked by a monster in front of her classmates."
    ">You stop moving the tentacles."
    gen "Now tell them what you are."
    her "W-w-what? No please, just don't stop."
    gen "Tell them what you are and I'll keep going."
    her "I can't... Just keep going..."
    gen "Say it."
    her "{size=-3}I'm a slut.{/size}"
    ">You start rotating the tentacles in her vagina ever so slowly."
    gen "What was that? I don't think that they heard you. Why don't you say it once more, with feeling."
    her "I'm a slut!"
    ">You begin fiercely fucking her vagina."
    her "Yes, yes, I'm a fucking slut. Fuck me harder."
    gen "See that wasn't so hard now was it. How about I give you a little reward."
    her "Wha-"
    call cg_scene("p5")
    ">You thrust a ribbed tentacle deeply into her asshole in one motion."
    her "!!!"
    her "It's in my ass... I-I'm cumming."
    ">You take alternating turns pumping into her ass and pussy."
    her "I'm cumming! It's too much..."
    call cg_scene("p6")
    ">You feel her body shudder as the orgasm rocks her."
    ">This only spurs you on to fuck her harder."
    her "Please... no more... I'll faint..."
    ">You start to feel a strange energy flowing through the vines, moving towards the tips."
    gen "This is it girl, get ready."
    her "...ready?..."
    call cg_scene("p7")
    ">With one final surge you release the pent up energy in a surge of white sap all over her."
    gen "Oh gods, it's like each vine is cumming. This is amazing..."
    ">The sensations proved to much for hermione and she faints, going limp in your tentacles."
    mal "What a slut..."
    fem "I told you so."
    mal2 "Man, I'm going to have to join Gryffindor."
    ">You place Hermione back onto the desk as the plant that you are occupying slowly wilts and dies."
    ">Professor Sprout quickly runs over."
    spo "Miss Granger are you okay?"
    her "..."
    spo "Quickly, someone take her to the hospital."
    mal "Should we cover her up?"

    # This is the public route, don't change writing please!

    if hermione.is_worn("panties"):
        spo "Oh yes, I suppose you should."
        mal "{size=-4}Damn dude, have you seen her tits?!{/size}"
        ">*Squeeze* *Squeeze*"
        mal2 "{size=-4}Holy shit, they're soft."
        spo "If you two don't stop that at once you'll get expelled."
        mal "S-sorry..."
        mal2 "Yes, sorry."
        spo "Just take her out."
    else:
        spo "No need, if she feels comfortable parading without panties in MY class, then she should be fine being taken naked to the infirmary."
        mal "Are you su-..."
        spo "I said take her out!"
        mal "Y-yes ma'am..."

    call play_sound("walking")

    ">You can hear the boys snickering to each other while they carry hermione out in some unknown direction..."
    ">...Probably to have some fun with her while she's still unconcious..."

    spo "Class dismissed!"

    hide screen cg
    show screen blkfade
    with d9
    pause.8

    return

label tentacle_2: # Personal path
    call cg_scene(folder="", layer="p1")
    hide screen blkfade
    with d9
    call ctc

    her "What kind of sick plant is this?!"
    ">You start pumping the tentacles in her vagina slowly..."
    her "Oh..."
    ">You move a small tentacle with a mouth on the end to her ear so that only she can hear you."
    gen "Enjoying yourself, [hermione_name]?"
    her "Profes-"

    call cg_scene("e2")
    call ctc

    ">You quickly force another flowered tentacle into her mouth."
    gen "Now, now [hermione_name], you don't want anyone to find out how much you actually are enjoying yourself now, do you?"
    her "*Hmmmhhhhhhhhh* !"
    gen "Well, then just do what Miss Sprout says and stay still."
    gen "Just act like this is some horrible accident, that you are just a victim."
    gen "Instead of the slut that you really are..."
    ">You start to rotate the tentacles in her vagina."
    gen "!!! *HMMMMM*"
    mal "Wow, I think she's starting to enjoy it."
    fem "Hermione? No way, she's too stuck-up to let boys kiss her, not to mention enjoying sex. {size=-6}With a plant but still..{/size}"
    mal2 "I don't know man, she doesn't look like she hates it."
    ">You increase the speed of the tentacles in her vagina."
    gen "Hear that, [hermione_name]? Your classmates are starting to realize how much you like your slutty pussy getting stuffed."
    her "*NNNNNNNNNm*"
    gen "What was that? Faster you say?"
    gen "You got it, [hermione_name]!"
    call cg_scene("e3")
    ">You begin fucking Hermione in earnest."
    her "*HMMMMMMm...!!!*"
    ">The sensation of fucking Hermione in two different holes is almost overwhelming."
    gen "I know you are loving every second of this..."
    gen "...Being fucked in front of your classmates."
    gen "Having your tits and pussy on display..."
    ">You move a ridged tentacle towards her ass."
    her "*mm eehh oorr mmmnooo*!"
    # TODO: Sound enter her bottocks :DDD
    call cg_scene("e4")
    ">You enter her tight ass. The feeling of being in every hole at once is incredible."
    her "*mmmmmmmm*"
    ">Hermione barely manages a groan. She is being overwhelmed by the shear amount of pleasure she is currently bombarded with."
    gen "Admit it! You're loving this aren't you."
    gen "Being forced to take dick in front of you classmates like the whore you are."
    gen "Go on say it! Tell me what you are!"
    her "*hmmm aaaaa hhhhhhuuuttt*"
    gen "What was that, I couldn't quite make it out over the sound of you sucking dick."
    her "*hmmm aaaaa hhhhhhuuuttt*!"
    gen "One last time. Say it like you mean it."
    call cg_scene("e5")
    ">As she goes to exhale you quickly remove the tentacle from her mouth."
    her "{size=+5}I'm a slut!{/size}"
    ">The realisation of what has just occurred hits her like a ton of bricks."
    her "I-I'm cumming... Profes-"
    call cg_scene("e6")
    ">You quickly reinsert the tentacle into her mouth, silencing her."
    gen "Good girl. Time for your reward."
    ">You quicken the pace as she convulses beneath you."
    call cg_scene("e7")
    ">You explode inside of her from every tentacle-like heads, filling her up to the brim."
    mal "Told you she was a slut."
    fem "I guess you were right..."
    ">Professor Sprout quickly runs over."
    spo "Miss Granger are you okay? Miss granger!"
    her "..................*ah*"
    spo "....She's breathing, thank be Merlin."
    hide screen cg
    show screen blkfade
    with d9
    pause.8
    spo "You! Yes, you girls! Take her to the hospital wing at once!"
    fem "W-wha-.. But..."
    spo "What are you waiting for!"
    fem "Fine... {size=-4}"

    call play_sound("running")
    pause 3.0

    spo "Class dismissed!"

    return

###COSTUME SCENES
label costume_scene_1: #Maid role-play
    call her_main("A costume? What on earth do you need me to dress up for?", "angry", "wide", "base", "stare")
    m "[hermione_name], have you ever heard of the term role-play?"
    call her_main("role-play?", "smile", "narrow", "base", "mid_soft")
    m "It's where you pretend to be someone you're not."
    call her_main("I gathered that much but why would I want to do that?", "smile", "narrow", "base", "mid_soft")
    m "Because it can be fun!"
    call her_main("Hmmmm. Who would I be role-playing?", "smile", "narrow", "base", "mid_soft")
    m "Well I was thinking seeing as how I purchased you that lovely new cleaning outfit."
    m "You could play the role of my personal maid."
    if her_whoring < 17:
        call her_main("And how much would this \"personal maid\" be paid?", "smile", "narrow", "base", "mid_soft")
        m "Thirty-five points sounds fair."
    call her_main("...", "smile", "narrow", "base", "mid_soft")
    call her_main("Let me go change.", "smile", "narrow", "base", "mid_soft")
    $ hermione.equip(her_outfit_maid)
    call her_main("", "smile", "narrow", "base", "mid_soft")
    call ctc

    call her_main("Well?", "smile", "narrow", "base", "mid_soft")
    m "You certainly look the part. The question is can you act the part?"
    call her_main("Act? I thought you just wanted me to clean your room?", "smile", "narrow", "base", "mid_soft")
    m "Where's the fun in that? If I wanted a clean room, I'd just get those ugly dwarves to do it."
    call her_main("House-elves.", "smile", "narrow", "base", "mid_soft")
    m "Whatever. Anyway I want you to act like a sexy french maid."
    her "Why does it have to be french?"
    m "Must I explain everything?"
    call her_main("Fine...", "smile", "narrow", "base", "mid_soft")
    call her_main("Is there anything you need cleaned today sir?", "smile", "narrow", "base", "mid_soft")
    m "At least try to do the accent."
    call her_main("...", "smile", "narrow", "base", "mid_soft")
    call her_main("Is there anything that you need cleaned today Monsieur?", "mad", "base", "angry", "mid",cheeks="blush")
    m "Much better."
    call her_main("Thank you Monsieur.", "smile", "narrow", "base", "mid_soft")
    m "Now as for your cleaning I think that the fireplace could you a good dusting."
    call her_main("As you command Monsieur!", "smile", "narrow", "base", "mid_soft")
    ">Hermione stands on her toes to reach the mantelpiece giving you a lovely view of the top of her stockings."
    m "That's it, just a little higher."
    ">You reach under the desk and start to stroke your cock."
    her "..."
    her "Ooh-la-la, You wouldn't happen to be doing anything naughty under that table would you now Monsieur?"
    m "Of course not mademoiselle, just an itch, now back to cleaning."
    her "Yes yes."
    ">She resumes dusting the mantelpiece, reaching even higher this time."
    ">You can now almost make out the start of her bottom."
    her "Oh my! When was the last time this was cleaned?"
    m "I couldn't say..."
    her "It's so dirty! I will have to put all my effort into this."
    ">She starts making small hops with each dust to reach the top of the books."
    m "That's it. I think you might have missed a spot near the bottom however."
    her "Did I? How about this."
    ">She bends over in front of you, giving you a clear view up her skirt."
    m "That's it."
    ">You erupt underneath your desk, shooting spunk up and over it and onto the floor."
    her "Monsieur! You are so naughty!"
    her "Making a mess as I am cleaning up this filthy filthy room."
    her "At this rate I'll never be done!"
    m "Well you're cleaning was responsible for this mess."
    her "Hmmm, I suppose you are right as always Monsieur, I better start cleaning."
    ">Hermione drops to her knees and starts wiping up your cum."
    her "Such a big mess!"
    ">Hermione cleans up your cum from the floor and table."
    her "Well how did I do?"
    m "Very well indeed! You've taken to role-play like a duck to water."
    m "Forty points to Gryffindor."
    her "Thank you [genie_name]."

    return