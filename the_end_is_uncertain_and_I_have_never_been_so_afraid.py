#!/usr/bin/env python3

from ev3dev2.sound import Sound

sound = Sound()

song_location = "Songs/MariahCarey-AllIWantforChristmasIsYou.wav"

sound.play_file(wav_file=song_location)