label __init_variables:
    #Check if you have visit room of req before
    if not hasattr(renpy.store,'first_visit_req'): #important!
        $ first_visit_req = False