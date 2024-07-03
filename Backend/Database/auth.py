from Database import handle_database_operations

@handle_database_operations
def validateLogin(mysql,cursor,user_data:dict):
    username = user_data['username']
    password = user_data['password']

    print(user_data)

    cursor.execute('SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s ;',(username,password))
    response = cursor.fetchone()

    if response:
        return response

    return None

@handle_database_operations
def get_roles(mysql,cursor,user_id:int):
    cursor.execute('SELECT id_usuario,nombre FROM usuarios_roles JOIN roles ON roles.id_rol = usuarios_roles.id_rol WHERE usuarios_roles.id_usuario = %s ;',(user_id,))

    response = cursor.fetchall()
    return response
