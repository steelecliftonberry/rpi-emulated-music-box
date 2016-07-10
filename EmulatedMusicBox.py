#!/usr/bin/env python
# Instructions here: http://blog.computerbacon.com/playing-audio-in-python-with-libvlc.html

import libvlc
import time
from random import randint
from strategy_one import StrategyOne
from strategy_two import StrategyTwo

def create_audio_player(instance, audio_file_path):
    audio_player = instance.media_player_new()
    audio_player.set_media(instance.media_new(audio_file_path))
    return audio_player

def load_tracks():
    instance = libvlc.Instance()
    audio_players = []
    for track_number in range(1,12+1):
        audio_file_path = "./resources/audio/default/musicbox_track{0}.wav".format(track_number)
        print audio_file_path
        audio_player = create_audio_player(instance, audio_file_path)
        audio_players.append(audio_player)
    return audio_players

if __name__ == '__main__':
    audio_players = load_tracks()
    strategy = StrategyTwo(audio_players)
    #revolution_duration = 30 #TODO: Not relevant yet
    while(True):
        strategy.update()
        time.sleep(randint(1,3))
