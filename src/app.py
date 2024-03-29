from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication
import sys

"""
Aplikasi Download Video Youtube sederhana
v 0.1

# current feature
- Preview Video
- Download Button
- Progress Bar
- Resolution Selection

# feature to be added
- choose where to save the downloded video
- threading
"""


class App:

    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        downloader_app = MainWindow()
        downloader_app.show()

        sys.exit(self.app.exec())


if __name__ == "__main__":
    App()