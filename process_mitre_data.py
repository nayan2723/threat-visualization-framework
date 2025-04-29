import json

# Load MITRE data
with open("mitre_data.json", "r", encoding="utf-8") as file:
    mitre_data = json.load(file)

# Extract techniques
techniques = [
    {
        "id": obj["external_references"][0]["external_id"],
        "name": obj["name"],
        "description": obj.get("description", "No description available."),
    }
    for obj in mitre_data["objects"]
    if obj["type"] == "attack-pattern"
]

# Save processed techniques
with open("processed_mitre_data.json", "w", encoding="utf-8") as file:
    json.dump(techniques, file, indent=2)

print(f"Processed {len(techniques)} techniques and saved to 'processed_mitre_data.json'.")
