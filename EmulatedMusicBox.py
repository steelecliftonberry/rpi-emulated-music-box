#!/usr/bin/env python
# Instructions here: http://blog.computerbacon.com/playing-audio-in-python-with-libvlc.html

import time
from random import randint
from strategy_one import StrategyOne
from strategy_two import StrategyTwo
from track_manager import TrackManager

def load_track_paths():
    paths = []
    for track_number in range(1,12+1):
        path = "./resources/audio/default/musicbox_track{0}.wav".format(track_number)
        paths.append(path)
    return paths

if __name__ == '__main__':
    tracks = load_track_paths()
    track_manager = TrackManager(tracks)
    strategy = StrategyOne(track_manager)
    #revolution_duration = 30 #TODO: Not relevant yet
    while(True):
        strategy.update()
        time.sleep(randint(1,3))
