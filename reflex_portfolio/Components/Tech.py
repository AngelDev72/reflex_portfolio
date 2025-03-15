import reflex as rx
from reflex_portfolio.Components.Image import TecImage


def Tech_Stack() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Language"
                        ),
                        rx.hstack(
                            rx.image(
                                src="/Img/Language/python-wordmark.png",
                                width="50px",
                                height="auto"
                            ),
                            rx.image()
                        ),
                        rx.hstack(
                            rx.image(
                                src="/Img/Language/css3.png"
                            ),
                            rx.image(
                                src="/Img/Language/html5.png"
                            )
                        )
                    )
                ),
                rx.spacer(),
                rx.box(
                    rx.text(
                        "Framework"
                    ),
                ),
                rx.spacer(),
                rx.box(
                    rx.text(
                        "Technology"
                    )
                )
            )
        ),width="100%"
    )