from reactpy import component, html, use_state, event
from reactpy.html import form, input, button, div, label

# Sequel.py does not prescribe a way to handle UI building.
# This is just an example of how to use bootstrap with reacypy in a Sequel.py app


FORM_LABEL_CLASS = "form-label"
FORM_CONTROL_CLASS = "form-control"
FORM_BLOCK_CLASS = "mb-3"
FORM_INPUT_CLASS = "form-control"
FORM_BUTTON_CLASS = "btn btn-primary my-2"
TEXT_AREA_CLASS = "form-control"


@component
def Container(props):
    return div({"className": "container"}, props)


@component
def ExampleForm():
    formdata, set_formdata = use_state(
        {
            "username": "",
            "name": "",
            "email": "",
        }
    )

    def handle_change(e, name):
        set_formdata({**formdata, name: e["target"]["value"]})

    def handle_submit(e):
        print(formdata)

    return Container(
        html._(
            form(
                div(
                    {"className": f"{FORM_BLOCK_CLASS}"},
                    label("Username:"),
                    input(
                        {
                            "className": f"{FORM_INPUT_CLASS}",
                            "value": formdata["username"],
                            "name": "username",
                            "on_change": lambda e: handle_change(e, "username"),
                        }
                    ),
                ),
                div(
                    label("Name:"),
                    input(
                        {
                            "className": f"{FORM_INPUT_CLASS}",
                            "value": formdata["name"],
                            "name": "name",
                            "on_change": lambda e: handle_change(e, "name"),
                        }
                    ),
                ),
                div(
                    label("Email:"),
                    input(
                        {
                            "className": f"{FORM_INPUT_CLASS}",
                            "value": formdata["email"],
                            "name": "email",
                            "on_change": lambda e: handle_change(e, "email"),
                        }
                    ),
                ),
                button(
                    {
                        "className": "btn btn-primary my-2",
                        "type": "submit",
                        "on_click": event(
                            lambda event: handle_submit(event), prevent_default=True
                        ),
                    },
                    "Submit",
                ),
            ),
        )
    )
