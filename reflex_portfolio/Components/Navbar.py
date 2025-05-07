import reflex as rx
#from reflex_portfolio.Backend import State
from reflex_portfolio.Colors.Colors import Colors


def Navbar(active_page: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            "AngelDev 🐍"
        ),
        rx.spacer(spacing="2"),
        rx.cond(
            active_page=="home",
            rx.link("projects", href="/projects", style={"text_decoration": "none"}),
            rx.link("About Me", href="/about", style={"text_decoration": "none"})
        ),
        rx.cond(
            active_page=="about",
            rx.link("Home", href="/", style={"text_decoration": "none"}),
            rx.link("projects", href="/projects", style={"text_decoration": "none"}),
        ),
        rx.cond(
            active_page=="projects",
            rx.link("Home", href="/", style={"text_decoration": "none"}),
            rx.link("About Me", href="/about", style={"text_decoration": "none"})
        ),
        top="0",
        z_index="999",
        width="100%",
        background_color=Colors.Navbar.value,
        box_shadow="md"
    )