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
    - SPI Display
    - Potentiometer
    
"""
import time
import random
import threaded_button as BUTTON
import potentiometer as POT
import threaded_led as LED
import spi_screen as SPI


class GuitarHero():
    
    music_list = ["Major Chords", "Minor Chords", "Diminished Chords", "Augmented Chords"]
    chosen_song = None
    chosen_tempo = None
    
    
    def __init__(self, reset_time=3.0, button="P2_2", potentiometer="P1_19"):
        
        self.reset_time     = reset_time
        self.metronome_led  = LED.LED("P2_4")
        self.potentiometer  = POT.Potentiometer(potentiometer)
        self.button         = BUTTON.Button(button)
        self.display        = SPI.SPI_Display()
        
        self.music_list     = music_list
        
        
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
        length_of_music = len(music_list)          #this is the list of music
        potentiometer_range = 4095

        value = self.potentiometer.get_value
        
        for i in range(length_of_music):
            low_range = (potentiometer_range/length_of_music) * i
            high_range = (potentiometer_range / length_of_music) * (i+1)
            print("Low = {0}  High = {1}".format(low_range, high_range))
            song_ranges.append((low_range, high_range))

        while chosen_song == None:
            for song in song_ranges:
                if value > song(0) and value < song(1):
                    current_song_index = song_ranges.index(song)
                    current_song = music_list(current_song_index)
                    self.display.text(current_song)
        return current_song
        
        

    def select_song(self):
        """
        Uses button input to confirm the song you will be playing
            - Takes song you are "hovering" over (song that corresponds to the potentiometer's value)
            - Press button to confirm you will be playing this song
            
        Returns the selected song
        """
        current_song = self.song_scrolling()
        if self.button.is_pressed():
            chosen_song = current_song
            self.display.blank()
            return chosen_song

        
    def tempo(self):
        """
        Returns the tempo selected using the value of the potentiometer
            - Manipulate the potentiometer to select a tempo reflected on the value it displays
            - Sets the music's tempo to the value of the potentiometer
            
        """
        # max value in potentiometer is 4095
        # max tempo possible is 204.8
        music_tempo = (self.potentiometer.get_value() / 20)
        print(music_tempo)
        self.display.text(str(music_tempo))
        if self.button.is_pressed():
            chosen_tempo = music_tempo
        return chosen_tempo
        
    def led_metronome(self):
        """
        Sets the tempo of the flashing LED that acts as the metronome
            - First determines number of flashes necessary per second using tempo()
            - Determines time for LED to be on and LED to be off while meeting requirements
            - Toggles LED off and on using sleep_time
            
        """
        timeperflash = 60 / tempo()      #time each flash takes within one minute
        led_on_time = timeperflash / 2   #time needed for LED to flash on and off (should be equal)
        
        self.metronome_led.run(led_on_time)
        
    def display_tabs(self):
        
        major_chords = ["tab_one", "tab_two"]
        minor_chords = ["tab_three", "tab_four"]
        diminished_chords = ["tab_five", "tab_six"]
        augmented_chords = ["tab_seven", "tab_eight"]
        
        chosen_chords = None
        
        if (self.select_song() == "Major Chords"):
            chosen_chords = major_chords
        elif (self.select_song() == "Minor Chords"):
            chosen_chords = minor_chords
        elif (self.select_song() == "Diminished Chords"):
            chosen_chords = diminished_chords
        elif (self.select_song() == "Augmented Chords"):
            chosen_chords = augmented_chords
            
        current_tab = random.choice(chosen_chords)
        
        self.display.image(current_tab)
        
        
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
        """
        Runs the program
        """
        
        while chosen_song == None:
            
            # Start by scrolling through songs + display on screen
            self.song_scrolling(music_list)
        
            # Confirmed selection of song 
            self.select_song()
        
        # Select tempo
        while chosen_tempo == None:
            self.tempo()
        
        # Have LED blink at selected tempo
        self.led_metronome()
        
        # Run the song
        t_end = time.time() + 60
        while time.time() < t_end:
            self.display_tabs()
            time.sleep(120 / self.tempo())
            
        self.display.blank()
        time.sleep(2)
        
        
        
# Main Script

if __name__ == '__main__':
    
    print("Program Start")
    
    guitar_hero = GuitarHero()
    
    guitar_hero.run()
    
        
    
    
    