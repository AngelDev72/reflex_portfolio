import reflex as rx
from reflex_portfolio.Backend import State
from .Components.Navbar import Navbar
from .Components.Footer import Footer

def Projects() -> rx.Component:
    return rx.container(
        rx.vstack(
            Navbar(),
            rx.box(
                rx.heading(
                    "Pymon"
                    ),
                rx.text(
                    """
                    Game design to have an inluence of AI later on the go. Pymon introduces 130 species of Pymons.
                        You may notice some similarity to Pokémon, but I tried to make it the most original as posible without making it too similar also.
                    """
                    )
                ),
            rx.box(
                rx.heading(
                    "EON"
                    ),
                rx.text(
                    """
                    Eon is basicly an AI Model I'm trying to develop on a basis of Psychology, Philosophy, Ethics and Morality.
                        The purpose of this project is to try and see if an AI Model can take better decisions once it's been trained on a more complex decision system.
                    """
                    )
                ),
            rx.box(
                rx.heading(
                    "ChickNTec"
                    ),
                rx.text(
                    """
                    Smart poultry project integrating IoT with data tracking. Chick’Ntec aims to modernize small-scale chicken farming
                    through real-time monitoring, ticketing systems, and AI-based production optimization.
                    """
                    )
                ),
            Footer(),
            )
        )