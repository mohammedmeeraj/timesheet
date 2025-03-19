from ui.py.add_subtask import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal
import mysql.connector
import sys

class NewSubtask(QDialog):
    form_data_submitted=pyqtSignal(str,str,str)
    def __init__(self,project_names):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.psp_element_le.setReadOnly(True)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self._is_dragging = False
        self._drag_start_position = QPoint()
        self.update_project_names(project_names)
        self.default_project_name_psp()
        self.ui.project_combo_box.currentIndexChanged.connect(self.update_psp_element)
        self.ui.add_subtask_btn.clicked.connect(self.on_submit)

        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    def on_submit(self):
        try:
            data1=self.ui.project_combo_box.currentText()
        except Exception:
            data1=""
        data2=self.ui.subtask_name_le.text().strip()
        if not data2:
            QMessageBox.warning(self,"Input Error","Subtask name cannot be empty!")
            return
        data3=self.ui.psp_element_le.text()
        self.form_data_submitted.emit(data1,data2,data3)
        self.close()
    def update_project_names(self,project_names):
        self.ui.project_combo_box.clear()
        self.ui.project_combo_box.addItems(project_names)
    def default_project_name_psp(self):
        selected_project=self.ui.project_combo_box.currentText()
        if not selected_project:
            self.ui.psp_element_le.clear()
            return
        try:
            conn=mysql.connector.connect(
                host="10.95.136.128",
                user="app_user",
                password="Mohammed&meeraj786",
                database="timesheet"
            )
            cursor = conn.cursor()
            query="Select pspelement from projects where project_name=%s"
            cursor.execute(query,(selected_project,))
            result=cursor.fetchone()
            if result:
                self.ui.psp_element_le.setText(result[0])
            else:
                self.ui.psp_element_le.clear()
        except mysql.connector.Error as err:
            print("Error fetching psp element:",err)
            self.ui.psp_element_le.clear()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


    def update_psp_element(self):
        selected_project=self.ui.project_combo_box.currentText()
        if not selected_project:
            self.ui.psp_element_le.clear()
            return
        try:
            conn=mysql.connector.connect(
                host="10.95.136.128",
                user="app_user",
                password="Mohammed&meeraj786",
                database="timesheet"
            )
            cursor = conn.cursor()
            query="Select pspelement from projects where project_name=%s"
            cursor.execute(query,(selected_project,))
            result=cursor.fetchone()
            if result:
                self.ui.psp_element_le.setText(result[0])
            else:
                self.ui.psp_element_le.clear()
        except mysql.connector.Error as err:
            print("Error fetching psp element:",err)
            self.ui.psp_element_le.clear()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # Left mouse button starts dragging
            self._is_dragging = True
            self._drag_start_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if self._is_dragging:
            self.move(event.globalPosition().toPoint() - self._drag_start_position)
            event.accept()
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # Stop dragging when left mouse button is released
            self._is_dragging = False
            event.accept()

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
    dialog=NewSubtask()
    dialog.show()
    sys.exit(app.exec())