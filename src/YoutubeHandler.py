from PySide6.QtWidgets import QMessageBox
from pytube import YouTube


class YouTubeHandler:
    def __init__(self):
        pass

    def get_youtube_instance(self, url):
        return YouTube(url)

    def download_video(self, yt, selected_quality, folder_path):
        try:
            stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=selected_quality).first()
            stream.download(output_path=folder_path)
            return True
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")
            return False

    def get_video_stream(self, yt):
        return yt.streams.filter(progressive=True, file_extension='mp4').first()