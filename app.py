from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = {}

# Home Page
@app.route("/")
def home():
    return render_template("index.html", students=students)


# Add Student
@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"]
    marks = int(request.form["marks"])

    students[name] = marks

    return redirect("/")


# Check Result
@app.route("/result", methods=["POST"])
def check_result():

    name = request.form["check_name"]

    if name in students:

        marks = students[name]

        if marks >= 50:
            result = f"{name} is PASS"
        else:
            result = f"{name} is FAIL"

    else:
        result = "Student Not Found"

    return render_template(
        "index.html",
        students=students,
        result=result
    )


# Delete Student
@app.route("/delete", methods=["POST"])
def delete_student():

    name = request.form["delete_name"]

    if name in students:
        del students[name]

    return redirect("/")


# Update Student Marks
@app.route("/update", methods=["POST"])
def update_student():

    name = request.form["update_name"]
    marks = int(request.form["update_marks"])

    if name in students:
        students[name] = marks

    return redirect("/")


# Exit / Run App
if __name__ == "__main__":
    app.run(debug=True)