import reflex as rx
from reflex_portfolio.Components.Image import Tech_Image as Tech

def Language() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Language"
            ),
        rx.flex(
            Tech(
                "/Img/Language/python-wordmark.png",
                "50",
                "50"
                ),
            Tech(
                "/Img/Language/rust.png",
                "50",
                "50"
                ),
            Tech(
                "/Img/Language/Mojo.png",
                "50",
                "55"
                ),
            Tech(
                "/Img/Language/css3.png",
                "50",
                "50"
                ),
            Tech(
                "/Img/Language/html5.png",
                "50",
                "50"
                ),
                flex_wrap="wrap",
                spacing="2"
                #max_width="33%"
            )
        )

def Framework() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Frameworks"
            ),
        rx.flex(
            Tech(
                "/favicon.ico",
                "50",
                "50"
                ),
            Tech(
                "/Img/Framework/tensorflow.png",
                "50",
                "50"
                ),
            Tech(
                "/Img/Framework/pandas.png",
                "50",
                "50"
                ),
            Tech(
                "Img/Framework/numpy.png",
                "50",
                "50"
                ),
            Tech(
                "/Img/Framework/keras.png",
                "50",
                "50"
                ),
            Tech(
                "/Img/Framework/fastapi.png",
                "50",
                "50"
                ),
                flex_wrap="wrap",
                spacing="2",
                #max_width="33%"
            )
        )

def Technology() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Technology"
            ),
        rx.flex(
            Tech(
                "Img/Technology/git.png",
                "50",
                "50"
                ),
            Tech(
                "Img/Technology/vsc.png"
                "50",
                "50"
                ),
                
            )
        )