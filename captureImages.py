from time import sleep
from fractions import Fraction
import picamera
with picamera.PiCamera() as camera:

    # Looks like this does the open included in the logic:
    
    camera.start_preview()
    camera.exposure_mode = 'off'

    # Print basic information:
    
    print 'framerate     : ', camera.framerate
    print 'shutter speed : ', camera.shutter_speed
    print 'iso           : ', camera.iso
    print 'exposure_mode : ', camera.exposure_mode
    print 'resolution    : ', camera.resolution
    print 'sensor_mode   : ', camera.sensor_mode

# Force sensor mode 4 (the long exposure mode), set
# the framerate to 1/6fps, the shutter speed to 6s,

#    print 'Defaulting to 1640x1232 resolution'
#    print '              1/10 hertz frame rate'
#    print '              sensor_mode is 4'

#    camera = PiCamera(
#        resolution=(1640, 1232),
#        framerate=Fraction(1, 4),
#        sensor_mode=4)

# Changing resolution to 1640x1232 for telescope

    print 'Enter shutter speed 0.000001 to 2.0 seconds)'
    shutterSpeedSeconds  = input('Shutter speed (seconds) : ')
    
    camera.shutter_speed = int(shutterSpeedSeconds * 1000000)

    print 'Enter ISO, 100, 200, 300, ..., 800'
    camera.iso = input('ISO: ')

    numberOfImages = input('Enter number of images to grab : ')
    
    camera.resolution  = (1640,1232)
    camera.sensor_mode = 4

    # Set framerate based on the shutter speed.

    newFrameRate = 2.0 * shutterSpeedSeconds
    print 'newFrameRate: ', newFrameRate
    
    if newFrameRate < 0.250:
        camera.framerate = Fraction(2,1)
    elif newFrameRate < 0.500:
        camera.framerate = Fraction(1,1)
    elif newFrameRate < 1.0:
        camera.framerate = Fraction(1,2)
    elif newFrameRate < 2.5:
        camera.framerate = Fraction(1,5)
    elif newFrameRate < 5.0:
        camera.framerate = Fraction(1,10)

    print 'Wait 20 seconds to reset camera.'
    sleep(20)
    
# Mode 4 for the V2 will do a 2x2 binning, a resolution of 1640x1233,
#        support framerates of 1/10 to 15 frames per seconds,
#        and uses the entire frame.

                           
# Give the camera a good long time to set gains and
# measure AWB (you may wish to use fixed AWB instead)
#

    print 'framerate           : ', camera.framerate
    print 'framerate           : ', float(camera.framerate)
    print 'shutterSpeedSeconds : ', shutterSpeedSeconds
    print 'shutter speed       : ', camera.shutter_speed/1000000.0
    print 'iso                 : ', camera.iso
    print 'exposure_mode       : ', camera.exposure_mode
    print 'resolution          : ', camera.resolution
    print 'sensor_mode         : ', camera.sensor_mode

# worked but will try a smaller number: sleep(30)
#    print 'sleep 10 seconds'
#    sleep(10)

# Finally, capture an image with a 6s exposure. Due
# to mode switching on the still port, this will take
# longer than 6 seconds


    try:
        print 'Enter loop:'
        for i, filename in enumerate(
                camera.capture_continuous('image{counter:02d}.png')):
            print(filename)
            if i == numberOfImages-1:
                break
    except:
        print 'except section hit'
        print 'call stop_preview'
        camera.stop_preview()
    finally:
        print 'finally section hit'
        print 'call stop_preview'
        camera.stop_preview()
        # print 'Close camera'
        # camera.close()

