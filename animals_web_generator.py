import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


# JSON-Datei laden
animals_data = load_data("animals_data.json")


# HTML-String für die Tiere erzeugen
animals_info = ""

for animal in animals_data:
    animals_info += '<li class="cards__item">\n'

    # Name
    if "name" in animal:
        animals_info += f'<div class="card__title">{animal["name"]}</div>\n'

    # Textbereich
    animals_info += '<p class="card__text">\n'

    # Diet
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        animals_info += (
            f"<strong>Diet:</strong> "
            f"{animal['characteristics']['diet']}<br/>\n"
        )

    # Location
    if "locations" in animal and animal["locations"]:
        animals_info += (
            f"<strong>Location:</strong> "
            f"{animal['locations'][0]}<br/>\n"
        )

    # Type
    if "characteristics" in animal and "type" in animal["characteristics"]:
        animals_info += (
            f"<strong>Type:</strong> "
            f"{animal['characteristics']['type']}<br/>\n"
        )

    animals_info += "</p>\n"
    animals_info += "</li>\n"


# HTML Template lesen
with open("animals_template.html", "r") as file:
    html_content = file.read()


# Platzhalter ersetzen
html_content = html_content.replace(
    "__REPLACE_ANIMALS_INFO__",
    animals_info
)


# Vorhandene HTML-Datei aktualisieren
with open("animals_template.html", "w") as file:
    file.write(html_content)


print("animals_template.html wurde erfolgreich aktualisiert!")