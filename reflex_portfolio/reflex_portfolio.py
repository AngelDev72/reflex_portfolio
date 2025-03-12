"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_portfolio.Components.Navbar import Navbar
from reflex_portfolio.Components.Memorium import Memory


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.vstack(
            Navbar(),
            #Angel(),
            #rx.image(
            #    src="/workspaces/reflex_portfolio/reflex_portfolio/Img/Yo.jpg"
            #),
            Memory(),
        )
    )


app = rx.App()
app.add_page(index)
