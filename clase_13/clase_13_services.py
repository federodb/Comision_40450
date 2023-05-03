
class ConsoleInteractionService:

    def retorna_indice_de_la_lista(self, lista_opciones, titulo="Elija una opción:"):

        while True:

            print(f"\n\n{titulo}")

            for posicion, valor in enumerate(lista_opciones, 1):
                print(f"{posicion} - {valor}")
            
            opcion = input("Selección: ")

            try:
                indice = int(opcion)
            except ValueError:
                print("Error en el valor ingresado, debe ingresar un número entero.")
            else:
                return indice
    
    def printea_total_a_pagar(self, valor):
        
        print("#" * 50)
        
        texto_interno = f"$ {valor}".center(48)
        texto = "#" + texto_interno + "#"
        print(texto)
        
        print("#" * 50)

class DataBaseService:

    db_productos = {
        1: {
            "precio": 100,
            "detalle": "Arroz",
            "unidad_med": "1kg",
            "promo_desc": 5,
        },
        2: {
            "precio": 200,
            "detalle": "Fideos",
            "unidad_med": "500g",
            "promo_desc": 50,
        },
        3: {
            "precio": 300,
            "detalle": "Masitas",
            "unidad_med": "30u",
            "promo_desc": 0,
        },
        4: {
            "precio": 400,
            "detalle": "Gaseosa",
            "unidad_med": "1L",
            "promo_desc": 0,
        },
        5: {
            "precio": 500,
            "detalle": "Carne",
            "unidad_med": "1kg",
            "promo_desc": 10,
        },
    }

    def devuelve_producto(self, codigo):

        if codigo in DataBaseService.db_productos:
            return DataBaseService.db_productos[codigo]
        return None

    def devuelve_lista_de_productos(self):
        
        lista_productos = []
        
        for value in DataBaseService.db_productos.values():
            texto = ""
            texto += f"{value['unidad_med']}"
            texto += f" de {value['detalle']}"
            texto = texto.ljust(15)
            texto += f"   ///   precio: {value['precio']}"
            lista_productos.append(texto)
        
        return lista_productos


console_interaction_service = ConsoleInteractionService()
data_base_service = DataBaseService()

