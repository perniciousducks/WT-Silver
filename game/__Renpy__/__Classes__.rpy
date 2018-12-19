

### Classes ###

init -2 python:

    #Favours
    class silver_request(object):
        menu_text = ""
        start_label = ""
        complete_label = ""
        points = 0
        progress_hint = False

    class personal_favor(silver_request):
        level = 0
        imagination_level = 0
        costume_event = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getMenuText(self):
            menu_image = "interface/heart_0"+str(self.level)+".png"
            ret_str = "\""+self.menu_text+"\" {image="+menu_image+"}"
            if self.progress_hint:
               ret_str += "  {image=interface/check_True.png}"
            if self.costume_event:
               ret_str += "  {image=interface/clothes.png}"
            return ret_str

    class public_request(silver_request):
        imagination_level = 0
        complete = False
        inProgress = False

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            ret_str = "\""+self.menu_text+"\" {image="+menu_image+"}"
            if self.progress_hint:
               ret_str += "  {image=interface/check_True.png}"
            return ret_str

    class public_shaming(silver_request):
        imagination_level = 0
        complete = False
        inProgress = False

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            ret_str = "\""+self.menu_text+"\" {image="+menu_image+"}"
            if self.progress_hint:
               ret_str += "  {image=interface/check_True.png}"
            return ret_str
