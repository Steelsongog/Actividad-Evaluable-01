############################################################

# ACTIVIDAD 03
# Partiendo de un contexto en el que queremos almacenar un usuario y su contraseña. Haz un ejemplo que explica cómo se haría:
# ● Utilizando una lista.
# ● Utilizando un diccionario.
# Al llenarse, las contraseñas deben pasarse a un formato Hash (por ejemplo
# SHAhttps://recursospython.com/guias-y-manuales/hashlib-md5-sha/). El ejemplo debe rellenar la
# lista con 5 usuarios/contraseña y realizar dos consultas.

import hashlib

class PasswordManager:
    def __init__(self):
        self.user_list = []  # Lista para almacenar usuarios y contraseñas
        self.user_dict = {}  # Diccionario para almacenar usuarios y contraseñas

    def add_user_password_list(self, user, password):
        hashed_password = self._hash_password(password)
        self.user_list.append((user, hashed_password))

    def add_user_password_dict(self, user, password):
        hashed_password = self._hash_password(password)
        self.user_dict[user] = hashed_password

    def _hash_password(self, password):
        # Utilizamos SHA-256 para hashear la contraseña
        hash_object = hashlib.sha256()
        hash_object.update(password.encode())
        hashed_password = hash_object.hexdigest()
        return hashed_password

    def print_user_passwords(self):
        print("Usuarios y contraseñas (Lista):")
        for user, hashed_password in self.user_list:
            print(f"Usuario: {user}, Contraseña (Hash): {hashed_password}")

        print("\nUsuarios y contraseñas (Diccionario):")
        for user, hashed_password in self.user_dict.items():
            print(f"Usuario: {user}, Contraseña (Hash): {hashed_password}")

# Crear instancia de la clase PasswordManager
password_manager = PasswordManager()

# Agregar usuarios/contraseñas a la lista y al diccionario
password_manager.add_user_list("user1", "password123")
password_manager.add_user_list("user2", "securepass")
password_manager.add_user_list("user3", "pythonrules")
password_manager.add_user_list("user4", "hashedpass")
password_manager.add_user_list("user5", "123456")

password_manager.add_user_dict("user1", "password123")
password_manager.add_user_dict("user2", "securepass")
password_manager.add_user_dict("user3", "pythonrules")
password_manager.add_user_dict("user4", "hashedpass")
password_manager.add_user_dict("user5", "123456")

# Imprimir usuarios y contraseñas
password_manager.print_user_passwords()