from ui.py.excel_export_user_dialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication,QMessageBox,QCompleter,QComboBox
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal,QStringListModel,QSortFilterProxyModel,QRegularExpression
from db.database_worker import DatabaseWorker
import sys
from sqlalchemy.sql import text

class Extract_to_Excel(QDialog):
    form_data_submitted=pyqtSignal(object,str,str,str)
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Export Data")
        self.threads=[]
        self.ui.month_or_week_com.clear()
        self.ui.month_or_week_com.addItem("--Extract by month or week--")
        self.ui.month_or_week_com.setCurrentIndex(0)
        self.ui.month_or_week_com.model().item(0).setEnabled(False)
        self.ui.month_or_week_com.addItems(["Month","Week"])
        self.ui.month_or_week_com.currentIndexChanged.connect(self.handle_items)
        self.ui.start_mon_week_combo.clear()
        self.ui.end_month_week_combo.clear()
        # self.load_employee_combo()
        # self.make_employee_combo_searchable(self.ui.employee_combo)
        self.ui.btn_extract.clicked.connect(self.on_submit)


    def load_employee_combo(self):
        reporting_to=self.reporting_to
        query=text("select username from users where reporting_to=:reporting_to")
        params={"reporting_to":reporting_to}
        worker=DatabaseWorker((query,params))
        def populate_employee_combo(data):
            if data:
                self.ui.employee_combo.clear()
                self.ui.employee_combo.addItem("All Employees")
                employees=[i[0] for i in data]
                self.ui.employee_combo.addItems(employees)

        def handle_error(error):
            QMessageBox.warning(self,"Error",f"{error}")

        worker.result_ready.connect(populate_employee_combo)
        worker.error_occured.connect(handle_error)
        worker.finished.connect(lambda:self.threads.remove(worker))
        self.threads.append(worker)
        worker.start()


    

    def handle_items(self):
        current_text=self.ui.month_or_week_com.currentText()
        # print("The current text is ",current_text)
        if current_text.lower()=="month":
            # print("im month")
            months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
            self.ui.start_mon_week_combo.clear()
            self.ui.end_month_week_combo.clear()
            self.ui.start_mon_week_combo.addItem("--Select starting month--")
            self.ui.start_mon_week_combo.setCurrentIndex(0)
            self.ui.start_mon_week_combo.model().item(0).setEnabled(False)
            self.ui.end_month_week_combo.addItem("--Select ending month--")
            self.ui.end_month_week_combo.setCurrentIndex(0)
            self.ui.end_month_week_combo.model().item(0).setEnabled(False)
            self.ui.start_mon_week_combo.addItems(months)
            self.ui.end_month_week_combo.addItems(months)
        elif current_text.lower()=="week":
            week=[str(i)for i in range(1,54)]
            self.ui.start_mon_week_combo.clear()
            self.ui.end_month_week_combo.clear()
            self.ui.start_mon_week_combo.addItem("--Select starting week--")
            self.ui.start_mon_week_combo.setCurrentIndex(0)
            self.ui.start_mon_week_combo.model().item(0).setEnabled(False)
            self.ui.end_month_week_combo.addItem("--Select ending week--")
            self.ui.end_month_week_combo.setCurrentIndex(0)
            self.ui.end_month_week_combo.model().item(0).setEnabled(False)
            self.ui.start_mon_week_combo.addItems(week)
            self.ui.end_month_week_combo.addItems(week)

    def on_submit(self):
        filter_by=self.ui.month_or_week_com.currentText()
        starting_mon_week=self.ui.start_mon_week_combo.currentText()
        ending_mon_week=self.ui.end_month_week_combo.currentText()
        self.form_data_submitted.emit(self,filter_by,starting_mon_week,ending_mon_week)
        
    

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
    dialog=Extract_to_Excel()
    dialog.show()
    sys.exit(app.exec())