from ui.py.edit_subtask import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal
import sys,mysql.connector
class EditSubtask(QDialog):
    form_data_submitted=pyqtSignal(str,str,str)
    def __init__(self,project_names):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self._is_dragging = False
        self._drag_start_position = QPoint()
        self.ui.edit_subtask_btn.clicked.connect(self.on_submit)
        self.update_project_names(project_names=project_names)
        self.ui.project_combo_box_edit.currentIndexChanged.connect(self.update_psp_element)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
    def on_submit(self):
        project_name=self.ui.project_combo_box_edit.currentText()
        psp_element=self.ui.psp_element_le_edit.text()
        subtask=self.ui.subtask_name_le_edit.text()
        self.form_data_submitted.emit(project_name,psp_element,subtask)
        self.close()

    def update_psp_element(self):
        selected_project=self.ui.project_combo_box_edit.currentText()
        if not selected_project:
            self.ui.psp_element_le_edit.clear()
            return
        try:
            conn=mysql.connector.connect(
                host="10.95.136.128",
                user="app_user",
                password="Mohammed&meeraj786",
                database="timesheet"
            )
            cursor=conn.cursor()
            query="select pspelement from projects where project_name=%s"
            cursor.execute(query,(selected_project,))
            result=cursor.fetchone()
            if result:
                self.ui.psp_element_le_edit.setText(result[0])
            else:
                self.ui.psp_element_le_edit.clear()
        except mysql.connector.Error as err:
            print("Error fetching psp element")
            self.ui.psp_element_le_edit.clear()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update_project_names(self,project_names):
        self.ui.project_combo_box_edit.clear()
        self.ui.project_combo_box_edit.addItems(project_names)
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
    dialog=EditSubtask()
    dialog.show()
    sys.exit(app.exec())