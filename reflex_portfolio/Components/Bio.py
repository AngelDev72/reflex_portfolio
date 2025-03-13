import reflex as rx

def Bio() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.text(
                "hey"
            )
        )
    )