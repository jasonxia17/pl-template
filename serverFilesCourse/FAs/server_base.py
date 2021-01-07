import chevron

def generate(data):
    data["params"]["names_for_user"] = []

    data["params"]["names_from_user"] = [
        {"name": "fa", "type": "either a DFA or NFA"},
    ]

    with open(data["options"]["server_files_course_path"] + "/FAs/question_base.html") as f:
        data["params"]["html"] = chevron.render(f, data).strip()
