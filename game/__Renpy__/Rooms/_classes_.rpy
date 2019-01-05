

### Classes ###

init -1 python:

    #Favours
    class room_object_class(item_class):
        room_image = ""
        room_image_path = ""

        idle_image = ""
        idle_image_path = ""

        hover_image = ""
        hover_image_path = ""

        xpos = 0
        ypos = 0

        def get_room_image(self):
            if self.room_image_path != "":
                return "" +str(self.room_image_path)+ "" +str(self.room_image)+ ".png"
            else:
                return self.room_image #stored image already has an imagepath. Can be used for animations.

        def get_idle_image(self):
            if self.idle_image_path != "":
                return "" +str(self.idle_image_path)+ "" +str(self.idle_image)+ ".png"
            else:
                return self.idle_image

        def get_hover_image(self):
            if self.hover_image_path != "":
                return "" +str(self.hover_image_path)+ "" +str(self.hover_image)+ ".png"
            else:
                return self.hover_image
