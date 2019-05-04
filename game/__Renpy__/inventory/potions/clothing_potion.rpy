

### TRANSPARENCY POTION ###

label potion_scene_4: #Transparent uniform
    m "[hermione_name], I have another potion for you."
    call her_main("I'm not sure that I like these potions [genie_name].","normal","frown")
    call her_main("Especially after the time you tried to turn me into a cat.","annoyed","frown")
    m "To be fair I was trying to turn you into another girl..."
    call her_main("That's not much better [genie_name].","angry","angry")
    m "Isn't it?"
    call her_main("Well at least promise me that this one isn't going to embarrass me in the middle of class.","open","angryCl")
    call her_main("My reputation is suffering enough as it is. I don't need these constant potions causing me to transform in front of my peers.","annoyed","angryL")
    m "I promise that this potion won't affect your body in any way."
    call her_main("Well then what on earth is it going to do?","angry","angry")
    m "As always [hermione_name], you'll ha-"
    call her_main("Have to wait and see. I know.","normal","frown")

    call her_chibi("drink_potion","mid","base")

    call nar(">Hermione quickly drinks the potion.") #new
    call her_main("","open","angryCl")

    call her_chibi("stand","mid","base")

    her "Can I go now?"
    m "Yes you may. 20 points to Gryffindor"

    $ gryffindor += 20

    call her_main("Thank you [genie_name].","open","closed")

    call her_walk(action="leave", speed=2)

    $ hermione_busy = True

    if her_whoring <= 7:
        call set_her_transparency(top=0.8, bottom=0.9)
    elif her_whoring <= 13:
        call set_her_transparency(top=0.5, bottom=0.6)
    elif her_whoring <= 20:
        call set_her_transparency(top=0.3, bottom=0.4, bra=0.6, onepiece=0.6, panties=0.6)
    else:
        call set_her_transparency(top=0.2, bottom=0.2, bra=0.4, onepiece=0.4, panties=0.4)

    $ transparent_quest = True

    jump main_room


label potion_scene_4_2: #Scene where Hermione comes back after classes angry and confused at having her uniform made transparent
    $ transparent_quest = False
    call play_sound("door") #Sound of a door opening.
    call her_chibi("stand","mid","base")

    show screen bld1
    if her_whoring <= 7: #Very angry and embarrassed
        call nar(">Hermione bursts into your office.")
        call her_main("How could you [genie_name]!","angry","base",tears="soft")
        call her_main("I am the laughing stock of the entire school!","angry","base",tears="soft")
        call her_main("Now everyone knows what I look like naked!","mad","worriedCl",tears="soft_blink")
        m "Tell me about what happened."
        call her_main("Tell you about what happened? I'm never speaking to you again.","angry","base",tears="soft")
        $ her_mood += 20

    elif her_whoring <= 13: #Mildly aggravated
        call nar(">Hermione comes into your office quickly without knocking.")
        call her_main("Again?","angry","worriedCl",emote="05")
        m "What's this about [hermione_name]?"
        call her_main("Why would you make my clothes invisible again?","open","base")
        m "Why not?"
        call her_main("Ugh, you're such a pig.","annoyed","worriedL")
        m "Tell me about what happened."
        call her_main("...","normal","worriedCl")
        call her_main("Fine, but I expect an extra 10 points.","open","base")
        m "As you wish."
        call her_main("Well I started off with potions class as usual when I started to feel like all eyes were on me.","disgust","glance")
        m "I wonder why."
        call her_main("As I was saying I was completing potions class and felt like everyone wouldn't take their eyes off of me.","annoyed","angryL")
        call her_main("I didn't think anything of it until I was approached by Professor Snape at the end of the lesson.","annoyed","annoyed")
        call her_main("He normally criticises me during potions class. Stuff like getting dosages wrong, things that I know are correct.","annoyed","worriedL")
        m "Back to the story [hermione_name]."
        call her_main("Well when he commented that he liked my outfit I was suspicious. I thought that perhaps he was talking about my shirt until I looked down and saw that everything was see through.","disgust","glance")
        call her_main("But I just ignored him, finished class and ran here.","annoyed","angryL")
        m "You just finished class?"
        call her_main("Of course, I can't afford to miss potions class. I'm doing poorly enough without missing class.","annoyed","annoyed")
        m "Well fair enough. You may go now."
        call her_main("Hmmph. Goodbye [genie_name].","annoyed","worriedL")

    elif her_whoring <= 20: #Slightly aroused
        call nar(">Hermione enters your office")
        call her_main("Can you at least warn me next time?","open","suspicious")
        m "Well, that'd take away from the suspense wouldn't it?"
        call her_main("Hmmmm, well at least ask what I'm doing before you give me the potion.","open","worriedL")
        m "Why, what did you have to do today that was so important?"
        call her_main("I had to give a speech for languages!","angry","worried")
        call her_main("Do you have any idea how inappropriate it was giving a speech on morality in front of the entire class-","open","closed")
        call her_main("{size=+5}As my clothes became transparent!{/size}","angry","worried")
        m "Well I imagine it depends on what side of morality you were arguing."
        call her_main("It doesn't matter.","open","closed")
        m "Are you sure that you didn't enjoy it?"
        call her_main("How could I. I had to stand there as my friends and peers all saw me naked.","annoyed","suspicious")
        m "You finished your speech?"
        call her_main("Certainly, I had to make sure that everyone knew my views on morality.","soft","base")
        m "Well I'm sure they have a crystal clear view of it now."
        call her_main("Hmmph, are you done?","annoyed","angryL")
        m "Yes, you may go now."
        call her_main("Good bye [genie_name].","open","base")

    else: #Highly aroused (doesn't even acknowledge that her clothes are see-through)
        call nar(">Hermione enters the office casually.")
        m "Hello [hermione_name], how was your day today?"
        call her_main("Fine [genie_name]. Why do you ask?","base","base")
        m "No reason. Anything unusual happen today?"
        call her_main("Hmmmm, now that you mention it I suppose that boys in class were a little more forward than usual.","open","worriedL")
        m "How so?"
        call her_main("Well nothing serious, just small stuff like calling me names, groping me.","soft","baseL")
        m "Groping you? What on earth could have provoked them to do that?"
        call her_main("I don't know [genie_name]. I can't imagine any reason that I would be attracting attention today...","base","base")
        m "You're getting off on this aren't you?"
        call her_main("...","smile","baseL")
        call her_main("I've never been so turned on in my life. Having all eyes on me. Having every boy imagine doing unspeakable things to me.","soft","ahegao")
        call her_main("Snape made me stand out the front of class after I talked back to him.","base","down")
        call her_main("I think that I orgasmed just from the looks people gave me.","grin","dead")
        m "Well done [hermione_name]. You're becoming quite the slut."
        call her_main("Thank you [genie_name]. Is that all?","base","glance")
        m "Yes, you can go now slut."
        call her_main("{image=textheart}","smile","baseL")

    call reset_her_transparency
    $ transparent_quest = False

    call her_walk(action="leave", speed=2)

    $ hermione_busy = True

    jump main_room
