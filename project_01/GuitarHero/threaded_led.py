"""
--------------------------------------------------------------------------
Threaded LED Driver
--------------------------------------------------------------------------
License:   
Copyright 2024 - Brian Mercado dbm5@rice.edu

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
"""

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

