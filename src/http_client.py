import time
import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Cliente HTTP IoT")
    parser.add_argument("--url", type=str, default="http://httpbin.org/post", help="URL do endpoint HTTP")
    parser.add_argument("--repeticoes", type=int, default=30, help="Número de mensagens a enviar")
    parser.add_argument("--intervalo", type=int, default=10, help="Intervalo (segundos) entre envios")
    args = parser.parse_args()

    PAYLOAD = {"coordenadas": "-29.7, -55.8"}

    print(f"Iniciando envio via HTTP (POST) para {args.url}...")
    print(f"Configuração: {args.repeticoes} envios com intervalo de {args.intervalo}s")
    
    for i in range(args.repeticoes):
        try:
            requests.post(args.url, json=PAYLOAD)
            print(f"Envio {i+1}/{args.repeticoes}: Coordenadas enviadas via HTTP (POST).")
            time.sleep(args.intervalo)
        except KeyboardInterrupt:
            print("\nEncerrando cliente HTTP pelo utilizador.")
            break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()