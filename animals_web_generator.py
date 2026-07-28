import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")


for animal in animals_data:
    print()

    # Name
    if "name" in animal:
        print(f"Name: {animal['name']}")

    # Diet
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print(f"Diet: {animal['characteristics']['diet']}")

    # Location (erster Eintrag)
    if "locations" in animal and animal["locations"]:
        print(f"Location: {animal['locations'][0]}")

    # Type
    if "characteristics" in animal and "type" in animal["characteristics"]:
        print(f"Type: {animal['characteristics']['type']}")