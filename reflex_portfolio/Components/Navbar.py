import reflex as rx

from reflex_portfolio.Colors.Colors import Colors


def Navbar(active_page: str) -> rx.Component:
    pages={
        "AngelDev":[
            (
                "Projects",
                "/projects",
                ),
            (
                "About",
                "/about"
                )
            ]
        "About":[
            (
                "AngelDev",
                "/",
                ),
            (
                "Projects",
                "/projects",
                )
            ]
        "Projects":[
            (
                "AngelDev",
                "/",
                ),
            (
                "About",
                "/about"
                )
            ]
    }
    links=[
        rx.link(
            label,
            href=url,
            style={
                "text_decoration":"none"
            }
            for label, url in pages.get(active_page, [])
            )
        ]
        
    return rx.hstack(
        rx.text(
            "AngelDev 🐍"
        ),
        rx.spacer(spacing="2"),
        ),
        top="0",
        z_index="999",
        width="100%",
        background_color=Colors.Navbar.value,
        box_shadow="md"
    )