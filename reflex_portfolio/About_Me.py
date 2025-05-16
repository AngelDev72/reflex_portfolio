import reflex as rx


from .Components.Navbar import Navbar
from .Components.Footer import Footer

@rx.page(route="/about", title="About Me")
def About() -> rx.Component:
    return rx.container(
        rx.vstack(
            Navbar("About"),
            rx.box(
                rx.heading(
                    "About Me"
                    ),
                rx.text(
                    """
                    Things about me here
                    """
                    )
                ),
            Footer()
            )
        )