"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_portfolio.Components.Navbar import Navbar
from reflex_portfolio.Components.Header import Header
from reflex_portfolio.Components.Memorium import Memory


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.vstack(
            Navbar(),
<<<<<<< HEAD
            #Angel(),
            #rx.image(
            #    src="/workspaces/reflex_portfolio/reflex_portfolio/Img/Yo.jpg"
            #),
            Memory(),
=======
            rx.center(
                Header(),
                Bio()
            ),
            Footer()
>>>>>>> d2ba8c8 (made changes)
        )
    )


app = rx.App()
app.add_page(index)
