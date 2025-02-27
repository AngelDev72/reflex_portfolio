import reflex as rx

def Stack() -> rx.Component:
    return rx.center(
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
            ),
        ),
        width="75%"
    ),

def Stack_icon() -> rx.Component:
    return rx.icon()