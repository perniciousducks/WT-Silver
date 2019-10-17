

label start_slytherin_match:
    # Chat with Cho the day before.

    $ cho_busy = True
    $ cc_event_pause  += 1  # Event starts on the next day.
    $ cc_summon_pause += 1  # Can't be summoned until next event.

    $ lock_cho_training = True
    $ lock_cho_practice = True

    $ slytherin_match = "start"

    jump main_room



### Main Match ###

#Office before game
label slytherin_match:
    call play_music("stop")

    call play_sound("knocking")
    call bld
    "*Knock-knock-knock*"

    menu:
        m "(...)"
        "\"Who is this?\"":
            call bld
            ton "Tonks, Sir."
            m "First and last name, please."
            with hpunch
            ton "What?!"
            g9 "Tell me your first and last name, and you may enter."
            ton "Are you fucking with me right now?"
            g9 "No. But I'd love to."
            ton "Bloody hell..."
            ton "Nymphadora Tonks. Can I get in now?"
            m "Sure..."
        "\"Come on...\"":
            pass

    #Tonks enters
    call ton_walk(action="enter", xpos="desk", ypos="base", speed=2.5)

    call ton_main("Hi, [ton_genie_name].","base","base","base","mid", xpos="mid", ypos="base")
    m "Tonks... I was expecting someone else."
    ton "I was afraid you might've forgotten about todays-..."
    g9 "Quidditch match?"
    ton "So you didn't forget!"
    g9 "How could I, last match was a great show!"
    ton "It sure was..." #Horny
    ton "So, is Hermione going to show up or not?"
    m "Who knows with her honestly..."
    ton "So, do you want me to come with or?" #sad
    ton "I've been looking forward to watch the game from the commentator booth..."
    g9 "Of course! I'm sure both Snape and Miss Granger... if she shows up, would be delighted to have you!"
    ton "Hmm... How could I say no when you ask so nicely..."
    ton "Are we to expect another great performance this time around?"
    g9 "Oh, you'll see..."
    ton "Great, shall we?"
    g9 "After me!"
    #Genie barges past Tonks

    #Black screen footstep sound
    nar "You make your way down the grand staircase with Tonks, meeting Snape half way down."
    sna "Gen... Albus, sorry I'm late. I had some business to attend to."
    ton "Albus?"
    ton "I know who he is Snape, there's no need for the pretence."
    sna "Of course...{w} although I think it would be best to refer to him as sir or Dumbledore outside the headmaster's office."
    ton "Hmm, you have a good point..."
    m "I'm standing right here."
    sna "Right..."
    sna "I assume miss Tonks will be accompanying us?"
    ton "If that's okay with you?" #Flirty
    sna "I suppose..." #blushes
    ton "Great!"
    ton "Are we going?"
    sna "Ah, yes..."
    m "Hold...{w=0.3} hold on a moment!"
    m "Oh, no.{w=0.1}.{w=0.1}.{w=0.1} this isn't good..."
    sna "What's wrong?"
    m "I...{w=0.3} I'm dying!"
    sna "What!!" #big text
    sna "I thought genies were supposed to be immortal!"
    m "No Snape...{w=0.4} this is it for me..."
    sna "..."
    m "You've found it..."
    m "My only weakness..."
    ton "..."
    m "Awkwardness..."
    ton "*Giggles*"
    sna "Go splich yourself..."
    nar "You continue making your way down to the Quidditch pitch the silence only broken by Tonks giggling to herself ever so often..."

    #Hermione temp outfit set (Normal clothes)
    #Scene Cloudy/rainy pitch
    #Sounds slightly windy/rain (Might need a new sound we'll see... It shouldn't overpower things)

    #Quidditch pitch fills up a little
    #Low crowd sounds
    #Hermione enters from the left and walks up to the podium

    #Snape enters and stands at the back
    ton "Watch your head!"
    #Genie smacks his head again
    m "Blooming bleachers!"
    sna "..." #Smirks
    #Genie enters
    #Tonks enters
    ton "Oh, what a view! Now that's much better than from the Hufflepuff stands!"
    #Hermione turns around
    her "Oh, hello Tonks!"
    ton "Miss Granger, so glad you made it!"
    her "Of course, as you know I take my responsibilities seriously!"
    #Quidditch pitch fills up a little
    #Crowdsound goes up
    sna "Unfortunately..." #small text
    ton "I'm here if you need me!"
    her "I appreciate the thought but I'll be fine. I'd rather not give people another reason to make fun of me if you took over."
    ton "What ever you want sweetie." #smile
    her "..." #smiles and blushes
    #Quidditch pitch full
    sna "The crowd is waiting Miss Granger..."
    her "Sorry!"
    #Hermione turns

    $ renpy.sound.play("sounds/microphone_feedback.mp3")
    her "*Ahem*"
    #Crowdsounds go down
    her "Welcome back to the second match of the season!"
    sly1 "Not the Gryffindor slut again!"
    sly2 "Get off the podium Mudblood!"
    sly1 "Boooo!"
    her "Hmph!"
    #Hermione Turns to Tonks, Genie and Snape
    her "Sir, I'm trying to do my job here and those Slytherin boys just can't keep their filthy mouths shut!"
    sna "Surely you've been called worse Miss Granger..."
    ton "Just ignore them sweetie, you're doing great."
    her "..." #annoyed
    her "Fine..." #Open mouth glances to the right
    #Hermione turns to the crowd again
    her "I know the weather might not be optimal but the games must go on."
    her "Therefore, let me now welcome onto the pitch..."
    her "The team known for their tactical prowess and... lately... unconventional tactics..."
    her "Team Ravenclaw!"
    #Crowd Sounds
    her "And now let me welcome onto the pitch..."
    her "The team known for their..."
    her "their..."
    sly1 "Got a cock down your throat? Get on with it!"
    sly2 "Yeah! Get on with it!"
    her "..."
    with hpunch
    qcr "Get on with it!" # loud
    her "The team known for their thick skin or should I say, thick skulls..."
    her "Team Slytherin!"
    #cheers
    g9 "..."
    sna "..." #pissed off
    her "And now, if both teams has managed to find their way to their starting positions..."
    her "Madam Hooch, if you please!"

    nar "The grey haired lady glances up to the podium and gives Hermione a wink as she throws the quaffle into the air."

    #Whistle sound
    her "And we're off!"
    nar "Looking up you can see Cho giving a quick smirk towards Malfoy as she darts off towards the Slytherin half of the pitch."
    her "As we can see, one of the Ravenclaw chasers and team captain Roger Davies is immediately going for the quaffle..."
    her "The Slytherin Chaser and captain Graham Montague not far behind."
    her "Oh! Davies catches it and passes to Bradley-"
    ton "She's pretty cute when she's excited isn't she..."
    m "..."
    ton "I feel like we've got the best view in the house being behind the podium... Who cares about the match."
    m "You might enjoy it a bit more if you took a look towards the Slytherin's side of the pitch..."
    ton "Oh... I see, miss Chang has decided to forego the coat today..."
    ton "And those trousers seem to sit pretty tight on her..."
    m "I have done some research and know for a fact that those Slytherin boys are men of class and very much enjoys such a thing as well."
    sna "Feels a bit like cheating considering our bet... I would've imagined that you wouldn't use such tactics during the game against Slytherin..."
    m "(Oh shit, I forgot he was here... there goes that fucking bet.)"

    her "The Slytherin beaters Crabbe and Goyle are now yet again focusing their efforts on beating the bludgers as hard as they can towards the enemy chasers!"

    m "Well, if you remembered the bet correctly you'd know that we said nothing about any tampering on my part. It was only you who made such an agreement..."
    ton "Oooh, that's so naughty..."
    sna "Quite..."
    ton "Surely a Quidditch bet should be made on equal terms... where's the sportsmanship?"

    menu:
        "Agree and call the bet off":  # No options actually calls it off
            ton "That's the spirit, now lets just enjoy the... match shall we."
            sna "No, we're fine. I got some cards up my own sleeves.."
            #Keep the bet going, Snape should've listened properly
            sna "Hmph, I suppose a bet is a bet..."
            sna "I'm confident in my abi... our team's abilities though."
            ton "..." #Disappointed
        "Forfeit and give Snape the money":
            m "Fuck no, you think I'm some kind of charity..."
            sna "What?"
            #Back to other two options


    her "Crabbe just whacked the bludger straight towards Davis' broom-"
    her "Scratch that, he hit the quaffle in his hand!"
    her "That's crazy lucky"
    her "Where's the quaffle?{w} Pucey's got it! And he's already flown past the beaters!"
    g4 "..."
    her "But can he get through the keeper!"
    #Screen shake audience groans
    her "Another bludger hit by Crabbe going straight into the stomach of the Ravenclaw keeper!"
    her "Pucey passes the quaffle to Warrington who scores another goal for team Slytherin!"
    sna "..." #Smirks
    m "That's insane, how the hell did he hit that? He was on the other side of the pitch!"
    sna "That's my boys, thick as oatmeal but built like a brick shithouse."
    ton "They're so strong... I've never seen a bludger hit its target from that far before..." #horny
    ton "Is it me or is it getting a bit hot in here?"
    sna "Something to cool you down perhaps?"
    ton "Good idea, Did you bring any of that firewhisky Gen... Albus?"
    m "Err..."
    sna "Firewhisky? For such a special day as today I've brought some of my finest wine."
    sna "Now, if I may Miss Tonks?"
    ton "Hmm... I tend not to drink wine too often..."
    ton "Oh what the heck, go on then. I'll have a glass."
    #Blackscreen
    nar "You sit down with Snape and Tonks to enjoy the match - drinking some of the finest wine you've tasted, Tonks' cheeks turning redder as the game continues."
    #Fades back
    m "Doesn't look great..."
    ton "What are you on about... I've got a great view!"
    sna "He's talking about the game..."
    ton "Game? What game...{w=0.5} Oh yes, Quidditch! I almost forgot about that!"


    her "And we're now 60-0 to Slytherin as their onslaught continues, the seekers not yet having spotted the snitch."
    her "If it wasn't for those foul tactics from the brutes on the Slytherin team..."
    her "Ravenclaw would have no issues beating the ever living sh-{w=1.2}{nw}"

    #Hermione gets hit in the face by a bludger
    call play_sound("kick")
    with hpunch

    #Audience groans
    sna "*Pfffffffffff*-" # Snape has wine gushing out of his nose (image edit)
    sna "*Ha-ha-HA-HA!*{w=0.4}{nw}"

    call play_music("fun")
    stop weather fadeout 0.5
    show screen blkfade
    with d1

    centered "{size=+7}{color=#cbcbcb}-\{Intermission\}-{/color}{/size}\n\n"

    centered "{size=+7}{color=#cbcbcb}-\{Intermission\}-{/color}{/size}\n\n"

    centered "{size=+7}{color=#cbcbcb}-\{Intermission\}-{/color}{/size}\n\n"

    centered "{size=+7}{color=#cbcbcb}-\{Intermission\}-{/color}{/size}\n\n"

    call play_music("stop")
    pause.5

    call weather_sound
    call play_music("quidditch")
    hide screen blkfade
    with d3

    pause.8

    sna "I'm surprised she didn't swallow that one with how wide she was blabbing her mouth."
    sna "That's liquid luck for you!"
    ton "What?" #Shocked
    g4 "What the fuck is liquid luck?"
    ton "You gave those brutes a luck potion?!"
    sna "Well...{w=0.6}{nw}"
    ton "I can't believe you, Snape...{w=0.3} look what they've done to her face!"
    ton "Her beautiful face..." #Sad
    sna "Looks like an improvement to me."
    ton "Quiet!"
    g4 "..."
    ton "I'm taking her to the hospital wing..."
    g4 "What about the game..."
    ton "Leave it to me..."
    g4 "What?"
    #Whistle sound
    nar "Tonks Signals Hooch and a whistle is heard to signify a short break... a murmur erupts across the crowd, some not realizing what has gone down."
    #Tonks' and Hermione's chibi disappears down the staircase (Would hermiones crying chibi walking slowly work here)
    m "She sure sobered up quickly..."
    #Tonks crashes down the stairs sound effect
    ton "Bloody stairs!"
    m "Nevermind..."
    sna "This isn't good."
    m "You tell me, her face is fucked, and not in the fun way."
    sna "Not that, she'll be out of it for now but should be fine by the end of the day..."
    sna "Unfortunately..."
    #Black screen
    nar "A couple of minutes goes by and no signs of Tonks, the crowd now whispering even more, some beginning to spot the empty podium."
    #Fades back, crowd noises louder
    sna "You better get up there and do something."
    m "What do you want me to do? I already did a speech last time... I'm out of material."
    m "Also, doesn't this feel a bit like rehashing content?"
    #Snape starts walking slowly to the podium
    sna "Fine, in that case. I'll just go up and give a motivational..."
    #Genie walks past him and snape stops
    m "No, I got it..."
    #Genie at podium and Snape teleports back to his spot
    $ renpy.sound.play("sounds/microphone_feedback.mp3")
    m "Ladies and gentlemen..."
    m "An intermission if you will...{w} some motivation...{w} not to any of the teams in particular... "
    cho "..."

    menu:
        "\"Independence\"": #Independence day
            m "Good morning. In less than an hour, aircraft from here will join others from around the world. And you will be launching the largest aerial battle in this history of mankind."
            sna "Not again..."
            g9 "Mankind... that word should have new meaning for all of us today."
            #Crowd confusion
            m "We can't be consumed by our petty differences anymore."
            m "We will be united in our common interests."
            m "Perhaps its fate that today is the 4th of July, and you will once again be fighting for our freedom, not from tyranny, oppression, or persecution -- but from annihilation."
            m "We're fighting for our right to live, to exist."
            m "And should we win the day, the 4th of July will no longer be known as an American holiday, but as the day when the world declared in one voice."
            m "We will not go quietly into the night!"
            m "We will not vanish without a fight!"
            m "We're going to live on!"
            m "We're going to survive!"

        "\"Sunshine and rainbows\"": #Rocky
            $ renpy.sound.play("sounds/microphone_feedback.mp3")
            m "The world ain’t all sunshine and rainbows... It is a very mean and nasty place and it will beat you to your knees and keep you there permanently if you let it."
            mal "An inspirational speech in the middle of the game?"
            m "You, me, or nobody is gonna hit as hard as life."
            sna "Aint that true..."
            m "But it ain’t how hard you hit... it’s about how hard you can get hit, and keep moving forward."
            cra "Bullshit."
            m "How much you can take, and keep moving forward. That’s how winning is done."
            m "Now, if you know what you’re worth, then go out and get what you’re worth. But you gotta be willing to take the hit, and not pointing fingers saying you ain’t where you are because of him, or her, or anybody."
            m "Cowards do that and that ain’t you. You’re better than that!"
            #Crowd cheers
            m "Nailed it."

        "\"Don't care about the scoreboard\"": #Hoosiers
            m "There's a tradition in tournament play to not talk about the next step until you've climbed the one in front of you."
            m "I'm sure going to the State finals is beyond your wildest dreams, so let's just keep it right there."
            cho "(state finals?!?)"
            m "Forget about the crowds, the size of the school, their fancy uniforms, and remember what got you here."
            m "Focus on the fundamentals that we've gone over time and time again."
            m "And most important, don't get caught up thinking about winning or losing this game."
            m "If you put your effort and concentration into playing to your potential, to be the best that you can be, I don't care what the scoreboard says at the end of the game, in my book we're gonna be winners!"
            m "Okay?!!" #Large text
            $ renpy.sound.play("sounds/crowd_cheer2.mp3")
            m "Alright!!"
            m "Let's go!!"
            m "Let's go!!"
            m "Let me hear it!!!"
            #Applause


    her "I'm back!" #whispering #Blushing from this point forward
    sna "Miss Granger?"
    her "It's..."
    m "Get up there, the crowd has started to suspect something..."
    her "Oh...{w=0.2} of course!"
    #Hermione/Tonks walks up to the podium
    #Microphone static sound
    her "Ahem... oh, these boobs are so heavy..."
    #Crowd ???
    her "And why is this shirt so tight..."
    #Unbuttons shirt
    g4 "..."
    her "That's better."
    her "So, after that short... intermission and removing that... streaker of the pitch..."
    #Crowd !!!
    m "There was a streaker on the pitch? WHEN!?!"
    sna "She's deflecting the attention from the podium..."
    m "Oh, of course..."

    her "Now, back to your positions...{w} nice, I'm not used to being listened to this easily!"
    #Crowd exclamation
    sly1 "Oh, shut up slut... or I'll make you!"
    her "Looking forward to it!"
    #Crowd questionmark
    sly1 "..."
    m "What's wrong with her, did she get hit to hard?"
    her "Hooch, give that whistle a good blow for me will you?"
    #whistle
    sna "..."
    sna "Hmm... wouldn't be the first time a students personality changed from a bludger hit... "
    sna "I wouldn't be surprised if Madam Pomfrey's healing drafts weren't being distilled properly..."
    m "..."
    m "If you say so..."

    her "With those strong and muscular Slytherins in a firm lead we're now back in the game."
    her "Look at those bats swing, I wouldn't mind being hit by one of those if you know what I'm saying."
    her "And look at those Ravenclaws go, such finesse and style is a rare sight..."
    her "Miss Chang sure knows how to handle that broom between her thighs."
    cho "!!!"

    #Needs proofreading
    #Section where genie goes up and touches Hermione (tonks) under her skirt
    sna "You know... Tonks isn't here right now..."#Small text
    m "So?"#Small text
    sna "..." #Smirks
    m "Oh...{w=0.3} I see what you mean..."#Small text
    #Genie starts sneaking up behind Hermione (Tonks) Could this be synced to have him arrive when she yells whoa?
    her "Cute brunette passes to handsome blonde boy...{w=0.5}Whoa!"
    #Crowd ???
    g9 "..."
    her "No worries ladies and gentlemen, I just had a bit of a slip. It's very... wet up here..." #blushing
    m "(And it's about to get even wetter in a minute...)"
    nar "You begin touching Hermione, moving your hands up and down and gently massaging her butt and thighs."
    her "*Hmm* Those boys are going way to fast! I don't think I'll be able to keep it up if they went any faster."
    g9 "(Let's slow down a bit then shall we...)"
    nar "You continue touching Hermione and as you go on she's finding it more and more difficult to focus on the game."
    her "*Ahh*{w=03} Still...{w=03} Still no...*Ahh*{w=03} sign of the golden snitch..."
    m "(That's because I'm about to give that snitch a rub for good luck...)"
    her "*Mmmm* Those boys sure are doing well. I've never... *Hnngh* experienced such a...{w=0.3} such a...{w=0.3} thrill before!" #Thrill big text
    g9 "(Time to get some of my own liquid luck!)"
    nar "As you keep touching Hermione you move your hand further underneath her skirt and as you begin rubbing her vagina you can feel a bit of a wet spot on her panties."
    her "(Oh! That's naughty!{w=0.3} *Ahh*...{w=0.3} One of the Slytherin beaters just smashed their elbows into an opposing player...)"
    nar "You begin rubbing her faster, moving your middle finger back and forwards across her clitoris."
    her "And we all know...{w=0.3} *Ahh*{w=0.3} No excessive use of elbows...{w=0.3} *Ahh*{w=0.3} Permitted..."
    her "But it seems to have done the trick!"
    her "The Slytherin chasers are... {w=0.3}*Ahh*...{w=0.3} Edging ever so closer to the goal posts!"
    nar "As the quaffle is thrown towards one of the hoops you give Hermione one last rub across her panties bringing her over the edge."
    #Crowd cheer
    her "Cumming!!!" #Big text, Considering if she should yell Gooooaaal! instead
    nar "Hermione's legs tremble as her knees buckles, the words of her orgasm drowned out by the cheers of the crowd."
    nar "She glances up at you, cheeks flushed and legs still shaking slightly."
    her "*Ahh*...{w=0.3}*Ahh*...{w=0.3}Sir...{w=0.2} that was..."
    #Genie walks back to his seat
    nar "Before she finishes her sentence you give Hermione a quick smirk and swiftly head back to your seat..."
    g9 "It's not just the Slytherin players that are quick to score this game."#Small text
    sna "..." #Smirks
    sna "Seems like Miss Granger wont be forgetting this match anytime soon..."#Small text
    nar "You look back up at Hermione who's still trying to compose herself and get back to commentating."
    sna "You can wipe that smile of your face now..."
    sna "Gryffindor has no chance, We've got this game in the bag."


    sna "Whatever your plan is I doubt you'll succeed..." #smirk
    sna "Another couple of goals and you wont win even if Miss Chang manages to catch the snitch."
    g9 "You say that..."
    nar "Cho now with her eyes fixed behind one of the goalposts seemingly having spotted the snitch gives you a quick glance and a smile as she flies up to Crabbe and Goyle."

    #Cuts to Cho flying
    # TODO: add ass shot (CG)
    cho "Hey boys, check this out..."
    cra "What do you want slu..."
    nar "Cho spins around, flaunts her butt and gives them a quick wink."
    goy "..."
    goy "Looks like this little Ravenclaw girl has finally come to her senses Crabbe."
    cra "Why wouldn't she Goyle... Those Ravenclaw boys has nothing even close to our sheer strength!"
    nar "Cho tightens her butt cheeks and flutters her eyelashes in a way that to anyone except Crabbe and Goyle would be an obvious distraction tactic."

    her "And there's a goal for Ravenclaw ladies and gentlemen, look at those cuties go... those clothes must be completely stuck to their skin in this weather!"

    nar "Malfoy suddenly turns around with a surprised look on his face that a goal was let in and then angrily flies up to Crabbe and Goyle."
    malf "What the hell are you guys doing, have those bludgers been hitting you too hard? You're supposed to be blocking the goal until that Ravenclaw girl spots the snitch!"
    cra "Well, about that..."
    malf "How dare you speak over me, I'm not done with you!"
    cra "But Dra...{w=0.6}{nw}"
    malf "What?!?"
    cra "She's going after the Snitch!"

    nar "Malfoy spins his head around, finally noticing that Cho's currently chasing the snitch in the distance he quickly darts after her."
    malf "You Fucking idiots!"

    her "Oh... it looks like things are heating up as Malfoy has finally realised Chang is going for the Snitch..."
    her "Look at that girl fly, I didn't think you could grip a broom so tightly... maybe I could learn a thing or two from her."
    sna "I see we've been playing different games..."
    g9 "Quite..."
    her "Chang, now only inches away can almost taste that ball..."
    her "Malfoy on his superior broom edging ever so much closer..."
    sna "Well, congratulations... You've got me beat, sure as hell is a better view than last season..."
    her "And she's caught it! Ravenclaw wins and makes it to the finals against Gryffindor!"
    sna "I was looking forward to seeing that cup in my office again this year... Oh well..."
    her "And what a well deserved victory as well!"
    m "You put the cup in your office?"
    #Fades to black
    #Fades back to empty stadium
    sna "Well, that was good... and to my dismay the commentary was... acceptable."
    m "What?!"
    m "I thought that you didn't like miss Granger..."
    m "Where's that Slytherin pride you're so adamant about?"
    sna "*HMPH*... I'm sure you can find your own way back to your office..."
    sna "Here's your winnings..."
    #Fucking money, bitches
    sna "I sure know when I've been beaten."
    #Blackfade
    nar "You make your way back to your office... wondering how the real old man could stand all these stairs, no wonder he always stayed in there."

    call blkfade

    jump night_start



label slytherin_match_return:
    #Office screen, evening after game
    m "(That went well... Money,{w=0.8} Ass...{w=0.5} and a good sho-...){w=0.8}{nw}"

    #Tonks as Hermione walks in
    m "(Oh, shit...)"
    her "That was...{w=0.5} amazing!"
    g4 "What?"
    her "I've never experienced such a thrill before..."
    her "Trying to keep it together when everyone was watching the game..."
    g4 "Err..."
    g9 "Glad you enjoyed it!"
    her "*Hmm* - I think someone deserves a bit of a reward..." #Horny
    g4 "What do you-...{w=0.8}{nw}"
    #Hermione takes her top off
    m "Miss Granger?"
    her "Be quiet you, just enjoy it!"
    #Hermione takes her bottoms off
    her "*Hmm* - You like the looks of these cute panties?"
    #Giggle sound effect
    her "*Hi-Hi-Hi*"
    g4 "..."
    her "Or these little puppies..."
    #Hermione takes her bra off
    nar "Hermione glances at her breasts and removes her bra whilst shaking her breasts at you lustfully."
    her "Much better without the bra don't you think?"
    m "I..."
    her "You like looking at this body, don't you?"
    her "Tell me!"
    g4 "I do!"
    her "I knew you did, I could feel your eyes in the back of my neck when I was up there..."
    m "Who wouldn't with a body like that..."
    her "Damn right...*Mmmm*"
    her "And since you love this butt so much..."
    nar "Hermione bends over and takes her panties off, throwing them to the side."
    her "..."
    her "What do you think?"
    m "Looking grea-{w=0.6}{nw}"

    #Cho walks in
    cho "I did it! We won the...{w=0.8}{nw}"
    #Hermione turns to Cho
    cho "!!!" #Shocked face
    her "Oh, hello there Miss Chang..."
    her "Like what you see?"
    cho "I..."
    #Giggle sound effect
    her "*Hi-Hi-Hi*"
    her "What's wrong sweetie?"
    her "Want to find out if Gryffindors tastes the same as Ravenclaws?"
    cho "..." #Blushes
    cho "*HMPH!"
    #Cho walks out and slams the door
    her "Meh...{w=0.4} Suit yourself..." #Shruggs it off and turns back to genie
    m "What the hell are you doing Granger?"
    her "Granger?" #confused
    her "What are you talking about genie?"
    #Tonks turns back into herself (clothed)
    g4 "Whoa!"

    if tonks_morph_known:
        m "It all makes sense now."
        ton "Hello sweet cheeks!"
        ton "Thought I was about to lose focus there for a second when you started going at it!"
        m "You should’ve told me it was you..."
        ton "I tried to!"
        ton "You pretty much pushed me onto the podium when I got back..."
        m "Oh, yeah..."

    else:
        $ tonks_morph_known = True
        g4 "You were Miss Granger the whole time?"
        m "Plot twist of the fucking century."
        ton "Of course not, don't be silly..."
        ton "I'm a metamorphmagi..."
        m "A meta what?"
        m "(I thought I was the only one allowed to be meta in this game...)"

    ton "It means I can look like whatever I want."
    m "Really?"
    ton "Of course!"
    #Tonks turns into cho
    cho "Hi professor, want to give this snatch a little lick?"
    #Tonks turns into Astoria if you've met her
    ast "How about giving this little butt a spanking?"
    #Tonks Turns into Susan if you've met her
    sus "You want to s...spank me? W-Why would you want to s... spank me professor? Did I do something wrong?"
    #Tonks turns into Luna if you've met her
    lun "Oh, Tonks look out you got a jigglypuff on your shoulder, let me lick it off for you!"
    lun "*Hi-Hi-Hi*"
    #Tonks turn into snape (Wearing the weird hat and handbag?)
    sna "Want some of this Genie? Mind if I...{w=0.4} Slithered in?"
    g4 "..."
    sna "*Hi-Hi-Hi*"
    #Tonks turns into herself
    ton "I'm especially proud of that last one..."
    m "..."
    m "So...{w=0.2} Can all wizards do this?"
    ton "Nah, I was born with it."
    m "This world, I swear there's something new every day..."
    m "What next?{w=0.2} Can you time travel?"
    ton "I Wish! The ministry wont let me do it..."
    ton "If I could I'd just go back to kill baby \"you know who\"..."
    m "(That is always the first thing people consider when talking about time travel...)"
    m "Unbelievable..."

    m "So...when Miss Granger got hit by that bludger..."
    ton "I took her to the Hospital wing..."
    ton "And I replaced her so she wont get bullied."
    m "I see..."
    m "And she..."
    ton "Her face is fine... *Hmmm* - Your face is so cute when you worry, you know..."
    m "So, won't people find out you replaced her?"
    ton "You think so?"
    ton "I can lie if I want! Who will they believe?"
    g4 "..."
    ton "Anyway..."
    ton "Unless she has a really good reason to I doubt she'll tell anyone."
    ton "*Urgh* My head hurts I'm gonna go sleep off whatever this is..."
    ton "Toodeloo!"
    #Tonks leaves
    #End

    $ tonks_busy = True
    $ snape_busy = True
    $ hermione_busy = True
    $ cho_busy = True

    #$ cho_tier = 3 # TODO: activate this after adding favors.

    jump main_room
