import pandas as pd
import streamlit as st
import random

CHARACTERS: list = [
    "5pb.",
    "Abaddon",
    "Abnes",
    "Affimojas",
    "Ai Masujima",
    "Anonydeath",
    "Arfoire",
    "Artisan",
    "Artura Arrima",
    "Azna=Leb",
    "B-Sha",
    "Bamo",
    "Blanc",
    "Blossom Aisen",
    "Bouquet",
    "Broccoli",
    "C-Sha",
    "Cave",
    "CFW Brave",
    "CFW Judge",
    "CFW Magic",
    "CFW Trick",
    "Cheekama",
    "Cheetah",
    "Chian",
    "Chika Hakozaki",
    "Chrome",
    "Chuko",
    "Compa",
    "Copypaste",
    "Croire",
    "CyberConnect2",
    "Dark Black",
    "Dark CPU",
    "Dark Green",
    "Dark Knight",
    "Dark Purple",
    "Dark White",
    "DCD",
    "Deco",
    "Demon King Jester",
    "Dengekiko",
    "Dogoo Lady",
    "Dogoo Man",
    "Dreamcast",
    "Ein Al",
    "Estelle",
    "Ester Zira",
    "Fair",
    "Falcom",
    "Famitsu",
    "Filyn",
    "Financier",
    "Fried Shrimp",
    "Furapura",
    "Game Gear",
    "Ganache",
    "Generia G.",
    "Gheytz",
    "GM",
    "God Eater",
    "Goobs",
    "Grim Reaper",
    "Guild Woman",
    "Gust",
    "Hatsumi Sega",
    "Histoire",
    "Horyuchu",
    "IF",
    "Jade",
    "K-Sha",
    "Kei Jinguji",
    "Kiria",
    "Kurome Ankokuboshi",
    "Kuterogi",
    "Lady Wac",
    "Lee-Fi",
    "Lid",
    "Linda",
    "Little Rain",
    "Luke",
    "MAGES.",
    "Maker",
    "MarvelousAQL",
    "Mega Drive",
    "Mi",
    "Miamoato",
    "Million Arthur",
    "Mina Nishizawa",
    "Mine",
    "Minotauros",
    "Mister Badd",
    "Moru",
    "Nepgear",
    "Nepgya",
    "Neptune",
    "Next-Gen Mech",
    "Nisa",
    "Nitroplus",
    "Noire",
    "Older Brother",
    "Order Woman",
    "Overlord Momus",
    "Paix St. Gliss",
    "Peashy",
    "Pippin@",
    "Plutia",
    "Poona",
    "Ram",
    "Raw Meat",
    "RED",
    "Regu",
    "Rei Ryghts",
    "Resta",
    "Rom",
    "Ryuka",
    "S-Sha",
    "Sango",
    "Saori",
    "Sega Saturn",
    "Singe",
    "Steamax",
    "Stella",
    "Sting",
    "Tamsoft",
    "Tekken",
    "Tiara",
    "Time Eater",
    "Tsunemi",
    "Turquoise",
    "Umio",
    "Uni",
    "Uranus",
    "Uzume Tennouboshi",
    "Vert",
    "Vio",
    "Warechu",
    "Wyn",
    "Younger Brother",
    "Yu",
    "Yurina",
    "Yuzusuki",
    "Yvoire",
    "Zolgelicoff Tetsu",
    "†Black Cat Princess†",
]
NUM_CHARACTERS: int = len(CHARACTERS)
URL_BASE: str = "https://neptunia.fandom.com/wiki/"


def get_character_link(character: str) -> str:
    return f"{URL_BASE}{character.replace(" ","_")}"


def randomise_characters(n: int = NUM_CHARACTERS) -> pd.DataFrame:
    random_characters: list = random.sample(CHARACTERS, n)
    l = []
    for character in random_characters:
        l.append(get_character_link(character))
    return pd.DataFrame(l, columns=["Name"])


def display_characters(df: pd.DataFrame | None = None) -> None:
    if df is None:
        df = st.session_state.get("neptunia_randomised_characters")
        if df is None:
            st.warning(
                "Randomised character list not found. Showing sorted list of all characters.",
                icon=":material:error:",
            )
            l = []
            for character in CHARACTERS:
                l.append(get_character_link(character))
            df = pd.DataFrame(l, columns=["Name"])

    st.dataframe(
        df,
        column_config={
            "Name": st.column_config.LinkColumn(
                display_text=rf"{URL_BASE}([\s\S]+)",
            )
        },
    )


st.title("Neptune Character Name Randomiser")

st.markdown("This page randomises a list of names of all Neptunia characters.")
st.markdown("")
st.markdown("I use it as to generate hostnames for servers in my homelab.")

if "neptunia_randomised_characters" not in st.session_state:
    st.session_state["neptunia_randomised_characters"] = randomise_characters()

with st.form("settings"):
    num: int = st.slider(
        "\\# of characters to display", 1, NUM_CHARACTERS, NUM_CHARACTERS
    )
    st.form_submit_button(
        label="Randomise",
        icon=":material/shuffle:",
        type="primary",
        on_click=lambda: st.session_state.update(
            {"neptunia_randomised_characters": randomise_characters(num)}
        ),
    )


display_characters()
