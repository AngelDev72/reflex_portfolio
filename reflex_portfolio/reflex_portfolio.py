"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_portfolio.Colors.colors import Colors

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
            rx.vstack(
            rx.heading("AngelDev"),
            
        ),
    )


app = rx.App()
app.add_page(index)
