from ui.py.forgot_password_dialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication
from PyQt6.QtGui import QRegion,QIcon
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal
import sys
class Forgot_Password(QDialog):
    form_data_submitted=pyqtSignal(object,str)
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Reset Password")
        self.ui.send_request_btn.clicked.connect(self.on_submit)
        

    def on_submit(self):
        username=self.ui.username_le.text().strip()
        self.form_data_submitted.emit(self,username)
        
    

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
    dialog=Forgot_Password()
    dialog.show()
    sys.exit(app.exec())

