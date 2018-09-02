label hermione_map_BJ:
    $ renpy.call('forest_BJ_'+str(forest_BJ_progress))
    jump day_main_menu

label forest_BJ_1: #BJ in the forest interrupted by moaning myrtle
    show screen blkfade
    with d3
    ">Sure enough, the map seems to {b}magically{/b} guide you to the young girl, alone in the midnight air..."
    ">Seemingly scrapping the resin off of a tree..."
    hide screen blkfade 
    with d3
    m "Miss Granger? What are you doing out here at this time of night?"
    her "[genie_name]! I, ugh, I wasn't doing anything bad, I swear!"
    m "..."
    her "Ugh, fine! If you must know, I was out here gathering up some mastick resin."
    her "I know Students aren't {i}technically{/i} supposed to touch the stuff since it's normally just used to make belch powder..."
    her "But I'm using it in my research for a natural analgesic!"
    m "Whatever..."
    menu:
        "-Let her get back to her botany-":
            m "Well I better leave you be then..."
            her "Really?"
            her "You mean you don't want to..."
            m "Maybe some other time."
            her "..."
            show screen blkfade
            with d3
            ">You turn away from the miffed young girl."
            m "..."
            m "(What's wrong with me?)"
            return
        "-Ask for a blowjob-":
            m "Well, seeing that we're all alone out here..."
            her "Oh... I, um, guess we are..."
            m "Wanna fool around?"
            her "Oh thank goodness... I thought you were going to murder me for a second there..."
            m "What? How could you think such a thing!"
            m "I don't know if I'll be able to-"
            her "How about I make it up to you with my mouth then, hmmm?"
            m "Done."
    show screen blkfade
    with d3
    ">The girl softly lays her robe on the cool grass before kneeling down on it in front of your steaming cock."
    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = 1
    $ ccg3 = "overlay"
    show screen ccg
    hide screen blkfade
    with d3
    her "Mmmm... I don't think I'll ever get sick of this cock..."
    m "It'll get sick of having to wait for you to put it in your mouth though."
    $ ccg2 = 2
    her "Hmph... now, now, [genie_name], patience is a virtue..."
    $ ccg2 = 3
    her "Besides, doesn't my hand feel nice?"
    m "Not as nice as your mouth."
    her "Alright then... Have it your way."
    $ ccg2 = 4
    ">With that, Hermione leans forward and engulfs the head of your cock in her mouth."
    who2 "{size=-10}Wow...{/size}"
    $ ccg2 = 5
    her "!!!"
    her "Did you hear something?"
    m "What? I don't believe so..."
    m "Not unless you count the sound of you sucking away..."
    m "Speaking of which..."
    $ ccg2 = 6
    her "..."
    $ ccg2 = 7
    ">Hermione goes back to work, slobbering her way up and down your cock."
    m "Gods... they'd make you a queen for sucking cock like this in Agrabah..."
    $ ccg2 = 8
    her "(Where?)"
    m "Mmmmm... Fuck yes..."
    who2 "{size=-8}tehehehe...{/size}"
    $ ccg2 = 5
    her "!!!"
    $ ccg2 = 9
    her "Tell me you heard something that time sir!"
    menu:
        "-Tell her to get back to work-":
            m "All I hear is a mouth that needs to get back to sucking."
            $ ccg2 = 10
            her "Not now sir!"
            her "I think there's someone else here..."
            her "Or something else..."
            m "Wait..."
            m "You don't mean..."
            pass
        "-Agree with her-":
            $ ccg2 = 10
            m "You might be right..."
            m "Did it sound like someone laughing?"
            her "Yeah..."
            her "{size=+10}Show yourselves!!!{/size}"
            pass
    $ ccg1 = "m1"
    myr "Tehehehe... Hi Hermione..."
    $ ccg2 = 11
    g9 "{size=+10}AH! A G-G-GHOST!{/size}"
    myr "hahahahah!"
    myr "Good one dumbledore! You always were a joker."
    her "Myrtle!"
    her "This isn't what it looks like!"
    myr "Isn't it?"
    myr "I think it looks lovely..."
    her "Argh! Please don't tell anyone!!!"
    show screen blkfade
    with d3
    hide screen ccg
    ">With that, Hermione hastily covers up and sprints away angrily as the ghostly apparition fades away..."
    hide screen blkfade 
    with d3
    m "What was that..."
    ">You stumble back to your office in a confused and blue-balled stupor..."
    return

label forest_BJ_2: 
    show screen blkfade
    with d3
    ">The map yet again leads you to the curly haired girl, alone at the edge of the forest, picking mushrooms."
    hide screen blkfade
    with d3
    m "More late night gardening?"
    her "{size=+10}Professor!{/size}"
    her "Ugh... Don't startle me like that!"
    her "And yes, I've been collecting some mushroom samples."
    m "Cool..."
    her "So what are you doing out here?"
    her "I thought you didn't leave your office anymore?"
    m "Oh, you know me... Always looking to connect with my students..."
    her "Mhmmm... So that's what you're down here for then? To {i}connect{/i}?"
    m "Always..."
    her "Fine... Just let me take my robe off..."
    show screen blkfade
    with d3
    ">Hermione quietly folds up her robe and places it on the cold ground before kneeling down on it."
    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = 12
    $ ccg3 = "overlay"
    show screen ccg
    hide screen blkfade
    with d3
    m "So you're not worried about that ghost?"
    her "You mean Myrtle? You know She's harmless..."
    $ ccg2 = 10
    her "It's the gossip I'm worried about..."
    m "Gossip?"
    $ ccg2 = 13
    her "Stop playing dumb [genie_name]! Everyone knows Myrtle's the biggest gossip in the history of gossips..."
    $ ccg2 = 4
    ">Hermione quickly pops your cock into her mouth in between her words..."
    $ ccg2 = 10
    her "*pop* Not to mention she never forgets! She's {b}still{/b} going on about the whole McCartney thing..."
    $ ccg2 = 8
    her "*shlrp* *schkk* *slurp*"
    m "Mmmm..."
    m "So have you heard any gossip floating around then?"
    $ ccg2 = 10
    her "Surprisingly not..."
    $ ccg2 = 14
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 13
    her "although She probably wouldn't want to upset you..."
    $ ccg2 = 4
    her "*shlrp* *schkk* *slurp*"
    m "Mmmm..."
    $ ccg2 = 10
    her "Still... I didn't think she'd be able to help herself..."
    $ ccg2 = 14
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 15
    her "Ablus Dumbledore having his {b}cock{/b} sucked by Hermione Granger..."
    $ ccg2 = 16
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 12
    her "It'd be the gossip of the century...."
    $ ccg2 = 18
    her "*slurp* *schkk* *shlrp*"
    m "You almost sound disappointed that she didn't tell anyone."
    $ ccg2 = 17
    her "What? How could you say such a thing!"
    $ ccg2 = 16
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 19
    her "I'd never be able to show my face around hogwarts again..."
    $ ccg2 = 20
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 21
    her "Everyone would just be imagining me on me knees..."
    $ ccg2 = 18
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 21
    her "{b}Covered{/b} in your thick spunk..."
    $ ccg2 = 20
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 17
    her "Word would probably even get back to mommy and daddy..."
    $ ccg2 = 16
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 19
    her "imagine what they'd think of their little girl..."
    $ ccg2 = 18
    her "*slurp* *schkk* *shlrp*"
    $ ccg2 = 21
    her "sucking all that cum out her headmasters {b}fat, {size=+2}juicy, {size=+2}cock...{/size}{/b}{image=textheart}"
    g9 "ARGH THAT's IT GIRL!"
    g9 "HERE IT COMES"
    $ ccg2 = 22
    ">You grab a hold of the back of hermione's head and thrust forward, planting your cock firmly down her throat."
    $ ccg1 = "m1"
    myr "Wow... I didn't think you'd fit it all in..."
    $ ccg2 = 23
    her "!!!"
    ">Not even the sudden appearance of a ghost can stop your colossal orgasm at this point..."
    g9 "ARGH!!!"
    ">You start firing off a thick deluge of cum down Hermione's tender throat, the presence of someone else only serving to coax more out of your balls..."
    $ ccg2 = 24
    her "!!!!!!"
    $ ccg2 = 25
    g9 "Gods I Needed this!"
    $ ccg2 = 26
    myr "So much...{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 25
    ">Your hips continue to pump more and more cum down hermione's throat."
    $ ccg2 = 26
    her "..."
    $ ccg2 = 25
    myr "Bye Hermione{image=textheart}{image=textheart}{image=textheart}"
    show screen blkfade 
    with d3
    ">Eventually your orgasm subsides and you allow your softening member to slide out of hermione's cum coated throat."
    hide screen ccg
    hide screen blkfade
    with d3
    her "I can't believe you just did that?"
    m "really? After everything we've done?"
    her "It's a figure of speech! And More importantly..."
    her "{size=+10}You just came down my throat in front of moaning myrtle!{/size}"
    her "She's going to tell everyone about this now!"
    m "So? Doesn't everyone sort of know by now anyway?"
    her "Argh! That's not the point and you know it!"
    her "You can't keep treating me like your {image=textheart}dirty{image=textheart} little {b}cumdump{/b} to use as you please!"
    her "To coat in your filthy nasty {b}{image=textheart}cum{image=textheart}{/b}..."
    her "In front of whoever, or whatever, you want..."
    her "..."
    her "Well... I hope you've learned your lesson!"
    her "I'm going to go back and..."
    her "ge-Clean! myself off..."
    her "And remember..."
    her "no {size=-1}more... {size=-1}{b}cum{/b}... {size=-1}all... {size=-1}over... {size=-1}me... {size=-1}please...{image=textheart}{image=textheart}{image=textheart}{/size}"
    show screen blkfade
    with d3
    ">With that, hermione staggers back to the castle, still coated in your thick layer of seed."
    hide screen blkfade
    with d3
    return

    
label forest_BJ_3: #Complete BJ with Myrtle appearing after the cumshot
    show screen blkfade
    with d3
    ">Surely enough, the handwritten words \'hermione granger\', manage to lead you to the lone girl at the edge of an imposing forest."
    ">However she doesn't seem preoccupied with her usual botany."
    hide screen blkfade
    with d3
    m "Aren't you usually out her to collect some forbidden plant [hermione_name]?"
    her "Not always... Sometimes I just come out her to enjoy the cool air..."
    m "I see..."
    m "So you're not waiting out here for your headmaster to arrive, just so you can suck his cock in public?"
    her "What! o-of course not!"
    her "I'm just out here to admire the moon!"
    m "What moon?"
    ">Hermione frantically looks to the cloudy sky, unable to even glimpse the moon through the impenetrable greyness."
    her "Oh... um..."
    m "It's alright for you to admit that you're a dirty little cumslut, miss granger."
    her "It's not like that!"
    her "I just like sucking your dick OK!"
    m "So you don't want me to cover you in cum like the cumslut you are?"
    her "..."
    her "Ugh..."
    show screen blkfade
    with d3
    ">With that, Hermione studiously removes, folds and lays her robe on the cool night grass."
    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = 15
    $ ccg3 = "overlay"
    show screen ccg
    hide screen blkfade 
    with d3
    her "Maybe I wouldn't have ended up a dirty little cumslut if your dick wasn't so nice..."
    #Have her suck his cock
    $ ccg2 = 16
    pause
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 17
    her "ah....{image=textheart}{image=textheart}{image=textheart}"
    her "Thank you for being here tonight [genie_name]...."
    $ ccg2 = 16
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 19
    her "I wasn't sure if you were going come..."
    $ ccg2 = 18
    her "*glck* *shlrp* *Gluck*"
    m "If you want me to keep cumming, I suggest you do a little less talking..."
    $ ccg2 = 20
    her "Hsss hrrr! (Yes sir!)"
    $ ccg2 = 27
    ">In response, hermione thrusts her entire lithe frame forwards, forcing your thick cock all the way down her throat."
    $ ccg2 = 28
    g9 "Ugh.... that's it [hermione_name]"
    $ ccg2 = 29
    m "How are you able go so deep?..."
    $ ccg2 = 17
    her "Hmmm, I had a good teacher..."
    $ ccg2 = 19
    m "As flattered as I am..."
    ">You softly low your hand on to the back of the little sluts head..."
    $ ccg2 = 30
    g9 "THIS!"
    pause
    $ ccg2 = 31
    g9 "Can't be taught!"
    $ ccg2 = 30
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 31
    ">You vigorously start fucking the poor girls throat with little regard for her well being."
    $ ccg2 = 32
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 33
    g9 "You were born a cocksucker."
    $ ccg2 = 32
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 33
    g9 "It's just taken you until now to realise."
    $ ccg2 = 32
    her "*glck* *shlrp* *Gluck*"
    $ ccg2 = 33
    $ ccg1 = "m2"
    $ ccg2 = 33
    ">You're so focussed in your facefuck session you almost fail to notice the ghostly appartation of an attractive little witch appear behind Hermione."
    $ ccg2 = 32
    g4 "!!!"
    $ ccg2 = 33
    ">Before you even have time to scream, Myrtle, raises her finger to her lips, shushing you."
    $ ccg2 = 32
    ">Instead, it appears like she only wants to watch hermione have her throat fucked silly..."
    $ ccg2 = 34
    g9 "Well if it's a show you want, {size=+3}it's {size=+3}a {size=+3}show {size=+3}you'll {size=+3}get!{/size}"
    $ ccg2 = 35
    her "???"
    $ ccg2 = 34
    ">Coaxed on by the prospect of an ethereal audience, you begin to get into a firm, rough rhythm of properly fucking hermione's throat raw."
    $ ccg2 = 35
    her "*glck*!!!*glck*!!!*glck*"
    $ ccg2 = 34
    her "*glck*{image=textheart}*glck*{image=textheart}*glck*"
    $ ccg2 = 35
    myr "..."
    $ ccg2 = 34
    her "*Slurp!* *Gulp!* *Slurp!*"
    $ ccg2 = 35
    m "Yes, like that... that's a good little slut..."
    $ ccg2 = 34
    her "*Slurp!* *Slurp!* *Slurp!*"
    $ ccg2 = 35
    m "Deeper now."
    $ ccg2 = 34
    her "*Slurp!* *Slurp!* *Slurp!*"
    $ ccg2 = 35
    m "Come on cock-slut."
    $ ccg2 = 36
    her "*Slurp!* *Gobble!* *Gobble!*"
    $ ccg2 = 37
    g4 "Deeper now!"
    $ ccg2 = 36
    her "*Gobble-goble-slurp-goble!*"
    $ ccg2 = 37
    g4 "Yes, like that!"
    $ ccg2 = 36
    her "{size=+5}*Gobble-gobble-slurp-gobble!* !!!{/size}"
    $ ccg2 = 34
    g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
    $ ccg2 = 35
    g9 "See? Your body was made for this..."
    $ ccg2 = 36
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 37
    g9 "Made to take my cock!"
    $ ccg2 = 36
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 37
    g9 "Any time of day!"
    $ ccg2 = 34
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 35
    g9 "Anywhere you can get it!"
    $ ccg2 = 34
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 37
    g9 "And in front of anyone who will watch you!"
    $ ccg2 = 38
    her "{size=+10}!!!{/size}"
    $ ccg2 = 37
    myr "hehehe, hi hermione..."
    $ ccg2 = 36
    her "*glck*Stt-*glck*{image=textheart}*glck*"
    $ ccg2 = 37
    ">Hermione starts to struggle against you in her embarressment, her face turns a deep red and tears start to roll down her face."
    $ ccg2 = 36
    ">Unfortunately for petite witch, her shame only serves to intensify your pleasure."
    $ ccg2 = 37
    g9 "ARGH, HERE IT COMES SLUT!"
    $ ccg2 = 36
    g4 "{size=+7}ARGH!{/size}"
    $ ccg2 = 37
    g4 "{size=+7}Eat my cum, slut!{/size}"
    $ ccg2 = 34
    ">Your cock starts firing off a huge load against the back of the poor girls throat, quickly overflowing up through her nostrils and back at you."
    $ ccg2 = 39
    her "{size=+14}!!!{/size}"
    $ ccg2 = 40
    myr "{size=+3}Oh {size=+3}my {size=+3}God!{/size}"
    $ ccg2 = 39
    myr "I've never seen this much cum in my whole life or even since then!"
    $ ccg2 = 40
    myr "Here Dumbledore, shoot some more!"
    $ ccg2 = 39
    show screen blkfade
    with d3
    $ ccg1 = "m3"
    ">With that Moaning Myrtle rises up from the dewy ground and flashes her see-through breasts towards you."
    $ ccg2 = 41
    hide screen blkfade 
    with d3
    g4 "{size=+7}ARGH! YES!!!{/size}"
    $ ccg2 = 42
    ">With your orgasm renewed by the sight of some heavenly cans, you begin shooting cum down hermione throat anew."
    $ ccg2 = 41
    her "*gulp* *argggglelggg* *gobble*...."
    $ ccg2 = 42
    myr "More dumbledore MORE!"
    $ ccg2 = 41
    g4 "{size=+15}ARGH!!!!{/size}"
    $ ccg2 = 42
    her "*gllllgggggg*..."
    $ ccg2 = 41
    myr "{size=+14}MORE!!!{size=+14}"
    $ ccg2 = 42
    show screen blkfade
    with d3
    hide screen ccg
    ">Eventually, your orgasm comes to a halt and you finally pull your sloppy cock out of Hermione's well used hole..."
    ">She collapses onto her robe, no longer held up by your member."
    m "You did good, kid..."
    m "Wouldn't you say ghost?"
    m "Ghost?"
    m "Oh well..."
    ">You notice Hermione start to shiver in the cold air..."
    m "I suppose I better get you back to your room."
    ">You wrap her robe over her like a blanket and carry her back to her room."
    ">You softly place her into her bed and pull up her sheets."
    menu:
        "Clean the cum off her face?"
        "-clean it-":
            m "(I suppose I should probably clean that off..."
            ">You use a rag and wipe her face clean."
            her "*zzz* no... *zzz* I wanna be a*zzz* cumslut...*zzz*"
            m "(Guess I probably should have left it..."
        "-leave it-":
            m "(She looks better like this anyway...)"
            ">As you turn to leave, you notice a content smile form over Hermione's face as she pulls her sheets up over her shoulders."
            her "{size=-10}Night sir...{/size}"
            her "{size=-15}I love you...{/size}"
    ">You turn and leave the warm room and return to your cold, dark office..."
    hide screen blkfade
    with d3
    return





label forest_BJ_4: #Moaning myrtle dirty talk (Repeatable) (Threaten to expose)
    show screen blkfade
    with d3
    ">Once more, the marauders map leads you to Hermione at the edge of the forest, waiting patiently, apparently having dropped all pretences botanical."
    hide screen blkfade
    with d3
    m "[hermione_name]..."
    her "About time you got here [genie_name]!"
    her "Do you know how long I've been waiting out here in the cold?"
    menu:
        "-Apologise-":
            m "Sorry about that..."
            m "I'll try and be on time for our blowjobs from now on."
            her "Good... It's the least you can do..."
        "-Tell her to come to your office instead-":
            m "You know where my office is..."
            her "Hmph..."
    show screen blkfade
    with d3
    ">Hermione then kneels down onto the pillow and rug she must have lain down before your arrival."
    ">You quickly walk over to the small girl and present her your thick cock."
    $ ccg_folder = "herm_forest"
    $ ccg1 = "blank"
    $ ccg2 = 15
    $ ccg3 = "overlay"
    show screen ccg
    hide screen blkfade 
    with d3
    her "Mmmmm..."
    $ ccg2 = 17
    her "This almost makes waiting out in the cold worth it..."
    m "Only almost?"
    her "Well it's not the real reason I'm down here [genie_name]..."
    $ ccg2 = 19
    her "this is..."
    $ ccg2 = 16
    ">With that, Hermione quickly pops her head forward, wrapping her soft lips around the tip of your shaft."
    her "*Mmmmm*"
    $ ccg2 = 18
    her "*slurp* *glck* *slrp*"
    $ ccg2 = 20
    m "Ughhhh.... that's it [hermione_name]..."
    m "Be a good little cockslut for you headmaster..."
    $ ccg2 = 16
    her "*slurp*{image=textheart}*slurp*{image=textheart}*glck*"
    #Myrtle fade in
    $ ccg1 = "m2"
    m "And for casper the slutty ghost here..."
    $ ccg2 = 43
    her "*slurp*!!!*slurp*!!!*glck*"
    menu:
        "Once again, Hermione tries to pull herself of your cock..."
        "-Let her-":
            ">Reluctantly, you allow the girl to pull herself of your throbbing member..."
            $ ccg2 = 10
            her "Myrtle! What are you doing here again?"
            myr "Aren't I allowed a bit of fun in my afterlife?"
            myr "It's not like I ever got any when I was alive..."
            $ ccg2 = 6
            her "Oh alright then..."
            $ ccg2 = 10
            her "Just don't go blabbing to everyone in the girls bathroom, OK?"
            myr "Deal..."
            m "Good... Now why don't you just sit back and enjoy the show then..."
        "-facefuck her-":
            pass
    $ ccg2 = 28
    ">you place your hand on the back of Hermione's head and pull her hard into your waiting cock, impaling the poor girls throat... "
    $ ccg2 = 29
    her "{size=+10}!!!{/size}"
    $ ccg2 = 30
    g4 "Ugh... fuck yes..."
    $ ccg2 = 31
    her "{size=+5}*Gobble-gobble-slurp-gobble!* !!!{/size}"
    $ ccg2 = 30
    g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
    $ ccg2 = 31
    myr "Wow... you're so rough on her..."
    $ ccg2 = 32
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 33
    g9 "Ugh... don't worry... she loves it..."
    $ ccg2 = 32
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 33
    g9 "She's probably wetter than the nile down there..."
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 32
    myr "You think so?"
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 33
    g9 "Go see for yourself!"
    $ ccg2 = 32
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 33
    myr "..."
    $ ccg2 = 32
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 33
    ">Myrtle floats down into the earth."
    $ ccg2 = 34
    her "{size=+10}!!!{/size}"
    $ ccg2 = 35
    myr "She's dripping!"
    $ ccg2 = 34
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 35
    myr "Not to mention she isn't wearing any panties!"
    $ ccg2 = 34
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 35
    g4 "She stopped wearing them months ago."
    $ ccg2 = 34
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 35
    myr "Hermione! You horny little girl!"
    $ ccg2 = 34
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 35
    myr "Just wait until the girls bathrooms hear about tonight!"
    $ ccg2 = 34
    her "{size=+5}*glck*HNNOOO*glck*{/size}"
    $ ccg2 = 44
    myr "So long as you're alright with that Sir... I don't have to mention you! It can just be Hermione!"
    $ ccg2 = 34
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 35
    menu:
        "-\"go nuts\"-":
            $ ccg2 = 34
            myr "Really?"
            $ ccg2 = 35
            her "{size=+5}*glck*{image=textheart}PRFFSSRR!!!{image=textheart}*glck*{/size}"
            $ ccg2 = 34
            myr "Oh thank you, thank you, thank you!"
            $ ccg2 = 35
            her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
            $ ccg2 = 34
            myr "This is going to be the best decade of my afterlife!"
            $ ccg2 = 35
            her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
            $ ccg2 = 34
        "-\"you can say it was me\"-":
            $ ccg2 = 34
            myr "{size=+2}{b}Really?{/b}{/size}"
            $ ccg2 = 35
            her "{size=+5}*glck*{image=textheart}WHHTT!!!{image=textheart}*glck*{/size}"
            $ ccg2 = 34
            myr "Oh thank you, thank you, thank you!"
            $ ccg2 = 35
            her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
            $ ccg2 = 34
            myr "This is going to be the best decade of my afterlife!"
            $ ccg2 = 35
            her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 34
    myr "I can't wait to tell everyone!!!"
    $ ccg2 = 35
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 34
    myr "I'll go to rave-NO the Slytherin bathroom first!"
    $ ccg2 = 44
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 34
    myr "Then gryffindor!"
    $ ccg2 = 35
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 34
    myr "Ravenclaw!"
    $ ccg2 = 35
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 34
    myr "Hufflepuff!"
    $ ccg2 = 35
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 34
    myr "The prefect's bathroom!"
    $ ccg2 = 35
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 34
    myr "Then the teachers!"
    $ ccg2 = 35
    her "{size=+5}*glck*{image=textheart}*glck*{image=textheart}*glck*{/size}"
    $ ccg2 = 34
    myr "Then hogsmead!"
    $ ccg2 = 35
    myr "{size=+2}THEN {size=+2}THE {size=+2}WHOLE {size=+2}WORLD!!!{/size}"
    $ ccg2 = 34
    g9 "ARGH, HERE IT COMES SLUTS!"
    $ ccg2 = 35
    g4 "{size=+7}ARGH!{/size}"
    $ ccg2 = 34
    g4 "{size=+7}Eat my cum, slut!{/size}"
    show screen blkfade
    with d3
    $ ccg1 = "blank"
    ">At the edge of your orgasm, Hermione forcefully pushes herself off your dick and wraps your cock in her hands and hair."
    $ ccg2 = 45
    hide screen blkfade 
    with d3
    her "{size=+5} That's it Professor Cum for me! sir! cover me in front of Myrtle!{/size}"
    with hpunch
    g4 "{size=+5}What the hell is this?!{/size}"
    $ ccg2 = 46
    her "{size=+5}Cum on sir! Aren't I your dirty little cumslut?{/size}"
    g4 "Argh! You cum obsessed whore!"
    $ ccg2 = 45
    her "{size=+5}Yes I am!{/size}"
    her "{size=+5}Nothing but your cum hungry little slut, sir!{/size}"
    $ ccg2 = 47
    her "{size=+5}Now why don't you show Myrtle here what a real load looks like!{/size}"
    with hpunch
    g4 "{size=+7}Argh!!!{/size}"
    g4 "{size=+7}Take this, then!!!{/size}"
    show screen white
    pause .1
    hide screen white
    with hpunch
    $ ccg2 = 48
    her "{size=+5}Ah! Yes, sir! Yes! cum all over me!{/size}"
    show screen white
    pause.1
    hide screen white
    $ ccg2 = 49
    pause.2
    show screen white
    pause .1
    hide screen white
    with hpunch
    g4 "{size=+7}ARGH!{/size}"
    g4 "{size=+7}Argh!!! YES!!!{/size}"
    $ ccg2 = 50
    her "{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
    show screen blkfade 
    with d3
    #Genie and Hermione back in the forest...
    hide screen blkfade
    with d3
    her "Wait, where's Myrtle?"
    m "Oh, she left as soon as I gave her the OK to blab on about you."
    her "WHAT?"
    her "you mean she didn't see any of..."
    her "(I got my hair all sticky for nothing...)"
    m "So are you going to clean yourself up and get dressed?"
    her "I'll get dressed..."
    her "If it's all the same to you, I might leave the cum on..."
    m "Good girl..."
    show screen blkfade 
    with d3
    ">With that, you and Hermione walk back to the castle together, Hermione complaining about how rude Myrtle was for missing the cumshot the whole way..."
    hide screen blkfade
    with d3
    return










































