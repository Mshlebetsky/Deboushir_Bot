import json

with open("app/templates/text.json", 'r', encoding='utf-8') as f:
    text = json.load(f)
welcome_text = text['welcome_text']