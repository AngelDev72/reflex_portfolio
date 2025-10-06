"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
#from reflex_portfolio.Backend import State
from .Components.Navbar import Navbar
from .Components.Header import Header, Social
from .Components.Memorium import Memory
from .Components.Bio import Bio
from .Components.Footer import Footer
from .Components.Tech import Language as Lang, Framework as Frames, Technology as Soft
from .Components.Projects import Projects
from .Colors.Colors import Colors
from .Styles.Styles import Size


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.flex(
        rx.vstack(
            Navbar("AngelDev"),
            Header(),
            Social(),
            Bio(),
            rx.hstack(
                Lang(),
                Frames(),
                Soft(),
                align="center",
                    ),
            Projects(),
            rx.hstack(
                Memory(),
                align="center",
            ),
            align="center",
            padding_top=Size.XX.value,
            width="100%"
            ),
        ),
        Footer(),
        flex_direction="column",
        align="center",
        width="100%",
        text_color=Colors.Text.value,
        padding_bottom=Size.BIG.value,
        bg= Colors.Bg.value,
        
    )




app = rx.App()
app.add_page(index, route="/", title="AngelDev")