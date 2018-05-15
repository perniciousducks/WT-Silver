

label sna_main(text="",face="",xpos=snape_xpos,ypos=snape_ypos):
    hide screen snape_main
    hide screen snape_head
    show screen bld1

    if xpos != snape_xpos:
        if xpos == "base" or xpos == "default":
            $ snape_xpos = 525
        else:
            $ snape_xpos = xpos
    if ypos != snape_ypos:
        if ypos == "base" or ypos == "default":
            $ snape_ypos = 0
        else:
            $ snape_ypos = ypos

    if face != "":
        $ s_sprite = "characters/snape/main/"+str(face)+".png"

    show screen snape_main
    with d3

    if text != "":
        if "[hermione_name]" in text or "[genie_name]" in text:
            if "[genie_name]" in text:
                $ text = text.replace("[genie_name]",genie_name)
            if "[hermione_name]" in text:
                $ text = text.replace("[hermione_name]",hermione_name)
        sna "[text]"

    return
   
    
label sna_head(text="",face="",xpos=snape_head_xpos ,ypos=snape_head_ypos):
    hide screen snape_main
    hide screen snape_head
    show screen bld1
    
    if xpos != snape_head_xpos:
        if xpos == "base" or xpos == "default":
            $ snape_head_xpos = 540
        else:
            $ snape_head_xpos = xpos

    if ypos != snape_head_ypos:
        if ypos == "base" or ypos == "default":
            $ snape_head_ypos = 380
        else:
            $ snape_head_ypos = ypos

    if face != "":
        $ s_sprite = "characters/snape/main/"+str(face)+".png"

    show screen snape_head
    with d3

    if text != "":
        sna "[text]"
    hide screen snape_head
    with d3

    return
    

### SNAPE FULL
screen snape_main: #Snape. Full size.
    tag big_snape
    add s_sprite xpos snape_xpos ypos snape_ypos #tt_xpos+140 ypos tt_ypos
    #zorder hermione_main_zorder #(5) Otherwise candle light is shown on top.
    zorder snape_zorder #5
    
### SNAPE HEAD
screen snape_head: #Snape. Full size.
    tag big_snape
    add s_sprite xpos snape_head_xpos ypos snape_head_ypos
    zorder 8 #8 #In front of text box.


### SNAPE EMOTIONS
screen s_emo_01: #Closed eyes and closed mouth.
    tag semo
    add "characters/snape/main/s_emo_01.png" xpos tt_xpos ypos tt_ypos
    zorder 4 #2 #Otherwise candle light is shown on top.
