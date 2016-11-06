import time
import random

class StrategyThree:
    def __init__(self, track_manager):
        self.track_manager = track_manager
        self.track_map = range(self.track_manager.track_count())

        self.next_track = 0
        self.direction = 1
        random.shuffle(self.track_map)

    def do_next_track(self):
        index = self.track_map[self.next_track]
        if self.direction == 1:
            print('Playing {0}'.format(self.next_track))
            self.track_manager.play_track(index)
        else:
            print('Stopping {0}'.format(self.next_track))
            self.track_manager.stop_track(index)
        self.next_track += self.direction

    def update(self):
	if self.next_track <= 0:
	  # Store index of old track 0
	  old_track_zero_index = self.track_map[0]
	  # Play new track 0
	  random.shuffle(self.track_map)
          print('Playing new track 0')
          index = self.track_map[0]
          self.track_manager.play_track(index)
          time.sleep(1.5)
	  # Stop old track 0
	  print('Stopping old track 0')
          self.track_manager.stop_track(old_track_zero_index)
	  self.next_track = 1
          self.direction = 1
	else:
          self.do_next_track()

        if self.next_track >= len(self.track_map):
            self.next_track = len(self.track_map) - 1
            self.direction = -1
