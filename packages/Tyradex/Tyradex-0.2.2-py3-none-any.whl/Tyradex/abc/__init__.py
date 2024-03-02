from PIL import Image

from Tyradex.maker import call_image, special_call_image


class Name:
    def __init__(self, data):
        self.fr = data['fr'] if data['fr'] else 'Unknown'
        self.en = data['en'] if data['en'] else 'Unknown'
        self.jp = data['jp'] if data['jp'] else 'Unknown'

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.fr == other.fr and self.en == other.en and self.jp == other.jp
        return False

    def concat(self, other, *, fill=' - '):
        return Name({
            'fr': f"{self.fr}{fill}{other.fr}",
            'en': f"{self.en}{fill}{other.en}",
            'jp': f"{self.jp}{fill}{other.jp}",
        })


class Sprites:
    class GMaxSprites:
        def __init__(self, data):
            self.regular = call_image(data['regular']) if data and data['regular'] else b''
            self.shiny = call_image(data['shiny']) if data and data['shiny'] else b''

    def __init__(self, data):
        self.regular = call_image(data['regular']) if data['regular'] else b''
        self.shiny = call_image(data['shiny']) if data['shiny'] else b''
        self.gmax = self.GMaxSprites(data['gmax'])


class Types:
    @staticmethod
    def get_all_types():
        types = [
            "Normal",
            "Plante",
            "Feu",
            "Eau",
            "Électrik",
            "Glace",
            "Combat",
            "Poison",
            "Sol",
            "Vol",
            "Psy",
            "Insecte",
            "Roche",
            "Spectre",
            "Dragon",
            "Ténèbres",
            "Acier",
            "Fée",
        ]
        return [[type1] if type1 == type2 else [type1, type2] for type1 in types for type2 in types]

    def __init__(self, data):
        if data:
            if len(data) == 2:
                self.name = f"{data[0]['name']} - {data[1]['name']}"
                self.image = special_call_image(data[0]['image'], data[1]['image'])
            else:
                self.name = data[0]['name']
                self.image = data[0]['image']
        else:
            self.name = "None"
            self.image = Image.new("RGBA", (60, 60))


class Talent:
    def __init__(self, data):
        self.name = data['name']
        self.tc = data['tc']


class Stats:
    def __init__(self, data):
        if data:
            self.hp = data['hp']
            self.atk = data['atk']
            self.def_ = data['def']
            self.spe_atk = data['spe_atk']
            self.spe_def = data['spe_def']
            self.vit = data['vit']
        else:
            self.hp = 0
            self.atk = 0
            self.def_ = 0
            self.spe_atk = 0
            self.spe_def = 0
            self.vit = 0


class Resistances:
    def __init__(self, data):
        raw_data = {}
        if data:
            for obj in data:
                name, multiplier = obj.values()
                raw_data[name] = multiplier
        self.normal = raw_data['Normal'] if 'Normal' in raw_data else 1
        self.plante = raw_data['Plante'] if 'Plante' in raw_data else 1
        self.feu = raw_data['Feu'] if 'Feu' in raw_data else 1
        self.eau = raw_data['Eau'] if 'Eau' in raw_data else 1
        self.electrik = raw_data['Électrik'] if 'Électrik' in raw_data else 1
        self.glace = raw_data['Glace'] if 'Glace' in raw_data else 1
        self.combat = raw_data['Combat'] if 'Combat' in raw_data else 1
        self.poison = raw_data['Poison'] if 'Poison' in raw_data else 1
        self.sol = raw_data['Sol'] if 'Sol' in raw_data else 1
        self.vol = raw_data['Vol'] if 'Vol' in raw_data else 1
        self.psy = raw_data['Psy'] if 'Psy' in raw_data else 1
        self.insecte = raw_data['Insecte'] if 'Insecte' in raw_data else 1
        self.roche = raw_data['Roche'] if 'Roche' in raw_data else 1
        self.spectre = raw_data['Spectre'] if 'Spectre' in raw_data else 1
        self.dragon = raw_data['Dragon'] if 'Dragon' in raw_data else 1
        self.tenebres = raw_data['Ténèbres'] if 'Ténèbres' in raw_data else 1
        self.acier = raw_data['Acier'] if 'Acier' in raw_data else 1
        self.fee = raw_data['Fée'] if 'Fée' in raw_data else 1


class Evolutions:
    class Pokemon:
        def __init__(self, data):
            self.pokedex_id = data['pokedex_id']
            self.name = data['name']
            self.condition = data['condition'] if 'condition' in data else ''

    class Mega:
        def __init__(self, data):
            self.orbe = data['orbe']
            self.sprites = Sprites.GMaxSprites(data['sprites'])

    def __init__(self, data):
        self.pre = [self.Pokemon(obj) for obj in data['pre']] if data and data['pre'] else []
        self.next = [self.Pokemon(obj) for obj in data['next']] if data and data['next'] else []
        self.mega = [self.Mega(obj) for obj in data['mega']] if data and data['mega'] else []

    @property
    def next_evo(self):
        return self.next[0]

    @property
    def previous_evo(self):
        return self.pre[-1]


class Height:
    def __init__(self, data: str):
        if data is None:
            data = f"0 m"
        try:
            self._height = float(data.replace(' m', '').replace(',', '.'))
        except ValueError:
            self._height = float(data.replace('m', '').replace(',', '.'))

    @property
    def height_m(self):
        return self._height

    @property
    def height_ft(self):
        return round(self._height * 3.281, 2)


class Weight:
    def __init__(self, data: str):
        if data is None:
            data = f"0 kg"

        self._weight = float(data.replace(' kg', '').replace(',', '.'))

    @property
    def weight_kg(self):
        return self._weight

    @property
    def weight_lb(self):
        return round(self._weight * 2.205, 2)


class Sexe:
    def __init__(self, data):
        self.male = data['male'] if data and data['male'] else 0
        self.female = data['female'] if data and data['male'] else 0


class Forme:
    def __init__(self, data):
        self.region = data['region']
        self.name = Name(data['name'])
