import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

# এই ফাংশনটি ফাইলটিকে .exe করার সময় পাথ ঠিক রাখতে সাহায্য করবে
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class AegisBrowser(QMainWindow):
    def _init_(self):
        super(AegisBrowser, self)._init_()
        self.browser = QWebEngineView()
        
        # index.html ফাইলটি লোড করা হচ্ছে
        html_path = resource_path("index.html")
        self.browser.setUrl(QUrl.fromLocalFile(html_path))
        
        self.setCentralWidget(self.browser)
        self.showMaximized() # উইন্ডোটি ফুল স্ক্রিন ওপেন হবে
        self.setWindowTitle("AEGIS SECURITY CORES // EEE CYBER RESEARCH LAB")

if _name_ == "_main_":
    app = QApplication(sys.argv)
    window = AegisBrowser()
    window.show()
    sys.exit(app.exec_())