#!/usr/bin/env python
# Instructions here: http://blog.computerbacon.com/playing-audio-in-python-with-libvlc.html

import libvlc
import time
from random import randint
from strategy_one import StrategyOne

'''
class SchmittTrigger:
    def __init__(self, upper_threshold, lower_threshold, output_threshold=LOW):
        self.upper_threshold = upper_threshold
        self.lower_threshold = lower_threshold
        self.output_level = output_threshold

    def update(self, voltage):
        transition = NONE
        if self.output_level == LOW and voltage >= self.upper_threshold:
            self.output_level = HIGH
            transition = RISING
        elif self.output_level == HIGH and voltage >= self.lower_threshold:
            self.output_level = LOW
            transition = FALLING
        return transition

    def output_level(self):
        return self.output_level

def poll_pin():
    trigger = SchmittTrigger(4.5, 0.5, LOW)
    while True:
        time.sleep(0.010) #10ms
        voltage = pin[x].get_voltage()
        edge = trigger.update(voltage)
        if (edge == RISING):
            sample.play()
'''

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
    strategy = StrategyOne(audio_players)
    #revolution_duration = 30 #TODO: Not relevant yet
    while(True):
        strategy.update()
        time.sleep(randint(1,3))

'''
    # Add a conditional here to only do all the below if the current LDR triggers
    #if(LDR_triggered):
    #if trigger.update(voltage) == RISING:
'''
