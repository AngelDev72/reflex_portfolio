import reflex as rx

def Tech_Stack() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.text(
                        "Language"
                    ),
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