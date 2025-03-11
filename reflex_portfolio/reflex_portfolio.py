"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_portfolio.Components.Navbar import Navbar
from reflex_portfolio.Components.Avatar import *


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.vstack(
            Navbar(),
            Angel(),
            Arturo(),
        )
    )


app = rx.App()
app.add_page(index)
