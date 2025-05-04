import reflex as rx

def About() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.box(
                rx.heading(
                    "About Me"
                    ),
                rx.text(
                    """
                    
                    """
                    )
                )
            )
        )