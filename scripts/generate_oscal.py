import json

def generate_oscal():
    oscal_data = {
        "OSCAL": "1.0",
        "Control": "AC-2",
        "Description": "Account management control for FedRAMP.",
        "Implementation": "Implemented",
    }

    with open("oscal_output.json", "w") as json_file:
        json.dump(oscal_data, json_file, indent=4)

if __name__ == "__main__":
    generate_oscal()
    print("OSCAL JSON file generated!")
