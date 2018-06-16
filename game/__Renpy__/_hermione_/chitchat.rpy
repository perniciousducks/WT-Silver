

### Hermione Chitchats ###

label chit_chat:
    #$ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    
    
    ### WHORING LEVEL 01 ###
    if whoring >= 0 and whoring <= 2:
        if one_of_ten == 1:
            call her_main("Maybe, if I'd work harder, I could squeeze a few more classes into my schedule...","open","angryCl") from _call_her_main_5160
            call her_main("","normal","base") from _call_her_main_5161
        
        elif one_of_ten == 2:
            call her_main("Actually, I don't mind being called a \"know-it-all\".","open","angryCl") from _call_her_main_5162
            her "I think it's rather flattering..."
            call her_main("","normal","base") from _call_her_main_5163

        elif one_of_ten == 3:
            call her_main("The basilisk, also known as the king of serpents.","open","angryCl") from _call_her_main_5164
            her "Herpo the Foul was the first to breed a Basilisk."
            her "He accomplished that by--"
            call her_main("Oh, I'm sorry, professor, we have another test tomorrow...","open","worriedL") from _call_her_main_5165
            her "I Just want to make sure that I'm ready..."
            call her_main("","base","base") from _call_her_main_5166

        elif one_of_ten == 4:
            call her_main("If my body wouldn't require sleep...","open","worriedL") from _call_her_main_5167
            call her_main("I would be able to spend twice as much time with studying!?","angry","wide") from _call_her_main_5168
            call her_main("I wonder if there's a spell for that...","open","base") from _call_her_main_5169
            call her_main("","normal","base") from _call_her_main_5170
        
        elif one_of_ten == 5:
            call her_main("So far professor Trelawney did not taught me a single piece of any actual knowledge, sir.","open","angryCl") from _call_her_main_5171
            call her_main("","normal","base") from _call_her_main_5172
       
        elif one_of_ten == 6:
            call her_main("If only more students were honest, responsible and diligent like me.","open","angryCl") from _call_her_main_5173
            call her_main("","normal","base") from _call_her_main_5174
      
        elif one_of_ten == 7:
            call her_main("How can some people be so ignorant to the world's problems?","open","angryCl") from _call_her_main_5175
            her "Personally, I think that every single one of us should work harder to make our world a better place."
            call her_main("","normal","base") from _call_her_main_5176
            
        elif one_of_ten == 8:
            call her_main("It's been raining quite a lot lately...","open","worriedL") from _call_her_main_5177
            call her_main("","base","base") from _call_her_main_5178
    
        elif one_of_ten == 9:
            call her_main("Very few people know this...","open","worriedL") from _call_her_main_5179
            call her_main("...But I really like chocolate.","base","base") from _call_her_main_5180
            call her_main("","base","base") from _call_her_main_5181
       
        elif one_of_ten == 10:
            call her_main("I am sorry sir, but I don't really have time for idle chat chats...","base","base") from _call_her_main_5182
            call her_main("","normal","base") from _call_her_main_5183


    ### WHORING LEVEL 02 ###
    if whoring >= 3 and whoring <= 5:
        if one_of_ten == 1:
            call her_main("I read somewhere that a full moon often makes it easier to concentrate at a task at hand...","open","angryCl") from _call_her_main_5184
            call her_main("","normal","base") from _call_her_main_5185
            
        elif one_of_ten == 2:
            call her_main("I love nothing more than to curl up by a fireplace during a rainstorm with a good book...","base","base") from _call_her_main_5186
            call her_main("","base","base") from _call_her_main_5187
            
        elif one_of_ten == 3:
            call her_main("A peculiar rumour concerning professor Snape has been circulating in the school lately...","open","worriedL") from _call_her_main_5188
            call her_main("No, I probably shouldn't...","soft","base") from _call_her_main_5189
            call her_main("","normal","base") from _call_her_main_5190
            
        elif one_of_ten == 4:
            call her_main("Despite the questionable nature of the favours you have been buying from me lately, sir...","open","angryCl") from _call_her_main_5191
            her "I am grateful to you for your help..."
            call her_main("Gryffindor needs those points now more than ever...","annoyed","frown") from _call_her_main_5192
            call her_main("","normal","base") from _call_her_main_5193
            
        elif one_of_ten == 5:
            call her_main("Why Quidditch is so popular among the girls is simply beyond me...","open","angryCl") from _call_her_main_5194
            call her_main("","normal","base") from _call_her_main_5195
            
        elif one_of_ten == 6:
            call her_main("The \"Men's Rights Movement\" is steadily gaining popularity.","open","angryCl") from _call_her_main_5196
            her "It's very fulfilling to know that you are helping to improve our society."
            call her_main("","normal","base") from _call_her_main_5197
            
        elif one_of_ten == 7:
            call her_main("The Hogwarts school library is considered to be quite extensive...","open","angryCl") from _call_her_main_5198
            call her_main("Still, I can't help but wish that it'd be bigger...","open","suspicious") from _call_her_main_5199
            call her_main("","normal","base") from _call_her_main_5200
            
        elif one_of_ten == 8:
            call her_main("As one of the top students in this school I have a reputation to keep...","open","worriedL") from _call_her_main_5201
            her "People look up to me..."
            call her_main("...So, your discretion is very appreciated, sir.","open","base") from _call_her_main_5202
            call her_main("","annoyed","worriedL") from _call_her_main_5203
            
        elif one_of_ten == 9:
            call her_main("That favour I sold you the other say, sir...","open","worried") from _call_her_main_5204
            call her_main(".......","normal","worriedCl") from _call_her_main_5205
            call her_main("I only agreed to it because the needs of my house always come first.","open","down") from _call_her_main_5206
            call her_main("I just wanted you to know that, sir...","upset","closed") from _call_her_main_5207
            
        elif one_of_ten == 10:
            call her_main("The \"Autumn Ball\" is still several months away...","open","angryCl") from _call_her_main_5208
            call her_main("But some girls are already discussing what kind of dress they are going to wear...","open","worried") from _call_her_main_5209
            call her_main("","annoyed","annoyed") from _call_her_main_5210


    ### WHORING LEVEL 03 ###
    if whoring >= 6 and whoring <= 8:
        if one_of_ten == 1:
            call her_main("Do you remember when you asked me to show you my panties for the first time sir?","open","angryCl") from _call_her_main_5211
            her "I was so furious with you then..."
            call her_main("Now I see that I was just being selfish...","annoyed","frown") from _call_her_main_5212
            her "After all, the honour of my house is at stake here..."
            call her_main("And that shall be my one and only concern!","normal","frown") from _call_her_main_5213
            
        elif one_of_ten == 2:
            call her_main("The rate at which the Slytherin house has been gaining points lately is simply ridiculous.","open","angryCl") from _call_her_main_5214
            call her_main("I think professor Snape might be behind it.","angry","angry") from _call_her_main_5215
            call her_main("You should look into this, sir.","open","angryCl") from _call_her_main_5216
            call her_main("","normal","base") from _call_her_main_5217
            
        elif one_of_ten == 3:
            call her_main("Ashwinder eggs, rose thorns, moonstone...","open","worriedL") from _call_her_main_5218
            call her_main("Huh? Am I thinking out loud again?","open","worried") from _call_her_main_5219
            call her_main("I apologize...","grin","worriedCl",emote="05") from _call_her_main_5220
            call her_main("It's just that we have another test soon...","soft","baseL") from _call_her_main_5221

        elif one_of_ten == 4:
            call her_main("I dislike the entire house of Slytherin with all my heart, sir.","angry","angry") from _call_her_main_5222
            
        elif one_of_ten == 5:
            call her_main("Hogwarts has really become a second home to me lately...","open","closed") from _call_her_main_5223
            call her_main("I don't even miss my parents nearly as much anymore...","annoyed","down") from _call_her_main_5224
            call her_main("Come to think of it I don't miss them at all...","angry","wide") from _call_her_main_5225
            call her_main("I'm an awful daughter...","angry","down_raised") from _call_her_main_5226

        elif one_of_ten == 6:
            call her_main("*Yawn!* I read about this technique that supposedly allows you to cut your sleep time in half...","annoyed","ahegao") from _call_her_main_5227
            call her_main("It don't think it's working though.... *Yawn!*","annoyed","down") from _call_her_main_5228

        elif one_of_ten == 7:
            call her_main("Even after I graduate from Hogwarts I plan to keep on working hard.","open","angryCl") from _call_her_main_5229
            call her_main("If I give it my all I can make this world a better place, I know it!","open","base") from _call_her_main_5230
            call her_main("","normal","base") from _call_her_main_5231
           
        elif one_of_ten == 8:
            call her_main("Somehow I have the feeling that this year will become a pivotal turning point in my life...","open","worried") from _call_her_main_5232
            call her_main("","soft","baseL") from _call_her_main_5233
  
        elif one_of_ten == 9:
            call her_main("Some of the less traveled school corridors are not very well lit and rather dusty...","open","angryCl") from _call_her_main_5234
            her "Please take care of this, sir..."
            call her_main("","normal","base") from _call_her_main_5235
       
        elif one_of_ten == 10:
            call her_main("I've read about this thing called \"Time-Turner\".","open","base") from _call_her_main_5236
            her "It allows the user to control the flow of time..."
            call her_main("Having a device like that would do wonders for my schedule...","open","closed") from _call_her_main_5237
            call her_main("","annoyed","suspicious") from _call_her_main_5238
        

    ### WHORING LEVEL 04 ###
    if whoring >= 9 and whoring <= 11:
        if one_of_ten == 1:
            call her_main("My \"men's rights movement\" has been losing its popularity lately...","open","worried") from _call_her_main_5239
            call her_main("It's as if people don't even care!","annoyed","angryL") from _call_her_main_5240

        elif one_of_ten == 2:
            call her_main("Thank you for buying all those favours from me, sir.","open","angryCl") from _call_her_main_5241
            call her_main("Some of them were borderline inappropriate, sure...","normal","frown") from _call_her_main_5242
            call her_main("But I don't mind sacrificing my dignity if it will allow Gryffindor to compete with Slytherin on equal ground.","open","angryCl") from _call_her_main_5243
            call her_main("","normal","base") from _call_her_main_5244

        elif one_of_ten == 3:
            call her_main("Quidditch is stupid!","angry","angry") from _call_her_main_5245
            call her_main("There. I said it.","annoyed","suspicious") from _call_her_main_5246
            
        elif one_of_ten == 4:
            call her_main("Sir, there is something about professor Snape that I think you should know...","open","base") from _call_her_main_5247
            call her_main(".................","open","worriedL") from _call_her_main_5248
            call her_main(".........................","annoyed","frown") from _call_her_main_5249
            call her_main("uhm... Never mind...","open","angryCl") from _call_her_main_5250
            call her_main("","normal","base") from _call_her_main_5251
 
        elif one_of_ten == 5:
            call her_main("Some of the Slytherin girls sell sexual favours almost openly these days...","open","angryCl") from _call_her_main_5252
            call her_main("You need to put an end to such practices, sir.","open","base") from _call_her_main_5253
            call her_main("(I can barely keep up...)","annoyed","angryL") from _call_her_main_5254

        elif one_of_ten == 6:
            call her_main("Life works in mysterious ways...","open","worriedL") from _call_her_main_5255
            call her_main("Wouldn't you agree, sir?","open","suspicious") from _call_her_main_5256
            call her_main("","soft","baseL") from _call_her_main_5257

        elif one_of_ten == 7:
            call her_main("Slytherins...","angry","angry",emote="01") from _call_her_main_5258
            call her_main("","angry","angry") from _call_her_main_5259
            
        elif one_of_ten == 8:
            call her_main("I've been spending so much time in your office lately, sir...","open","worriedL") from _call_her_main_5260
            call her_main("If I'm not careful some people may think that I have become your pet...","open","worried") from _call_her_main_5261
            call her_main("I meant to say the teacher's pet...","angry","worriedCl",emote="05") from _call_her_main_5262
            call her_main("","normal","worriedCl") from _call_her_main_5263

        elif one_of_ten == 9:
            call her_main("My favourite colours?","open","base") from _call_her_main_5264
            call her_main("scarlet and gold of course!","open","base") from _call_her_main_5265
            call her_main("","normal","base") from _call_her_main_5266
       
        elif one_of_ten == 10:
            call her_main("Is it weird that my best friends are boys?","open","worriedL") from _call_her_main_5267
            call her_main("","base","base") from _call_her_main_5268
        

    ### WHORING LEVEL 05 ###
    if whoring >= 12 and whoring <= 14:
        if one_of_ten == 1:
            call her_main("Sir, with all due respect...","normal","frown") from _call_her_main_5269
            her "Professor Snape's debauchery is getting out of hand!"
            call her_main("You must do something, sir.","open","worried") from _call_her_main_5270
            call her_main("","normal","base") from _call_her_main_5271

        elif one_of_ten == 2:
            call her_main("I am willing to go to great lengths to insure the superiority of my house...","open","angryCl") from _call_her_main_5272
            her "But that does not mean that I take pleasure in selling myself out to you in exchange for house points, sir."
            call her_main("{size=-4}(Like some sort of prostitute-witch...){/size}","angry","down_raised") from _call_her_main_5273

        elif one_of_ten == 3:
            call her_main("What will it be today, sir?","annoyed","annoyed") from _call_her_main_5274
            
        elif one_of_ten == 4:
            call her_main("lately I have not been studying nearly as much as I used to...","open","worried") from _call_her_main_5275
            call her_main("Am I losing my motivation?","open","worriedL") from _call_her_main_5276
            call her_main("","soft","baseL") from _call_her_main_5277
            
        elif one_of_ten == 5:
            call her_main("My least favourite subject?","open","suspicious") from _call_her_main_5278
            call her_main("Divination.","annoyed","frown") from _call_her_main_5279 
            
        elif one_of_ten == 6:
            call her_main("My father used to say: \"Magic is just science we don't understand yet\".","open","base") from _call_her_main_5280
            call her_main("He could't be more wrong of course...","open","worriedL") from _call_her_main_5281
            call her_main("","soft","baseL") from _call_her_main_5282
            
        elif one_of_ten == 7:
            call her_main("Despite everything...","open","angryCl") from _call_her_main_5283
            call her_main("I am thankful that you keep on buying favours from me, sir...","open","worriedL") from _call_her_main_5284
            call her_main("","soft","baseL") from _call_her_main_5285
            
        elif one_of_ten == 8:
            call her_main("It's quite cold outside today, isn't it?","open","base") from _call_her_main_5286
            call her_main("","soft","base") from _call_her_main_5287
            
        elif one_of_ten == 9:
            call her_main("The \"Autumn Ball\" will be soon...","open","base") from _call_her_main_5288
            call her_main("","soft","base") from _call_her_main_5289
            
        elif one_of_ten == 10:
            call her_main("People hardly show up for my \"men's rights movement\" meetings at all anymore...","open","worriedL") from _call_her_main_5290
            call her_main("","soft","baseL") from _call_her_main_5291
    
    
    ### WHORING LEVEL 06 ###
    if whoring >= 15 and whoring <= 17:
        if one_of_ten == 1:
            call her_main("Would you like me to show you my breasts today, sir?","open","down") from _call_her_main_5292
            call her_main("Yes... I would willingly expose myself to you, professor...","base","ahegao_raised") from _call_her_main_5293
            call her_main("That's how selfless I am!","annoyed","annoyed") from _call_her_main_5294
           
        elif one_of_ten == 2:
            call her_main("I can't help but feel bad for the house elves who do my laundry...","open","base") from _call_her_main_5295
            call her_main("I mean, all those dreadful semen stains...","open","down") from _call_her_main_5296
            call her_main("","angry","down_raised") from _call_her_main_5297

        elif one_of_ten == 3:
            call her_main("it Doesn't matter how many times you ask me this, sir...","open","base") from _call_her_main_5298
            her "The answer shall remain the same..."
            call her_main("I have nothing but resentment for the \"Slytherins\"!","angry","angry") from _call_her_main_5299
            call her_main("","annoyed","angryL") from _call_her_main_5300
        
        elif one_of_ten == 4:
            call her_main("When I think about all the favours I sold you over these last months, sir...","open","base") from _call_her_main_5301
            call her_main("Although I do feel a little bit embarrassed...","open","down") from _call_her_main_5302
            call her_main("I also feel very proud of myself.","upset","closed") from _call_her_main_5303
            
        elif one_of_ten == 5:
            call her_main("I still dedicate a lot of my time to studying...","open","base") from _call_her_main_5304
            her "But not nearly as much of it as I used to..."
            call her_main("Somehow I just don't enjoy studying at all anymore...","open","worried") from _call_her_main_5305
            call her_main("","soft","baseL") from _call_her_main_5306
        
        elif one_of_ten == 6:
            call her_main("Gryffindor shall get the house cup this year!","open","angryCl") from _call_her_main_5307
            call her_main("{size=-4}(Even if it should cost me my dignity...){/size}","angry","down_raised") from _call_her_main_5308
            call her_main("","upset","closed") from _call_her_main_5309
           
        elif one_of_ten == 7:
            call her_main("I don't mind the autumn weather...","open","base") from _call_her_main_5310
            call her_main("But my favourite season is winter.","open","closed") from _call_her_main_5311
            call her_main("","soft","base") from _call_her_main_5312
        
        elif one_of_ten == 8:
            call her_main("I used to look down on girls who spend too much time with worrying about the way they look...","open","base") from _call_her_main_5313
            her "But I was wrong to do so..."
            her "I am starting to understand how important it really is for a girl to look pretty."
            call her_main("...............","annoyed","worriedL") from _call_her_main_5314
            call her_main("I've been on a diet lately...","angry","wink") from _call_her_main_5315
            call her_main("","angry","worriedCl",emote="05") from _call_her_main_5316
            call her_main("","normal","worriedCl") from _call_her_main_5317
       
        elif one_of_ten == 9:
            call her_main("Lately I've been feeling rather confident around the boys...","open","base") from _call_her_main_5318
            call her_main("I think I have you to thank for that, sir.","base","base") from _call_her_main_5319
            
        elif one_of_ten == 10:
            call her_main("My favourite subject?","open","base") from _call_her_main_5320
            call her_main("Hm...","soft","baseL") from _call_her_main_5321
            call her_main("I suppose that would be \"charms\"...","open","base") from _call_her_main_5322
            call her_main("","soft","base") from _call_her_main_5323
  
  
    ### WHORING LEVEL 07 ###
    if whoring >= 18 and whoring <= 20:
        if one_of_ten == 1:
            call her_main("Just let me know what will be required of me today, sir.","open","angryCl") from _call_her_main_5324
            call her_main("","normal","base") from _call_her_main_5325
           
        elif one_of_ten == 2:
            call her_main("I barely study at all anymore...","open","worried") from _call_her_main_5326
            her "Despite that my popularity among the other students seems to be growing..."
            call her_main("Hm...","soft","baseL") from _call_her_main_5327
                 
        elif one_of_ten == 3:
            call her_main("I wouldn't say \"no\" to a bottle of butterbeer right about now...","smile","glance") from _call_her_main_5328
            call her_main("","grin","baseL") from _call_her_main_5329
        
        elif one_of_ten == 4:
            call her_main("What is it sir? Do you have another present for me?","base","base") from _call_her_main_5330
            call her_main("Oh... I see...","annoyed","angryL") from _call_her_main_5331

        elif one_of_ten == 5:
            call her_main("I am doing well, thank you for asking.","base","base") from _call_her_main_5332

        elif one_of_ten == 6:
            call her_main("Do I look fat to you sir?","open","worried") from _call_her_main_5333
            call her_main("I wonder if the diet is working...","annoyed","worriedL") from _call_her_main_5334
           
        elif one_of_ten == 7:
            call her_main("I remember that I used to say that books were my friends...","open","closed") from _call_her_main_5335
            call her_main("Now that sounds so lame.","grin","worriedCl",emote="05") from _call_her_main_5336
            call her_main("","soft","base") from _call_her_main_5337
        
        elif one_of_ten == 8:
            call her_main("Add ashwinder egg to cauldron...","open","angryCl") from _call_her_main_5338
            her "Then add horseshoe reddish and heat..."
            her "Then juice a squill bulb..."
            call her_main("Or was it a dash of thyme first?","open","worriedL") from _call_her_main_5339
            call her_main("..............","soft","baseL") from _call_her_main_5340
            call her_main("Oh, who cares?","grin","worriedCl",emote="05") from _call_her_main_5341
            call her_main("","base","base") from _call_her_main_5342
       
        elif one_of_ten == 9:
            call her_main("Do You think I am wearing enough makeup, sir?","open","base") from _call_her_main_5343 
            her "Wearing too much would look vulgar..."
            call her_main("But wearing too little would make me look plain...","soft","baseL") from _call_her_main_5344
            call her_main("I don't want to look plain!","annoyed","angryL") from _call_her_main_5345
            
        elif one_of_ten == 10:
            call her_main("Would you like to see my tits today, sir?","smile","glance") from _call_her_main_5346 
            call her_main("25 house points, please.","smile","angry") from _call_her_main_5347
            call her_main("","upset","closed") from _call_her_main_5348
    
   
    ### WHORING LEVEL 08+ ###
    if whoring >= 21:
        if one_of_ten == 1:
            call her_main("Do You have any adult magazines you don't need, sir?","open","baseL",cheeks="blush") from _call_her_main_5349
            call her_main("","base","baseL",cheeks="blush") from _call_her_main_5350

        elif one_of_ten == 2:
            call her_main("I am sorry to bother you with this, sir...","open","base") from _call_her_main_5351
            her "But do you have any condoms?"
            call her_main("This is not for me of course... I'm asking for a friend...","angry","worriedCl",emote="05") from _call_her_main_5352
                 
        elif one_of_ten == 3:
            call her_main("It's been getting so cold lately...","open","base") from _call_her_main_5353
            call her_main("I hope it's going to start snowing soon...","base","base") from _call_her_main_5354
        
        elif one_of_ten == 4:
            call her_main("Jump and scream for the Gryffindor team!","open","closed") from _call_her_main_5355
            call her_main("So daring and bold, sporting red and gold!","smile","happyCl",emote="06") from _call_her_main_5356
            call her_main("","base","base") from _call_her_main_5357

        elif one_of_ten == 5:
            call her_main("I hope the ball goes smoothly...","open","worriedL") from _call_her_main_5358
            call her_main("","soft","baseL") from _call_her_main_5359

        elif one_of_ten == 6:
            call her_main("I wonder what Ginny is going to wear for the ball...","base","base") from _call_her_main_5360
        
        elif one_of_ten == 7:
            call her_main("Considering the nature of the favours you keep buying from me sir...","open","closed") from _call_her_main_5361
            call her_main("I seldom bother to put on underwear at all anymore...","open","worried") from _call_her_main_5362
        
        elif one_of_ten == 8:
            call her_main("Sir, could you put your penis in my mouth?","angry","base") from _call_her_main_5363
            call her_main("Sir, I am begging you...","open_wide_tongue","ahegao") from _call_her_main_5364
            call her_main("Fifty five points, please!","smile","angry") from _call_her_main_5365
            call her_main("","angry","wink") from _call_her_main_5366

        elif one_of_ten == 9:
            call her_main("A read this one article about the positive effects of semen on a woman's skin...","open","closed") from _call_her_main_5367
            call her_main("I wonder where their information is coming from...","base","glance") from _call_her_main_5368
            call her_main("Did the magazine conduct research of some sort?","angry","wink") from _call_her_main_5369
            call her_main("","base","glance") from _call_her_main_5370

        elif one_of_ten == 10:
            call her_main("It goes like this...","open","closed") from _call_her_main_5371
            her "First Gryffindor, then Ravenclaw, then Hufflepuff..."
            call her_main("And Slytherin is not even on the list!","open","annoyed",cheeks="blush") from _call_her_main_5372
            call her_main("","upset","closed") from _call_her_main_5373


    return


    