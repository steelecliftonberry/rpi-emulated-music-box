class StrategyOne:
    def __init__(self, track_manager):
        self.track_manager = track_manager

        self.next_track = 0
        self.direction = 1

    def update(self):
        if self.next_track < 0:
            self.next_track = 0
            self.direction = 1

        elif self.next_track >= self.track_manager.track_count():
            self.next_track = self.track_manager.track_count() - 1
            self.direction = -1

        if self.direction == 1:
            print('Playing {0}'.format(self.next_track))
            self.track_manager.play_track(self.next_track)
        else:
            print('Stopping {0}'.format(self.next_track))
            self.track_manager.stop_track(self.next_track)

        self.next_track += self.direction
