import unittest
from unittest.mock import patch, MagicMock
from PySide6.QtWidgets import QApplication, QMessageBox
from Proyecto_Tempolarm.src.logica.inicioTempolarm import Mysidebar
from Proyecto_Tempolarm.src.logica.db_model import crear_usuario, obtener_usuarios, borrar_usuario

class TestMysidebar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.window = Mysidebar()

    def test_guardar_usuario(self):
        # Mocking QMessageBox to avoid actual dialog popup
        with patch.object(QMessageBox, 'critical', return_value=None):
            with patch('src.logica.inicioTempolarm.crear_usuario') as mock_crear_usuario:
                # Set test data
                self.window.lineEdit_Username.setText('testuser')
                self.window.lineEdit_Pass.setText('password')
                self.window.lineEdit_Correo.setText('test@example.com')
                self.window.lineEdit_Telefono.setText('1234567890')

                # Call guardar_usuario
                self.window.guardar_usuario()

                # Check if crear_usuario was called with correct parameters
                mock_crear_usuario.assert_called_with('testuser', 'password', 'test@example.com', '1234567890')

    def test_actualizar_combo_usuarios(self):
        with patch('src.logica.inicioTempolarm.obtener_usuarios', return_value=[
            MagicMock(username='user1'),
            MagicMock(username='user2')
        ]):
            self.window.actualizar_combo_usuarios()

            self.assertEqual(self.window.comboBox_SelectUser.count(), 2)
            self.assertEqual(self.window.comboBox_SelectUser.itemText(0), 'user1')
            self.assertEqual(self.window.comboBox_SelectUser.itemText(1), 'user2')

    def test_mostrar_usuario_seleccionado(self):
        with patch('src.logica.inicioTempolarm.obtener_usuarios', return_value=[
            MagicMock(username='testuser', password='password', correo='test@example.com', telefono='1234567890')
        ]):
            self.window.comboBox_SelectUser.addItem('testuser')
            self.window.comboBox_SelectUser.setCurrentIndex(0)

            self.window.mostrar_usuario_seleccionado(0)

            self.assertEqual(self.window.lblUsername.text(), ': testuser')
            self.assertEqual(self.window.lblPass.text(), ': password')
            self.assertEqual(self.window.lblcorreo.text(), ': test@example.com')
            self.assertEqual(self.window.lblTelefono.text(), ': 1234567890')

    def test_borrar_usuario_seleccionado(self):
        with patch.object(QMessageBox, 'question', return_value=QMessageBox.Yes):
            with patch('src.logica.inicioTempolarm.borrar_usuario') as mock_borrar_usuario:
                self.window.comboBox_SelectUser.addItem('testuser')
                self.window.comboBox_SelectUser.setCurrentIndex(0)

                self.window.borrar_usuario_seleccionado()

                mock_borrar_usuario.assert_called_with('testuser')

                self.assertEqual(self.window.comboBox_SelectUser.count(), 0)
                self.assertEqual(self.window.lblUsername.text(), 'Username:')
                self.assertEqual(self.window.lblPass.text(), 'Password:')
                self.assertEqual(self.window.lblcorreo.text(), 'Correo:')
                self.assertEqual(self.window.lblTelefono.text(), 'Teléfono:')

if __name__ == '__main__':
    unittest.main()
