import requests

url = 'https://swapi.co/api/people/' + str(input("Enter a name"))

r = requests.get(url)

response = r.json()

str_data = response.get("name")

print(str_data)
print(r.json())
print("I editted a file")
