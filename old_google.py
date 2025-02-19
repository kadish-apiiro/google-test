import google.generativeai as genai

def execute():
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(
        'Tell me a story in 300 words'
    )
    print(response.text)
