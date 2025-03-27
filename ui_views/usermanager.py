from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import pyqtSlot
from db.database_worker import DatabaseWorker
from sqlalchemy.sql import text
from db.db import GetCursor

class UserManager:
    def __init__(self,parent=None):
        self.parent=parent

    def validate_data(self,create_user_ob,username,employee_id,email,password,repeat_password,role,reporting_to):
        if password != repeat_password:
            return False,"Passwords do not match"
        
        if not email.endswith(("@schueco.in","@schueco.com")): 
            return False,"Email must be a company email."

        if role.lower() not in ["user","admin"]:
            return False, "Please select role"
        
        if not reporting_to:
            return False, "Reporting admin must be selected!"

        return True, "Validation successful!"
    
    def check_user_existence(self,create_user_ob,username,employee_id,email,password,role,reporting_to):
        query=text("select count(*) from users where username=:username or email=:email")
        params={"username":username,"email":email}
        self.user_check_worker=DatabaseWorker((query,params),self.parent)
        self.user_check_worker.result_ready.connect(lambda result:self.handle_user_existence_result(create_user_ob,result,username,employee_id,email,password,role,reporting_to))
        self.user_check_worker.start()

    @pyqtSlot(object)
    def handle_user_existence_result(self,create_user_ob,result,username,employee_id,email,password,role,reporting_to):
        count=result[0][0]
        if count>0:
            QMessageBox.warning(self.parent,"Validation Error","User already exists!")
        else:
            self.insert_user(create_user_ob,username,employee_id,email,password,role,reporting_to)

    def insert_user(self,create_user_ob,username,employee_id,email,password,role,reporting_to):
        emp_id=int(employee_id)
        # query=text("insert into users(username,email,password,role,reporting_to) values(:username,:email,:password,:role,:reporting_to)")
        # params={
        #     "username":username,
        #     "email":email,
        #     "password":password,
        #     "role":role,
        #     "reporting_to":reporting_to,
        # }
        # self.worker=DatabaseWorker((query,params),self.parent)
        # self.worker.result_ready.connect(lambda result:self.handle_insert_result(result))
        # self.worker.start()
        db=GetCursor()
        if db.conn and db.cursor:
            query="insert into users(username,user_id,email,password,role,reporting_to) values(%s,%s,%s,%s,%s,%s)"
            values=(username,emp_id,email,password,role,reporting_to)
            db.cursor.execute(query,values)
            db.conn.commit()
            if db.cursor.rowcount>0:
                create_user_ob.accept()
                QMessageBox.information(self.parent,"Success","User created successfully!")
            else:
                QMessageBox.information(self.parent,"Failed","Failed!")
        db.close_connection()


            



    # @pyqtSlot(object)
    # def handle_insert_result(self,result):
    #     QMessageBox.information(self.parent,"Success","User created successfully!")