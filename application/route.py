# from flask import Flask, redirect, url_for, render_template, request, session, flash
#
# app = Flask(__name__)
# app.secret_key = "hello"
#
#
# @app.route("/")
# @app.route("/home/")
# def root():
#     return render_template("index.html")
#
# @app.route("/display")
# def display():
#     return render_template("display.html")
#
#
# @app.route("/search", methods = ["POST", "GET"])
# def search():
#
#     return render_template("search.html")
#
# @app.route("/add")
# def add():
#     return render_template("add.html")
#
# @app.route("/update")
# def update():
#     return render_template("update.html")
#
# @app.route("/delete", methods=["POST", "GET"])
# def delete():
#     return render_template("delete.html")
#
#
#
#
