init python:
    # Function to add a section to the credits
    def addSection(credits_text, title, names):
        # Add the section title to the credits
        credits_text += "{k=5.0}{size=+15}{outlinecolor=#842500}{color=#f9a001}{{" + title + "}{/color}{/outlinecolor}{/size}{/k}\n\n"
        # Add all of the names in the section to the credits
        for name in names:
            credits_text += "{k=1.5}" + name + "{/k}\n"
        # Add some extra newlines to the credits
        credits_text += "\n"

        return credits_text

label credits:    
    python:
        # Variables to control and setup the credits text
        credits_duration = 30.0
        credits_text = "{image=logo/title.png}\n\n"

        credits_artists = ("Soggy", "DostojevskijSTG", "LoafyLemon", "Noodle")
        credits_writers = ("Johnny", "Mo")
        credits_programmers = ("Asease1", "LoafyLemon", "TropeCode")
        credits_music = ("Harry Potter OST\n{size=-5}{color=#808080}{k=0.7}\"Prologue\"\n\"Shanghai Honey\"\n\"Introducing Colin\"\n\"Neville's Waltz\"\n\"The Quidditch Match\"{/k}{/color}{/size}\n", "Kevin MacLeod\n{size=-5}{color=#808080}{k=0.7}\"Anguish\"\n\"Awkward Meeting\"\n\"Brittle Rille\"\n\"Chipper Doodle v2\"\n\"Dark Fog\"\n\"Despair\"\n\"Game Over Theme\"\n\"Boss Theme\"\n\"Hitman\"\n\"Music for Manatees\"\n\"Plaint\"\n\"Fuzzball Parade\"\n\"Teddy Bear Waltz\"\n\"Scheming Weasel (Slower version)\"\n\"Open Those Bright Eyes\"\n\"Wallpaper\"{/k}{/color}{/size}\n", "PhobyAk\n{size=-5}{color=#808080}{k=0.7}\"Under-the-radar\"{/k}{/color}{/size}\n", "Shadow16nh\n{size=-5}{color=#808080}{k=0.7}\"Playful Tension (Orchestral)\"{/k}{/color}{/size}\n", "controllerhead\n{size=-5}{color=#808080}{k=0.7}\"Item Shop\"{/k}{/color}{/size}\n", "jrayteam6\n{size=-5}{color=#808080}{k=0.7}\"Grape Soda is Fucking Raw\"{/k}{/color}{/size}\n", "Juhani Junkala\n{size=-5}{color=#808080}{k=0.7}Retro Game Music Pack:\n\"Title Screen\"\n\"Level 1\"\n\"Level 3\"{/k}{/color}{/size}")
        credits_special = ("{size=+4}Akabur{/size}\n{color=#808080}{size=-5}{k=0.7}Creator of the original Witch Trainer and other awesome games! {a=https://www.patreon.com/akabur}PATREON{/a}{/size}{/color}\n{/k}", "Dr. Lupin", "Lineup", "MaiL", "MedicBear", "STG Anon", "Boom313", "Sandmaster", "Pinguino", "UE Crew", "Catbug", "CaptainNemo", "Artguy", "Linear", "Amadan", "Anons", "Heretic", "Maverick", "Cleanzo", "Techy", "Zuel32", "Darwin7")
        
        # Start
        credits_text = addSection(credits_text, "Director", ["MadMerlin"])
        credits_text = addSection(credits_text, "Artists", credits_artists)
        credits_text = addSection(credits_text, "Writers", credits_writers)
        credits_text = addSection(credits_text, "Programmers", credits_programmers)
        credits_text = addSection(credits_text, "Music", credits_music)
        credits_text = addSection(credits_text, "Special Thanks", credits_special)
        
        credits_text += "\nSpecial thanks to our fans, discord moderators and {a=https://www.patreon.com/SilverStudioGames/}patreon supporters{/a} {image=images/misc/heart.png}\n\n\n"
        credits_text += "{image=logo/silverstudiogames.png}\n\n"
        credits_text += "\n{space=220}{image=characters/genie/mage9.png}{rb}{space=-60}Thank you for playing!{/rb}"

    show screen credits_screen
    with dissolve
    call update_interface_color("gray")
    $ achievement.unlock("Credits")
    $ renpy.pause(credits_duration)
    hide screen credits_screen
    with dissolve

    jump main_menu_screen
    
transform credits_scroll:
    subpixel True
    ypos absolute(20)
    time 2.0
    linear credits_duration-7 ypos absolute(-1470)
    
screen credits_screen(mainmenu=True):
    tag credits
    zorder 10

    button:
        if mainmenu:
            action MainMenu()
        else:
            action NullAction()
        style "empty"
    add "interface/blackfade.png"
    
    text "{color=#FFF}[credits_text]{/color}" xalign 0.5 xpos 540 text_align 0.5 outlines [(2, "#000", 0, 0)] at credits_scroll