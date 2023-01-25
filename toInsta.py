from PIL import Image
import glob

def process(ori_path, tart_path, rotate = 0):

    im = Image.open(ori_path)

    print(im.format, im.size, im.mode)

    width = im.size[0]
    height = im.size[1]

    bigger, smaller, start_x, start_y = 0,0,0,0
    if width == height:
        im = im.rotate(rotate)
        im.save(tart_path)
        return
    elif width > height:
        bigger, smaller = width, height
        start_y = int((bigger-smaller)/2)
    else:
        bigger, smaller = height, width
        start_x = int((bigger-smaller)/2)

    new_img = Image.new("RGB", (bigger, bigger), (255,255,255))

    if start_y != 0:
        new_img.paste(im, (0, start_y))
    else:
        new_img.paste(im, (start_x, 0))

    new_img = new_img.rotate(rotate)
    new_img.save(tart_path)

# process("origins/DSCF1294.JPG", "tarts/test.JPG")

allImgs = glob.glob("./origins/*")
for i in allImgs:
    tart = "tarts/" + i[10:]
    process(i, tart, rotate=90)