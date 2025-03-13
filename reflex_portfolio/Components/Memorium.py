import reflex as rx

from reflex_portfolio.Components.Avatar import Arturo

def Memory() -> rx.Component:
    return rx.center(
        rx.vstack(
            Arturo(),
            rx.text(
                "1984-2025"
            ),
            rx.text(
                """This portfolio  is a special thanks
                to a dear Friend, Colage and excellent Teacher.
                your lessons  will never be forgotten..."""
            ),
            rx.text(
                "R.I.P Arturo Moreno Salazar."
            ),
        )
    )