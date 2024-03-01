from reactpy import component, use_effect, use_state
from reactpy.html import div, h1
from reactpy_router import use_params
from components.example_use_form import ExampleForm
import requests


@component
def User():
    json, set_json = use_state([])
    params = use_params()
    id = params["id"]

    @use_effect(dependencies=[])
    def fetch_users():
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        set_json(response.json())

    if not json:
        return h1("loading...")
    else:
        return div(h1(f"Hello User #{id}"), ExampleForm())


@component
def handle():
    return User()
