from ui.py.create_user_dialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication,QLineEdit
from PyQt6.QtGui import QRegion,QIcon
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal
import sys
from sqlalchemy.sql import text
from db.database_worker import DatabaseWorker

class CreateUser(QDialog):
    form_data_submitted=pyqtSignal(object,str,str,str,str,str,str,str)
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.role_combo.addItem("Select role")
        self.ui.role_combo.setCurrentIndex(0)
        self.ui.role_combo.addItem("user")
        self.ui.role_combo.addItem("admin")
        self.ui.role_combo.model().item(0).setEnabled(False)
        self.setWindowTitle("Create User")
        self.setWindowIcon(QIcon())
        self.ui.reporting_to_combo.addItem("Reporting to")
        self.ui.reporting_to_combo.setCurrentIndex(0)
        self.ui.reporting_to_combo.model().item(0).setEnabled(False)
        self.ui.create_pass_le.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.repeat_pass_le.setEchoMode(QLineEdit.EchoMode.Password)
        self.load_admins()
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self._is_dragging = False
        # self._drag_start_position = QPoint()
        self.ui.btn_create_user.clicked.connect(self.on_submit)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    def on_submit(self):
        username=self.ui.username_le.text().strip()
        employee_id=self.ui.employee_id_le.text().strip()
        email=self.ui.email_le.text().strip()
        password=self.ui.create_pass_le.text().strip()
        repeat_password=self.ui.repeat_pass_le.text().strip()
        role=self.ui.role_combo.currentText()
        reporting_to=self.ui.reporting_to_combo.currentText()
        self.form_data_submitted.emit(self,username,employee_id,email,password,repeat_password,role,reporting_to)
    
    def load_admins(self):
        role='admin'
        query=text("select username from users where role=:role")
        self.worker=DatabaseWorker(query=(query,{'role':'admin'}))
        self.worker.result_ready.connect(self.populate_admins)
        self.worker.start()

    def populate_admins(self,data):
        admins=[d[0] for d in data]
        self.ui.reporting_to_combo.addItems(admins)

        
    

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
    dialog=CreateUser()
    dialog.show()
    sys.exit(app.exec())