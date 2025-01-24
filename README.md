# Generador de Menús Semanales

Esta es una pequeña aplicación web desarrollada con Flask que genera menús semanales aleatorios basados en una base de datos SQLite existente. La creé como un regalo especial para mi novia, que es chef y necesita cambiar el menú cada semana.

## Historia

Mi novia suele tener que diseñar nuevos menús semanalmente, lo cual puede ser una tarea bastante laboriosa. Para ayudarla, decidí construir este pequeño proyecto:

Los platos inicialmente estaban almacenados en un documento de Word. Utilicé Deepseek AI para extraer todos los platos y organizarlos de forma sistemática en categorías:
- Primeros platos: Ensalada, crema o sopa, y aperitivos.
- Segundos platos: Verdura, pescado, cerdo y ternera.

Con estos datos organizados, creé una base de datos SQLite con dos columnas:
- `categorías`: Las categorías mencionadas anteriormente.
- `platos`: Los nombres de los platos.

Después, desarrollé una aplicación Flask que:
- Muestra dos secciones: una para "Primeros platos" y otra para "Segundos platos".
- Incluye un botón para generar un menú aleatorio.

El proyecto es sencillo pero significativo, ya que le ayuda a agilizar su trabajo mientras también representa un regalo personal y útil.

## Funcionalidades

- Genera menús aleatorios basados en una base de datos categorizada de platos.
- Es fácil de ampliar añadiendo nuevas categorías o platos a la base de datos.
- Tiene una interfaz sencilla con secciones claras para "Primeros platos" y "Segundos platos".

## Tecnologías Utilizadas

- Python
- Flask
- SQLite
- HTML/CSS

## Instalación

1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar la aplicación: `python app.py`
