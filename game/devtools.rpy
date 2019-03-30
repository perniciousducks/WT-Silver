init python:
    rpy_version = int('%d%d%d%d' % renpy.version_tuple)
    
    if rpy_version >= 720000:
        pass
    else:
        raise Exception("Your Ren'Py launcher is outdated, the current minimal requirement is 7.2.0+\nPlease perform an update or use official game executable instead.")