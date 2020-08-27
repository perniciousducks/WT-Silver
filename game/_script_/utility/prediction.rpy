
init -1 python:

    def predict_doll_say(doll_name, who, *args, **kwargs):
        # Call original predict function
        renpy.predict_show_display_say(who, *args, **kwargs)

        # Predict current doll state (mostly for clothing and body layers)
        doll = getattr(store, doll_name, None)
        if doll:
            renpy.display.predict.displayable(doll.get_image())

        # Predict all facial expression layers
        images_pattern = "characters/{}/face/*.webp".format(doll_name)
        for name in renpy.expand_predict(images_pattern):
            d = renpy.displayable(name)
            renpy.display.predict.displayable(d)

    def doll_prediction(doll_name):
        return renpy.partial(predict_doll_say, doll_name)

define config.predict_statements = 64
