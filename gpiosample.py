from gpiozero import Button
from gpiozero import LED
import time

def lightLED():
    button = Button(13)
    led = LED(19)

    oldStatus = False

    try:
        while True:
            newStatus = button.is_pressed
            if oldStatus != newStatus:
                oldStatus = newStatus
                if newStatus:
                    print('pressed')
                    led.on()
                else:
                    print('released')
                    led.off()

    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        print("\nexit program")

def blinkLED():
    button = Button(13)
    led = LED(19)

    swStatus = False

    ledPhase = True
    try:
        time_sta = time.perf_counter()

        while True:
            time_now = time.perf_counter()
            if time_now - time_sta >= 0.5:
                time_sta = time_now
                ledPhase = False if ledPhase else True
            
            ledLight = ledPhase
            
            newStatus = button.is_pressed
            if swStatus != newStatus:
                swStatus = newStatus
                if newStatus:
                    print('pressed')
                else:
                    print('released')

            if swStatus:
                ledLight = True
                
            if ledLight:
                led.on()
            else:                    
                led.off()
    
    except KeyboardInterrupt  :         #Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        print("\nexit program")


lightLED()
#blinkLED()


