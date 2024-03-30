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

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    downloader_app = MainWindow()
    downloader_app.show()

    sys.exit(app.exec())
