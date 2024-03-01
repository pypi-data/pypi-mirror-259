from app_router import AppRouter, app


# Example of loading a CSS library. These will be placed in the HTML head of the app
boot_strap = [
    {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css",
        "rel": "stylesheet",
        "integrity": "sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9",
        "crossorigin": "anonymous",
    },
    {
        "src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm",
        "crossorigin": "anonymous",
    },
    {
        "src": "https://kit.fontawesome.com/cdf7b08825.js",
        "crossorigin": "anonymous",
    },
    {
        "rel": "stylesheet",
        "href": "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.8.0/build/styles/atom-one-dark.min.css",
    },
    {
        "src": "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.8.0/build/highlight.min.js"
    },
    {
        "src": "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.8.0/build/languages/go.min.js"
    },
]

# Pass the link attributes to ReactPy
link_attributes = [*boot_strap]

app_router = AppRouter(app)

# circumvents the file router and servers a jinja or HTML template using python's render_template function
# by design, direct pages take precedence over file routes.
app_router.serve_direct_page("/example", "example.html", name="Example")


# Finally, call configure_reactpy to start the app with your configuration
app_router.configure_reactpy(link_attributes)
