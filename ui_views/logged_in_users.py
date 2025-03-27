from ui.py.logged_in_users_dialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication,QTableWidgetItem,QMessageBox
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal
import sys,mysql.connector
from db.db_pool import DatabasePool
from .extract_log_user_admin import ExtractUserLogAdmin

class LoggedInUsers(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.populate_logged_in_users()
        self.ui.search_le.textChanged.connect(self.search_logged_in_users)
        self.ui.btn_extract_logs.clicked.connect(self.show_extract_dialog)
        
    def populate_logged_in_users(self):
        db_instance=DatabasePool(pool_type="read")  
        with db_instance.get_db_connection() as conn:
            cursor=conn.cursor()
            try:
                query="Select employee_name, login_time, logout_time, wifi_name, username, login_date, day_name, hours_logged,regularised FROM user_logs "
                cursor.execute(query)
                records=cursor.fetchall()
                # print("The records are ",records)
                if not records:
                    print("No records found")
                    return
                self.ui.tableWidget.setRowCount(len(records))
                num_columns=8

                #populate the table with serial numbers and other data

                for row_idx,row_data in enumerate(records):
                    #Add serial number
                    # sl_no_item = QTableWidgetItem(str(row_idx + 1))
                    # sl_no_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    # sl_no_item.setFlags(sl_no_item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Make read-only
                    # self.ui.tableWidget.setItem(row_idx, 0, sl_no_item) 

                    #Populate the rest of the columns
                    for col_idx, cell_data in enumerate(row_data):
                        item = QTableWidgetItem(str(cell_data) if cell_data else "-")  # Handle NULL values
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Make read-only
                        self.ui.tableWidget.setItem(row_idx, col_idx, item) 
                # Auto-resize columns for better UI
                 # Set equal width for all columns
                
                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

            except mysql.connector.Error as err:
                conn.rollback()
                QMessageBox.critical(self,"Database Error",f"An error occurred: {err}")


    def show_extract_dialog(self):
        dialog=ExtractUserLogAdmin()
        dialog.exec()

    def search_logged_in_users(self):
        search_text=self.ui.search_le.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            show_row=False
            for col in range(self.ui.tableWidget.columnCount()):
                item=self.ui.tableWidget.item(row,col)
                if item and search_text in item.text().lower():
                    show_row=True
                    break
            self.ui.tableWidget.setRowHidden(row,not show_row)
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
    dialog=LoggedInUsers()
    dialog.show()
    sys.exit(app.exec())