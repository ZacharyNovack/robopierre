# RoboPierre - French Impressionistic MIDI Generation and Intelligent Voice Leading

http://robopierre.glitch.me

RoboPierre is an online sonic art piece created by Joseph Sandler and Zachary Novack, and was premiered in collaboration with Carnegie Mellon University's Exploded Ensemble for their Spring 2020 production *Art at the End of the World*. This code repository includes:
* The Recurrent Neural Network (RNN) that produced the MIDI files for the installation (made using Google Magenta's Polyphony RNN trained on a corpus of French Impressionist works)
* The python script that utilizes the music21 Computational Musicology module to create long strings of midi files that are connected through traditional harmonic progressions
* The javascript code used to build the web installation

## Required Modules
* Magenta
* music21

## Using the Code
Once the bundled model (.mag) and midiGeneration folder are downloaded, the following must be done to produce your own MIDI files from RoboPierre:
1. Go into seed.py and change the path variables defined to match your local file system
2. Run seed.py from the command line with the additional argument of **x** many midi files to write (**x** >= 1)

This will produce **x** midi files in whatever folder you specified as the output, which can then be easily copied and pasted into any traditional Digital Audio Workstation (DAW) like Logic Pro or Ableton Live.
