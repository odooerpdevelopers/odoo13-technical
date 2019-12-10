dict_country = {

    "es": "España",
    "ec": "Ecuador",
    "mx": "México",
    "pe": "Perú",
    "co": "Colombia",
    "ve": "Venezuela"
}

valid_codes = ['ec', 'mx']

paises = [val for key, val in dict_country.items() if key in valid_codes]

print(paises)
