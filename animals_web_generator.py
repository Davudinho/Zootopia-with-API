import data_fetcher  # nutzt das neues Modul


def serialize_animal(animal_obj):
    """Converts a single animal object into an HTML <li> string."""
    name = animal_obj.get("name", "Unknown")
    locations = animal_obj.get("locations", [])
    characteristics = animal_obj.get("characteristics", {})

    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")
    location = locations[0] if locations else "Unknown"

    return f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <p class="card__text">
            <strong>Diet:</strong> {diet}<br/>
            <strong>Location:</strong> {location}<br/>
            <strong>Type:</strong> {animal_type}<br/>
        </p>
    </li>
    """


def generate_animals_html(data):
    """Generates the full HTML list string."""
    return "".join(serialize_animal(a) for a in data)


def show_no_animals(user_input):
    return f'<h2>The animal "{user_input}" doesn’t exist.</h2>'


def main():
    animal_name = input("Please enter an animal: ")

    # 🔹 fetch data from the API using data_fetcher
    animals_data = data_fetcher.fetch_data(animal_name)

    # 🔹 read HTML template
    with open("animals_template.html", "r", encoding="utf-8") as f:
        html_template = f.read()

    # 🔹 decide what to insert
    if not animals_data:
        animals_html = show_no_animals(animal_name)
    else:
        animals_html = generate_animals_html(animals_data)

    # 🔹 replace placeholder
    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # 🔹 save output
    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    print("✅ File 'animals.html' has been generated successfully!")


if __name__ == "__main__":
    main()
