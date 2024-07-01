from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define el motor de la base de datos
engine = create_engine('sqlite:///base_de_datos.db', echo=True)
# Define la clase base para las clases de modelos
Base = declarative_base()

# Definir el modelo de la tabla Usuarios
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    correo = Column(String)
    telefono = Column(String)

class Temporizador(Base):
    __tablename__ = 'temporizador'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    horas = Column(Integer)
    minutos = Column(Integer)
    segundos = Column(Integer)
    tono = Column(String)

class Pomodoro(Base):
    __tablename__ = 'pomodoros'

    id = Column(Integer, primary_key=True)
    minutos_pomodoro = Column(Integer)
    segundos_pomodoro = Column(Integer)
    tiempo_pomodoro = Column(Integer)
    tiempo_descanso_corto = Column(Integer)
    tiempo_descanso_largo = Column(Integer)
    numero_periodos = Column(Integer)
    tono_alarma = Column(String)
    nombre = Column(String)


class Alarma(Base):
    __tablename__ = 'alarma'

    id = Column(Integer, primary_key=True)
    horas = Column(Integer)
    minutos = Column(Integer)
    tono = Column(String)
    nombre = Column(String)
    repetir = Column(String)

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Función para crear un nuevo usuario en la base de datos
def crear_usuario(username, password, correo, telefono):
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    nuevo_usuario = Usuario(username=username, password=password, correo=correo, telefono=telefono)
    session.add(nuevo_usuario)
    session.commit()
    session.close()

# Función para obtener todos los usuarios de la base de datos
def obtener_usuarios():
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    usuarios = session.query(Usuario).all()
    session.close()
    return usuarios

def borrar_usuario(username):
    Session = sessionmaker(bind=engine)
    session = Session()
    usuario = session.query(Usuario).filter_by(username=username).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        session.close()
    else:
        session.close()
        raise Exception(f"No se encontró el usuario con nombre de usuario '{username}' en la base de datos.")


##************************************************************************************************************************

# Función para crear un nuevo temporizador en la base de datos
def crear_temporizador(nombre, horas, minutos, segundos, tono):
    Session = sessionmaker(bind=engine)
    session = Session()
    nuevo_temporizador = Temporizador(nombre=nombre, horas=horas, minutos=minutos, segundos=segundos, tono=tono)
    session.add(nuevo_temporizador)
    session.commit()
    session.close()

# Función para obtener todos los temporizadores de la base de datos
def obtener_temporizadores():
    Session = sessionmaker(bind=engine)
    session = Session()
    temporizadores = session.query(Temporizador).all()
    session.close()
    return temporizadores

# Función para borrar un temporizador de la base de datos
def borrar_temporizador(nombre):
    Session = sessionmaker(bind=engine)
    session = Session()
    temporizador = session.query(Temporizador).filter_by(nombre=nombre).first()
    if temporizador:
        session.delete(temporizador)
        session.commit()
        session.close()
    else:
        session.close()
        raise Exception(f"No se encontró el temporizador con nombre '{nombre}' en la base de datos.")

##************************************************************************************************************************

# Función para crear un nuevo pomodoro en la base de datos
# Función para crear un nuevo temporizador en la base de datos
def crear_pomodoro(minutos_pomodoro, segundos_pomodoro, tiempo_pomodoro, tiempo_descanso_corto,
                   tiempo_descanso_largo, numero_periodos, tono_alarma, nombre):
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    nuevo_pomodoro = Pomodoro(minutos_pomodoro=minutos_pomodoro, segundos_pomodoro=segundos_pomodoro,
                              tiempo_pomodoro=tiempo_pomodoro, tiempo_descanso_corto=tiempo_descanso_corto,
                              tiempo_descanso_largo=tiempo_descanso_largo, numero_periodos=numero_periodos,
                              tono_alarma=tono_alarma, nombre=nombre)
    session.add(nuevo_pomodoro)
    session.commit()
    session.close()


# Función para obtener todos los pomodoros de la base de datos
def obtener_pomodoros():
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    pomodoros = session.query(Pomodoro).all()
    session.close()
    return pomodoros

# Función para borrar un pomodoro de la base de datos por nombre
def borrar_pomodoro(nombre):
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    pomodoro = session.query(Pomodoro).filter_by(nombre=nombre).first()
    if pomodoro:
        session.delete(pomodoro)
        session.commit()
        session.close()
    else:
        session.close()
        raise Exception(f"No se encontró el pomodoro con nombre '{nombre}' en la base de datos.")

##************************************************************************************************************************

# Función para crear una nueva alarma en la base de datos
def crear_alarma(horas, minutos, tono, nombre, repetir):
    Session = sessionmaker(bind=engine)
    session = Session()
    nueva_alarma = Alarma(horas=horas, minutos=minutos, tono=tono, nombre=nombre, repetir=repetir)
    session.add(nueva_alarma)
    session.commit()
    session.close()

# Función para obtener todas las alarmas de la base de datos
def obtener_alarmas():
    Session = sessionmaker(bind=engine)
    session = Session()
    alarmas = session.query(Alarma).all()
    session.close()
    return alarmas

# Función para borrar una alarma de la base de datos por nombre
def borrar_alarma(nombre):
    Session = sessionmaker(bind=engine)
    session = Session()
    alarma = session.query(Alarma).filter_by(nombre=nombre).first()
    if (alarma):
        session.delete(alarma)
        session.commit()
        session.close()
    else:
        session.close()
        raise Exception(f"No se encontró la alarma con nombre '{nombre}' en la base de datos.")


def obtener_todos_los_registros():
    Session = sessionmaker(bind=engine)
    session = Session()

    temporizadores = session.query(Temporizador).all()
    pomodoros = session.query(Pomodoro).all()
    alarmas = session.query(Alarma).all()

    session.close()

    return temporizadores, pomodoros, alarmas