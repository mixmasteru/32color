"""

"""
from PIL import Image
import math


class ImgTo7Color:
    WIDTH = 600
    HEIGHT = 448

    def __init__(self):
        self.ratio = self.HEIGHT / self.WIDTH
        self.palette = [0, 0, 0, 255, 255, 255, 255, 128, 28, 0, 0, 255, 0, 255, 0, 255, 255, 0, 255, 0, 0]
        self.palimage = Image.new('P', (49, 49))
        self.palimage.putpalette(self.palette * 32)

    def crop_y(self, image):
        w, h = image.size
        new_h = math.floor(h * self.ratio)
        y = math.floor((h - new_h) / 2)
        area = (0, y, w, h - y)

        return image.crop(area)

    def crop_x(self, image):
        w, h = image.size
        img_ratio = h / w
        crop_factor = img_ratio / self.ratio
        new_h = math.floor(w * crop_factor)
        x = math.floor((w - new_h) / 2)
        area = (x, 0, w - x, h)

        return image.crop(area)

    def resize(self, image):
        return image.resize((self.WIDTH, self.HEIGHT), Image.ANTIALIAS)

    def quantizetopalette(self, image, dither=False):
        """Convert an RGB or L mode image to use a given P image's palette.
           from https://stackoverflow.com/questions/29433243/convert-image-to-specific-palette-using-pil-without-dithering/29438149
        """

        image.load()

        # use palette from reference image
        self.palimage.load()
        if self.palimage.mode != "P":
            raise ValueError("bad mode for palette image")
        if image.mode != "RGB" and image.mode != "L":
            raise ValueError(
                "only RGB or L mode images can be quantized to a palette"
            )
        im = image.im.convert("P", 1 if dither else 0, self.palimage.im)
        # the 0 above means turn OFF dithering

        # Later versions of Pillow (4.x) rename _makeself to _new
        try:
            return image._new(im)
        except AttributeError:
            return image._makeself(im)

    def convert_img(self, image, dither=True):
        image = self.crop_x(image)
        image = self.resize(image)
        image = self.quantizetopalette(image, dither)
        return image

    def convert(self, image_path, dither=True):
        image = Image.open(image_path).convert("RGB")
        return self.convert_img(image, dither)
