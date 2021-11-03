from flask import Flask, render_template, request
from translate import get

application = Flask(__name__)

def parseform():
    return request.form.get("textarea", ""), request.form.get("action", "")
@application.route("/", methods=["post", "get"])
def process():
    r = get(*parseform())
    if "json" in request.form:
        return {"result": r["result"]}
    return render_template("index.html", data=r)


@application.route("/api", methods=["post"])
def api():
    return get(*parseform())


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=8080)
