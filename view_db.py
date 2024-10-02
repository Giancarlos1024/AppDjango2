import os
import sqlite3
from datetime import datetime
from django.conf import settings
from django.contrib.auth.hashers import make_password

# Configurar las configuraciones de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DocumentAutomation.settings')
import django
django.setup()

# Conectar a la base de datos
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Crear un nuevo usuario
username = 'giancarlos1024'
password = 'giancarlos123'
hashed_password = make_password(password)  # Usar Django para hashear la contraseña
first_name = 'giancarlos'
last_name = 'velasquez'
email = 'giancarlos@gmail.com'
is_superuser = 0
is_staff = 1
is_active = 1
date_joined = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
role = 'OPERATOR'

# Insertar el nuevo usuario en la tabla
cursor.execute("""
    INSERT INTO Administration_customuser (
        password, last_login, is_superuser, username, 
        first_name, last_name, email, is_staff, 
        is_active, date_joined, role
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (hashed_password, None, is_superuser, username, 
      first_name, last_name, email, is_staff, 
      is_active, date_joined, role))

# Confirmar los cambios
conn.commit()

print("Nuevo usuario creado con éxito.")

# Cerrar la conexión
conn.close()
