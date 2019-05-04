

# Cho Gift Menu

label cho_gift_menu:

    python:

        category_list = []
        category_list.append("ui_gifts")
        #category_list.append("ui_quest_items")

        if current_category == None:
            current_category = category_list[0]
            category_choice = category_list[0]

        item_list = []
        if current_category == "ui_gifts":
            menu_title = "Gift Items"
            item_list.extend(candy_gift_list)
            item_list.extend(mag_gift_list)
            item_list.extend(drink_gift_list)
            item_list.extend(toy_gift_list)
        if current_category == "ui_quest_items":
            menu_title = "Quest Items"
            item_list.extend(toy_gift_list)

        #item_list = list(filter(lambda x: x.unlocked==False, item_list))
    show screen bottom_menu(item_list, category_list, menu_title, xpos=0, ypos=475)

    $ _return = ui.interact()

    hide screen bottom_menu
    if category_choice != current_category:
        $ current_category = _return

    elif isinstance(_return, item_class):
        if _return.number > 0:
            call give_cho_gift(_return)
        else:
            ">You don't own this item."
            jump cho_gift_menu

        if cho_mood != 0:
            jump cho_gift_menu
        else:
            jump cho_requests

    elif _return == "Close":
        $ current_page = 0
        $ category_choice = None
        hide screen bottom_menu
        with d3

        jump cho_requests

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump cho_gift_menu



# Cho Gift Responses

label give_cho_gift(gift_item):

    #$ gave_cho_gift = True

    if gift_item == lollipop_ITEM:
        if main_matches_won == 3:
            cho "Sweets?"
            call give_gift(">You give the sweets to Cho...",gift_item)
            cho "I'll keep it for later, I like licking it in front of my teammates to tease them a bit."
            cho "*mmmh*, but in the future... I'm more of a savory kind of girl when it comes to sucking on things..."
            cho "But thanks, [cho_genie_name]."
            call cho_mood_change(-1)
        elif main_matches_won == 2:
            cho "Sweets?"
            cho "But we're up against Gryffindor soon, I don't want to get addicted to sugar..."
            call give_gift(">You give the sweets to Cho...",gift_item)            
            cho "Thank you, [cho_genie_name]."
            call cho_mood_change(-1)
        elif main_matches_won == 1:
            cho "Sweets?"
            call give_gift(">You give the sweets to Cho...",gift_item)            
            cho "Thank you, [cho_genie_name] I do think I deserve one at least after winning our first match."
            call cho_mood_change(-2)
        else:
            call cho_main("Sweets?",pupils="down",face="horny",xpos="mid",ypos="base",trans="d5")
            call cho_main("My team captain hasn't let buy any to keep my blood sugar balanced, whatever that means.",mouth="soft",face="annoyed")
            call give_gift(">You give the sweets to Cho...",gift_item)
            call cho_main("But thanks, [cho_genie_name].",face="neutral")
            call cho_mood_change(-2)

    if gift_item == chocolate_ITEM:
        if main matches_won == 3:
            cho "Chocolate?"
            call give_gift(">You give the chocolate to Cho...",gift_item)
            cho "YES!"
            cho "I've been trying to stay away from it but since the season is over I can have as much as I'd like..."
            cho "Within reason."
            call cho_mood_change(-2)
        elif main_matches_won == 2:
            cho "Chocolate?"
            cho "But we're up against Gryffindor soon, I don't want to get addicted to sugar..."
            call give_gift(">You give the chocolate to Cho...",gift_item)
            cho "Thanks"
            call cho_mood_change(-1)
        elif main_matches_won == 1:
            cho "Chocolate... now that would be a treat..."
            call give_gift(">You give the chocolate to Cho...",gift_item)
            cho "What the heck, I deserve it."
            cho "Thank you, [cho_genie_name]."
            call cho_mood_change(-2)
        else:
            call cho_main("Chocolate?",pupils="down",face="horny",xpos="mid",ypos="base",trans="d5")
            call cho_main("I probably shouldn't... although.",pupils="R",face="horny")
            call give_gift(">You give the chocolate to Cho...",gift_item)
            call cho_main("I'll take it, [cho_genie_name]!",face="happy")
            call cho_mood_change(-2)

    if gift_item == plush_owl_ITEM:
        if main_matches_won == 3:
            cho "A toy?"
            call give_gift(">You give the stuffed owl to Cho...",gift_item)            
            cho "Not the kind of Toy I'd like..."
            cho "Thank you I suppose."
            call cho_mood_change(0)
        elif main_matches_won == 2:
            cho "A toy?"
            call give_gift(">You give the stuffed owl to Cho...",gift_item)            
            cho "I'm not a child [cho_genie_name]..."
            cho "Thank you I guess..."
            call cho_mood_change(0)
        elif main_matches_won == 1:
            cho "A toy?"
            call give_gift(">You give the stuffed owl to Cho...",gift_item)
            cho "That's very nice of you [cho_genie_name] but I'd probably be made fun of owning this..."
            cho "I guess I could give it to someone."
            call cho_mood_change(0)
        else:
            call cho_main("A toy?",face="annoyed",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give the stuffed owl to Cho...",gift_item)
            call cho_main("My team would probably laugh if they saw me with this...",mouth="open",face="annoyed")
            call cho_main("I guess it's cute...",face="annoyed")
            call cho_mood_change(0)

    if gift_item == butterbeer_ITEM:
        if main_matches_won == 3: 
            cho "Butterbeer?"
            cho "Don't you have any firewhisky?"
            call give_gift(">You give the Butterbeer to Cho...",gift_item)
            call cho_main("Thank you I suppose, [cho_genie_name].",face="neutral")
            call cho_mood_change(0)
        elif main_matches_won == 2: 
            cho "Butterbeer?"
            cho "It's a bit tame isn't it? I chugged a lot of it after our last win and can't say I felt a buzz even."
            call give_gift(">You give the Butterbeer to Cho...",gift_item)
            call cho_main("Thank you I suppose, [cho_genie_name].",face="neutral")
            call cho_mood_change(0)
        elif main_matches_won == 1:
            cho "Butterbeer?"
            cho "Yes, I'll take it... turns out my team mates had been lying about the alcohol content to mess with me."
            cho "I guess I'll finally find out what I've been missing out on!"
            call give_gift(">You give the Butterbeer to Cho...",gift_item)  
            call cho_main("Thank you, [cho_genie_name].",face="neutral")            
            call cho_mood_change(-2)
        else:
            call cho_main("Butterbeer?",face="disgusted",xpos="mid",ypos="base",trans="d5")
            call cho_main("Isn't this supposed to be alcoholic? I'm not supposed to drink during the season...",face="annoyed")
            call cho_mood_change(1)

    if gift_item == science_mag_ITEM:
        if main_matches_won == 3: 
            cho "Experts guide, How to maintain and store your Quidditch gear."
            cho "Isn't that what a broom closet is for?"
            call give_gift(">You give an assortment of educational magazines to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-1)
        elif main_matches_won == 2:
            cho "5 steps to modify your brooms legally..."
            cho "Seems be useful."
            call give_gift(">You give an assortment of educational magazines to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-1)
        elif main_matches_won == 1:
            cho "*Hmm,* Broom aerodynamics and how to utilize your opponents slipstream..."
            cho "Interesting..."
            call give_gift(">You give an assortment of educational magazines to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-1)
        else:
            call cho_main("Oh, I heard that they put out a new formula for broom polish in this issue.",mouth="open",pupils="R",face="neutral",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give an assortment of educational magazines to Cho...",gift_item)
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-1)

    if gift_item == girls_mag_ITEM:
        if main_matches_won == 3:
            cho "Girls magazines?"
            cho "I did enjoy last months issue about cultural appropriation with traditional clothing..."
            call give_gift(">You give an assortment of rather girly magazines to Cho...",gift_item)
            cho "Don't tell the boys I said that."
            call cho_main("Thank you, [cho_genie_name].",face="neutral") 
            call cho_mood_change(-1)
        elif main_matches_won == 2:
            cho "Girls magazines?"
            call give_gift(">You give an assortment of rather girly magazines to Cho...",gift_item)
            cho "They do have some interesting stuff on skincare I suppose..."
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-1)
        elif main_matches_won == 1:
            call cho_main("Girls magazines?",pupils="down",face="annoyed",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give an assortment of rather girly magazines to Cho...",gift_item)
            call cho_main("I don't usually read these types of magazines, the boys used to make fun of me for it.",face="annoyed")
            call cho_main("But they can't get into the girls dorm.",face="neutral")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-1)
        else:
            cho "Girls magazines, what do you think I am... a gi-"
            cho "I'm good thank you..."
            call cho_mood_change(0)

    if gift_item == adult_mag_ITEM:
        if main_matches_won == 3:    
            cho "Adult magazines?"
            cho "Wow, look at that guys abs..."
            cho "And that girls..."
            cho "I'll take it."
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-2)
        elif main_matches_won == 2: 
            cho "Adult magazines?"
            cho "They're all so fit in these magazines, totally my type."
            cho "Does this one model in the nude?"
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-1)
        elif main_matches_won == 1:
            call cho_main("Adult magazines?",face="disgusted",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give an assortment of adult magazines to Cho...",gift_item)
            call cho_main("These people do have nice, posture...",face="horny")
            call cho_main("I... I guess they could be useful.",face="horny")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-1)
        else:
            cho "Adult magazines?"
            cho "This is highly inappropriate [cho_genie_name]!"
            cho "Is this the kind of thing you usually give to people?"
            call cho_mood_change(1)

    if gift_item == porn_mag_ITEM:
        if main_matches_won == 3:   
            cho "Porn magazines?"
            cho "Ooh, are those two doing it on a broom? That's impressive..."
            cho "[cho_genie_game], this is naughty. Even for you..."
            cho "I've got my eyes on you."
            call give_gift(">You give an assortment of porn magazines to Cho...",gift_item)
            cho "Thank you."
            call cho_mood_change(-3)
        elif main_matches_won == 2:
            call cho_main("What's this?",face="annoyed",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give an assortment of porn magazines to Cho...",gift_item)
            call cho_main("What's with these positions? Is that a broom handle up her...",mouth="open",eyes="wide",eyebrows="raised",pupils="down")
            call cho_main("Oh my-...",mouth="soft",pupils="R",face="disgusted")
            call cho_mood_change(0)
        elif main_matches_won == 1:
            cho "What is this?"
            cho "Porn magazines? Sir, that's too much even for you..."
            cho "Is that a snitch in her sna... No... just no..."
            call cho_mood_change(2)
        else:
            cho "What is this!?!"
            cho "Porn magazines? Sir, why would you even think of giving me something like this?"
            call cho_mood_change(3)

    if gift_item == krum_poster_ITEM:       
        if main_matches_won == 3:
            call cho_main("A Viktor Krum poster?",mouth="scream",eyes="wide",eyebrows="raised",pupils="mid",xpos="mid",ypos="base",trans="hpunch")
            call give_gift(">You give the poster to Cho...",gift_item)
            call cho_main("I'll take that if you don't mind.",pupils="downR",face="horny")
            call cho_main("(...)",mouth="soft",pupils="up",face="horny")
            call cho_main("I love it, [cho_genie_name].",pupils="mid",face="horny")
            call cho_mood_change(-5)
        elif main_matches_won == 2:
            cho "A Viktor Krum poster?"
            cho "Wasn't his nudes leaked in Wizard Hunks weekly?"
            cho "..."
            cho "Not that I'd read such a thing."
            call give_gift(">You give the poster to Cho...",gift_item)
            cho "Thank you [cho_genie_name]."            
            call cho_mood_change(-3)
        elif main_matches_won == 1: 
            cho "A viktor Krum poster?"
            cho "He really is quite muscular isn't he..."
            cho "I'll use it..."
            call give_gift(">You give the poster to Cho...",gift_item)
            cho "As a motivational poster that is!"
            cho "Thank you [cho_genie_name]."
            call cho_mood_change(-2)
        else:
            cho "A viktor Krum poster?"
            cho "Professor, he doesn't have his shirt on!"
            cho "That's...{w=0.3} highly inappropriate..."
            cho "I can't...{w=0.3} I can't accept this."
            call cho_mood_change(0)

    if gift_item == sexy_lingerie_ITEM:
        if main_matches_won == 3:  
            cho "Lingerie?"
            cho "Sexy... Did you pick them out yourself?"
            cho "You've got good taste... I tore mine last year during the ball..."
            cho "Well, someone tore them at least..."
            call give_gift(">You give the lingerie to Cho...",gift_item)
            cho "Thank you [cho_genie_name]"
            call cho_mood_change(-3)
        elif main_matches_won == 2:
            call cho_main("Lingerie?",face="annoyed",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give the lingerie to Cho...",gift_item)
            call cho_main("Seems pretty flexible. I might be able use these when stretching.",mouth="pout",pupils="down",face="annoyed")
            call cho_mood_change(-2)
        elif main_matches_won == 1:
            cho "Lingerie?"
            cho "Why would I want this? I have plenty of clothes I like already..."
            cho "I'll pass on that one, thanks."
            call cho_mood_change(0)
        else:
            cho "Lingerie?"
            cho "Sir, are you expecting me to wear this?"
            cho "Are you insane?!"
            cho "No thank you..."
            call cho_mood_change(2)

    if gift_item == pink_condoms_ITEM:
        if main_matches_won == 3:
            call cho_main("Condoms?",face="annoyed",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give a pack of condoms to Cho...", gift_item)
            call cho_main("I do surround myself with mostly boys, so having these at hand could be useful...",pupils="downR",face="horny")
            call cho_main("Thank you for your concerns, [cho_genie_name]...",mouth="soft",pupils="mid",face="neutral")
            call cho_mood_change(-2)
        elif main_matches_won == 2:
            cho "Condoms?"
            cho "Are you expecting me that I should use these? I know safe sex is important and all but I know what you're insinuating."
            cho "Keep them..."
            call cho_mood_change(0)
        elif main_matches_won == 1:
            cho "Condoms?"
            cho "I'm not the kind of girl to go around banging everything I come across..."
            cho "Thanks but no thanks..."
            call cho_mood_change(1)
        else:
            cho "Condoms?"
            cho "You're expecting me to go and fuck the teachers, is that what you want?"
            cho "I'm not one of those Slytherin skanks that impale themselves daily on the teachers."
            cho "Get them away from me..."
            call cho_mood_change(2)

    if gift_item == vibrator_ITEM:
        if main_matches_won == 3:
            call cho_main("A Vibrator?",face="horny",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give the vibrator to Cho...", gift_item)
            call cho_main("Ahh, It does promote a healthy lifestyle...",face="horny")
            call cho_main("Thank you, [cho_genie_name].",face="happy")
            call cho_mood_change(-3)
        elif main_matches_won == 2:
            cho "A vibrator?"
            cho "Sir, I don't think this would be appropriate to bring to my dorm..."
            cho "The girls... they'd hear it... not that I want it or anything!"
            call cho_mood_change(0)
        elif main_matches_won == 1:
            cho "A vibrator?"
            cho "Why would you give me that..."
            cho "Give it to Granger, I'm sure she'd love to accept a sex toy from her headmaster."
            call cho_mood_change(2)
        else:
            cho "A vibrator?"
            cho "Sir, are you out of your mind?"
            cho "I'm your student for crying out loud, giving gifts in general is a bit weird but sex toys..."
            cho "Seriously?!"
            call cho_mood_change(3)

    if gift_item == anal_lube_ITEM:   
        if main_matches_won == 3:
            call cho_main("Lubricant?",face="annoyed",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give the jar of anal lube to Cho...", gift_item)
            call cho_main("You should've given me this yesterday, [cho_genie_name].",mouth="soft",face="annoyed")
            call cho_main("I haven't been able to sit on a broom all day after yesterday's game...",mouth="pout",pupils="down",face="annoyed")
            call cho_mood_change(-5)
        elif main_matches_won == 2:
            cho "Anal lube?"
            cho "Why would I need something like this? The broom goes under my butt, not in my butt..."
            call cho_mood_change(0)
        elif main_matches_won == 1:
            cho "A lube?"
            cho "*Ew* Why are you giving me this... when would I ever have the need for lube."
            cho "Give it to one of those Slytherin skanks, they probably go through a ton of it every week."
            call cho_mood_change(3)
        else:
            cho "A lubricant?"
            cho "What the hell, why do you think this is an appropriate gift? What's wrong with you..."
            cho "Senile old man..."
            call cho_mood_change(4)

    if gift_item == ballgag_and_cuffs_ITEM:
        if main_matches_won == 3:
            call cho_main("Ball gag and cuffs?",pupils="down",face="annoyed",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give the ball gag and cuffs to Cho...", gift_item)
            call cho_main("How progressive... do they require a safe-word to open?",face="horny")
            call cho_main("Wait, how would a safe-word work when you have a ball in your mouth...",mouth="quiver",eyes="wide",eyebrows="raised",pupils="down")
            call cho_mood_change(-3)
        elif main_matches_won == 2:
            cho "Ball gag and cuffs?"
            cho "I prefer not to lock myself up, I'm a free spirit."
            cho "Thanks... but no thanks."
            call cho_mood_change(0)
        elif main_matches_won == 1:
            cho "Ball gag and cuffs?"
            cho "Sir, this is highly inappropriate gift to give to a student"
            cho "Why would you give me these, how is this going to help me with Quidditch?"
            call cho_mood_change(3)
        else:
            cho "Ball gag... and cuffs?"
            cho "Wait, is this a sex thing?"
            cho "Professor, that's disgusting... why would you give me this."
            call cho_mood_change(4)

    if gift_item == anal_plugs_ITEM:
        if main_matches_won == 3:
            call cho_main("Anal plugs?",face="annoyed",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give a set of anal plugs to Cho...", gift_item)
            call cho_main("But these would stick out under my robes...",face="annoyed")
            call cho_main("Maybe people would just think it's a tail or something...",face="horny")
            call cho_main("Thank you, [cho_genie_name].",face="neutral")
            call cho_mood_change(-2)
        elif main_matches_won == 2:
            cho "Anal plugs?"
            cho "Sir, are you expecting me to wear this?"
            cho "During Quidditch?"
            cho "No, no, no, no no."
            cho "NO!"
            call cho_mood_change(2)
        elif main_matches_won == 1:
            cho "Anal plugs?"
            cho "Why do you have these? They're not used are they..."
            cho "*Ew* Just, no..."
            call cho_mood_change(3)
        else:
            cho "Anal plugs?"
            cho "That's disgusting... why do you think it's a good idea to give these to me?"
            cho "That one has a tail on it..."
            call cho_mood_change(4)

    if gift_item == testral_strapon_ITEM:
        if main_matches_won == 3:
            call cho_main("A strap-on?",mouth="open",eyes="wide",eyebrows="sad",pupils="down",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give the thestral strap-on to Cho...", gift_item)
            call cho_main("How would that even fit in anyone?",mouth="quiver",eyes="wide",eyebrows="raised",pupils="down")
            call cho_mood_change(-1)
        elif main_matches_won == 2:
            cho "A strap-on?"
            cho "But it's so big..."
            cho "I.. I don't want it..."
            call cho_mood_change(0)
        elif main_matches_won == 1:
            cho "A strap-on?"
            cho "Seriously? Why are you giving me this..."
            cho "That's disgusting..."
            call cho_mood_change(2)
        else:
            cho "Is that a strap-on?"
            cho "It's huge!"
            cho "I mean, why are you showing me this?"
            cho "get it away from me."
            call cho_mood_change(3)

    if gift_item == broom_2000_ITEM:
        if main_matches_won == 3:
            call cho_main("Is that a skittle diddler 2000, with a built-in vibrator and pulse function?",mouth="scream",eyes="wide",eyebrows="raised",pupils="down",xpos="mid",ypos="base",trans="hpunch")
            call give_gift(">You give the broom to Cho...", gift_item)
            call cho_main("I mean, it's a nice broom alright...",pupils="downR",face="horny")
            call cho_main("But, to be honest, [cho_genie_name]...",mouth="soft",pupils="down",face="horny")
            call cho_main("I can't wait to try it out!",pupils="mid",face="happy")
            call cho_mood_change(-6)
        elif main_matches_won == 2:
            cho "A broom?"
            cho "A sex broom? Where did you even get this..."
            cho "No..{w=0.3} I don't...{w=0.3} I don't want that."
            call cho_mood_change(0)
        elif main_matches_won == 1:
            cho "Is that a broom with dildos on it?"
            cho "Professor, seriously... why... just why."
            call cho_mood_change(2)
        else:
            cho "A broom... yes! Finally something better than my old-"
            cho "Hold on, is that a double ended dildo sticking out of it?!?"
            cho "What's wrong with you?"
            cho "Get that away from my... from me!"
            call cho_mood_change(4)

    if gift_item == sexdoll_ITEM:    
        if main_matches_won == 3:
            call cho_main("A sex doll?",face="annoyed",xpos="mid",ypos="base",trans="d5")
            call give_gift(">You give the sex doll to Cho...", gift_item)
            call cho_main("It says Joanne on it...",face="disgusted")
            call cho_main("I leave it in the boys changing room, should be a good reward after a practice.",face="annoyed")
            call cho_mood_change(-7)
        elif main_matches_won == 2:
            cho "A sex doll?"
            cho "Why would I need this, it's a girl doll..."
            cho "I mean, why would I need a sex doll in general. I'm not into this sort of thing..."
            call cho_mood_change(1)  
        elif main_matches_won == 1:
            cho "A sex doll?"
            cho "Why would you give this to me? Wait, did you use this?"
            cho "Get it away from me..."
            call cho_mood_change(3)
        else:
            cho "A sex doll? What the heck... why do you have this?"
            cho "And more importantly..."
            cho "{size=+4}Why are you giving it to me?{/size}"
            cho "You disgust me..."
            call cho_mood_change(4)

    call cho_main(xpos="base",ypos="base",trans="d5")

    return

label cho_mood_change(value=0):
    show screen blktone5
    with d3

    if value > 0:
        if value == 1:
            "Cho's mood worsened slightly."
        else:
            "Cho's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Cho's mood has improved slightly."
        else:
            "Cho's mood has improved significantly."
    else:
        "Cho's mood hasn't changed."
            
    $ cho_mood = max(min(cho_mood+value, 100), 0)
    hide screen blktone5
    return
