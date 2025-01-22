import sqlite3

def mostrar_menu():
    try:
        # Conectar a la base de datos
        conexion = sqlite3.connect('MenuSemanal.db')
        cursor = conexion.cursor()

        # Obtener todas las categorías únicas
        cursor.execute("SELECT DISTINCT categoria FROM MenuSemanal")
        categorias = [categoria[0] for categoria in cursor.fetchall()]

        # Mostrar los platos por categoría
        for categoria in categorias:
            print(f"\n--- {categoria.upper()} ---")
            cursor.execute("SELECT plato FROM MenuSemanal WHERE categoria = ?", (categoria,))
            platos = cursor.fetchall()
            
            for i, plato in enumerate(platos, 1):
                print(f"{i}. {plato[0]}")

    except sqlite3.Error as error:
        print(f"Error al acceder a la base de datos: {error}")
        
    finally:
        if conexion:
            conexion.close()
            print("\nConexión cerrada correctamente")

if __name__ == "__main__":
    mostrar_menu()