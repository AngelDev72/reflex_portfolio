import reflex as rx

def Projects() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.hstack(
                rx.text(
                    "Some of my current Projects"
                )
            ),
            rx.box(
                rx.text("Pymon:"),
                rx.text(""),
                #rx.link()
            ),rx.spacer(spacing="2"),
            
        )
    )