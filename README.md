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
   pip install flask flask_sqlalchemy
   ```
3. Iniciar la aplicacion:
   ```bash
   python run.py
   ```
4. Abrir `http://localhost:5000` en el navegador.
