import reflex as rx
from ..Styles.Styles import Size

def Projects() -> rx.Component:
    return rx.container(
        rx.vstack(
                rx.text(
                    "Some of my current Projects"
                ),
                padding_bottom=Size.BIG.value,
            ),
            rx.hstack(
            rx.box(
                rx.text("Pymon:"),
                rx.text("""
                        Game design to have an inluence of AI later on the go. 
                        Pymon introduces 160 species of Pymons.
                        You may notice some similarity to Pokémon, 
                        but I tried to make it the most original as posible without making it too similar also.
                        """),
                #rx.link()
            ),rx.spacer(spacing="2"),
            rx.box(
                rx.text("Pymon Wiki:"),
                rx.text("""
                        
                        """),
                #rx.link()
            ),rx.spacer(spacing="2"),
            rx.box(
                rx.text(
                    "Chick'NTec:"),
                rx.text("""
                        
                        """),
                #rx.link()
            ),rx.spacer(spacing="2"),
            rx.box(
                rx.text("AviTec:"),
                rx.text("""
                        
                        """),
            #    #rx.link()
            ),rx.spacer(spacing="2"),
        ),
            align="center",
            flex_wrap="wrap",
            padding_top=Size.XX.value,
    )