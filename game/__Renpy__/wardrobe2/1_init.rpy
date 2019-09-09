# This file should be named "1_init.rpy" to ensure that variables are defined before characters and clothes.
# Hopefully this is a temporary workaround that will be replaced by a cleaner solution.

#TODO Find a way to not rely on `character_list` and `character_clothes_list`
# 1. Can be replaced with: dict([(x.char, x) for x in globals().itervalues() if isinstance(x, char_class)])
# 2. Can be replaced with: [x for x in globals().itervalues() if isinstance(x, cloth_class)]

# Define global object stores for wardrobe
default character_list = {}
default character_clothes_list = []
