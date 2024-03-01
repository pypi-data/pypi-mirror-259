from reactpy import component, html, use_effect, use_state
import requests


@component
def User():
    # Example usage of state
    json, set_json = use_state([])

    # Example usage of hooks
    @use_effect(dependencies=[])
    def fetch_users():
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        set_json(response.json())

    # Example usage of html
    return html.div(
        html.h1("This page loads an HTTP request and displays the results on the page"),
        html.h1(
            {"className": "text-3xl text-blue-500 font-bold underline text-clifford"},
            f"{json}",
        ),
    )


@component
def handle():
    return User()
