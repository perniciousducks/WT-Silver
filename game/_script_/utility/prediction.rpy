
init -1 python:

    def predict_doll_say(doll_name, who, *args, **kwargs):
        # Call original predict function
        renpy.predict_show_display_say(who, *args, **kwargs)
        print "predict doll {}".format(doll_name)

        # Predict current doll state (mostly for clothing and body layers)
        doll = getattr(store, doll_name, None)
        if doll:
            print doll.get_image()
            renpy.display.predict.displayable(doll.get_image())

        print "predict face {}".format(doll_name)

        # Predict all facial expression layers
        images_pattern = "characters/{}/face/*/*.png".format(doll_name)
        for name in renpy.expand_predict(images_pattern):
            print name
            d = renpy.displayable(name)
            renpy.display.predict.displayable(d)

    def doll_prediction(doll_name):
        return renpy.partial(predict_doll_say, doll_name)

define config.predict_statements = 64

label jump_to_test:
    "Testing doll prediction"
    jump test_doll_predict

label test_doll_predict:

    $ r_temp = renpy.random.randint(0, 3)

    if r_temp == 0:
        call her_main("her", face="neutral")
        hide screen hermione_main
    elif r_temp == 1:
        call ast_main("ast", face="neutral")
        hide screen astoria_main
    elif r_temp == 2:
        call cho_main("cho", face="neutral")
        hide screen cho_main
    elif r_temp == 3:
        call ton_main("ton", face="neutral")
        hide screen tonks_main

    jump test_doll_predict
