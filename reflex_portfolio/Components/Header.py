import reflex as rx
from reflex_portfolio.Components.Avatar import Angel

def Header() -> rx.Component:
    return rx.vstack(
        Angel(),
        rx.text(
            "@AngelDev72"
            ),
        rx.vstack(
            #rx.i
        )
        )