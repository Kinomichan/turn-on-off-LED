#!/usr/bin/env python3

import time, random, colorsys
import board
import neopixel

def main():
    pixelPin = board.D18
    numPixels = 10
    pixelBrightness = 0.05
    colorOrder = neopixel.RGB # RGB
    colorRed = 0.38 # Hue value showing Red in (hue, 1.0, 1.0)

    pixels = neopixel.NeoPixel(
        pixelPin, numPixels, brightness=pixelBrightness, auto_write=False, pixel_order=colorOrder
    )

    # Initializing pixel Color List (Green to Red)
    pixelColorList = initColorList(colorRed, numPixels)

    while True:
        for i in range(1,11):
            turnOnLed(pixels, pixelColorList, i)
            time.sleep(0.1)

        turnOffLed(pixels)


def initColorList(colorRed, numPixels):
    pixelColorList = []

    for i in range(numPixels):
        # hue: 0.00 ~ pixelRed (starting from green to red)
        hue = colorRed * (i / numPixels)
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        pixelColorList.append([int(r*255), int(g*255), int(b*255)])

    return pixelColorList


def turnOnLed(pixels, pixelColorList, number):
    try:
        for i in range(number):
            pixels[i] = pixelColorList[i]
            pixels.show()
    except KeyboardInterrupt:
        turnOffLed(pixels)
    except Exception as e:
        turnOffLed(pixels)


def turnOffLed(pixels):
    pixels.fill((0, 0, 0)) # turn off all LEDs
    pixels.show()


if __name__ == "__main__":
    main()