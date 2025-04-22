"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .Components.Navbar import Navbar
from .Components.Header import Header
from .Components.Header import Social
from .Components.Memorium import Memory
from .Components.Bio import Bio
from .Components.Footer import Footer
from .Components.Tech import Language as Lang
from .Components.Tech import Frameworks as Frames
from .Components.Tech import Technology as Soft

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        Navbar(),
        rx.center(
            rx.vstack(
                Header(),
                Social(),
                Bio(),
                rx.hstack(
                    Lang(),
                    Frames(),
                    Tecnology(),
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
