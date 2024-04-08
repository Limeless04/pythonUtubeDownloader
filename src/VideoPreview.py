from pytube import YouTube
from YoutubeHandler import YouTubeHandler

class VideoPreview:
    def __init__(self, url_entry, quality_combo, web_view):
        self.youtube_handler = YouTubeHandler()
        self.url_entry = url_entry
        self.quality_combo = quality_combo        
        self.populate_quality_options()
        self.web_view = web_view
        self.url_entry.textChanged.connect(self.load_preview)
    
    def load_preview(self):
        print("Load Preview")
        url = self.url_entry.text()
        if url:
            yt = self.youtube_handler.get_youtube_instance(url)
            video_stream = self.youtube_handler.get_video_stream(yt)
            if video_stream:
                video_id = yt.video_id
                embed_code = f'<iframe width="100%" height="100%" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'
                self.web_view.setHtml(embed_code)


    def populate_quality_options(self):
        self.quality_combo.clear()
        quality_array = ["Choose Video Quality", "720p", "480p", "360p"]
        for resolution in quality_array:
            self.quality_combo.addItem(resolution)


