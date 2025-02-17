import reflex as rx


rx.flex(
    rx.avatar(src="/img/Yo.jpg", fallback="AS", size="9", radius="full"),
    rx.text("Angel Sanchez", weight="bold", size="4"),
    #rx.text("@reflexuser", color_scheme="gray"),
#     rx.button(
#         "Edit Profile",
#         color_scheme="indigo",
#         variant="solid",
#     ),
    direction="column",
    spacing="1",
)