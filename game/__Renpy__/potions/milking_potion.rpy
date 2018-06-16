

label potion_scene_11: #Milking potion

    if potion_scene_11_progress == 0 or whoring < 13:
        $ potion_scene_11_progress = 1
        jump potion_scene_11_1
    elif potion_scene_11_progress == 1 or whoring < 18:
        $ potion_scene_11_progress = 2
        jump potion_scene_11_2
    else:
        jump potion_scene_11_3


label potion_scene_11_1: #Milking potion part 1
    m "[hermione_name], how would you like to try a nice little potion?"
    call her_main("...","open","angryCl") from _call_her_main_2015
    call her_main("If I had the option I'd prefer not to...","open","base") from _call_her_main_2016
    m "well-"
    call her_main("but unfortunately, \"Slytherin\" winning the house cup this year isn't an option!","scream","angryCl") from _call_her_main_2017
    m "So you'll drink the potion then?"
    call her_main("Yes [genie_name], I'll drink your potion.","annoyed","suspicious") from _call_her_main_2018
    m "Fantastic!"
    call nar(">You hand her the cloudy potion.","start") from _call_nar_279
    call nar(">Hermione cautiously smells the mixture.","end") from _call_nar_280
    call her_main("Is this milk?","annoyed","angryL") from _call_her_main_2019
    call her_main("...","annoyed","frown") from _call_her_main_2020
    call her_main("I guess it doesn't matter...","open","suspicious") from _call_her_main_2021
    
    call her_chibi("drink_potion","mid","base") from _call_her_chibi_92
    
    call nar(">Hermione quickly drinks the potion.") from _call_nar_281
    
    call her_chibi("stand","mid","base") from _call_her_chibi_93
    
    call her_main("Ah...","cum","worriedCl") from _call_her_main_2022
    call her_main("It was milk!","smile","baseL") from _call_her_main_2023
    m "Yes. Apparently it's a special kind of milk."
    call her_main("Apparently?","open","suspicious") from _call_her_main_2024
    call her_main("Do you even know where this came from?","annoyed","frown") from _call_her_main_2025
    m "O-Of course I do."
    m "I'm the great dingledoor after all!"
    call her_main("...","open","suspicious") from _call_her_main_2026
    call her_main("If you don't want to say what it is that's fine sir...","open","angryCl") from _call_her_main_2027
    call her_main("But there's no need to insult me.","normal","frown") from _call_her_main_2028
    m "(what did I say?)"
    m "Yes, well, you should notice the effects starting to manifest soon enough."
    call her_main("Hmmm...","base","glance") from _call_her_main_2029
    call her_main("And what sort of \'effects\' would that be?","open","suspicious") from _call_her_main_2030
    m "You may notice a some minor swelling in those nice tits of yours."
    call her_main("...","base","base") from _call_her_main_2031
    call her_main("Is this milk going to make by breasts bigger [genie_name]?","annoyed","frown") from _call_her_main_2032
    m "That's one half of it."
    call her_main("...","normal","frown") from _call_her_main_2033
    call her_main("And the other half?","annoyed","angryL") from _call_her_main_2034
    m "Well you might start to notice a little milk coming from your-"
    call her_main("What???","shock","wide") from _call_her_main_2035
    call her_main("Professor, Do you mean to say that this potion is going to cause me to lactate?","annoyed","frown") from _call_her_main_2036
    m "That's one way to put it."
    call her_main("...","normal","frown") from _call_her_main_2037
    call her_main("Well how long is it supposed to last? I do have classes today.","annoyed","angryL") from _call_her_main_2038
    call her_main("I'm falling behind enough as it is...","annoyed","worriedL") from _call_her_main_2039
    m "Really?"
    call her_main("Yes... I think it's all this fooling around sir.","normal","worriedCl") from _call_her_main_2040
    call her_main("I nearly got a \"b\" in biology the other day...","angry","worried") from _call_her_main_2041
    m "Well speaking of biology..."
    call nar(">You notice hermione's breasts slight to swell slightly.") from _call_nar_282
    call her_main("!!!","angry","wide") from _call_her_main_2042
    call her_main("[genie_name], they're growing rather quickly!","angry","worried") from _call_her_main_2043
    m "This is all perfectly normal."
    call her_main("...","open","suspicious") from _call_her_main_2044
    call nar(">Hermione's breasts start to visibly swell again.") from _call_nar_283
    call her_main("Ugh... it feels like my organs are sliding into my chest...","angry","worried") from _call_her_main_2045
    call her_main("This isn't going to cause any ongoing issues is it?","annoyed","frown") from _call_her_main_2046
    m "O-o-of course not..."
    call her_main("...","normal","frown") from _call_her_main_2047
    call her_main("That wasn't very inspiring...","annoyed","frown") from _call_her_main_2048
    m "Just focus on the matter at hand."
    
    $ hermione_expand_breasts = True #Temporary.
    
    call update_her_uniform from _call_update_her_uniform_44 #Updates body.
    with hpunch
    
    call her_main("!!!","angry","wide") from _call_her_main_2049
    
    if hermione_wear_top:
        call nar(">You hear a faint popping as Hermione's shirt fails to hold back her rapidly expanding breasts.") from _call_nar_284
    else:
        if hermione_wear_bra:
            call nar(">You hear a faint popping as Hermione's bra fails to hold back her rapidly expanding breasts.") from _call_nar_285
        else:
            call nar(">You watch in awe as Hermione's breasts start to rapidly expand!") from _call_nar_286
            
    call her_main("[genie_name], this is ridiculous!","angry","worried") from _call_her_main_2050
    call her_main("I can't be expected to go to class looking like this!","annoyed","worriedL") from _call_her_main_2051
    m "Why not? I don't think they're that much bigger than normal."
    call her_main("Are you kidding me?","disgust","glance") from _call_her_main_2052
    call her_main("They're {size=+5}humungous!{/size}","angry","angry") from _call_her_main_2053
    m "Well if you want them to go back to normal..."
    call her_main("What? Do you have an antidote?","grin","baseL") from _call_her_main_2054
    m "Not an antidote, but I do have a method that would alleviate the swelling."
    call her_main("...","annoyed","angry") from _call_her_main_2055
    call her_main("I'm listening...","annoyed","frown") from _call_her_main_2056
    m "Well as far as I can tell, your breasts are swelling due to an excess supply of milk."
    call her_main("...","annoyed","angry") from _call_her_main_2057
    m "If we somehow got it all out of there, I'm sure they'd revert to normal size in no time at all."
    call her_main("...","scream","wide_stare") from _call_her_main_2058
    call her_main("You can't be serious!","annoyed","annoyed") from _call_her_main_2059
    call her_main("Are you suggesting that I be milked! Like some sort of animal!","annoyed","annoyed") from _call_her_main_2060
    m "I'm simply offering a way to fix your problem."
    m "If you don't want my help then I'm afraid you'll have to go to class in your current condition."
    call her_main("*hmph*","annoyed","frown") from _call_her_main_2061
    call her_main("It can't be any worse than being milked.","open","suspicious") from _call_her_main_2062
    call her_main("Honestly, [genie_name], I'm shocked that you would even suggest something so completely ridiculous.","normal","frown") from _call_her_main_2063
    call her_main("I think I better get going...","annoyed","angryL") from _call_her_main_2064
    m "Well, 20 points to \"gryffindor\""
    $ gryffindor += 20
    call her_main("Thanks...","annoyed","suspicious") from _call_her_main_2065
    $ milking = -1
    
    call her_walk("mid","leave",2) from _call_her_walk_63
    
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_11_2: #Milking potion part 2
    #Genie offers hermione the potion again
    #She reluctantly accepts, but says that she expects to be paid double.
    #takes potion
    #comments on taste
    #wait
    #breasts expand
    #Genie offers milking
    #Hermione reluctantly accepts
    #Pulls out machine
    #Hermione shocked, expected to be by hand
    #Tries to refuse
    #Genie says she has already agreed
    #Upset, she puts on the milker
    #Slowly starts to work
    #Hermione is Cautious at first but gradually starts to enjoy it
    #starts to enjoy it a little too much
    #starts moaning, gets close to cumming
    #milking stops
    #she is somewhat upset but goes to class wearing expanded clothes
    
    m "[hermione_name], how would you like to try some nice milk?"
    call her_main("...","annoyed","frown") from _call_her_main_2066
    call her_main("is this the damn milk potion again sir?","scream","angryCl") from _call_her_main_2067
    m "maybe..."
    call nar(">You hand her the cloudy potion.","start") from _call_nar_287
    call nar(">Hermione cautiously smells the mixture.","end") from _call_nar_288
    call her_main("It is!","annoyed","angryL") from _call_her_main_2068
    call her_main("...","annoyed","frown") from _call_her_main_2069
    call her_main("well...","open","suspicious") from _call_her_main_2070
    call her_main("if you want me to drink this damn potion again...","open","suspicious") from _call_her_main_2071
    call her_main("I have two conditons...","annoyed","angryL") from _call_her_main_2072
    m "Name them."
    call her_main("One!","scream","angryCl") from _call_her_main_2073
    call her_main("I demand to be paid one hundred points!","scream","angryCl") from _call_her_main_2074
    call her_main("Two!","scream","angryCl") from _call_her_main_2075
    call her_main("I expect you to make the milking stop...","scream","worriedCl") from _call_her_main_2076
    m "Deal!"
    call her_main("Well alright then...","angry","worriedCl",emote="05") from _call_her_main_2077
    call nar(">Hermione takes one last look at the potion before closing her eyes...") from _call_nar_289
    
    call her_chibi("drink_potion","mid","base") from _call_her_chibi_94
    
    call her_main("...","full_cum","dead") from _call_her_main_2078
    call nar(">Hermione quickly gulps down the potion.") from _call_nar_290
    
    call her_chibi("stand","mid","base") from _call_her_chibi_95
    
    call her_main("Ah...","cum","worriedCl") from _call_her_main_2079
    call her_main("That doesn't actually taste too bad.","smile","baseL") from _call_her_main_2080
    m "Is it just like cows milk?"
    call her_main("Sort of...","open","suspicious") from _call_her_main_2081
    call her_main("It's a little sweeter...","upset","wink") from _call_her_main_2082
    call her_main("but not in a bad way...","base","baseL") from _call_her_main_2083
    call her_main("It also looks a little more yellow.","annoyed","down") from _call_her_main_2084
    m "Yes, well, you should notice it start to affect you soon."
    call her_main("Hmmm...","annoyed","down") from _call_her_main_2085
    call her_main("well how are you going to solve the milk problem, [genie_name]?","open","down") from _call_her_main_2086
    call her_main("Am I going to have to stand here...","base","ahegao_raised") from _call_her_main_2087
    call her_main("With my shirt off...","soft","squintL") from _call_her_main_2088
    
    call set_hermione_action("lift_top") from _call_set_hermione_action_57
    pause.5
    
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call set_hermione_action("none","skip_update") from _call_set_hermione_action_58
    pause.5
    
    call nar(">Hermione quickly removes her top.") from _call_nar_291
    call her_main("while you use your rough hands to milk me...","grin","ahegao") from _call_her_main_2089
    call her_main("like some sort of animal!","grin","dead") from _call_her_main_2090
    m "Not quite..."
    call nar(">YOu hand her the milking harness.") from _call_nar_292
    call her_main("What's this???","scream","wide") from _call_her_main_2091
    m "A milker."
    call her_main("Professor, Do you really expect me to put this on?","open","worriedCl") from _call_her_main_2092
    m "unless you want to go to class with those puppies full of milk."
    call her_main("but...","shock","worriedCl") from _call_her_main_2093
    call her_main("Can't you just do it by hand...","soft","ahegao") from _call_her_main_2094
    call her_main("I though it would be just like when you play with them normally...","angry","wink") from _call_her_main_2095
    m "No can do. I don't think I'd be able to get it all out before your classes anyway"
    call her_main("I'm sure there's tim-","base","worriedCl") from _call_her_main_2096
    
    if hermione_perm_expand_breasts or hermione_expand_breasts:
        pass
    else:
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded.png"
    
    call her_main("","shock","wide",cheeks="blush",trans="hpunch") from _call_her_main_2097
    pause.5
    
    call her_main("!!!","angry","worriedCl",cheeks="blush") from _call_her_main_2098
    call nar(">You notice hermione's breasts slight to swell slightly.") from _call_nar_293
    call her_main("[genie_name], they're growing rather quickly!","angry","worriedCl",cheeks="blush",emote="05") from _call_her_main_2099
    m "This is all perfectly normal."
    call her_main("please...","disgust","shocked",cheeks="blush") from _call_her_main_2100
    
    $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_large.png"
    with hpunch
    pause.5    
    
    call nar(">Hermione's breasts start to visibly swell again.") from _call_nar_294
    call her_main("ughhh...","grin","ahegao") from _call_her_main_2101
    
    $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png"
    with hpunch
    pause.5    
    
    call nar(">You notice hermione's breasts swell for the final time.") from _call_nar_295
    call her_main("!!!","upset","worriedCl",cheeks="blush") from _call_her_main_2102
    call her_main("[genie_name], this is ridiculous!","open","worriedCl",cheeks="blush") from _call_her_main_2103
    call her_main("do they have to be so big?","angry","angry",cheeks="blush") from _call_her_main_2104
    m "Yes."
    call her_main("...","annoyed","annoyed") from _call_her_main_2105
    call her_main("pervert.","open","annoyed",cheeks="blush") from _call_her_main_2106
    m "Well seeing as how they've reached full size..."
    call her_main("*hmph* Fine!","annoyed","annoyed") from _call_her_main_2107
    call her_main("Let me just put on your weird milking device that you own for some reason!","annoyed","angryL") from _call_her_main_2108
    m "Well technically I'm just borrowing it, so if you could make sure not to break it..."
    call her_main("...","annoyed","frown") from _call_her_main_2109
    call her_main("Ugh... the things I put up with for this house.","annoyed","suspicious") from _call_her_main_2110
    call nar(">hermione slowly slips the harness on.") from _call_nar_296
    
    $ milking = 1
    call set_hermione_action("milk_breasts") from _call_set_hermione_action_59
    
    call her_main("There! Happy now!","disgust","narrow") from _call_her_main_2111
    m "I mean if you could moo that would really Complete the picture..."
    call her_main("...","angry","angry") from _call_her_main_2112
    call her_main("can we just get this over with...","annoyed","angryL") from _call_her_main_2113
    m "Um... It's enchanted..."
    "(Does it have an on switch)"
    call her_main("Wait... This is an enchanted item? Please don't turn it on-","angry","base") from _call_her_main_2114
    call nar(">You hear a faint noise as the harness on hermione's chest springs to life.") from _call_nar_297
    
    $ milking = 2
    call set_hermione_action("milk_breasts") from _call_set_hermione_action_60
    
    call her_main("!!!","base","ahegao_raised",cheeks="blush") from _call_her_main_2115
    call her_main("{size=+5}OFF! TURN OFF!{/size}","shock","worriedCl") from _call_her_main_2116
    m "I think you need to wait until it's done."
    call her_main("Ugh...","open_tongue","ahegao_raised",cheeks="blush") from _call_her_main_2117
    call her_main("I can't...","open","worriedCl") from _call_her_main_2118
    call her_main("It's too much...","open","worriedCl") from _call_her_main_2119
    m "What's wrong?"
    call her_main("Ugh... it's the sucking...","open","worriedCl") from _call_her_main_2120
    call her_main("It's too intense!","shock","worriedCl") from _call_her_main_2121
    m "Can't you just ride it out?"
    call her_main("Ugh.... maybe... {p}I'll try.","silly","ahegao") from _call_her_main_2122
    call nar(">You wait a few more mintues as hermione is milked in front of you.") from _call_nar_298
    
    $ milking = 3
    call set_hermione_action("milk_breasts") from _call_set_hermione_action_61
    
    call her_main("...","open_wide_tongue","ahegao") from _call_her_main_2123
    call nar(">Her expression slowly fades from discomfort to pleasure.") from _call_nar_299
    call her_main("...","silly","dead") from _call_her_main_2124
    
    $ milking = 4
    call set_hermione_action("milk_breasts") from _call_set_hermione_action_62
    
    call nar(">The machine makes a pleasant sounding click as it looks to turn off.") from _call_nar_300
    m "Alright, well, look like you're good to head off to class."
    call her_main("What?","annoyed","angryL") from _call_her_main_2125
    call her_main("Can't you leave it on...","open","worriedCl") from _call_her_main_2126
    m "I'm afraid not."
    m "(I don't even know how it turns on...)"
    call her_main("But I was so close...","shock","worriedCl") from _call_her_main_2127
    call her_main("...","annoyed","angryL") from _call_her_main_2128
    call her_main("Fine... I better get to potions class then...","annoyed","down") from _call_her_main_2129
    
    hide screen hermione_main
    call blkfade from _call_blkfade_91
    
    call nar(">Hermione takes off the harness. You see the passing look of regret on her face.") from _call_nar_301
    
    $ hermione_expand_breasts = True
    call h_action("none") from _call_h_action_29
    call update_her_uniform from _call_update_her_uniform_45
    pause.5
    hide screen bld1
    call hide_blkfade from _call_hide_blkfade_47
    
    m "Feel better?"
    call her_main("Surprisingly yes...","annoyed","base") from _call_her_main_2130
    call her_main("They even seem like they've shrunk a little bit.","open","down") from _call_her_main_2131
    call her_main("So you're sure they're not going to leak anymore?","open","suspicious") from _call_her_main_2132
    m "oh um, no of course not..."
    call her_main("...","normal","frown") from _call_her_main_2133
    call her_main("well I'd like to be paid now [genie_name]...","annoyed","angryL") from _call_her_main_2134


    m "Oh yes, quite right. 100 points to \"gryffindor\"!"
    $ gryffindor += 100
    
    call her_main("Thank you sir...","open","suspicious") from _call_her_main_2135
    call her_main("(Although I still have to head to class with these huge things...)","annoyed","angryL") from _call_her_main_2136
    call her_main("(not that I mind the extra attention...)","soft","squintL") from _call_her_main_2137

    $ milking = 0

    call her_walk("mid","leave",2) from _call_her_walk_64
    
    $ hermione_takes_classes = True
    $ hermione_sleeping = True #this is intentional 
    jump day_main_menu

label potion_scene_11_3: #Milking potion part 3
    $ milking = 0
    #Genie offers hermione the potion
    #Agrees on the condition that she milks him
    #Genie agrees
    #option to add extra ingredient
    #Hermione drinks potion
    #Comments that the milk tastes sweeter than regular milk
    #wait
    #Breasts expand
    #takes her top off

    #option 1 (futa)

    #option 2 (Permanent expansion)
    m "[hermione_name], feel like a milkshake?"
    call her_main("Really? Strawberry, please!","smile","happyCl",emote="06") from _call_her_main_2138
    m "I've only got vanilla, sorry..."
    call nar(">You hand her the cloudy potion.","start") from _call_nar_302
    call nar(">Hermione cautiously smells the mixture.","end") from _call_nar_303
    call her_main("This is that damn milk again!","angry","wide") from _call_her_main_2139
    call her_main("...","annoyed","frown") from _call_her_main_2140
    call her_main("I wanted a milkshake...","annoyed","down") from _call_her_main_2141
    m "I'm sure if you shake the bottle it'll go frothy."
    call her_main("It's not the same!","scream","angryCl") from _call_her_main_2142
    call her_main("There's no sugar or flavouring!","annoyed","frown") from _call_her_main_2143
    
    if potion_version > 1:
        m "well, this one does have an extra ingredient..."
        call her_main("Really?","angry","wink") from _call_her_main_2144
        call her_main("Is it Strawberry?","soft","ahegao") from _call_her_main_2145
        m "WHy don't you have a taste and find out?"
        call her_main("Alright then...","open","suspicious") from _call_her_main_2146
        call her_main("(I hope it's Strawberry!)","smile","happyCl",emote="06") from _call_her_main_2147
    else:
        m "Just drink it..."
        call her_main("*hmph* fine...","open","suspicious") from _call_her_main_2148
        call her_main("(At the very least he should have added chocolate flavouring...)","open","suspicious") from _call_her_main_2149
        
    call nar(">Hermione takes one last look at the potion before closing her eyes...") from _call_nar_304
    
    call her_chibi("drink_potion","mid","base") from _call_her_chibi_96
    
    call nar(">Hermione quickly gulps down the potion.") from _call_nar_305
    
    call her_chibi("stand","mid","base") from _call_her_chibi_97
    
    call her_main("Ah...","cum","worriedCl") from _call_her_main_2150
    call her_main("That wasn't Strawberry!","annoyed","annoyed") from _call_her_main_2151
    m "Did you really think it would be?"
    call her_main("I mean... Sort of?","annoyed","down") from _call_her_main_2152
    call her_main("you are a wizard after all...","annoyed","down") from _call_her_main_2153
    call her_main("the house elfs make me a milkshake whenever i ask...","annoyed","angry") from _call_her_main_2154
    m "Speaking of milkshakes!"
    call nar(">You notice hermione's breasts start to swell...") from _call_nar_306
    call her_main("Ugh... this always feels so weird...","angry","down_raised") from _call_her_main_2155
    
    if hermione_wear_top:
        call her_main("I better take my shirt off before \'they\' rip the buttons...","normal","frown") from _call_her_main_2156
    else:
        if hermione_wear_bra:
            call her_main("I better take my bra off before \'they\' rip the buttons...","normal","frown") from _call_her_main_2157
    
    call set_hermione_action("lift_top") from _call_set_hermione_action_63
    pause.5
    
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call set_hermione_action("none","skip_update") from _call_set_hermione_action_64
    pause.5
    
    if hermione_perm_expand_breasts or hermione_expand_breasts:
        pass
    else:
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded.png" 
        with hpunch
        pause.5    
    
    
    if not potion_version == 2: #Orgasms while milking
        call her_main("!!!","angry","wide") from _call_her_main_2158
        call nar(">You notice hermione's breasts start to grow a little more.") from _call_nar_307
        call her_main("ugh...","grin","ahegao") from _call_her_main_2159
        m "mmmm, just like that."
        call her_main("(this is so weird...)","angry","down_raised") from _call_her_main_2160
        
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_large.png" 
        with hpunch
        pause.5    
    
        call her_main("!!!","angry","wide") from _call_her_main_2161
        call nar(">Hermione's breasts start to visibly swell again.") from _call_nar_308
        
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        with hpunch
        pause.5    
    
        call her_main("!!!","angry","down_raised") from _call_her_main_2162
        call nar(">You notice hermione's breasts swell for the final time.") from _call_nar_309
        call her_main("[genie_name], this is ridiculous!","annoyed","annoyed") from _call_her_main_2163
        call her_main("did you make the potion stronger this time?","annoyed","angryL") from _call_her_main_2164
        m "What are you talking about, they're the same size as always."
        call her_main("are you sure...","annoyed","frown") from _call_her_main_2165
        call nar(">Hermione jiggles her boobs side to side.") from _call_nar_310
        call her_main("They just feel so much ...heavier... than before.","annoyed","down") from _call_her_main_2166
        m "Well seeing as how you emptied them of their milk last time, maybe they made more..."
        call her_main("they better not have...","shock","worriedCl") from _call_her_main_2167
        call her_main("just hand me the milker so I can get to class...","annoyed","annoyed") from _call_her_main_2168
        m "Is that the only reason you want it?"
        call her_main("What? Why else would I want it?","open","baseL") from _call_her_main_2169
        m "I seem to remember you enjoying yourself with it last time."
        call her_main("You really are disgusting sometimes, [genie_name]...","annoyed","angryL") from _call_her_main_2170
        m "Whatever you say..."
        call nar(">You hand hermione the harness.","start") from _call_nar_311
        call nar(">hermione takes it from your hands and slowly slips it on, taking care to make sure the cups fit.","end") from _call_nar_312
        
        $ milking = 1
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_65
        
        call her_main("...","upset","worriedCl",cheeks="blush") from _call_her_main_2171
        m "are you sure you can't moo?..."
        call her_main("...","soft","squintL") from _call_her_main_2172
        call her_main("{size=-5}moo...{/size}","open","baseL") from _call_her_main_2173
        m "what was that?"
        call her_main("I'm not saying it again, [genie_name]... {size=-5}once is enough...{/size}","annoyed","angryL") from _call_her_main_2174
        call her_main("...","annoyed","down") from _call_her_main_2175
        call her_main("on!","open","worriedCl") from _call_her_main_2176
        call nar(">You hear a faint noise as the harness on hermione's chest springs to life.") from _call_nar_313
        
        $ milking = 2
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_66
        
        call her_main("!!!","soft","squintL") from _call_her_main_2177
        call her_main("Ugh... it feels different this time...","open","worriedCl") from _call_her_main_2178
        call her_main("like there's so much more in my breasts...","shock","worriedCl") from _call_her_main_2179
        call her_main("and it all wants to come out...","silly","dead") from _call_her_main_2180
        call her_main("It's too much...","silly","ahegao") from _call_her_main_2181
        m "What's wrong?"
        call her_main("ah... it's the sucking...","grin","ahegao") from _call_her_main_2182
        call her_main("It's not like before!","silly","ahegao") from _call_her_main_2183
        m "is it hurting you?"
        call her_main("ah.... no... {p}It's not bad...","silly","dead") from _call_her_main_2184
        
        $ milking = 3
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_67
        
        call her_main("ah...{image=textheart}{image=textheart}{image=textheart}","grin","dead") from _call_her_main_2185
        call nar(">You notice the canister in front of her fill with milk at an alarming rate...") from _call_nar_314
        call her_main("ah... it's so good...","grin","ahegao") from _call_her_main_2186
        
        $ milking = 4
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_68
        
        call nar(">The machine makes a pleasant sounding click as it looks to turn off.") from _call_nar_315
        m "Alright, well, look like you're good to head off to class."
        call her_main("What? but sir...","open","worriedCl") from _call_her_main_2187
        call her_main("they're still so full...","shock","worriedCl") from _call_her_main_2188
        m "it looks like the machine is full, I'm afraid."
        call her_main("(But I was so close...)","open","worriedCl") from _call_her_main_2189
        call her_main("ah... and if I go to class like this I'll leak everywhere!","shock","worriedCl") from _call_her_main_2190
        m "well, if you empty the cannister It'll probably turn back on."
        call her_main("empty it...","angry","wink") from _call_her_main_2191
        call nar(">Hermione takes a look at the full milk cannister.") from _call_nar_316
        call her_main("Can I just pour it out on the floor then?","annoyed","down") from _call_her_main_2192
        m "And waste all that nutritious milk?"
        
        menu:
            "-make her drink it-":
                call her_main("Do you want to drink it then, [genie_name]?","angry","wink") from _call_her_main_2193
                m "Um, I'm afraid not... I just had a big bowl of cereal."
                call her_main("...","annoyed","down") from _call_her_main_2194
                call her_main("Then do you have a bottle for me to store it in...","angry","wink") from _call_her_main_2195
                m "fresh out..."
                call her_main("...","annoyed","angryL") from _call_her_main_2196
                m "I'm afraid you'll have to drink it yourself."
                call her_main("...","soft","squintL") from _call_her_main_2197
                call her_main("{size=-5}alright...{/size}","open","baseL") from _call_her_main_2198
                m "Really?"
                call her_main("It's not like I can go to class leaking milk again...","annoyed","angryL") from _call_her_main_2199
                call her_main("and besides, it's not the worst feeling in the world...","angry","down_raised") from _call_her_main_2200
                call her_main("I wouldn't mind giving the machine another go...","soft","ahegao") from _call_her_main_2201
                m "Well, bottoms up!"
                call her_main("...","annoyed","down") from _call_her_main_2202
                
                $ milking = 5
                call set_hermione_action("milk_breasts") from _call_set_hermione_action_69
                
                call nar(">Hermione gives the cannister one final look before unscrewing it and putting it to her lips.") from _call_nar_317
                call her_main("(For gryffindor!)","scream","angryCl") from _call_her_main_2203
                call nar(">She takes a mouthful of her own milk.") from _call_nar_318
                call her_main("...","full_cum","dead") from _call_her_main_2204
                call her_main("*gulp*","cum","worriedCl") from _call_her_main_2205
                call nar(">She takes the last half into her mouth.") from _call_nar_319
                call her_main("...","full_cum","dead") from _call_her_main_2206
                call her_main("*gulp*","cum","worriedCl") from _call_her_main_2207
                call her_main("ah...","grin","dead") from _call_her_main_2208
                call her_main("I think I'll need to skip a meal after all this milk...","angry","wink") from _call_her_main_2209
                call nar(">She slowly screws the cannister back into milker.") from _call_nar_320
                
                $ milking = 1
                call set_hermione_action("milk_breasts") from _call_set_hermione_action_70
                
                call her_main("...","base","down") from _call_her_main_2210
                call her_main("on!","open","closed") from _call_her_main_2211
                call nar(">The milker once again comes to life as it starts to milk Hermione for a second time.") from _call_nar_321
                
            "-drink it yourself-":
                call her_main("Do you want to drink it then, [genie_name]?","angry","wink") from _call_her_main_2212
                m "Waste not, want not!"
                call her_main("...","angry","wide") from _call_her_main_2213
                call her_main("well, here you are then...","angry","base") from _call_her_main_2214
                
                $ milking = 5
                call set_hermione_action("milk_breasts") from _call_set_hermione_action_71
                
                call nar(">Hermione gives the cannister one final look before unscrewing it and handing it to you.") from _call_nar_322
                call her_main("(weirdo...)","angry","down_raised") from _call_her_main_2215
                call nar(">you take a mouthful of her milk.") from _call_nar_323
                m "Mmmmmm... Delicious!"
                call her_main("...","angry","wink") from _call_her_main_2216
                call her_main("really? You liked my milk?","open","baseL") from _call_her_main_2217
                m "More than water from an oasis!"
                call her_main("...","annoyed","angryL") from _call_her_main_2218
                call her_main("well...","soft","squintL") from _call_her_main_2219
                call her_main("Are you going to finish it?","smile","angry") from _call_her_main_2220
                call nar(">You finish the cannister in one final mouthful.") from _call_nar_324
                call her_main("...","smile","happyCl") from _call_her_main_2221
                call nar(">She slowly screws the cannister back into milker.") from _call_nar_325
                
                $ milking = 1
                call set_hermione_action("milk_breasts") from _call_set_hermione_action_72
                
                call her_main("(I can't believe he liked it...)","smile","baseL") from _call_her_main_2222
                call her_main("(maybe it does taste good...)","grin","baseL") from _call_her_main_2223
                call her_main("...","base","down") from _call_her_main_2224
                call her_main("on!","open","closed") from _call_her_main_2225
                call nar(">The milker once again comes to life as it starts to milk Hermione for a second time.") from _call_nar_326


        call her_main("!!!","grin","dead") from _call_her_main_2226
        call her_main("ugh... it's so gooood...","grin","ahegao") from _call_her_main_2227
        $ hermione_dribble = True
        
        $ milking = 2
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_73
        
        call her_main("ah... it's like the straps are massaging me while it sucks...","silly","dead") from _call_her_main_2228
        call her_main("mmmm... it's amazing...","silly","ahegao") from _call_her_main_2229
        call nar(">Hermione lets the machine continue its work.") from _call_nar_327
        
        $ milking = 3
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_74
        
        call her_main("ah... I think that's all of it, [genie_name]...","annoyed","down") from _call_her_main_2230
        call nar(">You notice the amount of milk coming from hermione's breasts has almost stopped.") from _call_nar_328
        m "How was it?"
        call her_main("it felt amazing...","grin","ahegao") from _call_her_main_2231
        call her_main("it even almost made me cum...","base","down") from _call_her_main_2232
        call her_main("but you can turn it off now...","angry","wink") from _call_her_main_2233
        m "Um..."
        call nar(">The machine struggles to suck any more milk from hermione's heaving chest.") from _call_nar_329
        m "I'm not sure how... I think it only shuts off when it's full?"
        call her_main("well I don't think it's going to be able to get much more-","upset","closed") from _call_her_main_2234
        call nar(">You hear the harness start to whir, like a vacuum cleaner caught on carpet.") from _call_nar_330
        call her_main("!!!","disgust","shocked",cheeks="blush") from _call_her_main_2235
        call nar(">You hear a strange click come from the harness.") from _call_nar_331
        "*Zzzzkkk*"
        
        call cum_block from _call_cum_block_32
        $ hermione_squirt = True
        
        call her_main("Ah!!!","grin","ahegao_mad",cheeks="blush") from _call_her_main_2236
        call nar(">You see a small squirt of milk come out of hermione's nipples.") from _call_nar_332
        $ hermione_squirt = False
        
        call nar(">The cannister is still barely more than half full.") from _call_nar_333
        "*Zzzzkkk*"
        
        call cum_block from _call_cum_block_33
        $ hermione_squirt = True
        
        call her_main("{size=+5}Ah!!!{/size}","silly","ahegao") from _call_her_main_2237
        call nar(">Another small squirt of milk comes out of hermione's nipples.") from _call_nar_334
        $ hermione_squirt = False
        
        call her_main("{size=+5}It's making me cum!{/size}","shock","worriedCl") from _call_her_main_2238
        call her_main("{size=+5}why is it-{/size}","open","worriedCl") from _call_her_main_2239
        "*Zzzzkkk*"
        
        call cum_block from _call_cum_block_34
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","silly","dead") from _call_her_main_2240
        $ hermione_squirt = False
        "*Zzzzkkk*"
        
        call cum_block from _call_cum_block_35
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","grin","ahegao") from _call_her_main_2241
        $ hermione_squirt = False
        
        hide screen hermione_main
        call blkfade from _call_blkfade_92
        
        call nar(">The machine continues for another couple of minutes. Each crack is accompanied by a small squirt of milk into the cups...") from _call_nar_335
        
        $ milking = 4
        call h_action("milk_breasts") from _call_h_action_30
        pause.5
        call hide_blkfade from _call_hide_blkfade_48

        call her_main("...","open_wide_tongue","ahegao") from _call_her_main_2242
        call nar(">Hermione stands before you, unable to speak.") from _call_nar_336
        m "Oh um... 20 points to \"gryffindor\"!"
        $ gryffindor += 20
        call her_main("...","open_wide_tongue","ahegao") from _call_her_main_2243
        m "And I'll be needing this back."
        call her_main("...","open_wide_tongue","ahegao") from _call_her_main_2244
        call blkfade from _call_blkfade_93
        
        call nar(">You slowly remove the milk filled harness. There are red marks, surrounding her tender-looking nipples, where the cups were.") from _call_nar_337
        call h_action("none","skip_update") from _call_h_action_31
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        m "Hmmm... maybe we overdid it a little today."
        call hide_blkfade from _call_hide_blkfade_49
        
        call her_main("...","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2245
        m "Why don't you head back to your room... I think you've earned a day off."
        call her_main("yes...","silly","dead") from _call_her_main_2246
        call her_main("I'll go now...","silly","ahegao") from _call_her_main_2247
        m "Maybe you should get dressed first..."
        call her_main("...","grin","ahegao") from _call_her_main_2248
        call blkfade from _call_blkfade_94
        
        call nar(">Hermione slowly dresses herself, fumbling at every point.") from _call_nar_338
        
        $ hermione_perm_expand_breasts = True #Temporary.
        call h_action("none") from _call_h_action_32 #Resets clothing.
        call hide_blkfade from _call_hide_blkfade_50
        
        call her_main("good bye, sir...","silly","dead") from _call_her_main_2249
        if potion_version == 2:
            call nar(">Hermione's breasts will now be permanently large thanks to Snape's added ingredient.","start") from _call_nar_339
            call nar(">however, Making her take the potion again may reset the effect...","end") from _call_nar_340



    else: #futa variant
        call nar(">You notice hermione's breasts start to grow a little more.") from _call_nar_341
        call her_main("!!!","angry","wide") from _call_her_main_2250
        # change boobs
        call her_main("ugh...","grin","ahegao") from _call_her_main_2251
        m "mmmm, just like that."
        call her_main("(this is so weird...)","angry","down_raised") from _call_her_main_2252
        
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_large.png" 
        with hpunch
        pause.5
        
        call her_main("!!!","angry","wide") from _call_her_main_2253
        call nar(">Hermione's breasts start to visibly swell again.") from _call_nar_342
        
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        with hpunch
        pause.5
        
        call her_main("!!!","angry","down_raised") from _call_her_main_2254
        call nar(">You notice hermione's breasts swell for the final time.") from _call_nar_343
        call her_main("[genie_name], this is ridiculous!","annoyed","annoyed") from _call_her_main_2255
        call her_main("did you make the potion stronger this time?","annoyed","angryL") from _call_her_main_2256
        m "Well there was an extra ingredient in there..."
        call her_main("What? are my boobs going to get even bigger?","annoyed","angryL") from _call_her_main_2257
        call nar(">Hermione jiggles her boobs side to side.") from _call_nar_344
        call her_main("I don't think I'd be able to stand!","annoyed","down") from _call_her_main_2258
        m "Your breasts shouldn't grow any bigger..."
        call her_main("Oh...","base","down") from _call_her_main_2259
        m "You may notice something else start to grow however."
        call her_main("What? Not cat ears again please...","annoyed","angryL") from _call_her_main_2260
        m "Don't worry, it's-- Uhm... it's something else..."
        call her_main("...","angry","wide") from _call_her_main_2261
        call her_main("wait...","angry","down_raised") from _call_her_main_2262
        call her_main("you don't mean...","disgust","down_raised") from _call_her_main_2263
        call her_main("you wouldn't... would you?","annoyed","angryL") from _call_her_main_2264
        m "We'll just have to wait and see..."
        call her_main("You really are a disgusting pervert [genie_name]...","open","annoyed",cheeks="blush") from _call_her_main_2265
        m "Whatever you say..."
        call her_main("Please tell me I'm not going to grow a damn d-","angry","down_raised") from _call_her_main_2266
        
        hide screen hermione_main
        call h_action("lift_skirt") from _call_h_action_33
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        show screen hermione_main
        with d3
        pause.5
        
        hide screen hermione_main
        $ hermione_wear_bottom = False
        $ hermione_wear_panties = False
        call h_action("none","skip_update") from _call_h_action_34
        $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        show screen hermione_main
        with d3
        pause.5
        
        call her_main("...","angry","wide") from _call_her_main_2267
        
        $ hermione_futa = True
        
        call her_main("","shock","down_raised",trans="hpunch") from _call_her_main_2268
        pause.8
        
        call her_main("You damn {size=+10}pervert!{/size}","shock","worriedCl",cheeks="blush") from _call_her_main_2269
        g9 "Woah! Nice..."
        call her_main("Nice? How is this nice?","scream","angry",emote="01") from _call_her_main_2270
        call her_main("I have a damn {size=+10}cock!{/size}","angry","angry",emote="01") from _call_her_main_2271
        m "Come on [hermione_name]... where's your sense of adventure?"
        call her_main("Adventure?","annoyed","annoyed") from _call_her_main_2272
        call her_main("Going into the chamber of secrets was an adventure sir...","open","suspicious") from _call_her_main_2273
        call her_main("Standing in my headmasters office while he makes me drink some random potion he probably found in the gutter-","scream","angryCl") from _call_her_main_2274
        call her_main("-That makes me have huge, {size=+3}lactating{/size}, {size=+5}tits{/size} and a giant {size=+10}{b}DICK{/b}{/size} is {size=+2}not {size=+2}an {size=+4}adventure!{/size}","scream","angry",emote="01") from _call_her_main_2275
        m "Don't forget about the magical milking machine..."
        call nar(">You hand hermione the milking harness.") from _call_nar_345
        m "Surely this makes it an adventure..."
        call her_main("What do you expect me to do with this?","annoyed","frown") from _call_her_main_2276
        call her_main("It's hardly going to be able to get rid of this {size=+10}DICK{/size} now is it.","angry","angry") from _call_her_main_2277
        m "Actually, it should."
        m "(I hope it does anyway... Snape did say it was magic.)"
        call her_main("really?","annoyed","annoyed") from _call_her_main_2278
        m "Really, really."
        call her_main("Ugh, fine... (the stuff I put up with)","annoyed","angryL") from _call_her_main_2279
        call nar(">hermione takes it from your hands and goes to put it on.") from _call_nar_346
        call her_main("Where's my stupid dick supposed to go...","angry","base") from _call_her_main_2280
        call her_main("It's in the way of the cannister.","angry","down_raised") from _call_her_main_2281
        m "Try sticking it into the bottom of the cannister."
        call her_main("What... why would that-","annoyed","annoyed") from _call_her_main_2282
        
        $ milking = 1
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_75
        
        call her_main("!!!","silly","dead") from _call_her_main_2283
        m "how's that?"
        call her_main("I'm sorry about being angry before [genie_name]...","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2284
        call her_main("I didn't know it would feel like this...","grin","ahegao") from _call_her_main_2285
        m "like what?"
        call her_main("It's so fricking good...","silly","ahegao") from _call_her_main_2286
        call her_main("I never though sex could be like this...","silly","dead") from _call_her_main_2287
        call her_main("being inside something...","silly","ahegao") from _call_her_main_2288
        call her_main("It's the best!","grin","ahegao") from _call_her_main_2289
        call her_main("At this rate I'll cum before we even have to turn the thing on-","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2290
        call nar(">You hear a faint noise as the harness on hermione's chest springs to life.") from _call_nar_347
        
        $ milking = 2
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_76
        
        call her_main("!!!","grin","dead") from _call_her_main_2291
        call her_main("no!","clench","worried",cheeks="blush",tears="soft") from _call_her_main_2292
        call her_main("Stop it!","angry","suspicious",cheeks="blush") from _call_her_main_2293
        call her_main("{size=+5}I'm serious!!!{/size}","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2294
        call her_main("{size=+10}It's too much... TURN it off!!!{/size}","scream","wide") from _call_her_main_2295
        m "What's wrong?"
        call her_main("ah... it's sucking {b}everything{/b}...","silly","ahegao") from _call_her_main_2296
        call her_main("ah... and the milk is splashing on my {image=textheart}dick{image=textheart}......","grin","ahegao") from _call_her_main_2297
        m "is it hurting you?"
        call her_main("ah.... no... {p}It's just too good...{image=textheart}","grin","dead") from _call_her_main_2298
        
        $ milking = 3
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_77
        
        call her_main("ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead") from _call_her_main_2299
        call nar(">You notice the canister in front of her fill with milk at an alarming rate...") from _call_nar_348
        call her_main("ah... please [genie_name]...","angry","suspicious",cheeks="blush") from _call_her_main_2300
        call her_main("ah... you have to turn it off...","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_2301
        call her_main("{size=-2}i'll {size=-2}go {size=-2}insane {size=-2}if {size=-2}you {size=-2}don't...{/size}","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2302
        
        $ milking = 4
        call set_hermione_action("milk_breasts") from _call_set_hermione_action_78
        
        call nar(">You notice the cannister fill, yet the machine keeps working.") from _call_nar_349
        call her_main("What? but it's full...","annoyed","down") from _call_her_main_2303
        call her_main("it should turn off...","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2304
        call her_main("please... let it turn off...","angry","suspicious",cheeks="blush",tears="messy") from _call_her_main_2305
        m "(What did snape say again? untellable extension ham?)"
        m "Well i should have mentioned something about that cannister being extended invisibly...."
        call her_main("Did you put an undetectable extension charm on this cannister?","open","surprised",cheeks="blush",tears="messy") from _call_her_main_2306
        call her_main("{size=+5}did you?!{/size}","scream","suspicious",cheeks="blush",tears="messy") from _call_her_main_2307
        m "Possibly."
        call her_main("no...","scream","worriedCl",cheeks="blush",tears="messy") from _call_her_main_2308
        call nar(">Hermione takes a look at the full milk cannister.") from _call_nar_350
        call her_main("Will it ever stop?","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_2309
        m "ahhhh..."
        call her_main("!!!","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2310
        call her_main("ugh... {image=textheart}it's so{image=textheart} gooood...","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2311
        
        $ hermione_dribble = True
        call her_main("ah... the straps are massaging me while it sucks my dick...","silly","ahegao") from _call_her_main_2312
        call her_main("mmmm... it's amazing...{image=textheart}{image=textheart}","grin","ahegao") from _call_her_main_2313
        call nar(">Hermione lets the machine continue it's work.") from _call_nar_351
        call her_main("...","open_wide_tongue","ahegao") from _call_her_main_2314
        call nar(">You notice the amount of milk coming from hermione's breasts has almost stopped.") from _call_nar_352
        call her_main("it feels amazing...","grin","ahegao") from _call_her_main_2315
        call her_main("it's made me cum so much...","silly","ahegao") from _call_her_main_2316
        call nar(">The machine struggles to suck any more milk from hermione's heaving chest.") from _call_nar_353
        m "Well hopefully it has a safety mechanism for when you're out of milk..."
        call her_main("well that should be soon-","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2317
        call nar(">You hear the harness start to whir, like a vacuum cleaner caught on carpet.") from _call_nar_354
        call her_main("!!!","angry","wide") from _call_her_main_2318
        call nar(">You hear a strange click come from the harness.") from _call_nar_355
        "*Zzzzkkk*"
        
        call cum_block from _call_cum_block_36
        $ hermione_squirt = True
        
        call her_main("{size=+15}!!!{image=textheart}{image=textheart}{image=textheart}!!!{/size}","grin","dead") from _call_her_main_2319
        call nar(">You see a small squirt of milk come out of hermione's nipples.") from _call_nar_356
        $ hermione_squirt = False
        
        call nar(">The cannister still looks completely full.") from _call_nar_357
        "*Zzzzkkk*"
        
        call cum_block from _call_cum_block_37
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","grin","dead") from _call_her_main_2320
        call nar(">Another small squirt of milk comes out of hermione's nipples.") from _call_nar_358
        $ hermione_squirt = False
        
        call her_main("{size=+5}It's making me cum so {b}hard{/b}...{/size}","silly","worried",cheeks="blush",tears="soft") from _call_her_main_2321
        call her_main("{size=+5}why is it-{/size}","shock","baseL",cheeks="blush",tears="soft") from _call_her_main_2322
        "*Zzzzkkk*"
        
        call cum_block from _call_cum_block_38
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","grin","ahegao") from _call_her_main_2323
        $ hermione_squirt = False
        
        "*Zzzzkkk*"
        
        call cum_block from _call_cum_block_39
        $ hermione_squirt = True
        
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","silly","ahegao") from _call_her_main_2324
        $ hermione_squirt = False
        call blkfade from _call_blkfade_95
        
        call nar(">The machine continues for another couple of minutes. Each crack is accompanied by a small squirt of milk into the cups and a pulse of her cock into the cannister...") from _call_nar_359
        
        $ milking = 4
        call h_action("milk_breasts") from _call_h_action_35
        call nar(">You let it continue for a little longer before it finally stops.") from _call_nar_360
        call hide_blkfade from _call_hide_blkfade_51

        call her_main("{size=-10}t-turn it...{/size}","angry","suspicious",cheeks="blush") from _call_her_main_2325
        call nar(">Hermione stands before you, barely able to speak.") from _call_nar_361
        call her_main("{size=-8}t-turn it...{/size}","angry","suspicious",cheeks="blush") from _call_her_main_2326
        call her_main("{size=-6}t-turn it...{/size}","angry","suspicious",cheeks="blush") from _call_her_main_2327
        call her_main("{size=-4}t-turn it... up...{/size}","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2328
        m "I think you've had enough... 20 points to \"gryffindor\"!"
        $ gryffindor += 20
        call her_main("...","angry","suspicious",cheeks="blush") from _call_her_main_2329
        call nar(">And I'll be needing this back.") from _call_nar_362
        call her_main("...","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_2330
        call blkfade from _call_blkfade_96
        
        call nar(">You slowly remove the milk filled harness. There are red marks, surrounding her tender looking nipples, where the cups were.") from _call_nar_363
        call h_action("none","skip_update") from _call_h_action_36
        $ hermione_futa = False
        $ hermione_dribble = False
        
        call nar(">As you pull the heavy cannister off her cock it flops down before wilting away into nothingness.") from _call_nar_364
        m "(eww...)"
        m "Hmmm, I think you probably overdid it a little today."
        call hide_blkfade from _call_hide_blkfade_52
        
        call her_main("{size=-6}more...{/size}","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2331
        m "Why don't you head back to your room... I think you've earned another day off."
        call her_main("yes...","angry","suspicious",cheeks="blush") from _call_her_main_2332
        call her_main("I'll go now...","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_2333
        m "Maybe you should get dressed first..."
        call her_main("...","angry","dead",cheeks="blush",tears="crying") from _call_her_main_2334
        
        call blkfade from _call_blkfade_97
        call nar(">Hermione slowly dresses herself, fumbling at every point.") from _call_nar_365
        
        $ hermione_perm_expand_breasts = True #Temporary.
        call h_action("none") from _call_h_action_37 #Resets clothes.
        call hide_blkfade from _call_hide_blkfade_53
        
        call her_main("good bye sir...","shock","down_raised",cheeks="blush",tears="crying") from _call_her_main_2335


    $ milking = 0
    
    call her_walk("mid","leave",2) from _call_her_walk_65
    
    $ hermione_takes_classes = True
    $ hermione_sleeping = True
    
    if potion_version == 3:
        $ hermione_perm_expand_breasts = True
        
    $ hermione_expand_breasts = True #Temporary one.
    $ hermione_expand_breasts_counter = 0 #If 0 resets temporary one the next day.
        
    jump day_main_menu



label potion_scene_11_1_2: #Milking potion part 1 night time
    $ aftersperm = True
    $ milking = 0
    
    call play_sound("door") from _call_play_sound_93
    call her_walk("door","desk",2.5) from _call_her_walk_66
    
    call her_main("Professor! why didn't you warn me about this!","angry","angry",xpos="right",ypos="base") from _call_her_main_2336
    
    m "About what? I told you your breasts would expand."
    call her_main("Look at my shirt!","angry","angry",emote="01") from _call_her_main_2337
    m "Hmmm, seems like you had a bit of an accident."
    call her_main("An accident?","open","suspicious") from _call_her_main_2338
    call her_main("I've been leaking milk all day!","scream","angry",emote="01") from _call_her_main_2339
    m "It doesn't seem that bad..."
    call her_main("This is the third shirt that I've had to wear today!","open","angryCl") from _call_her_main_2340
    call her_main("All the others are soaked through!","angry","angry") from _call_her_main_2341
    call her_main("Even my vest is soaked...","annoyed","frown") from _call_her_main_2342
    m "Well I did offer to relieve your issue..."
    call her_main("by milking me like some sort of... animal!","angry","angry") from _call_her_main_2343
    call her_main("I'm upset you'd even think that would be a possibility.","angry","annoyed",emote="01") from _call_her_main_2344
    m "Well it would have solved your \'problem\'."
    call her_main("...","open","suspicious") from _call_her_main_2345
    call her_main("Well I expect to be paid extra after this humiliation.","annoyed","annoyed") from _call_her_main_2346
    m "how much?"
    call her_main("30 points.","annoyed","angry") from _call_her_main_2347
    m "Fine, 30 points to \"gryffindor\"."
    $ gryffindor += 30 
    call her_main("*hmph*","annoyed","annoyed") from _call_her_main_2348
    call her_main("So when are these \'things\' going to go away? Or do I have to go get one of the nurses to shrink them?","angry","annoyed",emote="01") from _call_her_main_2349
    m "They should go back to normal Sometime tonight."
    call her_main("good...","open","suspicious") from _call_her_main_2350
    call her_main("but don't think I've forgiven you!","open","angryCl") from _call_her_main_2351
    call nar(">Hermione storms out in a huff.") from _call_nar_366
    $ mad =+ 10
    
    call her_walk("desk","leave",2.5) from _call_her_walk_67
    
    $ hermione_sleeping = True
    $ aftersperm = False
    
    m "(bitches... you'd think she'd be happy to get some {size=+5}big kahunas{/size} for free!)"
    
    return
    
    #comes back after class
    #shirt covered in milk stains
    #furious at genie 
    #Genie responds saying he should have let him milk her
    #Hermione is angry again at him for suggesting it
    #demands more points 
    #asks when they're going to go away
    #genie says she has to get the milk out of them
    #offers to milk her again
    #refuses and says she can take care of it herself
    #leaves

label potion_scene_11_2_2: #Milking potion part 2 night time
    m "asd"
    #comes back after class
    #breasts still expanded
    #genie asks her how her day was
    #She had a good day
    #Appreciates the attention from everyone
    #Milking prevented her from leaking
    #Says she wouldn't mind taking the potion again some time

