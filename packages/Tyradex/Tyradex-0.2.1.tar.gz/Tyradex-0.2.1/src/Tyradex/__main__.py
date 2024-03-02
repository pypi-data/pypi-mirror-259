# Utilisation console de L'API

import json
import sys

from src.Tyradex import call


if __name__ == '__main__':
    if len(sys.argv) <= 1 or sys.argv[1] == '--help':
        print("Usage python -m Tyradex <endpoint>\n")
        print("Pokemon :")
        print("\t- python -m Tyradex pokemon")
        print("\t\tAllows you to obtain the list of all Pokémon.\n")
        print("\t- python -m Tyradex pokemon <identifiant> [region]")
        print("\t- python -m Tyradex pokemon/<identifiant>/[region]")
        print("\t\tAllows you to obtain information about a specific Pokémon.\n")
        print("\t\t<identifier> Required, Int or String, Corresponds to the Pokémon's identifier in the National "
              "Pokédex or its name.")
        print("\t\t[region] Optional, String, Corresponds to the region of the Pokémon. Allows you to retrieve "
              "information on a regional form of a Pokémon.\n")
        print("Generations :")
        print("\t- python -m Tyradex gen")
        print("\t\tAllows you to obtain the list of the different generations.\n")
        print("\t- python -m Tyradex gen <generation>")
        print("\t- python -m Tyradex gen/<generation>")
        print("\t\tAllows you to obtain information about a specific generation.\n")
        print("\t\t<generation> Required, Int, Corresponds to the generation number.\n")
        print("Types :")
        print("\t- python -m Tyradex types")
        print("\t\tGets the list of all types.\n")
        print("\t- python -m Tyradex types <type1> [type2]")
        print("\t- python -m Tyradex types/<type1>/[type2]")
        print("\t\tAllows you to obtain information about a specific type.\n")
        print("\t\t<type1> Required, Int or String, Corresponds to the type identifier, or its English or French "
              "name.")
        print("\t\t<type2> Optional, Int or String, Corresponds to the second desired type. With the combination, "
              "this allows you to obtain Pokémon with this dual type.")
    else:
        print(json.dumps(call('/'.join(sys.argv[1:])), indent=2))
