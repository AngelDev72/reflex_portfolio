import reflex as rx

def Bio() -> rx.Component:
    return rx.box(
        rx.text(
        "Hi! My name is Miguel Angel M. de Oca Sanchez."
        ),
        rx.text(
        """I'm passionate about Machine Learning and Data Science. 
        My preffered language for programming is Python,
        but I'm also learning other languages like Rust and Mojo."""
        ),
        max_width="550px",
        width="100%",
        spacing="1",
    )