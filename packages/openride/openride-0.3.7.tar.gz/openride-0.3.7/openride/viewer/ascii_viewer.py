from openride import Viewer
from typing import Tuple

import numpy as np
import cv2
import curses


def image_to_ascii_art(img: np.ndarray, resolution: Tuple[int, int]) -> str:
    """Convert an Image to ASCII Art"""

    pixels_rgb = cv2.resize(img, resolution)
    pixels = np.mean(pixels_rgb, axis=-1).astype(int)

    # chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    chars = [".", ":", "!", "*", "?", "%", "S", "&", "$", "#", "@"]
    new_pixels = [chars[pixel // 25] for pixel in np.ravel(pixels)]
    new_pixels = "".join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index : index + resolution[0]] for index in range(0, new_pixels_count, resolution[0])]
    ascii_image = "\n".join(ascii_image)

    return ascii_image



class AsciiViewer(Viewer):
    def __init__(self):
        super().__init__(background=(0, 0, 0), mouse_camera_interactions=False, render_offscreen=True)
        self.screen = curses.initscr()
            
    def update(self):
        width  = self.screen.getmaxyx()[1]
        height = self.screen.getmaxyx()[0]
        resolution = (width-2, height-2)

        rendered_image = super().update(return_image=True)
        ascii_image = image_to_ascii_art(rendered_image, resolution)

        for y, line in enumerate(ascii_image.splitlines()):
            for x, char in enumerate(line):
                self.screen.addstr(y, x, char)
        self.screen.refresh()

    def close(self):
        curses.endwin()

    def __del__(self):
        self.close()
