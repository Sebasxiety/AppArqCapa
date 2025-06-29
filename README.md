# AppArqCapa


Aplicacion de ejemplo con arquitectura por capas (presentacion, negocios y datos) desarrollada en Python con Flask.

## Estructura
- **app/data**: modelos y acceso a datos.
- **app/business**: logica de negocio.
- **app/presentation**: rutas y plantillas.

## Ejecucion
1. Crear un entorno virtual y activar.
2. Instalar dependencias:
   ```bash
   pip install flask flask_sqlalchemy pymysql
   pip install cryptography
   ```
3. Configurar la cadena de conexion a MySQL mediante la variable `DATABASE_URL`. Ejemplo:
   Antes de eso ejecutar el script create_bd.py
   ```bash
   export DATABASE_URL='mysql+pymysql://usuario:clave@localhost/products_db'
   ```
4. Iniciar la aplicacion:
   ```bash
   python run.py
   ```
5. Abrir `http://localhost:5000` en el navegador.