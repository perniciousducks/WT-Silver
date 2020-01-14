
# After the ending when Dumbledore has returned and the original credits have played
# the player gets a choice to either end the game or return to before the ending happened

# Genie gets stuck in the cosmos not being able to go anywhere
label ending_after:
    call blkfade
    centered "{size=+7}{color=#cbcbcb}Somewhere outside of time and space...{/color}{/size}\n\n"
    play music "music/epic-unease-by-kevin-macleod.mp3" fadein 1 fadeout 1 # noloop
    pause 3
    g2 "Where... where am I...?" with d5
    g2 "Am I dead... is this the end...?"
    g2 "Genies aren't supposed to die are they?"
    g12 "No wait...{w=0.4} this is different...{w=0.4} I feel..."
    g12 "I feel..."
    show screen white
    pause .1
    hide screen white
    g14 "Everything!" with hpunch
    g14 "The...{w=0.6} The cosmic power is running through me!"
    g14 "I can see it, the universe... No...{w=0.6} Multiple universes... all around me."
    g14 "But... Why?"
    g14 "Why am I not back yet!?"
    show screen white
    pause .1
    hide screen white
    g15 "ARGH!" with hpunch
    g15 "I... I feel like I'm being torn apart!"
    g15 "My form is being pulled in multiple directions!"
    show screen white
    pause .1
    hide screen white
    g14 "Wait...{w=0.4} I know..." with d3
    g14 "This...{w=0.6} this spell!"
    g14 "I need to focus where I want to be... Or I'll be stuck... stuck here forever!"
    g14 "Stupid...{w=0.4} life choices!"
    g14 "Focus..."
    g14 "I just left a bunch of Sluts at that school!"
    g14 "But...{w=0.6} I need to get home!"

    # Choose to end the game or continue playing
    menu:
        g14 "What should I do?"
        "Go home to Agrabah (exit to main menu)":
            g14 "Yes, that is probably for the best..."
            show screen white
            pause .1
            hide screen white
            g15 "Agrabah... here I come! You better prepare yourself..." with hpunch

            stop music fadeout 10
            call big_bang

            $ renpy.full_restart()

        "Cause a time paradox at Hogwarts":
            g14 "On the other hand..."
            g14 "Who doesn't love-"
            show screen white
            pause .1
            hide screen white
            g15 "A good old time paradox!" with hpunch
            g15 "It better be worth it... Here I go!"

            stop music fadeout 10
            call big_bang

            # Genie stands in the forest before he's about to leave
            $ ccg_folder = "ball"
            $ ccg(layer1="171", layer2="172", layer3="173")
            call play_music("night_outside")
            pause.5
            call hide_blkfade

            m "Good bye world of bizarre magic..."
            m "Good bye my who--......"
            m "Wait..."

            # Record scratch, music stops
            $ ccg(layer3="blank")
            stop music fadeout 1.5
            $ renpy.play('sounds/scratch.wav')
            with hpunch

            g4 "What the fuck am I doing..."
            g4 "Why leave now when I'm the king of a castle filled with women ready to serve!?"

            # Heading back to the castle
            call play_music("night_outside")
            call blkfade
            hide screen ccg
            call play_sound("walking_on_grass")
            pause .5

            ">You hastily make your way back to the castle, wondering what kind of impulse made you want to leave in the first place..."
            stop music fadeout 3

            if public_whore_ending:
                ">Arriving at the great hall you glance through the doors and notice some of the other students gawking at Hermione."
                ">Just as you decide to head back to your office she spots you and begins making her way in your direction."
                ">Behind Hermione's back a bunch of Slytherin students have turned in her direction, smirking as she approaches you."
                her "Back so soon?"
                m "I um...{w=0.4} had a change of heart."
                her "Cold outside?"
                m "Yes... that's it."
                ">Standing there in silence, looking at Hermione, you can't help but struggle with what to say."
                call play_music("ball") #can this fade in/be a bit lower volume
                ">But before you get the chance to say anything, music suddenly emerges out the great hall doorway."
                her "Care for a dance?" # smiles
                m "I... of course!"
                her "..." # smiles
                ">With your arms wrapped around Hermione's waist the two of you begin moving along with the music."
                ">As some time passes it's very clear that the students are still eyeing Hermione up and are now staring at her through the doorway."
                m "Miss Granger..."
                her "Yes?"
                call play_sound("slap_3")
                her "..." # shocked
                her "Hey! At least warn me!" # Blush, smiles
                ">Swiftly taking your hand away from Hermione's butt you give a quick smirk towards your audience."
                her "I didn't say stop..."
                m "Of course..."
                ">Without a moments hesitation you lift her skirt up, holding it against her back and leaving her panties exposed."
                her "Sir..." #could change the sirs here to the name that the player has set for hermione to call you
                ">Now firmly gripping her butt with your other hand you begin to massage her cheeks whilst moving along with the music."
                her "..." #Look of pleasure
                ">Suddenly the feeling of her soft cheeks is interrupted by something hard brushing against he back of your palm..."
                ">Moving your hand up against her back, you realize Hermione has tucked the letter you gave her firmly in-between the top edge of her skirt..."
                ">Continuing to move along with the music your hand finds its way back down, pulling Hermione's panties with them."
                her "Sir...{w=0.4} what are you doing?"
                m "You seem a little bit tense... just giving you a hand..."
                her "But... What if someone notices..."
                ">Ignoring her pleas you begin rubbing your fingers between her thighs, not bothering to be discreet."
                her "*Ah*...{w} Sir..."
                ">As you move your hand higher up her thighs, Hermione's breathing quickens and a wetness begins to spread across the side of your hand, her legs shaking slightly as she tries to keep it together."
                her "Sir...{w=0.4} I..."
                ">With the music soon coming to a close you shift your hand and begin stroking against her vagina with even more vigour than before."
                her "Sir...{w=0.3} *Ah*...{w=0.5} they'll...{w=0.2} they'll hear me..."
                m "You better \"come\" quietly then..."
                her "Sir... this isn't the time for..."
                ">As the music reaches it's peak, Hermione moves one of her hands off your back and puts it against her mouth to quickly try and stifle herself."
                her "*Mmmmf*..."
                stop music fadeout 3
                ">Hermione shudders in your arms and then quickly lets go as the music comes to an end and you snag the letter from her skirt, pocketing it."
                her "*Ah*...{w=0.3}*Ah*...{w=0.3}*Ah*..."
                ">With a quick glance towards the doorway you notice some Slytherin students have blocked it with their backs towards you."
                m "You look tired girl, you'd better pull yourself together..."
                her "Yes...{w=0.3} *Ah*... I just need to...{w=0.3} catch my breath..."
                m "Perhaps sooner rather than later, the music has stopped..."
                her "Oh...{w=0.3} *Ah*...{w=0.3} I didn't even notice..."
                ">Hermione moves to stand up but stumbles as she tries to compose herself..."
                ">As she gets on her feet she looks up and notices the backs of the Slytherins in the doorway. She spins around to look at you, a red colour quickly spreading across her cheeks."
                her "I...{w=0.3} I think I'd better head off to bed then..." #Worried #Sheepish looking
                m "Sounds like a good idea..."
                her "And I'll make sure that I-"
                her "..." # shocked
                her "The letter!"
                her "It's gone!"
                m "..."
                m "No matter, it wasn't that important."
                m "Nothing that you don't already know..."
                her "You sure?"
                m "As sure as my name is Albus Dumbledore."
                her "Okay..." # smiles
                her "Good night then..."
                m "Good night Miss Granger."


                # Back in the office
                call room("main_room")
                call gen_chibi("hide")
                show screen chair_left
                show screen desk
                call hide_blkfade
                pause 1.0
                call play_sound("door")
                call gen_chibi("stand","door","base",flip=False)
                with d3
                pause 0.3

                m "Good night princess..."

                call blkfade

                # Next day
                centered "{size=+7}{color=#cbcbcb}The next morning...{/color}{/size}"

                call common_start(True) #TODO We should probably have a special label for day/night advance during events
                call music_block
                call hide_blkfade

                # Snape enters and walks up to desk
                call sna_walk(action="enter", xpos="desk")
                g4 "What did I said about knocking!"
                sna "Who rule..."
                sna "You mother fucker..."
                sna "I knew it!"
                sna "I knew you couldn't make yourself leave yet."
                g9 "Hey, it's not my fault this place has so many..."
                g4 "I have urges okay!"
                sna "How very uncharacteristic of you..."
                sna "But good news nonetheless..." # Smirks
                sna "So I take it you have... unfinished business before you depart?"
                m "A headmaster can't just up and leave before the school year is over can he?"
                m "Also I'm getting quite fond of the place... Not that I want to pick out curtains or anything."
                sna "..." # Smirks
                sna "Very well... our little scheme continues."
                sna "Although at the moment I've got a class to attend to."
                call sna_walk(xpos="door")
                m "Yes... I also have very important business to get on with..."
                sna "I'm sure..."
                call sna_walk(action="leave")
                jump main_room
            else:
                call play_music("ball") #How do I add fade in to this?/can we make the music a bit lower since they're outside the doors
                ">Arriving at the great hall you decide to take a quick glance through the doors before heading back to your office."
                ">Hermione is currently occupied looking out one of the windows and doesn't notice your presence."
                ">You look over at the teachers table and lock eyes with Snape who stands up and quickly slides towards you."
                call sna_main("Good evening sir...{w=0.5} I...{w=0.8} I didn't expect you so soon.","snape_29",ypos="head")
                m "Hello again Severus."
                m "I have returned..."
                call sna_main ("*Ahem...*{w=0.4} I see...","snape_06",ypos="head")
                call sna_main ("Well...{w=0.5} Here it goes...","snape_04",ypos="head")
                call sna_main ("Who...{w=0.5}who rules?","snape_09",ypos="head")
                m "..."
                call sna_main (".............","snape_25",ypos="head")
                call sna_main ("...","snape_26",ypos="head")
                g9 "Robin Williams."
                call sna_main("You mother fucker!","snape_20",ypos="head") #Epic handshake meme (jk)
                g9 "..."
                call sna_main("...","snape_12",ypos="head")
                call sna_main("About the thing I said earlier.","snape_12",ypos="head")
                m "yes?"
                call sna_main("The whole friend thing...","snape_14",ypos="head")
                m "Ah... yes..."
                m "I mean, I was leaving and all that-"
                call sna_main("No...{w=0.4} Even that being the case... I did mean it...{w=0.4} good ones are hard to come by.","snape_24",ypos="head")
                g9 "Well... even if you didn't mean it, I bet you ain't never had a friend like me."
                call sna_main ("Ain't that true...{w=0.3}","snape_45",ypos="head")
                call sna_main ("So...{w=0.4} You're staying then?","snape_46",ypos="head")
                g9 "Can't just leave in the middle of the school year can I? What kind of headmaster would do that?"
                call sna_main ("Is that so...","snape_47",ypos="head")
                g9 "There are still plenty of girls that haven't seen me at my best!"
                call sna_main("There it is...","snape_02",ypos="head")
                call sna_main("Well then...{w=0.4} Business as usual tomorrow?","snape_05",ypos="head")
                m "Business as usual..."
                call sna_main ("{size=-4}Fuck yes!{/size}","snape_47",ypos="head")
                m "What did you say?"
                call sna_main ("Nothing...","snape_38",ypos="head")
                m "Okay then..."
                m "In that case I'll head back to my office."

                ">As Snape heads back towards the teachers table, Hermione notices your presence and quickly starts heading in your direction."
                ">Before you can even attemp to slip into the shadows again, she's already come through the doorway with one of her arms held out in front of her."
                her "Care for a dance?" # smiles
                m "I...{w=0.4}Oh, what the hell... why not."
                her "..." # smiles
                ">With your arms wrapped around Hermione's waist the two of you begin moving along with the music."
                ">After some time passes you can't help but look down on Hermione's butt sticking out below your hands."
                m "Miss Granger..."
                her "Yes?"
                ">Hands now wandering down towards Hermione's butt she smiles and tightens her grip around you."
                ">Gently resting your hands against her cheeks you return to slowly moving along with the music."
                her "Sir..." #same thing as earlier here, get hermione to use the name you've set and genie to do the same
                m "Yes Miss Granger?"
                her "Could..."
                her "Why can't this moment go on forever?"
                m "We both know that everything has to come to an end..."
                m "But hopefully I've been able to teach you to cherish every moment."
                ">Hermione tightens her arms even more as you continue the dance in silence."
                ">After a while her grip loosens slightly as she shifts her head to look up at you."
                her "I..."
                her "I just wanted to say that...{w=0.5} I'm glad I have you."
                m "Where's this suddenly coming from Miss Granger?"
                her "I don't know... it's just..."
                her "I couldn't help having this bad feeling in my stomach the entire day."
                her "And it's stayed there up until now...{w} Now it's finally feeling as if the pain has started to go away..."
                ">Not knowing how to respond you stand there in silence for a moment until Hermione pulls you towards her and you both begin moving along with the music once more."
                ">After what only feels like seconds the music comes to a close and Hermione takes a step back to look up at you."
                m "You look tired girl, you'd better head off to bed...{w=0.4} there's always tomorrow."
                her "Oh, yes... I suppose so..."
                her "Good night then..."
                m "Good night."
                her "Oh... wait,{w=0.3} before you go..."
                m "Yes?"
                call play_sound("kiss")
                #Heart animation on screen?
                her "..."
                g9 "What was that for?"
                her "Nothing, I just felt like you earned it."
                her "See you tomorrow..."
                m "Good night Miss Granger."

                stop music fadeout 1

                # Back in the office
                call room("main_room")
                call gen_chibi("hide")
                show screen chair_left
                show screen desk
                call hide_blkfade
                pause 1.0
                call play_sound("door")
                call gen_chibi("stand","door","base",flip=False)
                with d3
                pause 0.3

                m "Good night princess..."

                call blkfade

                jump day_start

label big_bang:
    show screen big_bang
    with Fade(0.7, 0.5, 0.7, color='#fff')
    play bg_sounds "sounds/rumble.mp3" fadein 2
    pause 3
    show screen big_bang(True)
    $ renpy.sound.play("sounds/bang.mp3")
    pause 1.5
    #with Move((0, 25), (0, -25), 0.2, bounce=True, repeat=True, delay=1.0)
    pause 12
    stop bg_sounds fadeout 2
    hide screen big_bang
    with d5
    return

screen big_bang(bang=False):
    zorder 7

    add Solid("#000")

    showif bang:
        add "images/misc/bang.png":
            at transform:
                zoom 0.0
                anchor (0.5, 0.5)
                pos (540, 300)
                on show:
                    easeout 15.0 zoom 3
    else:
        add "glow_effect" zoom 0.2 anchor (0.5, 0.5) align (0.5, 0.5)
