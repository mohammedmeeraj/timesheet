from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton,QDialog,QMessageBox
import os,mysql.connector,sys

from PyQt6.QtCore import Qt,QSettings
from PyQt6.QtGui import QFontDatabase,QFont
from ui_views.employee import MyEmployee
from ui_views.admin import MyAdmin
from db.db_pool import DatabasePool

from ui_views.login import Login
def resource_path(relative_path):
    if hasattr(sys,'_MEIPASS'):
        return os.path.join(sys._MEIPASS,relative_path)
    return os.path.join(os.path.abspath("."),relative_path)
def load_stylesheet(file_path):
    """Load the QSS stylesheet from the given file path."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error loading stylesheet: {e}")
        return ""
    

def load_fonts():
    font_path=resource_path("assets/fonts/Roboto-Medium.ttf")
    font_id=QFontDatabase.addApplicationFont(font_path)
    if font_id==-1:
        print("Failed to load font")
    else:
        print("fon succsw")

def open_admin_ui(username):
    admin_window=MyAdmin(username)
    admin_window.show()

def open_user_ui(username):
    user=username
    user_window=MyEmployee(user)
    user_window.show()

def check_auto_login():
    
    settings = QSettings("Schueco", "app")
    token = settings.value("login_token", "")
    db_instance=DatabasePool(pool_type="read")

    if token:
        with db_instance.get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                query = "SELECT username, role FROM users WHERE login_token=%s AND token_expiry > NOW()"
                cursor.execute(query, (token,))
                result = cursor.fetchone()

                if result:
                    username, role = result
                    print(f"Auto-login successful for: {username}")

                    if role == "admin":
                        open_admin_ui(username)
                    elif role == "user":
                        open_user_ui(username)
                    # self.accept()
                    return True
            except mysql.connector.Error as err:
                QMessageBox.critical(None, "Database Error", f"An error occurred: {err}")
        
        
    
    return False



QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

app=QApplication(sys.argv)
load_fonts()
# load_fonts()
stylesheet_path=resource_path("assets/styles.qss")
stylesheet=load_stylesheet(stylesheet_path)
app.setStyleSheet(stylesheet)
# load_fonts(app=app)
# if not check_auto_login():
login_dialog=Login()
if not login_dialog.auto_login:
    result=login_dialog.exec()
    if result==QDialog.DialogCode.Accepted:
        print("user authenticated")
        print("The result is ",result)
    else:
        print("The code is ",result)
        sys.exit()


# if result==QDialog.DialogCode.Accepted:
#     print("user authenticated")
#     print("The result is ",result)
# else:
#     print("The code is ",result)

#     sys.exit()

sys.exit(app.exec())