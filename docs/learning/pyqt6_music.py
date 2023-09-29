import sys
from pathlib import Path

from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtWidgets import QApplication


class Playz:
    def __init__(self, path_music):
        self.path_music = path_music

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(str(self.path_music)))
        self.audio_output.setVolume(1)   # 0.0-1
        self.player.play()
        self.player.setLoops(-1) # -1=infinite


working_directory = Path(__file__).parent
path_music_1 = Path(working_directory, 'skins', 'terminator', 'music.mp3')
path_music_2 = Path(working_directory, 'skins', 'idiocracy', 'music.mp3')



app = QApplication([])

test_music = Playz(path_music_1)

print('\n')
input(' Hit enter for next song! ')
print('\n')

test_music = Playz(path_music_2)


sys.exit(app.exec())