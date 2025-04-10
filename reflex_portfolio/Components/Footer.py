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
        margin_y="15px",
        bg=Colors.Footer.value,
        bottom="0"
    )