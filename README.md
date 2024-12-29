# FedRAMP OSCAL Demo for IBM Compliance Position

This project is intended to demonstrate Steve Moore's familiarity with OSCAL, JSON, YAML, and Python in the context of automating FedRAMP compliance processes, including generating System Security Plans (SSPs), Plan of Action & Milestones (POA&Ms), and compliance reports.

## Files

- `oscal/oscal-controls.json`: Multiple OSCAL controls in JSON format.
- `config/config-compliance-settings.yaml`: Configuration file for defining compliance-related settings, such as required controls, reporting frequency, and audit logging.
- `config/config-secure-keys.yaml`: Configuration file for defining secure key management settings, including encryption algorithms, key rotation, and storage locations.
- `scripts/generate_compliance_oscal.py`: Python script that generates OSCAL JSON files, creates a compliance report, and updates the POA&M based on vulnerability scan results.
- `vulnerability-scan-results/scan_results.json`: Example vulnerability scan results in JSON format, used to update the POA&M.

## Features
- **OSCAL Generation**: The script automatically generates an OSCAL-compliant JSON file representing security controls.
- **Compliance Report**: A simple compliance report is generated in text format, summarizing the status of key security controls.
- **POA&M Update**: The script integrates vulnerability scan results (from `scan_results.json`) to automatically update the Plan of Action & Milestones (POA&M) file (`updated_poam.json`), reflecting remediation status based on scan findings.

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

- `oscal/`: Contains OSCAL JSON files demonstrating security controls and compliance examples.
- `config/`: Contains configuration files for key management and compliance settings.
- `scripts/`: Contains Python scripts for generating OSCAL files, compliance reports, and updating the POA&M.
- `vulnerability-scan-results/`: Contains sample vulnerability scan results used to update the POA&M.

## Dependencies

This project uses Python for automation. The following Python libraries are required:
- `json` (standard library, no installation needed)
- `yaml` (installable via `pip install pyyaml`)

To run the script, you need to have Python installed on your machine.
