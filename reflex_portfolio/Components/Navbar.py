import reflex as rx

def Navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "AngelDev"
        ),
        width="100%"
    )