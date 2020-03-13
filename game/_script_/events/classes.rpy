

### Classes ###

init -1 python:

    #Favours
    class shaming_class(object):
        title        = ""
        tier         = 0
        start_label  = ""
        complete_label = ""
        points       = 0 # For progress checks. Can be reset if needed.
        counter      = 0 # For stats
        hint         = False

        inProgress = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_menu_item(self, disabled=False, return_value=None):
            menu_text = ""

            if self.hint:
                menu_text += "{image=interface/check_True.png}"

            if self.title:
                menu_text += "\"{}\"".format(self.title)

            if disabled:
                menu_text = "{color=[menu_disabled]}" + menu_text + "{/color}"

            if return_value is None:
                return_value = "block" if disabled else self.start_label

            action = renpy.ui.ChoiceReturn(None, return_value, kwargs={})

            return (menu_text, action)
