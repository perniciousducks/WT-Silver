init python:
    # Function to add a line to the credits
    def addLine(credits_text, line):
        # Add the line to the credits
        credits_text += line + "\n\n"

        return credits_text

    # Function to add a section to the credits
    def addSection(credits_text, title, names):
        # Add the section title to the credits
        credits_text += "{size=+10}" + title + "{/size}\n\n"
        # Add all of the names in the section to the credits
        for name in names:
            credits_text += name + "\n"
        # Add some extra newlines to the credits
        credits_text += "\n"

        return credits_text

label credits:    
    python:
        # Variables to control and setup the credits text
        credits_duration = 40.0
        credits_text = "{image=logo/silverstudiogames.png}\n\n"

        # Text for artists credits
        credits_team = ["MadMerlin: {size=-5}Lead writer, QA Lead, Coder, Editor.{/size}", "Soggy: {size=-5}Lead Artist.{/size}", "Asease1: {size=-5}Lead Coder.{/size}", "DostojevskijSTG: {size=-5}Artist.{/size}", "Johnny: {size=-5}Writer, Editor, Designer, QA.{/size}", "LoafyLemon: {size=-5}Artist, C{s}o{/s}der, Designer.{/size}", "Dr. Lupin: {size=-5}Networking, Management and Administration.{/size}", "Lineup: {size=-5}Moderator, tester{/size}", "Mo: {size=-5}Writer, coder.{/size}"]
        credits_text = addSection(credits_text, "-Current Team-", credits_team)
        
        credits_additional = ["Akabur: {size=-5}Creator of the original Witch Trainer and other awesome games! {a=https://www.patreon.com/akabur}PATREON{/a}{/size}", "STG Anon: {size=-5}Coding.{/size}", "Booom313: {size=-5}Android Port. {a=https://www.patreon.com/booom313}PATREON{/a}{/size}", "Sandmaster: {size=-5}Assistant management, Networking and Moderation.{/size}", "Pinguino: {size=-5}Support, QA, Being a penguin.{/size}", "UE Crew: {size=-5}Tutoring and additional assets.{/size}", "Catbug: {size=-5}Writing, Coding and face emotion selection.{/size}", "CaptainNemo: {size=-5}Art (Luna).{/size}", "Artguy: {size=-5}Art (HeartDancer outfit and Weasley Twins).{/size}", "Linear: {size=-5}Art (Outfits).{/size}", "Heretic: {size=-5}Writing (Custom Events).{/size}", "Maverick", "Cleanzo: {size=-5}Coding (Helped with python methods).{/size}", "Techy: {size=-5}Art (Outfit).{/size}", "Amadan: {size=-5}Art (Madam Mafkin and some of the chibi scenes).{/size}", "Anons: {size=-5}Art and other stuff.{/size}", "MaiL: {size=-5}Tester of the cardgame{/size}", "Lineup: {size=-5}Recolored clothing, tester of the cardgame{/size}"]
        credits_text = addSection(credits_text, "-Additional Credits-", credits_additional)
        
        credits_text += "\nSpecial thanks to our fans, testers and {a=https://www.patreon.com/SilverStudioGames/}patreon supporters{/a} {image=images/misc/heart.png}\n\n\n"
        credits_text += "{size=-5}If you feel like you have contributed to this project and would like recognition\nplease email us at {a=mailto:silverstudiogamesofficial@gmail.com}silverstudiogamesofficial@gmail.com{/a}{/size}"
        credits_text += "\n\n\n{image=characters/genie/mage9.png}"

    show screen credits_screen
    with dissolve
    $ interface_color = "gray"
    $ achievement.unlock("Credits")
    $ renpy.pause(credits_duration)
    hide screen credits_screen
    with dissolve

    jump main_menu_screen
    
transform credits_scroll:
    subpixel True
    ypos absolute(20)
    time 2.0
    linear credits_duration-7 ypos absolute(-330)
    
screen credits_screen():
    tag credits
    zorder 10

    button:
        action MainMenu()
        style "empty"
    add "interface/blackfade.png"
    
    text "{color=#FFF}[credits_text]{/color}" xalign 0.5 xpos 540 text_align 0.5 at credits_scroll