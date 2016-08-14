#!/home/pi/git/rpi-emulated-music-box/venv/bin/python
# Instructions here: http://blog.computerbacon.com/playing-audio-in-python-with-libvlc.html

import time
from strategy_one import StrategyOne
from strategy_two import StrategyTwo
from track_manager import TrackManager
from triggers import SchmittTrigger
from sources import NormalisedMCPChannel
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI

def load_track_paths():
    paths = []
    for track_number in range(1,12+1):
        path = "./resources/audio/default/musicbox_track{0}.wav".format(track_number)
        paths.append(path)
    return paths

if __name__ == '__main__':
    tracks = load_track_paths()
    track_manager = TrackManager(tracks)
    strategy = StrategyTwo(track_manager)
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(0,0))
    source = NormalisedMCPChannel(mcp, 0)
    trigger = SchmittTrigger(0.25, 0.75, source)
    while True:
        if trigger.sample() == 'R':
            strategy.update()
        time.sleep(0.1)
