### Item Classes ###

init -2 python:

    #Items Main
    class item_class(object):
        def __init__(self, **kwargs):
            self.id = ""
            self.name = ""
            self.type = ""
            self.items = []
            self.image = ""
            self.imagepath = "interface/icons/box_blue_2.png"
            self.unlockable = False #If True, prevents this item to be shown in the shop.
            self.unlocked = False #Set to True once unlocked or purchased.
            self.number = 0 #Amount of items of this type that you possess. Can be used for weasley store and gift items.
            self.cost = 0
            self.wait_time = 1
            self.description = ""

            #Used in decorations
            self.active = False # Check if decoration is used or not

            self.__dict__.update(**kwargs)

        def get_name(self):
            return self.name

        def get_image(self):
            if self.image != "":
                self.imagepath = "interface/icons/"+str(self.image)+".png"
                return self.imagepath
            else:
                return self.imagepath

        # Need to simplify this
        def get_cost(self):
            if self.type == "poster" or self.type == "trophy" or self.type == "outfit_token":
                if self.cost == 1:
                    return ""+str(self.cost)+" token"
                else:
                    return ""+str(self.cost)+" tokens"
            else:
                return ""+str(self.cost)+" gold"

        def get_wait_time(self):
            if self.wait_time == 1:
                return "Wait Time: "+str(self.wait_time)+" day."
            else:
                return "Wait Time: "+str(self.wait_time)+" days."

        def get_items(self):
            return self.items
        def get_type(self):
            return self.type
        def get_description(self):
            return self.description
        def get_buttom_right(self):
            return ""

    #Outfit Items
    class costume_class(item_class):
        
        def __init__(self, **kwargs):
            self.top_layers = []
            self.outfit_layers = []
            self.actions = []
            self.action_images = []
            self.hair_layer = ""
            self.breast_layer = "breasts_nipfix"

            super(costume_class, self).__init__(**kwargs)

        def getOutfitLayers(self):
            return self.outfit_layers
        def getHairLayers(self):
            return self.hair_layer
        def getTopLayers(self):
            return self.top_layers
        def getActionImage(self, action):
            return self.action_images[self.actions.index(action)]

    #Book Items
    class silver_book_lib(object):
        read_books = []
        write_books = []
        fiction_books = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_all(self):
            all_books = []
            all_books.extend(self.read_books)
            all_books.extend(self.write_books)
            all_books.extend(self.fiction_books)
            return all_books
        def get_edu(self):
            edu_books = []
            edu_books.extend(self.read_books)
            edu_books.extend(self.write_books)
            return edu_books
        def get_fic(self):
            return self.fiction_books

        def isDone(self, id=""):
            for book in self.get_all():
                if book.id == id:
                    return book.done
            return None

    class book_class(item_class):
        chapters = 0
        progress = 0
        done = False
        effect = ""

        def __repr__(self):
            return self.id
        def getMenuText(self):
            return "-"+str(self.name)+"-"
        def getMenuTextDone(self):
            return "-"+str(self.name)+"-{image=check_08}"

        def get_description(self):
            out_des = ""
            if len(self.description) > 90:
                out_des = self.description[0:90] + "..."
            else:
                out_des = self.description
            return out_des

    class educational_book(book_class):
        pass

    class fiction_book(book_class):
        chapter_description = []
        def getChapterDesc(self):
           return self.chapter_description[self.progress-1] #"Chapter "+str(self.progress)+": "+

    #Scroll Items
    class scroll_class(item_class):
        scroll_image = ""
        comments = []

        def get_comment(self):
            return self.comments[renpy.random.randint(0, len(self.comments)-1)]
