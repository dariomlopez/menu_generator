import os
import sqlite3
import random
from flask import Flask, render_template, jsonify
from datetime import datetime

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
    """
    Fetch random dishes from the database with a consistent structure
    
    Returns:
    dict: A structured dictionary of menu items with categories
    """
    try:
        conn = get_db_connection()
        
        # Define the categories with their display names and database categories
        menu_structure = {
            'primeros_platos': {
                'ensalada': {'category': 'Ensalada', 'display_name': 'Ensalada'},
                'crema_o_sopa': {'category': 'Crema o Sopa', 'display_name': 'Crema o Sopa'},
                'aperitivos': {'category': 'Aperitivos y Otros', 'display_name': 'Aperitivos'}
            },
            'segundos_platos': {
                'verdura': {'category': 'Verdura', 'display_name': 'Verdura'},
                'pescado': {'category': 'Pescado', 'display_name': 'Pescado'},
                'cerdo': {'category': 'Cerdo', 'display_name': 'Cerdo'},
                'ternera': {'category': 'Ternera', 'display_name': 'Ternera'}
            }
        }
        
        # Fetch random dishes for each category
        for section in menu_structure:
            for key, category_info in menu_structure[section].items():
                cursor = conn.execute(
                    'SELECT plato FROM MenuSemanal WHERE categoria = ? ORDER BY RANDOM() LIMIT 1', 
                    (category_info['category'],)
                )
                dish = cursor.fetchone()
                category_info['plato'] = dish['plato'] if dish else 'No hay platos en esta categoría'
        
        conn.close()
        return menu_structure
    except sqlite3.Error as e:
        app.logger.error(f"Database query error: {e}")
        # Return a fallback structure in case of error
        return {
            'primeros_platos': {
                'ensalada': {'display_name': 'Ensalada', 'plato': 'Error al obtener plato'},
                'crema_o_sopa': {'display_name': 'Crema o Sopa', 'plato': 'Error al obtener plato'},
                'aperitivos': {'display_name': 'Aperitivos', 'plato': 'Error al obtener plato'}
            },
            'segundos_platos': {
                'verdura': {'display_name': 'Verdura', 'plato': 'Error al obtener plato'},
                'pescado': {'display_name': 'Pescado', 'plato': 'Error al obtener plato'},
                'cerdo': {'display_name': 'Cerdo', 'plato': 'Error al obtener plato'},
                'ternera': {'display_name': 'Ternera', 'plato': 'Error al obtener plato'}
            }
        }

@app.route('/')
def generar_menu():
    """
    Generate a weekly menu with error handling
    """
    try:
        menu = get_random_dishes()
        
        # Flatten the menu structure for template rendering
        template_menu = {}
        for section in menu.values():
            for key, value in section.items():
                template_menu[value['display_name']] = value['plato']
        
        return render_template('menu.html', menu=template_menu)
    except Exception as e:
        app.logger.error(f"Menu generation error: {e}")
        return "Error al generar el menú", 500

@app.route('/menu-texto')
def menu_texto():
    """
    Endpoint to display menu in plain text format
    """
    try:
        # menu = get_random_dishes()
        
        # Create a plain text representation of the menu
        menu_texto = "Menú Semanal:\n\n"
        
        # First dishes section
        menu_texto += "Primeros Platos:\n"
        for key, value in menu['primeros_platos'].items():
            menu_texto += f"- {value['display_name']}: {value['plato']}\n"
        menu_texto += "\n"
        
        # Second dishes section
        menu_texto += "Segundos Platos:\n"
        for key, value in menu['segundos_platos'].items():
            menu_texto += f"- {value['display_name']}: {value['plato']}\n"
        
        # Return as plain text
        return app.response_class(
            response=menu_texto, 
            status=200, 
            mimetype='text/plain; charset=utf-8'
        )
    except Exception as e:
        app.logger.error(f"Plain text menu generation error: {e}")
        return "Error al generar el menú en texto plano", 500

if __name__ == '__main__':
    # Only for local development
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
