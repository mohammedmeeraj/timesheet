from ui.py.create_project import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal
import sys
class NewProject(QDialog):
    form_data_submitted=pyqtSignal(str,str)
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Create Project")
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self._is_dragging = False
        # self._drag_start_position = QPoint()
        self.ui.create_project_btn.clicked.connect(self.on_submit)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    def on_submit(self):
        project_name=self.ui.project_name_le.text()
        psp_element=self.ui.psp_element_le.text()
        self.form_data_submitted.emit(project_name,psp_element)
        self.close()
        
    # def mousePressEvent(self, event):
    #     if event.button() == Qt.MouseButton.LeftButton:  # Left mouse button starts dragging
    #         self._is_dragging = True
    #         self._drag_start_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
    #         event.accept()
    # def mouseMoveEvent(self, event):
    #     if self._is_dragging:
    #         self.move(event.globalPosition().toPoint() - self._drag_start_position)
    #         event.accept()
    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.MouseButton.LeftButton:  # Stop dragging when left mouse button is released
    #         self._is_dragging = False
    #         event.accept()

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
    dialog=NewProject()
    dialog.show()
    sys.exit(app.exec())