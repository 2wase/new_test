from flask import Flask, render_template, request, url_for, redirect
import search
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tuwase'
app.config['DEBUG'] = True


@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        search_key = request.form['search']
        fine_data, data_url = search.find_jumia(search_key)
        return render_template("jum.html", search_key=search_key, fine_data=fine_data, data_url=data_url)
    else:
        return render_template("index.html")


@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/jumia/")
def jumia():
    return render_template("jum.html")


if __name__ == "__main__":
    app.run()
