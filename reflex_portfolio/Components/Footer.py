import reflex as rx

from reflex_portfolio.Components.Footer import footer

def Footer() -> rx.Component:
    return rx.container(
        rx.hstack(
        rx.text("Coding from México to the world!")
        )
    )