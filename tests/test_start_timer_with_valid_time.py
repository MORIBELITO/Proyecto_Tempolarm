import unittest
from PySide6.QtCore import QTime
from Proyecto_Tempolarm.src.logica.inicioTempolarm import Mysidebar

class TestTempolarm(unittest.TestCase):
    def test_start_timer_with_valid_time(self):
        tempolarm = Mysidebar()
        tempolarm.lineEdit_Horas_Temp.setText("0")
        tempolarm.lineEdit_Minutos_Temp.setText("1")
        tempolarm.lineEdit_Segundos_Temp.setText("30")
        tempolarm.start_timer()
        self.assertEqual(tempolarm.tiempo_limite, QTime(0, 1, 30))
        self.assertTrue(tempolarm.timer.isActive())

if __name__ == '__main__':
    unittest.main()
