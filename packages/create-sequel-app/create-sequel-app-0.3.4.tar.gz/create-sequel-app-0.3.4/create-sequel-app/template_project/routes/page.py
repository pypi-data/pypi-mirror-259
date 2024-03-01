from reactpy import component, html
from reactpy_router import link

# This is an example of a simple page.

# This page is special because it is not in a routes subdirectory

# This page will always render on "/".


@component
def Home():
    return html._(
        html.h1(
            "hello!",
        ),
        html.p(
            "This is the home page rendered by routes/page.py. Checkout the links below to see more pages:"
        ),
        html.ul(
            html.li(
                link(
                    "A page that loads an HTTP request",
                    to="/user",
                )
            )
        ),
        html.ul(
            html.li(
                link(
                    "A dynamic route to: User/1",
                    to="/user/1",
                )
            )
        ),
        html.ul(
            html.li(
                html.a(
                    {
                        "href": "/example",
                    },
                    "A direct page example that renders a template in the direct_pages directory",
                )
            )
        ),
        html.ul(
            html.li(
                link(
                    "A 404 page that will render if a route is not found",
                    to="/whereamiwhoisthis?",
                )
            )
        ),
    )


# The handle function is how the router knows how to render the page


# Every page.py file should have a handle function
@component
def handle():
    return Home()
