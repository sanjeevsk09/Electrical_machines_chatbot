import openai


openai.api_key = 'your-api-key'

def get_openai_response(prompt, model="gpt-3.5-turbo", max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"


custom_prompt = "Write a short story about a robot who learns to love."
response = get_openai_response(custom_prompt)
print("OpenAI Response:", response)
