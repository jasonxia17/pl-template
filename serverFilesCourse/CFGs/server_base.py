import chevron

def generate(data):
    data["params"]["names_for_user"] = []

    data["params"]["names_from_user"] = [
        {"name": "cfg", "type": "nltk.grammar.CFG"},
    ]

    with open(data["options"]["server_files_course_path"] + "/CFGs/question_base.html") as f:
        data["params"]["html"] = chevron.render(f, data).strip()
