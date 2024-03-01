from flask import jsonify

# API routes are essentially just an abstraction over the HTTP verbs.


def handle_get(req):
    # You can handle more complex requests inside the handler.
    # For Example:
    # if req.args.get("id"):
    #     return jsonify({"id": req.args.get("id")})
    # elif req.args.get("name"):
    #     return jsonify({"name": req.args.get("name")})
    # else:
    #     return ["User 1", "User 2"]
    return ["User 1", "User 2"]


def handle_post(req):
    return jsonify({"message": "User created"})


def handle_put(req):
    return jsonify({"message": "User updated"})


def handle_delete(req):
    return jsonify({"message": "User deleted"})


def handle(req):
    # Example: Return a JSON response
    POST = req.method == "POST"
    PUT = req.method == "PUT"
    DELETE = req.method == "DELETE"
    GET = req.method == "GET"

    if POST:
        return handle_post(req)
    if PUT:
        return handle_put(req)
    if DELETE:
        return handle_delete(req)
    if GET:
        return handle_get(req)
