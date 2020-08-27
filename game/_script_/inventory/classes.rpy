
# Item classes
init -1 python:

    class Item(object):
        def __init__(self, **kwargs):
            self.id = ""
            self.name = ""
            self.type = ""
            self.items = []
            self.image = ""
            self.imagepath = "interface/icons/box_blue_2.webp"
            self.unlockable = False # If True, prevents this item to be shown in the shop.
            self.unlocked = False # Set to True once unlocked or purchased.
            self.hidden = False # Not visible in any menus.
            self.number = 0 # Amount of items of this type that you possess. Can be used for weasley store and gift items.
            self.cost = 0
            self.wait_time = 1
            self.description = ""

            # Used with decorations
            self.active = False

            self.__dict__.update(**kwargs)

        def get_name(self):
            return self.name

        def get_image(self):
            if self.image:
                if isinstance(self.image, DollOutfit):
                    return self.image.get_image()
                else:
                    self.imagepath = "interface/icons/"+str(self.image)+".webp"
                    return Image(self.imagepath)
            else:
                return self.imagepath

        def get_cost(self):
            if self.type in ("owl", "fireplace", "mail", "phoenix", "poster", "trophy", "outfit_token"):
                return str(self.cost)+" token" if self.cost == 1 else str(self.cost)+" tokens"
            else:
                return str(self.cost)+" gold"

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

        def get_annotation(self):
            return ""

    class CostumeItem(Item):

        def __init__(self, **kwargs):
            self.top_layers = []
            self.outfit_layers = []
            self.hair_layer = ""
            self.breast_layer = "breasts_nipfix"

            super(CostumeItem, self).__init__(**kwargs)

    class BookCollection(object):
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

        def is_done(self, id=""):
            for book in self.get_all():
                if book.id == id:
                    return book.done
            return None

    class Book(Item):
        chapters = 0
        progress = 0
        done = False
        effect = ""

        def __repr__(self):
            return self.id

        def get_description(self):
            out_des = ""
            if len(self.description) > 90:
                out_des = self.description[0:90] + "..."
            else:
                out_des = self.description
            return out_des

    class FictionBook(Book):
        chapter_description = []
        def get_chapter_description(self):
           return self.chapter_description[self.progress-1] #"Chapter "+str(self.progress)+": "+

    class Scroll(Item):
        scroll_image = ""
        comments = []

        def get_comment(self):
            return self.comments[renpy.random.randint(0, len(self.comments)-1)]
