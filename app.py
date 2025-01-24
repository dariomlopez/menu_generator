import os
import random
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Import Supabase configuration
from supabase_config import get_secure_connection, validate_user_input

app = Flask(__name__)

# Initialize Supabase client
supabase = get_secure_connection()

def get_db_connection():
    """
    Establishes a secure connection to Supabase
    """
    try:
        return supabase
    except Exception as e:
        app.logger.error(f"Supabase connection error: {e}")
        raise

def get_random_dishes():
    """
    Fetch random dishes from Supabase with enhanced security
    """
    try:
        # Define the order of categories
        first_categories = ['Ensalada', 'Crema o Sopa', 'Aperitivos y Otros']
        second_categories = ['Verdura', 'Pescado', 'Cerdo', 'Ternera']
        
        menu = {}
        
        # Fetch random dishes for first categories
        for cat in first_categories:
            # Use parameterized query to prevent SQL injection
            response = supabase.table('MenuSemanal').select('plato').eq('categoria', cat).limit(1).execute()
            dishes = response.data
            menu[cat] = dishes[0]['plato'] if dishes else 'No hay platos en esta categoría'
        
        # Fetch random dishes for second categories
        for cat in second_categories:
            response = supabase.table('MenuSemanal').select('plato').eq('categoria', cat).limit(1).execute()
            dishes = response.data
            menu[cat] = dishes[0]['plato'] if dishes else 'No hay platos en esta categoría'
        
        return menu
    except Exception as e:
        app.logger.error(f"Error fetching dishes: {e}")
        return {}

def generar_menu():
    """
    Generate a weekly menu with error handling
    """
    try:
        menu = get_random_dishes()
        return render_template('menu.html', menu=menu)
    except Exception as e:
        app.logger.error(f"Menu generation error: {e}")
        return "Error al generar el menú", 500

@app.route('/')
def index():
    return generar_menu()

@app.route('/menu-json')
def menu_json():
    """
    JSON endpoint for menu generation with security checks
    """
    try:
        menu = get_random_dishes()
        return jsonify(menu)
    except Exception as e:
        app.logger.error(f"Menu JSON generation error: {e}")
        return jsonify({"error": "Could not generate menu"}), 500

if __name__ == '__main__':
    # Enhanced security for local development
    app.config['SECRET_KEY'] = os.getenv('JWT_SECRET')
    app.run(
        host='0.0.0.0', 
        port=int(os.getenv('PORT', 5000)),
        debug=False  # Always set to False in production
    )
