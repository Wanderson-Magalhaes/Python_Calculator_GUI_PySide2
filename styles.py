################################################################################
##
## STUDY PROJECT BY: WANDERSON M.
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 0.1
##
################################################################################

class style():

    # MAIN WINDOW
    mainWindow = ("""QToolTip {
                   background: rgb(50, 50, 50);
                   color: rgb(200, 200, 200);
                   border: 1px solid rgb(40, 40, 40);
                   }
                   QLabel { color: rgb(200, 200, 200); }""")
    # BTS TITLE BAR
    ############################################################################

    # BT MINIMIZE  ==> NORMAL
    bts_title_bar_minimize = (u"QPushButton {\n"
    "	background-color: transparent; \n"
    "	background-image: url(:/PNGs/Images/cil-window-minimize.png);\n"
    "	background-position: center;\n"
    "	background-repeat: no-repeat;\n"
    "	border-radius: 10px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(45, 45, 45); 	\n"
    "}\n"
    "QPushButton:pressed {\n"
    "	background-color: rgb(25, 25, 25); \n"
    "	border: 2px solid rgb(255, 0, 127);\n"
    "}")

    # BT MAXIMIZE  ==> NORMAL
    bts_title_bar_maximize = (u"QPushButton {\n"
    "	background-color: transparent; \n"
    "	background-image: url(:/PNGs/Images/cil-window-maximize.png);\n"
    "	background-position: center;\n"
    "	background-repeat: no-repeat;\n"
    "	border-radius: 10px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(45, 45, 45); 	\n"
    "}\n"
    "QPushButton:pressed {\n"
    "	background-color: rgb(25, 25, 25); \n"
    "	border: 2px solid rgb(255, 0, 127);\n"
    "}")

    # BT RESTORE  ==> NORMAL
    bts_title_bar_restore = (u"QPushButton {\n"
    "	background-color: transparent; \n"
    "	background-image: url(:/PNGs/Images/cil-window-restore.png);\n"
    "	background-position: center;\n"
    "	background-repeat: no-repeat;\n"
    "	border-radius: 10px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(45, 45, 45); 	\n"
    "}\n"
    "QPushButton:pressed {\n"
    "	background-color: rgb(25, 25, 25); \n"
    "	border: 2px solid rgb(255, 0, 127);\n"
    "}")

    # BT CLOSE  ==> NORMAL
    bts_title_bar_close = (u"QPushButton {\n"
    "	background-color: transparent; \n"
    "	background-image: url(:/PNGs/Images/cil-x.png);\n"
    "	background-position: center;\n"
    "	background-repeat: no-repeat;\n"
    "	border-radius: 10px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgb(45, 45, 45); 	\n"
    "}\n"
    "QPushButton:pressed {\n"
    "	background-color: rgb(25, 25, 25); \n"
    "	border: 2px solid rgb(255, 0, 127);\n"
    "}")

    # BTS NUMBERS STYLE
    ############################################################################

    # BTS NUMBERS ==> NORMAL
    bts_numbers = (u"QPushButton {\n"
    "	background-color: rgba(45, 45, 45, 50); \n"
    "	color: rgb(200, 200, 200);\n"
    "	border-radius: 10px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgba(255, 0, 127, 100); \n"
    "}\n"
    "QPushButton:pressed {\n"
    "	background-color: rgba(255, 0, 127, 150); \n"
    "	border: 2px solid rgb(255, 0, 127);\n"
    "}")

    # FUNCTIONS BUTTONS
    ############################################################################

    # BTS FUNCTIONS ==> NORMAL
    bts_functions = (u"QPushButton {\n"
    "	background-color: rgba(35, 35, 35, 15); \n"
    "	color: rgb(200, 200, 200);\n"
    "	border-radius: 10px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgba(255, 0, 127, 50); \n"
    "}\n"
    "QPushButton:pressed {\n"
    "	background-color: rgba(255, 0, 127, 100); \n"
    "	border: 2px solid rgb(255, 0, 127);\n"
    "}")

    # BTS BACKSPACE ==> NORMAL
    bts_backspace = (u"QPushButton {\n"
    "	background-color: rgba(35, 35, 35, 15);	\n"
    "	background-image: url(:/PNGs/Images/backspace.png);\n"
    "	background-position: center;\n"
    "	background-repeat: no-repeat;\n"
    "	color: rgb(200, 200, 200);\n"
    "	border-radius: 10px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgba(255, 0, 127, 50); \n"
    "}\n"
    "QPushButton:pressed {\n"
    "	background-color: rgba(255, 0, 127, 100); \n"
    "	border: 2px solid rgb(255, 0, 127);\n"
    "}")

    # BTS EQUAL ==> NORMAL
    bts_equal = (u"QPushButton {\n"
    "	background-color: rgba(35, 35, 35, 15); \n"
    "	color: rgb(200, 200, 200);\n"
    "	border-radius: 10px;\n"
    "}\n"
    "QPushButton:hover {\n"
    "	background-color: rgba(255, 0, 127, 100); \n"
    "}\n"
    "QPushButton:pressed {\n"
    "	background-color: rgba(255, 0, 127, 150); \n"
    "	border: 2px solid rgb(255, 0, 127);\n"
    "}")
