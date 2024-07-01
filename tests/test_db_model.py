import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Proyecto_Tempolarm.src.logica.db_model import Base, Usuario, Temporizador, Pomodoro


class TestDatabaseModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Crear una base de datos en memoria para las pruebas
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    def test_create_user(self):
        # Crear un usuario
        new_user = Usuario(username='test_user', password='password123', correo='test@example.com',
                           telefono='123456789')
        self.session.add(new_user)
        self.session.commit()

        # Leer el usuario de la base de datos
        user = self.session.query(Usuario).filter_by(username='test_user').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'test_user')

    def test_create_temporizador(self):
        # Crear un temporizador
        new_temporizador = Temporizador(nombre='Morning Alarm', horas=7, minutos=30, segundos=0, tono='classic')
        self.session.add(new_temporizador)
        self.session.commit()

        # Leer el temporizador de la base de datos
        temporizador = self.session.query(Temporizador).filter_by(nombre='Morning Alarm').first()
        self.assertIsNotNone(temporizador)
        self.assertEqual(temporizador.nombre, 'Morning Alarm')

    def test_create_pomodoro(self):
        # Crear un pomodoro
        new_pomodoro = Pomodoro(minutos_pomodoro=25, segundos_pomodoro=0, tiempo_pomodoro=1500,
                                tiempo_descanso_corto=300)
        self.session.add(new_pomodoro)
        self.session.commit()

        # Leer el pomodoro de la base de datos
        pomodoro = self.session.query(Pomodoro).filter_by(minutos_pomodoro=25).first()
        self.assertIsNotNone(pomodoro)
        self.assertEqual(pomodoro.minutos_pomodoro, 25)


if __name__ == '__main__':
    unittest.main()
