
init -1 python:

    class RoomObject(object):

        def __init__(self, **kwargs):
            self.type = ""

            self.room_image = ""
            self.room_image_path = ""

            self.idle_image = ""
            self.idle_image_path = ""

            self.hover_image = ""
            self.hover_image_path = ""

            self.xpos = 0
            self.ypos = 0

            self.__dict__.update(**kwargs)

        def get_room_image(self):
            if self.room_image_path != "":
                return "" +str(self.room_image_path)+ "" +str(self.room_image)+ ".webp"
            else:
                return self.room_image #stored image already has an imagepath. Can be used for animations.

        def get_idle_image(self):
            if self.idle_image_path != "":
                return "" +str(self.idle_image_path)+ "" +str(self.idle_image)+ ".webp"
            else:
                return self.idle_image

        def get_hover_image(self):
            if self.hover_image_path != "":
                return image_hover("" +str(self.hover_image_path)+ "" +str(self.hover_image)+ ".webp")
            else:
                return self.hover_image
