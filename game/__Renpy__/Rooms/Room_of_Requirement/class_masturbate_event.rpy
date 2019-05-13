

label class_masturbation_event: #LV.8 (Whoring = 21 - 23)
    call room("main_room")
    show screen blkfade
    with d3

    call reset_menu_position

    $ gen_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ gen_chibi_ypos = 10
    $ g_c_u_pic = "sex_slow_ani"

    nar "This event is written by WaxerRed."


    menu:
        "Path 1":
            $ pathvalue = 0
        "Path 2":
            $ pathvalue = 1
        "Path 3":
            $ pathvalue = 2
        "Path 4":
            $ pathvalue = 3

    call hide_blkfade

    #First Level
    if pathvalue == 0:
        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call bld
        m "[hermione_name] There is another task I have in mind for you."
        call her_main("I assume this is a new way to humiliate myself in front of you. Or will it be in front of my peers this time?", mouth="open", eye="annoyed")
        m "[hermione_name] you should know that when you 'Assume', you make and ass out of you..."
        call her_main("... and me?", mouth="shock", eye="base")
        m "Yep, you make an ass out of you and you."
        call her_main("...", mouth="annoyed", eye="annoyed")
        m "..."
        call her_main("... The favor?", mouth="open", eye="annoyed")
        m "The wha- Oh Right! I want you to masturbate during class."
        call her_main("[genie_name]!", mouth="shock", eye="wide")
        call her_main("I was right to assume that this would be humiliating!", mouth="angry", eye="angry")
        m "you know what they say about assuming, you make an"
        call her_walk(action="leave", speed=2.5)

        show screen blkfade
        call hide_blkfade

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call bld
        m "..."
        call her_main("...", mouth="upset", eye="down")
        m "...So"
        call her_main("I did it.", mouth="clench", eye="frown")
        m "Excellent work!"
        call her_main("I feel like I'm going to be sick.", mouth="upset", eye="down")
        m "Really? That shouldn't be happening. Are you sure you know what masturbating is?"
        call her_main("May I just have the points now.", mouth="angry", eye="angryCl")
        call her_main("And possibly the obliviate curse?", mouth="clench", eye="base")
        call her_main("Because I want my memory of this day gone!", mouth="scream", eye="wide")
        call her_main("", mouth="normal", eye="annoyed")
        m "Obliviate? I think you are thinking of Roofies."
        call her_main("POINTS!", mouth="angry", eye="angry")
        m "Now hold your horses [hermione_name] We need to verify you did your task correctly."
        call her_main("Sir!", mouth="scream", eye="angry")
        call her_main("", mouth="normal", eye="angry")
        m "Just give me a quick little run down and you're done."
        call her_main("I'd really rather not.", mouth="upset", eye="annoyed")
        m "Come on, you masturbated during class, is this really so hard in comparison?"
        call her_main("I did it during Professor Flitwick’s class.", mouth="annoyed", eye="annoyed")
        call her_main("He's...well he's a sweet short old man but not a very good teacher.", mouth="open", eye="base")
        call her_main("He might be the SECOND most senile person at Hogwarts.", mouth="smile", eye="narrow")
        m "Who’s the first?"
        call her_main("", mouth="clench", eye="narrow")
        m "Ahem, back to the story of flicking your flaps, [hermione_name]"
        call her_main("Professor Flitwick was giving the same lecture on levitation charms.", mouth="disgust", eye="worried")
        call her_main("For the third time this week, might I add. And no one was paying attention.", mouth="open", eye="base")
        call her_main("I found myself a quiet desk in the back of the room.", mouth="soft", eye="soft")
        call her_main("I'd never sat anywhere but the front before!", mouth="shock", eye="wide")
        m "The horror."
        call her_main("And then I placed my hand over my...", mouth="soft", eye="down")
        m "My?"
        call her_main("Over my...", mouth="open", eye="down")
        m "Meat curtains."
        call her_main("blegh.", mouth="disgust", eye="annoyed")
        m "Did you cum?"
        call her_main("{size=-5}(Swallow it down, just swallow it down you can do this.){/size} Yes.", mouth="clench", eye="down")
        m "Really?"
        call her_main("Only because I knew you wouldn't give me points If I didn't!", mouth="scream", eye="angry")
        m "What were you thinking about?"
        call her_main("None of your fricking business!", mouth="angry", eye="wide")
        m "Woah there, language. Miss Granger remember, I am Head Master FumbleSnore."
        call her_main("If you don't give me points right now, I'm leaving!", mouth="mad", eye="angry")

        menu:
            "\"Here's 80 points.\"":
                m "Party Pooper. 80 Points to Gryffindor."
                call her_main("Thank you, professor. Good Day!", mouth="open", eye="narrow")
                call her_main("{size=-5}(Was that even worth it? I’d rather have just sucked his cock twice then try that again.){/size}", mouth="annoyed", eye="annoyed")
                call her_main("{size=-5}(Did I really just think that?){/size}", mouth="open", eye="down")

            "\"Nah.\"":

                m "Points? What points?"
                call her_main("Sir...", mouth="clench", eye="frown")
                m "If you remember you left before we could discuss any form of points."
                call her_main("...", mouth="annoyed", eye="annoyed")
                m "Ah, is it you assumed I'd give you points for this?"
                m "Well, you know what they say about assuming it makes an ass out of yo-"
                call her_main("AGGGH!", mouth="scream", eye="angry")

        call her_walk(action="leave",2.5)

    #Second Level
    if pathvalue == 1:
        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call bld
        m "'Morning, [hermione_name]."
        call her_main("Good morning [genie_name]", mouth="smile", eye="happy")
        m "Did I ever tell you of the time I saved Christmas?"
        call her_main("Can we just skip to the part where you tell me to do something disgusting.", mouth="clench", eye="frown")
        m "...Go masturbate during class. 80 points."
        call her_main("Fine.", mouth="annoyed", eye="annoyed")

        call her_walk(action="leave", speed=2.5)

        call bld
        m "I would have given you 200 for listening to my story!"

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        m "Why hello there [hermione_name] you loo-"
        call her_main("[genie_name] I demand the expulsion of all those Slytherin Harlots!", mouth="angry", eye="angry")
        m "What happened this time?"
        call her_main("THEY HAVE GROWN TOO BOLD!", mouth="scream", eye="wide")
        m "Perhaps you should just start from the beginning."
        call her_main("THEY-I", mouth="scream", eye="wide")
        call her_main("It was in Snape's class, I was sitting in the back again. Masturbating in class like you made me", mouth="annoyed", eye="annoyed")
        call her_main("Snape's lesson was pointlessly infuriating, as per his usual.", mouth="open", eye="base")
        call her_main("Talking down at us, like we don't know how to brew a Pepperup Potion. What does he think we are? Mewling first years?", mouth="annoyed", eye="annoyed")
        m "I'm pretty sure Snape 'thinks of you as' a cu-"
        call her_main("And that Slytherin troublemaker Daphne Greengrass comes over! Says she can't concentrate with my moaning!", mouth="angry", eye="wide")
        m "Were you moaning?"
        call her_main("Shut up! That’s not important!", mouth="scream", eye="wide")
        m "{size=-5}Jeez.{/size}"
        call her_main("That two faced Slytherin has the nerve to call me a slut! ME!", mouth="angry", eye="angry")
        call her_main("But as soon as we started to argue professor Snape called us both to the front of the class.", mouth="upset", eye="soft")
        call her_main("Of course he asked Daphne for her side of the story first.", mouth="annoyed", eye="base")
        call her_main("She pretended to act all innocent and embarrassed at first.", mouth="open", eye="soft")
        call her_main("But when Snape asked her again, she might as well have screamed that I was 'playing with myself.'", mouth="annoyed", eye="squint")
        call her_main("When I tried to deny it, Proff- That disgusting pig Snape just grabbed my hand and sniffed it.", mouth="clench", eye="disgust")
        call her_main("The face he made had the whole class laughed at me! I was-", mouth="open", eye="wide", cheeks="blush")
        call her_main("I was- They-aghh!", mouth="angry", eye="angry")
        m "Just let it out [hermione_name]"
        call her_main("Those...THose...THOSE!", mouth="scream", eye="wide")
        call her_main("THOSE DISGUSTING WORMS! TALK TO ME LIKE THAT? TWO FACED HYPROCRITES! FUCK THEM!", mouth="scream", eye="wide")
        m "Feel better?"
        call her_main("...", mouth="normal", eye="base")
        call her_main("... No, no I do not. Not until those Slytherins pay.", mouth="open", eye="narrow")
        call her_main("[genie_name] I don't care about my points for this. I just want you to do something about Slytherin.", mouth="open", eye="soft")
        menu:
            "\"Give 80 Points to Gryffindor.\"":
                m "Sorry [hermione_name], but there isn't much I can do."
                m "But here these should cheer you up, 80 house points to Gryffindor."
                call her_main("Ugh- It's like you don't even listen to me.", mouth="annoyed", eye="annoyed")

            "\"Take 200 points from Slytherin.\"":
                m "Hmmm. While I doubt I can do anything official just yet..."
                m "200 house points from Slytherin!"
                call her_main("Serves them right. Heh, heh heh.", mouth="grin", eye="happy")
                call her_main("You know I understand now why I rushed here to talk to you.", mouth="smile", eye="happy")
                call her_main("You always know just what to say to make me feel good. [genie_name]", mouth="open", eye="happy")
                m "Glad to be appreciated [hermione_name]"
                call her_main("In this case I don't think I'd mind 'showing you some of that appreciate-", mouth="soft", eye="soft")
                call her_main("Ahem. I mean.... uhm It's getting time for dinner. So, goodnight [genie_name]", mouth="open", eye="down", cheeks="blush")
                m "See you tomorrow [hermione_name]"
                call her_main("Yes! I mean...if I must.", mouth="open", eye="glance")
                call her_main("{size=-5}Totally worth it.{/size}", mouth="smile", eye="happy")

            "\"Humiliate her.\"":
                m "I'm sorry can you say that again?"
                call her_main("Agh! For the hundredth time, DO SOMETHING about Slytherin!", mouth="annoyed", eye="annoyed")
                m "...For?"
                call her_main("For embarrassing me during class!", mouth="upset", eye="narrow")
                m "And how did they embarrass you?"
                call her_main("They told the whole class I was masturbating!", mouth="annoyed", eye="annoyed")
                m "Why'd they do that?"
                call her_main("Garr! I don't know, because they are petty unintelligent brutes?", mouth="angry", eye="angry")
                m "Is that the only reason?"
                call her_main("I don't know what motivates those Slytherin harl-", mouth="clench", eye="base")
                m "Are you sure it wasn't FOR masturbating during class?"
                call her_main("...", mouth="normal", eye="concerned")
                m "Which you were."
                m "And not for the first time."
                call her_main("That's that- You're making me!", mouth="annoyed", eye="annoyed")
                m "Making? All I did was offer you some house points. And not that many, what 80? I'm sure you could have done a little book report and gotten that many."
                m "Instead you choose to ignore your lesson in favour of pleasuring yourself in class."
                m "Are you sure that you aren't you the..."
                call her_main("Stop it...please.", mouth="upset", eye="down")
                m "The hypocritical harlot?"

        call her_walk(action="leave", speed=2.5)

    # Third Level
    elif pathvalue == 2:
        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call bld
        m "POP QUIZ!"
        call her_main("{size=-5}(my ears!){/size}", mouth="annoyed", eye="annoyed")
        m "Question 1 of 1 if you wanted to earn 80 points, you'd need to..."
        m "A. Kiss a girl? B. Flash your Tits. C. Masturbate during class. D. Eat a wand."
        call her_main("C? And you aren't actually going to make me eat a wand one day, are you?", mouth="open", eye="concerned")
        m "For 75 house points I might."
        call her_main("I feel like it should be a lot more than that.", mouth="open", eye="base")
        m "For sucking a dick? Nah seems fair."
        call her_main("Suck a di- But you said eat a wand.", mouth="clench", eye="frown")
        call her_main("Oh. I guess I walked into that one [genie_name].", mouth="smile", eye="happy", cheeks="blush")
        m "Hey you got it in the end! That's progress from before!"
        call her_main("Hmm, good point. Anyway, you wanted me to masturbate during class?", mouth="open", eye="base")
        m "Up for it?"
        call her_main("Sure why not...though I wish you had asked yesterday.", mouth="annoyed", eye="annoyed")
        call her_main("Snape gave a 2-hour lecture on the 'Rich and Pure' History of Slytherin.", mouth="open", eye="base")
        m "You don't ALWAYS need my permission to masturbate [hermione_name]"
        call her_main("Oh trust me, I know.", mouth="soft", eye="soft", cheeks="blush")

        call her_walk(action="leave", speed=2.5)

        show screen blkfade
        call hide_blkfade

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call bld
        m "Everything alright [hermione_name]? I usually expect you a bit earlier."
        call her_main("Uh.. yeah, yeah.", mouth="upset", eye="down")
        m "..."
        call her_main("...", mouth="clench", eye="base")
        m "..."
        call her_main("[genie_name] I promise I won’t be mad. I just need you to tell me something.", mouth="open", eye="base")
        m "Alright? {size=-5}(oh god, I hope she didn't learn it was me who rubbed my dick in her-){/size}"
        call her_main("Did you- Did you ever put a curse or something on me? Or give me some secret potion?", mouth="soft", eye="annoyed")
        m "...No?"
        call her_main("...", mouth="normal", eye="base")
        m "What are you trying to ask [hermione_name]"
        call her_main("I...", mouth="upset", eye="narrow")
        call her_main("I was masturbating in class like you asked, Flitwick again.", mouth="open", eye="soft", cheeks="blush")
        call her_main("And- I was doing 'well' but I couldn't -uh- finish.", mouth="upset", eye="down", cheeks="blush")
        call her_main("I don’t know why! It's never happened before!", mouth="scream", eye="wide")
        call her_main("Class was nearly over and I just couldn't do it no matter how much I tried.", mouth="annoyed", eye="annoyed")
        m "Maybe you weren't trying hard enough."
        call her_main("Not trying hard enough? [genie_name] to put it delicately... Hmmm.", mouth="open", eye="baseL")
        call her_main("How would you put shoving three fingers down my slit, rubbing my clit with my thumb, and using my free hand to pinch my nipples delicately?", mouth="soft", eye="soft", cheeks="blush")
        m "Sounds plenty delicate to me! But maybe it was just nerves."
        call her_main("I mean people were staring but...I'm pretty used to that by now.", mouth="upset", eye="frown")
        m "Maybe it was-"
        call her_main("Can I just tell you what it was?", mouth="open", eye="angry")
        m "Oh, fine."
        call her_main("Class was nearly over and I was really going at it...", mouth="soft", eye="soft", cheeks="blush")
        call her_main("Friction must have rubbed of a layer of skin at least.", mouth="open", eye="soft", cheeks="blush")
        call her_main("But nothing was happening. In my head I just kept telling myself to cum, again and again and again but it wasn't enough", mouth="clench", eye="annoyed", cheeks="blush")
        call her_main("...And then...", mouth="soft", eye="soft")
        m "And then?"
        call her_main("....", mouth="upset", eye="down", cheeks="blush")
        call her_main("I imagined 'you' telling me to cum [genie_name]", mouth="soft", eye="soft", cheeks="blush")
        m "And?"
        call her_main("I came.", mouth="smile", eye="soft", cheeks="blush")
        call her_main("I came really really hard.", mouth="grin", eye="wide", cheeks="blush")
        m "Sounds pretty standard to me."
        call her_main("Does it? I guess. I just-", mouth="open", eye="down")
        call her_main("I was wondering if you put the imperio curse on me, or some potion...Something that MADE me follow your orders.", mouth="open", eye="base")
        call her_main("I was just- Sorry I was being s-", mouth="clench", eye="concerned")
        m "[hermione_name]"
        m "I've never made you do anything. I've just offered you a reason."
        m "The choice to do all this has ALWAYS been yours. If you need ‘my voice’ in order to find completion there’s no one to blame but yourself."
        call her_main("Ah.", mouth="upset", eye="down", cheeks="blush")
        call her_main("... Thinking about something like that would've used upset me...but now.", mouth="open", eye="base")
        call her_main("Well the only person who doesn't seem to like the new me, is the old me.", mouth="clench", eye="glance")
        call her_main("And I think the new me is starting to listen to the old me less and less.", mouth="smile", eye="happy", cheeks="blush")
        call her_main("Does that make sense?", mouth="open", eye="base")
        m "Yes, I think it does. 80 house points."
        call her_main("{size=-5}Really?{/size} For what? Oh right masturbating during class. Hahah, I already forgot.", mouth="silly", eye="happy")
        m "Have a good night [hermione_name]"
        call her_main("You too [genie_name]", mouth="open", eye="base")

        call her_walk(action="leave", speed=2.5)

    #Fourth Level
    elif pathvalue == 3:
        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call bld
        m "How are you doing this fine, beautiful morning my little, wittle [hermione_name]"
        call her_main("How sweet of you to ask, I'm quite well my handsome, bandsome [genie_name]. And yourself?", mouth="smile", eye="happy")
        m "Every day with you in it is quite fine, my cutesy, dutesy [hermione_name]"
        call her_main("Oh you're incorrigible old caddy, daddy [genie_name] and how did you sleep?", mouth="open", eye="happy")
        m "I found this chair to be quite hospitable last night my slutty, dutty [hermione_name]"
        call her_main("That chair there? My word, my glamorous, amorous [genie_name] you deserve so much more!", mouth="shock", eye="wide")
        call her_main("In fact, I know a quite warm bed in the girl’s dormitory that would love to have you.", mouth="soft", eye="soft", cheeks="blush")
        m "Really? Well my whorish, shoaris- no my whorish, boari- no. Ah whatever. Let's get to business."
        call her_main("Of course, sir. {size=-5}(Yes! 1 conversation point to [hermione_name]){/size}", mouth="smile", eye="happy")
        call her_main("{size=-5}(Score is... [hermione_name] 1 - [genie_name]...58){/size}", mouth="clench", eye="worried")
        m "...Paying attention?"
        call her_main("Yes, yes of course gorgeous, dorg- I mean [genie_name]", mouth="open", eye="base", cheeks="blush")
        m "Right, well as I was saying for today’s favor, I want you to masturbate during class."
        call her_main("Can there be bonus points?", mouth="open", eye="base")
        call her_main("", mouth="base", eye="base")
        m "Bonus points?"
        call her_main("You know...for masturbating during more than one class, or masturbating more than once per class...", mouth="open", eye="soft", cheeks="blush")
        her "...for smuggling in and using a dildo."
        her ".... Or getting caught on purpose."
        call her_main("", mouth="soft", eye="soft", cheeks="blush")
        m "Oh you gorgeous little, teasing minx!"
        call her_main("I thought we were done with the nicknames.", mouth="annoyed", eye="base")
        m "Hmm yes, well unfortunately according to the official rules, I may only give 80 points per day for masturbation related favors."
        call her_main("Oh I see, that's too bad.", mouth="upset", eye="down")
        g9 "A real shame...but there nothing preventing you from doing those 'bonus’ acts on your own."
        call her_main("I guess...", mouth="upset", eye="frown")
        m "I'd certainly be happy about it...And perhaps my happiness will be its own reward?"
        call her_main("Heh. Yes, maybe it will. Well I better get to work then.", mouth="smile", eye="base")

        call her_walk(action="leave", speed=2.5)

        show screen blkfade
        call hide_blkfade

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2.5)

        call her_main("[genie_name]", mouth="open", eye="base")
        m "Did you complete your task?"
        call her_main("Of course, was there ever any doubt?", mouth="smile", eye="base")

        menu:
            "\"Just give her the points.\"":
                m "Well I trust you at your word, [hermione_name] 80 points."
                call her_main("Oh really? Are you sure you don't want me to give you the details to be sure?", mouth="upset", eye="frown")
                m "No no, it's quite alright you deserve my trust. I'm sure you have some studying or some such to get to"
                call her_main("I suppose. Well goodnight [genie_name]", mouth="annoyed", eye="annoyed")

            "\"Tell me about it.\"":
                m "Well [hermione_name], how was your day exactly?"
                call her_main("Let's just say it was...", mouth="open", eye="baseL")
                call her_main("Busy.", mouth="soft", eye="soft", cheeks="blush")
                call her_main("Do you want to hear about my class with Slughorn, or my class with mad eye moody?", mouth="open", eye="soft")
                m "Go ahead and pick your favourite."
                call her_main("I definitely preferred Mad Eyes. Today we had a written exam and well-", mouth="open", eye="base")
                m "Go on."
                call her_main("And well I didn't use to pay attention to my classmates whining about the written exams in that class before but...", mouth="open", eye="closed")
                call her_main("I think they might have a point. Written tests there are just stupid.", mouth="annoyed", eye="annoyed")
                m "Gasp."
                call her_main("I know it's rich coming from me, but I want to think my time with you is giving me a more practical view of the world and-", mouth="open", eye="happy")
                call her_main("Well come on, it's a defense against the dark arts class.  What's the point of a 'written exam'?", mouth="smile", eye="happy")
                call her_main("Am I going to send a letter to the dementors and bogarts asking them to stop?", mouth="open", eye="happyCl")
                m "{size=-5}(I don't think I want to know what those are.){/size}"
                m "Indeed, so encouraging to hear our session are making you a better person, but I think we are getting off track here."
                call her_main("Hmmm?", mouth="clench", eye="base")
                m "Masturbating in bad lipped Mike's class?"
                call her_main("{size=-5}(Bed lipp-?){/size} Oh, Professor Moody's class.", mouth="open", eye="narrow")
                call her_main("Right, there was an exam and I didn't study at all for it!", mouth="upset", eye="frown")
                m "Second gasp!"
                call her_main("You don't have to say \"gasp\" you can just gasp.", mouth="annoyed", eye="annoyed")
                call her_main("And who do you think is responsible for my lack of study time?", mouth="angry", eye="angry")
                call her_main("But anyway, I was staring at a test not knowing a thing, my worst nightmare.", mouth="upset", eye="down")
                call her_main("And then I might have got a naughty Idea...", mouth="soft", eye="soft", cheeks="blush")
                m "Oh?"
                call her_main("I thought if I was going to fail no matter what...", mouth="upset", eye="down")
                call her_main("Then I needed to make sure everyone else did too!", mouth="grin", eye="happy")
                m "And how did you accomplish that?"
                call her_main("Oh you know...I might have offered a bit of a distraction.", mouth="soft", eye="soft")
                call her_main("At first, I just began with some light rubbing, but when that wasn't enough, I knew I needed to step up my performance.", mouth="soft", eye="soft", cheeks="blush")
                call her_main("I started to make a little noise. You know, sneezing, squeaking my chair, complaining how hot the room was for some reason....", mouth="soft", eye="soft", cheeks="blush")
                m "Moaning?"
                call her_main("Maybe just a bit...mmmmh.", mouth="grin", eye="soft", cheeks="blush")
                call her_main("And it started to work, one after another students would start to glance up.", mouth="smile", eye="soft", cheeks="blush")
                call her_main("Hehehehe. Their reactions were all the same and funny every time.", mouth="grin", eye="happy")
                call her_main("They'd glance up annoyed at the noise, and do the biggest double take at me.", mouth="grin", eye="soft", cheeks="blush")
                call her_main("All the desks have a bottom covering unfortunately, but I think they could quite clearly see my hand moving.", mouth="soft", eye="soft", cheeks="blush")
                call her_main("I could see the doubt in their eyes, telling themselves I was just itching my legs and they were imagining things...", mouth="smile", eye="closed", cheeks="blush")
                call her_main("Then they'd look up...see my grin, the look in my eyes...mphhh..and let's say they wouldn't look at their own tests again.", mouth="grin", eye="ahegao", cheeks="blush")
                m "Need to take care of something, [hermione_name]?"
                hide screen hermione_main
                with d3

                $ hermione_wear_stockings = False
                $ hermione_wear_bottoms = False
                $ hermione_wear_panties = False
                call update_her_body

                call her_main()
                call set_her_action("fingering")
                call her_main("Thank you, [genie_name] But I wouldn't mind if you did this, your hands are much stronger then mine and so much better at finding my nhhh- sensitive spots", mouth="soft", eye="soft", cheeks="blush")
                m "No No, you're doing fine on your own. And don't forget your story."
                call her_main("Oh [genie_name] I really felt like a storybook witch then. Casting a charm over a whole village. Hagh Hagh, wrapping them around my finger.", mouth="grin", eye="wide", cheeks="blush")
                m "Or maybe a succubus!"
                call her_main("Yesssss. Ah I'm Cumming! {image=textheart}{image=textheart}{image=textheart}", mouth="open_tongue", eye="ahegao_wide", cheeks="blush")
                $ hermione_squirt = True
                call her_main("God, never in my whole life have I ever felt that wanted, all those eyes on me. Thinking ME more important to look at then their tests. Ngh!", mouth="grin", eye="ahegao", cheeks="blush")
                call her_main("And I was sure to grab the attention of the Slytherins first.", mouth="smile", eye="ahegao", cheeks="blush")
                m "Oh why's that?"
                $ hermione_squirt = False
                call her_main("I needed to make sure they failed the tests in particular. Of course, mhh No other reasons mhhh.", mouth="soft", eye="ahegao_intense", cheeks="blush")
                call her_main("But There was no need, by the time the bell rang there wasn't a single person not staring at me mhhhh- ah", mouth="smile", eye="ahegao", cheeks="blush")
                $ hermione_squirt = True
                call her_main("And from the looks on some of their faces...and the dripping down the desks...I wasn't the only one getting 'hot' in that room.", mouth="open", eye="ahegao", cheeks="blush")
                m "And Rad nose Booty didn't mind his entire class watching you get off?"
                call her_main("Oh him. Ha-ha Let's just say his eye wasn't doing much spinning that class. I hear it can even see through walls to so-", mouth="soft", eye="soft", cheeks="blush")
                call her_main("and ah ah ah, that was the best part. I got an owl delivering my graded test back, before coming here. ah ah", mouth="smile", eye="ahegao", cheeks="blush")
                call her_main("A+ 100% no questions answered.", mouth="grin", eye="wide", cheeks="blush")
                call her_main("AGGGH! {image=textheart}{image=textheart}{image=textheart}", mouth="open_wide_tongue", eye="ahegao", cheeks="blush")
                m "Well it certainly sounds like you had a fun day."
                call her_main("Pant Pant, heh and I didn't tell you about my other classes.", mouth="smile", eye="happy", cheeks="blush")
                m "[hermione_name] I'm going to repeal the rule about not giving bonus points, you'll get double for today."
                call her_main("Thank you, [genie_name]", mouth="smile", eye="base")

                call her_walk(action="leave", speed=2.5)

    call blkfade
    # call h_unequip_temp_outfit
    call her_chibi("hide")
    hide screen main_room

    jump enter_room_of_req
