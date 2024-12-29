import json
import yaml
from pprint import pprint  # Import pprint module for better formatting

# Function to load and use configurations
def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Example: Load the security key config
key_config = load_config("../config/config-secure-keys.yaml")

# Neatly print the key configuration
print("\nKey Management Configuration:")
pprint(key_config, indent=4)

# Example: Load the compliance settings config
compliance_config = load_config("../config/config-compliance-settings.yaml")

# Neatly print the compliance configuration
print("\nCompliance Settings Configuration:")
pprint(compliance_config, indent=4)


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
    print("OSCAL JSON file generated.")

def generate_compliance_report():
    # Sample report based on the OSCAL data
    report_data = """
    Compliance Summary Report:
    ---------------------------

    Control AC-2 (Account Management):
    Status: Implemented
    Description: Ensure user accounts are properly managed.

    Control SC-13 (Cryptographic Key Establishment):
    Status: Not Implemented
    Description: Ensure cryptographic keys are properly established.
    """

    # Write the compliance report to a file
    with open("../output/compliance_report.txt", "w") as report_file:
        report_file.write(report_data)

    print("Compliance report generated.")

# Call the report generation function
generate_compliance_report()

def update_poam():
    # Load vulnerability scan results
    with open("../output/vulnerability-scan-results/scan_results.json", "r") as file:
        vulnerabilities = json.load(file)

    # Simulate POA&M update
    poam_updates = []
    for vulnerability in vulnerabilities:
        poam_entry = {
            "control_id": vulnerability["control_id"],
            "vulnerability": vulnerability["vulnerability"],
            "risk_level": vulnerability["risk_level"],
            "status": "Remediation in Progress" if vulnerability["status"] == "Open" else "Resolved",
            "remediation_plan": "Strengthen password policy to require longer and more complex passwords." if vulnerability["control_id"] == "AC-2" else "Define cryptographic key management process and document procedures.",
            "milestones": [
                {
                    "due_date": "2024-06-30",
                    "status": "In Progress"
                },
                {
                    "due_date": "2024-09-30",
                    "status": "Completed"
                }
            ] if vulnerability["control_id"] == "AC-2" else [
                {
                    "due_date": "2024-07-31",
                    "status": "In Progress"
                }
            ]
        }
        poam_updates.append(poam_entry)

    # Write POA&M updates to a new file
    with open("../output/updated_poam.json", "w") as file:
        json.dump({"POA&M": {"controls": poam_updates}}, file, indent=4)

    print("POA&M updated with scan results.")

# Call the function to update POA&M
update_poam()
