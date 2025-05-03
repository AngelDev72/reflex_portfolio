import reflex as rx

@rx.page(
        route="/Projects",
        title="Projects"
)
def Pymon() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text(
                "Pymon:"
                ),
            rx.text(
                """
                Game design to have an inluence of AI later on the go. Pymon introduces 130 species of Pymons.
                        You may notice some similarity to Pokémon, but I tried to make it the most original as posible without making it too similar also.
                """
                )
            )
        )

def EON() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.text(
                """
                Eon is basicly an AI Model I'm trying to develop on a basis of Psychology, Philosophy, Ethics and Morality.
                        The purpose of this project is to try and see if an AI Model can take better decisions once it's been trained on a more complex decision system.
                """
                )
            )
        )

def ChickNTec() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.center(
                rx.text(
                    """
                    
                    """
                    )
                )
            )
        )
