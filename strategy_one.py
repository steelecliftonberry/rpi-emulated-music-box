class StrategyOne:
    def __init__(self, audio_players):
        self.audio_players = audio_players
        self.tracks_playing = []
        self.tracks_playing_count = 1
        self.increasing = True

    def update(self):
        print(self.tracks_playing_count)
        if(self.tracks_playing_count >= 12):
            self.increasing = False
        elif(self.tracks_playing_count <= 1):
            self.increasing = True

        if(self.increasing):
            track_to_add = self.audio_players[self.tracks_playing_count]
            self.tracks_playing.append(track_to_add)
            track_to_add.play()
            self.tracks_playing_count += 1
        else:
            track_to_stop = self.tracks_playing.pop()
            track_to_stop.stop() # TODO confirm this works
            self.tracks_playing_count -= 1
        return
