init python hide:v
    if not config.developer:
        config.missing_image_callback = missing_image_func
        #config.missing_label_callback = missing_label_func

init -2 python:
    rpy_version = int('%d%d%d%d' % renpy.version_tuple)
    
    if rpy_version >= 720000:
        pass
    else:
        raise Exception("Your Ren'Py launcher is outdated, the current minimal requirement is 7.2.0+\nPlease perform an update or use official game executable instead.")
        
    def missing_image_func(path):
        return im.Image("blank.png")
        
    def missing_label_func(name):
        return main_room