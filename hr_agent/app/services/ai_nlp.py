def generate_report(data):
    return {
        "status": "success",
        "content": f"Auto-generated report for patient ID: {data.get('patient_id')}"
    }


def validate_report(content):
    if "error" in content.lower():
        return False
    return True


def summarize_report(content):
    return content[:100] + "..."