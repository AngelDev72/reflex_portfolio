import reflex as rx

@rx.page(
    route="workspace/reflex_portfolio/reflex_portfolio/Routes/About/About_Me.py",
    title="About Me"
    )
def About() -> rx.Component:
    return rx.box(
        rx.text(
            "placeholder"
            )
        )