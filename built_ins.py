# sorted
dict_country = {

    "mx": "México",
    "es": "España",
    "ec": "Ecuador",
    "co": "Colombia",
    "pe": "Perú",
    "ve": "Venezuela"
}

paises = [

    "España",
    "Ecuador",
    "México",
    "Perú",
    "Colombia",
    "Venezuela"
]

ordenado = sorted(paises, reverse=True)

print(ordenado)


# Tradicional filter + funcion filtrado


def filtro(elemento):
    return elemento >= 10


filtro_2 = lambda arg: arg >= 10

numeros = [1, 10, 15, 25, 3]

for item in filter(filtro_2, numeros):
    print(item)
