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

        # Conexiones para Temp_page
        self.btn_Iniciar_Temp.clicked.connect(self.start_timer)
        self.btn_Pausa_Temp.clicked.connect(self.pause_timer)
        self.btn_Reiniciar_Temp.clicked.connect(self.reset_timer)


        # Conexiones para Pomodoro

        self.btn_Iniciar_Pom.clicked.connect(self.start_pomodoro)
        self.btn_Pausa_Pom.clicked.connect(self.pause_pomodoro)
        self.btn_Reiniciar_Pom.clicked.connect(self.reset_pomodoro)

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

        ##CONFIGURACIÓN TIEMPO

        # Timer para el conteo de tiempo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer_display)

        # Variables para almacenar tiempo
        self.tiempo_limite = QTime(0, 0, 0)
        self.tiempo_actual = QTime(0, 0, 0)
        self.timer_paused = False  # Bandera para indicar si el temporizador está pausado

        # Mostrar "00" en los QLineEdits al inicio
        self.lineEdit_Horas_Temp.setText("00")
        self.lineEdit_Minutos_Temp.setText("00")
        self.lineEdit_Segundos_Temp.setText("00")

        # Variables para Pomodoro
        self.pomodoro_timer = QTimer(self)
        self.pomodoro_timer.timeout.connect(self.update_pomodoro_display)
        self.pomodoro_running = False
        self.pomodoro_duration = QTime(0, 20, 0)  # Duración inicial de Pomodoro (20 minutos)
        self.short_break_duration = QTime(0, 5, 0)  # Duración de descanso corto (5 minutos)
        self.long_break_duration = QTime(0, 15, 0)  # Duración de descanso largo (15 minutos)
        self.current_pomodoro_type = 'Pomodoro'
        self.pomodoro_count = 0

        # Configuración de SpinBoxes
        self.spinBox_tmpPomodoro.setMinimum(20)
        self.spinBox_tmpPomodoro.setSingleStep(5)
        self.spinBox_tmpDescanso.setSingleStep(5)
        self.spinBox_tmpDescLargo.setValue(15)
        self.spinBox_tmpPeriodos.setMinimum(4)

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


    ##CONFIGURACIÓN TEMPORIZADOR


    def start_timer(self):
        # Obtener tiempo ingresado
        horas = int(self.lineEdit_Horas_Temp.text()) if self.lineEdit_Horas_Temp.text() else 0
        minutos = int(self.lineEdit_Minutos_Temp.text()) if self.lineEdit_Minutos_Temp.text() else 0
        segundos = int(self.lineEdit_Segundos_Temp.text()) if self.lineEdit_Segundos_Temp.text() else 0

        # Configurar tiempo límite
        self.tiempo_limite = QTime(horas, minutos, segundos)

        # Iniciar temporizador solo si no está corriendo y no está pausado
        if not self.timer.isActive() and not self.timer_paused:
            self.tiempo_actual = QTime(0, 0, 0)
            self.timer.start(1000)  # Actualizar cada segundo


    def pause_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.timer_paused = True
        else:
            self.timer.start(1000)  # Reanudar el temporizador
            self.timer_paused = False

    def reset_timer(self):
        self.timer.stop()
        self.tiempo_limite = QTime(0, 0, 0)
        self.tiempo_actual = QTime(0, 0, 0)
        self.lineEdit_Horas_Temp.setText("00")
        self.lineEdit_Minutos_Temp.setText("00")
        self.lineEdit_Segundos_Temp.setText("00")
        self.timer_paused = False  # Reiniciar bandera de pausa

    def update_timer_display(self):
        if not self.timer_paused:
            # Incrementar tiempo actual solo si no está pausado
            self.tiempo_actual = self.tiempo_actual.addSecs(1)

        # Mostrar tiempo actual en los QLineEdits
        self.lineEdit_Horas_Temp.setText(str(self.tiempo_actual.hour()).zfill(2))
        self.lineEdit_Minutos_Temp.setText(str(self.tiempo_actual.minute()).zfill(2))
        self.lineEdit_Segundos_Temp.setText(str(self.tiempo_actual.second()).zfill(2))

        # Comprobar si se alcanzó el tiempo límite
        if self.tiempo_actual >= self.tiempo_limite:
            self.timer.stop()
            # Aquí podrías agregar la lógica para reproducir el tono de alarma seleccionado
            QMessageBox.information(self, "Tiempo Finalizado", "El tiempo termino.")
            return

    ##CONFIGURACIÓN POMODORO

    #CONFIGURACIÓN BOTONES
    def start_pomodoro(self):
        if not self.pomodoro_timer.isActive():
            self.pomodoro_running = True
            self.update_pomodoro_duration()
            self.pomodoro_timer.start(1000)  # Inicia el timer con intervalo de 1 segundo

    def pause_pomodoro(self):
        self.pomodoro_timer.stop()

    def reset_pomodoro(self):
        self.pomodoro_timer.stop()
        self.pomodoro_running = False
        self.pomodoro_count = 0
        self.current_pomodoro_type = 'Pomodoro'
        self.update_pomodoro_duration()
        self.update_pomodoro_display()

    # EN LA PANTALLA
    def update_pomodoro_display(self):
        if self.pomodoro_running:
            self.pomodoro_duration = self.pomodoro_duration.addSecs(-1)
            if self.pomodoro_duration == QTime(0, 0, 0):
                self.show_notification(self.current_pomodoro_type + ' terminado')
                self.next_pomodoro()
        self.lineEdit_Minutos_Pom.setText(self.pomodoro_duration.toString("mm"))
        self.lineEdit_Segundos_Pom.setText(self.pomodoro_duration.toString("ss"))

    ##SECUENCIA POMODORO

    def next_pomodoro(self):
        if self.current_pomodoro_type == 'Pomodoro':
            self.pomodoro_count += 1
            if self.pomodoro_count % self.spinBox_tmpPeriodos.value() == 0:
                self.current_pomodoro_type = 'Descanso Largo'
                self.pomodoro_duration = self.long_break_duration
            else:
                self.current_pomodoro_type = 'Descanso Corto'
                self.pomodoro_duration = self.short_break_duration
        else:
            self.current_pomodoro_type = 'Pomodoro'
            self.pomodoro_duration = QTime(0, self.spinBox_tmpPomodoro.value(), 0)
        self.update_pomodoro_display()

    def update_pomodoro_duration(self):
        if self.current_pomodoro_type == 'Pomodoro':
            self.pomodoro_duration = QTime(0, self.spinBox_tmpPomodoro.value(), 0)
        elif self.current_pomodoro_type == 'Descanso Corto':
            self.pomodoro_duration = self.short_break_duration
        elif self.current_pomodoro_type == 'Descanso Largo':
            self.pomodoro_duration = self.long_break_duration
        # Asegurarse de que la interfaz se actualice al reiniciar
        self.lineEdit_Minutos_Pom.setText(self.pomodoro_duration.toString("mm"))
        self.lineEdit_Segundos_Pom.setText(self.pomodoro_duration.toString("ss"))