import reflex as rx
from reflex_portfolio.Components.Image import Tech_Image as Tech


# def Tech_Stack() -> rx.Component:
#     return rx.hstack(
#         rx.text(
#             "Language"
#             ),
#             rx.hstack(
#                 Tech(
#                     "/Img/Language/python-wordmark.png",
#                     "50",
#                     "50"
#                     ),
#                 Tech(
#                     "/Img/Language/rust.png",
#                     "50",
#                     "50"
#                     ),
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

def Stack() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(
                "Language"
                
                ),
                rx.spacer(spacing="4"),
            rx.text(
                "Framework"
                ),
                rx.spacer(spacing="4"),
            rx.text(
                "Technology"
                ),

                rx.spacer(spacing="4")
            )
        )

def Image_Stack() -> rx.Component:
    return rx.flex(
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
        
        )