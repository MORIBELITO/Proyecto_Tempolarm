import unittest

from unittest.mock import patch
from Proyecto_Tempolarm.src.logica.inicioTempolarm import Mysidebar


class TestSaveRecords(unittest.TestCase):

    @patch('inicioTempolarm.crear_temporizador')
    def test_save_temporizador(self, mock_crear_temporizador):
        atempolarm = Mysidebar()
        # Simulamos la entrada del usuario para crear un temporizador
        atempolarm.lineEdit_Horas_Temp.setText("1")
        atempolarm.lineEdit_Minutos_Temp.setText("30")
        atempolarm.lineEdit_Segundos_Temp.setText("0")
        atempolarm.start_timer()
        atempolarm.save_timer()  # Suponiendo que hay una función para guardar
        mock_crear_temporizador.assert_called_once()

    @patch('inicioTempolarm.crear_pomodoro')
    def test_save_pomodoro(self, mock_crear_pomodoro):
        btempolarm = Mysidebar()
        # Simulamos la creación de un pomodoro
        btempolarm.create_pomodoro(25, 5)  # Suponiendo que hay una función para crear pomodoro
        mock_crear_pomodoro.assert_called_once()

    @patch('inicioTempolarm.crear_alarma')
    def test_save_alarma(self, mock_crear_alarma):
        ctempolarm = Mysidebar()
        # Simulamos la entrada del usuario para crear una alarma
        ctempolarm.horas_alarma.setText("7")
        ctempolarm.minutos_alarma.setText("0")
        ctempolarm.save_alarm()  # Suponiendo que hay una función para guardar
        mock_crear_alarma.assert_called_once()

if __name__ == '__main__':
    unittest.main()
