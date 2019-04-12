init:
    default cc_pr_flirt_OBJ = event_class(name="Cho Flirt", 
                                          events=[[["cc_pr_flirt_t1_intro"], ["cc_pr_flirt_t1_event1"], ["cc_pr_flirt_t1_event2"]],
                                                  [["cc_pr_flirt_t2_event1"], ["cc_pr_flirt_t2_event2"], ["cc_pr_flirt_t2_event3"]],
                                                  [["cc_pr_flirt_t3_intro"], ["cc_pr_flirt_t3_event1"], ["cc_pr_flirt_t3_event2"]]])
                                                  
label event_class_test:
    menu:
        "-Start event-":
            $ cc_pr_flirt_OBJ.start()
        "-Set event tier-":
            $ cc_pr_flirt_OBJ.tier = int(renpy.input("Tier (0-2):", str(cc_pr_flirt_OBJ.tier), "0123456789", length=1))
            jump event_class_test
        "-Display current tier values-":
            python:
                tmp_values_display = cc_pr_flirt_OBJ.events[cc_pr_flirt_OBJ.tier]
            "{size=-5}[tmp_values_display]{/size}"
            jump event_class_test
        "-Reset all flags-":
            $ cc_pr_flirt_OBJ.tier = 0
            python:
                for i in xrange(cc_pr_flirt_OBJ.max_tiers):
                    for j in xrange(len(cc_pr_flirt_OBJ.events[i])):
                            cc_pr_flirt_OBJ.events[i][j][1] = False
            jump event_class_test
        "Exit":
            jump main_room
            
# TIER 1
################################
label cc_pr_flirt_t1_intro:
    "This is the intro {color=#80ff00}Tier1{/color}"
    jump event_class_test
    
label cc_pr_flirt_t1_event1:
    "This is the {color=#5490b5}first{/color} event in {color=#80ff00}Tier1{/color}"
    jump event_class_test
    
label cc_pr_flirt_t1_event2:
    "This is the {color=#ffae19}second{/color} event in {color=#80ff00}Tier1{/color}"
    jump event_class_test
    
# TIER 2
################################# (No intro)
label cc_pr_flirt_t2_event1:
    "This is the {color=#5490b5}first{/color} event in {color=#8000ff}Tier2{/color}"
    jump event_class_test
    
label cc_pr_flirt_t2_event2:
    "This is the {color=#ffae19}second{/color} event in {color=#8000ff}Tier2{/color}"
    jump event_class_test
    
label cc_pr_flirt_t2_event3:
    "This is the {color=#e42e4e}third{/color} event in {color=#8000ff}Tier2{/color}"
    jump event_class_test
    
# Tier 3
##################################
label cc_pr_flirt_t3_intro:
     "This is the intro {color=#b03841}Tier3{/color}"
     jump event_class_test
     
label cc_pr_flirt_t3_event1:
    "This is the {color=#5490b5}first{/color} event in {color=#b03841}Tier3{/color}"
    jump event_class_test
    
label cc_pr_flirt_t3_event2:
    "This is the {color=#ffae19}second{/color} event in {color=#b03841}Tier3{/color}"
    jump event_class_test