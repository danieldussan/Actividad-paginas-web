# Proyecto de Gestión de Asistencia mediante IoT

Este proyecto utiliza tecnología IoT para gestionar y monitorizar la asistencia de manera eficiente.

## Requisitos Previos

- [XAMPP](https://www.apachefriends.org/index.html) instalado
- [Git](https://git-scm.com/) instalado
- [Python 3](https://www.python.org/downloads/) instalado
- [MySQL](https://www.mysql.com/) incluido en XAMPP

## Instalación y Configuración

### Configuración del Frontend

1. **Dirígete a la carpeta `htdocs` de XAMPP:**

   - En Linux:
     ```bash
     cd /opt/lampp/htdocs
     ```
   - En Windows:
     ```cmd
     cd c:\xampp\htdocs
     ```

2. **Clona el repositorio:**
   ```bash
   git clone https://github.com/xJesusx0/Proyecto-gestion-asistencia-Iot.git
   ```

3. **Crea el archivo `config.js`:**

   - Dirígete a la siguiente ruta:
     ```bash
     cd Proyecto-gestion-asistencia-Iot/Frontend/js/config
     ```
   - Crea el archivo de configuración `config.js` basado en `config-example.js`:
     ```javascript
     // Frontend/js/config/config.js
     const config = {
       serverIp: 'localhost',  // Poner tu IP (opcional)
       serverPort: '5000',
       SECRET_TOKEN: 'token'   // Poner el token
     };

     config.baseUrl = `http://${config.serverIp}:${config.serverPort}`;
     ```

4. **Inicia XAMPP:**

   - Abre el Panel de Control de XAMPP y enciende Apache.

5. **Accede al frontend en tu navegador:**

   > :warning: **Si pusiste tu ip en el archivo de configuracion** Debes acceder de la siguiente manera
   ```bash
   http://tu-ip/Proyecto-gestion-asistencia-Iot/Frontend/
   ```

   ```bash
   http://localhost/Proyecto-gestion-asistencia-Iot/Frontend/
   ```

### Configuración del Backend

1. **Crear un entorno virtual en Python:**
   ```bash
   python3 -m venv env
   ```

2. **Activar el entorno virtual:**

   - En Linux:
     ```bash
     source env/bin/activate
     ```
   - En Windows:
     ```cmd
     .\env\Scripts\activate
     ```

3. **Instalar las dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos MySQL:**

   - Abre el cliente MySQL desde XAMPP.
   - Crear y usar la base de datos:
     ```sql
     CREATE DATABASE proyecto;
     USE proyecto;
     ```
   - Importar la base de datos:
     - Desde el cliente MySQL en Linux:
      ```sql
      SOURCE /opt/lampp/htdocs/Proyecto-gestion-asistencia-Iot/Backend/Database/Proyecto.sql;
      ```

5. **Crear el archivo `config.py`:**

   - Dirígete a la siguiente ruta:
     ```bash
     cd Proyecto-gestion-asistencia-Iot/Backend/app/
     ```
   - Crea el archivo de configuración `config.py` basado en `config-example.py`:
     ```python
     class Config:
         SESSION_PERMANENT = False
         SESSION_TYPE = 'filesystem'
         MYSQL_HOST = 'localhost'
         MYSQL_USER = 'root'
         MYSQL_PASSWORD = 'contraseña'  # Tu contraseña de MySQL
         MYSQL_DB = 'proyecto' #nombre de la base de datos
         SECRET_KEY = 'secret'

      SECRET_TOKEN = 'token'  # Poner el token secreto

      def valid_token(token):
         return token == SECRET_TOKEN
     ```

6. **Iniciar el backend:**
   ```bash
   python3 Backend/run.py
   ```