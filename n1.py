import google.generativeai as genai

genai.configure(api_key="AIzaSyDuSjvMlN7CMuqd8w6pr0-ObWiCVfssrKA")

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)