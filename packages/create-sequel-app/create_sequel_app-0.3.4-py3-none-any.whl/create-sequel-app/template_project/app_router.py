from reactpy import component, html
from reactpy.backend.flask import configure, Options
from reactpy_router import route, simple
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

import importlib
import os
import importlib.util

app = Flask(__name__, template_folder="direct_pages")
CORS(app)


class AppRouter:
    """
    See these links for more information on how to use this class:
    - https://reactpy.github.io/reactpy/
    - https://reactive-python.github.io/reactpy-router/usage/
    """

    def __init__(self, app, api_prefix="/api"):
        print("Initializing AppRouter...")
        self.route_directory = "routes"
        self.routes = []
        self.app = app

        # Instantiate and set up the API router
        self.api_prefix = api_prefix
        self.register_route()

    def serve_direct_page(self, route_path, template_name, **template_kwargs):
        """
        Serve a Jinja template at the specified route path.

        Args:
            route_path (str): The path for the route.
            template_name (str): The name of the Jinja template to render.
            **template_kwargs: Additional keyword arguments to pass to the template.
        """

        @self.app.route(route_path)
        def serve_template():
            return render_template(template_name, **template_kwargs)

    # API "Route Registration". Effectively, this is a Flask route
    # that matches on any route with "/api" in the path.
    def register_route(self):
        @self.app.route(
            f"{self.api_prefix}/<path:subpath>",
            methods=["GET", "POST", "PUT", "DELETE"],
        )
        def api_redirect(subpath):
            return self.handle_request(subpath)

    # Handler method for API requests
    def handle_request(self, subpath):
        components = subpath.split("/")
        module_name = components[0]
        try:
            api_module = importlib.import_module(f"api.{module_name}.route")
            if len(components) > 1:
                return api_module.handle(*components[1:])
            return api_module.handle(request)
        except (ImportError, AttributeError):
            return jsonify({"error": "Not found"}), 404

    # Methods below build the routes from the route directory
    def import_route_module(self, module_path):
        # Convert file system path to Python module path
        module_path = module_path.replace("/", ".").rstrip(".py")
        return importlib.import_module(module_path)

    def construct_route_path(self, parts):
        # Convert parts into a route path, handling dynamic segments represented by square brackets
        route_path = "/".join(parts)
        route_path = route_path.replace("[", "{").replace("]", "}")
        return "/" + route_path

    def handle_directory(self, path, parts=[]):
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                # Recursively handle subdirectories
                self.handle_directory(full_path, parts + [entry])
            elif entry.endswith(".py"):
                modulename = entry[:-3]
                if modulename == "page":
                    # Construct route path from parts and handle the module
                    route_path = self.construct_route_path(parts)
                    module = self.import_route_module(
                        ".".join([self.route_directory] + parts + [modulename])
                    )
                    # Handle index
                    route_path = "/" if route_path.endswith(
                        "/index") else route_path
                    self.routes.append((route_path, module.handle()))

    def setup_routes(self):
        print("Colleciting routes")
        for directory in os.listdir(self.route_directory):
            dir_path = os.path.join(self.route_directory, directory)
            if os.path.isdir(dir_path):
                self.handle_directory(dir_path, [directory])

        # seed the router wtih "/" for index and "*" for 404

        print("Registering routes with the router")
        return simple.router(
            route("/", self.import_route_module("routes.page").handle()),
            *[route(route_path[0], route_path[1])
              for route_path in self.routes],
            route("*", self.import_route_module("routes.not_found").handle()),
        )

    # Configures and Runs the reactpy app from the app.py file
    def configure_reactpy(self, link_attributes):
        print("Configuring reactpy")

        @component
        def Router():
            return self.setup_routes()

        print("Loading CDN's")
        link_elements = [html.link(attrs) for attrs in link_attributes]

        configure(
            self.app,
            Router,
            options=Options(head=html._(*link_elements)),
        )
