#!/home/pi/git/rpi-emulated-music-box/venv/bin/python
# Instructions here: http://blog.computerbacon.com/playing-audio-in-python-with-libvlc.html

import time
import os
import argparse
from strategy_one import StrategyOne
from strategy_two import StrategyTwo
from strategy_three import StrategyThree
from track_manager import TrackManager
from triggers import SchmittTrigger
from sources import NormalisedMCPChannel
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI

def parse_args():
    parser = argparse.ArgumentParser(description='Play some crazy sounds')
    parser.add_argument('sample_dir', help='directory containing audio samples')
    return parser.parse_args()

def load_track_paths(sample_dir):
    paths = []
    for filename in os.listdir(sample_dir):
        if filename.endswith('.wav'):
            paths.append(os.path.join(sample_dir, filename))
    return paths

if __name__ == '__main__':
    args = parse_args()
    tracks = load_track_paths(args.sample_dir)
    track_manager = TrackManager(tracks)
    strategy = StrategyThree(track_manager)
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(0,0))
    source = NormalisedMCPChannel(mcp, 0)
    trigger = SchmittTrigger(0.25, 0.75, source)
    while True:
        if trigger.sample() == 'R':
            strategy.update()
        time.sleep(0.1)
