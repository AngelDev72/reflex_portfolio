import reflex as rx

def Stack() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.text(
                            "Language"
                        ),
                        rx.vstack()
                    ),
                    rx.box(
                        rx.text(
                            "Frameworks"
                        ),
                        rx.vstack()
                    ),
                    rx.box(
                        rx.text(
                            "Technologies"
                        ),
                        rx.vstack()
                    )
                ),
            ),

        )
    )



def Stack_icon() -> rx.Component:
    return rx.icon()