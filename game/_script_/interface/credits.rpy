init python:
    def credits_title(title):
        return "{k=5.0}{size=+15}{outlinecolor=#842500}{color=#f9a001}{{" + title + "}{/color}{/outlinecolor}{/size}{/k}\n"
    
    def credits_group(*lines):
        return "".join(map(lambda x: "{k=1.5}"+x+"{/k}\n", lines))

define credits_text = "\n".join([
    "{image=logo/title.png}{vspace=200}",
    credits_title("Director"),
    credits_group("MadMerlin"),
    credits_title("Artists"),
    credits_group("Soggy", "DostojevskijSTG", "LoafyLemon", "Noodle"),
    credits_title("Writers"),
    credits_group("Johnny", "Mo"),
    credits_title("Programmers"),
    credits_group("Asease1", "LoafyLemon", "TropeCode"),
    credits_title("Music"),
    credits_group(
        "Harry Potter OST\n{size=-5}{color=#808080}{k=0.7}\"Prologue\"\n\"Shanghai Honey\"\n\"Introducing Colin\"\n\"Neville's Waltz\"\n\"The Quidditch Match\"{/k}{/color}{/size}\n",
        "Kevin MacLeod\n{size=-5}{color=#808080}{k=0.7}\"Anguish\"\n\"Awkward Meeting\"\n\"Brittle Rille\"\n\"Chipper Doodle v2\"\n\"Dark Fog\"\n\"Despair\"\n\"Game Over Theme\"\n\"Boss Theme\"\n\"Hitman\"\n\"Music for Manatees\"\n\"Plaint\"\n\"Fuzzball Parade\"\n\"Teddy Bear Waltz\"\n\"Scheming Weasel (Slower version)\"\n\"Open Those Bright Eyes\"\n\"Wallpaper\"{/k}{/color}{/size}\n",
        "PhobyAk\n{size=-5}{color=#808080}{k=0.7}\"Under-the-radar\"{/k}{/color}{/size}\n",
        "Shadow16nh\n{size=-5}{color=#808080}{k=0.7}\"Playful Tension (Orchestral)\"{/k}{/color}{/size}\n",
        "controllerhead\n{size=-5}{color=#808080}{k=0.7}\"Item Shop\"{/k}{/color}{/size}\n",
        "jrayteam6\n{size=-5}{color=#808080}{k=0.7}\"Grape Soda is Fucking Raw\"{/k}{/color}{/size}\n",
        "Juhani Junkala\n{size=-5}{color=#808080}{k=0.7}Retro Game Music Pack:\n\"Title Screen\"\n\"Level 1\"\n\"Level 3\"{/k}{/color}{/size}"
    ),
    credits_title("Special Thanks"),
    credits_group(
        "{size=+4}Akabur{/size}",
        "{color=#808080}{size=-5}{k=0.7}Creator of the original Witch Trainer and other awesome games! {a=https://www.patreon.com/akabur}PATREON{/a}{/size}{/color}{/k}\n",
        "Dr. Lupin", "Lineup", "MaiL", "MedicBear", "STG Anon", "Boom313", "Sandmaster", "Pinguino", "UE Crew", "Catbug", "CaptainNemo", "Artguy", "Linear", "Amadan", "Anons", "Heretic", "Maverick", "Cleanzo", "Techy", "Zuel32", "Darwin7"
    ),
    credits_title("Original Credits"),
"""The following credits are from the original Witch Trainer game, and are not affiliated in any way with Witch Trainer Silver.

{color=#e5e297}-{{Written and directed by}-{/color}
{color=#cbcbcb}AKABUR{/color}

{color=#e5e297}-{{Head programmer}-{/color}
{color=#cbcbcb}AKABUR{/color}

{color=#e5e297}-{{Artwork by}-{/color}
{color=#cbcbcb}AKABUR{/color}

{color=#e5e297}-{{Additional Artwork}-{/color}
{color=#cbcbcb}DAHR{/color}

{color=#e5e297}-{{Texts proofread and edited by}-{/color}
{color=#cbcbcb}LYK.D9 (aka Silentchill){/color}

{color=#e5e297}-{{Technical advisor}-{/color}
{color=#cbcbcb}XALJIO{/color}

{color=#e5e297}-{{Game testers}-{/color}
{color=#cbcbcb}XALJIO\nLYK.D9\nDAHR\nAKABUR{/color}

{color=#e5e297}-{{Personal thanks to}-{/color}

{color=#cbcbcb}Dahr{/color}
{size=-5}{color=#e5e297}for still working for me pretty much free of charge, for inspiring me to keep on going and simply for being a good friend and colleague. {/color}{/size}

{color=#cbcbcb}Xaljio{/color}
{size=-5}{color=#e5e297} for not only being my personal \"Ren'Py\" consultant but also an extremely thorough game-tester.{/color}{/size}

{color=#cbcbcb}Lyk.D9 (a.k.a. Silentchill){/color}
{size=-5}{color=#e5e297}for toiling tirelessly over my texts full of typos and broken grammar.{/color}{/size}

{color=#cbcbcb}Bookfisher{/color}
{size=-5}{color=#e5e297}For everything.{/color}{/size}

{color=#cbcbcb}The fate (universe or higher power){/color}
{size=-5}{color=#e5e297}For giving me an opportunity to release another game while retaining complete creative freedom.{/color}{/size}

{size=-2}{color=#cbcbcb}A whole bunch of other people who helped me with development of this game in one way or another, but who I forgot to mention.{/color}{/size}
{size=-2}{color=#cbcbcb}And of course everyone else who supports me and my work.{/color}{/size}

{color=#e5e297}-{{Funding}-{/color}
{size=-2}{color=#cbcbcb}This is not a commercial video game. The entire project was independently funded solely through {a=https://www.patreon.com/akabur}Patreon{/a} and by \"Hentai United\" subscribers.{/color}{/size}

{color=#e5e297}-People who supported development of this game with extraordinary amount of money-{/color}
{size=-5}{color=#cbcbcb}Lawrence Dash, Wirefull, Dorago, Benoit Yan Larose, Talisca{/color}{/size}

{color=#e5e297}-\"INVESTOR\" pledges-{/color}
{size=-5}{color=#cbcbcb}Ace, Linus Furtenbach (Bluue), Eduardo Pereira Carneiro, Vicente Sampedro Burgos, Morning Dawnstar, Wolo, John Layon, stefan mitrano, Gavin Spears, sergio.{/color}{/size}

{color=#e5e297}-\"AGENT\" pledges-{/color}
{size=-5}{color=#cbcbcb}Cameron MacDowell, Zarsher, Guynonymous, Nerzha, Silvanus2004, Xipomus, Carpy Rex, Adler, Deitan-Baruch St-Amand, Martin Neal, wetrx, mark howard, Kenneth Aguilar, alt, David McClellan, Leo H Wilkin, Thorn, TheDudeAbides, Alexandre Rouleau, thomas taylor, Alexander, Redmoonx22, Valdee, Alexander Lykke Landkildehus, Lucas Ferrari, Dom, derek zhang,Charlatan, Preston C T, waylan, Forrest, Loopy, JohnnyBB, Phantom Void, Kyaa, Stephen Richardson, mark herzog, will newton, Sascha Klug, Joshua McDonald, Undying S, John Cawley III, KitsuneEyes, Slingthatcat, Kieran James, Homod saleh al-shammri, randomuser89, Paul Keating, Antonio B, Marko, Tobias, Akhil Chokshi, Smiling_Jack, Clif Morgan, Derek Heynsbergen, Jack Cartwright, Damien Zaid, callmemusashi Mozambiqued, Nemesis Valentine Vanyar, Stalker, Jason, 4nubis, Curtis, Michael Simon, AB, The Wanderer (Mark Hawker), paul, JEB, Voe, Aselobar, Elgrangato82, froste, YllegaL, Bisongun, Skye Tomlinson, Parad0x, Eric Chen, Destiny, Podchamawa Petrovitch, Will, lc, Sathyan Mathai, Lisandro Gil, bill tedd, Tommy Turner, Marcel Kral, Oric13, Ren Ashjiro, anthony donihee, Honey Withers, Christopher, TofuCats, Drake King, Bookfisher Herring, Dustpan, dusty parrott, Bjorn, Robert Jolly, wilson yang, Tudor G, Arzaz, Etienne Ngo, xazathothx, Robert L Schliff, RO, DavidB, Daedilus, david green, Matt, Ketil, ALEXANDER KOVALEV, Oa, John, PG, largo_leet, David, Artemsgvozdem, heyPert.{/color}{/size}

{color=#e5e297}-\"REBEL\" pledges-{/color}
{size=-5}{color=#cbcbcb}1234ghumm, A. R., AJ Ferolie, Catalyst Greenhorn, Abraham Benitio, Actafool812, Adam, Casax5, Adam, FearTheDee, Akasection, Alejandro Luna, Aleksandr, Alex Odoul, Alex P., Alexander Randolph, Maidaniuk Yurii, Alexander, Alexei, Alkosh, Allan Pineda, Altagar, Andreas Janning, Andrei Kuz, Andrey Nikolaev, Anton Belyankin, Anton Tropicflames, Antonio Jos Mucoz Gonzalez, Antonio Rivera, Artur Kevorkov, Baran, BearPerson, BeepBep, Benjamin Drew, Bernard Winters, Bob Mannaro, Boyko, Brad, Brandon Gauthier, Brandon Mirr, Brent, Brett Williams, Bruce Gates, Byakuya36, Cirrus, Calmea, Carez, Carnosaur, Chad Dunkerley, Charles Able, Chemmy, Chris, Christopher Coulter, Christopher Woo, Christopher, Conner Owen, Conrad Boucher, Cruise Russo, Cyanide Sam, DMetal, Dakota Rude, Damian Boggs, Daniel Beard, Daniel Nathans, Daniel Smith, Daniel Szczuka, Daniel Torres, Danno, Danny Johansson, Danny Nguyen, Darkflame256, David Lestina, David Ruskin, David, Dean, Devin Barr, Dirk Delva, Donaj88, Donoth Aveano, DoornailsAreJealous, Demodraken, Double A, Drity, Edward le coyte, Eldar Scum, Eric Hsu, Evan waleske, Fabian, Faux, Fetsch Sebastian, Finrock, Fix, Formless, FoxPrince623, Frank Pietsch, Fraziel, Frederic Chen, Garrett Smith, Geoff Levario, Georgika, Gregc, Greg Hartley, Gregory G, Gunderson, Harm Harm, Harry Tizard, Hooverspleen, Ian W, Innes French, Jacob Thompson, Jacob, Jake Smith, Janis Feldbergs, Janus, Jared Whisenand, Jarred Leverton, Jason Buisman, Jason Chong, Jeff Abrams, Jeff, Jeremiah, John F, John S, John doe, John, Jonathan Backer, Jonathan, Joseph Balbuena, Joseph Oliveira, Josh Stegmaier, Juan Gomez, Jurdia, Justin Golden, Karl Stevenson, Karolis, Kenneth Guevarra, Kenneth Jackson, Kenny Huang, Kimo Linder-Fattah, Kolkina, Kristian Lund Jensen, Kryssler, Kurrel, Kyle Sarty, Kyuubi43, LIndy, Levone W., Jonathan Liu, Lockkaliber, Lord G, Lord Rayek, Lothvarthian Malik, Lukas Vystup, Luke Arrowsmith, Magmanox, Majushi, Mario Mueller, Mark Walrusburg, Martino Livio Martinello, Mason Davis, Matt Sullivan, Matthew Young, Michael Klepper, Michael McPherson, Michael O'Hara, Michael, Mike M., Mike Orlando, MinoCrossing, Miran, Mitchell Goodwin, Monky of Space, Morten Brunebjerg Hansen, Myers, N Metso, Naintoxe, Nairolf, Nathan S, Neo Savoric, Niels T, NugLord, Number37, Nym Nemo, Oliver Pirie, Oscar Lan, PS, Passionately Odd Syntax, Patrick Fochler, Patrick, Paul Allen, Peter Grnlykke, Professor Snape, PuddingPowder, Pel-Tore, Rabe, Raglan Strom, Randolph Carter, Random, Reaver78, Rekoar, Reny Frederiksen, Richard Buettner, RickRub, Rightmind, Rob, Robert Doughty, Robert Simmons, Rodrigo Das Flores, Rune Daugaard Lundsteen, Runkle, Russell, SJ M, SYukito, Sane 300, Sayting, Sinedd, Scorch289, Sean Carstensen, Sebastian Tauch, Sehad, Shane Fitzsimons, Shawn Aiken, Skellman, Skull616, SlaveToTheSound, Smaug, Some Guy, Steffen Nissen, Stephen Krieger, Steve Jones, Steven Cunningham, Syr, TGriz, Talon Grant, Teemu, Thae, The Masked Masturbator, This Isntmahname, Thomas Frobish, Thomas Grimes, Thomas Vazquez, Timmothy Firewood, Tom Arne Vestby2, Tony Taylor, Tony Veliz, Truvor, Tuki, Tyler, Venron, Vervalsen, Vi9, Visp, Wanderer, Weenie Beenie, Wesley Gamble, XDrakeX, Xev, YummyTiger, Yuu Yi, Zach Rzepiela, Zakmonster, Zeath, Zenzard, Zim outside, Zoggy, alvin suryaputra, am1tg3, andrew gardiner, artisticMink, barry r king, bloodangel99, butts, caleb4532, charles turnbull, cvonsuela28, dingo egret, dingo1489, eXotic, fernando frias, gliph13, ippherita, izys, jabix, jassem dashti, john smith, josiah richter, karkazin, kyle mock, lia sven, lucas2684, n1ghtfox, nobody, potatohead, progste, randellspec, retchedegg, robster, silvarius2000, srt20022003, strider19, tehcalipwnt, terribleplan, thegreatbambe, timmy turner, varoksa, xenus, ziric.{/color}{/size}

{color=#e5e297}-\"ACTIVIST\" pledges-{/color}
{size=-5}{color=#cbcbcb}Adam, Alvin, AmateurArtist98, Anders Sandahl, Naqqash Chaudhry, Andre, Andrew E., Bayushi, Ben Belcastro, Brandon Louie, Brandon Robinet, Brian Wilson, Carmen Williams, Chad Bennett, Dan George, Darklogic, Darknezzz, Dave Shevlin, David Crosby, David Sparkes, Douglas Jones, Draconic Paragon, DragonTamer, Ervin, Francis Dixson, Fredinator, Gene Boglin, George Craig, Greg, Guillaume Mroz, Gustaf Johansson, Hirin, Ian Lindop, IanDasein, Inge, Izzy Sabur, JBTClown, JP, Jack, Jacob Kain, Jan Hanenkamp, Jan M., Jan, Johannes Uwer, John Turner, Joshua Baadsgaard, KiSwordsman, Krux2022, L, Legio 20th, Marconi Ribeiro, Mike, Marius L, Mathias Frandsen, Matthew Marqueta, Max, Michael Webb, Miha Antauer, Mikhail V. Platonov, Mitch, Mountainj6, MrDurper, Sean Hill, Sam, Muirewedd, Neogeta, Nick Foronda, Nick, Noah Gerhards, Oren Barzilai, Pashike, Peeves, Phil Fairbanks, Philip G Honore, Riu Bas, Robert, Reinis Aleksejevs, Rougespartan181, Robert Lesundak, SO, SYH, Sacs, Sapherin, Sayyid, Sean, Shawn MacInnis, Simanith, Soda Zero, Speculations, Stephen Evans, Stonedrake, TRONboy, Tamenund Jones, Tintron, Victor Jd, Vincent McCool, Vitaliy Kasianenko, Vorcai0, Wolfcub, X.p., X39, Yan Luong, Zaker, chippy, joesco726, kurorol2, lambroll, ljennia, matthew lampell, moonwalkin, nh, raaq, six2make4, zack, Andry Sidorov.{/color}{/size}

{color=#e5e297}-\"SUPPORTER\" pledges-{/color}
{size=-5}{color=#cbcbcb}AS84, Aaron Gregory, Gianfranco Calzoni, Aarvil Kemph, Aestus, Alex Martin, Andrea, Andreas, Andrew, Antilles, Antonboeg, Aran, Armando Soto, Azuliar, Batman, Balint Sule, Ben Rog-Wilhelm, Benjamin Cathey, Beth, Brad Hingston, Brandon Grant, Brendan, Brian Borden, Bru, Canyon, Capperroff, Chaintan, Christian Wong, Colton Clayton, Corey S., D, Damian Paradis, Daniel Chai, Daniel Geach, Daniel, Danny Mullay, Darpy, Dave doedry, David Leitner, Dax, Doctor Worm, Dragonman, Edd Holmes, Erebe, Eric Speaker, Fattycakes, FearTheDee, FeyOne, Filip Jaromin, Florian Eberle, FooldiverDX, Fortifel, Frank Bull, G V, Gaetano, Gary Tinsley, Gerald, Gerald, Gerhalt, Gregoire Fauconnier, Gregory, Happy Days, Hellomellowyellow, Hurf durf, Ian Sayer, Ilya, Ivan Nadasaki, J Solomon, Jack Simons, Jack Trebles, James Brown, James Do, Jan-Kristoffer Brekke, Jayro Zipzapili, Jesse Doerksen, Jim, John Jon'zz, John Smith, Jonas Högman, Jose Gonzalez, Joshua West, Julian Silva, KC maps, Kabuto, Kasper Nohr, Kenny Bailey, Kevin McKie, Kuroguma, Lanthanio, Louie Castro, MaiconMM, Majinken, Malcom Reynolds, Marc Voigt, Marcel Muller, Marius Thomassen, MarkAurel, Martin Ax, Matri, Matt, Matthew Lam, Max Robitzsch, MehMonkeys, MercuryTwins, Messor Marra, Michael Troseth, Michael, Michael, Michael, Mike Bow, Mike Jones, Mike Moperz, Mikhail, N0body, NalfeinDoUrden, Nate A, Nicholas Alan McGuire, Nikuss, Nils Harder, Nitrat, Nordicberserk, Notsutos, Oberon, Onyxdime, Oxion1988, Ozzy, Paradosi, Pasi Huttunen, Patrick Gill, Paul Coad, patrick welsh, Paul, Pshenitsyn, PeeM, Peter Nikolas, Peter Ryskin, Pitt85, Preator, Pulimanne, Randall Lively, Richard Dumont, Richard Heying, Richard Soderberg, Riley Heffernan, Robert Bodo, Robert Davis, Rodrigo Rosado, Ronald, Roy Zimmermann, Ryan Bossard, Ryan Calhoun, Salvadore Broadfoot, Scott Barrie, Sebastien Elie, Sebastien Jalbert, SgtAfro, Shadefalcon, Stefano Sottocorna, SilverAxe, Sixxiie, Sky Valverde, Sodajuice, Steffen Sloth, TK, TP Samblanet, Taylor Patton, Taylor, Tenebrys Hentai Flash Games, Matthew Pruter, John Stanko, craig chadwick, TheOriginalJ, Thomas, Timeyy, Tony Li, TonyNinja, Tracy Scops, Travis Haapala, TrikJoker, Tyler Jones, Tyson, Urza Viderico, VC, Vasder, Vay Jay, Victor Sarosi, Warren P Nelson, Wayne Chattillon, William Farris, William Golding, Wlodzimierz Donatowicz, Xaljio, Xisis, brett, bronzeRanger, clerk4470, ghosti1, gillen, ismael torres, jaron uecker, levi tibbals, oakland, otakuguy01, rip_cpu, severin, sirpoffalot, teh_cabbage, tenko, trajor white, wilhelm, winsloven, Arkadii Terentiev, xxx, DAHR.{/color}{/size}

{size=-5}{color=#e5e297}Thank you, Joseph Antoni, for organising all these 750+ names.{/color}{/size}
{vspace=200}

Special thanks to our fans, discord moderators
and {a=https://www.patreon.com/SilverStudioGames/}patreon supporters{/a} {image=images/misc/heart.png}

{image=logo/silverstudiogames.png}
{vspace=50}

Thank you for playing!

{space=100}{image=characters/genie/mage9.png}"""
])

define credits_duration = 60

define credits_chibis = (
    (Transform("ch_sna wand_defend", xzoom=-1), 1, 10, True),
    (Transform("ch_sna jerk_off", yoffset=120), 12, 10, False),
    ("ch_hem run", 14, 8, True),
    (Transform("hj", zoom=2, crop=(225,200,200,235)), 24, 8, True),
    (Transform("ch_gen read", offset=(80,120)), 34, 16, False),
)

label credits:
    if not _menu:
        play music ["music/02 - Shanghai Honey.mp3", "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3"] fadein 1 fadeout 1 noloop
    show screen credits(credits_text)
    with dissolve
    call update_interface_color("gray")
    $ achievement.unlock("Credits")
    pause credits_duration
    if not _menu:
        stop music fadeout 3
    call ctc
    hide screen credits
    with dissolve
    
    if _menu:
        # play music config.main_menu_music fadein 1 fadeout 3
        jump main_menu_screen
    else:
        return

transform credits_chibi_fade(start, duration):
    alpha 0
    pause start
    linear 0.5 alpha 1.0
    pause duration
    linear 0.5 alpha 0.0

screen credits(credits=credits_text, duration=credits_duration, chibis=credits_chibis):
    tag credits
    zorder 8
    
    add Solid("#000")

    for img, t, d, left in chibis:
        add img:
            at credits_chibi_fade(t, d)
            zoom 0.5
            if left:
                pos (20, config.screen_height - 20)
                align (0.0, 1.0)
            else:
                pos (config.screen_width - 20, config.screen_height - 20)
                align (1.0, 1.0)
   
    text credits:
        at transform:
            subpixel True
            xalign 0.5
            yanchor 0.0
            ypos (config.screen_height / 2 - 125)
            pause 1
            parallel:
                linear (duration - 1) yanchor 1.0
            parallel:
                linear (duration - 1) ypos (config.screen_height + 50)
        xsize int(config.screen_width * 0.65)
        text_align 0.5
        color "#fff"
        outlines [(2, "#000", 0, 0)]
