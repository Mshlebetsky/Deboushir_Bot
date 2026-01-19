import json

with open("templates/text.json", 'r', encoding='utf-8') as f:
    text = json.load(f)
welcome_text = text['welcome_text']
propose_text = text['propose_text_to_all']
propose_text_to_bonya = text['propose_text_to_bonya']