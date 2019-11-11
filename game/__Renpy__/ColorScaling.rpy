init python:
    import threading
        
    whitespace_dict = {}
    with renpy.file(".whitespace") as fp:
        line = fp.readline()
        while line:
            whitespace_dict[line.split(':')[0]] = tuple(int(x) for x in line.split(':')[1].split(','))
            line = fp.readline()
            
    def start_image_crop():
        for cloth in character_clothes_list:
            if not cloth.sprite_ico.done:
                cloth.sprite_ico.start_thread()
                break
                
    def check_crop_progress(): # Debug function
        for i, cloth in enumerate(character_clothes_list):
            if not cloth.sprite_ico.done:
                return "Working {}/{}".format(i, len(character_clothes_list))
        return "Done!"

    def crop_whitespace(path, thread=None):
        try:
            box = whitespace_dict[path]
        except KeyError:
            surf = Image(path).load()
            box = surf.get_bounding_rect() # Does not return a list/tuple but an object!
            box = tuple(x for x in box)
            whitespace_dict[path] = box
            
        if thread:
            thread.box = box
            thread.done = True
            start_image_crop()
            return
        return box

    def crop_image_zoom(path, xsize, ysize, grayscale=False):
        box = crop_whitespace(path)

        if float(xsize)/box[2] < float(ysize)/box[3]:
            zoom = float(xsize)/box[2]
        else:
            zoom = float(ysize)/box[3]
            
        if grayscale:
            sprite = Image(im.MatrixColor(path, im.matrix.desaturate()))
        else:
            sprite = Image(path)
        sprite = Crop(box, sprite)

        return (sprite, zoom)

    class lazyload(object):
        def __init__(self, images, color, image_index, layers):
            self.images = images
            self.color = color
            self.image_index = image_index
            self.layers = layers
            self.cached = False
            self.sprite = None

            try:
                self.box = whitespace_dict[images[image_index]]
                self.done = True
            except KeyError:
                self.box = None
                self.done = False

        def start_thread(self):
            # Note: Thread objects cannot be stored. (HIGHEST PROTOCOL pickle error)
            threading.Thread(target=crop_whitespace, args=(self.images[self.image_index], self)).start()

        def get_matrixcolor(self, layer):
            return im.matrix.tint(float(self.color[layer][0])/255.0, float(self.color[layer][1])/255.0, float(self.color[layer][2])/255.0)
            
        def get_imagelayer_color(self, layer):
            return im.MatrixColor(self.images[layer], self.get_matrixcolor(layer))

        def get_image(self):
            if self.done:
                if not self.cached:
                    self.cached = True
                    sprite = Composite((1010, 1200), (0,0), self.get_imagelayer_color(0))
                    
                    if len(self.images) > 0:
                        for i in xrange(0, len(self.images)):
                            if i < self.layers: # Colored layers
                                sprite = Composite((1010, 1200), (0,0), sprite, (0,0), self.get_imagelayer_color(i))
                            else: # Additional non-colored layers
                                sprite = Composite((1010, 1200), (0,0), sprite, (0,0), self.images[i])
                    sprite = Crop(self.box, sprite)
                    self.sprite = sprite
                return self.sprite
            # If for some reason crop calculation isn't finished yet, calculate on the main thread and recursively return the image.
            self.box = crop_whitespace(self.images[self.image_index])
            self.done = True
            return self.get_image()