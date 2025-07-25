import json
from jinja2 import Template
from pathlib import Path

def load_entries(file_path):
    with open(file_path) as f:
        return json.load(f)

def render_card(entry, template_path="templates/artifact_card_template.md"):
    with open(template_path) as f:
        tmpl = Template(f.read())
    return tmpl.render(**entry)

def export_cards(entries, out_dir="exported_cards/"):
    Path(out_dir).mkdir(exist_ok=True)
    for name, data in entries.items():
        card_text = render_card(data)
        out_file = Path(out_dir) / f"{name.replace(' ', '_')}.md"
        with open(out_file, 'w') as f:
            f.write(card_text)
        print(f" Exported: {out_file.name}")

if __name__ == "__main__":
    print(" Field Manual Exporter")
    input_path = input(" Path to JSON archive: ").strip()
    export_cards(load_entries(input_path))
