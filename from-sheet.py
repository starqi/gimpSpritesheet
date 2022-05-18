#!/usr/bin/env python

from gimpfu import *

def from_sheet(image, numSpritesHorizontal, numSpritesVertical, firstImageIsFirstLayer):
    layer = image.layers[0]
    frameWidth = int(layer.width / numSpritesHorizontal)
    frameHeight = int(layer.height / numSpritesVertical)

    pdb.gimp_undo_push_group_start(image)

    vRange = range(int(numSpritesVertical))
    hRange = range(int(numSpritesHorizontal))

    if firstImageIsFirstLayer:
        vRange = reversed(vRange)
        hRange = reversed(hRange)

    for j in vRange:
        for i in hRange:
            d = layer.copy()
            image.add_layer(d,0)
            d.resize(frameWidth,frameHeight,i * -frameWidth,j * -frameHeight)
            d.translate(i * -frameWidth,j * -frameHeight)

    image.resize(frameWidth,frameHeight,0,0)
    image.remove_layer(layer)

    pdb.gimp_undo_push_group_end(image)


register("python-fu-from-sheet",
         "turns a sprite sheet into a bunch of layers",
         "yee",
         "daly","daly","2018",
         "Sheet to Layers",
         "RGB*",
         [
            (PF_IMAGE, "image", "Input image", None),
            (PF_SPINNER, "numSpritesHorizontal", "Number of sprites horizontally", 1, (1,100,1)),
            (PF_SPINNER, "numSpritesVertical", "Number of sprites vertically", 1, (1,100,1)),
            (PF_BOOL, "firstImageIsFirstLayer", "First image (top-left) is first layer", False)
         ],
         [],
         from_sheet,
         menu="<Image>/Filters/Sheet")

main()
