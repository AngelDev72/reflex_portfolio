import reflex as rx

from reflex_portfolio.Components.Avatar import Arturo

def Memory() -> rx.Component:
    return rx.center(
        rx.vstack(
            Arturo(),
            rx.text(
                "1984-2025"
            )
        )
    )