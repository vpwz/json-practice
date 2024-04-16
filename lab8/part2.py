import json

input_file = 'data/schacon.repos.json'
output_file = 'chacon.csv'

with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

with open(output_file, 'w', encoding='utf-8') as file:
    for repo in data[:5]: 
        name = repo['name']
        html_url = repo['html_url']
        updated_at = repo['updated_at']
        visibility = repo['visibility']
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        file.write(line)
