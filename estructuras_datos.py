# acceso indice
#            0, 1, 2, 3
secuencia = [1, 3, 5, 7]
print(secuencia[2])
secuencia[2] = 10
print(secuencia[2])

# add elemento
secuencia.append(22)
print(secuencia[-1])

# eliminar elemento
valor_eliminado = secuencia.pop(4)

print(secuencia, " ", valor_eliminado)

paises = [

    "España",
    "Ecuador",
    "México",
    "Perú",
    "Colombia",
    "Venezuela"
]

# recorrer una lista Python
for elemento in paises:
    print(elemento)
print("############ Tuplas################")

# Tuplas ()
claves = ("123", "541")
for item in claves:
    print(item)
print("################ Diccionarios ############")

dict_country = {

    "es": "España",
    "ec": "Ecuador",
    "mx": "México",
    "pe": "Perú",
    "co": "Colombia",
    "ve": "Venezuela"
}

print(dict_country.get("mx"))

for key, value in dict_country.items():
    print(key, ": ", value)

print(dict_country.keys())
print(dict_country.values())

if "ec" in dict_country.keys():
    print(">> ", dict_country.get("ec"))

res = {
    'warning': "Mensaje de alerta",
    'values': {
        "id": 158,
        "name": "XXFGTX NAME",
        "price": 1245.58,
        "taxes": {
            "vat_1": 0.21,
            "vat_2": 0.4,
        },
    },
}

for key, value in res.items():
    print(key, ": ", value)
    if "values" == key:
        print("id: {} - name: {}".format(value.get("id"), value.get("name")))

