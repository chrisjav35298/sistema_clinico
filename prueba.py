import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/users")

print("TIPO DE respuesta")
print(type(respuesta))

print("\nTIPO DE respuesta.text")
print(type(respuesta.text))

usuarios = respuesta.json() # Convertir la respuesta en formato JSON a un objeto de Python

print("\nTIPO DE usuarios")
print(type(usuarios))

print("\nTIPO DEL PRIMER ELEMENTO")
print(type(usuarios[0]))

print("valores en crudo de la respuesta")
print(respuesta.text)