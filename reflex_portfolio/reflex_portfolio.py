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
            padding_top="50px",
            padding_bottom="50px",
            max_width="1200px",
            width="100%"
            ),
        justify="center",
        align="center",
        padding_top="25px",
        direction="column",
        width="100%",
        heigth="100%",
        ),
        Footer(),
        flex_direction="column",
        align="center",
        width="100%",
        min_height="100hv",
        bg= Colors.Bg.value,
        text_color=Colors.Text.value,
        
    )




app = rx.App()
app.add_page(index, route="/", title="AngelDev")