import random

import pandas as pd
import streamlit as st

from characters import Characters
from random_org import GenerateIntegers, RandomOrgAPIException

URL_BASE: str = "https://neptunia.fandom.com/wiki/"
NUM_CHARACTERS = len(Characters)


def get_character_link(character: str) -> str:
    return f"{URL_BASE}{character.replace(' ', '_')}"


def _get_random_indices(n: int) -> list[int]:
    if not st.secrets.get("random_org_api_key"):
        return random.sample(range(NUM_CHARACTERS), n)

    try:
        return GenerateIntegers(0, NUM_CHARACTERS - 1, n, replacement=False).post()
    except RandomOrgAPIException:
        st.warning(
            "Random.org API error encountered. Falling back to local randomisation.",
            icon=":material/warning:",
        )
        return random.sample(range(NUM_CHARACTERS), n)


def randomise_characters(n: int | None = None) -> pd.DataFrame:
    if not n or n > NUM_CHARACTERS:
        n = NUM_CHARACTERS

    random_indices = _get_random_indices(n)

    characters = [Characters(i) for i in random_indices]
    names = [str(character) for character in characters]
    links = [get_character_link(str(character)) for character in characters]
    return pd.DataFrame({"Name": names, "Wiki": links})


def display_characters(df: pd.DataFrame | None = None) -> None:
    if df is None:
        df = st.session_state.get("neptunia_randomised_characters")
        if df is None:
            st.warning(
                "Unable to fetch randomised character list. Please try again.",
                icon=":material/error:",
            )

    st.dataframe(
        df,
        column_config={
            "Wiki": st.column_config.LinkColumn(
                # display_text=rf"{URL_BASE}([\s\S]+)"
                display_text="🔗 Link"
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
