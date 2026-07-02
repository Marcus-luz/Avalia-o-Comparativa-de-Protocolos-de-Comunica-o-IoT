import asyncio
import argparse
from aiocoap import *

async def run_coap(uri, repeticoes, intervalo):
    protocol = await Context.create_client_context()
    payload = b"Lat:-29.7, Long:-55.8"
    
    print(f"Iniciando envio via CoAP para {uri}...")
    print(f"Configuração: {repeticoes} envios com intervalo de {intervalo}s")
    
    for i in range(repeticoes):
        try:
            request = Message(code=PUT, payload=payload, uri=uri)
            await protocol.request(request).response
            print(f"Envio {i+1}/{repeticoes}: Coordenadas enviadas via CoAP.")
            await asyncio.sleep(intervalo)
        except asyncio.CancelledError:
            break
        except Exception as e:
            print(f"Erro no envio {i+1}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Cliente CoAP IoT")
    parser.add_argument("--uri", type=str, default="coap://californium.eclipseprojects.io:5683/test", help="URI do servidor CoAP")
    parser.add_argument("--repeticoes", type=int, default=30, help="Número de mensagens a enviar")
    parser.add_argument("--intervalo", type=int, default=10, help="Intervalo (segundos) entre envios")
    args = parser.parse_args()

    try:
        asyncio.run(run_coap(args.uri, args.repeticoes, args.intervalo))
    except KeyboardInterrupt:
        print("\nEncerrando cliente CoAP pelo utilizador.")

if __name__ == "__main__":
    main()