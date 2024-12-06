pokemon_dict = {
            "CHARIZARD": "Es un pokemon tipo fuego-volador",
            "GENGAR": "Es un pokemon GOD tipo fantasma",
            "CHIKORITA": "Es un pokemon Kwai tipo planta",
            "BLASTOISE": "Es un pokemon mamalon grandotote y de agua"
            }

pokemon = input("Escribe un pokemon que quieras conocer (¡con mayúsculas!): ")

if pokemon in pokemon_dict.keys():
    print(pokemon_dict[pokemon])
else:
    print("No existe ese pokemon en nuestra base de datos")
