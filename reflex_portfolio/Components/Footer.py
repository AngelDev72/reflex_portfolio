import reflex as rx
from ..Colors.Colors import Colors

def Footer() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "Coding from México to the world!"
                ),
        ),
        align="center",
        width="100%",
        bg=Colors.Footer.value,
        bottom="0",
        position="fixed",
        left="0"
        ),