import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView


class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IM Tech | Driving Exam Practice")
        self.load(QUrl("http://127.0.0.1:8000"))
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            self.back()
        elif event.key() == Qt.Key_Forward:
            self.forward()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec())
