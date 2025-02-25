"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_portfolio.Colors.colors import Colors
from reflex_portfolio.Components.Navbar import navbar
from reflex_portfolio.Components.Footer import Footer


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
            navbar(),
            rx.hstack(
                rx.flex(
                rx.avatar(fallback="AS", radius="full",size="6", color_scheme="cyan"),
                rx.text("AngelDev", size="7", weight="bold"),
                spacing="2",
                padding="10px"
            ),
        
        ),
        rx.flex(
            rx.box(
                
            )
        ),
        rx.container (
            Footer()
        )
    )


app = rx.App()
app.add_page(index)
