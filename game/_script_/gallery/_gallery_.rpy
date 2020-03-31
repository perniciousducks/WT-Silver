label open_gallery():
    $ hide_transitions = True
        
    # Door dictionary
    $ character_info = {
        "All": {"ico": "head_hermione_2_locked", "flag": True, "active": False, "activity": ""},
        "Tonks": {"ico": "head_tonks_1", "flag": tonks_wardrobe_unlocked, "active": False, "activity": ""},
        "Hermione": {"ico": "head_hermione_2", "flag": hermione_wardrobe_unlocked, "active": False, "activity": ""},
        "Cho": {"ico": "head_cho_2", "flag": cho_wardrobe_unlocked, "active": False, "activity": ""},
        "Luna": {"ico": "head_luna_2", "flag": luna_wardrobe_unlocked, "active": False, "activity": ""},
        "Astoria": {"ico": "head_astoria_2", "flag": astoria_wardrobe_unlocked, "active": False, "activity": ""},
        "Susan": {"ico": "head_susan_2", "flag": susan_wardrobe_unlocked, "active": False, "activity": ""}
    }
    $ sorting_modes = ["newest", "Best this month", "Best ever", "Least voted"]
    $ select_sorting = 0
    $ outfits_displayed = 3
    $ loadet_gallery = []
    $ cached_outfits = {}
    $ sorting_list = []
    $ gallery_page = 0
    $ month_in_sec = 2419200 #60*60*24*7*4 
    label gallery_reapet():
    
    show screen gallery_outfits(character_info, loadet_gallery)

    $ _return = ui.interact()

    hide screen gallery_outfits

    if _return[0] == "summon":
        python:
            sorting_list = []
            gallery_page = 0
            select_sorting = 0
            url = "http://172.104.129.60:8080/outfit/"
            header_info = ""
            
            if not cached_outfits.get(_return[1], None) == None:
                loadet_gallery = cached_outfits[_return[1]]
                sorting_list.extend(loadet_gallery)
            
            else:
                if _return[1] == "All":
                    for key, value in character_info.iteritems():
                        if not key == "All" and value["flag"]:
                            header_info += key.lower()+","
                else:
                    #The character string is what the server is looking for in the header
                    header_info = _return[1].lower()
                
                web_resualt = get_request(url, ('character', header_info))
                if not web_resualt[0] == 200:
                    print("Some error handling")
                loadet_gallery = evaluate(web_resualt[1])
                sorting_list.extend(loadet_gallery)

                #cached outfits so it dont ping the server every time the button is hit.
                #Dont change this or the server will have to get a time out per ip.
                cached_outfits[_return[1]] = loadet_gallery

            for i in xrange(outfits_displayed):
                if i >= len(loadet_gallery):
                    pass
                else:
                    create_folder_if_not_exist(config.basedir+"/game/outfits/"+loadet_gallery[i][4].lower()+"/")
                    outfit_cached(loadet_gallery[i])
                        
    elif _return[0] == "upvote":
        $ url = "http://172.104.129.60:8080/outfit/upvote/"+str(_return[1][0]) # Set destination URL here
        if not persistent.gallery_votes.get(_return[1][0], "netrual") == "upvote":
            if persistent.gallery_votes.get(_return[1][0], "netrual") == "downvote":
                $ delete_request("http://172.104.129.60:8080/outfit/downvote/"+str(_return[1][0]))
                $ _return[1][2] = int(_return[1][2]) - 1
                
            $ put_request(url)
            $ persistent.gallery_votes[_return[1][0]] = "upvote"
            $ _return[1][3] = int(_return[1][3]) + 1
        else:
            $ delete_request(url)
            $ persistent.gallery_votes[_return[1][0]] = "netrual"
            $ _return[1][3] = int(_return[1][3]) - 1
            
    elif _return[0] == "downvote":
        $ url="http://172.104.129.60:8080/outfit/downvote/"+str(_return[1][0])
        if not persistent.gallery_votes.get(_return[1][0], "netrual") == "downvote":
            if persistent.gallery_votes.get(_return[1][0], "netrual") == "upvote":
                $ delete_request("http://172.104.129.60:8080/outfit/upvote/"+str(_return[1][0]))
                $ _return[1][3] = int(_return[1][3]) - 1 
                
            $ put_request(url)
            $ persistent.gallery_votes[_return[1][0]] = "downvote"
            $ _return[1][2] = int(_return[1][2]) + 1
        else:
            $ delete_request(url)
            $ persistent.gallery_votes[_return[1][0]] = "netrual"
            $ _return[1][2] = int(_return[1][2]) - 1
            
    elif _return[0] == "import":
        $ file_path = config.basedir+"/game/outfits/"+_return[1][4].lower()+"/"+str(loadet_gallery[i][0])+loadet_gallery[i][1].split("/",-1)[-1]
        $ target_path = config.basedir+"/game/outfits/"+loadet_gallery[i][1].split("/",-1)[-1]
        if not system.path.isfile(target_path):
            $ copyfile(file_path, target_path)
            
    elif _return[0] == "sort":
        python:
            select_sorting = (select_sorting + 1) % len(sorting_modes)
            if select_sorting == 0:
                sorting_list.sort(key=lambda elm : int(elm[5]), reverse=False)
                loadet_gallery = sorting_list
            elif select_sorting == 1:
                loadet_gallery = []
                for elm in sorting_list:
                    if int(elm[5]) + month_in_sec > int(time.time()):
                        loadet_gallery.append(elm)
                    loadet_gallery.sort(key=lambda elm : int(elm[3]) - int(elm[2]), reverse=True)
            elif select_sorting == 2:
                sorting_list.sort(key=lambda elm : int(elm[3]) - int(elm[2]), reverse=True)
                loadet_gallery = sorting_list
            elif select_sorting == 3:
                sorting_list.sort(key=lambda elm : int(elm[3]) + int(elm[2]), reverse=False)
                loadet_gallery = sorting_list
                
    elif _return[0] == "dec":
        $ gallery_page -= 1
    elif _return[0] == "inc":
        $ gallery_page += 1
                
    else:
        $ hide_transitions = False
        jump main_room_menu
        
    python:
        for i in xrange(outfits_displayed):
            select_element = i+(gallery_page+outfits_displayed)
            if select_element >= len(loadet_gallery):
                pass
            else:
                outfit_cached(loadet_gallery[select_element])
                    
    jump gallery_reapet
    
    
screen gallery_outfits(character, gallery):
    zorder 6
    use close_button
    use gallery_character_menu(menu_info=character)

    if len(gallery) > 0:
        use gallery_screen(gallery)
        
screen gallery_screen(gallery):
    #Up Button
    imagebutton:
        xpos 928
        ypos 240
        idle "interface/general/"+interface_color+"/button_arrow_up.png"
        if not gallery_page <= 0:
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return(["dec"])

    #Down Button
    imagebutton:
        xpos 928
        ypos 292
        idle "interface/general/"+interface_color+"/button_arrow_down.png"
        if gallery_page < math.ceil((len(loadet_gallery)-1)/outfits_displayed):
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return(["inc"])
            
    for i in xrange(outfits_displayed):
        if i+(outfits_displayed*gallery_page) < len(loadet_gallery):
            use gallery_image((227*i)+247, character=gallery[i+(outfits_displayed*gallery_page)])
        
screen gallery_image(xx, yy=90, character):
    frame:
        style "empty"
        pos (xx, yy)
        xsize 207
        ysize 454

        add "interface/achievements/"+interface_color+"/panel_left.png"
        vbox:
            pos (6, 6)
            
            frame:
                style "empty"
                xsize 195
                ysize 30
                
                text character[1].split("/",-1)[-1] xalign 0.5
                
            $ image_path = "outfits/"+character[4].lower()+"/"+str(character[0])+character[1].split("/",-1)[-1]
            add image_path zoom get_zoom(image_path, 195, 800)
            if persistent.gallery_votes.get(character[0], "netrual") == "upvote":
                textbutton "Upvotes!:   " + str(character[3]) action Return(["upvote", character])
            else:
                textbutton "Upvotes:   " + str(character[3]) action Return(["upvote", character])
                
            if persistent.gallery_votes.get(character[0], "netrual") == "downvote":
                textbutton "DownVotes!: " + str(character[2]) action Return(["downvote", character])
            else:
                textbutton "DownVotes: " + str(character[2]) action Return(["downvote", character])
            
            
            textbutton "import" action Return(["import", character])
        
screen gallery_character_menu(xx=20, yy=90, menu_info):
    tag character_menu
    zorder 6

    
    frame:
        style "empty"
        pos (xx, yy)
        xsize 207
        ysize 454

        add "interface/achievements/"+interface_color+"/panel_left.png"
        
        vbox:
            pos (6, 384)
            button action NullAction() style "empty" xsize 195 ysize 32
            frame:
                style "empty"
                textbutton "sort: " + sorting_modes[select_sorting] style "empty" xsize 195 ysize 32 text_align (0.4, 0.5) text_size 12 hover_background btn_hover action Return(["sort"])
                
        vbox:
            pos (6, 6)
            $ tmp_x = 0
            for key, value in menu_info.iteritems():
                if not value["flag"]:
                    pass
                else:
                    if not door_show_busy and value["active"]:
                        pass
                    else:
                        $ tmp_x += 1
                        frame:
                            style "empty"
                            xsize 195
                            ysize 50
                            vbox:
                                vbox:
                                    if not value["active"]:
                                        textbutton key xsize 195 ysize 48 style "empty" hover_background "interface/achievements/"+interface_color+"/highlight_left_b.png" text_xalign 0.6 text_yalign 0.5 text_xanchor 0.5 text_size 20 action Return(["summon", key, False])
                                    else:
                                        textbutton key xsize 195 ysize 48 style "empty" hover_background "interface/achievements/"+interface_color+"/highlight_left_b.png" text_xalign 0.6 text_yalign 0.5 text_xanchor 0.5 text_size 20 text_color "#8C8C70" action Return(["summon", key, True])

                                add "interface/achievements/"+interface_color+"/spacer_left.png"
                            add "interface/achievements/"+interface_color+"/iconbox.png" yoffset 1
                            if not value["active"]:
                                $ image_zoom = crop_image_zoom("interface/icons/head/"+value.get("ico")+".png", 42, 42)
                            else:
                                $ image_zoom = crop_image_zoom("interface/icons/head/"+value.get("ico")+".png", 42, 42, True)
                            frame:
                                style "empty"
                                xsize 42
                                ysize 42
                                add image_zoom[0] zoom image_zoom[1] align (0.5, 1.0) offset (3, 4)
                            add "interface/achievements/glass_iconbox.png" pos (3, 3)
                            text value["activity"] size 10 xalign 0.625 yalign 0.9 xanchor 0.5
            