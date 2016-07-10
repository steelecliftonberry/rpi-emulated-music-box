import libvlc

class TrackManager:
    def __init__(self, paths):
        self.tracks = []
        self.track_paths = paths
        self.load_tracks()

    def load_tracks(self):
        instance = libvlc.Instance()
        for path in self.track_paths:
            player = instance.media_player_new()
            media = instance.media_new(path)
            player.set_media(media)
            self.tracks.append(player)

    def track_count(self):
        return len(self.tracks)

    def play_track(self, index):
        if index >= len(self.tracks):
            return False
        self.tracks[index].play()
        return True

    def stop_track(self, index):
        if index >= len(self.tracks):
            return False
        self.tracks[index].stop()
        return True
