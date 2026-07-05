import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_persona(data):

    prompt = f"""
You are a professional marketing strategist.

Create a detailed customer persona.

Customer Details

Name: {data['name']}
Age: {data['age']}
Occupation: {data['occupation']}
Income: {data['income']}
Interests: {data['interests']}
Goals: {data['goals']}
Challenges: {data['challenges']}

Return ONLY HTML.

Use exactly this structure.

<h2>Persona Name</h2>

<h3>Background</h3>
<p>...</p>

<h3>Personality</h3>
<ul>
<li>...</li>
</ul>

<h3>Pain Points</h3>
<ul>
<li>...</li>
</ul>

<h3>Buying Behaviour</h3>
<p>...</p>

<h3>Preferred Platforms</h3>
<ul>
<li>...</li>
</ul>

<h3>Marketing Strategy</h3>
<ul>
<li>...</li>
</ul>

<h3>Product Recommendations</h3>
<ul>
<li>...</li>
</ul>

Return ONLY valid HTML.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text