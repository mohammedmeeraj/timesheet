from ui.py.reset_user_password_dialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication,QLineEdit
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal
import sys
class Reset_User_Password(QDialog):
    form_data_submitted=pyqtSignal(object,str,str,str)
    def __init__(self,usernames):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Reset Password")
        self.usernames=usernames
        self.populate_employee_combo()
        # self.ui.password_le.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.new_pass_le.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.confirm_new_pass_le.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.reset_pass_btn.clicked.connect(self.on_submit)
        # self.ui.edit_push_btn.clicked.connect(self.on_submit)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    def on_submit(self):
        employee=self.ui.employee_combo.currentText()
        password=self.ui.new_pass_le.text().strip()
        confirm_password=self.ui.confirm_new_pass_le.text().strip()
        self.form_data_submitted.emit(self,employee,password,confirm_password)

    def populate_employee_combo(self):
        self.ui.employee_combo.clear()
        self.ui.employee_combo.addItem("--Select User--")
        self.ui.employee_combo.setCurrentIndex(0)
        self.ui.employee_combo.model().item(0).setEnabled(False)
        
        self.ui.employee_combo.addItems(self.usernames)
        
    

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
    dialog=Reset_User_Password()
    dialog.show()
    sys.exit(app.exec())