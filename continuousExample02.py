y
from picamera import PiCamera
from time import sleep
from fractions import Fraction

print "continuousExample02.py -merging feature from captureImages.py"

# Force sensor mode 4 (the long exposure mode), set
# the framerate to 1/6fps, the shutter speed to 6s,

camera = PiCamera(
#    resolution=(1280, 720),
    resolution=(1640, 1232),
# worked by 1/10 hertz    framerate=Fraction(1, 10),
    framerate=Fraction(1, 2 ),
    sensor_mode=4)

print 'framerate: ', camera.framerate

# Mode 4 for the V2 will do a 2x2 binning, a resolution of 1640x1233,
#        support framerates of 1/10 to 15 frames per seconds,
#        and uses the entire frame.

# worked but overexposed during the day: camera.shutter_speed = 5000000
camera.shutter_speed = 100000

# worked but overexposed during the day: camera.iso = 800
camera.iso = 100
# Give the camera a good long time to set gains and
# measure AWB (you may wish to use fixed AWB instead)
#
camera.exposure_mode = 'off'

print 'shutter speed: ', camera.shutter_speed
print 'iso          : ', camera.iso

# worked but will try a smaller number: sleep(30)
print 'sleep 10 seconds'
sleep(10)

try:
    print 'Enter loop:'
    for i, filename in enumerate(
            camera.capture_continuous('image{counter:02d}.jpg')):
        print(filename)
        if i == 4:
            break
finally:
    print 'Close camera'
    camera.close()
