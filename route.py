import pandas as pd
from flask import Flask, redirect, url_for, render_template, request, session, flash, json
from application.controller import Controller
from application.models import Record
import plotly.express as px
import json
import json
import plotly
import plotly.graph_objects as go
import numpy as np

app = Flask(__name__)
# app.config.from_object(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


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
    if request.method == "GET":
        return render_template("search.html")

    if request.method == "POST":
        incident_number = request.form["incident_number"]
        incident_type = request.form["incident_type"]
        reported_date = request.form["reported_date"]
        pop_center = request.form["pop_center"]
        province = request.form["province"]
        company = request.form["company"]
        substance = request.form["substance"]
        significant = request.form["significant"]
        category = request.form["category"]
        c = Controller()
        db = c.db_connect()
        col = db['pipeline']
        results = list(col.find({"$or": [
            {"Incident Number": incident_number},
            {"Incident Types": incident_type},
            {"Reported Date": reported_date},
            {"Nearest Populated Centre": pop_center},
            {"Province": province},
            {"Company": company},
            {"Substance": substance},
            {"Significant": significant},
            {"What happened category": category}
        ]}, {'Incident Number': 1, 'Incident Types': 1, 'Reported Date': 1, 'Nearest Populated Centre': 1,
             'Province': 1, 'Company': 1, 'Substance': 1, 'Significant': 1, 'What happened category': 1,
             '_id': 0}))
        json.dumps(results, default=object)
        session['res'] = results
        return redirect(url_for("searchresult"))


@app.route('/searchresult', methods=["POST", "GET"])
def searchresult():
    results = session.get('res', None)
    if results is None:
        flash("There is no matching record in database")
    return render_template("searchresult.html", results=results)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        incident_number = request.form["incident_number"]
        incident_type = request.form["incident_type"]
        reported_date = request.form["reported_date"]
        pop_center = request.form["pop_center"]
        province = request.form["province"]
        company = request.form["company"]
        substance = request.form["substance"]
        significant = request.form["significant"]
        category = request.form["category"]

        record = Record(
            incident_num=incident_number,
            incident_typ=incident_type,
            report_date=reported_date,
            nearest_centre=pop_center,
            province=province,
            company=company,
            substance=substance,
            significant=significant,
            category=category,
        )
        c = Controller()
        db = c.db_connect()
        col = db['pipeline']
        inc_num_in_db = c.record_eixsing_to_insert(incident_number)
        col.insert_one(record.asdict())
        return redirect("/display")


@app.route("/<string:inc_num>/update", methods=["POST", "GET"])
def update(inc_num):
    if request.method == "GET":
        c = Controller()
        db = c.db_connect()
        col = db['pipeline']
        results = col.find_one({"Incident Number": inc_num},
                               {'Incident Number': 1, 'Incident Types': 1, 'Reported Date': 1,
                                'Nearest Populated Centre': 1,
                                'Province': 1, 'Company': 1, 'Substance': 1, 'Significant': 1,
                                'What happened category': 1,
                                '_id': 0})
        return render_template("update.html", results=results)

    if request.method == "POST":
        incident_number = request.form["incident_number"]
        incident_type = request.form["incident_type"]
        reported_date = request.form["reported_date"]
        pop_center = request.form["pop_center"]
        province = request.form["province"]
        company = request.form["company"]
        substance = request.form["substance"]
        significant = request.form["significant"]
        category = request.form["category"]

        record = Record(
            incident_num=incident_number,
            incident_typ=incident_type,
            report_date=reported_date,
            nearest_centre=pop_center,
            province=province,
            company=company,
            substance=substance,
            significant=significant,
            category=category,
        )
        c = Controller()
        c.db_connect()
        c.update_record(record)
        flash("Record updated successfully!")
    return redirect("/display")


@app.route("/chart")
def chart():
    c = Controller()
    db = c.db_connect()
    df = c.all_in_df()
    year = extract_year(df)
    count = {}
    for i in year:
        count[i] = year.count(i)

    fig1 = px.bar(df, x='Company', y='Province', color='Incident Types',
                  barmode='group')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    header1 = "Fig 1"
    description1 = ""

    fig2 = bar_chart1()
    out = fig2.to_html(full_html=False)
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    fig3 = go.Figure(data=[go.Pie(labels=['Reported Date', 'Province', 'Substance', 'Significant'],
                                  values=['Reported Date', 'Province', 'Substance', 'Significant'])])
    fig3.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20)
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("chart.html", title="Chart", graph1JSON=graph1JSON, header1=header1,
                           description1=description1, graph3JSON=out, graph3JSON=graph3JSON)

def extract_year(df):
    temp = pd.DatetimeIndex(df['Reported Date']).year
    year = []
    for t in temp:
        year.append(t)
    return year

def bar_chart1():
    c = Controller()
    db = c.db_connect()
    datum = c.get_all()
    alberta_count = 0
    manitoba_count = 0
    bc_count = 0
    saskatchewan_count = 0
    ontario_count = 0
    new_brunswick_count = 0
    nova_scotia_count = 0
    quebec_count = 0

    for data in datum:
        if data['Province'] == "Alberta":
            alberta_count += 1
        elif data['Province'] == "British Columbia":
            bc_count += 1
        elif data['Province'] == "Saskatchewan":
            saskatchewan_count += 1
        elif data['Province'] == "Manitoba":
            manitoba_count += 1
        elif data['Province'] == "Ontario":
            ontario_count += 1
        elif data['Province'] == "New Brunswick":
            new_brunswick_count += 1
        elif data['Province'] == "Nova Scotia":
            nova_scotia_count += 1
        elif data['Province'] == "Quebec":
            quebec_count += 1
    x = np.array(
        ["AB", "BC", "SK", "MB", "ON", "NB", "NS", "QC"])
    y = np.array([alberta_count, bc_count, saskatchewan_count, manitoba_count, ontario_count, new_brunswick_count,
                  nova_scotia_count, quebec_count])
    fig2 = px.bar(x, y)
    fig2.show()
    return fig2

def pie_chart():
    c = Controller()
    db = c.db_connect()
    df = c.all_in_df()
    temp = pd.DatetimeIndex(df['Reported Date']).year
    year = []
    for t in temp:
        year.append(t)
    x = np.array(
        ["AB", "BC", "SK", "MB", "ON", "NB", "NS", "QC"])
    y = np.array([alberta_count, bc_count, saskatchewan_count, manitoba_count, ontario_count, new_brunswick_count,
                  nova_scotia_count, quebec_count])

@app.route("/<string:inc_num>/delete", methods=["POST", "GET"])
def delete(inc_num):
    if request.method == "POST":
        c = Controller()
        c.db_connect()
        c.delete_record(inc_num)
        return redirect("/search")
    return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)
