import reflex as rx

from ..Colors.Colors import Colors


def Navbar(active_page: str) -> rx.Component:
    pages={
        "AngelDev":[
            (
                "/projects",
                "Projects",
                ),
            (
                "/about",
                "About"
                )
            ],
        "About":[
            (
                "/",
                "AngelDev"
                ),
            (
                "/projects",
                "Projects",
                )
            ],
        "Projects":[
            (
                "/",
                "AngelDev",
                ),
            (
                "/about",
                "About"
                )
            ]
    }
    links=[
        rx.link(
            rx.text(label),
            href=path,
            style={"text_decoration"=="none"},
            )
            for group in pages.values()
            for path, label in group
            if path != f"/{active_page}" and not (active_page=="AngelDev" and path=="/")
        ]
        
    return rx.hstack(
        rx.text(
            "AngelDev 🐍"
        ),
        rx.spacer(spacing="2"),
        *links,
        top="0",
        z_index="999",
        width="100%",
        background_color=Colors.Navbar.value,
        box_shadow="md"
        )