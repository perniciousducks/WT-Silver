

label read_letter:

    $ letter = letter_queue_list[0]

    $ menu_x = 0.5
    $ menu_y = 0.9

    show screen letter
    with d5
    label read_letter_again:
    call ctc

    menu:
        "-Done reading-":
            pass
        "-Not yet-":
            jump read_letter_again

    $ letter.mailRead()

    $ menu_x = 0.5
    $ menu_y = 0.5

    hide screen letter
    hide screen bld1
    with d5

    if letter.label != "":
        pause.2
        show screen bld1
        with d3

        $ renpy.call(letter.label)

        hide screen bld1
        with d3

        if letter.label == "letter_from_hermione_A" and day == 1:
            jump event_00 # First event with Snape.

    call screen main_room_menu


screen letter:
    tag letter

    add "interface/points/letter.png" at Position(xpos=340, ypos=30)
    hbox:
        spacing 40 xpos 410 ypos 80 xmaximum 250
        text letter.getLetterText()

    zorder 4



### Letter Attachment Call Labels ###

# Hermione Granger Letters.
label letter_from_hermione_A:
    m "Ehm..............................."
    m "What?"
    m "................................."

    return

# Ministry of Magic letters.
label letter_paperwork_unlock:
    m "Payments? Hm..."

    call give_reward(">From now on you can do paperwork at your desk in order to earn additional gold...","interface/icons/gold.png")

    return

label letter_paperwork_report:
    call update_report_money
    call give_reward(">You received {size=+4}"+str(report_money)+"{/size} gold coins.","interface/icons/gold.png")
    $ gold += report_money

    $ report_money = 0
    $ finished_report = 0

    return

label update_report_money:

    if game_difficulty <= 1: #easy
        $ report_money += 80*finished_report

    elif game_difficulty == 2: #normal
        $ report_money += 60*finished_report

    else: #hardcore
        $ random_number = renpy.random.randint(1, 10)

        if random_number in [1]:
            $ report_money += 10*finished_report
        elif random_number in [2]:
            $ report_money += 100*finished_report
        elif random_number in [3,4]:
            $ report_money += 30*finished_report
        elif random_number in [5,6]:
            $ report_money += 80*finished_report
        else:
            $ report_money += 60*finished_report

    return

label letter_curse_complaint:
    m "That doesn't sound good..."
    m "Perhaps I should tell Snape about this."
    m "Or maybe miss granger?"

    return








label get_package:
    show screen blktone

    python:
        for item in deliveryQ.get_mail():
            if item.type == 'Event_item':
                pass

            if item.type == 'outfit':
                gift = item.object
                gift.unlocked = True
                outfit_is_worked_on = False
                mannequin_preview = gift.get_image()

                renpy.show_screen("clothing_unlock")
                renpy.with_statement(Dissolve(0.3))

                renpy.say(None,"You received a new outfit.")

                renpy.hide_screen("clothing_unlock")
                renpy.with_statement(Dissolve(0.3))

            if item.type == 'Gift':
                gift = item.object
                gift.number += item.quantity
                the_gift = gift.get_image()

                renpy.show_screen("gift")
                renpy.with_statement(Dissolve(0.3))
                if item.quantity > 1:
                    renpy.say(None,"You received "+str(item.quantity)+" "+str(gift.name)+"'s")
                else:
                    renpy.say(None,"You received "+str(item.quantity)+" "+str(gift.name))
                renpy.hide_screen("gift")
                renpy.with_statement(Dissolve(0.3))

    hide screen blktone
    with d3

    $ package_is_here = False

    call screen main_room_menu



label __init_variables:

    if not hasattr(renpy.store,'letter_queue_list'):
        $ letter_queue_list = []
        $ report_money = 0

    # Hermione Granger Letters.
    if not hasattr(renpy.store,'letter_from_hermione_A_OBJ'):
        $ letter_from_hermione_A_OBJ = mail_letter_class()
    $ letter_from_hermione_A_OBJ.text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\nNot in this day and age, not in our school.\n\nPlease take action.\n\n{size=-3}With deepest respect,\nHermione Granger{/size}"
    $ letter_from_hermione_A_OBJ.label = "letter_from_hermione_A"

    if not hasattr(renpy.store,'letter_from_hermione_B_OBJ'):
        $ letter_from_hermione_B_OBJ = mail_letter_class()
    $ letter_from_hermione_B_OBJ.text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided inme... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.\n\n{size=-3}With deepest respect,\nHermione Granger.{/size}"
    $ letter_from_hermione_B_OBJ.label = "" #No comment on letter.


    # Ministry of Magic Letters.
    if not hasattr(renpy.store,'letter_paperwork_unlock_OBJ'):
        $ letter_paperwork_unlock_OBJ = mail_letter_class()
    $ letter_paperwork_unlock_OBJ.text = "{size=-7}From: Ministry of Magic\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore,\nWe remind you that only upon providing us with a completed report will we be able to make a payment in your name.\n\n{size=-3}With deepest respect,\nThe Ministry of Magic.{/size}"
    $ letter_paperwork_unlock_OBJ.label = "letter_paperwork_unlock"

    if not hasattr(renpy.store,'letter_paperwork_report_OBJ'):
        $ letter_paperwork_report_OBJ = mail_letter_class()
    $ letter_paperwork_report_OBJ.text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing a report this week.\n\nYou will find you payment in the attached purse.{/size}\n\n\n{size=-3}-With deepest respect-{/size}\n\n{size=-2}The Ministry of Magic.{/size}"
    $ letter_paperwork_report_OBJ.label = "letter_paperwork_report"

    if not hasattr(renpy.store,'letter_curse_complaint_OBJ'):
        $ letter_curse_complaint_OBJ = mail_letter_class()
    $ letter_curse_complaint_OBJ.text = "{size=-7}Dear Albus Dubmbledore, as we are sure you are aware, an unforgivable curse has been detected within the grounds of Hogwarts.\nWhile the punishment for such a curse is usually lifetime incarceration in the prison, Azkaban, we are allowing you to address this matter at your own discretion.\nThis is due to the possible nature of the spell being cast by a minor who has not fully grasped the serious nature of the curse.\nIf this is the case we expect no further communication from you regarding this unfortunate event.\nIf, however, you believe the curse has been cast by someone other than a student, or if any other complications arise we expect direct communication.\nLastly, the detection of any further curses will result in the immediate dispatchment of an auror to Hogwarts.\n\nCornelius Fudge,\nDepartment Head: Improper Use of Magic Office{/size}"
    $ letter_curse_complaint_OBJ.label = "letter_curse_complaint"

    return



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

    if not hasattr(renpy.store,'deliveryQ'):
        deliveryQ = deliveryQueue()

    class mail_letter_class(object):
        mailed = False
        read = False
        text = "Add Text"
        label = "" #If Genie doesn't comment on the letter, this should remain ""

        def getLetterText(self):
            return self.text

        def mailLetter(self):
            self.mailed = True
            self.read = False
            if self not in letter_queue_list:
                letter_queue_list.append(self)
            return

        def mailRead(self):
            self.read = True
            if self in letter_queue_list:
                letter_queue_list.remove(self)
            return
