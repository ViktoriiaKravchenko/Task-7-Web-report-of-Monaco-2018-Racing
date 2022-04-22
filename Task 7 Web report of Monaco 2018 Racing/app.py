from flask import Flask, render_template, url_for, request
from report import *
import pathlib


BASE_DIR = pathlib.Path(__file__).resolve().parent
START_DATA_FILE = BASE_DIR / 'data' / 'start.log'
FINISH_DATA_FILE = BASE_DIR / 'data' / 'end.log'
ABBREVIATIONS_FILE = BASE_DIR / 'data' / 'abbreviations.txt'


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/report")
def report_form():
    result = ordering(order="asc", driver_id="")
    return render_template("report_form.html", the_result=result)


@app.route("/report/", methods=["GET"])
def show_report():
    order = request.args.get("order")
    result = ordering(order=order, driver_id="")
    return render_template("show_report.html", the_order=order, the_result=result)


@app.route("/report/drivers")
def drivers_form():
    result = ordering(order="asc", driver_id="")
    return render_template("drivers_form.html", the_result=result)


@app.route("/report/drivers/")
def drivers_report():
    driver_id = request.args.get("driver_id")
    order = request.args.get("order")

    if "order" in request.args:
        result = ordering(order=order, driver_id="")
        return render_template("drivers_report.html", the_order=order, the_result=result)

    if "driver_id" in request.args:
        result = ordering(driver_id=driver_id, order="")
        return render_template("driver_info.html", the_result=result)


if __name__ == "__main__":
    app.run(debug=True)
