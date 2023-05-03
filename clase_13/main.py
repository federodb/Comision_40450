from clase_13_adicional import Producto, Pedido
from clase_13_services import console_interaction_service as instancia_cis
from clase_13_services import data_base_service as instancia_db

while True:
    
    print("*" * 50)
    print("\nGENERAR PEDIDO NUEVO")
    
    pedido = Pedido()
    lista_prod = instancia_db.devuelve_lista_de_productos()
    lista_prod.append("VER LISTADO")
    lista_prod.append("CONSULTAR CANT PEDIDOS DEL DÍA")
    lista_prod.append("CONSULTAR CANT PRODUCTOS")
    lista_prod.append("COBRAR")

    while True:
        
        indice = instancia_cis.retorna_indice_de_la_lista(lista_prod)
        
        if indice == len(lista_prod):
            break

        if indice == len(lista_prod) - 1:
            print(f"\nLa cantidad de productos es: {len(pedido)}\n")
            continue

        if indice == len(lista_prod) - 2:
            print(f"\nLa cantidad de pedidos hasta el momento es: {pedido.devuelve_cantidad_pedidos()}\n")
            continue

        if indice == len(lista_prod) - 3:
            print()
            for prod in pedido.lista_pedido:
                print(prod)
            continue

        data_prod = instancia_db.devuelve_producto(indice)
        
        if not data_prod:
            print("El producto buscado no existe en la base de datos.")
            continue
        
        producto = Producto(
            codigo=indice,
            precio=data_prod["precio"],
            detalle=data_prod["detalle"],
            unid_med=data_prod["unidad_med"],
            promo_desc=data_prod["promo_desc"]
        )

        pedido.agregar_producto(producto)
    
    instancia_cis.printea_total_a_pagar(pedido.obtener_total())