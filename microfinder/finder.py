from flask import Flask, render_template, request, url_for, redirect
import search
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tuwase'
app.config['DEBUG'] = True


@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        search_key = request.form['search']
        data_name, data_url, data_price = search.find_jumia(search_key)
        return render_template("jum.html", search_key=search_key, data_name=data_name, data_url=data_url, data_price=data_price)
    else:
        return render_template("index.html")


@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/jumia/", methods=['GET', 'POST'])
def jumia():
    if request.method == "POST":
        search_key = request.form['search']
        data_name, data_url, data_price = search.find_jumia(search_key)
        return render_template("jum.html", search_key=search_key, data_name=data_name, data_url=data_url, data_price=data_price)


if __name__ == "__main__":
    app.run()
