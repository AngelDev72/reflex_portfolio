import reflex as rx

def Tech_Stack() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Language"
                        ),
                        rx.flex(
                            rx.image(),
                            rx.image(),
                            rx.image(),
                            rx.image()
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
        )
    )