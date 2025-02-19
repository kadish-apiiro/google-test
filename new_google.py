from google import genai

def execute():
    client = genai.Client(api_key='GEMINI_API_KEY')
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents='Why is the sky blue?'
    )
