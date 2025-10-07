import reflex as rx
from ..Styles.Styles import Size

def Projects() -> rx.Component:
    return rx.container(
        rx.vstack(
                rx.text(
                    "Some of my current Projects:"
                ),
                padding_bottom=Size.BIG.value,
                align="center",
            ),
            rx.hstack(
            rx.box(
                rx.vstack(
                    rx.text("Pymon:"),
                    padding_bottom=Size.MEDIUM.value,
                ),
                rx.text("""
                        Game design to have an inluence of AI later on the go. 
                        Pymon introduces 160 species of Pymons.
                        You may notice some similarity to Pokémon, 
                        but I tried to make it the most original as posible without making it too similar also.
                        """),
                #rx.link()
            ),
            rx.spacer(spacing="2"),
            rx.box(
                rx.vstack(
                    rx.text("Pymon Wiki:"),
                    padding_bottom=Size.MEDIUM.value,
                ),
                rx.text("""
                        Landing page with steticand modern pixel art,
                        disinged to catch players and present
                        the World of Pymon with a envolping
                        visaul narrative and retro futurist style.
                        
                        """),
                #rx.link()
            ),
            rx.spacer(spacing="2"),
            rx.box(
                rx.vstack(
                    rx.text("Chick'NTec:"),
                    padding_bottom=Size.MEDIUM.value,
                ),
                rx.text("""
                        Intelligent platform for poultry automatization
                        , disigned to control incubation, monitoring 
                        and farm gestion with digital presesion and 
                        sostainable focus.
                        """),
                #rx.link()
            ),
            rx.spacer(spacing="2"),
            rx.box(
                rx.vstack(
                    rx.text("AviTec:"),
                    padding_bottom=Size.MEDIUM.value,
                ),
                rx.text("""
                        Page focused on technical solutions and smart 
                        system devolpment to optimize agroindustrial  
                        processes and connect innovation and real life 
                        producctions.
                        """),
            #    #rx.link()
            )
            ,rx.spacer(spacing="2"),
            padding_top=Size.MEDIUM.value,
        ),
            align="center",
            flex_wrap="wrap",
            padding_top=Size.XX.value,
    )