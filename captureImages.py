from picamera import PiCamera
from time import sleep
from fractions import Fraction

print 'Running program: captureImages'

camera = PiCamera()

print 'Done with camera constructor'

loopForever = True
while loopForever:

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

    camera.resolution  = (1640, 1232)
    camera.sensor_mode = 4

# Changing resolution to 1640x1232 for telescope

    print 'Enter shutter speed 0.000001 to 10.0 seconds)'
    checkInput = True
    while checkInput:
        shutterSpeedSeconds  = input('Shutter speed (seconds) : ')
        if shutterSpeedSeconds < 0.0000001 or shutterSpeedSeconds > 10.0:
            print 'Out of range, enter a valid shutter time.'
        else:
            checkInput = False
           
# Set framerate based on the shutter speed.

    newFrameRate = 2.0 * shutterSpeedSeconds
    
    if newFrameRate < 0.250:
        camera.framerate = Fraction(2,1)
        print 'framerate           : ', camera.framerate
    elif newFrameRate < 0.500:
        camera.framerate = Fraction(1,1)
        print 'framerate           : ', camera.framerate
    elif newFrameRate < 1.0:
        camera.framerate = Fraction(1,2)
        print 'framerate           : ', camera.framerate
    elif newFrameRate < 2.5:
        camera.framerate = Fraction(1,5)
        print 'framerate           : ', camera.framerate
    else:
        camera.framerate = Fraction(1,10)
        print 'framerate           : ', camera.framerate

    camera.shutter_speed = int(shutterSpeedSeconds * 1000000.0)
    print 'exposure speed       : ', camera.exposure_speed

    print 'Enter ISO, 100, 200, 300, ..., 800'
    camera.iso = input('ISO: ')

    numberOfImages = input('Enter number of images to grab : ')
    
# Mode 4 for the V2 will do a 2x2 binning, a resolution of 1640x1233,
#        support framerates of 1/10 to 15 frames per seconds,
#        and uses the entire frame.

                           
# Give the camera a good long time to set gains and
# measure AWB (you may wish to use fixed AWB instead)

    print 'Sleep 30 seconds per the recommendation from documentation'
    sleep (30)
    
    camera.exposure_mode = 'off'

    print 'framerate           : ', camera.framerate
    print 'shutterSpeedSeconds : ', shutterSpeedSeconds
    print 'shutter speed       : ', camera.exposure_speed
    print 'iso                 : ', camera.iso
    print 'exposure_mode       : ', camera.exposure_mode
    print 'resolution          : ', camera.resolution
    print 'sensor_mode         : ', camera.sensor_mode

    try:
        print 'Enter loop to grab ', numberOfImages, 'images:'
        for i, filename in enumerate(
                camera.capture_continuous(
                    '/home/pi/AstroImages/TestingPiCamera/image-{timestamp:%Y-%m-%d-%H-%M-%S-%f}.png')):
            print(filename)
            if i == numberOfImages-1:
                break
    except:
        print 'except section hit'
        #    print 'call camera.close()'
        #    camera.close()
    finally:
        print 'finally section hit'

    x = input ('Enter 0 to quit, anything else to continue : ')
    if x == 0:
        loopForever = False

    camera.exposure_mode = 'auto'

# camera.close()

print 'end of the program'
