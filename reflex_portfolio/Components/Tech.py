import reflex as rx
from reflex_portfolio.Components.Image import Tech_Image as Tech



#                 Tech(
#                     "/Img/Language/Mojo.png",
#                     "50",
#                     "55"
#                     )
#                 ),
#             rx.hstack(
#                 Tech(
#                     "/Img/Language/css3.png",
#                     "50",
#                     "50"
#                     ),
#                 Tech(
#                     "/Img/Language/html5.png",
#                     "50",
#                     "50"
#                     )
#                 )
#             ),
#             rx.hstack(
#                 rx.vstack(
#                     rx.text(
#                         "Frameworks"
#                     ),
#                 rx.hstack(
#                     Tech(
#                         "/favicon.ico",
#                         "50",
#                         "50"
#                         ),
#                     Tech(
#                         "/Img/Framework/tensorflow.png",
#                         "50",
#                         "50"
#                         ),
#                     Tech(
#                         "/Img/Framework/pandas.png",
#                         "50",
#                         "50"
#                         )
#                 )
#                 rx.spacer(),
#                 rx.box(
#                     rx.text(
#                         "Technology"
#                         )
#                     )
#             )
#         )

def Language() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Language"
            )
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
                flex_wrap="wrap",
                spacing="2"
            )
        )