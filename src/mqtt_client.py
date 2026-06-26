import time
import paho.mqtt.client as mqtt

# O MQTT é ideal para IoT por ser leve e suportar redes instáveis
BROKER = "test.mosquitto.org"
PORT = 1883
TOPICO = "entregas/rastreio/1"
PAYLOAD = "Lat:-29.7, Long:-55.8" # Exemplo de coordenada de entrega

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("Iniciando envio via MQTT...")
try:
    for i in range(30): # 30 repetições conforme a metodologia
        client.publish(TOPICO, PAYLOAD)
        print(f"Envio {i+1}: Coordenadas publicadas via MQTT.")
        time.sleep(10)
except KeyboardInterrupt:
    client.disconnect()