# Music of Life

### The Music of Conway's Game of Life 

This is a project inspired by an idea I saw here: https://www.youtube.com/watch?v=x22zysfrVSk

For the audio, we used some code I found here: http://davywybiral.blogspot.com.br/2010/09/procedural-music-with-pyaudio-and-numpy.html

We implemented a simulation of Conway's Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) and then used the simulation to generate music. At each timestep of the simulation we represent all of the living cells in a certain column as musical notes. The notes that are played are determined by which rows the living cells are in. Each row corresponds to a certain note in the Pentatonic Major scale (you could change the scale used by modifying the code). We used the Pentatonic Major scale because it contains no dissonant intervals, meaning any combination of notes sound "nice" together.

## Running the Code

Before you run the code, you need to install two libraries: 

* **pygame** (pygame.org) for the graphics 
* **pyaudio** (https://people.csail.mit.edu/hubert/pyaudio/) for the audio. 


To make sure you have installed these correctly, I recommend opening up python and trying `import pygame` and `import pyaudio`. If these give you no errors, you should be good to go.

Now, you can type `python GameOfLifeGraphics.py` to run the main program.

## Controls

* Spacebar - Pause
* r - Reset game grid (remove all living cells)
* Enter/Return - Randomize game grid
* p - Insert "pulsar" at current mouse location
* g - Insert "glider" at current mouse location
* Left Click (when paused) - Toggle state of cell at current mouse location

## Program Parameters

There are several parameters that can be tweaked in GameOfLifeGraphics.py such as how fast the music plays, the width/height of the game grid, and the colors. 

