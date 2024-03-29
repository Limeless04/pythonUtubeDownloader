from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QMessageBox, QProgressBar
from PySide6.QtWebEngineWidgets import QWebEngineView
from pytube import YouTube
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Video Downloader")
        self.setMinimumSize(800, 600)

        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.url_entry = QLineEdit()
        self.url_entry.textChanged.connect(self.load_preview)
        self.url_entry.textChanged.connect(self.populate_quality_options)
        self.quality_combo = QComboBox()
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.download_video)
        self.web_view = QWebEngineView()
        self.progress_bar = QProgressBar()

    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.quality_combo)
        layout.addWidget(self.download_button)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

    def load_preview(self):
        url = self.url_entry.text()
        video_id = YouTube(url).video_id
        embed_code = f'<iframe width="800" height="600" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>'
        self.web_view.setHtml(embed_code)

    def populate_quality_options(self):
        self.quality_combo.clear()
        url = self.url_entry.text()
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
        for stream in streams:
            self.quality_combo.addItem(f"{stream.resolution} - {stream.mime_type}")

    def download_video(self):
        self.progress_bar.setValue(0)
        self.download_button.setEnabled(False)
        self.setCursor(Qt.WaitCursor)  # Set cursor to wait cursor
        url = self.url_entry.text()
        selected_quality = self.quality_combo.currentText().split(" - ")[0]

        try:
            yt = YouTube(url, on_progress_callback=self.show_progress, on_complete_callback=self.show_completed)
            stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=selected_quality).first()
            video_title = yt.title
            stream.download()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

        self.download_button.setEnabled(True)
        self.setCursor(Qt.ArrowCursor)

    def show_progress(self, stream, chunk, remaining):
        total_size = stream.filesize
        bytes_download = total_size - remaining
        progress = (bytes_download / total_size) * 100
        self.progress_bar.setValue(progress)

    def show_completed(self, stream, file_handle):
        video_title = stream.title
        QMessageBox.information(self, "Download Complete", f"Video '{video_title}' has been downloaded successfully.")
