################################################################################
##
## STUDY PROJECT BY: WANDERSON M.
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 0.1
##
################################################################################

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
# IMPORT IMAGES FILE
import files_rc
# IMPORT QSS
from styles import *

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        #
        # MAIN WINDOW PARAMETERS
        # CHANGE "MainWindow" TO "self"
        #

        self.setObjectName("MainWindow")
        self.resize(350, 600)
        self.setMinimumSize(QtCore.QSize(350, 600))
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICO/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet(style.mainWindow)
        self.centralwidget = QtWidgets.QWidget(self)

        #
        # START GUI SCRIPT
        #
        ############################################################################################

        # START --- WIDGETS
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setStyleSheet(u"margin: 0px; background-color: rgb(35, 35, 35);")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_principal)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_topMenu = QFrame(self.frame_principal)
        self.frame_topMenu.setObjectName(u"frame_topMenu")
        self.frame_topMenu.setMaximumSize(QSize(16777215, 70))
        self.frame_topMenu.setStyleSheet(u"background-color: transparent;")
        self.frame_topMenu.setFrameShape(QFrame.StyledPanel)
        self.frame_topMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_topMenu)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame_17 = QFrame(self.frame_topMenu)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: transparent;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_17)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_title = QLabel(self.frame_17)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout_4.addWidget(self.label_title)
        self.horizontalLayout_3.addWidget(self.frame_17)
        self.frame_18 = QFrame(self.frame_topMenu)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(170, 16777215))
        self.frame_18.setStyleSheet(u"background-color: transparent;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_18)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_minimize = QPushButton(self.frame_18)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        self.pushButton_minimize.setMinimumSize(QSize(50, 50))
        self.pushButton_minimize.setMaximumSize(QSize(50, 50))
        self.pushButton_minimize.setStyleSheet(style.bts_title_bar_minimize)
        self.horizontalLayout.addWidget(self.pushButton_minimize)
        self.pushButton_max_rest = QPushButton(self.frame_18)
        self.pushButton_max_rest.setObjectName(u"pushButton_max_rest")
        self.pushButton_max_rest.setMinimumSize(QSize(50, 50))
        self.pushButton_max_rest.setMaximumSize(QSize(50, 50))
        self.pushButton_max_rest.setStyleSheet(style.bts_title_bar_maximize)
        self.horizontalLayout.addWidget(self.pushButton_max_rest)
        self.pushButton_close = QPushButton(self.frame_18)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(50, 50))
        self.pushButton_close.setMaximumSize(QSize(50, 50))
        self.pushButton_close.setStyleSheet(style.bts_title_bar_close)
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.horizontalLayout_3.addWidget(self.frame_18)
        self.verticalLayout_2.addWidget(self.frame_topMenu)
        self.frame_labelTemp = QFrame(self.frame_principal)
        self.frame_labelTemp.setObjectName(u"frame_labelTemp")
        self.frame_labelTemp.setMaximumSize(QSize(16777215, 35))
        self.frame_labelTemp.setStyleSheet(u"background-color: transparent;")
        self.frame_labelTemp.setFrameShape(QFrame.StyledPanel)
        self.frame_labelTemp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_labelTemp)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(15, 0, 15, 0)
        self.label_temp = QLabel(self.frame_labelTemp)
        self.label_temp.setObjectName(u"label_temp")
        self.label_temp.setStyleSheet(u"background-color: transparent;")
        self.label_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.verticalLayout_5.addWidget(self.label_temp)
        self.verticalLayout_2.addWidget(self.frame_labelTemp)
        self.frame_lineEdit = QFrame(self.frame_principal)
        self.frame_lineEdit.setObjectName(u"frame_lineEdit")
        self.frame_lineEdit.setMaximumSize(QSize(16777215, 100))
        self.frame_lineEdit.setStyleSheet(u"background-color: rgba(255, 0, 127, 230); border-radius: 0px; margin: 5px; border-radius: 10px;")
        self.frame_lineEdit.setFrameShape(QFrame.StyledPanel)
        self.frame_lineEdit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_lineEdit)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_values = QLineEdit(self.frame_lineEdit)
        self.lineEdit_values.setObjectName(u"lineEdit_values")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_values.sizePolicy().hasHeightForWidth())
        self.lineEdit_values.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Roboto Light")
        font1.setPointSize(42)
        self.lineEdit_values.setFont(font1)
        self.lineEdit_values.setStyleSheet(u"color: rgb(255, 255, 255); selection-background-color: rgb(213, 0, 106); background-color: transparent;")
        self.lineEdit_values.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.lineEdit_values)
        self.verticalLayout_2.addWidget(self.frame_lineEdit)
        self.frame_buttons = QFrame(self.frame_principal)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setStyleSheet(u"background-color: transparent;")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_buttons)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.frame_19 = QFrame(self.frame_buttons)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_19)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bt_8 = QPushButton(self.frame_19)
        self.bt_8.setObjectName(u"bt_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bt_8.sizePolicy().hasHeightForWidth())
        self.bt_8.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Roboto Light")
        font2.setPointSize(22)
        self.bt_8.setFont(font2)
        self.bt_8.setStyleSheet(style.bts_numbers)
        self.verticalLayout_8.addWidget(self.bt_8)
        self.gridLayout.addWidget(self.frame_19, 1, 3, 1, 1)
        self.frame_7 = QFrame(self.frame_buttons)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bt_9 = QPushButton(self.frame_7)
        self.bt_9.setObjectName(u"bt_9")
        sizePolicy1.setHeightForWidth(self.bt_9.sizePolicy().hasHeightForWidth())
        self.bt_9.setSizePolicy(sizePolicy1)
        self.bt_9.setFont(font2)
        self.bt_9.setStyleSheet(style.bts_numbers)
        self.verticalLayout_16.addWidget(self.bt_9)
        self.gridLayout.addWidget(self.frame_7, 1, 4, 1, 1)
        self.frame_9 = QFrame(self.frame_buttons)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.bt_4 = QPushButton(self.frame_9)
        self.bt_4.setObjectName(u"bt_4")
        sizePolicy1.setHeightForWidth(self.bt_4.sizePolicy().hasHeightForWidth())
        self.bt_4.setSizePolicy(sizePolicy1)
        self.bt_4.setFont(font2)
        self.bt_4.setStyleSheet(style.bts_numbers)
        self.verticalLayout_13.addWidget(self.bt_4)
        self.gridLayout.addWidget(self.frame_9, 2, 2, 1, 1)
        self.frame_10 = QFrame(self.frame_buttons)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.bt_5 = QPushButton(self.frame_10)
        self.bt_5.setObjectName(u"bt_5")
        sizePolicy1.setHeightForWidth(self.bt_5.sizePolicy().hasHeightForWidth())
        self.bt_5.setSizePolicy(sizePolicy1)
        self.bt_5.setFont(font2)
        self.bt_5.setStyleSheet(style.bts_numbers)
        self.verticalLayout_14.addWidget(self.bt_5)
        self.gridLayout.addWidget(self.frame_10, 2, 3, 1, 1)
        self.frame_15 = QFrame(self.frame_buttons)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.bt_3 = QPushButton(self.frame_15)
        self.bt_3.setObjectName(u"bt_3")
        sizePolicy1.setHeightForWidth(self.bt_3.sizePolicy().hasHeightForWidth())
        self.bt_3.setSizePolicy(sizePolicy1)
        self.bt_3.setFont(font2)
        self.bt_3.setStyleSheet(style.bts_numbers)
        self.verticalLayout_12.addWidget(self.bt_3)
        self.gridLayout.addWidget(self.frame_15, 3, 4, 1, 1)
        self.frame_13 = QFrame(self.frame_buttons)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bt_1 = QPushButton(self.frame_13)
        self.bt_1.setObjectName(u"bt_1")
        sizePolicy1.setHeightForWidth(self.bt_1.sizePolicy().hasHeightForWidth())
        self.bt_1.setSizePolicy(sizePolicy1)
        self.bt_1.setFont(font2)
        self.bt_1.setStyleSheet(style.bts_numbers)
        self.verticalLayout_10.addWidget(self.bt_1)
        self.gridLayout.addWidget(self.frame_13, 3, 2, 1, 1)
        self.frame_14 = QFrame(self.frame_buttons)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bt_2 = QPushButton(self.frame_14)
        self.bt_2.setObjectName(u"bt_2")
        sizePolicy1.setHeightForWidth(self.bt_2.sizePolicy().hasHeightForWidth())
        self.bt_2.setSizePolicy(sizePolicy1)
        self.bt_2.setFont(font2)
        self.bt_2.setStyleSheet(style.bts_numbers)
        self.verticalLayout_11.addWidget(self.bt_2)
        self.gridLayout.addWidget(self.frame_14, 3, 3, 1, 1)
        self.frame_11 = QFrame(self.frame_buttons)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bt_6 = QPushButton(self.frame_11)
        self.bt_6.setObjectName(u"bt_6")
        sizePolicy1.setHeightForWidth(self.bt_6.sizePolicy().hasHeightForWidth())
        self.bt_6.setSizePolicy(sizePolicy1)
        self.bt_6.setFont(font2)
        self.bt_6.setStyleSheet(style.bts_numbers)
        self.verticalLayout_15.addWidget(self.bt_6)
        self.gridLayout.addWidget(self.frame_11, 2, 4, 1, 1)
        self.frame_12 = QFrame(self.frame_buttons)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_12)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bt_plus = QPushButton(self.frame_12)
        self.bt_plus.setObjectName(u"bt_plus")
        sizePolicy1.setHeightForWidth(self.bt_plus.sizePolicy().hasHeightForWidth())
        self.bt_plus.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamily(u"Roboto Light")
        font3.setPointSize(20)
        self.bt_plus.setFont(font3)
        self.bt_plus.setStyleSheet(style.bts_functions)
        self.verticalLayout_22.addWidget(self.bt_plus)
        self.gridLayout.addWidget(self.frame_12, 2, 5, 1, 1)
        self.frame_8 = QFrame(self.frame_buttons)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.bt_minus = QPushButton(self.frame_8)
        self.bt_minus.setObjectName(u"bt_minus")
        sizePolicy1.setHeightForWidth(self.bt_minus.sizePolicy().hasHeightForWidth())
        self.bt_minus.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(30)
        self.bt_minus.setFont(font4)
        self.bt_minus.setStyleSheet(style.bts_functions)
        self.verticalLayout_21.addWidget(self.bt_minus)
        self.gridLayout.addWidget(self.frame_8, 1, 5, 1, 1)
        self.frame_5 = QFrame(self.frame_buttons)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bt_7 = QPushButton(self.frame_5)
        self.bt_7.setObjectName(u"bt_7")
        sizePolicy1.setHeightForWidth(self.bt_7.sizePolicy().hasHeightForWidth())
        self.bt_7.setSizePolicy(sizePolicy1)
        self.bt_7.setFont(font2)
        self.bt_7.setStyleSheet(style.bts_numbers)
        self.verticalLayout_7.addWidget(self.bt_7)
        self.gridLayout.addWidget(self.frame_5, 1, 2, 1, 1)
        self.frame_2 = QFrame(self.frame_buttons)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bt_backspace = QPushButton(self.frame_2)
        self.bt_backspace.setObjectName(u"bt_backspace")
        sizePolicy1.setHeightForWidth(self.bt_backspace.sizePolicy().hasHeightForWidth())
        self.bt_backspace.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamily(u"Roboto Light")
        font5.setPointSize(15)
        self.bt_backspace.setFont(font5)
        self.bt_backspace.setStyleSheet(style.bts_backspace)
        self.verticalLayout_18.addWidget(self.bt_backspace)
        self.gridLayout.addWidget(self.frame_2, 0, 3, 1, 1)
        self.frame_1 = QFrame(self.frame_buttons)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bt_clear = QPushButton(self.frame_1)
        self.bt_clear.setObjectName(u"bt_clear")
        sizePolicy1.setHeightForWidth(self.bt_clear.sizePolicy().hasHeightForWidth())
        self.bt_clear.setSizePolicy(sizePolicy1)
        self.bt_clear.setFont(font5)
        self.bt_clear.setStyleSheet(style.bts_functions)
        self.verticalLayout_3.addWidget(self.bt_clear)
        self.gridLayout.addWidget(self.frame_1, 0, 2, 1, 1)
        self.frame_3 = QFrame(self.frame_buttons)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_3)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.bt_div = QPushButton(self.frame_3)
        self.bt_div.setObjectName(u"bt_div")
        sizePolicy1.setHeightForWidth(self.bt_div.sizePolicy().hasHeightForWidth())
        self.bt_div.setSizePolicy(sizePolicy1)
        self.bt_div.setFont(font3)
        self.bt_div.setStyleSheet(style.bts_functions)
        self.verticalLayout_19.addWidget(self.bt_div)
        self.gridLayout.addWidget(self.frame_3, 0, 4, 1, 1)
        self.frame_4 = QFrame(self.frame_buttons)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_4)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.bt_multiply = QPushButton(self.frame_4)
        self.bt_multiply.setObjectName(u"bt_multiply")
        sizePolicy1.setHeightForWidth(self.bt_multiply.sizePolicy().hasHeightForWidth())
        self.bt_multiply.setSizePolicy(sizePolicy1)
        self.bt_multiply.setFont(font5)
        self.bt_multiply.setStyleSheet(style.bts_functions)
        self.verticalLayout_20.addWidget(self.bt_multiply)
        self.gridLayout.addWidget(self.frame_4, 0, 5, 1, 1)
        self.frame_6 = QFrame(self.frame_buttons)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_6)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.bt_copy = QPushButton(self.frame_6)
        self.bt_copy.setObjectName(u"bt_copy")
        sizePolicy1.setHeightForWidth(self.bt_copy.sizePolicy().hasHeightForWidth())
        self.bt_copy.setSizePolicy(sizePolicy1)
        self.bt_copy.setFont(font5)
        self.bt_copy.setStyleSheet(style.bts_functions)
        self.verticalLayout_17.addWidget(self.bt_copy)
        self.gridLayout.addWidget(self.frame_6, 4, 2, 1, 1)
        self.frame_20 = QFrame(self.frame_buttons)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_20)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.bt_0 = QPushButton(self.frame_20)
        self.bt_0.setObjectName(u"bt_0")
        sizePolicy1.setHeightForWidth(self.bt_0.sizePolicy().hasHeightForWidth())
        self.bt_0.setSizePolicy(sizePolicy1)
        self.bt_0.setFont(font2)
        self.bt_0.setStyleSheet(style.bts_numbers)
        self.verticalLayout_9.addWidget(self.bt_0)
        self.gridLayout.addWidget(self.frame_20, 4, 3, 1, 1)
        self.frame_21 = QFrame(self.frame_buttons)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_21)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.bt_dot = QPushButton(self.frame_21)
        self.bt_dot.setObjectName(u"bt_dot")
        sizePolicy1.setHeightForWidth(self.bt_dot.sizePolicy().hasHeightForWidth())
        self.bt_dot.setSizePolicy(sizePolicy1)
        self.bt_dot.setFont(font4)
        self.bt_dot.setStyleSheet(style.bts_functions)
        self.verticalLayout_25.addWidget(self.bt_dot)
        self.gridLayout.addWidget(self.frame_21, 4, 4, 1, 1)
        self.frame_22 = QFrame(self.frame_buttons)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_22)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bt_equal = QPushButton(self.frame_22)
        self.bt_equal.setObjectName(u"bt_equal")
        sizePolicy1.setHeightForWidth(self.bt_equal.sizePolicy().hasHeightForWidth())
        self.bt_equal.setSizePolicy(sizePolicy1)
        self.bt_equal.setFont(font4)
        self.bt_equal.setStyleSheet(style.bts_equal)
        self.verticalLayout_23.addWidget(self.bt_equal)
        self.gridLayout.addWidget(self.frame_22, 3, 5, 2, 1)
        self.verticalLayout_2.addWidget(self.frame_buttons)
        self.frame_credits = QFrame(self.frame_principal)
        self.frame_credits.setObjectName(u"frame_credits")
        self.frame_credits.setMinimumSize(QSize(0, 0))
        self.frame_credits.setMaximumSize(QSize(16777215, 30))
        self.frame_credits.setStyleSheet(u"background-color: transparent;")
        self.frame_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_credits.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_credits)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_credits)
        self.label_credits.setObjectName(u"label_credits")
        font6 = QFont()
        font6.setFamily(u"Roboto")
        self.label_credits.setFont(font6)
        self.label_credits.setStyleSheet(u"QLabel { background-color: transparent; } QLabel:hover { color: rgb(190, 190, 190); }")
        self.horizontalLayout_2.addWidget(self.label_credits)
        self.verticalLayout_2.addWidget(self.frame_credits)
        self.verticalLayout.addWidget(self.frame_principal)

        # TAB INDEX ORDER
        self.setTabOrder(self.pushButton_minimize, self.pushButton_max_rest)
        self.setTabOrder(self.pushButton_max_rest, self.pushButton_close)
        self.setTabOrder(self.pushButton_close, self.lineEdit_values)
        self.setTabOrder(self.bt_0, self.bt_1)
        self.setTabOrder(self.bt_1, self.bt_2)
        self.setTabOrder(self.bt_2, self.bt_3)
        self.setTabOrder(self.bt_3, self.bt_4)
        self.setTabOrder(self.bt_4, self.bt_5)
        self.setTabOrder(self.bt_5, self.bt_6)
        self.setTabOrder(self.bt_6, self.bt_7)
        self.setTabOrder(self.bt_7, self.bt_8)
        self.setTabOrder(self.bt_8, self.bt_9)
        self.setTabOrder(self.bt_9, self.bt_dot)
        self.setTabOrder(self.bt_clear, self.bt_backspace)
        self.setTabOrder(self.bt_backspace, self.bt_div)
        self.setTabOrder(self.bt_div, self.bt_multiply)
        self.setTabOrder(self.bt_multiply, self.bt_minus)
        self.setTabOrder(self.bt_minus, self.bt_plus)
        self.setTabOrder(self.bt_plus, self.bt_equal)
        self.setTabOrder(self.bt_equal, self.bt_copy)

        # END --- WIDGETS

        ########################################################################
        # START - GUI FUNCTIONS
        ########################################################################

        ## TITLE BAR BTS
        ########################################################################

        # MINIMIZE
        self.pushButton_minimize.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE RESTORE
        globals()['state'] = 0
        def maximize():
            if globals()['state'] == 0:
                self.showMaximized()
                globals()['state'] = 1
                self.pushButton_max_rest.setToolTip("Restore")
                self.pushButton_max_rest.setStyleSheet(style.bts_title_bar_restore)
            elif globals()['state'] == 1:
                self.setWindowState(QtCore.Qt.WindowNoState)
                globals()['state'] = 0
                self.pushButton_max_rest.setToolTip("Maximize")
                self.pushButton_max_rest.setStyleSheet(style.bts_title_bar_maximize)

        self.pushButton_max_rest.clicked.connect(lambda: maximize())

        # CLOSE WINDOW
        self.pushButton_close.clicked.connect(lambda: self.close())

        ## BTS NUMBERS FUNCTIONS
        ########################################################################

        # DEF WRITE NUMBER
        def writeNumber(value):
            numbers = self.lineEdit_values.text()
            self.lineEdit_values.setText(numbers + str(value))
            self.clearRepeat()

        # BTS NUMBERS
        self.bt_0.clicked.connect(lambda: writeNumber(0))
        self.bt_1.clicked.connect(lambda: writeNumber(1))
        self.bt_2.clicked.connect(lambda: writeNumber(2))
        self.bt_3.clicked.connect(lambda: writeNumber(3))
        self.bt_4.clicked.connect(lambda: writeNumber(4))
        self.bt_5.clicked.connect(lambda: writeNumber(5))
        self.bt_6.clicked.connect(lambda: writeNumber(6))
        self.bt_7.clicked.connect(lambda: writeNumber(7))
        self.bt_8.clicked.connect(lambda: writeNumber(8))
        self.bt_9.clicked.connect(lambda: writeNumber(9))
        # DOT
        self.bt_dot.clicked.connect(lambda: writeNumber('.'))

        # BT CLEAR
        def clearFields():
            self.label_temp.setText('')
            self.lineEdit_values.setText('')
            self.lineEdit_values.setFocus()

        self.bt_clear.clicked.connect(lambda: clearFields())


        # BACKSPACE
        self.bt_backspace.clicked.connect(lambda: self.clearClick())



        # Bts Operators
        self.bt_div.clicked.connect(lambda: self.setOperations('÷'))
        self.bt_multiply.clicked.connect(lambda: self.setOperations('x'))
        self.bt_minus.clicked.connect(lambda: self.setOperations('-'))
        self.bt_plus.clicked.connect(lambda: self.setOperations('+'))

        # BT EQUAL
        self.bt_equal.clicked.connect(lambda: self.returnValue())

        # BT CREDITS
        globals()['valueTemp'] = ''
        def showCredits():
            self.bt_copy.setEnabled(False)
            globals()['valueTemp'] = self.lineEdit_values.text()
            self.lineEdit_values.setText('')
            QtCore.QTimer.singleShot(100, lambda: self.lineEdit_values.setPlaceholderText("Created"))
            QtCore.QTimer.singleShot(1300, lambda: self.lineEdit_values.setPlaceholderText("by:"))
            QtCore.QTimer.singleShot(2100, lambda: self.lineEdit_values.setPlaceholderText("Wanderson"))
            QtCore.QTimer.singleShot(3500, lambda: self.lineEdit_values.setPlaceholderText("with"))
            QtCore.QTimer.singleShot(4500, lambda: self.lineEdit_values.setPlaceholderText("Python"))
            QtCore.QTimer.singleShot(5500, lambda: self.lineEdit_values.setPlaceholderText("and"))
            QtCore.QTimer.singleShot(6500, lambda: self.lineEdit_values.setPlaceholderText("PySide2"))
            QtCore.QTimer.singleShot(7500, lambda: self.lineEdit_values.setPlaceholderText(":D"))
            QtCore.QTimer.singleShot(8000, lambda: self.lineEdit_values.setPlaceholderText(""))
            QtCore.QTimer.singleShot(8050, lambda: self.lineEdit_values.setText(globals()['valueTemp']))
            QtCore.QTimer.singleShot(8100, lambda: self.bt_copy.setEnabled(True))

        self.bt_copy.clicked.connect(lambda: showCredits())

        ## KEY PRESSED
        ########################################################################
        self.lineEdit_values.keyPressEvent = self.keyPressEvent

        ## WELCOME TEXT ANIMATION
        ########################################################################
        self.lineEdit_values.setFocus()
        self.bt_copy.setEnabled(False)
        QtCore.QTimer.singleShot(200, lambda: self.lineEdit_values.setPlaceholderText("H"))
        QtCore.QTimer.singleShot(600, lambda: self.lineEdit_values.setPlaceholderText("Hi"))
        QtCore.QTimer.singleShot(1000, lambda: self.lineEdit_values.setPlaceholderText("Hi!"))
        QtCore.QTimer.singleShot(3000, lambda: self.lineEdit_values.setPlaceholderText("Welcome!"))
        QtCore.QTimer.singleShot(4000, lambda: self.lineEdit_values.setPlaceholderText("..."))
        QtCore.QTimer.singleShot(5000, lambda: self.lineEdit_values.setPlaceholderText("Here we go"))
        QtCore.QTimer.singleShot(6500, lambda: self.lineEdit_values.setPlaceholderText(":D"))
        QtCore.QTimer.singleShot(7800, lambda: self.lineEdit_values.setPlaceholderText(""))
        QtCore.QTimer.singleShot(8000, lambda: self.bt_copy.setEnabled(True))


        ## MOVE WINDOW
        ########################################################################
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
                if globals()['state']:
                    globals()['state'] = 0
                    maximize()
                    self.setWindowState(QtCore.Qt.WindowNoState)
                    self.pushButton_max_rest.setStyleSheet(style.bts_title_bar_maximize)
                    globals()['state'] = 0

        self.frame_topMenu.mouseMoveEvent = moveWindow
        self.frame_labelTemp.mouseMoveEvent = moveWindow
        #self.label_title.mouseMoveEvent = moveWindow
        self.label_credits.mouseMoveEvent = moveWindow



        ########################################################################
        # END - GUI FUNCTIONS
        ########################################################################

        # CHANGE "MainWindow" TO "self"
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        ## SHOW WINDOW
        self.show()

    ## RETRANSLATE
    ############################################################################
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Calculator", None))
        #if QT_CONFIG(tooltip)
        self.pushButton_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        #endif // QT_CONFIG(tooltip)
        self.pushButton_minimize.setText("")
        #if QT_CONFIG(tooltip)
        self.pushButton_max_rest.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        #endif // QT_CONFIG(tooltip)
        self.pushButton_max_rest.setText("")
        #if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        #endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText("")
        self.label_temp.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.lineEdit_values.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.bt_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.bt_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.bt_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.bt_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.bt_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.bt_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.bt_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.bt_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.bt_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.bt_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.bt_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.bt_backspace.setText("")
        self.bt_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.bt_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.bt_multiply.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.bt_copy.setText(QCoreApplication.translate("MainWindow", u"\u00a9", None))
        self.bt_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bt_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.bt_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Modern Calculator", None))

    ## START -- APP EVENTS
    ############################################################################

    # RESIZE EVENT
    def resizeEvent(self, event):
        self.someFunction()
        return super(Ui, self).resizeEvent(event)

    def someFunction(self):
        if self.height() > 600:
            maximumSize = (self.height() / 20)
            self.frame_lineEdit.setMaximumSize(QSize(16777215, (100 + maximumSize * 2)))
        else:
            self.frame_lineEdit.setMaximumSize(QSize(16777215, 100))

    # MOUSE CLICK
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        self.lineEdit_values.setFocus()

    # BT EQUAL
    def returnValue(self):
        value = self.lineEdit_values.text()
        tempValue = self.label_temp.text()

        if tempValue != '' and value != '':
            join_values = str(tempValue + value).replace(' ', '').replace('÷','/').replace('x','*')
            result = eval(join_values)
            self.label_temp.setText('')
            self.lineEdit_values.setText(str(result))
        self.lineEdit_values.setFocus()


    # JUST NUMBERS AND ".", ","
    def justNumbers(self, value):
        text = str(self.lineEdit_values.text())
        value = str(value)
        clear = ''.join([n for n in value if n.isdigit() or n == '.' or n == ','])
        s = value.isdigit()

        if s:
            self.lineEdit_values.setText(text + value)
            self.clearRepeat()
        else:
            self.lineEdit_values.setText(text + clear)
            self.clearRepeat()
        self.lineEdit_values.setFocus()

    # CLEAR MULTIPLES DOTs
    def clearRepeat(self):
        text = str(self.lineEdit_values.text())
        text = text.replace(',','.').replace('+', '').replace('/', '').replace('*', '').replace('--', '-')
        return self.lineEdit_values.setText(text.replace('..','.'))

    # BT BACKSPACE
    def clearClick(self):
        values = self.lineEdit_values.text()
        if values != '':
            values = values[:-1]
            self.lineEdit_values.setText(values)
        self.lineEdit_values.setFocus()

    # BTS OPERATIONS
    globals()['operator'] = ''
    def setOperations(self, operator):
        value = self.lineEdit_values.text()
        tempValue = self.label_temp.text()

        if tempValue != '' and value != '':
            join_values = str(tempValue + value).replace(' ', '').replace('÷','/').replace('x','*')
            result = eval(join_values)
            self.label_temp.setText(str(result) + ' ' + operator)
            self.lineEdit_values.setText('')
            globals()['operator'] = operator
        elif value != '':
            self.label_temp.setText(value + ' ' + operator)
            self.lineEdit_values.setText('')
            globals()['operator'] = operator
        elif tempValue != '':
            tempValue = tempValue[:-1].replace(' ','')
            self.label_temp.setText(tempValue + ' ' + operator)
            globals()['operator'] = operator
        self.lineEdit_values.setFocus()

    def keyPressEvent(self, event):
        # PRESS ENTER
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.returnValue()
            self.lineEdit_values.setFocus()
            event.accept()

        # BACKSPACE
        if event.key() == Qt.Key_Backspace:
            self.clearClick()

        # OPERATIONS
        if event.text() == '-':
            if self.label_temp.text() == '' and self.lineEdit_values.text() == '':
                self.label_temp.setText('0-')
            self.setOperations('-')
        if event.text() == '+':
            self.setOperations('+')
        if event.text() == '*':
            self.setOperations('x')
        if event.text() == '/':
            self.setOperations('÷')

        # RETURN JUST NUMBERS
        self.justNumbers(event.text())

    ## END -- APP EVENTS
    ############################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/Roboto-Regular.ttf')
    ui = Ui()
    app.exec_()
