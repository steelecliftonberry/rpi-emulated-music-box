import random

class StrategyTwo:
    def __init__(self, track_manager):
        self.track_manager = track_manager
        self.track_map = range(self.track_manager.track_count())

        self.next_track = 0
        self.direction = 1
        random.shuffle(self.track_map)

    def update(self):
        if self.next_track < 0:
            self.next_track = 0
            self.direction = 1
            random.shuffle(self.track_map)

        elif self.next_track >= len(self.track_map):
            self.next_track = len(self.track_map) - 1
            self.direction = -1

        index = self.track_map[self.next_track]
        if self.direction == 1:
            print('Playing {0}'.format(self.next_track))
            self.track_manager.play_track(index)
        else:
            print('Stopping {0}'.format(self.next_track))
            self.track_manager.stop_track(index)

        self.next_track += self.direction
