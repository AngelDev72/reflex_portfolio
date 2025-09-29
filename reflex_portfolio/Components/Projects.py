import reflex as rx

def Projects() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.vstack(
                rx.text(
                    "Some of my current Projects"
                )
            ),
            rx.box(
                rx.text("Pymon:"),
                rx.text(""),
                #rx.link()
            ),rx.spacer(spacing="2"),
            rx.box(
                rx.text("Pymon Wiki:"),
                rx.text(""),
                #rx.link()
            ),rx.spacer(spacing="2"),
            rx.box(
                rx.text(
                    "Chick'NTec:"),
                rx.text(""),
                #rx.link()
            ),rx.spacer(spacing="2"),
            rx.box(
                rx.text("AviTec:"),
                rx.text(""),
                #rx.link()
            ),rx.spacer(spacing="2"),
            flex_wrap="wrap"
        )
    )