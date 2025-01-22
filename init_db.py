import os
import sqlite3

def init_database():
    # Determine the absolute path to the database
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_PATH = os.path.join(BASE_DIR, 'MenuSemanal.db')
    
    # Check if database already exists
    if os.path.exists(DATABASE_PATH):
        print(f"Database {DATABASE_PATH} already exists.")
        return
    
    # Create and connect to the database
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Create the MenuSemanal table
    cursor.execute('''
    CREATE TABLE MenuSemanal (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT NOT NULL,
        plato TEXT NOT NULL
    )''')
    
    # Sample data
    dishes = [
        # Ensaladas
        ('Ensalada', 'Ensaladilla rusa'),
        ('Ensalada', 'Ensalada de espinacas con perlas de queso, bacon y vinagreta de mostaza'),
        ('Ensalada', 'Ensalada de dados de queso feta, lechuga, cebolla encurtida, aceitunas y salsa de yogur'),
        ('Ensalada', 'Ensalada de espinaca, queso de cabra, nueces y vinagreta de mostaza'),
        ('Ensalada', 'Ensalada de cherrys con perlas de queso de cabra y membrillo'),
        ('Ensalada', 'Ensalada de espinacas con dátiles y melón'),
        ('Ensalada', 'Ensalada griega, con queso feta, pepino, aceitunas y salsa de yogurt'),
        ('Ensalada', 'Ensalada de pasta, canónigos, atún, tomate y maíz'),
        ('Ensalada', 'Ensalada de espinacas, naranja, bacon y nueces'),
        ('Ensalada', 'Ensalada de pasta con cherry y queso feta y vinagreta'),
        ('Ensalada', 'Ensalada de manzana, bacon y endibias con salsa de queso azul'),
        ('Ensalada', 'Ensalada de espinacas con bacon, cherry y crema de queso'),
        ('Ensalada', 'Ensalada de canónigos con perlas de queso y bacon'),
        ('Ensalada', 'Ensalada de espinacas, cherry, manzana y nueces con vinagreta de mostaza'),
        ('Ensalada', 'Ensalada de pasta con queso feta, cherry y espinacas'),
        ('Ensalada', 'Ensalada de queso azul, bacon y nueces'),
        ('Ensalada', 'Ensaladilla rusa con langostinos'),
        ('Ensalada', 'Ensalada de manzana, bacon y endibias con salsa de queso azul'),
        ('Ensalada', 'Ensalada de espinacas con bacon, cherry y crema de queso'),
        ('Ensalada', 'Ensalada de pasta con atún, maíz, cherry y rúcula'),

        # Cremas o Sopas
        ('Crema o Sopa', 'Fabada asturiana'),
        ('Crema o Sopa', 'Crema de calabacín con queso crema'),
        ('Crema o Sopa', 'Salmorejo con jamón y huevo duro'),
        ('Crema o Sopa', 'Crema de calabaza con queso parmesano'),
        ('Crema o Sopa', 'Crema de calabacín servida con tierra de bacon'),
        ('Crema o Sopa', 'Crema de calabacín y queso crema con aceite de albahaca'),
        ('Crema o Sopa', 'Crema de calabaza con queso fresco a la plancha'),
        ('Crema o Sopa', 'Crema de calabacín y pera'),
        ('Crema o Sopa', 'Vichyssoise (crema de puerro y patata)'),
        ('Crema o Sopa', 'Crema de calabacín con croutons'),
        ('Crema o Sopa', 'Crema de verduras con parmesano y picatostes'),

        # Aperitivos y Otros
        ('Aperitivos y Otros', 'Parrillada de verduras con queso de cabra'),
        ('Aperitivos y Otros', 'Wok de noodles con verduritas salteadas'),
        ('Aperitivos y Otros', 'FOCACCIA SETAS SALTEADAS Y QUESO BRIE'),
        ('Aperitivos y Otros', 'Berenjenas fritas con sirope de arce'),
        ('Aperitivos y Otros', 'FALAFEL de garbanzos con tzatziki y pan NAAN'),
        ('Aperitivos y Otros', 'Calabacín gratinado con queso y salsa de tomate'),
        ('Aperitivos y Otros', 'Setas empanadas con alioli'),
        ('Aperitivos y Otros', 'Hummus de queso, tomate seco y garbanzos'),
        ('Aperitivos y Otros', 'Focaccia de champiñones y queso brie'),
        ('Aperitivos y Otros', 'Patatas asadas con Philadelphia, cheddar, tierra de bacon y cebollino'),
        ('Aperitivos y Otros', 'Berenjena gratinada con salsa de tomate y queso'),
        ('Aperitivos y Otros', 'Espaguetis con crema de queso y pesto con cherry salteados'),
        ('Aperitivos y Otros', 'Pisto con parmesano y huevo frito'),
        ('Aperitivos y Otros', 'Quesadillas de bacon y queso crema con pico de gallo'),
        ('Aperitivos y Otros', 'Tempura de verduras con mayonesa chipotle'),
        ('Aperitivos y Otros', 'Hummus de garbanzo con pan NAAN'),
        ('Aperitivos y Otros', 'Focaccia de bacon, perlas de mozzarella y rúcula'),
        ('Aperitivos y Otros', 'Calabacín frito en parmesano y panko'),
        ('Aperitivos y Otros', 'Salteado de setas al ajillo con soja y huevo frito'),
        ('Aperitivos y Otros', 'Brochetas de caprese y jamón con aceite de albahaca'),
        ('Aperitivos y Otros', 'Focaccia de lacón, brie y pimentón'),
        ('Aperitivos y Otros', 'Quesadillas de jamón York, queso crema y pico de gallo'),
        ('Aperitivos y Otros', 'Brochetas de melón, jamón y perlas de mozzarella'),
        ('Aperitivos y Otros', 'Tempura de calabacín con alioli'),
        ('Aperitivos y Otros', 'Brochetas de melón con jamón y aceite de albahaca'),
        ('Aperitivos y Otros', 'Calabacín gratinado con tomate casero y parmesano'),
        ('Aperitivos y Otros', 'Huevos rellenos de ensaladilla con asadillo de pimientos'),
        ('Aperitivos y Otros', 'Quesadilla de queso brie y champiñones salteados'),
        ('Aperitivos y Otros', 'Focaccia de lacón con perlas de queso de cabra y pimentón'),
        ('Aperitivos y Otros', 'Tempura de verduras'),
        ('Aperitivos y Otros', 'FALAFEL de garbanzos con salsa de yogur y pepino'),
        ('Aperitivos y Otros', 'Espaguetis al pesto con cherry salteados'),
        ('Aperitivos y Otros', 'Queso provolone con pico de gallo y aceite de albahaca'),
        ('Aperitivos y Otros', 'Focaccia de setas, queso y cherrys'),
        ('Aperitivos y Otros', 'Pisto con huevo frito'),
        ('Aperitivos y Otros', 'Tempura de verduras con mayonesa chipotle'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con cherry y queso feta y vinagreta'),
        ('Aperitivos y Otros', 'Brochetas de melón con jamón y perlas de queso'),
        ('Aperitivos y Otros', 'Melanzane gratinado al horno'),
        ('Aperitivos y Otros', 'Focaccia de berenjena y queso'),
        ('Aperitivos y Otros', 'Patata asada con cheddar, queso crema y bacon'),
        ('Aperitivos y Otros', 'Queso provolone con pico de gallo'),
        ('Aperitivos y Otros', 'Arroz chaufa de pollo'),
        ('Aperitivos y Otros', 'Huevos rellenos de ensaladilla con pimientos asados'),
        ('Aperitivos y Otros', 'Hummus de garbanzos con pan NAAN'),
        ('Aperitivos y Otros', 'Focaccia de queso cabra y bacon'),
        ('Aperitivos y Otros', 'Gnocchi con crema de mascarpone y parmesano'),
        ('Aperitivos y Otros', 'Wok de fideos orientales y verduras salteadas'),
        ('Aperitivos y Otros', 'Pisto de champiñones y calabacín con queso gratinado'),
        ('Aperitivos y Otros', 'Blinis de salmón ahumado con queso crema y rúcula'),
        ('Aperitivos y Otros', 'Ensadilla de pollo y manzana con salsa cocktail'),
        ('Aperitivos y Otros', 'Garbanzos con curry y mantequilla'),
        ('Aperitivos y Otros', 'Calabacín gratinado con tomate y queso'),
        ('Aperitivos y Otros', 'Focaccia de queso brie y bacon'),
        ('Aperitivos y Otros', 'Cous cous de verduras salteadas'),
        ('Aperitivos y Otros', 'Queso provolone con pico de gallo'),
        ('Aperitivos y Otros', 'Costillas a la riojana con patatas'),
        ('Aperitivos y Otros', 'Ensadilla de espinacas, queso de cabra y bacon'),
        ('Aperitivos y Otros', 'Patatas asadas con cheddar, queso crema y tierra de bacon'),
        ('Aperitivos y Otros', 'Espaguetis al pesto con cherrys salteados y parmesano'),
        ('Aperitivos y Otros', 'FALAFEL de garbanzos con ensalada y crema de yogur'),
        ('Aperitivos y Otros', 'Arroz chaufa con pollo'),
        ('Aperitivos y Otros', 'Crema de calabacín y queso crema con aceite de albahaca'),
        ('Aperitivos y Otros', 'Huevos rellenos de ensaladilla con piquillos'),
        ('Aperitivos y Otros', 'Focaccia de queso, bacon y espinacas'),
        ('Aperitivos y Otros', 'Pisto con parmesano y huevo frito'),
        ('Aperitivos y Otros', 'Wok de fideos orientales con verduras salteadas'),
        ('Aperitivos y Otros', 'Lentejas con chorizo'),
        ('Aperitivos y Otros', 'Pisto con huevo frito'),
        ('Aperitivos y Otros', 'Croquetas de gorgonzola'),
        ('Aperitivos y Otros', 'Ensadilla de espinacas, queso feta y bacon'),
        ('Aperitivos y Otros', 'Crema de calabacín con queso crema'),
        ('Aperitivos y Otros', 'Ensadilla de pasta, cherry, atún, maíz, rúcula y vinagreta de mostaza'),
        ('Aperitivos y Otros', 'Ensadilla de queso azul, bacon y nueces'),
        ('Aperitivos y Otros', 'Ensadilla rusa con langostinos'),
        ('Aperitivos y Otros', 'Crema de calabaza con queso tierno a la plancha'),
        ('Aperitivos y Otros', 'Ensadilla de manzana, bacon y endibias con salsa de queso azul'),
        ('Aperitivos y Otros', 'Setas empanadas con alioli'),
        ('Aperitivos y Otros', 'Ensadilla de espinacas con bacon, cherry y crema de queso'),
        ('Aperitivos y Otros', 'Espagueti linguini con pesto y queso parmesano'),
        ('Aperitivos y Otros', 'Ensadilla de canónigos con perlas de queso y bacon'),
        ('Aperitivos y Otros', 'Tempura de calabacín con romesco'),
        ('Aperitivos y Otros', 'Ensadilla de espinacas, cherry, manzana y nueces con vinagreta de mostaza'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con queso feta, cherry y espinacas'),
        ('Aperitivos y Otros', 'Gajos de patata asada con cheddar, bacon y cebollino'),
        ('Aperitivos y Otros', 'Salmorejo'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con atún, maíz, cherry y rúcula'),
        ('Aperitivos y Otros', 'Ensadilla de queso de cabra, espinacas y bacon'),
        ('Aperitivos y Otros', 'Ensadilla de espinacas con bacon, cherry y crema de queso'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con cherry y queso feta y vinagreta'),
        ('Aperitivos y Otros', 'Ensadilla de espinacas con bacon, cherry y crema de queso'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con atún, maíz, cherry y rúcula'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con queso feta, cherry y espinacas'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con atún, maíz, cherry y rúcula'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con queso feta, cherry y espinacas'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con atún, maíz, cherry y rúcula'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con queso feta, cherry y espinacas'),
        ('Aperitivos y Otros', 'Ensadilla de pasta con atún, maíz, cherry y rúcula'),

        # Pescado
        ('Pescado', 'Lubina a la espalda'),
        ('Pescado', 'Dorada a la espalda con ajada y panaderas'),
        ('Pescado', 'Bacalao en tempura con salsa tartara'),
        ('Pescado', 'Lomo de salmón al grill con teriyaki y salsa de yogur'),
        ('Pescado', 'Boquerones fritos a la andaluza con ensalada'),
        ('Pescado', 'Cazón en adobo con ensalada'),
        ('Pescado', 'Pargo a la espalda con patatas panadera'),
        ('Pescado', 'Bacalao dorado con sus patatas paja'),
        ('Pescado', 'Tataki de atún acompañado de hummus y ensalada'),
        ('Pescado', 'Salmón al grill, con salsa de yogurt y ensalada verde'),
        ('Pescado', 'Fish and chips de merluza bien crujiente con nuestras patatas caseras'),
        ('Pescado', 'Bocaditos de merluza en tempura con ensalada verde'),
        ('Pescado', 'Atún a la parrilla con hummus de garbanzo y ensalada'),
        ('Pescado', 'Bocaditos de merluza rebozados al curry con ensalada y tabulé'),
        ('Pescado', 'Bocaditos de merluza a la Romana'),
        ('Pescado', 'Bocaditos de merluza en tempura con ensalada verde'),
        ('Pescado', 'Bocaditos de merluza al curry con ensalada y tabulé'),
        ('Pescado', 'Bocaditos de merluza a la Romana'),
        ('Pescado', 'Bocaditos de merluza en tempura con ensalada verde'),
        ('Pescado', 'Bocaditos de merluza al curry con ensalada y tabulé'),

        # Verdura
        ('Verdura', 'Wok de noodles y verduritas salteadas'),
        ('Verdura', 'Parrillada de verduras con queso de cabra'),
        ('Verdura', 'Berenjena rellena de carne gratinada'),
        ('Verdura', 'Berenjenas fritas con sirope de arce'),
        ('Verdura', 'Calabacín gratinado con queso y salsa de tomate'),
        ('Verdura', 'Berenjena gratinada con salsa de tomate y queso'),
        ('Verdura', 'Berenjenas fritas con salmorejo'),
        ('Verdura', 'Berenjenas fritas con miel'),
        ('Verdura', 'Berenjenas fritas con sirope de arce'),
        ('Verdura', 'Berenjenas fritas con miel'),
        ('Verdura', 'Berenjenas fritas con sirope de arce'),
        ('Verdura', 'Berenjenas fritas con miel'),
        ('Verdura', 'Berenjenas fritas con sirope de arce'),
        ('Verdura', 'Berenjenas fritas con miel'),
        ('Verdura', 'Berenjenas fritas con sirope de arce'),
        ('Verdura', 'Berenjenas fritas con miel'),
        ('Verdura', 'Berenjenas fritas con sirope de arce'),
        ('Verdura', 'Berenjenas fritas con miel'),
        ('Verdura', 'Berenjenas fritas con sirope de arce'),
        ('Verdura', 'Berenjenas fritas con miel'),

        ('Ternera', 'Brocheta de ternera con verduras y patatas fritas'),
        ('Ternera', 'Brocheta de ternera y verduras al grill'),
        ('Ternera', 'Hamburguesa con huevo frito y crema de queso azul'),
        ('Ternera', 'Wok de ternera salteada con fideos orientales'),
        ('Ternera', 'Asado de tira con mojo picón'),
        ('Ternera', 'Solomillitos al curry con arroz de coco'),
        ('Ternera', 'Entrecot a la parrilla con patatas fritas'),
        ('Ternera', 'Churrasco de ternera al grill con patatas ali-oli'),
        ('Ternera', 'Hamburguesa gourmet de angus'),
        ('Ternera', 'Costilla de ternera a la parrilla con crema de chimichurri'),

        # CERDO
        ('Cerdo', 'Sándwich cubano de secreto'),
        ('Cerdo', 'Wok de cerdo agridulce con noodles y verduras'),
        ('Cerdo', 'Costillas a la riojana con patatas'),
        ('Cerdo', 'Chuletas de cerdo con mostaza y miel'),
        ('Cerdo', 'Lacón a la gallega con patatas'),
        ('Cerdo', 'Secreto ibérico a la parrilla'),
        ('Cerdo', 'Chuletas de cerdo con salsa de manzana'),
        ('Cerdo', 'Costillar de cerdo estilo Thai'),
        ('Cerdo', 'Albóndigas en salsa verde con patatas fritas'),
        ('Cerdo', 'Cerdo agridulce con verduritas y noodles'),

        # POLLO
        ('Pollo', 'Milanesa de pollo con tomate casero y queso'),
        ('Pollo', 'Pollo asado a la lima y tomillo'),
        ('Pollo', 'Hamburguesa de pollo con bacon y salsa tártara'),
        ('Pollo', 'Alitas de pollo crujientes con salsa BBQ'),
        ('Pollo', 'Wrap de pollo curry con bacon y queso crema'),
        ('Pollo', 'Pollo al curry con arroz basmati'),
        ('Pollo', 'Pollo asado con miel y mostaza'),
        ('Pollo', 'Crujientes de pollo con mostaza de miel'),
        ('Pollo', 'Ensalada César con pollo crujiente'),
        ('Pollo', 'Pechugas de pollo en salsa de mostaza')
    ]
    
    # Insert sample dishes
    cursor.executemany('INSERT INTO MenuSemanal (categoria, plato) VALUES (?, ?)', dishes)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print(f"Database {DATABASE_PATH} created successfully.")

if __name__ == '__main__':
    init_database()
