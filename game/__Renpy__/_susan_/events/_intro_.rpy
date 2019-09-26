

### Susan Intro ###

label nt_he_susan_E1:
    call ton_main(".................","base","base","worried","down", ypos="head")
    m "Something on your mind?"
    call ton_main("Yes, there's this student in my class. She seems to be having a bad time.","open","base","sad","mid")
    m "Education isn't meant to be enjoyable."
    call ton_main("It's not that, she's being bullied by the other students apparently...","open","base","sad","R")
    m "For what reason?"
    call ton_main("For being shy,...insecure,...","upset","closed","base","mid")
    m "About what?"
    call ton_main("About her massive tits!","upset","base","base","mid")
    g4 "!!!"
    m "Why would she be insecure about that?"
    g9 "Surely that's something most girls would kill for!"
    call ton_main("That's what I said...","open","closed","base","mid")
    call ton_main("She didn't seem to think I was being genuine.","upset","base","worried","down")
    m "They're probably just jealous of her."
    call ton_main("Naturally... Even I'm jealous of those {b}milk-bags{/b} of hers!","open","base","angry","mid")
    g9 "I definitely need to see them!"
    call ton_main("That being said, I'm quite worried about her...","open","closed","worried","mid")
    call ton_main("Lately she's been too shy to even answer the simplest of questions during my class.","open","base","sad","R")
    call ton_main("She's lost quite a few points for her house that way.","upset","base","sad","mid")
    call ton_main("Not in my lessons, of course. I'd never take points from \"Hufflepuff!\"","upset","base","worried","down")
    g9 "Just send her my way and I'll drown her in house points!"
    m "And show her that her bod-..."
    g4 "*Ahem!* Show her that she's appreciated..."
    call ton_main("That's what I was thinking...","open","base","base","mid")
    g4 "Wait, you were?"
    call ton_main("Of course, why else would I be telling you about her?","open","closed","angry","mid")
    m "I don't know... banter?"
    m "Snape sure as hell hasn't sent me any girls up here..."
    call ton_main("I can teach him a thing or two about sharing - if you'd like...","horny","base","base","mid")
    call ton_main("The more the merrier in my opinion...","smile","happyCl","base","mid")
    m "You don't mean Snape and I..."
    call ton_main("Of course not, don't be silly!","base","happyCl","base","mid")
    call ton_main("Maybe he's afraid you'd steal them from him if you got the chance...","horny","base","angry","mid")
    m "I have my doubts those girls he's talking about even exist..."
    m "But don't tell him I said that."
    call ton_main("I shall talk to Miss Bones.","open","closed","base","mid")

    if letter_min_favors.read:
        m "Bones... I think I've heard that name before..."
        call ton_main("Her Aunt works at the ministry.","open","base","base","mid")
        m "..."
    else:
        g9 "*He-He*... Bones."

    call ton_main("I'm sure you'll find her less than bony...","base","base","angry","mid")
    m "..."
    call ton_main("But, you have to promise me that you won't go overboard with her!","angry","base","base","mid")
    call ton_main("I'd rather not risk having her contact that aunt of hers...","open","base","base","R")
    m "I can be slick and subtle when I want to..."
    call ton_main("...","upset","base","worried","R")
    call ton_main("You're making me regret this decision already...","open","closed","worried","mid")

    ">As the hours pass, you convince Tonks to describe Susan's {b}massive tits{/b} to you..."
    ">You are glued to every word she has to say about them..."

    $ nt_he.susan_E1 = True

    jump end_tonks_hangout_points
