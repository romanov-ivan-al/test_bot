import json

arr = []

with open ("../materials/vocabulary.txt", encoding="utf-8") as text:
    for word in text:
        n = word.lower().split('\n')[0]
        if n != "":
            arr.append(n)

print(arr)

with open("../materials/cenz.json", "w", encoding="utf-8") as file:
    json.dump(arr, file)
