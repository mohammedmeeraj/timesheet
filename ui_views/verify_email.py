from ui.py.verify_email_dialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal
import sys

class VerifyEmail(QDialog):
    form_data_submitted=pyqtSignal(object,str)
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Verify Email")
        self.ui.verify_btn.clicked.connect(self.on_submit)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def on_submit(self):
        email=self.ui.email_le.text()
        self.form_data_submitted.emit(self,email)
        
def load_stylesheet(file_path):
    """Load the QSS stylesheet from the given file path."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error loading stylesheet: {e}")
        return ""
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    stylesheet=load_stylesheet("c:/project management tool/assets/styles.qss")
    app.setStyleSheet(stylesheet)
    dialog=VerifyEmail()
    dialog.show()
    sys.exit(app.exec())
    