"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_portfolio.Components.Navbar import Navbar
from reflex_portfolio.Components.Header import Header
from reflex_portfolio.Components.Memorium import Memory
from reflex_portfolio.Components.Bio import Bio
from reflex_portfolio.Components.Footer import Footer
from reflex_portfolio.Components.Tech import Tech_Stack as Tech

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
                Bio(),
                Tech(),
                Memory(),
                ),
            ),
            Footer(),
    max_width="100%"
    )


app = rx.App()
app.add_page(index)
