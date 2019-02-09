

label room_objects_init:

    if not hasattr(renpy.store,'fireplace_OBJ'):
        $ fireplace_OBJ = room_object_class(type="fireplace",
            room_image="fireplace_w_shadow", room_image_path="images/rooms/_objects_/fireplace/",
            idle_image="fireplace_idle",     idle_image_path="images/rooms/_objects_/fireplace/",
            hover_image="fireplace_hover",   hover_image_path="images/rooms/_objects_/fireplace/",
            xpos=693, ypos=277)
        $ cupboard_top_OBJ = room_object_class(type="cupboard",
            idle_image="idle_scroll",      idle_image_path="images/rooms/_objects_/cupboard/",
            hover_image="hover_scroll",    hover_image_path="images/rooms/_objects_/cupboard/",
            xpos=260, ypos=280)
        $ cupboard_OBJ = room_object_class(type="cupboard",
            room_image="cupboard_w_shadow",  room_image_path="images/rooms/_objects_/cupboard/",
            idle_image="cupboard_idle",      idle_image_path="images/rooms/_objects_/cupboard/",
            hover_image="cupboard_hover",    hover_image_path="images/rooms/_objects_/cupboard/",
            xpos=260, ypos=280)
        $ hat_OBJ = room_object_class(type="hat",
            room_image="hat_idle",      room_image_path="images/rooms/_objects_/cupboard/",
            idle_image="hat_idle",      idle_image_path="images/rooms/_objects_/cupboard/",
            hover_image="hat_hover",    hover_image_path="images/rooms/_objects_/cupboard/",
            xpos=260, ypos=280)
        $ phoenix_OBJ = room_object_class(type="phoenix",
            room_image="phoenix_01",      room_image_path="images/rooms/_objects_/phoenix/",
            idle_image="pho_01",          idle_image_path="",
            hover_image="phoenix_hover",  hover_image_path="images/rooms/_objects_/phoenix/",
            xpos=557, ypos=272)
        $ door_OBJ = room_object_class(type="door",
            room_image="door_idle",      room_image_path="images/rooms/_objects_/doors/",
            idle_image="door_idle",      idle_image_path="images/rooms/_objects_/doors/",
            hover_image="door_hover",    hover_image_path="images/rooms/_objects_/doors/",
            xpos=898, ypos=315)

        #$ carpet_OBJ       = room_object_class(type="carpet", room_image="", xpos=0, ypos=0)

        $ candle_left_OBJ = room_object_class(type="candle",
            room_image="candle",  room_image_path="images/rooms/_objects_/candles/",
            xpos=350, ypos=160)
        $ candle_right_OBJ = room_object_class(type="candle",
            room_image="candle", room_image_path="images/rooms/_objects_/candles/",
            xpos=833, ypos=225)

        $ owl_OBJ = room_object_class(type="mail",
            room_image="owl_idle",              room_image_path="images/rooms/_objects_/mail/",
            idle_image="owl_with_letter_blink", idle_image_path="",
            hover_image="owl_hover",            hover_image_path="images/rooms/_objects_/mail/",
            xpos=455, ypos=289)

        $ package_OBJ = room_object_class(type="mail",
            room_image="package_idle",      room_image_path="images/rooms/_objects_/mail/",
            idle_image="package_idle",      idle_image_path="images/rooms/_objects_/mail/",
            hover_image="package_hover",    hover_image_path="images/rooms/_objects_/mail/",
            xpos=402, ypos=290)

    if not hasattr(renpy.store,'deco_list'):

        $ deco_list = []
        $ deco_overlay_list = []

        $ xmas_fireplace_deco_ITEM = room_object_class(type="fireplace", image="deco/fireplace_xmas", unlockable=True,
            room_image="fireplace_deco_xmas", room_image_path="images/rooms/_objects_/fireplace/")

        # New Decorations
        $ poster_OBJ = room_object_class(type="poster", room_image="", room_image_path="images/rooms/_objects_/posters/", xpos=332, ypos=260)
        $ trophy_OBJ = room_object_class(type="trophy", room_image="", room_image_path="images/rooms/_objects_/trophies/", xpos=690, ypos=150)
        # Phoenix hat
        $ phoenix_deco_OBJ = room_object_class(type="phoenix_deco", room_image="", room_image_path="images/rooms/_objects_/phoenix/", xpos=phoenix_OBJ.xpos, ypos=phoenix_OBJ.ypos-42)
        $ fireplace_deco_OBJ = room_object_class(type="fireplace_deco", room_image="", room_image_path="images/rooms/_objects_/fireplace/", xpos=fireplace_OBJ.xpos, ypos=fireplace_OBJ.ypos)
        $ owl_deco_OBJ = room_object_class(type="owl_deco", room_image="", room_image_path="images/rooms/_objects_/mail/", xpos=owl_OBJ.xpos, ypos=owl_OBJ.ypos)
        #

    return
