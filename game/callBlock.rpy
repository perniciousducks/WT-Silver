init python:
    def init_variables():
        initvarlabels = [label for label in renpy.get_all_labels() if label.endswith('__init_variables') ]
        for l in initvarlabels:
            renpy.call_in_new_context(l) 