from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from second import second
from application.controller import Controller
from application.models import Record

app = Flask(__name__)
# c = Controller().db_connect()
# db = Controller.get_all(c)

@app.route("/")
@app.route("/home/")
def home():
    return render_template("index.html")

@app.route("/display")
def display():
    c = Controller()
    dt = c.get_all()
    return render_template("display.html", data=dt)


@app.route("/search", methods=["POST", "GET"])
def search():
    c = Controller()
    db = c.db_connect()
    dt = c.search_record(search_form_post())
    return render_template("search.html", date=dt)

@app.route('/', methods=['POST'])
def search_form_post():
    to_search = request.form['inc_num']
    return to_search

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        incident_number = request.form["incident_number"]
        incident_tpye = request.form["incident_tpye"]
        reported_date = request.form["reported_date"]
        pop_center = request.form["pop_center"]
        province = request.form["province"]
        company = request.form["company"]
        substance = request.form["substance"]
        significant = request.form["significant"]
        category = request.form["category"]

        record = Record(
            incident_num = incident_number,
            incident_typ = incident_tpye,
            report_date = reported_date,
            nearest_centre = pop_center,
            province = province,
            company = company,
            substance = substance,
            significant = significant,
            category = category,
        )
        c = Controller()
        db = c.db_connect()
        col = db['pipeline']
        col.insert_one(record.asdict())
        return redirect("/display")

@app.route("/reload")
def reload():
    return render_template("reload.html")

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/delete", methods=["POST", "GET"])
def delete():
    return render_template("delete.html")

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)

