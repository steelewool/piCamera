import time
import picamera
with picamera.PiCamera() as camera:

    camera.start_preview()

    print 'framerate     : ', camera.framerate
    print 'shutter speed : ', camera.shutter_speed
    print 'iso           : ', camera.iso
    print 'exposure_mode : ', camera.exposure_mode
    print 'resolution    : ', camera.resolution
    print 'sensor_mode   : ', camera.sensor_mode


# worked for jpg will change to png

    try:
        for i, filename in enumerate(
                camera.capture_continuous('image{counter:02d}.jpg')):
            print(filename)
            # time.sleep(1)
            if i == 9:  # was 59 
                break
    finally:
        camera.stop_preview()


# may not be necessary: camera.close()
