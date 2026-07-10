import time
import requests
import argparse
import psutil
import os
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="Cliente HTTP IoT")
    parser.add_argument("--url", type=str, default="http://httpbin.org/post")
    parser.add_argument("--repeticoes", type=int, default=30)
    parser.add_argument("--intervalo", type=int, default=10)
    args = parser.parse_args()

    processo = psutil.Process(os.getpid())
    processo.cpu_percent()

    latencias = []
    sucessos = 0
    PAYLOAD = {"coordenadas": "-29.7, -55.8"}

    print(f"HTTP: Enviando {args.repeticoes} mensagens...", file=sys.stderr)
    for i in range(args.repeticoes):
        inicio = time.perf_counter()
        try:
            resposta = requests.post(args.url, json=PAYLOAD, timeout=5)
            fim = time.perf_counter()
            if resposta.status_code == 200:
                sucessos += 1
                latencias.append((fim - inicio) * 1000)
            else:
                print(f"Aviso HTTP: Status Code {resposta.status_code}", file=sys.stderr)
        except Exception as e:
            print(f"Erro HTTP na requisição {i+1}: {e}", file=sys.stderr)
        
        time.sleep(args.intervalo)

    cpu_media = processo.cpu_percent()
    memoria_mb = processo.memory_info().rss / (1024 * 1024)
    latencia_media = sum(latencias) / len(latencias) if latencias else 0
    taxa_sucesso = (sucessos / args.repeticoes) * 100

    resultado = {
        "protocolo": "HTTP",
        "cpu": round(cpu_media, 2),
        "memoria": round(memoria_mb, 2),
        "latencia": round(latencia_media, 2),
        "sucesso": round(taxa_sucesso, 1)
    }
    
    print(json.dumps(resultado))

if __name__ == "__main__":
    main()