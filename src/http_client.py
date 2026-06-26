import time
import requests

# HTTP utiliza TCP, sendo mais pesado para dispositivos restritos
URL = "http://httpbin.org/post"
PAYLOAD = {"coordenadas": "-29.7, -55.8"}

print("Iniciando envio via HTTP...")
for i in range(30):
    try:
        requests.post(URL, json=PAYLOAD)
        print(f"Envio {i+1}: Coordenadas enviadas via HTTP (POST).")
        time.sleep(10)
    except Exception as e:
        print(f"Erro: {e}")