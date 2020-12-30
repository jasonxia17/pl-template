import chevron

def render(element_html, data):
    hints = data["params"].get("hints", [])
    with open('hidden-hints.mustache', 'r') as f:
        return chevron.render(f, {
            "hints": [{"hint": hint, "index": i + 1} for i, hint in enumerate(hints)]
        }).strip()
