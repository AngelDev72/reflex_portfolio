import reflex as rx
from reflex_portfolio.Colors.colors import Colors

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "AngelDev 🐍",
        ),
        height="30px",
        #width="100%",
        top="0",
        position="sticky",
        z_index="999",
        bg=Colors.navbar.value
    )
    