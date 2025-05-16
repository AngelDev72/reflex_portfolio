"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
#from reflex_portfolio.Backend import State
from .Components.Navbar import Navbar
from .Components.Header import Header, Social
from .Components.Memorium import Memory
from .Components.Bio import Bio
from .Components.Footer import Footer
from .Components.Tech import Language as Lang, Framework as Frames, Technology as Soft
from .About_Me import About
from .Projects import Projects



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        #Navbar("AngelDev"),
        rx.flex(
            rx.vstack(
                Navbar("AngelDev"),
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
app.add_page(index, route="/", title="AngelDev")
app.add_page(Projects, route="/projects", title="Projects")
app.add_page(About, route="/about", title="About Me")
