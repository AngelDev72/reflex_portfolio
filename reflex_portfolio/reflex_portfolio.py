"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from reflex_portfolio.Colors.colors import Colors
from reflex_portfolio.Components.Navbar import navbar
from reflex_portfolio.Components.Footer import Footer
from reflex_portfolio.Components.Heading import Header
from reflex_portfolio.Components.Avatar import Avatar
from reflex_portfolio.Components.Bio import Bio


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        rx.hstack(
            navbar()
            ),
        rx.flex(
            Avatar(),
            Header(),
        ),
        rx.flex(
            rx.vstack(
                Bio(),
            ),
        ),
        Footer(),
        bg="black",
        
    )


app = rx.App()
app.add_page(index)
