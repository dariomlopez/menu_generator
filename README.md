# Generador de Menús Semanales

## Descripción
Esta aplicación web genera menús semanales aleatorios basados en una base de datos SQLite existente.

## Requisitos
- Python 3.8+
- Flask
- SQLite3

## Instalación
1. Clonar el repositorio
2. Crear un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```
3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución
```
python app.py
```
Abre un navegador y visita `http://localhost:5000`

## Características
- Genera menús aleatorios de 7 categorías
- Interfaz web simple y moderna
- Botón para regenerar menú
