# Form implementation generated from reading ui file '.\edit_project.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(343, 209)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setStyleSheet("QLineEdit{\n"
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
"        }\n"
"\n"
"QLabel {\n"
"   \n"
"    font-size: 12px;                    /* Medium font size */\n"
"\n"
"    color: #333;                        /* Dark gray color */\n"
"    margin-bottom: 5px;                 /* Spacing below the label */\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"border-radius:4px;\n"
"background-color:rgb(31, 149, 239);\n"
"color:white;\n"
"padding-right:14px;\n"
"padding-left:14px;\n"
"padding-top:8px;\n"
"padding-bottom:8px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1977bf;\n"
"\n"
"\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.header_widget = QtWidgets.QWidget(parent=self.widget)
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.header_widget)
        self.label.setStyleSheet("background-color:rgb(31, 149, 239);\n"
"color:white;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.gridLayout_2.addWidget(self.header_widget, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.edit_project_name_le = QtWidgets.QLineEdit(parent=self.widget)
        self.edit_project_name_le.setObjectName("edit_project_name_le")
        self.horizontalLayout.addWidget(self.edit_project_name_le)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(24)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.edit_psp_element_le = QtWidgets.QLineEdit(parent=self.widget)
        self.edit_psp_element_le.setObjectName("edit_psp_element_le")
        self.horizontalLayout_3.addWidget(self.edit_psp_element_le)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.edit_push_btn = QtWidgets.QPushButton(parent=self.widget)
        self.edit_push_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit_push_btn.setCheckable(True)
        self.edit_push_btn.setObjectName("edit_push_btn")
        self.horizontalLayout_4.addWidget(self.edit_push_btn)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color:#cc0000;\n"
"\n"
"border-top-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton_2.toggled['bool'].connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Edit Project"))
        self.label_2.setText(_translate("Dialog", "Project Name"))
        self.label_4.setText(_translate("Dialog", "PSP Element"))
        self.edit_push_btn.setText(_translate("Dialog", "Edit"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
