import reflex as rx
from reflex_portfolio.Colors.Colors import Colors

def Footer() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.center(
                rx.text(
                    "Coding from México to the world!"
                    )
            )
        ),
        width="100%",
        bg=Colors.Footer.value,
        bottom="0",
        position="fixed",
        left="0"
    )