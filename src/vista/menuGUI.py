# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import src.vista.recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 678)
        MainWindow.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_4 = QVBoxLayout(self.main_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Header = QWidget(self.main_menu)
        self.Header.setObjectName(u"Header")
        self.Header.setStyleSheet(u"text-align:left;")
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_menu = QPushButton(self.Header)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/Iconos/iconMove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(40, 40))
        self.btn_menu.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.btn_Inicio = QPushButton(self.Header)
        self.btn_Inicio.setObjectName(u"btn_Inicio")
        self.btn_Inicio.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/Iconos/IconHouse.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Inicio.setIcon(icon1)
        self.btn_Inicio.setIconSize(QSize(40, 40))
        self.btn_Inicio.setCheckable(True)
        self.btn_Inicio.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_Inicio)

        self.label_8 = QLabel(self.Header)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 40))
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setPixmap(QPixmap(u":/newPrefix/Iconos/TEMPOLARM_BAR_1.png"))
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.btn_Info = QPushButton(self.Header)
        self.btn_Info.setObjectName(u"btn_Info")
        self.btn_Info.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/Iconos/iconSobre.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Info.setIcon(icon2)
        self.btn_Info.setIconSize(QSize(40, 40))
        self.btn_Info.setCheckable(True)
        self.btn_Info.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_Info)


        self.verticalLayout_4.addWidget(self.Header)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(13, 13, 13);\n"
"	font: 10pt \"Century Gothic\";\n"
"	color: rgb(255, 249, 250);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(20, 28, 77);\n"
"text-align:center;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(38, 55, 149);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(244, 244, 244);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px border: 1px solid rgb(118, 0, 59);\n"
"}")
        self.Inicio_page = QWidget()
        self.Inicio_page.setObjectName(u"Inicio_page")
        self.verticalLayout_5 = QVBoxLayout(self.Inicio_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_Bienvenida = QLabel(self.Inicio_page)
        self.lbl_Bienvenida.setObjectName(u"lbl_Bienvenida")
        self.lbl_Bienvenida.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Century Gothic\";")
        self.lbl_Bienvenida.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_Bienvenida)

        self.lbl_icon = QLabel(self.Inicio_page)
        self.lbl_icon.setObjectName(u"lbl_icon")
        self.lbl_icon.setMinimumSize(QSize(100, 100))
        self.lbl_icon.setMaximumSize(QSize(1080, 700))
        self.lbl_icon.setLayoutDirection(Qt.LeftToRight)
        self.lbl_icon.setPixmap(QPixmap(u":/newPrefix/Iconos/Kirby_hola.jpg"))
        self.lbl_icon.setScaledContents(True)
        self.lbl_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_icon)

        self.stackedWidget.addWidget(self.Inicio_page)
        self.Temp_page = QWidget()
        self.Temp_page.setObjectName(u"Temp_page")
        self.verticalLayout_7 = QVBoxLayout(self.Temp_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.Temp_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 40))
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setStyleSheet(u"font: 75 20pt \"Century Gothic\";\n"
"background-color: rgb(35, 49, 127);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)

        self.groupBox_3 = QGroupBox(self.Temp_page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 12pt \"Century Gothic\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 75 12pt \"Century Gothic\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 75 12pt \"Century Gothic\";")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(36, 0, 35, -1)
        self.lineEdit_Horas_Temp = QLineEdit(self.groupBox_3)
        self.lineEdit_Horas_Temp.setObjectName(u"lineEdit_Horas_Temp")
        self.lineEdit_Horas_Temp.setMaximumSize(QSize(65, 50))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.lineEdit_Horas_Temp.setFont(font)
        self.lineEdit_Horas_Temp.setStyleSheet(u"text-align:center;\n"
"font: 75 36pt \"Century Gothic\";")

        self.horizontalLayout_7.addWidget(self.lineEdit_Horas_Temp)

        self.lblseparador = QLabel(self.groupBox_3)
        self.lblseparador.setObjectName(u"lblseparador")
        self.lblseparador.setStyleSheet(u"font: 75 36pt \"Century Gothic\";")
        self.lblseparador.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lblseparador)

        self.lineEdit_Minutos_Temp = QLineEdit(self.groupBox_3)
        self.lineEdit_Minutos_Temp.setObjectName(u"lineEdit_Minutos_Temp")
        self.lineEdit_Minutos_Temp.setMaximumSize(QSize(65, 50))
        self.lineEdit_Minutos_Temp.setStyleSheet(u"text-align:center;\n"
"font: 75 36pt \"Century Gothic\";")

        self.horizontalLayout_7.addWidget(self.lineEdit_Minutos_Temp)

        self.lblseparador_2 = QLabel(self.groupBox_3)
        self.lblseparador_2.setObjectName(u"lblseparador_2")
        self.lblseparador_2.setStyleSheet(u"font: 75 36pt \"Century Gothic\";")
        self.lblseparador_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lblseparador_2)

        self.lineEdit_Segundos_Temp = QLineEdit(self.groupBox_3)
        self.lineEdit_Segundos_Temp.setObjectName(u"lineEdit_Segundos_Temp")
        self.lineEdit_Segundos_Temp.setMaximumSize(QSize(65, 50))
        self.lineEdit_Segundos_Temp.setStyleSheet(u"text-align:center;\n"
"font: 75 36pt \"Century Gothic\";")

        self.horizontalLayout_7.addWidget(self.lineEdit_Segundos_Temp)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.btn_Pausa_Temp = QPushButton(self.Temp_page)
        self.btn_Pausa_Temp.setObjectName(u"btn_Pausa_Temp")
        self.btn_Pausa_Temp.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/Iconos/IconMinSize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Pausa_Temp.setIcon(icon3)
        self.btn_Pausa_Temp.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_Pausa_Temp)

        self.btn_Iniciar_Temp = QPushButton(self.Temp_page)
        self.btn_Iniciar_Temp.setObjectName(u"btn_Iniciar_Temp")
        self.btn_Iniciar_Temp.setMinimumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/Iconos/iconPlay.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Iniciar_Temp.setIcon(icon4)
        self.btn_Iniciar_Temp.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_Iniciar_Temp)

        self.btn_Reiniciar_Temp = QPushButton(self.Temp_page)
        self.btn_Reiniciar_Temp.setObjectName(u"btn_Reiniciar_Temp")
        self.btn_Reiniciar_Temp.setMinimumSize(QSize(40, 40))
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/Iconos/iconRedo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Reiniciar_Temp.setIcon(icon5)
        self.btn_Reiniciar_Temp.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_Reiniciar_Temp)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.groupBox = QGroupBox(self.Temp_page)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setSpacing(11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBoxTonosAlarma_Temp = QComboBox(self.groupBox)
        self.comboBoxTonosAlarma_Temp.setObjectName(u"comboBoxTonosAlarma_Temp")
        self.comboBoxTonosAlarma_Temp.setStyleSheet(u"background-color: rgb(35, 49, 127);")

        self.verticalLayout_6.addWidget(self.comboBoxTonosAlarma_Temp)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_6.addWidget(self.label_11)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.lineEdit_NombreTemp = QLineEdit(self.groupBox)
        self.lineEdit_NombreTemp.setObjectName(u"lineEdit_NombreTemp")
        self.lineEdit_NombreTemp.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.lineEdit_NombreTemp)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_Guardar_Temp = QPushButton(self.groupBox)
        self.btn_Guardar_Temp.setObjectName(u"btn_Guardar_Temp")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/Iconos/iconSave.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Guardar_Temp.setIcon(icon6)
        self.btn_Guardar_Temp.setIconSize(QSize(40, 40))
        self.btn_Guardar_Temp.setCheckable(True)
        self.btn_Guardar_Temp.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.btn_Guardar_Temp)

        self.btn_Limpiar_Temp = QPushButton(self.groupBox)
        self.btn_Limpiar_Temp.setObjectName(u"btn_Limpiar_Temp")
        self.btn_Limpiar_Temp.setIcon(icon6)
        self.btn_Limpiar_Temp.setIconSize(QSize(40, 40))
        self.btn_Limpiar_Temp.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.btn_Limpiar_Temp)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(8, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.Temp_page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 40))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setSpacing(9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.comboBoxConfigGuardadasTemp = QComboBox(self.groupBox_2)
        self.comboBoxConfigGuardadasTemp.setObjectName(u"comboBoxConfigGuardadasTemp")
        self.comboBoxConfigGuardadasTemp.setStyleSheet(u"background-color: rgb(35, 49, 127);")

        self.verticalLayout_9.addWidget(self.comboBoxConfigGuardadasTemp)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.Temp_page)
        self.Pom_page = QWidget()
        self.Pom_page.setObjectName(u"Pom_page")
        self.verticalLayout_23 = QVBoxLayout(self.Pom_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_28 = QLabel(self.Pom_page)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(200, 40))
        self.label_28.setMaximumSize(QSize(16777215, 40))
        self.label_28.setStyleSheet(u"font: 75 20pt \"Century Gothic\";\n"
"background-color: rgb(186, 75, 38);")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_28)

        self.groupBox_10 = QGroupBox(self.Pom_page)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_5 = QLabel(self.groupBox_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 75 12pt \"Century Gothic\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_5)

        self.label_29 = QLabel(self.groupBox_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 75 12pt \"Century Gothic\";")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_29)


        self.verticalLayout_20.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_24 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_20.addItem(self.verticalSpacer_24)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(36, 0, 35, -1)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)

        self.lineEdit_Minutos_Pom = QLineEdit(self.groupBox_10)
        self.lineEdit_Minutos_Pom.setObjectName(u"lineEdit_Minutos_Pom")
        self.lineEdit_Minutos_Pom.setMinimumSize(QSize(65, 50))
        self.lineEdit_Minutos_Pom.setMaximumSize(QSize(65, 50))
        self.lineEdit_Minutos_Pom.setStyleSheet(u"text-align:center;\n"
"font: 75 36pt \"Century Gothic\";")

        self.horizontalLayout_16.addWidget(self.lineEdit_Minutos_Pom)

        self.lblseparador_7 = QLabel(self.groupBox_10)
        self.lblseparador_7.setObjectName(u"lblseparador_7")
        self.lblseparador_7.setStyleSheet(u"font: 75 36pt \"Century Gothic\";")
        self.lblseparador_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lblseparador_7)

        self.lineEdit_Segundos_Pom = QLineEdit(self.groupBox_10)
        self.lineEdit_Segundos_Pom.setObjectName(u"lineEdit_Segundos_Pom")
        self.lineEdit_Segundos_Pom.setMaximumSize(QSize(65, 50))
        self.lineEdit_Segundos_Pom.setStyleSheet(u"text-align:center;\n"
"font: 75 36pt \"Century Gothic\";")

        self.horizontalLayout_16.addWidget(self.lineEdit_Segundos_Pom)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)


        self.verticalLayout_20.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_25 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_20.addItem(self.verticalSpacer_25)


        self.verticalLayout_23.addWidget(self.groupBox_10)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_17.setContentsMargins(10, 0, 10, 0)
        self.btn_Pausa_Pom = QPushButton(self.Pom_page)
        self.btn_Pausa_Pom.setObjectName(u"btn_Pausa_Pom")
        self.btn_Pausa_Pom.setMinimumSize(QSize(40, 40))
        self.btn_Pausa_Pom.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(186, 75, 38)\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(83, 33, 16);\n"
"}")
        self.btn_Pausa_Pom.setIcon(icon3)
        self.btn_Pausa_Pom.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.btn_Pausa_Pom)

        self.btn_Iniciar_Pom = QPushButton(self.Pom_page)
        self.btn_Iniciar_Pom.setObjectName(u"btn_Iniciar_Pom")
        self.btn_Iniciar_Pom.setMinimumSize(QSize(40, 40))
        self.btn_Iniciar_Pom.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(186, 75, 38)\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(83, 33, 16);\n"
"}")
        self.btn_Iniciar_Pom.setIcon(icon4)
        self.btn_Iniciar_Pom.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.btn_Iniciar_Pom)

        self.btn_Reiniciar_Pom = QPushButton(self.Pom_page)
        self.btn_Reiniciar_Pom.setObjectName(u"btn_Reiniciar_Pom")
        self.btn_Reiniciar_Pom.setMinimumSize(QSize(40, 40))
        self.btn_Reiniciar_Pom.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(186, 75, 38)\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(83, 33, 16);\n"
"}")
        self.btn_Reiniciar_Pom.setIcon(icon5)
        self.btn_Reiniciar_Pom.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.btn_Reiniciar_Pom)


        self.verticalLayout_23.addLayout(self.horizontalLayout_17)

        self.groupBox_11 = QGroupBox(self.Pom_page)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_30 = QLabel(self.groupBox_11)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_18.addWidget(self.label_30)

        self.spinBox_tmpPomodoro = QSpinBox(self.groupBox_11)
        self.spinBox_tmpPomodoro.setObjectName(u"spinBox_tmpPomodoro")
        self.spinBox_tmpPomodoro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_18.addWidget(self.spinBox_tmpPomodoro)


        self.verticalLayout_22.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_31 = QLabel(self.groupBox_11)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_19.addWidget(self.label_31)

        self.spinBox_tmpDescanso = QSpinBox(self.groupBox_11)
        self.spinBox_tmpDescanso.setObjectName(u"spinBox_tmpDescanso")
        self.spinBox_tmpDescanso.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_19.addWidget(self.spinBox_tmpDescanso)


        self.verticalLayout_22.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_32 = QLabel(self.groupBox_11)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_20.addWidget(self.label_32)

        self.spinBox_tmpDescLargo = QSpinBox(self.groupBox_11)
        self.spinBox_tmpDescLargo.setObjectName(u"spinBox_tmpDescLargo")
        self.spinBox_tmpDescLargo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_20.addWidget(self.spinBox_tmpDescLargo)


        self.verticalLayout_22.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_33 = QLabel(self.groupBox_11)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_21.addWidget(self.label_33)

        self.spinBox_tmpPeriodos = QSpinBox(self.groupBox_11)
        self.spinBox_tmpPeriodos.setObjectName(u"spinBox_tmpPeriodos")
        self.spinBox_tmpPeriodos.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_21.addWidget(self.spinBox_tmpPeriodos)


        self.verticalLayout_22.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_34 = QLabel(self.groupBox_11)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_22.addWidget(self.label_34)

        self.comboBoxtonoAlarmaPom = QComboBox(self.groupBox_11)
        self.comboBoxtonoAlarmaPom.setObjectName(u"comboBoxtonoAlarmaPom")
        self.comboBoxtonoAlarmaPom.setStyleSheet(u"background-color: rgb(186, 75, 38);\n"
"font: 8pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_22.addWidget(self.comboBoxtonoAlarmaPom)


        self.verticalLayout_22.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_7 = QLabel(self.groupBox_11)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_31.addWidget(self.label_7)

        self.horizontalSpacer_12 = QSpacerItem(157, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_12)

        self.lineEdit_NombrePom = QLineEdit(self.groupBox_11)
        self.lineEdit_NombrePom.setObjectName(u"lineEdit_NombrePom")
        self.lineEdit_NombrePom.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_31.addWidget(self.lineEdit_NombrePom)


        self.verticalLayout_22.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.btn_Guardar_Pom = QPushButton(self.groupBox_11)
        self.btn_Guardar_Pom.setObjectName(u"btn_Guardar_Pom")
        self.btn_Guardar_Pom.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(186, 75, 38)\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(83, 33, 16);\n"
"}")
        self.btn_Guardar_Pom.setIcon(icon6)
        self.btn_Guardar_Pom.setIconSize(QSize(40, 40))
        self.btn_Guardar_Pom.setAutoExclusive(True)

        self.horizontalLayout_23.addWidget(self.btn_Guardar_Pom)

        self.btn_Limpiar_Pom = QPushButton(self.groupBox_11)
        self.btn_Limpiar_Pom.setObjectName(u"btn_Limpiar_Pom")
        self.btn_Limpiar_Pom.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(186, 75, 38)\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(83, 33, 16);\n"
"}")
        self.btn_Limpiar_Pom.setIcon(icon6)
        self.btn_Limpiar_Pom.setIconSize(QSize(40, 40))
        self.btn_Limpiar_Pom.setAutoExclusive(True)

        self.horizontalLayout_23.addWidget(self.btn_Limpiar_Pom)


        self.verticalLayout_22.addLayout(self.horizontalLayout_23)


        self.verticalLayout_23.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.Pom_page)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(0, 40))
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_21.setSpacing(9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.comboBoxConfigGuardadasPom = QComboBox(self.groupBox_12)
        self.comboBoxConfigGuardadasPom.setObjectName(u"comboBoxConfigGuardadasPom")
        self.comboBoxConfigGuardadasPom.setStyleSheet(u"background-color: rgb(186, 75, 38);\n"
"font: 75 9pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_21.addWidget(self.comboBoxConfigGuardadasPom)


        self.verticalLayout_23.addWidget(self.groupBox_12)

        self.stackedWidget.addWidget(self.Pom_page)
        self.Alarm_page = QWidget()
        self.Alarm_page.setObjectName(u"Alarm_page")
        self.verticalLayout_26 = QVBoxLayout(self.Alarm_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_35 = QLabel(self.Alarm_page)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(200, 40))
        self.label_35.setMaximumSize(QSize(16777215, 40))
        self.label_35.setStyleSheet(u"font: 75 20pt \"Century Gothic\";\n"
"background-color: rgb(111, 1, 1);")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_35)

        self.groupBox_13 = QGroupBox(self.Alarm_page)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_6 = QLabel(self.groupBox_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 75 12pt \"Century Gothic\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_6)

        self.label_36 = QLabel(self.groupBox_13)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font: 75 12pt \"Century Gothic\";")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_36)


        self.verticalLayout_24.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_26 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_24.addItem(self.verticalSpacer_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(36, 0, 35, -1)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)

        self.lineEdit_Horas_Alarm = QLineEdit(self.groupBox_13)
        self.lineEdit_Horas_Alarm.setObjectName(u"lineEdit_Horas_Alarm")
        self.lineEdit_Horas_Alarm.setMaximumSize(QSize(60, 50))
        self.lineEdit_Horas_Alarm.setStyleSheet(u"text-align:center;\n"
"font: 75 36pt \"Century Gothic\";")

        self.horizontalLayout_25.addWidget(self.lineEdit_Horas_Alarm)

        self.lblseparador_8 = QLabel(self.groupBox_13)
        self.lblseparador_8.setObjectName(u"lblseparador_8")
        self.lblseparador_8.setStyleSheet(u"font: 75 36pt \"Century Gothic\";")
        self.lblseparador_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.lblseparador_8)

        self.lineEdit_Minutos_Alarm = QLineEdit(self.groupBox_13)
        self.lineEdit_Minutos_Alarm.setObjectName(u"lineEdit_Minutos_Alarm")
        self.lineEdit_Minutos_Alarm.setMaximumSize(QSize(65, 50))
        self.lineEdit_Minutos_Alarm.setStyleSheet(u"\n"
"text-align:center;\n"
"font: 75 36pt \"Century Gothic\";")

        self.horizontalLayout_25.addWidget(self.lineEdit_Minutos_Alarm)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_11)


        self.verticalLayout_24.addLayout(self.horizontalLayout_25)

        self.verticalSpacer_27 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_24.addItem(self.verticalSpacer_27)


        self.verticalLayout_26.addWidget(self.groupBox_13)

        self.label_38 = QLabel(self.Alarm_page)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_26.addWidget(self.label_38)

        self.groupBox_14 = QGroupBox(self.Alarm_page)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_25.setSpacing(11)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.comboBoxTonosAlarma_Alarm = QComboBox(self.groupBox_14)
        self.comboBoxTonosAlarma_Alarm.setObjectName(u"comboBoxTonosAlarma_Alarm")
        self.comboBoxTonosAlarma_Alarm.setStyleSheet(u"background-color: rgb(111, 1, 1);\n"
"font: 8pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_25.addWidget(self.comboBoxTonosAlarma_Alarm)

        self.verticalSpacer_28 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_25.addItem(self.verticalSpacer_28)

        self.label_37 = QLabel(self.groupBox_14)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_25.addWidget(self.label_37)

        self.verticalSpacer_29 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_25.addItem(self.verticalSpacer_29)

        self.lineEdit_NombreAlarm = QLineEdit(self.groupBox_14)
        self.lineEdit_NombreAlarm.setObjectName(u"lineEdit_NombreAlarm")
        self.lineEdit_NombreAlarm.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_25.addWidget(self.lineEdit_NombreAlarm)

        self.verticalSpacer_30 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_25.addItem(self.verticalSpacer_30)

        self.label_39 = QLabel(self.groupBox_14)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_25.addWidget(self.label_39)

        self.comboBoxRepetirAlarm = QComboBox(self.groupBox_14)
        self.comboBoxRepetirAlarm.setObjectName(u"comboBoxRepetirAlarm")
        self.comboBoxRepetirAlarm.setStyleSheet(u"background-color: rgb(111, 1, 1);\n"
"font: 8pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_25.addWidget(self.comboBoxRepetirAlarm)

        self.verticalSpacer_32 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_25.addItem(self.verticalSpacer_32)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.btn_Guardar_Alarm = QPushButton(self.groupBox_14)
        self.btn_Guardar_Alarm.setObjectName(u"btn_Guardar_Alarm")
        self.btn_Guardar_Alarm.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(111, 1, 1);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(58, 0, 0);\n"
"}")
        self.btn_Guardar_Alarm.setIcon(icon6)
        self.btn_Guardar_Alarm.setIconSize(QSize(40, 40))
        self.btn_Guardar_Alarm.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.btn_Guardar_Alarm)

        self.btn_Limpiar_Alarm = QPushButton(self.groupBox_14)
        self.btn_Limpiar_Alarm.setObjectName(u"btn_Limpiar_Alarm")
        self.btn_Limpiar_Alarm.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(111, 1, 1);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(58, 0, 0);\n"
"}")
        self.btn_Limpiar_Alarm.setIcon(icon6)
        self.btn_Limpiar_Alarm.setIconSize(QSize(40, 40))
        self.btn_Limpiar_Alarm.setAutoExclusive(True)

        self.horizontalLayout_26.addWidget(self.btn_Limpiar_Alarm)


        self.verticalLayout_25.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_31 = QSpacerItem(8, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_25.addItem(self.verticalSpacer_31)


        self.verticalLayout_26.addWidget(self.groupBox_14)

        self.stackedWidget.addWidget(self.Alarm_page)
        self.Regis_page = QWidget()
        self.Regis_page.setObjectName(u"Regis_page")
        self.verticalLayout_27 = QVBoxLayout(self.Regis_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_40 = QLabel(self.Regis_page)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(200, 40))
        self.label_40.setMaximumSize(QSize(16777215, 40))
        self.label_40.setStyleSheet(u"font: 75 20pt \"Century Gothic\";\n"
"background-color: rgb(59, 0, 29);")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_40)

        self.tableRegistro = QTableWidget(self.Regis_page)
        if (self.tableRegistro.columnCount() < 4):
            self.tableRegistro.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableRegistro.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableRegistro.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableRegistro.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableRegistro.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableRegistro.setObjectName(u"tableRegistro")
        self.tableRegistro.horizontalHeader().setVisible(True)
        self.tableRegistro.horizontalHeader().setDefaultSectionSize(125)
        self.tableRegistro.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.tableRegistro)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lblMensajeBorrar = QLabel(self.Regis_page)
        self.lblMensajeBorrar.setObjectName(u"lblMensajeBorrar")
        self.lblMensajeBorrar.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_27.addWidget(self.lblMensajeBorrar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer)

        self.btn_Actualizar = QPushButton(self.Regis_page)
        self.btn_Actualizar.setObjectName(u"btn_Actualizar")
        self.btn_Actualizar.setMaximumSize(QSize(60, 40))
        self.btn_Actualizar.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(59, 0, 29);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(34, 0, 17);\n"
"}")
        self.btn_Actualizar.setIcon(icon5)
        self.btn_Actualizar.setIconSize(QSize(40, 40))

        self.horizontalLayout_27.addWidget(self.btn_Actualizar)


        self.verticalLayout_27.addLayout(self.horizontalLayout_27)

        self.stackedWidget.addWidget(self.Regis_page)
        self.User_page = QWidget()
        self.User_page.setObjectName(u"User_page")
        self.verticalLayout_13 = QVBoxLayout(self.User_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_41 = QLabel(self.User_page)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(200, 40))
        self.label_41.setMaximumSize(QSize(16777215, 40))
        self.label_41.setStyleSheet(u"font: 75 20pt \"Century Gothic\";\n"
"background-color: rgb(59, 0, 29);")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_41)

        self.frame = QFrame(self.User_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.comboBox_SelectUser = QComboBox(self.frame)
        self.comboBox_SelectUser.setObjectName(u"comboBox_SelectUser")
        self.comboBox_SelectUser.setStyleSheet(u"background-color: rgb(59, 0, 29);\n"
"font: 10pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.comboBox_SelectUser)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(40, 40))
        self.label_15.setMaximumSize(QSize(150, 150))
        self.label_15.setPixmap(QPixmap(u":/newPrefix/Iconos/Userio_con.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_15)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.lblUsername = QLabel(self.frame)
        self.lblUsername.setObjectName(u"lblUsername")

        self.horizontalLayout_12.addWidget(self.lblUsername)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_13.addWidget(self.label_19)

        self.lblPass = QLabel(self.frame)
        self.lblPass.setObjectName(u"lblPass")

        self.horizontalLayout_13.addWidget(self.lblPass)


        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.lblcorreo = QLabel(self.frame)
        self.lblcorreo.setObjectName(u"lblcorreo")

        self.horizontalLayout_14.addWidget(self.lblcorreo)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_28.addWidget(self.label_13)

        self.lblTelefono = QLabel(self.frame)
        self.lblTelefono.setObjectName(u"lblTelefono")

        self.horizontalLayout_28.addWidget(self.lblTelefono)


        self.verticalLayout_11.addLayout(self.horizontalLayout_28)


        self.horizontalLayout_29.addLayout(self.verticalLayout_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_29)


        self.verticalLayout_13.addWidget(self.frame)

        self.groupBox_4 = QGroupBox(self.User_page)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(50, 0))
        self.label_16.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_5.addWidget(self.label_16)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.lineEdit_Username = QLineEdit(self.groupBox_4)
        self.lineEdit_Username.setObjectName(u"lineEdit_Username")
        self.lineEdit_Username.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.lineEdit_Username)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_8.addWidget(self.label_20)

        self.horizontalSpacer_3 = QSpacerItem(47, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.lineEdit_Pass = QLineEdit(self.groupBox_4)
        self.lineEdit_Pass.setObjectName(u"lineEdit_Pass")
        self.lineEdit_Pass.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_8.addWidget(self.lineEdit_Pass)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_9.addWidget(self.label_17)

        self.horizontalSpacer_4 = QSpacerItem(77, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.lineEdit_Correo = QLineEdit(self.groupBox_4)
        self.lineEdit_Correo.setObjectName(u"lineEdit_Correo")
        self.lineEdit_Correo.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_9.addWidget(self.lineEdit_Correo)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.horizontalSpacer_5 = QSpacerItem(69, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.lineEdit_Telefono = QLineEdit(self.groupBox_4)
        self.lineEdit_Telefono.setObjectName(u"lineEdit_Telefono")
        self.lineEdit_Telefono.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_10.addWidget(self.lineEdit_Telefono)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_BorrarUser = QPushButton(self.groupBox_4)
        self.btn_BorrarUser.setObjectName(u"btn_BorrarUser")
        self.btn_BorrarUser.setMinimumSize(QSize(100, 40))
        self.btn_BorrarUser.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(59, 0, 29);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(34, 0, 17);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/Iconos/iconClose.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_BorrarUser.setIcon(icon7)
        self.btn_BorrarUser.setIconSize(QSize(40, 40))

        self.horizontalLayout_11.addWidget(self.btn_BorrarUser)

        self.btn_GuardarUser = QPushButton(self.groupBox_4)
        self.btn_GuardarUser.setObjectName(u"btn_GuardarUser")
        self.btn_GuardarUser.setMinimumSize(QSize(100, 40))
        self.btn_GuardarUser.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(59, 0, 29);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(34, 0, 17);\n"
"}")
        self.btn_GuardarUser.setIcon(icon6)
        self.btn_GuardarUser.setIconSize(QSize(40, 40))

        self.horizontalLayout_11.addWidget(self.btn_GuardarUser)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)


        self.verticalLayout_13.addWidget(self.groupBox_4)

        self.stackedWidget.addWidget(self.User_page)
        self.Infor_page = QWidget()
        self.Infor_page.setObjectName(u"Infor_page")
        self.verticalLayout_16 = QVBoxLayout(self.Infor_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.groupBox_5 = QGroupBox(self.Infor_page)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_21)

        self.verticalSpacer_12 = QSpacerItem(20, 29, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_12)

        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_22)

        self.verticalSpacer_11 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_11)

        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_23)

        self.frame_2 = QFrame(self.groupBox_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(150, 120))
        self.frame_2.setMaximumSize(QSize(16777215, 120))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_6 = QSpacerItem(151, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_6)

        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(100, 150))
        self.label_25.setPixmap(QPixmap(u":/newPrefix/Iconos/kewin.jpg"))
        self.label_25.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_25)

        self.horizontalSpacer_7 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_7)


        self.verticalLayout_14.addWidget(self.frame_2)

        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_14.addWidget(self.label_24)


        self.verticalLayout_15.addWidget(self.groupBox_5)

        self.btn_GuardarUser_2 = QPushButton(self.Infor_page)
        self.btn_GuardarUser_2.setObjectName(u"btn_GuardarUser_2")
        self.btn_GuardarUser_2.setMinimumSize(QSize(100, 40))
        self.btn_GuardarUser_2.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(59, 0, 29);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(34, 0, 17);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/Iconos/iconCheck.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_GuardarUser_2.setIcon(icon8)
        self.btn_GuardarUser_2.setIconSize(QSize(40, 40))

        self.verticalLayout_15.addWidget(self.btn_GuardarUser_2)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.stackedWidget.addWidget(self.Infor_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.frame_Botones = QWidget(self.centralwidget)
        self.frame_Botones.setObjectName(u"frame_Botones")
        self.frame_Botones.setStyleSheet(u"QWidget{\n"
"background-color: rgb(118, 0, 59);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(59, 0, 29);\n"
"text-align:left;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(34, 0, 17);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(34, 0, 17);\n"
"font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.frame_Botones)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, -1)
        self.label_2 = QLabel(self.frame_Botones)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(145, 60))
        self.label_2.setMaximumSize(QSize(100, 60))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/Iconos/TEMPOLARM.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_2)

        self.btn_Tempo_2 = QPushButton(self.frame_Botones)
        self.btn_Tempo_2.setObjectName(u"btn_Tempo_2")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/Iconos/iconTemporizador.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Tempo_2.setIcon(icon9)
        self.btn_Tempo_2.setIconSize(QSize(40, 40))
        self.btn_Tempo_2.setCheckable(True)
        self.btn_Tempo_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_Tempo_2)

        self.btn_Pom_2 = QPushButton(self.frame_Botones)
        self.btn_Pom_2.setObjectName(u"btn_Pom_2")
        self.btn_Pom_2.setLayoutDirection(Qt.LeftToRight)
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/Iconos/iconPomodoro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Pom_2.setIcon(icon10)
        self.btn_Pom_2.setIconSize(QSize(40, 40))
        self.btn_Pom_2.setCheckable(True)
        self.btn_Pom_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_Pom_2)

        self.btn_Alm_2 = QPushButton(self.frame_Botones)
        self.btn_Alm_2.setObjectName(u"btn_Alm_2")
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/Iconos/iconAlarma.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Alm_2.setIcon(icon11)
        self.btn_Alm_2.setIconSize(QSize(40, 40))
        self.btn_Alm_2.setCheckable(True)
        self.btn_Alm_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_Alm_2)

        self.btn_Reg_2 = QPushButton(self.frame_Botones)
        self.btn_Reg_2.setObjectName(u"btn_Reg_2")
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/Iconos/iconRegistro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Reg_2.setIcon(icon12)
        self.btn_Reg_2.setIconSize(QSize(40, 40))
        self.btn_Reg_2.setCheckable(True)
        self.btn_Reg_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_Reg_2)

        self.verticalSpacer_2 = QSpacerItem(20, 282, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btn_User_2 = QPushButton(self.frame_Botones)
        self.btn_User_2.setObjectName(u"btn_User_2")
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix/Iconos/Userio_con.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_User_2.setIcon(icon13)
        self.btn_User_2.setIconSize(QSize(40, 40))
        self.btn_User_2.setCheckable(True)
        self.btn_User_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_User_2)

        self.pushButton_13 = QPushButton(self.frame_Botones)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix/Iconos/iconCerrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon14)
        self.pushButton_13.setIconSize(QSize(40, 40))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_13)


        self.gridLayout.addWidget(self.frame_Botones, 0, 1, 1, 1)

        self.frame_Iconos = QWidget(self.centralwidget)
        self.frame_Iconos.setObjectName(u"frame_Iconos")
        self.frame_Iconos.setStyleSheet(u"QWidget{\n"
"background-color: rgb(118, 0, 59);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(59, 0, 29);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(34, 0, 17);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(34, 0, 17);\n"
"font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.frame_Iconos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_Iconos)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u":/newPrefix/Iconos/IconJSheshe_Opacy.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_Tempo_1 = QPushButton(self.frame_Iconos)
        self.btn_Tempo_1.setObjectName(u"btn_Tempo_1")
        self.btn_Tempo_1.setIcon(icon9)
        self.btn_Tempo_1.setIconSize(QSize(40, 40))
        self.btn_Tempo_1.setCheckable(True)
        self.btn_Tempo_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Tempo_1)

        self.btn_Pom_1 = QPushButton(self.frame_Iconos)
        self.btn_Pom_1.setObjectName(u"btn_Pom_1")
        self.btn_Pom_1.setIcon(icon10)
        self.btn_Pom_1.setIconSize(QSize(40, 40))
        self.btn_Pom_1.setCheckable(True)
        self.btn_Pom_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Pom_1)

        self.btn_Alm_1 = QPushButton(self.frame_Iconos)
        self.btn_Alm_1.setObjectName(u"btn_Alm_1")
        self.btn_Alm_1.setIcon(icon11)
        self.btn_Alm_1.setIconSize(QSize(40, 40))
        self.btn_Alm_1.setCheckable(True)
        self.btn_Alm_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Alm_1)

        self.btn_Reg_1 = QPushButton(self.frame_Iconos)
        self.btn_Reg_1.setObjectName(u"btn_Reg_1")
        self.btn_Reg_1.setIcon(icon12)
        self.btn_Reg_1.setIconSize(QSize(40, 40))
        self.btn_Reg_1.setCheckable(True)
        self.btn_Reg_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Reg_1)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 278, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_User_1 = QPushButton(self.frame_Iconos)
        self.btn_User_1.setObjectName(u"btn_User_1")
        self.btn_User_1.setIcon(icon13)
        self.btn_User_1.setIconSize(QSize(40, 40))
        self.btn_User_1.setCheckable(True)
        self.btn_User_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_User_1)

        self.pushButton_7 = QPushButton(self.frame_Iconos)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon14)
        self.pushButton_7.setIconSize(QSize(40, 40))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.frame_Iconos, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_menu.toggled.connect(self.frame_Iconos.setHidden)
        self.btn_menu.toggled.connect(self.frame_Botones.setVisible)
        self.btn_Reg_1.toggled.connect(self.btn_Reg_2.setChecked)
        self.btn_Alm_1.toggled.connect(self.btn_Alm_2.setChecked)
        self.btn_Pom_1.toggled.connect(self.btn_Pom_2.setChecked)
        self.btn_Tempo_1.toggled.connect(self.btn_Tempo_2.setChecked)
        self.btn_Tempo_2.toggled.connect(self.btn_Tempo_1.setChecked)
        self.btn_Pom_2.toggled.connect(self.btn_Pom_1.setChecked)
        self.btn_Alm_2.toggled.connect(self.btn_Alm_1.setChecked)
        self.btn_Reg_2.toggled.connect(self.btn_Reg_1.setChecked)
        self.btn_User_2.toggled.connect(self.btn_User_1.setChecked)
        self.btn_User_1.toggled.connect(self.btn_User_2.setChecked)
        self.pushButton_7.toggled.connect(MainWindow.close)
        self.pushButton_13.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.btn_Inicio.setText("")
        self.label_8.setText("")
        self.btn_Info.setText("")
        self.lbl_Bienvenida.setText(QCoreApplication.translate("MainWindow", u"BIENVENIDO!", None))
        self.lbl_icon.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TEMPORIZADOR", None))
        self.groupBox_3.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"HORAS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"MINUTOS", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"SEGUNDOS", None))
        self.lineEdit_Horas_Temp.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lblseparador.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.lineEdit_Minutos_Temp.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lblseparador_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.lineEdit_Segundos_Temp.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.btn_Pausa_Temp.setText(QCoreApplication.translate("MainWindow", u"PAUSAR", None))
        self.btn_Iniciar_Temp.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.btn_Reiniciar_Temp.setText(QCoreApplication.translate("MainWindow", u"REINICIAR", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"TONO DE ALARMA", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DE TEMPORIZADOR:", None))
        self.lineEdit_NombreTemp.setText("")
        self.btn_Guardar_Temp.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.btn_Limpiar_Temp.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GUARDADOS:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"POMODORO", None))
        self.groupBox_10.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"MINUTOS", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"SEGUNDOS", None))
        self.lineEdit_Minutos_Pom.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lblseparador_7.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.lineEdit_Segundos_Pom.setInputMask("")
        self.lineEdit_Segundos_Pom.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.btn_Pausa_Pom.setText(QCoreApplication.translate("MainWindow", u"PAUSAR", None))
        self.btn_Iniciar_Pom.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.btn_Reiniciar_Pom.setText(QCoreApplication.translate("MainWindow", u"REINICIAR", None))
        self.groupBox_11.setTitle("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"TIEMPO POMODORO", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TIEMPO DESCANSO", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"DESCANSO LARGO", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"PERIODOS", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TONO DE ALARMA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.btn_Guardar_Pom.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.btn_Limpiar_Pom.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"GUARDADOS:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"ALARMA", None))
        self.groupBox_13.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HORAS", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"MINUTOS", None))
        self.lineEdit_Horas_Alarm.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lblseparador_8.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.lineEdit_Minutos_Alarm.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"CONFIGUAR NUEVA ALARMA:", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"TONO DE ALARMA", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DE TEMPORIZADOR:", None))
        self.lineEdit_NombreAlarm.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"REPETIR", None))
        self.btn_Guardar_Alarm.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.btn_Limpiar_Alarm.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"REGISTRO", None))
        ___qtablewidgetitem = self.tableRegistro.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.tableRegistro.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tiempo Registrado", None));
        ___qtablewidgetitem2 = self.tableRegistro.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tono", None));
        ___qtablewidgetitem3 = self.tableRegistro.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Repetir", None));
        self.lblMensajeBorrar.setText("")
        self.btn_Actualizar.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"USUARIOS", None))
        self.comboBox_SelectUser.setCurrentText("")
        self.label_15.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"USUARIO:", None))
        self.lblUsername.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A:", None))
        self.lblPass.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CORREO:", None))
        self.lblcorreo.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TELEFONO:", None))
        self.lblTelefono.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"USUARIO:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CORREO:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TELEFONO:", None))
        self.btn_BorrarUser.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR", None))
        self.btn_GuardarUser.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Acerca de:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\"TEMPOLARM\"", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"________________________________________________", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Es una aplicaci\u00f3n de gesti\u00f3n de tiempo\n"
" multiprop\u00f3sito que combina \n"
"un temporizador, una alarma y un \n"
"temporizador Pomodoro. La aplicaci\u00f3n \n"
"permitir\u00e1 alos usuarios configurar y\n"
" gestionar diferentes tipos de \n"
"temporizadores seg\u00fan sus necesidades, \n"
"con la capacidad de iniciar, pausar, \n"
"reiniciar y salir de cada uno deellos. \n"
"Adem\u00e1s, la aplicaci\u00f3n incluir\u00e1 un ring \n"
"de 3 segundos que se activar\u00e1 al \n"
"finalizar cada temporizador.", None))
        self.label_25.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u00a9alba\u00f1ilesdesoftware", None))
        self.btn_GuardarUser_2.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.label_2.setText("")
        self.btn_Tempo_2.setText(QCoreApplication.translate("MainWindow", u"Temporizador", None))
        self.btn_Pom_2.setText(QCoreApplication.translate("MainWindow", u"Pomodoro", None))
        self.btn_Alm_2.setText(QCoreApplication.translate("MainWindow", u"Alarma", None))
        self.btn_Reg_2.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.btn_User_2.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.label.setText("")
        self.btn_Tempo_1.setText("")
        self.btn_Pom_1.setText("")
        self.btn_Alm_1.setText("")
        self.btn_Reg_1.setText("")
        self.btn_User_1.setText("")
        self.pushButton_7.setText("")
    # retranslateUi

