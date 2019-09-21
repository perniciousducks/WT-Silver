init python:
    whitespace_dict = {}
    with renpy.file("BakedWhiteSpaceInfo.whitespace") as fp:
        line = fp.readline()
        while line:
            whitespace_dict[line.split(':')[0]] = line.split(':')[1].split(',')
            line = fp.readline()

    def crop_blank(images, thread_class, image_index):
        image = Image(images[image_index])
        surf = image.load()
        width, height = (1010,1200)
        minx = width
        maxx = 0
        miny = height
        maxy = 0
        for x in xrange(int(width)):
            for y in xrange(int(height)):
                if(surf.get_at((x,y))[3] > 0):
                    minx = min(minx, x)
                    maxx = max(minx, x)
                    miny = min(miny, y)
                    maxy = max(maxy, y)
        thread_class.width = max(maxx-minx,0)
        thread_class.height = max(maxy-miny,0)
        thread_class.posx = minx
        thread_class.posy = miny
        thread_class.thread_done = True
        start_image_crop()


    def crop_image_zoom(path, xsize, ysize, grayscale=False):
        width = int(whitespace_dict[path][2])
        height = int(whitespace_dict[path][3])
        posx = int(whitespace_dict[path][0])
        posy = int(whitespace_dict[path][1])

        if float(xsize) / width < float(ysize) / height:
            zoom = float(xsize) / width
        else:
            zoom = float(ysize) / height
        if grayscale:
            sprite = Image(im.MatrixColor(path, im.matrix.desaturate()))
        else:
            sprite = Image(path)
        sprite = Composite((width, height), (-posx, -posy), sprite)

        return (sprite, zoom)


    def start_image_crop():
        for cloth in character_clothes_list:
            if not cloth.sprite_ico.thread_done:
                cloth.sprite_ico.start_thread()
                break


    class lazyload():
        def __init__(self, images, colorlist, image_index, layercount):
            self.images = images
            self.colorlist = colorlist
            self.image_index = image_index
            self.layercount = layercount

            self.width = 0
            self.height = 0
            self.posx = 0
            self.posy = 0
            self.cached = False
            self.thread_done = False
            self.new_composite = None

            if images[image_index] in whitespace_dict:
                self.width = int(whitespace_dict[images[image_index]][2])
                self.height = int(whitespace_dict[images[image_index]][3])
                self.posx = int(whitespace_dict[images[image_index]][0])
                self.posy = int(whitespace_dict[images[image_index]][1])
                self.thread_done = True

        def get_matrixcolor(self, layer):
            return im.matrix.tint(float(self.colorlist[layer][0])/255.0, float(self.colorlist[layer][1])/255.0, float(self.colorlist[layer][2])/255.0)

        def start_thread(self):
            threading.Thread(target=crop_blank, args=(self.images, self, self.image_index)).start()

        def get_image(self):
            if self.cached:
                return self.new_composite
            if self.thread_done:
                self.cached = True
                image = Composite((self.width+18, self.height+18), (-self.posx-9,-self.posy-9), im.MatrixColor(self.images[0], self.get_matrixcolor(0)))
                if len(self.images) > 0:
                    for i in xrange(1, self.layercount):
                        image = Composite((self.width+18, self.height+18), (0,0), image, (-self.posx-9,-self.posy-9), im.MatrixColor(self.images[i], self.get_matrixcolor(i)))
                    image = Composite(
                            (self.width+18, self.height+18),
                            (0,0), image,
                            (-self.posx-9,-self.posy-9), self.images[self.layercount],
                            (-self.posx-9,-self.posy-9), self.images[self.layercount+1])
                self.new_composite = image

                return self.new_composite
            raise Exception("Thread not done calculating image area")
            return Image("blank.png")
