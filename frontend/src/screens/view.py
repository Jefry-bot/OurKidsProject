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
        self.top_bar_frame = QFrame(self.content_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setGeometry(QRect(80, 30, 341, 71))
        self.top_bar_frame.setStyleSheet(u"border: 2px solid white;\n"
"border-top: 0;\n"
"border-left: 0;\n"
"border-right: 0;")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.top_bar_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 321, 51))
        self.label.setStyleSheet(u"border: 0;\n"
"font-size: 60px;\n"
"color: white;\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;")
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(530, 60, 241, 71))
        self.frame.setStyleSheet(u"background-color: rgb(63, 51, 71);\n"
"box-shadow: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 10, 111, 51))
        self.label_2.setStyleSheet(u"border: 0;\n"
"font-size: 40px;\n"
"color: rgb(255, 255, 240);\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;\n"
"text-align: center;")
        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(510, 160, 281, 281))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 20, 241, 101))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.top_bar_frame_2 = QFrame(self.frame_3)
        self.top_bar_frame_2.setObjectName(u"top_bar_frame_2")
        self.top_bar_frame_2.setGeometry(QRect(10, 10, 101, 21))
        self.top_bar_frame_2.setStyleSheet(u"border: 2px solid white;\n"
"border-top: 0;\n"
"border-left: 0;\n"
"border-right: 0;")
        self.top_bar_frame_2.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.top_bar_frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 111, 16))
        self.label_3.setStyleSheet(u"border: 0;\n"
"font-size: 15px;\n"
"color: rgb(255, 255, 240);\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;\n"
"text-align: center;")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 221, 25))
        self.lineEdit.setStyleSheet(u"background-color: none\n"
"")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 130, 241, 101))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.top_bar_frame_3 = QFrame(self.frame_4)
        self.top_bar_frame_3.setObjectName(u"top_bar_frame_3")
        self.top_bar_frame_3.setGeometry(QRect(10, 10, 101, 21))
        self.top_bar_frame_3.setStyleSheet(u"border: 2px solid white;\n"
"border-top: 0;\n"
"border-left: 0;\n"
"border-right: 0;")
        self.top_bar_frame_3.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.top_bar_frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 111, 16))
        self.label_4.setStyleSheet(u"border: 0;\n"
"font-size: 15px;\n"
"color: rgb(255, 255, 240);\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;\n"
"text-align: center;")
        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 50, 221, 25))
        self.lineEdit_2.setStyleSheet(u"background-color: none\n"
"")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 240, 89, 25))
        self.pushButton.setStyleSheet(u"color: white")
        self.frame_5 = QFrame(self.content_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(40, 170, 411, 71))
        self.frame_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.432881, y1:0.415, x2:1, y2:1, stop:0.493812 rgba(45, 186, 188, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 2px solid white")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 20, 401, 31))
        self.label_5.setStyleSheet(u"border: 0;\n"
"background-color: none;\n"
"font-size: 40px;\n"
"color: rgb(255, 230, 255);\n"
"font-family: \"Trebuchet MS\", Verdana, sans-serif;\n"
"text-align: center;")
        self.frame_6 = QFrame(self.content_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(40, 300, 411, 71))
        self.frame_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.274, y1:0.415, x2:1, y2:1, stop:0 rgba(135, 0, 169, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 2px solid white;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 20, 401, 41))
        self.label_6.setStyleSheet(u"border: 0;\n"
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
        self.label.setText(QCoreApplication.translate("Form", u"OurKids", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"About us", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Contact us", None))
    # retranslateUi

