import os
import openai
from django.shortcuts import render, redirect
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def home(request):
    return render(request, 'home/home.html')


def display_output(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        return render(request, 'home/display_output.html', {'url': url})


def translate_to_french(request):
    if request.method == "POST":
        input_text = request.POST.get("input_text")
        response = openai.Completion.create(
            engine="text-davinci-002",  # Use the appropriate engine for translation
            prompt=f"Translate the following English text to French: '{input_text}'",
            max_tokens=50,
            temperature=0.7,  # Adjust temperature as needed for translation quality
        )
        result = response.choices[0].text
        return render(request, "translate.html", {"result": result})

    return render(request, "translate.html")
