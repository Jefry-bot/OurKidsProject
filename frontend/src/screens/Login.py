# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(862, 462)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralWidget = QFrame(Form)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setFrameShape(QFrame.StyledPanel)
        self.centralWidget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.centralWidget)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.636, y1:0.869636, x2:1, y2:1, stop:0.493812 rgba(31, 33, 28, 246), stop:1 rgba(255, 255, 255, 255))")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"background-color: none\n"
"")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.main_logo = QFrame(self.content_frame)
        self.main_logo.setObjectName(u"main_logo")
        self.main_logo.setGeometry(QRect(80, 30, 341, 71))
        self.main_logo.setStyleSheet(u"border: 2px solid white;\n"
"border-top: 0;\n"
"border-left: 0;\n"
"border-right: 0;")
        self.main_logo.setFrameShape(QFrame.StyledPanel)
        self.main_logo.setFrameShadow(QFrame.Raised)
        self.label_logo = QLabel(self.main_logo)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(40, 10, 321, 51))
        self.label_logo.setStyleSheet(u"border: 0;\n"
"font-size: 60px;\n"
"color: white;\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;")
        self.content_login = QFrame(self.content_frame)
        self.content_login.setObjectName(u"content_login")
        self.content_login.setGeometry(QRect(530, 60, 241, 71))
        self.content_login.setStyleSheet(u"background-color: rgb(63, 51, 71);")
        self.content_login.setFrameShape(QFrame.StyledPanel)
        self.content_login.setFrameShadow(QFrame.Raised)
        self.label_login = QLabel(self.content_login)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(70, 10, 111, 51))
        self.label_login.setStyleSheet(u"border: 0;\n"
"font-size: 40px;\n"
"color: rgb(255, 255, 240);\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;\n"
"text-align: center;")
        self.content_form = QFrame(self.content_frame)
        self.content_form.setObjectName(u"content_form")
        self.content_form.setGeometry(QRect(510, 160, 281, 281))
        self.content_form.setFrameShape(QFrame.StyledPanel)
        self.content_form.setFrameShadow(QFrame.Raised)
        self.content_username = QFrame(self.content_form)
        self.content_username.setObjectName(u"content_username")
        self.content_username.setGeometry(QRect(20, 20, 241, 101))
        self.content_username.setFrameShape(QFrame.StyledPanel)
        self.content_username.setFrameShadow(QFrame.Raised)
        self.content_label_username = QFrame(self.content_username)
        self.content_label_username.setObjectName(u"content_label_username")
        self.content_label_username.setGeometry(QRect(10, 10, 101, 21))
        self.content_label_username.setStyleSheet(u"border: 2px solid white;\n"
"border-top: 0;\n"
"border-left: 0;\n"
"border-right: 0;")
        self.content_label_username.setFrameShape(QFrame.StyledPanel)
        self.content_label_username.setFrameShadow(QFrame.Raised)
        self.label_username = QLabel(self.content_label_username)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(10, 0, 111, 16))
        self.label_username.setStyleSheet(u"border: 0;\n"
"font-size: 15px;\n"
"color: rgb(255, 255, 240);\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;\n"
"text-align: center;")
        self.input_username = QLineEdit(self.content_username)
        self.input_username.setObjectName(u"input_username")
        self.input_username.setGeometry(QRect(10, 50, 221, 25))
        self.input_username.setStyleSheet(u"background-color: none\n"
"")
        self.content_password = QFrame(self.content_form)
        self.content_password.setObjectName(u"content_password")
        self.content_password.setGeometry(QRect(20, 130, 241, 101))
        self.content_password.setFrameShape(QFrame.StyledPanel)
        self.content_password.setFrameShadow(QFrame.Raised)
        self.content_label_password = QFrame(self.content_password)
        self.content_label_password.setObjectName(u"content_label_password")
        self.content_label_password.setGeometry(QRect(10, 10, 101, 21))
        self.content_label_password.setStyleSheet(u"border: 2px solid white;\n"
"border-top: 0;\n"
"border-left: 0;\n"
"border-right: 0;")
        self.content_label_password.setFrameShape(QFrame.StyledPanel)
        self.content_label_password.setFrameShadow(QFrame.Raised)
        self.label_password = QLabel(self.content_label_password)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(10, 0, 111, 16))
        self.label_password.setStyleSheet(u"border: 0;\n"
"font-size: 15px;\n"
"color: rgb(255, 255, 240);\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;\n"
"text-align: center;")
        self.input_password = QLineEdit(self.content_password)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(10, 50, 221, 25))
        self.input_password.setStyleSheet(u"background-color: none\n"
"")
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setReadOnly(False)
        self.submit = QPushButton(self.content_form)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(100, 240, 89, 25))
        self.submit.setStyleSheet(u"color: black; border: 1px solid; background: white;")
        self.label_verify = QLabel(self.content_form)
        self.label_verify.setObjectName(u"label_verify")
        self.label_verify.setGeometry(QRect(200, 250, 67, 17))
        self.label_verify.setStyleSheet(u"color: green;")
        self.content_about = QFrame(self.content_frame)
        self.content_about.setObjectName(u"content_about")
        self.content_about.setGeometry(QRect(40, 170, 411, 71))
        self.content_about.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.432881, y1:0.415, x2:1, y2:1, stop:0.493812 rgba(45, 186, 188, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 2px solid white")
        self.content_about.setFrameShape(QFrame.StyledPanel)
        self.content_about.setFrameShadow(QFrame.Raised)
        self.label_about = QLabel(self.content_about)
        self.label_about.setObjectName(u"label_about")
        self.label_about.setGeometry(QRect(110, 20, 401, 31))
        self.label_about.setStyleSheet(u"border: 0;\n"
"background-color: none;\n"
"font-size: 40px;\n"
"color: rgb(255, 230, 255);\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;\n"
"text-align: center;")
        self.content_contact = QFrame(self.content_frame)
        self.content_contact.setObjectName(u"content_contact")
        self.content_contact.setGeometry(QRect(40, 300, 411, 71))
        self.content_contact.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.274, y1:0.415, x2:1, y2:1, stop:0 rgba(135, 0, 169, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 2px solid white;")
        self.content_contact.setFrameShape(QFrame.StyledPanel)
        self.content_contact.setFrameShadow(QFrame.Raised)
        self.label_contact = QLabel(self.content_contact)
        self.label_contact.setObjectName(u"label_contact")
        self.label_contact.setGeometry(QRect(100, 20, 401, 41))
        self.label_contact.setStyleSheet(u"border: 0;\n"
"background-color: none;\n"
"font-size: 40px;\n"
"color: rgb(255, 230, 255);\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;\n"
"text-align: center;")

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.centralWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_logo.setText(QCoreApplication.translate("Form", u"OurKids", None))
        self.label_login.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_username.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.input_password.setPlaceholderText("")
        self.submit.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.label_verify.setText("")
        self.label_about.setText(QCoreApplication.translate("Form", u"About us", None))
        self.label_contact.setText(QCoreApplication.translate("Form", u"Contact us", None))
    # retranslateUi

