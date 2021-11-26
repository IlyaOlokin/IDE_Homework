from PIL import Image
import numpy as np
import sys


def convert_image_to_mosaic():
    img = Image.open(input())
    cell_size = int(input())
    grayscale = 255 // int(input())

    res = image_to_black_and_white(img, cell_size, grayscale)
    res.save(input())
    return


def get_cell_brightness(arr, cell_x, cell_y, _cell_size):
    brightness_sum = 0
    for current_x in range(cell_x, cell_x + _cell_size):
        for current_y in range(cell_y, cell_y + _cell_size):
            r, g, b = arr[current_x][current_y][:]

            pixel_brightness = r / 3 + g / 3 + b / 3
            brightness_sum += pixel_brightness

    return int(brightness_sum // (_cell_size * _cell_size))


def cell_to_black_and_white(arr, cell_x, cell_y, cell_brightness, _grayscale, _cell_size):
    arr[cell_x: cell_x + _cell_size, cell_y: cell_y + _cell_size][:] = int(cell_brightness // _grayscale) * _grayscale


def image_to_black_and_white(image, _cell_size, _grayscale):
    arr = np.array(image)

    for cell_x in range(0, len(arr), _cell_size):
        for cell_y in range(0, len(arr[0]), _cell_size):
            cell_brightness = get_cell_brightness(arr, cell_x, cell_y, _cell_size)
            cell_to_black_and_white(arr, cell_x, cell_y, cell_brightness, _grayscale, _cell_size)

    return Image.fromarray(arr)


convert_image_to_mosaic()
