
init -1 python:

    class shaming_class(object):
        #TODO This class should be replaced by event_class after the events have been restructured into tiers
        """
        Represents a shaming event.

        `counter` (int): The number of times this event has been completed.
        `points` (int): The number of times that count as progress.
        """
        def __init__(self, **kwargs):
            self.title = ""
            self.tier = 0
            self.start_label = ""
            self.complete_label = ""
            self.counter = 0
            self.points = 0
            self.hint = False
            self.inProgress = False

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
