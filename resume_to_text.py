import json

def json_to_plain_text(json_data):
    basics = json_data.get("basics", {})
    work = json_data.get("work", [])
    volunteer = json_data.get("volunteer", [])
    education = json_data.get("education", [])
    awards = json_data.get("awards", [])
    skills = json_data.get("skills", [])
    interests = json_data.get("interests", [])
    
    output = []

    # Basics
    output.append(f"Name: {basics.get('name', 'N/A')}")
    output.append(f"Label: {basics.get('label', 'N/A')}")
    output.append(f"Image: {basics.get('image', 'N/A')}")
    output.append(f"Email: {basics.get('email', 'N/A')}")
    output.append(f"Phone: {basics.get('phone', 'N/A')}")
    location = basics.get("location", {})
    output.append(f"Location: {location.get('city', '')}, {location.get('region', '')}, {location.get('postalCode', '')}, {location.get('countryCode', '')}")
    output.append(f"Summary: {basics.get('summary', 'N/A')}")
    output.append("\n")

    # Work Experience
    output.append("Work Experience:")
    for job in work:
        output.append(f"**{job.get('name', 'N/A')}**")
        output.append(f"Position: {job.get('position', 'N/A')}")
        output.append(f"Duration: {job.get('startDate', 'N/A')} - {job.get('endDate', 'N/A')}")
        output.append(f"Summary: {job.get('summary', 'N/A')}")
        output.append("Highlights:")
        for highlight in job.get('highlights', []):
            output.append(f"- {highlight}")
        output.append("\n")

    # Volunteer
    output.append("Volunteer Experience:")
    for vol in volunteer:
        output.append(f"**{vol.get('organization', 'N/A')}**")
        output.append(f"Position: {vol.get('position', 'N/A')}")
        output.append(f"Duration: {vol.get('startDate', 'N/A')} - {vol.get('endDate', 'N/A')}")
        output.append(f"Summary: {vol.get('summary', 'N/A')}")
        output.append("Highlights:")
        for highlight in vol.get('highlights', []):
            output.append(f"- {highlight}")
        output.append("\n")

    # Education
    output.append("Education:")
    for edu in education:
        output.append(f"Institution: {edu.get('institution', 'N/A')}")
        output.append(f"Area: {edu.get('area', 'N/A')}")
        output.append(f"Degree: {edu.get('studyType', 'N/A')}")
        output.append(f"Duration: {edu.get('startDate', 'N/A')} - {edu.get('endDate', 'N/A')}")
        output.append("\n")

    # Awards
    output.append("Awards:")
    for award in awards:
        output.append(f"{award.get('title', 'N/A')} - {award.get('awarder', 'N/A')} ({award.get('date', 'N/A')})")
        output.append("\n")

    # Skills
    output.append("Skills:")
    for skill in skills:
        output.append(f"{skill.get('name', 'N/A')}: {', '.join(skill.get('keywords', []))}")
        output.append("\n")

    # Interests
    output.append("Interests:")
    for interest in interests:
        output.append(f"{interest.get('name', 'N/A')}: {', '.join(interest.get('keywords', []))}")
        output.append("\n")

    return "\n".join(output)

# Load JSON from a file
def load_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Example usage
file_path = 'data.json'  # Replace with your JSON file path
json_data = load_json_file(file_path)
plain_text_output = json_to_plain_text(json_data)

# Output the result
print(plain_text_output)
