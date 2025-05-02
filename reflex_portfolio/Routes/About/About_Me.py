import reflex as rx

@rx.page(
    route="/About",
    title="About Me"
    )
def About() -> rx.Component:
    return rx.box(
        rx.text(
            "placeholder"
            )
        )