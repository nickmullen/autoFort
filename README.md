# autoFort
A quick python script for Elite Dangerous that automatically gathers fortification when you're afk.

## Disclaimer
Use at your own risk!
This is nothing but an app to send key events to WHATEVER application is in the foreground. If that happens not to be Elite, then a whole bunch of keystrokes will get sent to the wrong application!
This script has only been tested on Windows.
This script has only been tested in Carter Port.
This script is DUMB - it cannot receive any feedback from EliteDangerous to say that anything "worked". Therefore if you leave the UI in an unexpected location before starting, bad things might happen!
I take no responsibility if the script causes you to accidentally sell a ship, buy something you didn't want etc...
During alpha testing, three kittens exploded and a duck got sick...

## Requirements
You will need Python installed on your computer (if this takes off, I'll build it into an exe)

## Setup
Edit the sendKeys.ini file, and set the appropriate key-bindings for your UI Panel. 
        if you use A as one of your keybindings, then put DIK_A  (DIK standing for Direct Input Key)

If you're unsure of the naming for a key, there's a full list buried in the keybindings.json file.
        
Also set how many packages you want to collect, and how often you would like to run:
eg:  if you are rating 5 (and can collect 50 packages at a time) and have an empty cargo bay of 260t you would want the sequence to run 5 times.

## Usage
From the command prompt:
        python sendKeys.py

You'll hear a beep, which is your 10 second warning, and then 5 more beeps as it counts down to the start. During that time alt-tab to ED and leave it on the initial starport screen (with "Starport services" the highlighted option)
That's it, don't touch anything!  There are plenty of pauses built in, as sometimes the ED UI can be slow to update - but you're in no hurry, you're AFK :)

Just over 30 mins later, you'll hear the countdown beep sequence and the whole thing will go again.

## Problems
Sucks to be you!
(oh alright - buzz me in game / via the Minutemen forums / FedEscort Channel / carrier pidgeon)

## Acknowledgement
All the hard work was actually lifted from StackOverflow....   Copy and paste FTW!


