"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .Components.Navbar import Navbar
from .Components.Header import Header, Social
from .Components.Memorium import Memory
from .Components.Bio import Bio
from .Components.Footer import Footer
from .Components.Tech import Language as Lang, Framework as Frames, Technology as Soft
from .About_Me import About
from .Projects import Projects
from reflex_portfolio.Backend import State


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        Navbar(),
        rx.center(
            rx.vstack(
                Header(),
                Social(),
                Bio(),
                rx.hstack(
                    Lang(),
                    Frames(),
                    Soft()
                    ),
                Memory(),
                ),
            ),
        Footer(),
    max_width="100%"
    )



app = rx.App()
app.add_page(index)
app.add_page(Projects, route="/projects", title="Projects")
app.add_page(About, route="/projects", title="Projects")
