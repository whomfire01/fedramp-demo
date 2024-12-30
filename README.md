# FedRAMP OSCAL Demo for IBM Compliance Position

I created this project to showcase my skills in automating FedRAMP compliance using OSCAL, JSON, YAML, and Python. At IBM, keeping up with compliance documentation will be a major challenge, so I built tools to automate Security Plans, POA&Ms, and compliance reports, streamlining what could otherwise be time-consuming manual processes.
 
By automating these processes based on vulnerability scans, I'm considering how to make compliance both efficient and accurate. The tools I've developed can automatically update documentation when new vulnerabilities are detected, ensuring everything stays current without manual intervention. My hope is that this work aligns with IBM's cloud security goals and demonstrates my ability to handle complex compliance requirements in large-scale environments. I'm particularly focused on making these tools scalable, so they can adapt as compliance needs grow and change.

## Files

- `oscal/oscal-controls.json`: Multiple OSCAL controls in JSON format.
- `config/config-compliance-settings.yaml`: Configuration file for defining compliance-related settings, such as required controls, reporting frequency, and audit logging.
- `config/config-secure-keys.yaml`: Configuration file for defining secure key management settings, including encryption algorithms, key rotation, and storage locations.
- `scripts/generate_compliance_oscal.py`: Python script that generates OSCAL JSON files, creates a compliance report, and updates the POA&M based on vulnerability scan results.
- `output/`: Contains generated files from the Python script, including OSCAL data, compliance reports, and POA&M updates.
   - `output/compliance_report.txt`: Compliance summary report detailing the status of key controls.
   - `output/generated_compliance_oscal.json`: OSCAL-compliant JSON file representing security controls.
   - `output/updated_poam.json`: Updated POA&M file reflecting remediation status based on vulnerability scan results.
   - `output/vulnerability-scan-results/scan_results.json`: Example vulnerability scan results in JSON format. Results are used by the script to update the POA&M with remediation status and milestones.

## Features
- **OSCAL Generation**: The script automatically generates an OSCAL-compliant JSON file representing security controls.
- **Compliance Report**: A simple compliance report is generated in text format, summarizing the status of key security controls.
- **POA&M Update**: The script integrates vulnerability scan results (from `scan_results.json`) to automatically update the POA&M file (`updated_poam.json`), tracking remediation progress for identified vulnerabilities.

## How to Use
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fedramp-oscal-demo.git
   cd fedramp-oscal-demo
   ```

2. **Run the `generate_compliance_oscal.py` script** to:
   - Generate an OSCAL compliance JSON file (`generated_compliance_oscal.json`).
   - Generate a simple compliance summary report (`compliance_report.txt`).
   - Update the POA&M (`updated_poam.json`) based on vulnerability scan results from `scan_results.json`.

   ```bash
   python scripts/generate_compliance_oscal.py
   ```

3. **Review the generated files**:
   - `generated_compliance_oscal.json`: Contains OSCAL JSON data for compliance controls.
   - `compliance_report.txt`: A summary report detailing the status of controls.
   - `updated_poam.json`: A POA&M file with updates based on vulnerability scan results.

## Directory Structure

- `config/`: Contains configuration files for key management and compliance settings.
- `oscal/`: Contains OSCAL JSON files demonstrating security controls and compliance examples.
- `output/`: Contains generated output from Python script.
- `scripts/`: Contains Python scripts for generating OSCAL files, compliance reports, and updating the POA&M.
- `vulnerability-scan-results/`: Contains sample vulnerability scan results used to update the POA&M.

## Dependencies

This project uses Python for automation. The following Python libraries are required:
- `json` (standard library, no installation needed)
- `yaml` (installable via `pip install pyyaml`)

To run the script, you need to have Python installed on your machine.
