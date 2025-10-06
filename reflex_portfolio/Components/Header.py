import reflex as rx
from .Avatar import Angel
from .Image import Link_Image as Link
from ..Styles.Styles import Size


def Header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            Angel(),
            rx.text(
                "@AngelDev72"
            ),
            #text_size=Size.BIG.value,
        )
    )

def Social() -> rx.Component:
    return rx.hstack(
        Link(
            "https://github.com/AngelDev72",
                src="/Img/Social/github.png",
                height=45,
                width=45
                ),
                rx.spacer(spacing="2"),
        Link(
            "https://kaggle.com/angeldev72",
            src="/Img/Social/kaggle.png",
            height=45,
            width=45
            ),
            rx.spacer(spacing="2"),
        Link(
            "https://.linkedin.com/in/miguel-angel-m-de-oca-sanchez-a44b00261?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
            src="Img/Social/linkedin.png",
            height=45,
            width=45
            ),
        rx.spacer(spacing="2"),
        Link(
            "https://x.com/AngelDev72",
                src="/Img/Social/X.png",
                height=45,
                width=45
            ),
        rx.spacer(spacing="2")
        )