import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")


animals_info = ""

for animal in animals_data:
    animals_info += '<li class="cards__item">\n'

    if "name" in animal:
        animals_info += f'<div class="card__title">{animal["name"]}</div>\n'

    animals_info += '<div class="card__text">\n'

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        animals_info += f'Diet: {animal["characteristics"]["diet"]}<br>\n'

    if "locations" in animal and animal["locations"]:
        animals_info += f'Location: {animal["locations"][0]}<br>\n'

    if "characteristics" in animal and "type" in animal["characteristics"]:
        animals_info += f'Type: {animal["characteristics"]["type"]}<br>\n'

    animals_info += "</div>\n"
    animals_info += "</li>\n"


# Bestehendes Template lesen
with open("animals_template.html", "r") as file:
    html_content = file.read()


# Platzhalter ersetzen
html_content = html_content.replace(
    "__REPLACE_ANIMALS_INFO__",
    animals_info
)


# Bestehende Datei überschreiben
with open("animals_template.html", "w") as file:
    file.write(html_content)


print("animals_template.html wurde aktualisiert!")