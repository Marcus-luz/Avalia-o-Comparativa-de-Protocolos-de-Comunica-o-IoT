import time
import argparse
import paho.mqtt.client as mqtt

def main():
    # Configuração dos argumentos da linha de comandos
    parser = argparse.ArgumentParser(description="Cliente MQTT IoT")
    parser.add_argument("--broker", type=str, default="test.mosquitto.org", help="Endereço do Broker MQTT")
    parser.add_argument("--porta", type=int, default=1883, help="Porta do Broker MQTT")
    parser.add_argument("--repeticoes", type=int, default=30, help="Número de mensagens a enviar")
    parser.add_argument("--intervalo", type=int, default=10, help="Intervalo (segundos) entre envios")
    args = parser.parse_args()

    TOPICO = "entregas/rastreio/1"
    PAYLOAD = "Lat:-29.7, Long:-55.8" # Exemplo de coordenada de entrega

    client = mqtt.Client()
    client.connect(args.broker, args.porta, 60)

    print(f"Iniciando envio via MQTT para {args.broker}:{args.porta}...")
    print(f"Configuração: {args.repeticoes} envios com intervalo de {args.intervalo}s")
    
    try:
        for i in range(args.repeticoes):
            client.publish(TOPICO, PAYLOAD)
            print(f"Envio {i+1}/{args.repeticoes}: Coordenadas publicadas via MQTT.")
            time.sleep(args.intervalo)
    except KeyboardInterrupt:
        print("\nEncerrando cliente MQTT pelo utilizador.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()