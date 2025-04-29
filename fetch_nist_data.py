import requests
import json
import pandas as pd

# NIST API URL
NIST_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

# Function to fetch data from NIST
def fetch_nist_data():
    params = {"resultsPerPage": 50}  # Fetch 50 CVEs
    response = requests.get(NIST_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Process data
def process_nist_data(data):
    if not data:
        return None

    cve_items = data.get("vulnerabilities", [])
    processed_data = []

    for item in cve_items:
        cve = item.get("cve", {})
        cve_id = cve.get("id", "N/A")
        description = cve.get("descriptions", [{}])[0].get("value", "No description available")
        severity = cve.get("metrics", {}).get("cvssMetricV2", [{}])[0].get("baseSeverity", "N/A")
        
        processed_data.append({
            "CVE ID": cve_id,
            "Description": description,
            "Severity": severity
        })

    return pd.DataFrame(processed_data)

# Main
if __name__ == "__main__":
    raw_data = fetch_nist_data()
    df = process_nist_data(raw_data)
    
    if df is not None:
        df.to_csv("nist_data.csv", index=False)
        print("NIST data saved to 'nist_data.csv'")
    else:
        print("Failed to fetch or process data")
