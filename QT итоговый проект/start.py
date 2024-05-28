from PyQt6.QtWidgets import QApplication
import sys

from TestWindow import TestWindow


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    window = TestWindow()

    window.show()

    sys.exit(app.exec())