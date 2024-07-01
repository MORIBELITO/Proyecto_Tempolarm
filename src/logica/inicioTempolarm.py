from Proyecto_Tempolarm.src.vista.menuGUI import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTime, QTimer
from PySide6.QtGui import QIntValidator

class Mysidebar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        #Ocultar barra iconos
        self.frame_Iconos.setHidden(True)

        # Conexiones de botones para cambiar de página
        self.btn_Inicio.clicked.connect(self.switch_to_Inicio_page)
        self.btn_Info.clicked.connect(self.switch_to_Infor_page)
        self.btn_Tempo_1.clicked.connect(self.switch_to_Temp_page)
        self.btn_Tempo_2.clicked.connect(self.switch_to_Temp_page)
        self.btn_Pom_1.clicked.connect(self.switch_to_Pom_page)
        self.btn_Pom_2.clicked.connect(self.switch_to_Pom_page)
        self.btn_Alm_1.clicked.connect(self.switch_to_Alarm_page)
        self.btn_Alm_2.clicked.connect(self.switch_to_Alarm_page)
        self.btn_Reg_1.clicked.connect(self.switch_to_Regis_page)
        self.btn_Reg_2.clicked.connect(self.switch_to_Regis_page)
        self.btn_User_1.clicked.connect(self.switch_to_User_page)
        self.btn_User_2.clicked.connect(self.switch_to_User_page)

    ##ALTERNAR ENTRE PAGINAS

    def switch_to_Inicio_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_Temp_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_Pom_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_Alarm_page(self):
        self.stackedWidget.setCurrentIndex(3)


    def switch_to_Regis_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_User_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_Infor_page(self):
        self.stackedWidget.setCurrentIndex(6)