import reflex as rx

#from reflex_portfolio.Backend import State
from .Components.Navbar import Navbar
from .Components.Footer import Footer

def About() -> rx.Component:
    return rx.container(
        rx.vstack(
            Navbar(active_page="about"),
            rx.box(
                rx.heading(
                    "About Me"
                    ),
                rx.text(
                    """
                    
                    """
                    )
                ),
            Footer()
            )
        )