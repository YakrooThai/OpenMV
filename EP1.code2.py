import sensor, image, time, display

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)

clock = time.clock()

thresholds = [(30, 100, 15, 127, -128, 127)]  

lcd = display.SPIDisplay()
lcd.backlight(95) 
while True:
    clock.tick()
    img = sensor.snapshot()

    blobs = img.find_blobs(thresholds, pixels_threshold=200, area_threshold=200, merge=True)

    if blobs:
        for blob in blobs:
            img.draw_rectangle(blob.rect(), color=(255, 0, 0))  
            img.draw_cross(blob.cx(), blob.cy(), color=(0, 255, 0))  
    
    lcd.write(img)

    print(clock.fps())
