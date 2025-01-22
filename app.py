import os
import sqlite3
import random
from flask import Flask, render_template, jsonify

# Import database initialization
from init_db import init_database

app = Flask(__name__)

# Determine the absolute path to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'MenuSemanal.db')

# Ensure database exists
if not os.path.exists(DATABASE_PATH):
    init_database()

def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        app.logger.error(f"Database connection error: {e}")
        raise

def get_random_dishes():
    try:
        conn = get_db_connection()
        
        # Define the order of categories as specified
        first_categories = ['Ensalada', 'Crema o Sopa', 'Aperitivos y Otros']
        second_categories = ['Verdura', 'Pescado', 'Cerdo', 'Ternera']
        
        menu = {}
        
        # Select random dishes for first categories
        for cat in first_categories:
            cursor = conn.execute('SELECT plato FROM MenuSemanal WHERE categoria = ? ORDER BY RANDOM() LIMIT 1', (cat,))
            dish = cursor.fetchone()
            menu[cat] = dish['plato'] if dish else 'No hay platos en esta categoría'
        
        # Select random dishes for second categories
        for cat in second_categories:
            cursor = conn.execute('SELECT plato FROM MenuSemanal WHERE categoria = ? ORDER BY RANDOM() LIMIT 1', (cat,))
            dish = cursor.fetchone()
            menu[cat] = dish['plato'] if dish else 'No hay platos en esta categoría'
        
        conn.close()
        return menu
    except sqlite3.Error as e:
        app.logger.error(f"Database query error: {e}")
        return {cat: 'Error al obtener platos' for cat in first_categories + second_categories}

@app.route('/')
def generar_menu():
    try:
        menu = get_random_dishes()
        return render_template('menu.html', menu=menu)
    except Exception as e:
        app.logger.error(f"Menu generation error: {e}")
        return "Error al generar el menú", 500

@app.route('/menu-json')
def menu_json():
    try:
        menu = get_random_dishes()
        return jsonify(menu)
    except Exception as e:
        app.logger.error(f"JSON menu generation error: {e}")
        return jsonify({"error": "No se pudo generar el menú"}), 500

if __name__ == '__main__':
    # Only for local development
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
