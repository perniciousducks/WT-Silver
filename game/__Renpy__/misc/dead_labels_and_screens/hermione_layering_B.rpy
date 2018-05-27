
    
init python:
    
    
    def changeHermione( hair_color=None,
                        hair_style=None,
                        face=None,
                        
                        x_pos=None,
                        y_pos=None):
        ###DEFINE GLOBAL VARIABLES
        global h_xpos
        global h_ypos
        global h_base
        global h_body
        global h_hair_color
        global h_hair_style
        ###HIDE OLD SCREEN
        renpy.hide_screen("hermione_main_new")
        renpy.with_statement(Dissolve(0.5))
        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            h_xpos = x_pos
        else:
            h_xpos = luna_xpos
        if y_pos is not None:
            h_ypos = y_pos
        else:
            h_ypos = h_ypos
        
        
        if hair_color is not None and (hair_color >= 1 and hair_color <= 6):
            h_hair_color = hair_color
        else:
            h_hair_color = h_hair_color
            
        if hair_style is not None and (hair_style == "A" or hair_style == "B"):
            h_hair_style = hair_style
        else:
            h_hair_style = h_hair_style
        
        hermione_hair_a = "characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+".png"
        hermione_hair_b = "characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+"_2.png"
        
        if face is not None:
            h_body = h_body
    
    def changeHermioneDialoug(   image_name,
                                    hid_char_list=None,
                                    hid_dialog_list=None,
                                    x_pos=370,
                                    y_pos=0,
                                    hide_trans=Dissolve(0.3),
                                    show_trans=Dissolve(0.3),
                                    char_list=None,
                                    dialog_list=None):
        # SCOPE THESE VARIABLES TO GLOBAL SO WE CAN REALLY
        # UPDATE THEM
        global h_xpos
        global h_ypos
        global h_body
        renpy.hide_screen("hermione_main")
        if hide_trans is not None:
            renpy.with_statement(hide_trans)
        #dialog if present
        if hid_char_list is not None:
            if len(hid_char_list) == 1:
                #single character
                for i in range(0,len(hid_dialog_list)):
                    renpy.say(hid_char_list[0],hid_dialog_list[i])
            elif len(hid_char_list) > 1:
                #multiple characters
                for i in range(0,len(hid_char_list)):
                    renpy.say(hid_char_list[i],hid_dialog_list[i])
        h_xpos = x_pos
        h_ypos = y_pos
        if image_name is not None:
            h_body = image_name

        renpy.show_screen("hermione_main")
        if show_trans is not None:
            renpy.with_statement(show_trans)
        #dialog if present
        if char_list is not None:
            if len(char_list) == 1:
                #single character
                for i in range(0,len(dialog_list)):
                    renpy.say(char_list[0],dialog_list[i])
            elif len(char_list) > 1:
                #multiple characters
                for i in range(0,len(char_list)):
                    renpy.say(char_list[i],dialog_list[i])
                   
