# FedRAMP Demo for IBM Compliance Position

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

3. **Review the generated files in the `output` folder**:
   - `compliance_report.txt`: A summary report detailing the status of controls.
   - `generated_compliance_oscal.json`: Contains OSCAL JSON data for compliance controls.
   - `updated_poam.json`: A POA&M file with updates based on vulnerability scan results.
   - `vulnerability-scan-results/scan_results.json`: Results from each vulnerability scan.

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

To run the script, you'll need Python installed on your machine.

## Instructions for Testing

After cloning this repository, you can test the functionality of the Python scripts and validate the generated output files to ensure everything is working correctly.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fedramp-oscal-demo.git
   cd fedramp-oscal-demo
2. **Install Dependencies**:
   This project uses **Python** and the **PyYAML** library to handle YAML configuration files. To install dependencies, run:
   ```bash
   pip install -r requirements.txt

> **Note**: If you don't have a `requirements.txt` file yet, you can manually install `pyyaml` via `pip install pyyaml`.

3. **Run the Python Script**:
   The main script **`generate_compliance_oscal.py`** generates the OSCAL JSON file, the compliance report, and updates the POA&M based on vulnerability scan results. To execute the script:
   ```bash
   python scripts/generate_compliance_oscal.py

4. **Verify the Generated Files**:
   After running the script, the following output files will be generated in the **`output/`** directory:
   - **`generated_compliance_oscal.json`**: Verify that this file contains OSCAL-compliant JSON data for the security controls.
   - **`compliance_report.txt`**: Review the generated compliance report to ensure it summarizes the status of the key security controls.
   - **`updated_poam.json`**: Check that this file has been correctly updated based on the example vulnerability scan results, with appropriate remediation status and milestones.

5. **Test POA&M Updates**:
   To test that the POA&M updates are working correctly:
   - Open the **`updated_poam.json`** file and verify that the **`control_id`**, **`vulnerability`**, **`risk_level`**, and **`remediation_plan`** fields are properly updated based on the scan results in **`scan_results.json`**.
   - The POA&M should also reflect any progress made on remediation with milestones (e.g., **“In Progress”** or **“Completed”**).
   
   If you're using different **scan results** (e.g., for a different vulnerability), you can replace the sample **`scan_results.json`** file in the **`vulnerability-scan-results/`** folder and rerun the script to see how the POA&M is updated.

6. **Validate OSCAL Compliance**:
   To validate that the **OSCAL JSON** is correctly formatted and meets **FedRAMP** or general **OSCAL** standards, you can use tools like the [OSCAL Validator](https://csrc.nist.gov/projects/risk-management) or validate manually by checking the structure of the generated JSON.


