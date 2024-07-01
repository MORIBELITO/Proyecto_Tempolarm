from Proyecto_Tempolarm.src.vista.menuGUI import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTime, QTimer
from PySide6.QtGui import QIntValidator
from Proyecto_Tempolarm.src.logica.db_model import crear_usuario, obtener_usuarios, borrar_usuario
from Proyecto_Tempolarm.src.logica.db_model import crear_temporizador, obtener_temporizadores
from Proyecto_Tempolarm.src.logica.db_model import crear_pomodoro, obtener_pomodoros
from Proyecto_Tempolarm.src.logica.db_model import crear_alarma, obtener_alarmas

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
        self.reset_timer()  # Reinicia el contador al cambiar a esta página

        # Actualiza ComboBox de tonos de alarma al cambiar a la página de temporizador
        self.comboBoxTonosAlarma_Temp.clear()
        self.comboBoxTonosAlarma_Temp.addItems(["Tono 1", "Tono 2", "Tono 3", "Tono 4"])


    def switch_to_Pom_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.reset_pomodoro()  # Reinicia el contador Pomodoro al cambiar a esta página
        ##Alarma
        self.comboBoxtonoAlarmaPom.clear()
        self.comboBoxtonoAlarmaPom.addItems(["Tono 1", "Tono 2", "Tono 3", "Tono 4"])


    def switch_to_Alarm_page(self):
        self.stackedWidget.setCurrentIndex(3)
        # Actualiza ComboBox de tonos de alarma al cambiar a la página de Alarma
        self.comboBoxTonosAlarma_Alarm.clear()
        self.comboBoxTonosAlarma_Alarm.addItems(["Tono 1", "Tono 2", "Tono 3", "Tono 4"])

        self.comboBoxRepetirAlarm.clear()
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.comboBoxRepetirAlarm.addItems(dias_semana)


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

    def save_timer(self):
        # Obtener valores de los campos
        nombre = self.lineEdit_NombreTemp.text()
        horas = int(self.lineEdit_Horas_Temp.text()) if self.lineEdit_Horas_Temp.text() else 0
        minutos = int(self.lineEdit_Minutos_Temp.text()) if self.lineEdit_Minutos_Temp.text() else 0
        segundos = int(self.lineEdit_Segundos_Temp.text()) if self.lineEdit_Segundos_Temp.text() else 0
        tono = self.comboBoxTonosAlarma_Temp.currentText()


        # Verificar si el nombre ya existe en la base de datos
        temporizadores = obtener_temporizadores()
        for temp in temporizadores:
            if temp.nombre == nombre:
                QMessageBox.information(self, "Nombre ya existe",
                                        "Una configuración con ese nombre ya existe. Por favor, elija otro nombre.")
                return

        # Guardar en la base de datos
        crear_temporizador(nombre, horas, minutos, segundos, tono)

        # Recargar las configuraciones guardadas en el combo box
        self.load_saved_configs()

    def clear_fields(self):
        self.lineEdit_Horas_Temp.setText("00")
        self.lineEdit_Minutos_Temp.setText("00")
        self.lineEdit_Segundos_Temp.setText("00")
        self.lineEdit_NombreTemp.clear()
        self.comboBoxTonosAlarma_Temp.setCurrentIndex(0)

    def load_saved_configs(self):
        # Obtener configuraciones guardadas de la base de datos
        temporizadores = obtener_temporizadores()

        # Limpiar comboBox y agregar configuraciones guardadas
        self.comboBoxConfigGuardadasTemp.clear()
        self.comboBoxConfigGuardadasTemp.addItem("Seleccione una configuración", None)
        for temp in temporizadores:
            self.comboBoxConfigGuardadasTemp.addItem(temp.nombre, temp)

    def load_selected_config(self):
        # Obtener la configuración seleccionada
        index = self.comboBoxConfigGuardadasTemp.currentIndex()
        if index > 0:  # Ignorar el índice 0 que es "Seleccione una configuración"
            temporizador = self.comboBoxConfigGuardadasTemp.itemData(index)

            # Cargar la configuración en los campos del temporizador
            self.lineEdit_NombreTemp.setText(temporizador.nombre)
            self.lineEdit_Horas_Temp.setText(str(temporizador.horas).zfill(2))
            self.lineEdit_Minutos_Temp.setText(str(temporizador.minutos).zfill(2))
            self.lineEdit_Segundos_Temp.setText(str(temporizador.segundos).zfill(2))
            self.comboBoxTonosAlarma_Temp.setCurrentText(temporizador.tono)
        else:
            self.clear_fields()

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

    def save_pomodoro(self):
        # Obtener valores de los campos
        minutos_pomodoro = int(self.lineEdit_Minutos_Pom.text()) if self.lineEdit_Minutos_Pom.text() else 0
        segundos_pomodoro = int(self.lineEdit_Segundos_Pom.text()) if self.lineEdit_Segundos_Pom.text() else 0
        tiempo_pomodoro = self.spinBox_tmpPomodoro.value()
        tiempo_descanso_corto = self.spinBox_tmpDescanso.value()
        tiempo_descanso_largo = self.spinBox_tmpDescLargo.value()
        numero_periodos = self.spinBox_tmpPeriodos.value()
        tono_alarma = self.comboBoxtonoAlarmaPom.currentText()
        nombre = self.lineEdit_NombrePom.text()

        # Guardar en la base de datos
        crear_pomodoro(minutos_pomodoro, segundos_pomodoro, tiempo_pomodoro, tiempo_descanso_corto,
                       tiempo_descanso_largo, numero_periodos, tono_alarma, nombre)

        # Recargar las configuraciones guardadas en el combo box
        self.load_saved_configs_Pom()

    def clear_pomodoro_fields(self):
        self.lineEdit_Minutos_Pom.clear()
        self.lineEdit_Segundos_Pom.clear()
        self.spinBox_tmpPomodoro.setValue(25)
        self.spinBox_tmpDescanso.setValue(5)
        self.spinBox_tmpDescLargo.setValue(15)
        self.spinBox_tmpPeriodos.setValue(4)
        self.comboBoxtonoAlarmaPom.setCurrentIndex(0)
        self.lineEdit_NombrePom.clear()

    def load_saved_configs_Pom(self):
        # Obtener configuraciones guardadas de la base de datos
        pomodoros = obtener_pomodoros()

        # Limpiar comboBox y agregar configuraciones guardadas
        self.comboBoxConfigGuardadasPom.clear()
        self.comboBoxConfigGuardadasPom.addItem("Seleccione una configuración", None)
        for pomodoro in pomodoros:
            self.comboBoxConfigGuardadasPom.addItem(pomodoro.nombre, pomodoro)

    def load_selected_config_Pom(self):
        # Obtener la configuración seleccionada
        index = self.comboBoxConfigGuardadasPom.currentIndex()
        if index > 0:  # Ignorar el índice 0 que es "Seleccione una configuración"
            pomodoro = self.comboBoxConfigGuardadasPom.itemData(index)

            # Cargar la configuración en los campos del Pomodoro
            self.lineEdit_NombrePom.setText(pomodoro.nombre)
            self.lineEdit_Minutos_Pom.setText(str(pomodoro.minutos_pomodoro).zfill(2))
            self.lineEdit_Segundos_Pom.setText(str(pomodoro.segundos_pomodoro).zfill(2))
            self.spinBox_tmpPomodoro.setValue(pomodoro.tiempo_pomodoro)
            self.spinBox_tmpDescanso.setValue(pomodoro.tiempo_descanso_corto)
            self.spinBox_tmpDescLargo.setValue(pomodoro.tiempo_descanso_largo)
            self.spinBox_tmpPeriodos.setValue(pomodoro.numero_periodos)
            self.comboBoxtonoAlarmaPom.setCurrentText(pomodoro.tono_alarma)
        else:
            self.clear_fields()  # Define esta función para limpiar los campos del formulario

#####ALARMA


    def save_alarm(self):
        # Obtener valores de los campos
        horas_alarma = int(self.lineEdit_Horas_Alarm.text()) if self.lineEdit_Horas_Alarm.text() else 0
        minutos_alarma = int(self.lineEdit_Minutos_Alarm.text()) if self.lineEdit_Minutos_Alarm.text() else 0
        tono_alarma = self.comboBoxTonosAlarma_Alarm.currentText()
        nombre_alarma = self.lineEdit_NombreAlarm.text()
        repetir_alarma = self.comboBoxRepetirAlarm.currentText()

        # Validar que el nombre no esté vacío
        if not nombre_alarma:
            QMessageBox.information(self, "Ingrese nombre", "Ingrese nombre de su configuración.")
            return

        if horas_alarma == 0 and minutos_alarma == 0:
            QMessageBox.information(self, "Campos vacíos",
                                    "Por favor, ingrese un tiempo mayor que 0 en al menos uno de los campos.")
            return

        # Verificar si el nombre ya existe en la base de datos
        alarmas = obtener_alarmas()
        for alarma in alarmas:
            if alarma.nombre == nombre_alarma:
                QMessageBox.information(self, "Nombre ya existe",
                                        "Una configuración con ese nombre ya existe. Por favor, elija otro nombre.")
                return

        # Guardar en la base de datos
        crear_alarma(horas_alarma, minutos_alarma, tono_alarma, nombre_alarma, repetir_alarma)


    # Función para limpiar los campos de entrada de la alarma
    def clear_alarm_fields(self):
        self.lineEdit_Horas_Alarm.setText("00")
        self.lineEdit_Minutos_Alarm.setText("00")
        self.comboBoxTonosAlarma_Alarm.setCurrentIndex(0)
        self.lineEdit_NombreAlarm.clear()
        self.comboBoxRepetirAlarm.setCurrentIndex(0)

    #CONFIGURACIÓN DE ERRORES
    def show_error_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def show_notification(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Notificación")
        msg_box.setText(message)
        msg_box.exec()


    ##CONFIGURACION USUARIO

    def actualizar_combo_usuarios(self):
        # Limpiar ComboBox antes de actualizar
        self.comboBox_SelectUser.clear()

        # Obtener usuarios de la base de datos
        usuarios = obtener_usuarios()

        # Llenar ComboBox con nombres de usuario
        for usuario in usuarios:
            self.comboBox_SelectUser.addItem(usuario.username)

    def guardar_usuario(self):
        # Obtener datos de los lineEdit
        username = self.lineEdit_Username.text()
        password = self.lineEdit_Pass.text()
        correo = self.lineEdit_Correo.text()
        telefono = self.lineEdit_Telefono.text()

        # Guardar en la base de datos usando la función del modelo
        crear_usuario(username, password, correo, telefono)

        # Actualizar ComboBox con el nuevo usuario
        self.actualizar_combo_usuarios()

        # Mostrar información en los QLabel
        self.lblUsername.setText(f' {username}')
        self.lblPass.setText(f' {password}')
        self.lblcorreo.setText(f' {correo}')
        self.lblTelefono.setText(f' {telefono}')

    def mostrar_usuario_seleccionado(self, index):
        # Obtener nombre de usuario seleccionado del ComboBox
        username = self.comboBox_SelectUser.currentText()

        # Obtener datos del usuario seleccionado de la base de datos
        usuarios = obtener_usuarios()
        for usuario in usuarios:
            if usuario.username == username:
                # Mostrar datos del usuario en los QLabel
                self.lblUsername.setText(f': {usuario.username}')
                self.lblPass.setText(f': {usuario.password}')
                self.lblcorreo.setText(f': {usuario.correo}')
                self.lblTelefono.setText(f': {usuario.telefono}')
                break

    def borrar_usuario_seleccionado(self):
        # Obtener nombre de usuario seleccionado del ComboBox
        username = self.comboBox_SelectUser.currentText()


        # Confirmar con el usuario antes de borrar
        reply = QMessageBox.question(self, 'Confirmar Borrado', f"¿Estás seguro de borrar al usuario {username}?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Borrar usuario de la base de datos
            borrar_usuario(username)
            QMessageBox.information(self, 'Usuario Borrado', f'El usuario {username} ha sido borrado.')

            # Limpiar datos mostrados
            self.lblUsername.setText('Nuevo Nombre')
            self.lblPass.setText('Nueva Contraseña')
            self.lblcorreo.setText('Nuevo Correo')
            self.lblTelefono.setText('Nuevo Teléfono')

            # Actualizar ComboBox después de borrar
            self.actualizar_combo_usuarios()