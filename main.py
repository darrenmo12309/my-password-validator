import flask


# TODO: change this to your academic email
AUTHOR = "darrenmo@sas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: to be implemented
    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Too short"}), 200
    elif sum([c.isupper() for c in pw]) < 1:
        return flask.jsonify({"valid": False, "reason": "No uppercase"}), 200
    elif sum([c.isdigit() for c in pw]) < 1:
        return flask.jsonify({"valid": False, "reason": "No digit"}), 200
    else:
        for c in pw:
            if c == "!" or c == "@" or c == "#" or c == "$" or c == "%" or c == "^" or c == "&" or c == "*":
                return flask.jsonify({"valid": True, "reason": ""}), 200
            
    return flask.jsonify({"valid": False, "reason": "No special character"}), 200
