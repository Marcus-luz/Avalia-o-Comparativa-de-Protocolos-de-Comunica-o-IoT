import asyncio
import argparse
import psutil
import os
import time
from aiocoap import *

async def run_coap(uri, repeticoes, intervalo):
    processo = psutil.Process(os.getpid())
    processo.cpu_percent()

    protocol = await Context.create_client_context()
    payload = b"Lat:-29.7, Long:-55.8"
    
    latencias = []
    sucessos = 0

    print(f"CoAP: Enviando {repeticoes} mensagens...")
    for i in range(repeticoes):
        inicio = time.time()
        try:
            request = Message(code=PUT, payload=payload, uri=uri)
            await protocol.request(request).response
            fim = time.time()
            
            sucessos += 1
            latencias.append((fim - inicio) * 1000)
        except Exception:
            pass
        
        await asyncio.sleep(intervalo)

    cpu_media = processo.cpu_percent()
    memoria_mb = processo.memory_info().rss / (1024 * 1024)
    latencia_media = sum(latencias) / len(latencias) if latencias else 0
    taxa_sucesso = (sucessos / repeticoes) * 100

    with open("docs/resultados.csv", "a", encoding="utf-8") as f:
        f.write(f"CoAP,{cpu_media:.2f},{memoria_mb:.2f},{latencia_media:.2f},{taxa_sucesso:.1f}\n")

    print(f"CoAP Finalizado -> Latência: {latencia_media:.2f}ms | Sucesso: {taxa_sucesso}% | CPU: {cpu_media}% | RAM: {memoria_mb:.2f}MB")

def main():
    parser = argparse.ArgumentParser(description="Cliente CoAP IoT")
    parser.add_argument("--uri", type=str, default="coap://californium.eclipseprojects.io:5683/test")
    parser.add_argument("--repeticoes", type=int, default=30)
    parser.add_argument("--intervalo", type=int, default=10)
    args = parser.parse_args()

    asyncio.run(run_coap(args.uri, args.repeticoes, args.intervalo))

if __name__ == "__main__":
    main()