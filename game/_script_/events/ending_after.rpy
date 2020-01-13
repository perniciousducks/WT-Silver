
# After the ending when Dumbledore has returned and the original credits have played
# the player gets a choice to either end the game or return to before the ending happened

# Genie gets stuck in the cosmos not being able to go anywhere
label ending_after:
    call blkfade
    centered "{size=+7}{color=#cbcbcb}Somewhere outside of time and space...{/color}{/size}\n\n"
    play music "music/epic-unease-by-kevin-macleod.mp3" fadein 1 fadeout 1 # noloop
    pause 3
    g2 "Where... where am I...?" with d5
    g2 "Did I finally find it, the end...?"
    g12 "No wait... this is different... I feel..."
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

            stop music fadeout 15
            call big_bang

            $ renpy.full_restart()

        "Cause a time paradox at Hogwarts":
            show screen white
            pause .1
            hide screen white
            g15 "A good old time paradox!" with hpunch
            g15 "It better be worth it... Here I go!"

            stop music fadeout 15
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
            g4 "Why leave now when I'm the king of a castle filled with women ready to serve."

            # Heading back to the castle
            call play_music("night_outside")
            call blkfade
            hide screen ccg
            call play_sound("walking_on_grass")
            pause .5

            ">You hastily make your way back to the castle, wondering what kind of impulse made you want to leave in the first place..."
            stop music fadeout 3

            if public_whore_ending:
                ">As you're about to make your way past the great hall Hermione rushes up to you."
                her "Back so soon?"
                m "I um...{w=0.4} had a change of heart."
                her "Cold outside?"
                m "Yes... that's it."
                ">As you stand there, looking at Hermione you wonder how you're going to be able to get that letter back from her."
                #TODO ball music plays
                ">Before you get a chance to say something, music suddenly emerges out the great hall doorway."
                her "Care for a dance?" # smiles
                m "I... of course!"
                her "..." # smiles
                ">You put your arms around Hermione's waist and begin moving along with the music."
                ">After some time passes you notice the letter wedged inside the top of Hermione's skirt."
                m "Miss Granger..."
                her "Yes?"
                her "..." # shocked
                her "Hey! at least warn me..." # Blush, smiles
                ">You swiftly take your hand away from Hermione's butt, grabbing the letter and pocketing it."
                her "I didn't say stop..."
                m "Of course..."
                stop music fadeout 3
                ">You continue dancing and once the song ends you take a step back from Hermione."
                m "You look tired girl, you'd better head off to bed... there's always tomorrow."
                her "Yes I'd better... and I'll make sure to-"
                her "..." # shocked
                her "The letter!"
                her "It's gone!"
                m "..."
                m "No matter, it wasn't that important."
                m "Nothing that you don't already know..."
                her "You sure?"
                m "As sure as my name is Albus Dumbledore."
                her "Okay..." # smiles
                m "Good night Miss Granger." # use [hermione_name] instead?
                her "Good night!"

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

                m "Always another day tomorrow."

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
                ">As you make your way past the great hall you glance through the door."
                ">Hermione is currently occupied looking out one of the windows, not noticing that she's being stared at by some other students."
                ">Snape catches your eye and walks up to you."
                sna "Good evening sir."
                m "Hello again Severus..."
                sna "*Ahem...* Who... rules?"
                m "..."
                sna "............." # Worried
                g9 "Robin Williams!"
                sna "You mother fucker!" # Smirks
                sna "..." # Goes a bit serious/worried again
                sna "About the thing I said earlier."
                m "yes?"
                sna "The whole friend thing..."
                m "Ah... yes..."
                sna "I did mean it... good ones are hard to come by."
                m "Well... even if you didn't mean it, I bet you ain't never had a friend like me."
                sna "*Ahem*...{w=0.3} So...{w=0.4} You're staying then?"
                m "Can't just leave in the middle of the school year can I? What kind of headmaster does that..."
                sna "Great to-" # Eyes light up
                m "There's still plenty of girls that haven't seen me at my best!"
                sna "There it is..." # Smirks
                m "I'm heading back to my office."
                m "Business as usual tomorrow..."
                sna "{size=-4}Fuck yes!{/size}"
                m "What did you say?"
                sna "Nothing..."
                m "Okay then..."
                ">You make your way back to your office and sit down at your desk."
                m "Business as usual..."

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
