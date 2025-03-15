import reflex as rx

def TecImage(source: str, height: int = None, width: int = None) -> rx.Component:
    style = {}
    if height:
        style["height"] = f"{height}px"
    if width:
        style["width"] = f"{width}px"
    return rx.image(src=source, style=style)