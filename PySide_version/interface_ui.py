# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 550)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Form.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/assets/empty.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"QFrame#frm_bottom {\n"
" margin: 0 0 0 0;\n"
"	border: 2px solid  #021fb3;\n"
"	background-color: #021fb3;\n"
"	border-radius: 30px;\n"
"        border-bottom-left-radius: 0px; /* Square bottom left corner */\n"
"        border-bottom-right-radius: 0px; /* Square bottom right corner */\n"
"padding: 20px\n"
"}\n"
"\n"
"QFrame#frm_top {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLineEdit, QPushButton {\n"
"	color: white;\n"
"	background-color: #2e54e8;\n"
"	border: 2px solid transparent;\n"
"	border-radius: 8px;\n"
"padding: 5px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"		background-color: #3241ff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"		background-color: #2e54e8;\n"
"}\n"
"\n"
"QWidget#Form {\n"
"background-color: white\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.frm_top = QFrame(Form)
        self.frm_top.setObjectName(u"frm_top")
        self.frm_top.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_top.setFrameShadow(QFrame.Shadow.Plain)
        self.frm_top.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frm_top)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_img = QLabel(self.frm_top)
        self.lbl_img.setObjectName(u"lbl_img")
        self.lbl_img.setMinimumSize(QSize(400, 400))
        self.lbl_img.setMaximumSize(QSize(400, 400))
        self.lbl_img.setFrameShape(QFrame.Shape.NoFrame)
        self.lbl_img.setFrameShadow(QFrame.Shadow.Plain)
        self.lbl_img.setLineWidth(0)
        self.lbl_img.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.lbl_img, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frm_top)

        self.frm_bottom = QFrame(Form)
        self.frm_bottom.setObjectName(u"frm_bottom")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_bottom.sizePolicy().hasHeightForWidth())
        self.frm_bottom.setSizePolicy(sizePolicy)
        self.frm_bottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bottom.setFrameShadow(QFrame.Shadow.Raised)
        self.frm_bottom.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frm_bottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_text = QLineEdit(self.frm_bottom)
        self.le_text.setObjectName(u"le_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_text.sizePolicy().hasHeightForWidth())
        self.le_text.setSizePolicy(sizePolicy1)
        self.le_text.setMinimumSize(QSize(300, 40))
        self.le_text.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.le_text)

        self.btn_generate = QPushButton(self.frm_bottom)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setMinimumSize(QSize(90, 40))
        self.btn_generate.setMaximumSize(QSize(80, 40))

        self.horizontalLayout.addWidget(self.btn_generate)

        self.btn_save = QPushButton(self.frm_bottom)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(90, 40))
        self.btn_save.setMaximumSize(QSize(80, 40))

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addWidget(self.frm_bottom)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_img.setText("")
        self.btn_generate.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

