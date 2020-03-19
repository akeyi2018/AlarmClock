import vlc

class MusicPlayer:

    def __init__(self, musicPath):

        self.musicPathh = musicPath
        #prepare music
	      self.player = vlc.MediaListPlayer()
	      self.mediaList = vlc.MediaList([self.musicPath])
        self.player.set_media_list(self.mediaList)
        self.player.set_playback_mode(vlc.PlaybackMode.loop)

    def Play(self):
        pass

    def Stop(self):
        pass

    def GetMusic(self):
        pass

    def SetMusic(self):
        pass
