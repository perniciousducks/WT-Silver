label __init_variables:
    # custom made outfit for events 
    if not hasattr(renpy.store,'hg_standart_school_OBJ'): #important!
        $ hg_standart_school_OBJ = hermione_outfit()
    $ hg_standart_school_OBJ.name = "Standart School"
    $ hg_standart_school_OBJ.type = "outfit"
    $ hg_standart_school_OBJ.items = ["outfit"]
    $ hg_standart_school_OBJ.outfit_layers = ["../uniform/skirt_2.png", "../uniform/top_1.png"]
    $ hg_standart_school_OBJ.breast_layer = "breasts_nipfix"
    
    if not hasattr(renpy.store,'hg_standart_school_noshirt_OBJ'): #important!
        $ hg_standart_school_noshirt_OBJ = hermione_outfit()
    $ hg_standart_school_noshirt_OBJ.name = "Standart School"
    $ hg_standart_school_noshirt_OBJ.type = "outfit"
    $ hg_standart_school_noshirt_OBJ.items = ["outfit"]
    $ hg_standart_school_noshirt_OBJ.outfit_layers = ["../uniform/skirt_2.png", "../underwear/base/bra_base.png"]
    $ hg_standart_school_noshirt_OBJ.breast_layer = "breasts_nipfix"