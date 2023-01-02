import json


with open('static/language_tags.json', 'r') as file:
    content = json.load(file)

content_items = content.items()
revs_items = map(reversed, content_items)
revs_tags = dict(revs_items)
print(revs_tags.keys())

with open('static/language_tags.json', 'w') as file:
    json.dump(revs_tags, file, indent=4)