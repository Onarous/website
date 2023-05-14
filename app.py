from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("index.html")


@app.route('/about')
def hello():
    return render_template("about.html")


@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return f"Привет {name}, ваш id - {str(id)}"


if __name__ == "__main__":
    app.run(debug=True)