from PySide6.QtWidgets import QMessageBox
from pytube import YouTube
from PySide6.QtCore import Qt
from YoutubeHandler import YouTubeHandler

class VideoDownloaderController:
    def __init__(self, main_window, folder_path):
        self.main_window = main_window 
        self.youtube_handler = YouTubeHandler()
        self.folder_path = folder_path

    def download_video(self):
        print("Donwloading...")
        url = self.url_entry.text()
        self.progress_bar.setValue(0)
        self.download_button.setEnabled(False)
        self.setCursor(Qt.WaitCursor)  # Set cursor to wait cursor
        selected_quality = self.quality_combo.currentText().split(" - ")[0]

        yt = self.youtube_handler.get_youtube_instance(url)
        success = self.youtube_handler.download_video(yt, selected_quality, self.folder_path)

        self.download_button.setEnabled(True)
        self.setCursor(Qt.ArrowCursor)
        if success:
            self.show_completed(yt)     

    def show_progress(self, stream, chunk, remaining):
        total_size = stream.filesize
        bytes_download = total_size - remaining
        progress = (bytes_download / total_size) * 100
        self.progress_bar.setValue(progress)

    def show_completed(self, stream, file_handle):
        video_title = stream.title
        QMessageBox.information(self, "Download Complete", f"Video '{video_title}' has been downloaded successfully.")