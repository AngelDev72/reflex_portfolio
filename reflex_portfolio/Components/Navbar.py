import reflex as rx

from ..Colors.Colors import Colors


def Navbar(active_page: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            "AngelDev 🐍"
        ),
        rx.spacer(spacing="2"),
        top="0",
        z_index="999",
        width="100%",
        background_color=Colors.Navbar.value,
        box_shadow="md"
        )