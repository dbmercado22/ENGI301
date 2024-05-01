"""
--------------------------------------------------------------------------
GuitarHero
--------------------------------------------------------------------------
License:   
Copyright 2024 Brian Mercado

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
Using the following component to build an LED array guitar chord exercise device
    - button
    - green LED
    - LED array 16x32
    - Potentiometer
    
"""

import threaded_button as BUTTON
import "pdf to music code"
import potentiometer as POT
import led as LED
import "code for LED array for guitar tabs"


class GuitarHero():
    
    music_list = None
    
    def __init__(self, reset_time=3.0, button="P2_2", potentiometer="P1_19"):
        
        self.reset_time     = reset_time
        self.metronome_led  = LED.LED("P2_4")
        self.potentiometer  = POT.Potentiometer(potentiometer)
        self.button         = BUTTON.Button(button)
        
        self.music_list     = ["one", "two"]
        
        
    def _setup(self):
        #setup instances of each code imported
        self.set_display_dash()
        
    def song_scrolling(self, music_list):
        """
        Scroll through all possible songs
            - music_list - the list of all songs downloaded
            
            - Use potentiometer to scroll through all songs
            - Divide each song to a range of values accessible by the potentiometer
            
        Returns the song the potentiometer's value is within its range
        """
        current_song_index = 0
        length_of_music = len(music_list):          #this is the list of music
        potentiometer_range = 4095

        value = self.potentiometer.get_value
        
        for i in range(length_of_music):
            low_range = (potentiometer_range/length_of_music) * i
            high_range = (potentiometer_range / length_of_music) * (i+1)
            print("Low = {0}  High = {1}".format(low_range, high_range))
            song_ranges.append((low_range, high_range))

        while select_song(self) == None:
            for song in song_ranges:
                if value > song(0) and value < song(1):
                    current_song_index = song_ranges.index(song)

        return current_song = music_list(current_song_index)

    def pdf_to_music(self):
        pass
        
    def select_song(self):
        """
        Uses button input to confirm the song you will be playing
            - Takes song you are "hovering" over (song that corresponds to the potentiometer's value)
            - Press button to confirm you will be playing this song
            
        Returns the selected song
        """
        current_song = self.song_scrolling()
        if self.button.is_pressed():
            return confirmed_song = current_song

        
    def tempo(self):
        """
        Returns the tempo selected using the value of the potentiometer
            - Manipulate the potentiometer to select a tempo reflected on the value it displays
            - Sets the music's tempo to the value of the potentiometer
            
        """
        # max value in potentiometer is 4095
        # max tempo possible is 204.8
        music_tempo = (self.potentiometer.get_value() / 20)
        return music_tempo
        
    def led_metronome(self):
        """
        Sets the tempo of the flashing LED that acts as the metronome
            - First determines number of flashes necessary per second using tempo()
            - Determines time for LED to be on and LED to be off while meeting requirements
            - Toggles LED off and on using sleep_time
            
        """
        while end_song == False:
            num_flashes = tempo() / 60      #number of flashes metronome must take per second
            led_on_time = num_flashes / 2   #time needed for LED to flash on and off (should be equal)
            self.metronome_led.on()
            self.sleep_time(led_on_time)
            self.metronome_led.off()
            self.sleep_time(led_on_time)
            if self.pause_song() == True:
                self.sleep_time(100)
    
    def display_tabs(self):
        pass
    
    def pause_song(self):
        """
        Pauses song using the press of a button. Pauses the metronome and the leds displayed on the array.
            - When button is pressed, it sets the system to sleep for 100 seconds
        """
        self.button.wait_for_press()
        if (self.button.is_pressed() == True):
            if self.button.get_last_press_duration() < self.reset_time:
                self.sleep_time(100)
            
    def continue_song(self):
        """
        Continues the song after the program is paused.
            - When button is pressed, it resumes the system from where it was paused
        """
        self.button.wait_for_press()
        if self.sleep_time() > 0:
            if (self.button.is_pressed == True):
                if self.button.get_last_press_duration() < self.reset_time:
                    self.sleep_time(0)
    
    def reset_song(self):
        """
        Resets the program to the beginning of the "playing" phase
        """
        self.button.wait_for_press
        if self.button.get_last_press_duration() > 5:
            if self.start_song() != None:
                self.display_tabs()
                
    
    def end_song(self):
        """
        Resets program to the song selection phase
        """
        if self.display_tabs() == None:
            self.metronome_led.off()
            self.display_tabs.off()
            self.select_song() == None
            
    
    def run(self):
        
        self.song_scrolling()
        #self.led_metronome()
        #self.select_song()
        #self.display_tabs()
        
        
# Main Script

if __name__ == '__main__':
    
    print("Program Start")
    
    guitar_hero = GuitarHero(debug=True)
    
    try:
        guitar_hero.run()
    
    
    