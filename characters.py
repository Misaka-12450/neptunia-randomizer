from enum import IntEnum

_DISPLAY_NAMES: dict[int, str] = {
    0: "5pb.",
    9: "Azna=Leb",
    10: "B-Sha",
    16: "C-Sha",
    57: "Generia G.",
    70: "K-Sha",
    76: "Lee-Fi",
    81: "MAGES.",
    96: "Next-Gen Mech",
    103: "Paix St. Gliss",
    105: "Pippin@",
    116: "S-Sha",
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
        return _DISPLAY_NAMES.get(self.value, self.name.replace("_", " "))

    def __repr__(self):
        return f"Characters.{self.name}"