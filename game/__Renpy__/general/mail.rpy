init python:

    class deliveryItem(object):
        object = None
        transit_time = 0
        quantity=1
        type = ''

        def __init__(self,object,transit_time,quantity,type):
            self.object = object
            self.transit_time = transit_time
            self.quantity = quantity
            self.type = type

    class deliveryQueue(object):
        queue = []
        max_wait = 15

        def send(self, item, transit_time, quantity, type):
            if transit_time > self.max_wait:
                transit_time = self.max_wait
            self.queue.append(deliveryItem(item, transit_time, quantity, type))

        def got_mail(self):
            for i in self.queue:
                i.transit_time -= 1
            for i in self.queue:
                if i.transit_time <= 0:
                    return True
            return False

        def get_mail(self):
            delivery = []
            for i in self.queue:
                if i.transit_time <= 0:
                    delivery.append(i)
            for i in delivery:
                self.queue.remove(i)
            return delivery

    deliveryQ = deliveryQueue()

label mail:
    if finished_report >= 1:
        $ letters -= 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        $ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
        hide screen owl
        show screen owl_02
        ">You read your mail."
        play sound "sounds/money.mp3"  #Quiet...

        if game_difficulty <= 1: #Rewards Doubled.
            if finished_report == 1:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing one report this week.\nHere is your payment:{/size} \n{size=+4}80 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 80

            if finished_report == 2:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing two reports this week.\nHere is your payment:{/size} \n{size=+4}140 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 140

            if finished_report == 3:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing three reports this week.\nHere is your payment:{/size} \n{size=+4}180 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 180

            if finished_report == 4:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing four reports this week.\nHere is your payment:{/size} \n{size=+4}220 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 220

            if finished_report == 5:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing five reports this week.\nHere is your payment:{/size} \n{size=+4}300 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 300

            if finished_report >= 6:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing six reports this week.\nHere is your payment:{/size} \n{size=+4}400 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 400

        elif game_difficulty == 2: #normal difficulty
            if finished_report == 1:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing one report this week.\nHere is your payment:{/size} \n{size=+4}60 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 60

            if finished_report == 2:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing two reports this week.\nHere is your payment:{/size} \n{size=+4}90 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 90

            if finished_report == 3:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing three reports this week.\nHere is your payment:{/size} \n{size=+4}120 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 120

            if finished_report == 4:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing four reports this week.\nHere is your payment:{/size} \n{size=+4}160 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 160

            if finished_report == 5:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing five reports this week.\nHere is your payment:{/size} \n{size=+4}220 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 220

            if finished_report >= 6:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing six reports this week.\nHere is your payment:{/size} \n{size=+4}300 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 300

        else: #hardcore difficulty
            if finished_report == 1:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing one report this week.\nHere is your payment:{/size} \n{size=+4}40 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 40

            if finished_report == 2:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing two reports this week.\nHere is your payment:{/size} \n{size=+4}70 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 70

            if finished_report == 3:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing three reports this week.\nHere is your payment:{/size} \n{size=+4}90 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 90

            if finished_report == 4:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing four reports this week.\nHere is your payment:{/size} \n{size=+4}110 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 110

            if finished_report == 5:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing five reports this week.\nHere is your payment:{/size} \n{size=+4}150 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 150

            if finished_report >= 6:
                $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing six reports this week.\nHere is your payment:{/size} \n{size=+4}200 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"
                $ gold += 200

        show screen bld1
        show screen letter
        show screen ctc
        pause
        hide screen letter
        hide screen bld1
        hide screen ctc

        $ finished_report = 0

        call screen main_room_menu


### MAIL FROM HERMIONE ###
#place after ### MAIL FROM HERMIONE ###

if outfit_ready:
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}From: Madam Mafkin\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore.\nThis is a reminder that you have an order ready for pickup at the clothes store\n\n{size=-3}Thank you for your busness,\n M.M.{/size}"
    label letter_outfit:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump letter_outfit
    $ letters -= 1
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_room_menu

if day == 1:
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger-{/size}"
    $ letter_text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided in me... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.\n\n{size=-3}With deepest respect,\nHermione Granger.{/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter01_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump letter01_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    show screen bld1
    with d3
    m "Ehm..............................."
    m "What?"
    m "................................."
    hide screen bld1
    with d3
    jump event_00
    #call screen main_room_menu



if letter_from_hermione_02: #Letter from Hermione #02.
    $ letter_from_hermione_02 = False
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger--{/size}"
    $ letter_text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided inme... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.\n\n{size=-3}With deepest respect,\nHermione Granger.{/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter02_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump letter02_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_room_menu

if ministry_letter: #Letter from the ministry
    $ ministry_letter = False
    $ letter_text = "{size=-7}Dear Albus Dubmbledore, as we are sure you are aware, an unforgivable curse has been detected within the grounds of Hogwarts.\nWhile the punishment for such a curse is usually lifetime incarceration in the prison, Azkaban, we are allowing you to address this matter at your own discretion.\nThis is due to the possible nature of the spell being cast by a minor who has not fully grasped the serious nature of the curse.\nIf this is the case we expect no further communication from you regarding this unfortunate event.\nIf, however, you believe the curse has been cast by someone other than a student, or if any other complications arise we expect direct communication.\nLastly, the detection of any further curses will result in the immediate dispatchment of an auror to Hogwarts.\n\nCornelius Fudge,\nDepartment Head: Improper Use of Magic Office{/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label ministry_letter_again:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump ministry_letter_again
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    m "That doesn't sound good..."
    m "Perhaps I should tell Snape about this."
    m "Or maybe miss granger?"

    #Unlocks next event.
    $ ministry_letter_received = True
    call screen main_room_menu





### MAIL THAT UNLOCKS ABILITY TO WORK ###
if work_unlock: # Send a letter that will unlock an ability to write reports
    $ work_unlock = False # Send a letter that will unlock an ability to write reports
    $ letters -= 1
    $ work_unlock2 = True # Unlocks the "Paperwork" button.
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}From: Ministry of Magic\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore,\nWe remind you that only upon providing us with a completed report will we be able to make a payment in your name.\n\n{size=-3}With deepest respect,\nThe Ministry of Magic.{/size}"
    label letter_work:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump letter_work
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    m "Payments? Hm..."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    ">From now on you can do paperwork at your desk in order to earn additional gold..."
    hide screen blktone8
    with d3
    call screen main_room_menu



label get_package:
    python:
        for item in deliveryQ.get_mail():
            if item.type == 'Gift':
                gift = item.object
                gift_item_inv[gift.id] += item.quantity
                the_gift = gift.image
                renpy.show_screen("gift")
                renpy.with_statement(Dissolve(0.3))
                if item.quantity > 1:
                    renpy.say(None,"You received "+str(item.quantity)+" "+str(gift.name)+"'s")
                else:
                    renpy.say(None,"You received "+str(item.quantity)+" "+str(gift.name))
                renpy.hide_screen("gift")
                renpy.with_statement(Dissolve(0.3))

            if item.type == 'Event_item':
                pass

    $ package_is_here = False
    call screen main_room_menu

label mail_02: #Packages only. <=====================================================================### PACKAGES ###===================================================

### ITEMS ###
    if gift_order != None:
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True

        $ gift_item_inv[gift_order.id] += order_quantity

        $ the_gift = gift_order.image
        show screen gift
        with d3
        $ tmp_str = "\""+gift_order.name
        if order_quantity > 1:
            $ tmp_str += "'s\""
            ">([order_quantity]) [tmp_str] have been added to your possessions."
        else:
            $ tmp_str += "\""
            ">([order_quantity]) [tmp_str] has been added to your possessions."
        hide screen gift
        with d3
        $ gift_order = None
        call screen main_room_menu



init python:

    class mail_letter_class(object):
        id = ""
        mailed = False
        read = False
        text = ""

        def mailLetter(self):
            self.mailed = True
            self.read = False
            if self not in mail_queue_list:
                return mail_queue_list.append(self)
            else:
                return

        def mailRead(self):
            self.read = True
            return mail_queue_list.remove(self)

        def getLetterText(self):
            return self.text
