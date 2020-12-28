#!/usr/bin/env python3
from python.ImgTo7Color import ImgTo7Color
from PIL import Image
import hitherdither

conv = ImgTo7Color()

org = Image.open('../img/falcon9_full.jpg')
image = conv.crop_x(org)
image = conv.resize(org)
image.save('../img/falcon9_600x448.jpg')

seven_color = conv.quantizetopalette(image, dither=True)
seven_color.show()

palette = hitherdither.palette.Palette(
    [(0, 0, 0), (255, 255, 255), (255, 128, 28), (0, 0, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0)]
)
img_dithered = hitherdither.ordered.bayer.bayer_dithering(
    image, palette, [256 / 4, 256 / 4, 256 / 4], order=8)

img_dithered.show()

# img_dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(image, palette, order=8)
img_dithered = hitherdither.ordered.cluster.cluster_dot_dithering(image, palette, thresholds=64)
img_dithered.show()

img_dithered = hitherdither.diffusion.error_diffusion_dithering(image, palette, method="stucki")
img_dithered.show()
