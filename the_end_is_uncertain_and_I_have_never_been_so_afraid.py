from ev3dev2.sound import Sound

sound = Sound()

song_location = "Songs\TobyMac-LightOfChristmasFtOwlCity.wav"

sound.play_file(wav_file=song_location)