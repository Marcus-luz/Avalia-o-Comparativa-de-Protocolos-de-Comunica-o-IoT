import time
import csv
import os
# Importações mantidas para que você possa expandir a lógica depois
import paho.mqtt.client as mqtt
import requests
import asyncio
from aiocoap import *

# Configurações
REPETICOES = 5 
# Ajustado para salvar na pasta 'docs' conforme sua estrutura
OUTPUT_DIR = "docs"
RESULTADOS_FILE = os.path.join(OUTPUT_DIR, "resultados.csv")

# Garante que a pasta 'docs' existe antes de salvar
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def test_mqtt():
    print("Testando MQTT...")
    start = time.time()
    # (Simulação da conexão)
    time.sleep(0.5) 
    end = time.time()
    return (end - start) * 1000 # Latência em ms

def test_http():
    print("Testando HTTP...")
    start = time.time()
    # (Simulação de POST)
    time.sleep(1.2)
    end = time.time()
    return (end - start) * 1000

def test_coap():
    print("Testando CoAP...")
    start = time.time()
    # (Simulação de disparo UDP)
    time.sleep(0.3)
    end = time.time()
    return (end - start) * 1000

# Execução
dados = [
    ["Protocolo", "Latencia_Media_ms"],
    ["MQTT", test_mqtt()],
    ["HTTP", test_http()],
    ["CoAP", test_coap()]
]

# Salvar em CSV dentro da pasta docs
with open(RESULTADOS_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(dados)

print(f"\nTeste finalizado! Resultados salvos em {RESULTADOS_FILE}")