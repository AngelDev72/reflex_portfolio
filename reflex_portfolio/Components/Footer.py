import reflex as rx
from reflex_portfolio.Colors.colors import Colors

def Footer() -> rx.Component:
    return rx.container(
        rx.hstack(
        rx.text("Coding from México to the world!")
        ),
        bottom="0",
        bg=Colors.footer.value
    )