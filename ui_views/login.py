from ui.py.login_dialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QApplication,QMessageBox,QLineEdit
from PyQt6.QtGui import QRegion
from PyQt6.QtCore import Qt,QPoint,QRect,pyqtSignal,QMetaObject,Q_ARG,pyqtSlot,QSettings
import mysql.connector
from mysql.connector import pooling
import sys,random,smtplib,os,pytz
from email.mime.text import MIMEText
from .admin import MyAdmin
from .employee import MyEmployee
import uuid,requests
from sqlalchemy.sql import text
from .verify_email import VerifyEmail
import datetime,socket,subprocess,platform
from db.database_worker import DatabaseWorker
from .forgot_password import Forgot_Password
from db.db_pool import DatabasePool
class Login(QDialog):
    form_data_submitted=pyqtSignal(str,str)
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.auto_login=False
        if not self.check_auto_login():
            self.ui.setupUi(self)
            self.threads=[]
            self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            self._is_dragging = False
            self._drag_start_position = QPoint()
            self.ui.btn_login.clicked.connect(self.on_submit)
            self.ui.username_le.returnPressed.connect(self.on_submit)
            self.ui.password_le.returnPressed.connect(self.on_submit)
            self.ui.password_le.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.show_password_cb.stateChanged.connect(self.toggle_password_visibility)
            self.ui.btn_forgot_pass.clicked.connect(self.show_reset_pass_dialog)
            self.load_saved_credentials()
            self.create_db_pool()
        # self.ui.btn_forgot_password.clicked.connect(self.open_verify_email_dialog)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    
    def load_saved_credentials(self):
        settings=QSettings("Schueco","app")
        saved_username=settings.value("username","")
        saved_password=settings.value("password","")
        self.ui.username_le.setText(saved_username)
        self.ui.password_le.setText(saved_password)
        if saved_username and saved_password:
            self.ui.remember_me_cb.setChecked(True)

    def show_reset_pass_dialog(self):
        dialog=Forgot_Password()
        dialog.form_data_submitted.connect(self.verify_username)
        dialog.exec()
    def verify_username(self,obj,username):
        # print("The username is", username)

        query1 = text("SELECT reporting_to FROM users WHERE binary username = :username")
        params1 = {"username": username}

        worker1 = DatabaseWorker((query1, params1))
        worker1.result_ready.connect(lambda result: self.handle_reporting_to(result, username,obj))
        worker1.error_occured.connect(self.handle_error)
        worker1.finished.connect(lambda:self.threads.remove(worker1))
        self.threads.append(worker1)
        worker1.start()
    def handle_reporting_to(self, result, username,obj):
        if not result:
            QMessageBox.warning(self, "User Not Found", "The username does not exist.")
            return

        reporting_to = result[0][0]  # Extract reporting_to

        # Step 2: Check if username already exists in reset_password table
        query2 = text("SELECT 1 FROM password_reset WHERE username = :username")
        params2 = {"username": username}

        worker2 = DatabaseWorker((query2, params2))
        worker2.result_ready.connect(lambda check_result: self.handle_check_reset_request(check_result, username, reporting_to,obj))
        worker2.error_occured.connect(self.handle_error)
        worker2.finished.connect(lambda:self.threads.remove(worker2))
        self.threads.append(worker2)
        worker2.start()
    def handle_check_reset_request(self, result, username, reporting_to,obj):
        if result:
            QMessageBox.warning(self, "Request Already Exists", "You have already sent a password reset request. Please wait for the admin to reset your password.")
            obj.close()
            return

        # Step 3: Insert username and reporting_to into reset_password table
        query3 = text("INSERT INTO password_reset (username, reporting_to) VALUES (:username, :reporting_to)")
        params3 = {"username": username, "reporting_to": reporting_to}

        worker3 = DatabaseWorker((query3, params3))
        worker3.set_write_operation(True)
        worker3.result_ready.connect(lambda result:self.close_window(result,obj) )
        worker3.error_occured.connect(self.handle_error)
        worker3.finished.connect(lambda:self.threads.remove(worker3))
        self.threads.append(worker3)
        worker3.start() 

    def close_window(self,result,obj):
        QMessageBox.information(self, "Success", "Password reset request submitted successfully.")
        obj.close()



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
    def toggle_password_visibility(self):
        if self.ui.show_password_cb.isChecked():
            self.ui.password_le.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.password_le.setEchoMode(QLineEdit.EchoMode.Password)
    def create_db_pool(self):
        db_config={
            "host":"10.95.136.128",
            "user":"app_user",
            "password":"Mohammed&meeraj786",
            "database":"timesheet"

        }
        self.db_pool=pooling.MySQLConnectionPool(pool_name="mypool", pool_size=15, **db_config)
    def get_db_connection(self):
        return self.db_pool.get_connection()
    # def on_submit(self):
    #     username=self.ui.username_le.text()
    #     password=self.ui.password_le.text()
    #     self.username=username
    #     try:
    #         conn=mysql.connector.connect(
    #             # host="127.0.0.1",
    #             # user="Meeraj",
    #             # password="Mohammed&meeraj786",
    #             # database="timesheet"
    #             host="10.95.136.128",
    #             user="app_user",
    #             password="Mohammed&meeraj786",
    #             database="timesheet"
    #         )
    #         cursor=conn.cursor()
    #         query="Select role from users where binary username=%s and binary password=%s"
    #         cursor.execute(query,(username,password))
    #         result=cursor.fetchone()
    #         # print(result)
    #         if result:
    #             role=result[0]
    #             # print("The role is ",role)
    #             if self.ui.remember_me_cb.isChecked():
    #                 settings=QSettings("Schueco","app")
    #                 settings.setValue("username",username)
    #                 settings.setValue("password",password)
    #             else:
    #                 settings=QSettings("Schueco","app")
    #                 settings.remove("username")
    #                 settings.remove("password")

    #             if role=="admin":
    #                 self.open_admin_ui()
    #             elif role=="user":
    #                 self.open_user_ui()
    #             self.accept()
                
    #         else:
    #             QMessageBox.warning(self,"Login Failed","Invalid username or password.")
    #     except mysql.connector.Error as err:
    #         conn.rollback()
    #         QMessageBox.critical(self,"Database Error",f"An error occured: {err}")
    #     finally:
    #         if conn.is_connected():
    #             cursor.close()
    #             conn.close()
    # def on_submit(self):
    #     username=self.ui.username_le.text()
    #     password=self.ui.password_le.text()
    #     self.username=username
    #     conn=self.get_db_connection()
    #     cursor=conn.cursor()
    #     try:
    #         query="Select role from users where binary username=%s and binary password=%s"
    #         cursor.execute(query,(username,password))
    #         result=cursor.fetchone()
    #         if result:
    #             role=result[0]
    #             # print("The role is ",role)
    #             if self.ui.remember_me_cb.isChecked():
    #                 settings=QSettings("Schueco","app")
    #                 settings.setValue("username",username)
    #                 settings.setValue("password",password)
    #             else:
    #                 settings=QSettings("Schueco","app")
    #                 settings.remove("username")
    #                 settings.remove("password")

    #             if role=="admin":
    #                 self.open_admin_ui()
    #             elif role=="user":
    #                 login_time,ip_address,wifi_name=self.get_login_details()
    #                 usernamee=os.getlogin()
    #                 print("The username is ",usernamee)
    #                 print("The login time is ",login_time)
    #                 print("The ipaddress is ",ip_address)
    #                 print("The wifi name is ",wifi_name)
    #                 self.open_user_ui()
    #             self.accept()
    #         else:
    #             QMessageBox.warning(self,"Login Failed","Invalid username or password.")
    #     except mysql.connector.Error as err:
    #         conn.rollback()
    #         QMessageBox.critical(self,"Database Error",f"An error occured: {err}")
    #     finally:
    #         cursor.close()
    #         conn.close()

    def check_auto_login(self):
        settings = QSettings("Schueco", "app")
        token = settings.value("login_token", "")
        # print("The token is ",token)
        db_instance=DatabasePool(pool_type="read")

        if token:
            with db_instance.get_db_connection() as conn:
                cursor = conn.cursor()
                try:
                    query = "SELECT username, role FROM users WHERE login_token=%s AND token_expiry > NOW()"
                    cursor.execute(query, (token,))
                    result = cursor.fetchone()
                    print("The result is ",result)
                    query="Select NOW()"
                    cursor.execute(query)
                    time=cursor.fetchone()[0]
                    print("The time is ",time)

                    if result:
                        username, role = result
                        print("The username is ",username)
                        print("The role is ",role)
                        self.username=username
                        print(f"Auto-login successful for: {username}")
                        self.auto_login=True
                        if role == "admin":
                            self.open_admin_ui()
                        elif role == "user":
                            self.open_user_ui()
                        self.accept()
                        return True
                except mysql.connector.Error as err:
                    print(f"The error is ",err)
                    QMessageBox.critical(self, "Database Error", f"An error occurred: {err}")
        return False
    
    def on_submit(self):
        db_instance=DatabasePool(pool_type="read")
        username=self.ui.username_le.text()
        password=self.ui.password_le.text()
        self.username=username
        with db_instance.get_db_connection() as conn:
            cursor=conn.cursor()
            try:
                query="Select role from users where binary username=%s and binary password=%s"
                cursor.execute(query,(username,password))
                result=cursor.fetchone()
                if result:
                    role=result[0]
                    token=str(uuid.uuid4())
                    utc_timezone = pytz.utc
                    # expiration_time=datetime.datetime.now().replace(microsecond=0)+datetime.timedelta(minutes=1)
                    expiration_time=datetime.datetime.now().replace(microsecond=0)+datetime.timedelta(minutes=1)
                    print("The expiration date is ",expiration_time)
                    update_query="update users set login_token=%s,token_expiry=%s where username=%s"
                    cursor.execute(update_query,(token,expiration_time,username))
                    conn.commit()
                    print("Token saved")
                    settings=QSettings("Schueco","app")
                    settings.setValue("login_token",token)
                    if self.ui.remember_me_cb.isChecked():
                        settings.setValue("username",username)
                        settings.setValue("password",password)
                    else:
                        settings.remove("username")
                        settings.remove("password")

                    if role=="admin":
                        # login_time,ip_address,wifi_name,login_date,day_name=self.get_login_details()
                        # system_user=os.getlogin()
                        # self.push_logs_to_db(login_time,wifi_name,login_date,day_name,system_user,username)
                        # print("The username is ",system_user)
                        # print("The login time is ",login_time)
                        # print("The ipaddress is ",ip_address)
                        # print("The wifi name is ",wifi_name)
                        # print("The date is ",login_date)
                        # print("The day name is ",day_name)
                        self.open_admin_ui()
                    elif role=="user":
                        # login_time,ip_address,wifi_name,login_date,day_name=self.get_login_details()
                        # system_user=os.getlogin()
                        # self.push_logs_to_db(login_time,wifi_name,login_date,day_name,system_user,username)
                        # print("The username is ",system_user)
                        # print("The login time is ",login_time)
                        # print("The ipaddress is ",ip_address)
                        # print("The wifi name is ",wifi_name)
                        # print("The login date is ",login_date)
                        # print("The day name is ",day_name)
                        self.open_user_ui()
                    self.accept()
                else:
                    QMessageBox.warning(self,"Login Failed","Invalid username or password.")
            except mysql.connector.Error as err:
                conn.rollback()
                QMessageBox.critical(self,"Database Error",f"An error occured: {err}")
        
    def push_logs_to_db(self,login_time,wifi_name,login_date,day_name,system_user,username):
        db_instance=DatabasePool(pool_type="write")
        with db_instance.get_db_connection() as conn:
            cursor=conn.cursor()
            try:
                query="select user_id from users where binary username=%s"
                cursor.execute(query,(username,))
                user_id=cursor.fetchone()[0]
                query="insert into user_logs(employee_id,employee_name,username,login_time,wifi_name,login_date,day_name) values(%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query,(user_id,username,system_user,login_time,wifi_name,login_date,day_name))
                conn.commit()
            except mysql.connector.errors.IntegrityError as e:
                if e.errno==1062:
                    pass
                else:
                    print(f"Database error")
            except mysql.connector.Error as err:
                conn.rollback()
                # pass
                QMessageBox.critical(self,"Database Error",f"An error occured: {err}")
            
            

    def get_login_details(self):
        # login_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        login_time=datetime.datetime.now().strftime("%H:%M:%S")
        login_date=datetime.datetime.now().strftime("%Y-%m-%d")
        date_obj=datetime.datetime.strptime(login_date,"%Y-%m-%d")
        day_name=date_obj.strftime("%A")
        try:
            hostname=socket.gethostname()
            ipaddress=socket.gethostbyname(hostname)
        except Exception as e:
            ipaddress=f"Error: {e}"
            print(ipaddress)
        #Get Wifi Name
        wifi_name="Unknown"
        if platform.system()=="Windows":
            try:
                result=subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
                for line in result.stdout.split("\n"):
                    if "SSID" in line:
                        wifi_name=line.split(":")[1].strip()
                        break
            except Exception as e:
                wifi_name=f"Error: {e}"
        return login_time,ipaddress,wifi_name,login_date,day_name
    
    
    

        






        
        
    # @pyqtSlot(list)
    # def process_login_result(self,data):
    #         print("the data is here is the data",data)
    #         if data and isinstance(data,list) and len(data)>0 and len(data[0])>0:
    #             role=data[0][0]
    #             print("The role is ",role)
    #             self.accept()
    #             if role=="admin":
    #                 self.open_admin_ui()
    #             elif role=="user":
    #                 self.open_user_ui()

    #         else:
    #             QMessageBox.warning(self,"Login failed","Invalid username or password.")
    # def on_submit(self):
    #     username=self.ui.username_le.text()
    #     password=self.ui.password_le.text()
    #     self.username=username
    #     if not username or not password:
    #         QMessageBox.warning(self,"Validation Error","Username and password cannot be empty.")
    #         return
        
    #     query=text("Select role from users where username=:username and password=:password")
    #     params={"username":username,"password":password}
    #     worker=DatabaseWorker((query,params))
    #     def handle_validation(data):
    #         print("being hit",data)
    #         self.process_login_result(data)
        
    #     worker.result_ready.connect(handle_validation)
    #     worker.error_occured.connect(self.handle_error)
    #     worker.finished.connect(lambda:self.threads.remove(worker))
    #     self.threads.append(worker)
    #     worker.start()
        
    def handle_error(self,error):
        QMessageBox.warning(self,"Error",f"{error}")
    def open_admin_ui(self):
        self.admin_window=MyAdmin(self.username)
        self.admin_window.show()

    def open_user_ui(self):
        user=self.username
        self.user_window=MyEmployee(user)
        self.user_window.show()

def load_stylesheet(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error loading stylesheet: {e}")
        return ""
    
# if __name__=="__main__":
#     app=QApplication(sys.argv)
#     stylesheet=load_stylesheet("styles.qss")
#     app.setStyleSheet(stylesheet)
#     dialog=Login()
#     dialog.show()
#     sys.exit(app.exec())