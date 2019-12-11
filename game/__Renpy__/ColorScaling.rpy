init python:
    import threading
        
    whitespace_dict = {}
    with renpy.file(".whitespace") as fp:
        line = fp.readline()
        while line:
            path, area = line.strip("\r\n").split(':')
            whitespace_dict[path] = map(int, area.split(','))
            line = fp.readline()
            
    def start_image_crop():
        # Start loop in worker thread
        threading.Thread(target=image_crop_loop).start()

    def image_crop_loop():
        for cloth in character_clothes_list:
            # Call to ensure whitespace is calculated
            crop_whitespace(cloth.sprite_ico.path)
                
    def crop_whitespace(path):
        # Return box from whitespace_dict, or calculate and store it
        if path in whitespace_dict:
            box = whitespace_dict[path]
        else:
            surf = Image(path).load()
            box = surf.get_bounding_rect() # Does not return a list/tuple but an object!
            box = tuple(x for x in box)
            whitespace_dict[path] = box
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
            self.path = images[image_index]
            self.layers = layers
            self.cached = False
            self.sprite = None

        def get_matrixcolor(self, layer):
            return im.matrix.tint(float(self.color[layer][0])/255.0, float(self.color[layer][1])/255.0, float(self.color[layer][2])/255.0)
            
        def get_imagelayer_color(self, layer):
            return im.MatrixColor(self.images[layer], self.get_matrixcolor(layer))

        def get_image(self):
            if not self.cached:
                box = crop_whitespace(self.path) # Get or calculate image area
                
                self.cached = True
                sprite = Composite((1010, 1200), (0,0), self.get_imagelayer_color(0))
                
                if len(self.images) > 0:
                    for i in xrange(0, len(self.images)):
                        if i < self.layers: # Colored layers
                            sprite = Composite((1010, 1200), (0,0), sprite, (0,0), self.get_imagelayer_color(i))
                        else: # Additional non-colored layers
                            if self.images[i]:
                                sprite = Composite((1010, 1200), (0,0), sprite, (0,0), self.images[i])
                sprite = Crop(box, sprite)
                self.sprite = sprite
            return self.sprite