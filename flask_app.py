from flask import Flask, render_template, request, session
from processing import difference_calculator, convert, format_input
from format_results import format_results

app = Flask(__name__)
# app.config["SECRET_KEY"] = "84RVb%625DA%6nf&2g4$P422EcdM"
app.config["DEBUG"] = True
@app.route("/", methods=["GET", "POST"]) #Flask view function
def index():
    user_input = None
    formatted_input = None
    if request.method == "GET":
        return render_template("main.html")
    if request.method == "POST":
        user_input = request.form["contents"]
        formatted_input = convert(user_input, request.form["time-zone"])
    if formatted_input is not None:
        result = difference_calculator(formatted_input)
        entered_date = format_input(formatted_input)
        result = format_results(result,"{d} days, {h} hours, {m} minutes and {s} seconds passed")
        return render_template("main.html",entered_date = entered_date, result = result, result_zone = "Results shown for " + request.form["time-zone"] +" time zone.")

    else:
        result = f"The following input: {user_input} is not valid, please check"
        return render_template("main.html", error = result)