import unittest
from PyQt5.QtCore import QTime
from Proyecto_Tempolarm.src.logica.inicioTempolarm import Mysidebar

class TestTempolarm(unittest.TestCase):
    def test_start_timer_no_time_input(self):
        tempolarm = Mysidebar()
        tempolarm.lineEdit_Horas_Temp.setText("")
        tempolarm.lineEdit_Minutos_Temp.setText("")
        tempolarm.lineEdit_Segundos_Temp.setText("")
        tempolarm.start_timer()
        self.assertEqual(tempolarm.tiempo_limite, QTime(0, 0, 0))
        self.assertFalse(tempolarm.timer.isActive())

if __name__ == '__main__':
    unittest.main()
