import reflex as rx
from reflex_portfolio.Colors.colors import Colors

def Footer() -> rx.Component:
    return rx.container(
        rx.vstack(
        rx.text("Coding from México to the world!")
        ),
        width="100%",
        margin_y="15px",
        bg=Colors.footer.value
    )