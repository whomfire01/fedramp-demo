import json

def generate_oscal():
    controls = [
        {"ID": "AC-2", "Name": "Account Management", "Implementation": "Implemented"},
        {"ID": "SC-13", "Name": "Cryptographic Key Establishment", "Implementation": "Not Implemented"}
    ]
    
    oscal_data = {
        "OSCAL": "1.0",
        "Controls": controls
    }

    with open("generated_oscal.json", "w") as json_file:
        json.dump(oscal_data, json_file, indent=4)

if __name__ == "__main__":
    generate_oscal()
    print("OSCAL JSON file generated!")
