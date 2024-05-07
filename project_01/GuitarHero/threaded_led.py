import time
import threading
import Adafruit_BBIO.GPIO as GPIO

HIGH          = GPIO.HIGH
LOW           = GPIO.LOW

class ThreadingLED(threading.Thread):
    
    pin                 = None
    sleep_time          = None
    led_on_time         = None
    
    
    def __init__(self, pin=None, sleep_time=0.1):
        
        threading.Thread.__init__(self)
        
        if (pin == None):
            raise ValueError("Pin not provided for LED()")
        else:
            self.pin = pin
        
        if low_off:
            self.on_value  = HIGH
            self.off_value = LOW
        else:
            self.on_value  = LOW
            self.off_value = HIGH
            
            
        self.sleep_time = sleep_time
        self.stop_led = False
        
        self._setup()
        
        
    def _setup(self):
        GPIO.setup(self.pin, GPIO.OUT)
        self.off()
        
        pass

        self.off()
        
        
    def is_on(self):
        """ Is the LED on?
        
           Returns:  True  - LED is ON
                     False - LED is OFF
        """
        
        # !!! NEED TO IMPLEMENT !!! #
        return GPIO.input(self.pin) == self.on_value
        
    def run(self, led_on_time):
        
        while(self.stop_led):
            
            self.on()
            time.sleep(led_on_time)
            self.off()
            time.sleep(led_on_time)
            
            if self.stop_led:
                break
            
    def on(self):
        """ Turn the LED ON """
        GPIO.output(self.pin, self.on_value)

        # !!! NEED TO IMPLEMENT !!
        # !!! NEED TO IMPLEMENT !!! #
    
    # End def
    
    
    def off(self):
        """ Turn the LED OFF """
        GPIO.output(self.pin, self.off_value)
        # !!! NEED TO IMPLEMENT !!! #
        print("Turning LED OFF")
        # !!! NEED TO IMPLEMENT !!! #
    
    # End def


    def cleanup(self):
        """ Cleanup the hardware components. """
        # Turn LED off 
        self.off()
        
    # End def

# End class

