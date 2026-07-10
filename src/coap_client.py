import asyncio
import argparse
import psutil
import os
import time
import sys
import json
from aiocoap import *

async def run_coap(uri, repeticoes, intervalo):
    processo = psutil.Process(os.getpid())
    processo.cpu_percent()

    try:
        protocol = await Context.create_client_context()
    except Exception as e:
        print(f"Erro ao criar contexto CoAP: {e}", file=sys.stderr)
        sys.exit(1)
        
    payload = b"Lat:-29.7, Long:-55.8"
    
    latencias = []
    sucessos = 0

    print(f"CoAP: Enviando {repeticoes} mensagens...", file=sys.stderr)
    for i in range(repeticoes):
        inicio = time.perf_counter()
        try:
            request = Message(code=PUT, payload=payload, uri=uri)
            resposta = await protocol.request(request).response
            fim = time.perf_counter()
            
            if resposta.code.is_successful():
                sucessos += 1
                latencias.append((fim - inicio) * 1000)
            else:
                 print(f"Aviso CoAP: Resposta não sucedida com código {resposta.code}", file=sys.stderr)
        except Exception as e:
            print(f"Erro CoAP na requisição {i+1}: {e}", file=sys.stderr)
        
        await asyncio.sleep(intervalo)

    cpu_media = processo.cpu_percent()
    memoria_mb = processo.memory_info().rss / (1024 * 1024)
    latencia_media = sum(latencias) / len(latencias) if latencias else 0
    taxa_sucesso = (sucessos / repeticoes) * 100

    resultado = {
        "protocolo": "CoAP",
        "cpu": round(cpu_media, 2),
        "memoria": round(memoria_mb, 2),
        "latencia": round(latencia_media, 2),
        "sucesso": round(taxa_sucesso, 1)
    }
    
    print(json.dumps(resultado))

def main():
    parser = argparse.ArgumentParser(description="Cliente CoAP IoT")
    parser.add_argument("--uri", type=str, default="coap://californium.eclipseprojects.io:5683/test")
    parser.add_argument("--repeticoes", type=int, default=30)
    parser.add_argument("--intervalo", type=int, default=10)
    args = parser.parse_args()

    asyncio.run(run_coap(args.uri, args.repeticoes, args.intervalo))

if __name__ == "__main__":
    main()