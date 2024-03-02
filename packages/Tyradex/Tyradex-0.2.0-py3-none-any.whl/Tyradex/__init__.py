# Utilisation libs de l'API
import datetime
import time

from PIL import Image

from src.Tyradex import abc
from src.Tyradex.errors import *
from src.Tyradex.maker import call, call_image, concat


class Pokemon:
    """ Represents the data of a Pokémon."""

    @staticmethod
    def all():
        """ Lists all Pokémon.

        :return: All Pokémon
        :rtype: list[Pokemon]
        """

        class Waiting:
            def __init__(self):
                self._times = []

            def add(self, start, end):
                self._times.append((start, end))
                if len(self._times) > 5:
                    self._times.pop(0)

            @property
            def x_more_time(self):
                i = 0
                tt = datetime.timedelta(seconds=0)
                for t in self._times:
                    i += 1
                    tt += datetime.timedelta(seconds=t[1] - t[0])
                return tt / i

        all_pokemon = []
        all_data = call(f"pokemon")
        o = len(all_data)
        waiting = Waiting()
        for data in all_data:
            s = time.time()
            i = len(all_pokemon)
            p = round(i * 100 / o)
            all_pokemon.append(Pokemon(data))
            waiting.add(s, time.time())
            print(f"\r[{i:4}/{o}]▐{'█' * p}{' ' * (100 - p)}▌ : {p:3}% ({waiting.x_more_time * (o - i)})", end='')
        print('\r', end='')

        return all_pokemon

    @staticmethod
    def get(identifiant, region=...):
        """ Give the identified Pokémon.

        :param identifiant: The name (French or English) or the national pokédex number of the pokémon
        :type identifiant: int | str
        :param region: (optional) The Pokémon region
        :type region: str

        :raise DataNotExistError: The identifier is improbable (less than 0)
        :raise DataNotFoundError: The Pokémon doesn't exist
        """
        def is_number(x):
            try:
                int(x)
                return True
            except ValueError:
                return False

        if is_number(identifiant) and int(identifiant) < 0:
            raise DataNotExistError
        return Pokemon(call(f"pokemon/{identifiant}", region=region))

    def __init__(self, data=...) -> None:
        """ Constructor of Pokémon

        :param data: All data of the Pokémon.
        :type data: dict
        """
        self._pokedex_id: int = data['pokedex_id']
        self._generation: int = data['generation']
        self._category: str = data['category']
        self._name: abc.Name = abc.Name(data['name'])
        self._sprites: abc.Sprites = abc.Sprites(data['sprites'])
        self._types: abc.Types = abc.Types(data['types'])
        self._talents: list[abc.Talent] = [abc.Talent(obj) for obj in data['talents']] if data['talents'] else []
        self._stats: abc.Stats = abc.Stats(data['stats'])
        self._resistances: abc.Resistances = abc.Resistances(data['resistances'])
        self._evolution: abc.Evolutions = abc.Evolutions(data['evolution'])
        self._height: abc.Height = abc.Height(data['height'])
        self._weight: abc.Weight = abc.Weight(data['weight'])
        self._egg_groups: list[str] = data['egg_groups']
        self._sexe: abc.Sexe = abc.Sexe(data['sexe'])
        self._catch_rate: int = data['catch_rate']
        self._level_100: int = data['level_100']
        self._formes: list[abc.Forme] = [abc.Forme(obj) for obj in data['formes']] if data['formes'] else []

    @property
    def pokedex_id(self):
        """ The number in the national pokédex

        :rtype: int
        """
        return self._pokedex_id

    @property
    def generation(self):
        """ The publication generation

        :rtype: int
        """
        return self._generation

    @property
    def category(self):
        """ The Pokémon category

        :rtype: str
        """
        return self._category

    @property
    def name(self):
        """ The name of the Pokémon

        :rtype: abc.Name
        """
        return self._name

    @property
    def sprites(self):
        """ The sprites of the Pokémon

        :rtype: abc.Sprites
        """
        return self._sprites

    @property
    def types(self):
        """ The types of the Pokémon

        :rtype: abc.Types
        """
        return self._types

    @property
    def talents(self):
        """ The list of Pokémon talents

        :rtype: list[abc.Talent]
        """
        return self._talents

    @property
    def stats(self):
        """ The stats of the Pokémon

        :rtype: abc.Stats
        """
        return self._stats

    @property
    def resistances(self):
        """ Pokémon resistances

        :rtype: abc.Resistances
        """
        return self._resistances

    @property
    def evolution(self):
        """ Pokémon evolutions

        :rtype: abc.Evolutions
        """
        return self._evolution

    @property
    def height(self):
        """ The size of the Pokémon

        :rtype: abc.Height
        """
        return self._height

    @property
    def weight(self):
        """ The weight of the Pokémon

        :rtype: abc.Weight
        """
        return self._weight

    @property
    def egg_groups(self):
        """ The list of Pokémon egg's group

        :rtype: list[str]
        """
        return self._egg_groups

    @property
    def sexe(self):
        """ The percentage chance of gender appearing

        :rtype: abc.Sexe
        """
        return self._sexe

    @property
    def catch_rate(self):
        """ Pokémon capture rate

        :rtype: int
        """
        return self._catch_rate

    @property
    def level_100(self):
        """ The number of experience of the Pokémon to reach level 100

        :rtype: int
        """
        return self._level_100

    @property
    def formes(self):
        """ Alternative forms of the Pokémon

        :rtype: list[abc.Forme]
        """
        return self._formes

    def __str__(self) -> str:
        return self._name.fr

    def __repr__(self) -> str:
        return f"<{self._pokedex_id:04}:{str(self)}>"

    def __eq__(self, other) -> bool:
        if isinstance(other, Pokemon):
            return self._pokedex_id == other._pokedex_id and self._name == other._name
        return False


class Generation:
    """Represent the data of a generation"""
    @staticmethod
    def all():
        """List all generation."""
        all_gen = []
        all_data = call(f"gen")
        o = len(all_data)
        for data in all_data:
            i = len(all_gen)
            p = round(i * 100 / o)
            print(f"\r[{i:2}/{o:02}]▐{'█' * p}{' ' * (100 - p)}▌ : {p:3}%", end='')
            all_gen.append(Generation(data))
        print('\r', end='')

        return all_gen

    @staticmethod
    def get(generation: int):
        """Give the identified generation"""
        return Generation(call(f"gen/{generation}"))

    def __init__(self, data: dict | list):
        if isinstance(data, dict):
            self._generation = data['generation']
            self._from = data['from']
            self._to = data['to']
        else:
            self._generation = data[0]['generation']
            self._from = data[0]['pokedex_id']
            self._to = data[-1]['pokedex_id']

    @property
    def generation(self):
        return self._generation

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    def __str__(self):
        return f"Génération {self._generation}"

    def __repr__(self):
        return f"<{self._generation}:[{self._from} -> {self._to}]>"

    def __eq__(self, other):
        if isinstance(other, Generation):
            return self._generation == other._generation

    @property
    def pokemons(self) -> list[Pokemon]:
        return [Pokemon.get(i) for i in range(self.from_, self.to + 1)]


class Type:
    _LENGTH = len(call(f"types"))

    @staticmethod
    def get(type1: int | str, type2: int | str = ...):
        if isinstance(type1, int) and type1 > Type._LENGTH:
            type2 = type1 % Type._LENGTH
            type1 //= Type._LENGTH
        return Type(call(f"types/{type1}{'/' + str(type2) if type2 is not ... else ''}"))

    @staticmethod
    def all():
        all_types = []
        all_data = call(f"types")
        o = len(all_data)
        for data in all_data:
            i = len(all_types)
            p = round(i * 100 / o)
            print(f"\r[{i:4}/{o}]▐{'█' * p}{' ' * (100 - p)}▌ : {p:3}%", end='')
            all_types.append(data)
        print('\r', end='')

        return all_types

    def __init__(self, data: dict):
        if isinstance(data['id'], int):
            self._id: int = data['id']
            self._name: abc.Name = abc.Name(data['name'])
            self._sprites: Image.Image = call_image(data['sprites'])
        else:
            self._id: int = data['id'][0] * self._LENGTH + data['id'][1]
            self._name: abc.Name = abc.Name.concat(
                abc.Name({"fr": data["name"]["fr"][0], "en": data["name"]["en"][0], "jp": data["name"]["jp"][0]}),
                abc.Name({"fr": data["name"]["fr"][1], "en": data["name"]["en"][1], "jp": data["name"]["jp"][1]})
            )
            self._sprites: Image.Image = concat(
                call_image(data['sprites'][0]),
                call_image(data['sprites'][1]),
                self._name.fr
            )
        self._resistances: abc.Resistances = abc.Resistances(data['resistances'])
        self._pokemons: list[Pokemon] = ([Pokemon(obj) for obj in data['pokemons']]) if 'pokemons' in data else []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def sprites(self):
        return self._sprites

    @property
    def resistances(self):
        return self._resistances

    @property
    def pokemons(self):
        return self._pokemons

    def __str__(self):
        return str(self._name.fr)

    def __repr__(self):
        return f"<{self._id}:{self._name}>"

    def __eq__(self, other):
        if isinstance(other, Type):
            return self._id == other._id
        return False
