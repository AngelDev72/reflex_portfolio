import reflex as rx
from reflex_portfolio.Colors.Colors import Colors



def Navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "AngelDev 🐍"
        ),
        top="0",
        width="100%",
        background_color=Colors.Navbar.value
    )