import time
import argparse
import paho.mqtt.client as mqtt
import psutil
import os
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="Cliente MQTT IoT")
    parser.add_argument("--broker", type=str, default="test.mosquitto.org")
    parser.add_argument("--porta", type=int, default=1883)
    parser.add_argument("--repeticoes", type=int, default=30)
    parser.add_argument("--intervalo", type=int, default=10)
    args = parser.parse_args()

    processo = psutil.Process(os.getpid())
    processo.cpu_percent()

    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    try:
        client.connect(args.broker, args.porta, 60)
    except Exception as e:
        print(f"Erro ao conectar ao broker MQTT: {e}", file=sys.stderr)
        sys.exit(1)
    
    latencias = []
    sucessos = 0

    print(f"MQTT: Enviando {args.repeticoes} mensagens...", file=sys.stderr)
    try:
        for i in range(args.repeticoes):
            inicio = time.perf_counter()
            resultado = client.publish("entregas/rastreio/1", "Lat:-29.7, Long:-55.8")
            resultado.wait_for_publish()
            fim = time.perf_counter()
            
            latencias.append((fim - inicio) * 1000)
            sucessos += 1
            time.sleep(args.intervalo)
    except Exception as e:
        print(f"Erro MQTT durante envio na requisição {i+1}: {e}", file=sys.stderr)
    finally:
        client.disconnect()

    cpu_media = processo.cpu_percent()
    memoria_mb = processo.memory_info().rss / (1024 * 1024)
    latencia_media = sum(latencias) / len(latencias) if latencias else 0
    taxa_sucesso = (sucessos / args.repeticoes) * 100

    resultado = {
        "protocolo": "MQTT",
        "cpu": round(cpu_media, 2),
        "memoria": round(memoria_mb, 2),
        "latencia": round(latencia_media, 2),
        "sucesso": round(taxa_sucesso, 1)
    }
    
    # Imprime apenas o JSON no stdout
    print(json.dumps(resultado))

if __name__ == "__main__":
    main()