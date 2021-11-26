from PIL import Image
import numpy as np


def convert_image_to_mosaic():
    image_file = Image.open(input())
    block_size = int(input())
    gradations_count = int(input())
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    for x in range(0, len(image), block_size):
        for y in range(0, len(image[0]), block_size):
            image[x:x + block_size, y:y + block_size] = get_average_brightness(
                image[x:x + block_size, y:y + block_size], block_size, gradation_step)

    res = Image.fromarray(image)
    res.save(input())


def get_average_brightness(block, size, gradation_step):
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


convert_image_to_mosaic()