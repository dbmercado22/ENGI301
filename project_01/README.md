# GuitarHero Project

All the code needed to run this project can be found in the GuitarHero folder. The code should be downloaded and implemented in the Cloud9 interface. All the hardware components and set up can be found on the Hackster.io page:
https://www.hackster.io/dbm5/engi-301-guitarhero-2c720b

# Setup Steps
1. Wire components as per the instructions on the Hackster.io page
2. Connect PocketBeagle to the internet
3. Download python by entering the following lines
  - sudo apt-get install python3-pip
  - sudo pip3 install --upgrade Pillow
  - sudo pip3 install adafruit-circuitpython-busdevice
  - sudo pip3 install adafruit-circuitpython-rgb-display
  - sudo apt-get install ttf-dejavu -y
  - sudo apt-get install python3-numpy

Run GuitarHero.py

# Code

The main files containing all code necessary for the project are the following:
   - GuitarHero.py: Runs the program by calling all other code necessary to use all components. It imports needed libraries and defines functions necessary for the project to run.
   - Potentiometer.py: Code that enables the potentiometer to function and return values
   - threaded_button.py: Code that enables the button component to function at all times while the main script is running. Serves to select various options throughout the main script
   - threaded_led.py: Code that enables the LED component to function at all times while the main script is running. Serves as the metronome for the project.
   - spi_screen.py: Code that enables the SPI screen to function. Currently not functional (an area of improvement) but is intended to display images of guitar chords along with text for the tempo and chord selections.


