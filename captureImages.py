from picamera import PiCamera
from time import sleep
from fractions import Fraction

# Force sensor mode 4 (the long exposure mode), set
# the framerate to 1/6fps, the shutter speed to 6s,

print 'Defaulting to 1640x1232 resolution'
print '              1/10 hertz frame rate'
print '              sensor_mode is 4'

camera = PiCamera(
    resolution=(1640, 1232),
    framerate=Fraction(1, 10),
    sensor_mode=4)

# Mode 4 for the V2 will do a 2x2 binning, a resolution of 1640x1233,
#        support framerates of 1/10 to 15 frames per seconds,
#        and uses the entire frame.

print 'Framerate : ', camera.framerate

print 'Enter shutter speed 0.000001 to 10 seconds)'
camera.shutter_speed = int(input('Shutter speed (seconds): ') * 1000000)

                           
# worked but overexposed during the day: camera.shutter_speed = 5000000
# camera.shutter_speed = 100000

# worked but overexposed during the day: camera.iso = 800

print 'Enter ISO, 100, 200, 300, ..., 800'

camera.iso = input('ISO: ')

numberOfImages = input('Enter number of images to grab : ')

# Give the camera a good long time to set gains and
# measure AWB (you may wish to use fixed AWB instead)
#
camera.exposure_mode = 'off'

print 'shutter speed: ', camera.shutter_speed / 1000000.0
print 'iso          : ', camera.iso

# worked but will try a smaller number: sleep(30)
print 'sleep 10 seconds'
sleep(10)

# Finally, capture an image with a 6s exposure. Due
# to mode switching on the still port, this will take
# longer than 6 seconds
print 'capture image'

#camera.capture('dark.png')

#print 'close camera'

#camera.close()

try:
    print 'Enter loop:'
    for i, filename in enumerate(
            camera.capture_continuous('image{counter:02d}.jpg')):
        print(filename)
        if i == numberOfImages-1:
            break
finally:
    print 'Close camera'
    camera.close()

