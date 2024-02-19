import json

# пайтън обект
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# преобразува се в json
y = json.dumps(x)

# резултат json стринг
print(y)