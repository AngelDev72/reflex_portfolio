"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .Components.Navbar import Navbar
from .Components.Header import Header, Social
from .Components.Memorium import Memory
from .Components.Bio import Bio
from .Components.Footer import Footer
from .Components.Tech import Language as Lang, Framework as Frames, Technology as Soft
from .About_Me import About
from .Projects import Projects

class State(rx.State):
    """The app state."""

    @rx.var
    def is_home(self) -> bool:
        return self.router.pathname == "/"

    @rx.var
    def is_about(self) -> bool:
        return self.router.pathname == "/about"

    @rx.var
    def is_projects(self) -> bool:
        return self.router.pathname == "/projects"


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        Navbar(),
        rx.center(
            rx.vstack(
                Header(),
                Social(),
                Bio(),
                rx.hstack(
                    Lang(),
                    Frames(),
                    Soft()
                    ),
                Memory(),
                ),
            ),
        Footer(),
    max_width="100%"
    )



app = rx.App()
app.add_page(index)
app.add_page(Projects, route="/projects", title="Projects")
app.add_page(About, route="/projects", title="Projects")
