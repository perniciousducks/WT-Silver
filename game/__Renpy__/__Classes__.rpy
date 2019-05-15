

### Classes ###

init -2 python:

    #Favours
    class silver_request(object):
        title        = ""
        tier         = 0
        start_label  = ""
        complete_label = ""
        points       = 0 # For progress checks. Can be reset if needed.
        counter      = 0 # For stats
        hint         = False

    class favor_class(silver_request):
        level        = 0 # Hearts
        max_level    = 3
        heart_color  = "red"

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getMenuText(self):
            heart_list = []
            menu_text = None
            for i in xrange(self.max_level):
                if i < self.level:
                    heart_list.append("interface/icons/small/heart_"+self.heart_color+".png")
                else:
                    heart_list.append("interface/icons/small/heart_empty.png")

            # Before Text
            if self.hint:
                menu_text = "{image=interface/check_True.png} "
            # Main Text
            if menu_text != None:
                menu_text += "\""+self.title+"\" "
            else:
                menu_text = "\""+self.title+"\" "
            # After Text
            for i in xrange(len(heart_list)):
                menu_text += "{image="+str(heart_list[i])+"}"

            return menu_text

    class request_class(silver_request):
        complete = False
        inProgress = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            ret_str = "\""+self.title+"\" {image="+menu_image+"}"
            if self.hint:
               ret_str += "  {image=interface/check_True.png}"
            return ret_str

    class shaming_class(silver_request):
        complete = False
        inProgress = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            ret_str = "\""+self.title+"\" {image="+menu_image+"}"
            if self.hint:
               ret_str += "  {image=interface/check_True.png}"
            return ret_str
