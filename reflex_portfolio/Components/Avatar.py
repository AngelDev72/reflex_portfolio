import reflex as rx

def Avatar() -> rx.Component:
    return rx.avatar(
        radius="full",
        size="7",
        fallback="AS",
        name="Angel Sanchez",
        color_scheme="cyan"
    ),
