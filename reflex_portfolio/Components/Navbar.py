import reflex as rx
from .Colors.Colors import Colors
from reflex_portfolio.Backend import State 


def Navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "AngelDev 🐍"
        ),
        rx.spacer(spacing="2"),
        rx.cond(
            ~State.is_home,
            rx.link("Home", href="/", style={"text_decoration": "none"})
        ),
        rx.cond(
            ~State.is_about,
            rx.link("About Me", href="/about", style={"text_decoration": "none"})
        ),
        rx.cond(
            ~State.is_projects,
            rx.link("Projects", href="/projects", style={"text_decoration": "none"})
        ),
        top="0",
        z_index="999",
        width="100%",
        background_color=Colors.Navbar.value,
        box_shadow="md"
    )