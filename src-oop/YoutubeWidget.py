from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout

class YouTubeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self)
        
        layout = QVBoxLayout()
        layout.addWidget(self)
        self.setLayout(layout)

    def load_video(self, video_url):
        self.player.setSource(QUrl(video_url))
        self.videoWidget = QVideoWidget()
        self.player.setVideoOutput(self.videoWidget)
        self.videoWidget.show()
        self.player.play()
