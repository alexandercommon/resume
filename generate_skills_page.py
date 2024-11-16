import json

# Load the skills data from the provided file
with open('skills.json', 'r') as file:
    data = json.load(file)

# Updated HTML Template with softer colors
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skills Showcase</title>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{
            font-family: 'Quicksand', sans-serif;
            background-color: #f7eadd;
            color: #5a4f3f;
            margin: 0;
            padding: 0;
        }}
        .container {{
            background: #fdf6ef;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 20px auto;
            max-width: 95%;
            width: 100%;
        }}
        @media (min-width: 768px) {{
            .container {{
                max-width: 750px;
                padding: 30px;
            }}
        }}
        @media (min-width: 1200px) {{
            .container {{
                max-width: 750px;
                padding: 40px;
            }}
        }}
        h1, h2 {{
            color: #4e3c70; /* Softer purple accent color */
        }}
        h1 {{
            font-size: 2.2rem;
            margin-bottom: 10px;
        }}
        h2 {{
            font-size: 1.7rem;
            margin-bottom: 8px;
        }}
        p {{
            margin: 0;
        }}
        .skill-info {{
            font-size: 0.9rem;
            color: #9b7aa0; /* Softer muted purple for better contrast */
            margin-left: 20px; /* Additional indentation for info lines */
            max-width: 75%;
            word-wrap: break-word;
        }}
        .skill-meter {{
            height: 16px;
            background-color: #e6d9c8; /* Softer tan background */
            position: relative;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 4px;
            align-self: flex-start;
        }}
        .skill-meter-bar {{
            height: 100%;
            background-color: #6a4a8c; /* Softer purple accent */
            text-align: right;
            padding-right: 5px;
            color: white;
            font-size: 12px;
            white-space: nowrap;
        }}
        .skill-section {{
            padding-bottom: 15px;
            border-bottom: 1px solid #d4b59e;
            margin-bottom: 20px;
        }}
        .skill-section:last-child {{
            border-bottom: none;
            margin-bottom: 0;
        }}
        .skill-item {{
            width: 70%; /* Fixed width for consistent sizing */
            margin-left: 10px; /* Slight indentation for skill names */
        }}
    </style>
</head>
<body>
    <div class="container mt-5">
        <!-- Header Section -->
        <div class="mb-4">
            <h1>Skill Showcase</h1>
            <h2>Alex Common</h2>
            <p>Here is a list of skills I have performed professionally. References or samples are available upon request.</p>
        </div>

        {content}
    </div>
</body>
</html>
"""

# Generate the content for each category with a modern relaxed design
content = ""
for category in data["categories"]:
    content += f"""
    <div class="skill-section">
        <h2>{category['categoryName']}</h2>
    """
    sorted_skills = sorted(category["skills"], key=lambda x: x["level"], reverse=True)
    for skill in sorted_skills:
        skill_percentage = skill["level"] * 10  # Assuming the level is from 0-10, scale it to percentage
        info_list = "".join([f"<p class='skill-info'>{line}</p>" for line in skill.get('info', [])])
        content += f"""
        <div class="d-flex justify-content-between align-items-start mb-3">
            <div class="skill-item">
                <p>{skill['name']}</p>
                {info_list}
            </div>
            <div class="skill-meter" style="width: 25%;">
                <div class="skill-meter-bar" style="width: {skill_percentage}%;">{skill['level']}/10</div>
            </div>
        </div>
        """
    content += """
    </div>
    """

# Generate the final HTML
html_content = html_template.format(content=content)

# Write the output to an HTML file
with open('skills.html', 'w') as file:
    file.write(html_content)

print("HTML file generated")
