import reflex as rx

def Stack() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.text(
                    "Language"
                    ),
                rx.text(
                    "Framework"
                ),
                rx.text(
                    "Technology"
                ),
                spacer="1",
                align="center"
            ),
        )
    )