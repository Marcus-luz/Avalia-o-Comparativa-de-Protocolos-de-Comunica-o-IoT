import time
import argparse
import paho.mqtt.client as mqtt
import psutil
import os

def main():
    parser = argparse.ArgumentParser(description="Cliente MQTT IoT")
    parser.add_argument("--broker", type=str, default="test.mosquitto.org")
    parser.add_argument("--porta", type=int, default=1883)
    parser.add_argument("--repeticoes", type=int, default=30)
    parser.add_argument("--intervalo", type=int, default=10)
    args = parser.parse_args()

    # Inicializar a monitorização do sistema
    processo = psutil.Process(os.getpid())
    processo.cpu_percent() # Primeira chamada para calibrar o psutil

    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.connect(args.broker, args.porta, 60)
    
    latencias = []
    sucessos = 0

    print(f"MQTT: Enviando {args.repeticoes} mensagens...")
    try:
        for i in range(args.repeticoes):
            inicio = time.time()
            resultado = client.publish("entregas/rastreio/1", "Lat:-29.7, Long:-55.8")
            resultado.wait_for_publish() # Esperar que a mensagem seja efetivamente enviada
            fim = time.time()
            
            latencias.append((fim - inicio) * 1000) # Converter para milissegundos
            sucessos += 1
            time.sleep(args.intervalo)
    except Exception as e:
        print(f"Erro MQTT: {e}")
    finally:
        client.disconnect()

    # Calcular médias finais
    cpu_media = processo.cpu_percent()
    memoria_mb = processo.memory_info().rss / (1024 * 1024)
    latencia_media = sum(latencias) / len(latencias) if latencias else 0
    taxa_sucesso = (sucessos / args.repeticoes) * 100

    # Gravar no CSV
    with open("docs/resultados.csv", "a", encoding="utf-8") as f:
        f.write(f"MQTT,{cpu_media:.2f},{memoria_mb:.2f},{latencia_media:.2f},{taxa_sucesso:.1f}\n")
    
    print(f"MQTT Finalizado -> Latência: {latencia_media:.2f}ms | Sucesso: {taxa_sucesso}% | CPU: {cpu_media}% | RAM: {memoria_mb:.2f}MB")

if __name__ == "__main__":
    main()