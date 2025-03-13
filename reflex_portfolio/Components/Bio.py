import reflex as rx

def Bio() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.text(
                """Hi! My name is Miguel Angel M. de Oca Sanchez.
                I'm passionate about Machine Learning and Data Science. 
                My preffered language for programming is Python,
                but I'm also learning other languages like Rust and Mojo."""
                ),
                width="100%",
                spacer="1",
            )
        )