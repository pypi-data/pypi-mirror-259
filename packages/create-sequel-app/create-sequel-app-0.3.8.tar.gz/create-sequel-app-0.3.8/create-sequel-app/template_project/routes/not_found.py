from reactpy import component, html

# This is an example of a 404 page.
# This page will render if a route is not found.


@component
def handle():
    return html.h1("Page not found 😭")
