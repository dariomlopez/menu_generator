import sqlite3
import random
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('MenuSemanal.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_random_dishes():
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

@app.route('/')
def generar_menu():
    menu = get_random_dishes()
    return render_template('menu.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
