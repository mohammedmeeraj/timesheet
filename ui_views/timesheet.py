from ui.py.timesheet_dialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication,QTableWidgetItem,QMessageBox
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal
from datetime import datetime,timedelta
from sqlalchemy.sql import text
from db.database_worker import DatabaseWorker

import sys
class Timesheet(QDialog):
    def __init__(self,user,week):
        super().__init__()
        self.ui=Ui_Dialog()
        self.setStyleSheet("""
                           QWidget{
                           border:2px solid black;
                           }
                           
                           """)
        self.ui.setupUi(self)
        self.setWindowTitle("Timesheet")
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self._is_dragging = False
        # self._drag_start_position = QPoint()
        self.user=user
        self.week=week
        self.ui.week_le.setText(week)
        self.ui.employee_le.setText(user)
        self.show_timesheet()

    
    def show_timesheet(self):
        self.update_table_headers()
        self.populate_timesheet_table()
        # self.calculate_daily_weekly_total()


    # def update_table_headers(self):
    #     year = datetime.now().year+1
    #     first_day_of_year = datetime(year, 1, 1)
    #     if first_day_of_year.weekday() != 0:  # If not Monday
    #         first_monday = first_day_of_year - timedelta(days=first_day_of_year.weekday())
    #     else:
    #         first_monday = first_day_of_year
    #     start_of_week = first_monday + timedelta(weeks=int(self.week) - 1)
    #     for i in range(7):
    #         day_date = start_of_week + timedelta(days=i)
    #         header = day_date.strftime("%b %d-%a")  # Format: "Jan 01-Mon"
    #         self.ui.timehseet_table.setHorizontalHeaderItem(2+i,QTableWidgetItem(header))
    #         month_date=header.split('-')[0]
    #         label=getattr(self.ui,f"day{i+1}")
    #         label.setText(month_date)
    def update_table_headers(self):
        year = datetime.now().year
        first_day_of_year = datetime(year, 1, 1)
        if first_day_of_year.weekday() != 0:
            first_monday = first_day_of_year - timedelta(days=first_day_of_year.weekday())
        else:
            first_monday = first_day_of_year
        start_of_week = first_monday + timedelta(weeks=int(self.week) - 1)
        days_in_year = (datetime(year + 1, 1, 1) - datetime(year, 1, 1)).days  # 365 or 366 days
        end_of_year = datetime(year, 12, 31)
        for i in range(7):
            day_date = start_of_week + timedelta(days=i)
            if day_date > end_of_year:
                break
            header = day_date.strftime("%b %d-%a")
            self.ui.timehseet_table.setHorizontalHeaderItem(3 + i, QTableWidgetItem(header))
            month_date = header.split('-')[0]
            label = getattr(self.ui, f"day{i + 1}")
            label.setText(month_date)
        
    def populate_timesheet_table(self):
        week=int(self.week)
        user=self.user
        query = text("""
    SELECT project,segment, subtask, weekday_1, weekday_2, weekday_3, weekday_4, weekday_5, weekday_6, weekday_7
    FROM tasks
    WHERE week = :week AND username = :user
""")
        params = {'week': week, 'user': user}
        # print(user)
        # print(week)
        self.worker=DatabaseWorker((query,params))
        self.worker.result_ready.connect(self.populate_rows)
        self.worker.start()
    


        
    def populate_rows(self,data):
        self.ui.timehseet_table.setRowCount(len(data))
        for row_idx,row_data in enumerate(data):
            for col_idx, val in enumerate(row_data):
                if val is not None and val != '':
                    item=QTableWidgetItem(str(val))
                    self.ui.timehseet_table.setItem(row_idx,col_idx,item)
                else:
                    item=QTableWidgetItem("")
                    self.ui.timehseet_table.setItem(row_idx,col_idx,item)
        self.calculate_daily_weekly_total()

    def calculate_daily_weekly_total(self):
        flag=True
        daily_totals=[0]*(self.ui.timehseet_table.columnCount()-3)
        for col in range(3,self.ui.timehseet_table.columnCount()):
            for row in range(self.ui.timehseet_table.rowCount()):
                item=self.ui.timehseet_table.item(row,col)
                # if item and item.text().isdigit():
                #     daily_totals[col-3]+=int(item.text())
                if item and item.text().strip():
                    try:
                        hours=float(item.text())
                        daily_totals[col-3]+=hours
                    except ValueError:
                        QMessageBox.warning(self,"Input Error",f"Invalid input for hours")

                    




        for i,total in enumerate(daily_totals):
            label=getattr(self.ui,f"day{i+1}_value")
            if total>8:
                label.setText("Invalid")
                flag=False
            else:
                label.setText(str(total))




        weekly_total=sum(daily_totals)
        if not flag:
            self.ui.total_time.setText("Invalid")
        else:
            t=str(weekly_total)
            self.ui.total_time.setText(f"{t} hours")

        # self.weekly_total=weekly_total


        


        








        





    

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
    dialog=Timesheet()
    dialog.show()
    sys.exit(app.exec())