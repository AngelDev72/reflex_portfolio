import reflex as rx

def Angel() -> rx.Component:
    return rx.avatar(
<<<<<<< HEAD
        src="/workspaces/reflex_portfolio/reflex_portfolio/Img/Yo.jpg",
=======
        src="/reflex_portfolio/reflex_portfolio/Img/Yo.jpg"
>>>>>>> d2ba8c8 (made changes)
        radius="full",
        size="7",
        fallback="AS",
        name="Angel Sanchez",
        color_scheme="cyan"
        ),

def Arturo() -> rx.Component:
    return rx.avatar(
        src="",
        radius="full",
        size="7",
        fallback="AM",
        name="Arturo Moreno",
        color_scheme="gray"
        )