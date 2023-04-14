# EJEMPLO 1

# f = open("./archivo.py", "w")
# f.write("print('Hola comisión 40450')\n")
# f.write("print('otro print')")
# f.close()


# EJEMPLO 2

# nombre = "Nicolas"
# apellido = "Perez"
# dni = 111111
# d = {"NOMBRE":nombre, "APELLIDO":apellido, "DNI":dni}
# f = open("./otro.txt", "w")
# f.write(d["NOMBRE"] + "," + d["APELLIDO"] + "," + str(d["DNI"] ))
# f.close()


# EJEMPLO 3

# f = open("./otro.txt", "r")
# content = f.read()
# f.close()
# print(content)


# EJEMPLO 4

# f = open("./otro.txt", "r")
# f.seek(20)
# print(f.read())
# f.close()


# EJEMPLO 5

# import json  #Importar las funciones de json en la 
# # #clase 15 entenderemos mejor el IMPORT

# data = {}

# data['clients'] = []

# data['clients'].append(
#         {
#             'first_name': 'Sigrid',
#             'last_name': 'Mannock',
#             'age': 27,
#             'amount': 7.17
#         }
#     )

# data['clients'].append({
#     'first_name': 'Joe',
#     'last_name': 'Hinners',
#     'age': 31,
#     'amount': [1.90, 5.50]})

# data['clients'].append({
#     'first_name': 'Theodoric',
#     'last_name': 'Rivers',
#     'age': 36,
#     'amount': 1.11})

# with open("./primerJson.json", 'w') as file:
#     json.dump(data, file, indent=4)



# EJEMPLO 6
# import json
# with open("./primerJson.json") as file:

#     dataLectura = json.load(file)

#     for client in dataLectura['clients']:
#         print('First name:', client['first_name'])
#         print('Last name:', client['last_name'])
#         print('Age:', client['age'])
#         print('Amount:', client['amount'])
#         print()
