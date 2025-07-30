from pygame import mixer

mixer.init()
mixer.set_num_channels(16)

snare = mixer.Sound('drums/snare.mp3')
hat = mixer.Sound('drums/hihat_closed.mp3')
kick = mixer.Sound('drums/kick.wav')
pedal = mixer.Sound('drums/hatfoot.wav')

snare.set_volume(0.3)
hat.set_volume(0.5)

def play_drum(sound):
    sound.play()
