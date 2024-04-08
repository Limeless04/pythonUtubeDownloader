from PySide6.QtWidgets import QMessageBox, QFileDialog
from pytube import YouTube
from PySide6.QtCore import Qt
from PySide6.QtCore import Qt, QThread, Signal

class VideoDownloaderWorker(QThread):
    progressChanged = Signal(int)
    downloadCompleted = Signal(str)

    def __init__(self, url, selected_quality, output_path):
        super().__init__()
        self.url = url
        self.selected_quality = selected_quality
        self.output_path = output_path

    def run(self):
        try:
            yt = YouTube(self.url, on_progress_callback=self.show_progress)
            stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=self.selected_quality).first()
            video_title = yt.title
            stream.download(output_path=self.output_path)
            self.downloadCompleted.emit(video_title)
        except Exception as e:
            self.downloadCompleted.emit(f"Error: {str(e)}")

    def show_progress(self, stream, chunk, remaining):
        total_size = stream.filesize
        bytes_download = total_size - remaining
        progress = (bytes_download / total_size) * 100
        self.progressChanged.emit(progress)

class VideoDownloaderController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.worker = None

    def download_video(self):
        url = self.main_window.url_entry.text()
        selected_quality = self.main_window.quality_combo.currentText().split(" - ")[0]
        output_path = self.main_window.folder_path.text()

        self.main_window.progress_bar.setValue(0)
        self.main_window.set_download_enabled(False)
        self.main_window.set_cursor(Qt.WaitCursor)

        self.worker = VideoDownloaderWorker(url, selected_quality, output_path)
        self.worker.progressChanged.connect(self.show_progress)
        self.worker.downloadCompleted.connect(self.show_completed)
        self.worker.start()

    def show_progress(self, progress):
        self.main_window.progress_bar.setValue(progress)

    def show_completed(self, message):
        if message.startswith("Error"):
            QMessageBox.critical(self.main_window, "Error", message)
        else:
            QMessageBox.information(self.main_window, "Download Complete", f"Video '{message}' has been downloaded successfully.")
        self.main_window.set_download_enabled(True)
        self.main_window.set_cursor(Qt.ArrowCursor)