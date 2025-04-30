import reflex as rx
from .Components.Navbar import Navbar
from .Components.Avatar import Angel


def Project() -> rx.Component:
    return rx.container(
        Navbar(),
        rx.vstack(
            Angel(),
            )
        )