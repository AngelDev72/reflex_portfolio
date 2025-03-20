import reflex as rx

def Tech_Image(source: str, height: int = None, width: int = None) -> rx.Component:
    style = {}
    if height:
        style["height"] = f"{height}px"
    if width:
        style["width"] = f"{width}px"
    return rx.image(src=source, style=style)

def Link_Image(url: str, src: str, height: int = None, width: int = None) -> rx.Component:
    style = {}
    if height:
        style["height"] = f"{height}px"
    if width:
        style["width"] = f"{width}px"
    return rx.link(
        rx.image(src=src, style=style),
        href=url,
        is_external=True,
        
    )