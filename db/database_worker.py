from PyQt6.QtCore import QThread,pyqtSignal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

#create connection pool
# engine=create_engine("mysql+pymysql://Meeraj:Mohammed%26meeraj786@127.0.0.1:3306/timesheet",pool_size=20,max_overflow=5)
engine=create_engine("mysql+pymysql://app_user:Mohammed%26meeraj786@10.95.136.128/timesheet",pool_size=20,max_overflow=5)
Session=sessionmaker(bind=engine)



class DatabaseWorker(QThread):
    result_ready=pyqtSignal(object)
    error_occured=pyqtSignal(str)

    def __init__(self,query, parent = None):
        super().__init__(parent)
        self.query,self.params=query if isinstance(query,tuple) else (query,{})
        self.is_write_operation=False

    def set_write_operation(self,is_write):
        self.is_write_operation=is_write

    def run(self):
        session=Session()
        try:
            if self.is_write_operation:
                session.execute(self.query,self.params)
                session.commit()
                self.result_ready.emit("write operation successfull.")
            else:
                result=session.execute(self.query,self.params).fetchall()
                self.result_ready.emit(result)
        except SQLAlchemyError as e:
            session.rollback()
            self.error_occured.emit(f"Database error: {str(e)}")
        finally:
            session.close()




