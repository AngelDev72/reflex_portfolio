import reflex as rx

def Angel() -> rx.Component:
    return rx.avatar(
        src="/Img/Yo.jpg",
        radius="full",
        size="7",
        fallback="AS",
        name="Angel Sanchez",
        color_scheme="cyan"
        ),

def Arturo() -> rx.Component:
    return rx.avatar(
        src="/Img/Arturo.jpg",
        radius="full",
        size="7",
        fallback="AM",
        name="Arturo Moreno",
        color_scheme="gray"
        )

def example() -> rx.Component:
    return rx.avatar(
        src="/Yo.jpg"
        )