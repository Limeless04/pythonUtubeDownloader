from PySide6.QtWidgets import  QVBoxLayout
from pytube import YouTube
from YoutubeWidget import YouTubeWidget

class VideoPreview:
    def __init__(self, url_entry, quality_combo):
        self.url_entry = url_entry
        self.quality_combo = quality_combo
        self.youtube_widget = YouTubeWidget()
        self.youtube_widget.setMinimumSize(800, 600)
        
        layout = QVBoxLayout()
        layout.addWidget(self.youtube_widget)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.quality_combo)
        
        self.setLayout(layout)
        
        self.url_entry.textChanged.connect(self.load_preview)
    
    def load_preview(self):
        print("Load Preview")
        url = self.url_entry.text()
        if url:
            yt = YouTube(url)
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            if video_stream:
                self.youtube_widget.load_video(video_stream.url)

            self.populate_quality_options()

    def populate_quality_options(self):
        self.quality_combo.clear()
        url = self.url_entry.text()
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
        for stream in streams:
            self.quality_combo.addItem(f"{stream.resolution} - {stream.mime_type}")


