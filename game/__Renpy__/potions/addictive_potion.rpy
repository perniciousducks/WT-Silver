

### CUM ADDICTION ###

label potion_scene_3_1_1: #cum addiction - work in progress, has some scenes adjusted for it
    m "[hermione_name], today I have a very special potion that I would like you to drink."
    call her_main("What does this one do?","normal","frown")
    m "As always, it's going to be a surprise."
    call her_main("You're not going to try to transform me into a cat again are you [genie_name]?","normal","frown")
    call her_main("","normal","frown")
    m "Of course not, now would you kindly drink the potion?"
    call her_main("...","annoyed","angryL")
    call her_chibi("drink_potion","mid","base")

    call nar(">Hermione cautiously starts drinking the potion.")
    call her_main("","cum","worriedCl")
    pause .5
    call her_chibi("stand","mid","base")

    call her_main("This isn't a potion! This is just a bottle full of your cum!","scream","angryCl")
    call her_main("Ughhh and it's cold as well.","disgust","narrow")
    m "So it just tastes like cum to you?"
    call her_main("Of course it does, what else would it taste like?","angry","angry")
    call nar(">Hermione starts unconsciously licking her lips.")
    call her_main("At least warn me next time you make me drink your cum, [genie_name].","open","worriedL")
    m "What do you mean next time?"
    call her_main("Well, you're such a pervert you'll probably try and do this again. At least warn me so it's not such a shock.","annoyed","annoyed")
    m "Ok, [hermione_name], I'll make sure to warn you next time."
    call her_main("Is that all then, [genie_name]?","annoyed","angryL")
    m "Yes [hermione_name], 20 points to Gryffindor."
    call her_main("Thank you, [genie_name].","open","suspicious")
    call nar(">Hermione leaves the room with the remaining potion firmly in her grasp.")
    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    hide screen ctc
    with d3

    call her_walk("mid","leave",2)

    $ addicted = True
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_3_1_2: #Scene where Hermione comes back addicted to your cum (replace sucking noises with actual text)
    call play_sound("door") #Sound of a door opening.
    call her_chibi("stand","mid","base")
    pause.5

    show screen bld1
    call nar(">Hermione quickly enters your office.")
    call her_main("What the hell did you do to me?","scream","worriedCl")
    m "Whatever are you talking about, [hermione_name]?"
    call her_main("Ughh, it doesn't matter, just let me suck it.","annoyed","worriedL")
    m "Why on earth would you want to do that? You're a top student, that doesn't sound appropriate."
    call her_main("You know exactly what you did to me. Now let me suck your filthy old cock.","angry","angry")

    menu:
        "-Let her suck your dick-":
            m "Well if you insist, [hermione_name]."
        "-Make her beg-":
            m "I don't think that you deserve to after calling it filthy and old."
            m "Perhaps if you asked nicely..."
            call her_main("Fine. Please let me suck your dick [genie_name].","upset","wink")
            m "Hmmm, I don't think that was sincere enough."
            call her_main("Please [genie_name], let me suck your big, thick dick. Pretty please.","angry","worriedCl",emote="05")
            m "Much better."

    call blkfade
    pause 1

    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ genie_chibi_xpos = -10 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_left
    show screen g_c_u

    call her_chibi("hide")
    hide screen blktone
    hide screen bld1
    call hide_blkfade
    call ctc

    $ hermione_main_zorder = 8

    show screen bld1
    call nar(">As soon as you remove your cock from your robe Hermione is on top of you.")
    call her_main("","disgust","glance")
    $ g_c_u_pic = "hand_ani"
    with d3
    her "Do you have any idea how hard it was sitting through classes today?"
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    her "*Slurp!* *Slurp!* *Slurp!*"    ###start sucking etc....
    call her_main("","annoyed","angryL")
    $ g_c_u_pic = "hand_ani"
    with d3
    her "Being this aroused."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    her "*Slurp!* *Gobble!* *Slurp!*"
    call her_main("","grin","baseL")
    $ g_c_u_pic = "hand_ani"
    with d3
    her "With no way to relieve myself."
    her "I tried everything."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    her "*Gobble!* *Slurp!* *Slurp!*"
    call her_main("","smile","glance")
    $ g_c_u_pic = "hand_ani"
    with d3
    her "I even masturbated in the girls bathroom."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    her "*Gobble!!* *Gltch!!* *Gobble!!!*"
    call her_main("","annoyed","annoyed")
    $ g_c_u_pic = "hand_ani"
    with d3
    her "But nothing worked."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    her "*Slurp!* *Gulp!* *Slurp!*"
    call her_main("","base","ahegao_raised")
    $ g_c_u_pic = "hand_ani"
    with d3
    her "All I could think about was the taste of your filthy cum."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    her "*Slurp!* *Gulp!* *Gulp!*"
    m "My my, someone is becoming quite the slut wouldn't you say [hermione_name]"
    her "*Slurp!* *Gulp!* *Slurp!*"
    call her_main("","open_tongue","glance")
    $ g_c_u_pic = "hand_ani"
    with d3
    her "You know why this is happening to me."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    her "*Slurp!* *Slurp!* *Gulp!*"
    call her_main("","smile","glance")
    $ g_c_u_pic = "hand_ani"
    with d3
    her "Whatever was in that delicious potion you made me drink this morning."
    hide screen hermione_main
    m "Delicious? I thought you said it was just a bottle full of my cum?"
    m "Are you sure that you're just not a little slut who's become addicted to her Headmaster's semen?"
    call her_main("I'm sure. There was something else in there.","angry","wink")
    hide screen hermione_main
    m "Whatever you say [hermione_name]. Now if you want your reward you better get back to work."
    call her_main("","base","suspicious")
    $ g_c_u_pic = "hand_ani"
    with d3
    her "..."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    with d3
    her "*Slurp!* *Slurp!* *Gulp!*"
    call nar(">She is incredibly enthusiastic. You can feel your load building.")

    menu:
        "-Cum down her throat-":
            m "Here it comes, slut!"
            call nar(">Hermione quickly swallows the majority of your shaft. You can feel the tip of your head pressed against the entrance to her throat.")
            m "You'll have to do better than that if you want your reward [hermione_name]."
            call nar(">You place your hands on the back of her head pull her head into you.")
            call her_main("{size=+7}!!!{/size}","scream","worriedCl")
            hide screen hermione_main
            call nar(">The sensation of entering her throat sends you over the edge.")
            m "Better start swallowing slut!"
            call nar(">You start pumping your thick load directly into her stomach.")
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            call nar(">Hermione's eyes widen and tears form as she senses your semen enter her.")
            call her_main("hhaanooo hhhheerrr","scream","wide")
            hide screen hermione_main
            call nar(">Her hands shoot down into her pants as she starts violently orgasming.","start")
            call nar(">The sight of her pleasuring herself as you use her throat only prolongs your orgasm.","end")
            m "You dirty little girl. Getting off from your headmaster sticking his cock down your throat."
            m "I bet your loving this, being used as a nothing more than a toy."
            call nar(">She says nothing but quickens the pace of her masturbation.","start")
            call nar(">You finally pull out of keen mouth with a satisfactory pop.","end")
            call her_main("It won't stop!","shock","worriedCl")
            hide screen hermione_main
            m "What won't?"
            call her_main("I-I can't stop cumming [genie_name]...","angry","base")
            hide screen hermione_main
            call nar(">The stimulation proves too much and she passes out.")

        "-Cum in her mouth-":
            m "This is it, girl! Get ready!"
            call nar(">Hermione starts swirling her tongue and focusing on the tip of your shaft.")
            g4 "That's done it slut! Start swallowing!"
            call nar(">You explode into her mouth.")
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            call her_main("mmmmmmm... *gulp* *gulp*","full_cum","dead")
            hide screen hermione_main
            call nar(">Hermiones eyes go blank as she starts swallowing down your load.")
            m "That's it, swallow it down like a good girl. You earned your prize."
            call her_main("*gulp* *gulp* *gulp* *gulp*","cum","worriedCl")
            hide screen hermione_main
            call nar(">As she swallows you notice her legs start to convulse as she starts to orgasm.")
            call her_main("*gulp* *gulp* *gulp* ","full_cum","dead")
            hide screen hermione_main
            call nar(">You finally remove your shaft from her hungry mouth.")
            m "Very good girl. Almost entirely clean... except for a bit of cum on the tip."
            m "I can't dirty my robes now can I? Better wipe this off."
            call nar(">You wipe yourself clean on the tip of her nose.")
            call her_main("...","cum","worriedCl")
            hide screen hermione_main
            m "There, much better."
            call nar(">Her legs have not stopped quivering since you first came.")
            m "Well aren't you going to say anything [hermione_name]?"
            call her_main("Thank you maste-","silly","dead")
            hide screen hermione_main
            call nar(">She collapses into a heap on the ground with her legs still shaking.")

        "-Cum on her face-":
            m "Get ready, girl! here it comes!"
            call nar(">Hermione increases her efforts and starts focusing on the head of your penis.")
            m "Not so quick [hermione_name]."
            $ g_c_u_pic = "hand_ani"
            with d3
            call nar(">You quickly pull your penis out from her mouth.")
            call her_main("What are you doing [genie_name]?","shock","wide")
            hide screen hermione_main
            m "Giving you your well earned reward."
            $ g_c_u_pic = "cum_on_face_ani"
            with d3
            $ uni_sperm = True
            call nar(">You start pumping your cock quickly and explode all over the young witch's face")
            m "Take it you filthy cum slut!"
            call her_main("{size=+5}!!!{/size}","soft","ahegao")
            hide screen hermione_main
            call nar(">Hermione immediately starts masturbating shamelessly in front of you.")
            call her_main("{size=+5}I'm cumming{/size}","angry","base")
            hide screen hermione_main
            m "What was that [hermione_name]?"
            call her_main("I-I'm cumming","scream","wide")
            hide screen hermione_main
            m "Just from a facial? What sort of cumslut have you become Miss Granger?"
            m "What would your parents think? Looking at you covered in some old mans cum."
            call her_main("No. Please stop, I'll-","angry","worriedCl",emote="05")
            hide screen hermione_main
            m "They'd be ashamed at what you've become. A whore who gets off from being used as a toy."
            call her_main("I-I'm cumming again [genie_name]. It won't stop...","scream","worriedCl")
            hide screen hermione_main
            call nar(">Hermione's voice trails off as she pass out from the over stimulation.")

        "-Cum on the floor-":
            m "I'm cumming, whore!"
            call her_main("mmmmmmmm...","open_wide_tongue","base")
            hide screen hermione_main
            call nar(">She goes to bury her face into her crouch but you put your palm on her forehead and push her away.")
            $ g_c_u_pic = "hand_ani"
            with d3
            call her_main("[genie_name], what are you doing?","angry","wide")
            hide screen hermione_main
            m "giving you your reward!"
            call nar(">After a few quick pumps you point your dick at the floor and explode.")
            call her_main("PROFESSOR! Why would you waste that?","angry","down_raised")
            hide screen hermione_main
            m "It's not wasted [hermione_name], your reward is right there waiting for you."
            call her_main("I'm not going to eat that. The floor in here is disgusting.","angry","base")
            hide screen hermione_main
            m "Well you can always wait until tomorrow morning then."
            call her_main("TOMORROW MORNING!? I can't wait that long! Can't you just cum again?","angry","wide")
            hide screen hermione_main
            m "No [hermione_name], I'm a tired old man and it's time for me to go to sleep."
            m "You can either eat off the floor or you can come back tomorrow."
            call her_main("...Fine.","upset","closed")
            hide screen hermione_main
            call nar(">She begrudgingly starts scooping your cum off the floor with her fingers.")

            menu:
                "-Watch her-":
                    call her_main("","full_cum","dead")
                    call nar(">She scoops up as much as she can into her palm and quickly moves it to her mouth.","start")
                "-Make her lick it up-":
                    m "Not with your fingers [hermione_name]."
                    call her_main("What do you mean not with my fingers? How else am I supposed to eat it?","angry","base")
                    hide screen hermione_main
                    m "You have a perfectly good tongue, I suggest that you put it to use."
                    call her_main("You expect me to LICK your old cum off the floor?","angry","down_raised")
                    hide screen hermione_main
                    m "I do. Unless of course you would prefer to go back to your room hungry and unsatisfied."
                    call her_main("...","angry","base")
                    hide screen hermione_main
                    call nar(">She bends over with her head to the floor.")
                    $ aftersperm = True
                    call her_main("(This is so degrading...)","open_wide_tongue","angry")
                    hide screen hermione_main
                    call nar(">She puts her tongue out licks your cum.","start")

            call nar(">The effect is instantaneous.","end")
            $ aftersperm = True
            call her_main("I-I'm cumming...","cum","worriedCl") #small text
            hide screen hermione_main
            m "What was that?"
            call her_main("I'm cumming!","silly","dead")
            hide screen hermione_main
            call nar(">Hermione's hand shoots under her skirt as she starts violently orgasming.")
            call her_main("What's wrong with me [genie_name]?","silly","ahegao")
            hide screen hermione_main
            m "A lot of things [hermione_name], considering you just ate my cum off the ground."
            call her_main("I can't stop cumming...","shock","baseL",cheeks="blush",tears="soft")
            hide screen hermione_main
            call nar(">Hermione loses conciousness.")

    hide screen bld1
    hide screen hermione_main
    call nar(">Hermione is in an unconscious heap on the floor.")

    menu:
        "-Carry her back to her room as is-":
            call nar(">You pick her limp body up and carry her to her room.","start")
            call nar(">As you enter the dormitory you hear her talk in her sleep.","end")
            call her_main("Of course I swallow... just form a line...","open","worriedCl")
            hide screen hermione_main
            call nar(">You place her carefully back into her bed.")
            m "Sleep tight, slut."
        "-Clean her up and take her back to her room-":
            $ uni_sperm = False
            call nar(">You pick her limp body up and carry her to her room.","start")
            call nar(">As you enter the dormitory you hear her mumble in her sleep.","end")
            call her_main("You want a kiss [genie_name]? Of course I don't mind...","open","closed")
            hide screen hermione_main
            call nar(">You place her carefully back into her bed.")
            m "Sleep tight, Hermione."

    call blkfade
    pause.5

    hide screen hermione_main
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_left
    hide screen desk
    show screen genie
    hide screen blktone
    $ addicted = False
    $ uni_sperm = False
    $ aftersperm = False
    call hide_blkfade

    $ hermione_main_zorder = 5

    $ hermione_sleeping = True
    call music_block
    jump night_main_menu






label potion_scene_7: #hyper sensitivity potion
    m "I'd like you to drink a potion today."
    her "Alright then."
    m "Just like that? No putting up a fight or demanding to know what it is?"
    her "Would you tell me what it is?"
    m "No, probably not."
    her "Then why ask?"
    m "Fair enough, here it is."
    menu:
        "-Drop it on her chest-":
            jump potion_scene_7_1
        "-Hand it to her-":
            jump potion_scene_7_2
        "-Drop it on her skirt-":
            jump potion_scene_7_3



### HYPER SENITIVITY POTION ###

label potion_scene_3_2_1: #Hyper sensitive breasts
    call nar(">You fumble with the potion, spilling it over Hermione's front, soaking her shirt through.")
    her "Professor! What were you thinking?"
    call nar(">You place the still half full bottle back on your desk in front of you.")
    m "It was an accident, my hands aren't what they once were."
    her "Ughhh, now I'm going to have to go change before classes."
    her "I expect to be compensated accordingly."
    m "Ok, ok. How about I give you a nice massage to calm you down."
    her "A massage? That's hardly fair compensation!"
    m "Are you sure?"
    her "Positive."
    m "Ok, I'll make a bet with you then."
    her "...{p}Go on..."
    m "I'll start massaging you. If you don't like it after two minutes then you can tell me to stop."
    her "And what do I get for telling you to stop?"
    m "two hundred points."
    her "two hundred points!"
    m "But if you don't ask me to stop I get to massage you for as long as I like, wherever I like."
    her "Deal."
    m "Are you sure?"
    her "No offense [genie_name], but I think I can resist a massage for 200 points."
    m "you sound confident. Care to raise the stakes?"
    her "Are you saying that I can earn more than 200 points?"
    m "five hundred."
    her "{size=+10}Five HUNDRED!{/size}" #size up
    her "Deal."
    m "I haven't even told you what happens if you lose."
    her "it doesn't matter, For 500 points I would turn down a massage from Viktor Krum himself."
    m "Well for the sake of the bet I'll explain anyway."
    m "I expect you to strip naked if you want to be massaged after your two minutes are up."
    her "Naked!"
    m "Only if you lose."
    her "Well I suppose that's OK then, it's not like I'll have to do it."
    m "well are you ready?"
    her "Yes, let's make it quick. I have to go back to the dorms and change after this. My shirt is soaked through."
    call nar(">Hermione walks over and stands in front of you.")
    her "So what's your plan? Do you expect me to give in just because you rub my shoulders?"
    m "Shoulders? Who said anything about shoulders?"
    her "Are you going to grope my butt again?"
    m "No, no. Today we're sticking with the fundamentals."
    call nar(">You grab her breasts through her soaked shirt.")
    her "!!!"
    m "There we are. I'll start the time now shall I?"
    her "What is wrong with me?"
    m "Nothing, apart from underestimating your elders."
    her "My breasts... they're on fire."
    m "If they were I think I would know."
    call nar(">You gently roll her nipples between your thumbs and forefingers.")
    her "!!!"
    her "Please [genie_name], you have to stop."
    m "You're not allowed to ask me to stop until the two minutes are up."
    m "And by my count there's still over a minute and a half to go."
    call nar(">You kneed her breasts firmly.")
    her "I'm calling off the bet..."
    m "Now now, no one likes a quitter."
    her "This isn't a joke, it feels like..."
    her "It feels amazing..."
    m "I told you I'm good."
    her "No [genie_name], this is the best thing I've ever felt."
    her ""

label potion_scene_3_2_2: #Hyper sensitive mouth/throat

label potion_scene_3_2_3: #Hyper sensitive pussy


### HYPNO POTION ###

### FACE NEEDS UPDATE ###
### EYE COLOR NEEDS TO BE CHANGED ###

label potion_scene_3_3_1: #Hypno potion
    m "[hermione_name], I have another special potion for you today."
    call her_main("Who are you even buying these off?","normal","frown")
    m "A good magician never tells."
    call her_main("Magician? You're a wizard, and this better not have any long-term side effects.","normal","frown")
    call her_main("I'm still coughing up fur balls every now again from that polyjuice potion.","normal","frown")
    m "Of course it won't, now would you kindly drink the potion."
    call her_main("...","annoyed","angryL")
    call her_chibi("drink_potion","mid","base")
    with d3
    hide screen hermione_blink
    call nar(">Hermione cautiously starts drinking the potion.")
    call her_main("","cum","worriedCl")
    pause .5
    call her_chibi("stand","mid","base")

    call her_main("This isn't bad at all.","base","squint")
    call her_main("I feel...","base","happyCl")
    m "You feel what?"
    call her_main("I-I feel grea--","annoyed","down")
    call nar(">Hermione's eyes go blank and she stares forward blankly.")
    call her_main("What am I?","grin","dead")
    m "Uhm..."
    m "(Should have thought of something. At least the potion seems to work. Lets see...)"
    menu:
        "-You're an air-headed bimbo-":
            show screen blktone
    #call set_h_hair(hair_style="B",color=2)
    call her_main("I am an airheaded bimbo who only wants to make people happy...","soft","dead")
    menu:
        "-You love being covered in my cum-":
            pass
    $ hermione_badge = "characters/hermione/accessories/badges/cum_badge.png"
    $ hermione_badges = True
    call her_main("I love being covered in your cum...","soft","dead")
    menu:
        "-Your breasts are incredibly sensitive to pleasure-":
            pass
    call her_main("My breasts are incredibly sensitive to pleasure......","soft","dead")
    pause.5

    hide screen blktone
    call nar(">Hermione closes her eyes and appears to nod off.")
    call her_main("......","base","closed")
    call her_main("Where am I?","upset","wink")
    m "You're in my office."
    call her_main("I am?","upset","wink")
    call her_main("How did I get here?","upset","wink")
    m "You walked in here about 2 minutes ago."
    call her_main("Huh, I must have forgotten, silly old me.","base","squint")
    call her_main("So professor, what am I doing here?","base","down")
    call her_main("Aaaaaaah!!!!","shock","worriedCl",cheeks="blush")
    call her_main("What happened to my outfit?!","shock","down_raised")
    call her_main("I can't be seen wearing all this stuff!!!","disgust","down")

    if hermione_wear_top:

        call set_hermione_action("lift_top")
        pause.5

        $ hermione_wear_top = False
        call set_hermione_action("none","skip_update")
        pause.5

        call her_main("That's soooooo much better!","soft","ahegao")

    if hermione_wear_bottom:
        call her_main("It really suuuuucks that I have to wear anything at all in this boring nunnery...","annoyed","ahegao")
        call her_main("(I can still wear something shorter. Like a skirt...)","")
        call her_main("(A reeealy short one!!!{image=textheart}{image=textheart}{image=textheart})","grin","happyCl")

        call set_hermione_action("lift_bottom")
        pause.5

        $ hermione_wear_bottom = False
        call set_hermione_action("none","skip_update")
        pause.5

        call her_main("I bet you like watching me strip mistah{image=textheart}","smile","glance")

    call her_main("I'm not sure what under-thingies I should wear though...","annoyed","down_raised")
    call her_main("Definitely something in pink!!!","smile","happyCl")
    hide screen hermione_main
    call blkfade

    call nar("Hermione pulls out her wand and casts a spell...")

    #Setting up Bimbo clothes.
    $ h_hair_color = 2 #Blonde
    $ h_lipstick = "pink_lipstick"

    $ h_request_wear_top = True
    $ h_top = "top_5_g"

    $ h_request_wear_bottom = True
    $ h_skirt = "skirt_4_low"
    $ h_skirt_color = "purple"

    $ h_request_wear_bra = True
    $ h_bra = "bra_lace"
    $ h_bra_color = "pink"

    $ h_request_wear_panties = True
    $ h_panties = "panties_lace"
    $ h_panties_color = "pink"

    $ h_request_wear_neckwear = True
    $ h_neckwear = "choker_lace"

    $ h_request_wear_stockings = True
    $ h_stockings = "stockings_fishnets"

    call load_hermione_clothing_saves
    call update_her_hair #Always update hair before the uniform! In case she wears cat-ears!
    call update_her_uniform

    pause.5
    call her_main("","base","glance")
    call hide_blkfade
    call ctc

    call her_main("Do you like it mistah?","grin","happyCl")

    menu:
        g9"!!!"
        "-You look amazing!-":
            call her_main("Thank youuuuu!!!{image=textheart}{image=textheart}{image=textheart}","grin","ahegao")
            call her_main("Aaaaanyway...","open","baseL")
            call her_main("Is there anything you want from me mistah... I'll do anything!{image=textheart}","soft","glance")
        "-Where is your badge, cumslut?!-" if I_love_cum_badge_OBJ.unlocked:
            call her_main("Oh no I forgot that!","soft","wide")
            call her_main("I'm soooo sorry!!!","shock","worriedCl",cheeks="blush")
            call her_main("It's this one, isn't it...","soft","down")
            call nar("Hermione conjures an -I {image=textheart} Cum- badge, which magically attaches itself to her breasts.")

            $ h_request_wear_body_accs = True
            $ hermione_body_accs_list = []
            $ hermione_body_accs_list.append("badge_I_love_cum")

            call load_hermione_clothing_saves
            call update_her_uniform

            call her_main("Yay! Do you like it?","grin","happyCl")
            call her_main("Anything else you want from me mistah?... I'll do anything!{image=textheart}","soft","glance")


    m "I'm just going to ask you a few questions."
    call her_main("(...)","annoyed","angry")
    call her_main("(And here I hoped he'd just ask to fuck...)","annoyed","angryL")
    call her_main("(Questions are so boooring! I hope they are at least naughty...)","annoyed","ahegao")
    call her_main("Are those questions going to be hard, mistah?","grin","worriedCl",emote="05")
    call her_main("I don't like hard questions.","grin","worriedCl")
    m "Don't worry they'll be nice and easy for you."
    call her_main("yay!","smile","happyCl")
    m "First question, Who are you?"
    call her_main("That's an easy one! I'm Hermione Granger, the prettiest girl in the whole school!","smile","happyCl",emote="06")
    m "And what are your hobbies?"
    call her_main("Doing my makeup{image=textheart}, dancing{image=textheart} and dressing happy{image=textheart}!","base","happyCl")
    m "Dressing happy?"
    call her_main("You know, wearing nice things to make other people happy!{image=textheart}","base","ahegao_raised")
    m "You like making people happy?"
    call her_main("Of course mistah professor, making people happy{image=textheart} makes me happy{image=textheart}!","smile","happyCl")
    call her_main("Once I finish school I want to get a job where all I do is make people happy{image=textheart}!","base","happyCl")
    m "Ok, final question;"
    m "How would you like to make yourself happy?"
    call her_main("Make myself happy?","annoyed","down")
    call her_main("But I'm already happy, silly!","base","happyCl")
    m "Even happier."
    call her_main("Even happier? {size=+10}YAY!{/size}","smile","happyCl",emote="06")
    call her_main("So how am I going to be happier? Am I going to get naked?","grin","baseL")
    m "That'd be a good start."
    call her_main("{image=textheart}AAAAAAWWWEEESOOOOOOOOMMME!{image=textheart}","grin","ahegao")

    call set_hermione_action("lift_top")
    pause.5

    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call set_hermione_action("none","skip_update")
    pause.5

    call her_main("You know they don't let us walk around naked at school?","annoyed","angryL")
    m "Really? I can't imagine why not."
    call her_main("I know right? It's like so dumb! Everyone would just be happier{image=textheart} if they got to be naked.","soft","ahegao")

    call set_hermione_action("lift_skirt")
    pause.5

    $ hermione_wear_bottom = False
    $ hermione_wear_panties = False
    call set_hermione_action("none","skip_update")
    pause.5

    call her_main("I know everyone who sees me naked is happy!","base","glance")
    m "You've certainly made me happy."
    call her_main("Thanks mistah professor sir! That makes me so happy{image=textheart}!","grin","worriedCl")
    m "(I don't think I can stand her saying the word happy much more...)"
    m "Now Hermione, I want you to touch your breasts."
    call nar(">Hermione moves her hands up to her breasts")
    call set_hermione_action("lift_breasts")

    call her_main("Like this? This feels sooooo gooood!","base","down")
    call her_main("It's like mah hands are moving on their own...","soft","ahegao")
    call her_main("It's soooo goodd but It's weeeiiird... I need something... anything...","open","worriedCl")
    m "Would you like to touch yourself down there?"
    call her_main("Yes mistah [genie_name]. please.","shock","worriedCl")

    menu:
        "-make her beg-":
            m "I want you to beg."
            call her_main("Please mistah sir...","shock","worriedCl")
            m "Please what?"
            call her_main("Ohmigawd Please let me touch myself down there... I'll do anything...","clench","worried",cheeks="blush",tears="soft")
            m "Anything?"
            call her_main("Anything. I just need to feel happy...","silly","worried",cheeks="blush",tears="soft")
            m "Tell me what you are and I'll let you."
            call her_main("I'm Hermione, the school slut.","grin","ahegao")
            m "More."
            call her_main("geez, I'm a dumb bimbo fuckbunny... that just wants to feel happy...","silly","ahegao")
            m "And what makes you happy?"
            call her_main("Making you happy{image=textheart} [genie_name].","silly","dead")
            m "Good girl."
        "-let her touch herself-":
            m "Go on then."
            call her_main("Thank you soooo{image=textheart} much [genie_name]!","silly","ahegao")

    call set_hermione_action("covering")
    call her_main("This is soooo goood","grin","ahegao")
    call her_main("Mistah [genie_name] can you please do something for me?","grin","wink",cheeks="blush")
    m "What's that?"
    call her_main("If it's not tooo much trouble could you...","silly","ahegao")
    call nar(">Hermione starts pinching her nipple.")
    call set_hermione_action("pinch")
    call her_main("could you please cum on me?","open_tongue","ahegao_raised",cheeks="blush")
    m "Well if it makes you happy."
    call nar(">you stand up and head towards her.")
    call her_main("thank you, thank you thank you! You're the best headmaster {size=+5}EVER!{/size}","smile","happyCl",emote="06")

    hide screen hermione_main
    call blkfade

    hide screen genie
    call gen_chibi("jerking_off","desk","base")
    show screen chair_left
    show screen desk

    hide screen blktone
    hide screen bld1
    call hide_blkfade
    call ctc

    call set_hermione_action("covering")
    call her_main("...","base","ahegao_raised")
    call set_hermione_action("pinch")
    call her_main("I don't know how other girls do it...","annoyed","down")
    m "Do what?"
    call her_main("Stop themselves from coming here and getting you to cover them in yummy cummy!","annoyed","down")
    call set_hermione_action("covering")
    call her_main("I mean I can barely stop mahself coming here everyday!","smile","happyCl")
    m "That's it..."
    call set_hermione_action("pinch")
    call her_main("Hmmm, I just luv playin' with mah boobies{image=textheart}{image=textheart}{image=textheart}","base","ahegao_raised")
    call her_main("They're just so soft...","open","ahegao_raised",cheeks="blush")
    call set_hermione_action("covering")
    call her_main("And they feel soo good. They're really sensi--","base","ahegao_raised",cheeks="blush")
    call her_main("Sensi---","base","ahegao_raised",cheeks="blush")
    call set_hermione_action("pinch")
    call her_main("What's the word?","annoyed","ahegao_raised",cheeks="blush")
    m "Sensitive."
    call set_hermione_action("covering")
    call her_main("That's right they're really sensitive!","silly","ahegao_raised",cheeks="blush")
    m "So am I..."
    call her_main("Are you going to cum?","open_tongue","ahegao_raised",cheeks="blush")
    call set_hermione_action("pinch")
    call her_main("Please do it on my face!","open_tongue","ahegao_raised",cheeks="blush")
    call her_main("No wait my tits...","scream","worriedCl",cheeks="blush")
    call set_hermione_action("covering")
    call her_main("No wait my face!","silly","ahegao_raised",cheeks="blush")

    menu:
        "-Cum on her face-":
            g4 "Here it comes slut!"
            call her_main("{image=textheart}!!!{image=textheart}","shock","wide",cheeks="blush")
            call gen_chibi("cumming","desk","base")
            $ u_sperm = "characters/hermione/face/auto_07.png"
            $ uni_sperm = True
            g4 "that's it, all over your face."
            call set_hermione_action("pinch")
            call her_main("...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush")
        "-Cum on her tits-":
            g4 "Here it comes fuckbunny!"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","shock","wide",cheeks="blush")
            call gen_chibi("cumming","desk","base")
            $ u_sperm = "characters/hermione/face/auto_02.png"
            $ uni_sperm = True
            g4 "All over your tits."
            call set_hermione_action("pinch")
            call her_main("It's so warm...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush")
        "-cover her in cum-":
            g4 "Here it comes whore!"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","shock","wide",cheeks="blush")
            call gen_chibi("cumming","desk","base")
            $ u_sperm = "characters/hermione/face/auto_05.png"
            $ uni_sperm = True
            g4 "that's right slut, All over you."
            call set_hermione_action("pinch")
            call her_main("{image=textheart}{image=textheart}{image=textheart}","silly","ahegao_raised",cheeks="blush")

    call gen_chibi("hold_dick","desk","base")
    call her_main("...","grin","ahegao")
    $ hermione_dribble = True
    call her_main("That felt {size=+5}SOOOOO!{/size} good!","silly","ahegao")
    call set_hermione_action("lift_breasts")

    call her_main("Can we do it again! Please! Pretty please! Pretty please with cum on top!","silly","dead")
    m "Not today."
    call her_main("Awwwwww.","shock","worriedCl")

    hide screen hermione_main
    call blkfade

    call gen_chibi("hide")
    hide screen chair_left
    hide screen desk
    show screen genie
    call her_chibi("stand","desk","base")
    call hide_blkfade

    call her_main("Well ok... I suppose I'll head to class then.","open","down")
    m "About that. I think it'd be better if you went back to your dorm."
    call her_main("Why's that mistah [genie_name] sir?","annoyed","base")
    m "I think you need to have a little nap and let this wear off."
    call her_main("whatever you say sir!","annoyed","closed")
    call set_hermione_action("none","skip_update")
    call her_main("And thanks again!{image=textheart} You're the best!","smile","happyCl",emote="06")

    call her_walk("desk","leave",2.5)

    m "(Maybe I should have told her to get dressed first...)"

    $ pink_lipstick_OBJ.unlocked = True #Unlocks pink lipstick.
    call give_reward(">Hermione can now use pink lipstick!","interface/icons/lipstick_pink.png") #Need lipstick shop image!

    call reset_hermione_main

    $ hermione_takes_classes = True
    call music_block
    jump day_main_menu


### AHEGAO POTION ###

label potion_scene_3_4_1:
    m "How long until your next class [hermione_name]?"
    call her_main("about fifteen minutes sir.","open","base")
    m "in that case I think you might have to be a little late."
    call her_main("what? why?","open","worried")
    g4 "Well, it might be a bit hard for you to attend class with my cock buried in your tight little pussy."
    call her_main("Oh...","soft","squintL")
    m "That's not going to be a problem is it [hermione_name]?"
    call her_main("of course not [genie_name]! Let me just take my clothes off...","grin","ahegao")

    show screen blkfade
    with d3
    hide screen bld1
    hide screen hermione_blink
    #SEX
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_main("ahhhhhhhhh....{image=textheart}","scream","wide")
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ ccg_folder = "herm_sex"
    $ ccg1 = "blank"
    $ ccg3 = "blank"
    $ ccg2 = 1
    show screen ccg
    hide screen blkfade
    with d3
    her "Ah...{image=textheart}"
    g4 "mmmm, you like that don't you slut?"
    $ ccg2 = 2
    her "yes...{image=textheart}"
    $ ccg2 = 3
    her "even though I have to miss class..."
    $ ccg2 = 4
    her "I Honestly don't care...{image=textheart}"
    $ ccg2 = 5
    her "This just feels too goooood..."
    pause
    ">You quietly pull out the small vial from your pocket and pull the stopper out."
    $ ccg2 = 6
    her "Mmmm, don't slow down [genie_name]..."
    g4 "You asked for it!"
    ">You speed up the pace as you go to pour a drop onto her ass, your hand barely managing to stay stable..."
    $ ccg2 = 7
    her "Harder [genie_name]!!!"
    pause
    ">You feel hermione suddenly push her pussy back towards you, causing you to spill about a quarter of the vial onto her ass..."
    $ ccg3 = "p1"
    m "..."
    $ ccg2 = 8
    her "What was that?"
    m "Ugh... nothing... just a bit of spit. Keep going slut."
    $ ccg2 = 9
    her "Ah...{image=textheart} alright then..."
    ">You quickly put the stopper back into the vial and slip it back into your robes."
    $ ccg2 = 10
    her "Ah... ah... ah..."
    pause
    $ ccg2 = 11
    her "[genie_name], you think you could... ah..."
    g4 "What is it slut?"
    $ ccg2 = 12
    her "Could you please... spank me... ah...?"
    g4 "of course!"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    ">You give her ass a hard spank, accidentally causing the potion to explode out from underneath your hand, coating her even more."
    $ ccg3 = "p2"
    $ ccg2 = 13
    pause
    her "{size=+10}!!!{/size}"
    ">Hermione's sopping cunt starts contracting around your cock uncontrollably."
    g4 "Mmmm, cumming already slut?"
    $ ccg2 = 14
    her "Y-yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 15
    her "I{image=textheart} can't{image=textheart} stop..........{image=textheart}{image=textheart}{image=textheart}"
    ">True to her word, you don't feel an end to her relentless spasming."
    g4 "I love it when cum on my cock whore!"
    $ ccg2 = 16
    pause
    her "no...{image=textheart} sir...{image=textheart} you...{image=textheart} don't...{image=textheart} understand...{image=textheart}"
    $ ccg2 = 17
    her "It...{image=textheart} won't...{image=textheart} stop...{image=textheart}"
    g4 "I don't see how that's my problem!"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    ">You give her ass another hard slap, savoring the feeling of another orgasm flowing through the young witch."
    $ ccg2 = 18
    her "{size=+10}!!!{/size}"
    $ ccg2 = 19
    her "its......{image=textheart} {image=textheart} "
    $ ccg2 = 20
    pause
    her "my{image=textheart}  whole{image=textheart}  body...{image=textheart}{image=textheart}{image=textheart} "
    g4 "Speak up slut!"
    $ ccg2 = 21
    her "My body's...{image=textheart} {image=textheart} on fire..."
    $ ccg2 = 22
    her "I can't...{image=textheart}"
    $ ccg2 = 23
    her "why...{image=textheart}"
    $ ccg2 = 24
    her "Why {image=textheart}does {image=textheart}it {image=textheart}feel {image=textheart}this {image=textheart}goooooooooood...{image=textheart}{image=textheart}{image=textheart}"
    g4 "enjoying yourself are we?"
    $ ccg2 = 25
    her "No...{image=textheart} ah... yesssss....{image=textheart}"
    $ ccg2 = 26
    her "it's like...{image=textheart}"
    $ ccg2 = 27
    her "each time you thrust...{image=textheart}{image=textheart} that big fat {image=textheart}cock{image=textheart} in me...{image=textheart}"
    $ ccg2 = 28
    pause
    her "it's like I {image=textheart}{image=textheart}cum{image=textheart}{image=textheart}..."
    her "But it never resets..."
    $ ccg2 = 29
    her "Each time is just another stronger {image=textheart}orgasm{image=textheart}..."
    $ ccg2 = 30
    her "{size=+10}AND{image=textheart} THEY{image=textheart} NEVER{image=textheart} STOOO{image=textheart}OOOP!!!!!!"
    g4 "Sounds nice... and what about when I give your fat ass a nice... slap?"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    ">You give her ass another hard slap, holding your hand against her warm flesh, swirling the potion around underneath it."
    $ ccg2 = 31
    her "{size=+20}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{/size}"
    $ ccg2 = 32
    her "{image=textheart}my{image=textheart} {image=textheart}brain...{image=textheart}"
    $ ccg2 = 33
    her "You're{image=textheart} going{image=textheart} to{image=textheart} kill{image=textheart} me...{image=textheart}"
    g4 "Stop being so overdramatic..."
    pause
    $ ccg2 = 34
    her "I'm not...{image=textheart}"
    her "Ah.....{image=textheart} some....{image=textheart} thing....{image=textheart} is....{image=textheart} wrong....{image=textheart}"
    ">Hermione's words start to slow, eventually only being able to mutter a squeak of a word every time you thrust into her."
    g4 "Maybe it was the potion I poured all over your ass earlier?"
    $ ccg2 = 35
    her "{size=+20}{image=textheart}{image=textheart}what?{image=textheart}{image=textheart}{/size}"
    g4 "Don't worry, the effects should wear off in about an hour..."
    $ ccg2 = 36
    her "{size=+20}!!!!!!!{/size}"
    g4 "In the mean time, why don't you just sit back and enjoy the ride."
    $ ccg2 = 37
    her "{image=textheart}e-e-enjoy....{image=textheart}"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    $ ccg2 = 38
    pause
    her "{size=+20}!!!!!!!{/size}"
    $ ccg2 = 39
    her "Pleeeease...{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 40
    her "my...{image=textheart}mind...{image=textheart}is...{image=textheart}breaking...{image=textheart}"
    ">You start to pick up the pace, treating her as nothing more than your mewling fuckmeat..."
    g4 "MMMM, you always know what to say to get me going!!"
    $ ccg2 = 41
    her "...{image=textheart}{image=textheart}{image=textheart}"
    ">Eventually the endless spasming of her drenched pussy around your cock proves too much."
    g4 "Ah!!! Here It comes whore!"
    $ ccg2 = 42
    pause
    her "{image=textheart}........{image=textheart}"
    ">You start firing cum directly into her womb."
    $ ccg3 = "s4"
    $ ccg2 = 43
    pause
    her "{image=textheart}!!!{image=textheart}"
    g4 "TAKE THIS!!!"
    $ renpy.play('sounds/slap.mp3')
    show screen white
    pause.1
    hide screen white
    with hpunch
    ">You give her ass one last slap, stinging your hand as you shoot the last rope into her waiting cunt."
    $ ccg3 = "s5"
    $ ccg2 = 44
    pause
    her "{image=textheart}........{image=textheart}"
    her "{image=textheart}...............{image=textheart}"
    $ ccg2 = 45
    pause
    her "{image=textheart}.......................{image=textheart}"
    show screen blkfade
    with d3
    ">Eventually hermione's eyes roll back into her head as she collapses forward onto your desk."
    ">you carry her unconscious body back to her room to sleep the last of the potion off."
    hide screen ccg
    hide screen hermione_main
    hide screen hermione_blink
    show screen genie
    hide screen blkfade
    with d3

    $ hermione_takes_classes = True
    call music_block
    jump day_main_menu
