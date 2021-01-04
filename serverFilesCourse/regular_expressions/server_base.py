import chevron

def generate(data):
    data["params"]["names_for_user"] = []

    data["params"]["names_from_user"] = [
        {"name": "reg_exp", "type": "string"},
    ]

    with open(data["options"]["server_files_course_path"] + "/regular_expressions/question_base.html") as f:
        data["params"]["html"] = chevron.render(f, data).strip()
