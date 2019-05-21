label genie_house_elf:
    show screen blkfade
    call room("main_room")
    $ temp_day = daytime
    $ temp_color = interface_color
    $ temp_weather = weather_gen
    $ daytime = True
    $ interface_color = "gold"
    $ weather_gen = 1
    $ show_weather()
    call music_block
    with d3

    pause 0.3
    hide screen blkfade
    with d3

    nar "This story takes place in between the introduction of Snape and first meeting Hermione."
    nar "The genie, the desk and the door:"
    nar "How does that door work? The genie thought."

    m "\"How do the people know I’ve summoned them? I don’t have a secretary...that I know of anyway.\""

    m "Have they been keeping a secretary from me? I should ask Sn..."

    nar "Snape then opened the door, his pointy nose protruding under his silky hair."

    call sna_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call sna_main("You called? ","snape_23", xpos="base", ypos="base")

    nar "Snape said with a smirk, doing his best to hide his amusement."

    g11 "How did you, how do you..."
    m "This door, how does it work?"

    nar " The genie said, now even more frustrated. "
    nar "The genie wasn’t used to this... this unfamiliar magic."
    nar "He was used to knowing the ins and outs of the universe. But this world, it was to alien to him..."
    nar "At least he knew things about aliens..."

    call sna_main("Well, you’re the headmaster are you not? ","snape_06", xpos="base", ypos="base")

    nar "Snape said as if that meant anything."

    nar "A look of confusion spread across the genies face which only made Snape smirk even more."
    nar "He then composed himself after seeing this unusual expression on the headmasters face."

    call sna_main("I keep forgetting that you don’t know these things.","snape_01", xpos="base", ypos="base")
    call sna_main("students learn it on day one.","snape_01", xpos="base", ypos="base")
    call sna_main("The headmaster is in control of the school and its inhabitants.","snape_24", xpos="base", ypos="base")

    nar "Snape said in a matter of fact sort of way."

    m "I know that, we have schools in my world too."
    m "But generally we don’t wave wooden sticks around yelling random words."

    nar "Snape flinched, as if the notion of magic consisting of waving a wand and yelling random words was utterly absurd."

    call sna_main("No. You’re literally in control over the school....look.","snape_08", xpos="base", ypos="base")

    nar "Snape says, pulling his wand out, waving it."

    call sna_main("Revelio!","snape_01", xpos="base", ypos="base")
    call sna_main(remove=True)

    nar "After a flash of light and a small pop a house elf appears in the corner of the room."

    call helf_main(" ")

    g5 "What the hell is that?"

    nar "The genie said, jumping onto the desk as if things appearing out of thin air was new to him."

    call helf_main(remove=True)

    call sna_main("That...is a house elf.","snape_01", xpos="base", ypos="base")

    m "A house...elf."
    g10 "Is that like a Santa's elf? "

    nar "The genie said, now climbing down to sit on his chair."

    call sna_main("Sort of, they don’t get paid so they do have that in common...","snape_05", xpos="base", ypos="base")

    nar "Snape muttered under his breath..."

    call sna_main("The houses elves here can send us messages so we can go where we're needed.","snape_05", xpos="base", ypos="base")

    call sna_main("He just sits here invisible during the day and cleans and eats at night.","snape_01", xpos="base", ypos="base")

    m "The house elf cleans?"
    m "I thought I had some sort of magic self cleaning desk..."

    nar "The genie said sheepishly."
    call sna_main(remove=True)

    call helf_main("No sir...")

    nar "Said the elf, trying its hardest to bite his tongue but failing."

    call helf_main("I see it all, I clean it all....every...last bit of it.")
    call helf_main(remove=True)

    call sna_main("...","snape_08", xpos="base", ypos="base")

    nar "After a few moments Snape turned around, started walking towards the door and said."

    call sna_main("If that is all, I’ll be in the dungeons.","snape_01", xpos="base", ypos="base")
    call sna_main("I’ve been working on a new cleaning solution.","snape_01", xpos="base", ypos="base")
    call sna_main("It might come in handy sooner than I thought.","snape_02", xpos="base", ypos="base")

    call sna_walk(action="leave", speed=2)

    nar "The door shut and silence spread across the room only interrupted after a few minutes by the house elf."

    call helf_main("So, should I turn invisible again sir?")

    m "Yes...yes that will be for the best."
    call helf_main(remove=True)
    "The end."
    
    $ daytime = temp_day
    $ interface_color = temp_color
    $ weather_gen = temp_weather
    $ show_weather()

    call room(hide_screens=True)
    jump enter_room_of_req