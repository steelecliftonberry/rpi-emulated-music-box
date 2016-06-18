# Instructions here: http://blog.computerbacon.com/playing-audio-in-python-with-libvlc.html

import libvlc
import time

instance = libvlc.Instance()
audio_player_one = instance.media_player_new()
audio_player_two = instance.media_player_new()

media_one = instance.media_new('./resources/audio/default/musicbox_track1.wav')
media_two = instance.media_new('./resources/audio/default/musicbox_track2.wav')
audio_player_one.set_media(media_one)
audio_player_two.set_media(media_two)

audio_player_one.play()
time.sleep(5)
audio_player_two.play()
time.sleep(10)


# player.set_position(10)
# player.audio_set_volume(70)

