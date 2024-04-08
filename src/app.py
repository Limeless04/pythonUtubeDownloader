# from MainWindow import MainWindow
from View import MainWindow
from VideoPreview import VideoPreview
from Controller import VideoDownloaderController
from PySide6.QtWidgets import QApplication
import sys

"""
Aplikasi Download Video Youtube sederhana
v0.1

# current feature
- Preview Video
- Download Button
- Progress Bar
- Resolution Selection

# feature to be added
- choose where to save the downloded video
- threading

v0.2
Refactor the code to be more inline with OOP
split the code into diffrent class
"""

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    sys.exit(app.exec())
