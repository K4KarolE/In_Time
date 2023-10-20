
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtCore import QUrl

from .cons_and_vars import Path
from .cons_and_vars import WORKING_DIRECTORY, skin_selected

class Music:
    def __init__(self, music_volume):
        self.path_music = Path(WORKING_DIRECTORY, 'skins', skin_selected, 'music.mp3')
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(str(self.path_music)))
        self.player.setLoops(-1) # -1=infinite
        self.audio_output.setVolume(music_volume)