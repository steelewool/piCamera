from picamera import PiCamera
from time import sleep
from fractions import Fraction

# Force sensor mode 3 (the long exposure mode), set
# the framerate to 1/6fps, the shutter speed to 6s,
# and ISO to 800 (for maximum gain)
camera = PiCamera(
#    resolution=(1280, 720),
    resolution=(1640, 1232),
    framerate=Fraction(1, 10),
    sensor_mode=4)

# Mode 4 for the V2 will do a 2x2 binning, a resolution of 1640x1233,
#        support framerates of 1/10 to 15 frames per seconds,
#        and uses the entire frame.

# worked but overexposed during the day: camera.shutter_speed = 5000000
camera.shutter_speed = 300000
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

# Finally, capture an image with a 6s exposure. Due
# to mode switching on the still port, this will take
# longer than 6 seconds
print 'capture image'

camera.capture('dark.png')
camera.close()

