# Form implementation generated from reading ui file '..\ui\login.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sys,os
from PyQt6.QtCore import Qt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1049, 563)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.main_widget = QtWidgets.QWidget(parent=Dialog)
        self.main_widget.setObjectName("main_widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.main_widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.image_widget = QtWidgets.QWidget(parent=self.main_widget)
        self.image_widget.setObjectName("image_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.image_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.image_widget)
        self.label.setMaximumSize(QtCore.QSize(744, 563))
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap(":/assets/icons/schiebetueren4-image-data.jpg"))
        self.label.setPixmap(QtGui.QPixmap(self.resource_path("assets/icons/schiebetueren4-image-data.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.image_widget)
        self.body_widget = QtWidgets.QWidget(parent=self.main_widget)
        self.body_widget.setStyleSheet("QLineEdit{\n"
"color: #666;\n"
"font-size: 14px;\n"
"padding: 4px;\n"
"border: 1px solid #ccc;\n"
"border-radius: 2px;\n"
"background-color: #f9f9f9;\n"
"}\n"
"QLineEdit:focus {\n"
"            border: 1px solid #0078d4;\n"
"            background-color: #fff;\n"
"        }")
        self.body_widget.setObjectName("body_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.body_widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border:none;\n"
"margin-right:8px;\n"
"margin-top:8px;")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(":/icons/Close Symbol.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(self.resource_path("assets/icons/Close Symbol.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_8.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.logo = QtWidgets.QLabel(parent=self.body_widget)
        self.logo.setMaximumSize(QtCore.QSize(196, 70))
        self.logo.setText("")
        # self.logo.setPixmap(QtGui.QPixmap(":/assets/icons/Schueco_Logo_RGB_Black.png"))
        self.logo.setPixmap(QtGui.QPixmap(self.resource_path("assets/icons/Schueco_Logo_RGB_Black.png")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        spacerItem3 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(1, -1, -1, -1)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(parent=self.body_widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.username_le = QtWidgets.QLineEdit(parent=self.body_widget)
        self.username_le.setObjectName("username_le")
        self.horizontalLayout_5.addWidget(self.username_le)
        spacerItem7 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.password_le = QtWidgets.QLineEdit(parent=self.body_widget)
        self.password_le.setObjectName("password_le")
        self.horizontalLayout_6.addWidget(self.password_le)
        spacerItem9 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(18, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.show_password_cb = QtWidgets.QCheckBox(parent=self.body_widget)
        self.show_password_cb.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.show_password_cb.setObjectName("show_password_cb")
        self.horizontalLayout_2.addWidget(self.show_password_cb)
        spacerItem10 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(18, -1, -1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.remember_me_cb = QtWidgets.QCheckBox(parent=self.body_widget)
        self.remember_me_cb.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.remember_me_cb.setObjectName("remember_me_cb")
        self.horizontalLayout.addWidget(self.remember_me_cb)
        spacerItem11 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.btn_forgot_pass = QtWidgets.QPushButton(parent=self.body_widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.btn_forgot_pass.setFont(font)
        self.btn_forgot_pass.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_forgot_pass.setStyleSheet("border:none;\n"
"color:#0078d4;")
        self.btn_forgot_pass.setObjectName("btn_forgot_pass")
        self.horizontalLayout.addWidget(self.btn_forgot_pass)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem12 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.btn_login = QtWidgets.QPushButton(parent=self.body_widget)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:4px;\n"
"padding:6px;\n"
"padding-left-10px;\n"
"padding-right:10px;\n"
"padding-top:8px;\n"
"padding-bottom:8px;\n"
"background-color: rgb(31, 149, 239);\n"
"color:white;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1668a7;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_7.addWidget(self.btn_login)
        spacerItem13 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        self.horizontalLayout_9.addWidget(self.body_widget)
        self.horizontalLayout_10.addWidget(self.main_widget)

        self.retranslateUi(Dialog)
        self.pushButton_4.toggled['bool'].connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def resource_path(self,relative_path):
        if getattr(sys, '_MEIPASS', False):
                base_path = sys._MEIPASS
                # print(f"Running in bundled mode. Base path: {base_path}")
        else:
                current_dir=os.path.dirname(os.path.abspath(__file__))
                # base_path = os.path.abspath(os.path.join(current_dir, "..",".."))
                project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
                base_path = os.path.join(project_root)
                
                # print(f"Running in source mode. Base pat: {base_path}")
        full_path = os.path.join(base_path, relative_path)
        # print(f"Resolved path for {relative_path}: {full_path}")
        return full_path
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Login"))
        self.username_le.setPlaceholderText(_translate("Dialog", "Username"))
        self.password_le.setPlaceholderText(_translate("Dialog", "Password"))
        self.show_password_cb.setText(_translate("Dialog", "Show password"))
        self.remember_me_cb.setText(_translate("Dialog", "Remember me"))
        self.btn_forgot_pass.setText(_translate("Dialog", "Forgot Password?"))
        self.btn_login.setText(_translate("Dialog", "LOGIN"))
