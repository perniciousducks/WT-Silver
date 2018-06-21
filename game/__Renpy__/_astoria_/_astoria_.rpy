
    


    
    
    

    
    
   
label astoria_intro_branches: #This label runs every day and night. Never call to it!

    if not ministry_letter_received:
    
        if not ministry_letter:
            $ ministry_letter = True
            $ letters += 1 #Displays Owl
        
        if daytime:
            jump day_resume
        else:
            jump night_resume
    
    #Talk to Hermione now.
    
    #Talk to Snape now.
    #Talk to Snape again if you talked to Snape first.
    
    #Hermione finds Astoria. #Start of day.
    if daytime and hermione_finds_astoria and days_without_an_event >= 2 and not astoria_unlocked:
        $ astoria_unlocked = True
        $ days_without_an_event = 0
        jump astoria_captured_intro
      
    #Tonks intro.
    if astoria_unlocked and not tonks_intro_happened:
        $ tonks_intro_happened = True
        jump tonks_intro_event
    
    #Snape prevents the ministry from detecting curses.
    if tonks_intro_happened and not spells_unlocked:
        if daytime:
            pass
        else:
            $ spells_unlocked = True #Astoria can now use spells.
            jump snape_spell_intro
        
    #Talk to Astoria now. #Triggers Susan intro.
    
    #Talk to Snape now. #Snape gives you the book. Can be done later.
    
    #Tonks becomes a teacher.
    if third_curse_got_cast and not tonks_unlocked:
        $ tonks_unlocked = True
        $ astoria_intro_completed = True
        jump astoria_tonks_intro
        
    if daytime:
        jump day_resume
    else:
        jump night_resume
 
    
label hermione_talk_branches:
    #You tell Hermione about the curses.
    if ministry_letter_received and not astoria_unlocked:
        if snape_on_the_lookout:
            $ hermione_finds_astoria = True
        if hermione_on_the_lookout:
            $ chitchated_with_her = True 
            call her_main("I'm still looking for that student, [genie_name]!","open","closed") 
            call her_main("Trust in me, I will find that slytherin scum!","angry","angry") 
            jump hermione_talk
        $ hermione_takes_classes = True
        $ hermione_on_the_lookout = True
        jump letter_intro_hermione
    
    else:
        jump hermione_talk_branches_return
      
label snape_talk:
    #You tell Snape about the curses.
    if ministry_letter_received and not astoria_unlocked:
    
        if hermione_on_the_lookout:
            $ hermione_finds_astoria = True
        if snape_on_the_lookout:
            $ chitchated_with_snape = True 
            call sna_main("I'm still on the lookout, Genie.","snape_01") 
            call sna_main("If I find the little maggot that casts those spells,...","snape_10") 
            call sna_main("I will crush his bones!","snape_16") 
            jump snape_ready
        $ snape_busy = True
        $ snape_on_the_lookout = True
        jump letter_intro_snape
        
    elif third_curse_got_cast and spells_unlocked and not snape_gave_spellbook:
        $ snape_gave_spellbook = True
        $ chitchated_with_snape = True
        jump snape_book_intro
        
    else:
        call snape_chitchat 
        jump snape_ready
       
        
    
label set_ast_susan_name:
    $ ast_susan_name = renpy.random.choice(["Susy","Cow","Cow Tits","Milk Bag","Slut","Whore","Piggy","Pig","Bessie","Moo Moo"])
    return
    
label set_ast_tonks_name:
    $ ast_tonks_name = renpy.random.choice(["Hag","Old Hag","Punk","Dyke","Lesbo"])
    return