import reflex as rx
from reflex_portfolio.Components.Avatar import Angel
from reflex_portfolio.Components.Image import Link_Image as Link


def Header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            Angel(),
            rx.text(
                "@AngelDev72"
            ),

        )
    )