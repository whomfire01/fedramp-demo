import json

# Function to generate an OSCAL-compliant JSON file
def generate_oscal():
    oscal_data = {
        "OSCAL": "1.0",
        "Controls": [
            {
                "ID": "AC-2",
                "Name": "Account Management",
                "Description": "Ensure user accounts are properly managed.",
                "Implementation": "Implemented"
            },
            {
                "ID": "SC-13",
                "Name": "Cryptographic Key Establishment",
                "Description": "Ensure cryptographic keys are properly established.",
                "Implementation": "Not Implemented"
            }
        ]
    }

    # Write the OSCAL JSON data to a file
    with open("generated_compliance_oscal.json", "w") as json_file:
        json.dump(oscal_data, json_file, indent=4)

# Run the function to generate the OSCAL file
if __name__ == "__main__":
    generate_oscal()
    print("OSCAL JSON file generated!")
