from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    grades = hackbright.get_grades_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/new-student")
def new_student_form():
    """Get info for new student."""

    return render_template("student_creation.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')
    hackbright.make_new_student(first_name, last_name, github)

    html = render_template("new_student_info.html",
                            first_name=first_name,
                            last_name=last_name,
                            github=github)

    return html

@app.route("/project")
def project_info():
    project_title = request.args.get('project')
    project_info = hackbright.get_project_by_title(project_title)
    project_grades = hackbright.get_grades_by_title(project_title)

    html = render_template("project_info.html",
                            project_info=project_info,
                            project_grades=project_grades)
    return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
