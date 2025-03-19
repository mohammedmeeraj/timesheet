from ui.py.edit_project_assign import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication,QCalendarWidget
from PyQt6.QtGui import QRegion,QIcon
from PyQt6.QtCore import Qt,QPoint,QRect,QDate,pyqtSignal
import sys,mysql.connector
class EditAssignment(QDialog):
    form_data_submitted=pyqtSignal(object,str,str,str,str,str,str)
    def __init__(self,project_names,users):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self._is_dragging = False
        self._drag_start_position = QPoint()
        self.calender_widget=QCalendarWidget(self)
        self.calender_widget.hide()
        self.calender_widget.setStyleSheet("""
QCalendarWidget QWidget{font-size:12px;color:#000;}
                                           
QCalendarWidget QToolButton{background-color: #FFFFFF;border: none;qproperty-icon: none;color: #000;font-size: 14px;padding: 5px;}                                        
                                                                                  
QCalendarWiget QToolButton::hover{background-color:#e3e3e3;border-radius:5px;}
QCalendarWidget QToolButton #qt_calendar_prevmonth,QCalendarWidget QToolButton #qt_calendar_nextmonth {border: none;min-width: 20px;max-width: 20px;min-height: 20px;max-height: 20px;}
QCalendarWidget QHeaderView::section { background-color: #FFFFFF; color: #A0A0A0;    font-size: 12px;}                                
                                         
                                           
                                           """)
        self.end_calender_widget=QCalendarWidget(self)
        self.end_calender_widget.hide()
        self.end_calender_widget.setStyleSheet("""
QCalendarWidget QWidget{font-size:12px;color:#000;}
                                           
QCalendarWidget QToolButton{background-color: #FFFFFF;border: none;qproperty-icon: none;color: #000;font-size: 14px;padding: 5px;}                                        
                                                                                  
QCalendarWiget QToolButton::hover{background-color:#e3e3e3;border-radius:5px;}
QCalendarWidget QToolButton #qt_calendar_prevmonth,QCalendarWidget QToolButton #qt_calendar_nextmonth {border: none;min-width: 20px;max-width: 20px;min-height: 20px;max-height: 20px;}
QCalendarWidget QHeaderView::section { background-color: #FFFFFF; color: #A0A0A0;    font-size: 12px;}                                
                                         
                                           
                                           """)
        

        self.ui.start_date_btn.clicked.connect(self.show_start_calender)
        self.ui.end_date_btn.clicked.connect(self.show_end_calender)
        self.update_project_names(project_names)
        self.update_subtask_names()
        self.update_usernames(users)
        self.ui.edit_project_combo.currentIndexChanged.connect(self.change_subtask_items)
        self.ui.edit_assign_btn.clicked.connect(self.on_submit)
        # self.populate_user_combo_box()
        


        # self.ui.start_date_btn.setIcon(QIcon())
        # self.ui.start_date_btn.setText("📆")
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    def populate_user_combo_box(self):
        try:
            conn=mysql.connector.connect(
                
                host="10.95.136.128",
                user="app_user",
                password="Mohammed&meeraj786",
                database="timesheet",



                
            )
            cursor=conn.cursor()
            query="select username from users"
            cursor.execute(query)
            a=cursor.fetchall()
            usernames=[username[0] for username in a]
            self.ui.edit_user_combo.addItems(usernames)

        except mysql.connector.Error as err:
            print("Error occured while retrieving usernames",err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    def on_submit(self):
        username=self.ui.edit_user_combo.currentText()
        project=self.ui.edit_project_combo.currentText()
        subtask=self.ui.edit_subtask_combo.currentText()
        start_date=self.ui.edit_start_date_le.text()
        end_date=self.ui.edit_end_date_le.text()
        duration=self.ui.edit_duration_le.text()
        self.form_data_submitted.emit(self,username,project,subtask,start_date,end_date,duration)
    def update_project_names(self,project_names):
        self.ui.edit_project_combo.clear()
        self.ui.edit_project_combo.addItems(project_names)
    def update_usernames(self,users):
        self.ui.edit_user_combo.clear()
        self.ui.edit_user_combo.addItems(users)
    def update_subtask_names(self):
        if self.ui.edit_project_combo.currentIndex==-1:
            pass
        else:
            project_name=self.ui.edit_project_combo.currentText()
            try:
                conn=mysql.connector.connect(
                host="10.95.136.128",
                user="app_user",
                password="Mohammed&meeraj786",
                database="timesheet"
            )
                cursor=conn.cursor()
                query="select subtask from subtasks where project_name=%s "
                cursor.execute(query,(project_name,))
                n=cursor.fetchall()
                subtask_names=[sub[0] for sub in n]
                self.ui.edit_subtask_combo.clear()
                self.ui.edit_subtask_combo.addItems(subtask_names)
            except mysql.connector.Error as err:
                print("Error occured",err)
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()
    def change_subtask_items(self):
        project=self.ui.edit_project_combo.currentText()
        try:
                conn=mysql.connector.connect(
                host="10.95.136.128",
                user="app_user",
                password="Mohammed&meeraj786",
                database="timesheet"
            )
                cursor=conn.cursor()
                query="select subtask from subtasks where project_name=%s "
                cursor.execute(query,(project,))
                n=cursor.fetchall()
                subtask_names=[sub[0] for sub in n]
                self.ui.edit_subtask_combo.clear()
                self.ui.edit_subtask_combo.addItems(subtask_names)
        except mysql.connector.Error as err:
                print("Error occured",err)
        finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()







    def show_start_calender(self):
        self.show_calender(self.ui.edit_start_date_le)
    def show_end_calender(self):
        self.show_calender2(self.ui.edit_end_date_le)
    def show_calender(self,target_le):
        # self.calender_widget=QCalendarWidget(self)
        self.calender_widget.setGridVisible(False)
        self.calender_widget.setWindowTitle("Select Date")
        self.calender_widget.setWindowFlags(self.windowFlags() | Qt.WindowType.Tool)
        self.calender_widget.clicked.connect(
            lambda date: self.set_date(target_le, date)
        )
        self.calender_widget.show()

    def set_date(self, target_lineedit, date: QDate):
        # Update QLineEdit with selected date
        target_lineedit.setText(date.toString("dd-MM-yyyy"))
        self.calculate_duration()

        self.calender_widget.close()
    def show_calender2(self,target_le):
        # self.calender_widget=QCalendarWidget(self)
        self.end_calender_widget.setGridVisible(False)
        self.end_calender_widget.setWindowTitle("Select Date")
        self.end_calender_widget.setWindowFlags(self.windowFlags() | Qt.WindowType.Tool)
        self.end_calender_widget.clicked.connect(
            lambda date: self.set_date_2(target_le, date)
        )
        self.end_calender_widget.show()

    def set_date_2(self, target_lineedit, date: QDate):
        # Update QLineEdit with selected date
        target_lineedit.setText(date.toString("dd-MM-yyyy"))
        self.calculate_duration()
        self.end_calender_widget.close()

    def calculate_duration(self):
        start_date_text = self.ui.edit_start_date_le.text()
        end_date_text = self.ui.edit_end_date_le.text()
        if start_date_text and end_date_text:
            start_date=QDate.fromString(start_date_text,"dd-MM-yyyy")
            end_date=QDate.fromString(end_date_text,"dd-MM-yyyy")
            if start_date.isValid() and end_date.isValid():
                days_difference=start_date.daysTo(end_date)
                self.ui.edit_duration_le.setText(f"{str(days_difference)} days")
            else:
                self.ui.edit_duration_le.setText("Invalid dates.")

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
    dialog=EditAssignment()
    dialog.show()
    sys.exit(app.exec())