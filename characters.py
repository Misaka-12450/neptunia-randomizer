from enum import IntEnum

_DISPLAY_NAMES: dict[int, str] = {
    0: "5pb.",
    1: "Abaddon",
    2: "Abnes",
    3: "Affimojas",
    4: "Ai Masujima",
    5: "Anonydeath",
    6: "Arfoire",
    7: "Artisan",
    8: "Artura Arrima",
    9: "Azna=Leb",
    10: "B-Sha",
    11: "Bamo",
    12: "Blanc",
    13: "Blossom Aisen",
    14: "Bouquet",
    15: "Broccoli",
    16: "C-Sha",
    17: "Cave",
    18: "CFW Brave",
    19: "CFW Judge",
    20: "CFW Magic",
    21: "CFW Trick",
    22: "Cheekama",
    23: "Cheetah",
    24: "Chian",
    25: "Chika Hakozaki",
    26: "Chrome",
    27: "Chuko",
    28: "Compa",
    29: "Copypaste",
    30: "Croire",
    31: "CyberConnect2",
    32: "Dark Black",
    33: "Dark CPU",
    34: "Dark Green",
    35: "Dark Knight",
    36: "Dark Purple",
    37: "Dark White",
    38: "DCD",
    39: "Deco",
    40: "Demon King Jester",
    41: "Dengekiko",
    42: "Dogoo Lady",
    43: "Dogoo Man",
    44: "Dreamcast",
    45: "Ein Al",
    46: "Estelle",
    47: "Ester Zira",
    48: "Fair",
    49: "Falcom",
    50: "Famitsu",
    51: "Filyn",
    52: "Financier",
    53: "Fried Shrimp",
    54: "Furapura",
    55: "Game Gear",
    56: "Ganache",
    57: "Generia G.",
    58: "Gheytz",
    59: "GM",
    60: "God Eater",
    61: "Goobs",
    62: "Grim Reaper",
    63: "Guild Woman",
    64: "Gust",
    65: "Hatsumi Sega",
    66: "Histoire",
    67: "Horyuchu",
    68: "IF",
    69: "Jade",
    70: "K-Sha",
    71: "Kei Jinguji",
    72: "Kiria",
    73: "Kurome Ankokuboshi",
    74: "Kuterogi",
    75: "Lady Wac",
    76: "Lee-Fi",
    77: "Lid",
    78: "Linda",
    79: "Little Rain",
    80: "Luke",
    81: "MAGES.",
    82: "Maker",
    83: "MarvelousAQL",
    84: "Mega Drive",
    85: "Mi",
    86: "Miamoato",
    87: "Million Arthur",
    88: "Mina Nishizawa",
    89: "Mine",
    90: "Minotauros",
    91: "Mister Badd",
    92: "Moru",
    93: "Nepgear",
    94: "Nepgya",
    95: "Neptune",
    96: "Next-Gen Mech",
    97: "Nisa",
    98: "Nitroplus",
    99: "Noire",
    100: "Older Brother",
    101: "Order Woman",
    102: "Overlord Momus",
    103: "Paix St. Gliss",
    104: "Peashy",
    105: "Pippin@",
    106: "Plutia",
    107: "Poona",
    108: "Ram",
    109: "Raw Meat",
    110: "RED",
    111: "Regu",
    112: "Rei Ryghts",
    113: "Resta",
    114: "Rom",
    115: "Ryuka",
    116: "S-Sha",
    117: "Sango",
    118: "Saori",
    119: "Sega Saturn",
    120: "Singe",
    121: "Steamax",
    122: "Stella",
    123: "Sting",
    124: "Tamsoft",
    125: "Tekken",
    126: "Tiara",
    127: "Time Eater",
    128: "Tsunemi",
    129: "Turquoise",
    130: "Umio",
    131: "Uni",
    132: "Uranus",
    133: "Uzume Tennouboshi",
    134: "Vert",
    135: "Vio",
    136: "Warechu",
    137: "Wyn",
    138: "Younger Brother",
    139: "Yu",
    140: "Yurina",
    141: "Yuzusuki",
    142: "Yvoire",
    143: "Zolgelicoff Tetsu",
    144: "†Black Cat Princess†",
}


class Characters(IntEnum):
    Fivepb = 0
    Abaddon = 1
    Abnes = 2
    Affimojas = 3
    Ai_Masujima = 4
    Anonydeath = 5
    Arfoire = 6
    Artisan = 7
    Artura_Arrima = 8
    Azna_Leb = 9
    B_Sha = 10
    Bamo = 11
    Blanc = 12
    Blossom_Aisen = 13
    Bouquet = 14
    Broccoli = 15
    C_Sha = 16
    Cave = 17
    CFW_Brave = 18
    CFW_Judge = 19
    CFW_Magic = 20
    CFW_Trick = 21
    Cheekama = 22
    Cheetah = 23
    Chian = 24
    Chika_Hakozaki = 25
    Chrome = 26
    Chuko = 27
    Compa = 28
    Copypaste = 29
    Croire = 30
    CyberConnect2 = 31
    Dark_Black = 32
    Dark_CPU = 33
    Dark_Green = 34
    Dark_Knight = 35
    Dark_Purple = 36
    Dark_White = 37
    DCD = 38
    Deco = 39
    Demon_King_Jester = 40
    Dengekiko = 41
    Dogoo_Lady = 42
    Dogoo_Man = 43
    Dreamcast = 44
    Ein_Al = 45
    Estelle = 46
    Ester_Zira = 47
    Fair = 48
    Falcom = 49
    Famitsu = 50
    Filyn = 51
    Financier = 52
    Fried_Shrimp = 53
    Furapura = 54
    Game_Gear = 55
    Ganache = 56
    Generia_G = 57
    Gheytz = 58
    GM = 59
    God_Eater = 60
    Goobs = 61
    Grim_Reaper = 62
    Guild_Woman = 63
    Gust = 64
    Hatsumi_Sega = 65
    Histoire = 66
    Horyuchu = 67
    IF = 68
    Jade = 69
    K_Sha = 70
    Kei_Jinguji = 71
    Kiria = 72
    Kurome_Ankokuboshi = 73
    Kuterogi = 74
    Lady_Wac = 75
    Lee_Fi = 76
    Lid = 77
    Linda = 78
    Little_Rain = 79
    Luke = 80
    MAGES = 81
    Maker = 82
    MarvelousAQL = 83
    Mega_Drive = 84
    Mi = 85
    Miamoato = 86
    Million_Arthur = 87
    Mina_Nishizawa = 88
    Mine = 89
    Minotauros = 90
    Mister_Badd = 91
    Moru = 92
    Nepgear = 93
    Nepgya = 94
    Neptune = 95
    Next_Gen_Mech = 96
    Nisa = 97
    Nitroplus = 98
    Noire = 99
    Older_Brother = 100
    Order_Woman = 101
    Overlord_Momus = 102
    Paix_St_Gliss = 103
    Peashy = 104
    Pippin = 105
    Plutia = 106
    Poona = 107
    Ram = 108
    Raw_Meat = 109
    RED = 110
    Regu = 111
    Rei_Ryghts = 112
    Resta = 113
    Rom = 114
    Ryuka = 115
    S_Sha = 116
    Sango = 117
    Saori = 118
    Sega_Saturn = 119
    Singe = 120
    Steamax = 121
    Stella = 122
    Sting = 123
    Tamsoft = 124
    Tekken = 125
    Tiara = 126
    Time_Eater = 127
    Tsunemi = 128
    Turquoise = 129
    Umio = 130
    Uni = 131
    Uranus = 132
    Uzume_Tennouboshi = 133
    Vert = 134
    Vio = 135
    Warechu = 136
    Wyn = 137
    Younger_Brother = 138
    Yu = 139
    Yurina = 140
    Yuzusuki = 141
    Yvoire = 142
    Zolgelicoff_Tetsu = 143
    Black_Cat_Princess = 144

    def __str__(self):
        return _DISPLAY_NAMES.get(self.value, self.name)
