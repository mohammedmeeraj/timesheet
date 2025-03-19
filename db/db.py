import mysql.connector as mc
class GetCursor:
    def __init__(self):
        self.conn=None
        self.cursor=None
        self.connect_to_db()
    def connect_to_db(self):
        try:
            # self.conn=mc.connect(host="localhost",user="Meeraj",password="Mohammed&meeraj786",database="timesheet",port=3306)
            self.conn=mc.connect(host="10.95.136.128",user="app_user",password="Mohammed&meeraj786",database="timesheet")
            self.cursor=self.conn.cursor()
        except mc.Error:
            print("Error occured")
            self.conn=None
            self.cursor=None
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            