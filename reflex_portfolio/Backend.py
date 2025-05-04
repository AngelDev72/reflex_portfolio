import reflex as rx

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