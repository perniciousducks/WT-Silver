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
        for cloth in hermione.wardrobe_list:
            # Call to ensure whitespace is calculated
            crop_whitespace(cloth.ico.bounds)
                
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

    class CroppedImage(object):
        size = (1010, 1200)
        
        def __init__(self, sprites, bounds):
            self.sprites = sprites
            self.bounds = bounds
            self.cached = False
            self.sprite = None
            
        def get_image(self):
            if not self.cached:
                self.cached = True
                box = crop_whitespace(self.bounds)
                self.sprite = Crop(box, Composite(self.size, *self.sprites))
            return self.sprite
            
    config.after_load_callbacks.append(start_image_crop)