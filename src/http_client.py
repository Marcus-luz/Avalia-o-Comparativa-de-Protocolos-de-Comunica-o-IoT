import time
import requests
import argparse
import psutil
import os

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

    print(f"HTTP: Enviando {args.repeticoes} mensagens...")
    for i in range(args.repeticoes):
        inicio = time.time()
        try:
            resposta = requests.post(args.url, json=PAYLOAD, timeout=5)
            fim = time.time()
            if resposta.status_code == 200:
                sucessos += 1
                latencias.append((fim - inicio) * 1000)
        except Exception:
            pass # Em caso de erro, a latência não é contabilizada e o sucesso falha
        
        time.sleep(args.intervalo)

    cpu_media = processo.cpu_percent()
    memoria_mb = processo.memory_info().rss / (1024 * 1024)
    latencia_media = sum(latencias) / len(latencias) if latencias else 0
    taxa_sucesso = (sucessos / args.repeticoes) * 100

    with open("docs/resultados.csv", "a", encoding="utf-8") as f:
        f.write(f"HTTP,{cpu_media:.2f},{memoria_mb:.2f},{latencia_media:.2f},{taxa_sucesso:.1f}\n")

    print(f"HTTP Finalizado -> Latência: {latencia_media:.2f}ms | Sucesso: {taxa_sucesso}% | CPU: {cpu_media}% | RAM: {memoria_mb:.2f}MB")

if __name__ == "__main__":
    main()