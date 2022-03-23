import requests
import json

sub_domain = input("please enter a sub domain name: ") #Enter Sub Domain name
response = requests.get(f"https://jsonplaceholder.typicode.com/{sub_domain}")
response.headers['content-type']
data = response.json()
parse_dict = {
    "users" : {"name","phone","address"},
    "comments" : {"name","email","body"},
    "albums" : {"title"},
    "photos" : {"title","url"},
    "todos" : {"title"},
}

data = [{key: info[key] for key in info.keys() & parse_dict[sub_domain]} for info in data ]

#writing to file
with open(f"{sub_domain}.txt", "w") as file: 
    file.write(str(data))
    json.dump(data, file)
