# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_windown.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Gui_windown(object):
    def setupUi(self, Gui_windown):
        Gui_windown.setObjectName("Gui_windown")
        Gui_windown.resize(1931, 1354)
        self.centralwidget = QtWidgets.QWidget(Gui_windown)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.label = QtWidgets.QLabel(self.home)
        self.label.setGeometry(QtCore.QRect(790, 210, 231, 211))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"border-image: url(:/pic_logo/image/98576c3bc08bc5393154d43d2ec07e47.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../LENOVO/.designer/backup/image/98576c3bc08bc5393154d43d2ec07e47.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.home)
        self.label_2.setGeometry(QtCore.QRect(240, 510, 1351, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.home)
        self.label_6.setGeometry(QtCore.QRect(700, 420, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_26 = QtWidgets.QLabel(self.home)
        self.label_26.setGeometry(QtCore.QRect(560, 630, 721, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_29 = QtWidgets.QLabel(self.home)
        self.label_29.setGeometry(QtCore.QRect(560, 690, 791, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.home)
        self.label_30.setGeometry(QtCore.QRect(690, 730, 661, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.pushButton_log_out = QtWidgets.QPushButton(self.home)
        self.pushButton_log_out.setGeometry(QtCore.QRect(1830, 0, 71, 61))
        self.pushButton_log_out.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../do_an_QT_designer/image/log_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_log_out.setIcon(icon)
        self.pushButton_log_out.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_log_out.setObjectName("pushButton_log_out")
        self.label_25 = QtWidgets.QLabel(self.home)
        self.label_25.setGeometry(QtCore.QRect(380, -10, 1051, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_28 = QtWidgets.QLabel(self.home)
        self.label_28.setGeometry(QtCore.QRect(680, 80, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_31 = QtWidgets.QLabel(self.home)
        self.label_31.setGeometry(QtCore.QRect(590, 150, 671, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.tabWidget.addTab(self.home, "")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.label_camera = QtWidgets.QLabel(self.main)
        self.label_camera.setGeometry(QtCore.QRect(100, 10, 841, 521))
        self.label_camera.setStyleSheet("background-color: rgb(85, 255, 255,100);\n"
"border-radius:10px;\n"
"border-color: black;\n"
"border: 3px solid blue;")
        self.label_camera.setObjectName("label_camera")
        self.pushButton_start_camera = QtWidgets.QPushButton(self.main)
        self.pushButton_start_camera.setGeometry(QtCore.QRect(170, 570, 201, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_start_camera.setFont(font)
        self.pushButton_start_camera.setStyleSheet("QPushButton{;\n"
"    background-color: rgb(85, 0, 127);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:8px;}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_start_camera.setObjectName("pushButton_start_camera")
        self.pushButton_stop_camera = QtWidgets.QPushButton(self.main)
        self.pushButton_stop_camera.setGeometry(QtCore.QRect(170, 670, 201, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_stop_camera.setFont(font)
        self.pushButton_stop_camera.setStyleSheet("QPushButton{    background-color: rgb(85, 0, 127);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:8px;}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_stop_camera.setObjectName("pushButton_stop_camera")
        self.label_44 = QtWidgets.QLabel(self.main)
        self.label_44.setGeometry(QtCore.QRect(1000, 30, 291, 61))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.main)
        self.label_45.setGeometry(QtCore.QRect(1000, 20, 291, 271))
        self.label_45.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius:25px;\n"
"border-color:rgb(0, 0, 0);\n"
"border: 3px solid blue;")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.main)
        self.label_46.setGeometry(QtCore.QRect(1060, 90, 17, 30))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.main)
        self.label_47.setGeometry(QtCore.QRect(1060, 170, 17, 30))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.main)
        self.label_48.setGeometry(QtCore.QRect(1060, 240, 17, 30))
        self.label_48.setObjectName("label_48")
        self.textEdit_ob_x = QtWidgets.QTextEdit(self.main)
        self.textEdit_ob_x.setGeometry(QtCore.QRect(1100, 90, 104, 41))
        self.textEdit_ob_x.setObjectName("textEdit_ob_x")
        self.textEdit_ob_y = QtWidgets.QTextEdit(self.main)
        self.textEdit_ob_y.setGeometry(QtCore.QRect(1100, 160, 104, 41))
        self.textEdit_ob_y.setObjectName("textEdit_ob_y")
        self.textEdit_ob_z = QtWidgets.QTextEdit(self.main)
        self.textEdit_ob_z.setGeometry(QtCore.QRect(1100, 230, 104, 41))
        self.textEdit_ob_z.setObjectName("textEdit_ob_z")
        self.label_49 = QtWidgets.QLabel(self.main)
        self.label_49.setGeometry(QtCore.QRect(1320, 20, 531, 281))
        self.label_49.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius:25px;\n"
"border-color:rgb(0, 0, 0);\n"
"border: 3px solid blue;")
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.main)
        self.label_50.setGeometry(QtCore.QRect(1420, 150, 291, 61))
        self.label_50.setObjectName("label_50")
        self.textEdit_number_of_box = QtWidgets.QTextEdit(self.main)
        self.textEdit_number_of_box.setGeometry(QtCore.QRect(1520, 200, 104, 41))
        self.textEdit_number_of_box.setObjectName("textEdit_number_of_box")
        self.pushButton_auto_stop = QtWidgets.QPushButton(self.main)
        self.pushButton_auto_stop.setGeometry(QtCore.QRect(770, 650, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_auto_stop.setFont(font)
        self.pushButton_auto_stop.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_auto_stop.setObjectName("pushButton_auto_stop")
        self.pushButton_auto_run = QtWidgets.QPushButton(self.main)
        self.pushButton_auto_run.setGeometry(QtCore.QRect(770, 560, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_auto_run.setFont(font)
        self.pushButton_auto_run.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_auto_run.setObjectName("pushButton_auto_run")
        self.pushButton_home_1 = QtWidgets.QPushButton(self.main)
        self.pushButton_home_1.setGeometry(QtCore.QRect(170, 760, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_home_1.setFont(font)
        self.pushButton_home_1.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_home_1.setObjectName("pushButton_home_1")
        self.label_69 = QtWidgets.QLabel(self.main)
        self.label_69.setGeometry(QtCore.QRect(460, 540, 481, 311))
        self.label_69.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius:25px;\n"
"border-color:rgb(0, 0, 0);\n"
"border: 3px solid blue;")
        self.label_69.setText("")
        self.label_69.setObjectName("label_69")
        self.pushButton_reset_auto = QtWidgets.QPushButton(self.main)
        self.pushButton_reset_auto.setGeometry(QtCore.QRect(770, 740, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_reset_auto.setFont(font)
        self.pushButton_reset_auto.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_reset_auto.setObjectName("pushButton_reset_auto")
        self.label_74 = QtWidgets.QLabel(self.main)
        self.label_74.setGeometry(QtCore.QRect(100, 540, 341, 311))
        self.label_74.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius:25px;\n"
"border-color:rgb(0, 0, 0);\n"
"border: 3px solid blue;")
        self.label_74.setText("")
        self.label_74.setObjectName("label_74")
        self.label_22 = QtWidgets.QLabel(self.main)
        self.label_22.setGeometry(QtCore.QRect(1220, 90, 51, 31))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.main)
        self.label_23.setGeometry(QtCore.QRect(1220, 170, 51, 31))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.main)
        self.label_24.setGeometry(QtCore.QRect(1220, 240, 51, 31))
        self.label_24.setObjectName("label_24")
        self.label_55 = QtWidgets.QLabel(self.main)
        self.label_55.setGeometry(QtCore.QRect(1430, 40, 291, 61))
        self.label_55.setObjectName("label_55")
        self.textEdit_number_of_shelves = QtWidgets.QTextEdit(self.main)
        self.textEdit_number_of_shelves.setGeometry(QtCore.QRect(1520, 100, 104, 41))
        self.textEdit_number_of_shelves.setObjectName("textEdit_number_of_shelves")
        self.label_mapping = QtWidgets.QLabel(self.main)
        self.label_mapping.setGeometry(QtCore.QRect(970, 420, 881, 431))
        self.label_mapping.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius:25px;\n"
"border-color:rgb(0, 0, 0);\n"
"border: 3px solid blue;")
        self.label_mapping.setText("")
        self.label_mapping.setObjectName("label_mapping")
        self.pushButton_total_location = QtWidgets.QPushButton(self.main)
        self.pushButton_total_location.setGeometry(QtCore.QRect(500, 600, 171, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_total_location.setFont(font)
        self.pushButton_total_location.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_total_location.setObjectName("pushButton_total_location")
        self.pushButton_a_few_location = QtWidgets.QPushButton(self.main)
        self.pushButton_a_few_location.setGeometry(QtCore.QRect(500, 710, 161, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_a_few_location.setFont(font)
        self.pushButton_a_few_location.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_a_few_location.setObjectName("pushButton_a_few_location")
        self.pushButton_start_mapping = QtWidgets.QPushButton(self.main)
        self.pushButton_start_mapping.setGeometry(QtCore.QRect(980, 350, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_mapping.setFont(font)
        self.pushButton_start_mapping.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_start_mapping.setObjectName("pushButton_start_mapping")
        self.pushButton_stop_mapping = QtWidgets.QPushButton(self.main)
        self.pushButton_stop_mapping.setGeometry(QtCore.QRect(1330, 350, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop_mapping.setFont(font)
        self.pushButton_stop_mapping.setStyleSheet("QPushButton{background-color: rgb(85, 0, 127);\n"
"border-radius:8px;\n"
"color:rgb(255, 255, 255);}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_stop_mapping.setObjectName("pushButton_stop_mapping")
        self.label_74.raise_()
        self.label_69.raise_()
        self.label_45.raise_()
        self.label_camera.raise_()
        self.pushButton_start_camera.raise_()
        self.pushButton_stop_camera.raise_()
        self.label_44.raise_()
        self.label_46.raise_()
        self.label_47.raise_()
        self.label_48.raise_()
        self.textEdit_ob_x.raise_()
        self.textEdit_ob_y.raise_()
        self.textEdit_ob_z.raise_()
        self.label_49.raise_()
        self.label_50.raise_()
        self.textEdit_number_of_box.raise_()
        self.pushButton_auto_stop.raise_()
        self.pushButton_auto_run.raise_()
        self.pushButton_home_1.raise_()
        self.pushButton_reset_auto.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_55.raise_()
        self.textEdit_number_of_shelves.raise_()
        self.label_mapping.raise_()
        self.pushButton_total_location.raise_()
        self.pushButton_a_few_location.raise_()
        self.pushButton_start_mapping.raise_()
        self.pushButton_stop_mapping.raise_()
        self.tabWidget.addTab(self.main, "")
        self.history = QtWidgets.QWidget()
        self.history.setObjectName("history")
        self.comboBox_chose_the_mode = QtWidgets.QComboBox(self.history)
        self.comboBox_chose_the_mode.setGeometry(QtCore.QRect(840, 130, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.comboBox_chose_the_mode.setFont(font)
        self.comboBox_chose_the_mode.setStyleSheet("border: 2px solid black;")
        self.comboBox_chose_the_mode.setEditable(False)
        self.comboBox_chose_the_mode.setObjectName("comboBox_chose_the_mode")
        self.comboBox_chose_the_mode.addItem("")
        self.comboBox_chose_the_mode.addItem("")
        self.comboBox_chose_the_mode.addItem("")
        self.pushButton_clear = QtWidgets.QPushButton(self.history)
        self.pushButton_clear.setGeometry(QtCore.QRect(950, 340, 93, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("QPushButton{\n"
"border: 3px solid blue;\n"
"background-color: rgb(85, 0, 255);\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_search = QtWidgets.QPushButton(self.history)
        self.pushButton_search.setGeometry(QtCore.QRect(840, 340, 93, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setStyleSheet("QPushButton{\n"
"border: 3px solid blue;\n"
"background-color: rgb(85, 0, 255);\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_calendar_1 = QtWidgets.QPushButton(self.history)
        self.pushButton_calendar_1.setGeometry(QtCore.QRect(1070, 200, 51, 51))
        self.pushButton_calendar_1.setStyleSheet("QPushButton{border:none;}\n"
"\n"
"")
        self.pushButton_calendar_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../do_an_QT_designer/image/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_calendar_1.setIcon(icon1)
        self.pushButton_calendar_1.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_calendar_1.setObjectName("pushButton_calendar_1")
        self.pushButton_calendar_2 = QtWidgets.QPushButton(self.history)
        self.pushButton_calendar_2.setGeometry(QtCore.QRect(1070, 280, 51, 41))
        self.pushButton_calendar_2.setStyleSheet("QPushButton{border:none;}\n"
"\n"
"")
        self.pushButton_calendar_2.setText("")
        self.pushButton_calendar_2.setIcon(icon1)
        self.pushButton_calendar_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_calendar_2.setObjectName("pushButton_calendar_2")
        self.dateEdit_1 = QtWidgets.QDateEdit(self.history)
        self.dateEdit_1.setGeometry(QtCore.QRect(840, 200, 231, 41))
        self.dateEdit_1.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 6, 24), QtCore.QTime(0, 0, 0)))
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.history)
        self.dateEdit_2.setGeometry(QtCore.QRect(840, 280, 231, 41))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 6, 24), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.tableWidget_account = QtWidgets.QTableWidget(self.history)
        self.tableWidget_account.setGeometry(QtCore.QRect(5, 41, 791, 651))
        self.tableWidget_account.setStyleSheet("")
        self.tableWidget_account.setObjectName("tableWidget_account")
        self.tableWidget_account.setColumnCount(0)
        self.tableWidget_account.setRowCount(0)
        self.pushButton_load = QtWidgets.QPushButton(self.history)
        self.pushButton_load.setGeometry(QtCore.QRect(850, 440, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_load.setFont(font)
        self.pushButton_load.setStyleSheet("QPushButton{\n"
"border: 3px solid blue;\n"
"background-color: rgb(85, 0, 255);\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_report = QtWidgets.QPushButton(self.history)
        self.pushButton_report.setGeometry(QtCore.QRect(850, 540, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_report.setFont(font)
        self.pushButton_report.setStyleSheet("QPushButton{\n"
"border: 3px solid blue;\n"
"background-color: rgb(85, 0, 255);\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover {background-color: rgb(85, 0, 127,200);}\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_report.setObjectName("pushButton_report")
        self.dateEdit_1.raise_()
        self.comboBox_chose_the_mode.raise_()
        self.pushButton_clear.raise_()
        self.pushButton_search.raise_()
        self.pushButton_calendar_1.raise_()
        self.pushButton_calendar_2.raise_()
        self.dateEdit_2.raise_()
        self.tableWidget_account.raise_()
        self.pushButton_load.raise_()
        self.pushButton_report.raise_()
        self.tabWidget.addTab(self.history, "")
        self.verticalLayout.addWidget(self.tabWidget)
        Gui_windown.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Gui_windown)
        self.statusbar.setObjectName("statusbar")
        Gui_windown.setStatusBar(self.statusbar)

        self.retranslateUi(Gui_windown)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Gui_windown)

    def retranslateUi(self, Gui_windown):
        _translate = QtCore.QCoreApplication.translate
        Gui_windown.setWindowTitle(_translate("Gui_windown", "MainWindow"))
        self.tabWidget.setToolTip(_translate("Gui_windown", "qưq"))
        self.tabWidget.setWhatsThis(_translate("Gui_windown", "<html><head/><body><p>ssss</p></body></html>"))
        self.label_2.setText(_translate("Gui_windown", "<html><head/><body><p align=\"center\"><span style=\" color:#00aaff;\">ĐIỀU KHIỂN NHẬN DIỆN VÀ QUẢN LÝ NHÀ KHO BẰNG DRONE </span></p><p align=\"center\"><span style=\" color:#00aaff;\">ỨNG DỤNG XỬ LÝ ẢNH </span></p></body></html>"))
        self.label_6.setText(_translate("Gui_windown", "<html><head/><body><p><span style=\" color:#ff0000;\">ĐỒ ÁN TỐT NGHIỆP</span></p></body></html>"))
        self.label_26.setText(_translate("Gui_windown", "GVHD: THẦY THS.NGUYỄN ĐỨC HOÀNG"))
        self.label_29.setText(_translate("Gui_windown", "SVTH:    BÙI MINH HIẾU                  2011182"))
        self.label_30.setText(_translate("Gui_windown", "NGUYỄN VÕ TẤN HẢI       2013076"))
        self.label_25.setText(_translate("Gui_windown", "<html><head/><body><p><span style=\" color:#000000;\">TRƯỜNG ĐẠI HỌC BÁCH KHOA TP. HỒ CHÍ MINH</span></p></body></html>"))
        self.label_28.setText(_translate("Gui_windown", "<html><head/><body><p><span style=\" color:#000000;\">KHOA ĐIỆN - ĐIỆN TỬ </span></p><p><br/></p></body></html>"))
        self.label_31.setText(_translate("Gui_windown", "<html><head/><body><p>BỘ MÔN ĐIỀU KHIỂN TỰ ĐỘNG </p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("Gui_windown", "Home"))
        self.label_camera.setText(_translate("Gui_windown", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#55007f;\">Camera</span></p></body></html>"))
        self.pushButton_start_camera.setText(_translate("Gui_windown", "Start Camera"))
        self.pushButton_stop_camera.setText(_translate("Gui_windown", "Stop Camera"))
        self.label_44.setText(_translate("Gui_windown", "<html><head/><body><p align=\"center\"><span style=\" color:#0000ff;\">Coodirnates of Object</span></p></body></html>"))
        self.label_46.setText(_translate("Gui_windown", "X"))
        self.label_47.setText(_translate("Gui_windown", "Y"))
        self.label_48.setText(_translate("Gui_windown", "Z"))
        self.label_50.setText(_translate("Gui_windown", "<html><head/><body><p align=\"center\"><span style=\" color:#0000ff;\">Number of Box </span></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_auto_stop.setText(_translate("Gui_windown", "STOP"))
        self.pushButton_auto_run.setText(_translate("Gui_windown", "RUN"))
        self.pushButton_home_1.setText(_translate("Gui_windown", "HOME"))
        self.pushButton_reset_auto.setText(_translate("Gui_windown", "RESET"))
        self.label_22.setText(_translate("Gui_windown", "cm"))
        self.label_23.setText(_translate("Gui_windown", "cm"))
        self.label_24.setText(_translate("Gui_windown", "cm"))
        self.label_55.setText(_translate("Gui_windown", "<html><head/><body><p align=\"center\"><span style=\" color:#0000ff;\">Number of shelves</span></p></body></html>"))
        self.pushButton_total_location.setText(_translate("Gui_windown", "TOTAL LOCATION"))
        self.pushButton_a_few_location.setText(_translate("Gui_windown", "A FEW LOCATION"))
        self.pushButton_start_mapping.setText(_translate("Gui_windown", "START MAPPING"))
        self.pushButton_stop_mapping.setText(_translate("Gui_windown", "STOP MAPPING"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("Gui_windown", "MAIN"))
        self.comboBox_chose_the_mode.setItemText(0, _translate("Gui_windown", "Chose the Mode"))
        self.comboBox_chose_the_mode.setItemText(1, _translate("Gui_windown", "Account"))
        self.comboBox_chose_the_mode.setItemText(2, _translate("Gui_windown", "Detected Box "))
        self.pushButton_clear.setText(_translate("Gui_windown", "Clear"))
        self.pushButton_search.setText(_translate("Gui_windown", "Search"))
        self.dateEdit_1.setDisplayFormat(_translate("Gui_windown", "dd/MM/yyyy"))
        self.dateEdit_2.setDisplayFormat(_translate("Gui_windown", "dd/MM/yyyy"))
        self.pushButton_load.setText(_translate("Gui_windown", "Product infomation"))
        self.pushButton_report.setText(_translate("Gui_windown", "Report"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history), _translate("Gui_windown", "HISTORY"))
import pic_logo 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gui_windown = QtWidgets.QMainWindow()
    ui = Ui_Gui_windown()
    ui.setupUi(Gui_windown)
    Gui_windown.show()
    sys.exit(app.exec_())