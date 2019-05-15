

### Flirt with the other Quidditch players ###

# Start
label cc_pr_flirt_start: # Not in use.

    # Intro
    if cc_pr_flirt.points == 0:
        m "[cho_name], to continue your training I'll need you to get more involved with the other players."
        cho "With whom? The Hufflepuff team?{w} Gryffindor?"
        g9 "No, our focus will be on your own team!"
        cho "Ravenclaw?"
        g9 "Remember when you told me you shower with them?"
        cho "And I whole heartedly regret it."
        g9 "It gave me an idea!"
        cho "What is it?"
        g9 "I need you to bond with them more! Acquire a deeper connection to your fellow team-mates!"
        cho "I can see why that would be benefitial to us. To strengthen our camaradery..."
        m "Yeah yeah... That's what I was going for."
        cho "And how would you suggest I do that, [cho_genie_name]?"
        g9 "Do what you girls do best! Flirt with them!"
        cho "Flirting? With my team?" # Shocked
        cho "[cho_genie_name], I don't think I can do that."
        cho "I've known them for years!{w} They'd just think I'm acting weird..."
        m "Just try it once, and we'll see what happens."
        cho "I'd rather not."
        m "If you question my methods, we might as well stop right here and you can say your Quiddtch-cup goodbye!"
        cho "(...)"
        cho "Very well, [cho_genie_name]."
        cho "But if they laugh or make fun of me we'll stop this at once!"
        m "Fine by me."
        m "Return to my office after classes and tell me how it went."
        cho "Ok, [cho_genie_name]."
        cho "See you after classes..."
        g9 "Off you go!"

    # Repeated
    else:
        m "I need you to have an eye on the other Quiddich players again."
        g9 "Flirt with them a little bit. See how they behave around you..."
        cho "Of course, Sir."
        m "Please return after classes to tell me about it."
        cho "Of course!"
        g9 "Now, off you go!"
        cho "See you later, [cho_genie_name]."

    call cho_walk(action="leave", speed=1.6)

    $ cc_pr_flirt.inProgress = True

    # Stats
    $ cc_pr_flirt.counter += 1

    jump end_cho_event


label event_class_test:
    menu:
        "-Start event-":
            $ cc_pr_flirt.start()
        "-Set event tier-":
            $ cc_pr_flirt.tier = int(renpy.input("Tier (0-2):", str(cc_pr_flirt.tier), "0123456789", length=1))
            jump event_class_test
        "-Display current tier values-":
            python:
                tmp_values_display = cc_pr_flirt.events[cc_pr_flirt.tier]
            "{size=-5}[tmp_values_display]{/size}"
            jump event_class_test
        "-Reset all flags-":
            $ cc_pr_flirt.tier = 0
            python:
                for i in xrange(cc_pr_flirt.max_tiers):
                    for j in xrange(len(cc_pr_flirt.events[i])):
                        cc_pr_flirt.events[i][j][1] = False
            jump event_class_test
        "Exit":
            jump main_room



# Ideas

### Tier 1 ###

# Intro:
# Cho was unsuccessful with flirting and gets angry at Genie. # cho "What did you think would happen?"
# Cho meets Cedric who asks her out on a date. She declines. Genie tells Cho to tease him more next time.
# She stumbles upon Hermione who interrogates Cho on the spot.

label cc_pr_flirt_T1_intro:
    $ cc_pr_flirt.level = 1

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the intro {color=#80ff00}Tier1{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event

# Random/Repeatable:
# Cho flirts with a member of her team but it gets awkward.
# Cho gets called a bro by one of her team members and she got angry about it.
# Cho again meets Cedric. She teased him by showing him her panties, lifting her skirt.

label cc_pr_flirt_T1_E1:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the {color=#5490b5}first{/color} event in {color=#80ff00}Tier1{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event

label cc_pr_flirt_T1_E2:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the {color=#ffae19}second{/color} event in {color=#80ff00}Tier1{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event


### Tier 2 ###

# Intro:
# Hermione stalks her.
# Cho meets Malfoy. She flashes her panties at him but he was unimpressed. Genie wonders if he maybe isn't into panties.

label cc_pr_flirt_T2_intro:
    $ cc_pr_flirt.level = 2

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the intro {color=#80ff00}Tier2{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event

# Random/Repeatable:
# Cho gets a polite kiss on her cheek by her team captain.

label cc_pr_flirt_T2_E1:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the {color=#ffae19}first{/color} event in {color=#8000ff}Tier2{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event

label cc_pr_flirt_T2_E2:

    # Cho enters.
    call cho_walk(action="enter", speed=1.6)

    "This is the {color=#e42e4e}second{/color} event in {color=#8000ff}Tier2{/color}"



    # Cho leaves.
    call cho_walk(action="leave", speed=1.6)

    jump end_cho_event


### Tier 3 ###

# Intro:
# Cho meets Harry.
# Che meets Ginny. Ginny is teasing Cho actually and she's embarrassed about it.

# Random/Repeatable:
# Cho again tries to flaunt Harry. Maybe he could compliment her ass?
# Ginny watches her while doing squads.They have a little Chat. Ginny reveals that she likes Cho.
