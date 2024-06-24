import sensor
import display
import time
from random import randint

sensor.reset()  # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565)  # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QQVGA2)  # Special 128x160 framesize for LCD Shield.
lcd = display.SPIDisplay()
clock = time.clock()

while True:
    clock.tick()

    img = sensor.snapshot()

    for i in range(10):
        x = randint(0, 2 * img.width()) - img.width() // 2
        y = randint(0, 2 * img.height()) - img.height() // 2
        w = randint(0, img.width() // 2)
        h = randint(0, img.height() // 2)

        r = randint(0, 127) + 128
        g = randint(0, 127) + 128
        b = randint(0, 127) + 128

        img.draw_rectangle(x, y, w, h, color=(r, g, b), thickness=2, fill=False)

    lcd.write(img)
    print(clock.fps())
