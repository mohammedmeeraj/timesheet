from ui.py.extract_log_user_dialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication,QTableWidgetItem,QMessageBox,QCalendarWidget,QFileDialog
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal,QDate
import sys,mysql.connector
from db.db_pool import DatabasePool
import pandas as pd
from datetime import datetime,date,time
from db.db_pool import DatabasePool
class ExtractUserLog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.calender_widget=QCalendarWidget(self)
        self.calender_widget.hide()
        self.calender_widget.setStyleSheet("""
QCalendarWidget QWidget {
    background-color: #fff;
    color: #000;
    border-radius: 2px;
    font-size: 14px;
}            

QCalendarWidget QAbstractItemView {
    background-color: #fff;
    color: #000;  /* Fixed text color */
    selection-background-color: #1F95EF;
}      

QCalendarWidget QTableView::item {
    border: 1px solid #f2f2f2; /* Border around individual cells */
}
QCalendarWidget QWidget#qt_calendar_navigationbar {
        background-color: #eee;
        
    } 
QCalendarWidget QToolButton {
                                          background-color: #eee;
    color: black;
    border-radius: 5px;
    padding: 15px;
                                          
                                          
                                          }     
                    
                                          
                                          """)
        self.calender_widget.setFirstDayOfWeek(Qt.DayOfWeek.Monday)
        self.calender_widget.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calender_widget_2=QCalendarWidget(self)
        self.calender_widget_2.hide()
        self.calender_widget_2.setStyleSheet("""
QCalendarWidget QWidget {
    background-color: #fff;
    color: #000;
    border-radius: 2px;
    font-size: 14px;
}            

QCalendarWidget QAbstractItemView {
    background-color: #fff;
    color: #000;  /* Fixed text color */
    selection-background-color: #1F95EF;
}      

QCalendarWidget QTableView::item {
    border: 1px solid #f2f2f2; /* Border around individual cells */
}
QCalendarWidget QWidget#qt_calendar_navigationbar {
        background-color: #eee;
        
    } 
QCalendarWidget QToolButton {
                                          background-color: #eee;
    color: black;
    border-radius: 5px;
    padding: 15px;
                                          
                                          
                                          }     
                    
                                          
                                          """)
        self.calender_widget_2.setFirstDayOfWeek(Qt.DayOfWeek.Monday)
        self.calender_widget_2.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.ui.pushButton.clicked.connect(self.extract_logs_to_excel)

        
        self.ui.btn_calender_1.clicked.connect(lambda:(self.show_calender(self.ui.start_le,self.calender_widget)))
        self.ui.btn_calender_2.clicked.connect(lambda:(self.show_calender(self.ui.end_le,self.calender_widget_2)))


    

    
    def extract_logs_to_excel(self):
        start_date=self.ui.start_le.text()
        end_date=self.ui.end_le.text()
        start_date_obj=datetime.strptime(start_date,"%d-%m-%Y")
        formated_start_date=start_date_obj.strftime("%Y-%m-%d")
        end_date_obj=datetime.strptime(end_date,"%d-%m-%Y")
        formated_end_date=end_date_obj.strftime("%Y-%m-%d")
        print(formated_start_date)
        print(formated_end_date)
        db_instance=DatabasePool(pool_type="read")
        with db_instance.get_db_connection() as conn:
            try:
                cursor=conn.cursor()
                query="""
select employee_name,login_time,logout_time,username,login_date,day_name,hours_logged from user_logs where login_date between %s and %s order by login_date asc



"""
                cursor.execute(query,(formated_start_date,formated_end_date))
                records=cursor.fetchall()
                records = [
    (
        row[0],  # Employee Name
        row[1] if row[1] is None else str(row[1]) ,  # Login Time
        row[2] if row[2] is None else str(row[2]) ,  # Logout Time
        row[3],  # Username
        row[4].strftime("%Y-%m-%d") if isinstance(row[4], date) else row[4],  # Login Date
        row[5],  # Day
        row[6] if row[6] is None else str(row[6])  # Hours Logged (Convert to string if needed)
    )
    for row in records
]

                if not records:
                    QMessageBox.warning(self,"No Logs","No logs found return")
                    return
                
                #convert data to a pandas dataframe
                df=pd.DataFrame(records,columns=["Employee Name","Login Time","Logout Time","Username","Login Date","Day","Hours Logged"])
                file_path,_=QFileDialog.getSaveFileName(self,"Save Excel File","","Excel Files (*.xlsx)")
                if file_path:
                    df.to_excel(file_path,index=False)
                    print(f"Excel file saved successfully:{file_path}")
                

                
            except mysql.connector.Error as err:
                conn.rollback()
                QMessageBox.critical(self,"Database Error",f"An error occured:{err}")

        

    def show_calender(self,target_le,calender):
        # self.calender_widget=QCalendarWidget(self)
        calender.setGridVisible(False)
        calender.setWindowTitle("Select Date")
        calender.setWindowFlags(self.windowFlags() | Qt.WindowType.Tool)
        calender.clicked.connect(
            lambda date: self.set_date(target_le, date)
        )
        calender.show()
    # def show_calender_2(self,target_le):
    #     # self.calender_widget=QCalendarWidget(self)
    #     self.calender_widget_2.setGridVisible(False)
    #     self.calender_widget_2.setWindowTitle("Select Date")
    #     self.calender_widget_2.setWindowFlags(self.windowFlags() | Qt.WindowType.Tool)
    #     self.calender_widget_2.clicked.connect(
    #         lambda date: self.set_date(target_le, date)
    #     )
    #     self.calender_widget_2.show()
    
    def set_date(self, target_lineedit, date: QDate):
        # Update QLineEdit with selected date
        target_lineedit.setText(date.toString("dd-MM-yyyy"))
        self.calender_widget.close()
    
    

    
        
    

    
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
    dialog=ExtractUserLog()
    dialog.show()
    sys.exit(app.exec())