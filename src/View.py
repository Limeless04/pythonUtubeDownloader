from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QMessageBox, QProgressBar, QHBoxLayout, QFileDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from pathlib import Path
from PySide6.QtCore import Qt
from VideoPreview import VideoPreview
from Controller import VideoDownloaderController
from PySide6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Video Downloader")
        self.setMinimumSize(800, 600)
        self.download_folder = str(Path.home() / "Downloads")

        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.url_entry = QLineEdit()
        self.url_entry.setPlaceholderText("Paste URL Here...")

        self.folder_layout = QHBoxLayout()
        self.folder_path = QLineEdit()
        self.folder_path.setPlaceholderText(self.download_folder)
        self.folder_button = QPushButton("Browse")
        self.folder_button.clicked.connect(self.select_folder)
        self.folder_layout.addWidget(self.folder_path)
        self.folder_layout.addWidget(self.folder_button)

        self.quality_combo = QComboBox()
        self.quality_combo.addItem("Choose Video Quality")
        self.quality_combo.setCurrentIndex(0)

        self.web_view = QWebEngineView()

        # Inisiasi Previw dan Controller
        self.controller = VideoDownloaderController(self, folder_path=self.folder_path)
        self.preview = VideoPreview(self.url_entry, 
                                    self.quality_combo, 
                                    self.web_view)

        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.controller.download_video)

        self.progress_bar = QProgressBar()

    def layout_widgets(self):
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        layout.addWidget(self.url_entry)
        layout.addLayout(self.folder_layout)
        layout.addWidget(self.quality_combo)
        layout.addWidget(self.download_button)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

    def select_folder(self):
        selected_folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if selected_folder:
            self.folder_path.setText(selected_folder)

    def set_download_enabled(self, enabled):
        self.download_button.setEnabled(enabled)

    def set_cursor(self, cursor):
        self.setCursor(cursor)