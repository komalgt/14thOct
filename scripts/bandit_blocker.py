import json
import sys

with open('bandit_report.json') as f:
    report = json.load(f)

critical_findings = [
    issue for issue in report.get('results', [])
    if issue.get('issue_severity', '').upper() == 'HIGH'
]

if critical_findings:
    print(f"ERROR: Found {len(critical_findings)} HIGH severity vulnerabilities.")
    for i in critical_findings:
        print(f"- {i.get('filename')}: {i.get('issue_text')}")
    sys.exit(2)  # Non-zero exit code blocks the merge
else:
    print("No HIGH severity vulnerabilities found.")
