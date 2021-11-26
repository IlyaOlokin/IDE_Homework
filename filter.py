import doctest

from PIL import Image
import numpy as np


def convert_image_to_mosaic():
    """
    Конвертирует изображение в чернобелый цвет и укрупняет писксели
    :return: чернобелое пиксельное изображение
    """
    image_file = Image.open(input())
    block_size = int(input())
    gradations_count = int(input())
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    for x in range(0, len(image), block_size):
        for y in range(0, len(image[0]), block_size):
            image[x:x + block_size, y:y + block_size] = get_average_brightness(
                image[x:x + block_size, y:y + block_size], block_size, gradation_step)
    return image


def get_average_brightness(block, size, gradation_step):
    """
    Расчитывает среднюю яркость пикселей
    :param block: двумерный массив пикселей размером (size, size)
    :param size: сторона массива пикселей
    :param gradation_step: шаг яркости пикселя
    :return: средняя яркость пикселей в block

    >>> get_average_brightness(np.array([[[0]*3]*2]*2), 2, 255 // 50)
    0
    >>> get_average_brightness(np.array([[[50]*3]*2]*2), 2, 255 // 50)
    50
    >>> get_average_brightness(np.array([[[4]*3]*2]*2), 2, 255 // 50)
    0
    >>> get_average_brightness(np.array([[[5]*3]*2]*2), 2, 255 // 50)
    5
    >>> get_average_brightness(np.array([[[6]*3]*2]*2), 2, 255 // 50)
    5
    >>> get_average_brightness(np.array([[[64]*3]*10]*10), 10, 255 // 255)
    64
    >>> get_average_brightness(np.array([[[25]*3]*10]*10), 10, 255 // 10)
    25
    >>> get_average_brightness(np.array([[[25]*3]*10]*10), 10, 255 // 1)
    0
    """
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


if __name__ == '__main__':
    doctest.testmod()
    res = Image.fromarray(convert_image_to_mosaic())
    res.save(input())
