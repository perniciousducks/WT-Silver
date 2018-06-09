





label susan_imperio:
    call ast_main("Alright, [ast_genie_name].","smile","base","base","mid")
    call ast_main("I will bring the [ast_susan_name]!","grin","angry","angry","mid")
    call blkfade
    
    call nar(">Astoria leaves to summon Susan.")
    pause.5
    call play_sound("door")
    hide screen blkfade
    call sus_main("Hello, Professor.","open","base","worried","mid",xpos="mid",ypos="base",trans="fade")
    call sus_main("You wanted to see me?","upset","base","worried","down")
    
    m "Yes, Miss Bones, if you could just stand there in the middle while--"
    call ast_main("Wait a second, [ast_genie_name],...","scream","closed","base","mid",trans="hpunch")
    call ast_main("50 points, remember!","grin","angry","angry","mid")
    m "..."
    m "Right..."
    m "Alright... 50 points to \"Slytherin\"!"
    $ slytherin +=50
    call ast_main("Thank you!","grin","happyCl","base","mid")
    pause.5
    call blkfade
                    
    call ast_main("","grin","angry","angry","L",xpos="base",ypos="base") #uses the fade from the next line.
    hide screen blkfade
    call sus_main("What are you--","open","wide","worried","R",xpos="mid",ypos="base",trans="fade")
                    
    call cast_spell("imperio")
    call ast_main("{size=+10}{b}IMPERIO{/b}{/size}","scream","angry","angry","angry")
                    
    show screen blktone
    call ast_main("[ast_susan_name], I command you to do whatever the old man tells you to do!")
    call sus_main("Of course, I will do whatever the old man sa--","open","base","base","up")
                    
    hide screen blktone
    call ast_main("All done, [ast_genie_name]! This will probably last a couple of days...","smile","base","base","R")
    call ast_main("You may leave now, [ast_susan_name]!","grin","happyCl","base","mid")
    call sus_main("Ok","base","base","base","up")
    hide screen susan_main
    with d3
                    
    $ susan_imperio_counter += 20 #Lasts 20 days.
    $ susan_imperio_influence = True
    $ spells_locked = True
                    
    call nar(">Susan is now under the influence of imperio.\n>The effect will last for 20 days.")
    jump astoria_requests