import asyncio
from aiocoap import *

# CoAP usa UDP para reduzir a latência em redes de baixa largura de banda
URI = "coap://californium.eclipseprojects.io:5683/test"

async def main():
    protocol = await Context.create_client_context()
    payload = b"Lat:-29.7, Long:-55.8"
    
    print("Iniciando envio via CoAP...")
    for i in range(30):
        request = Message(code=PUT, payload=payload, uri=URI)
        await protocol.request(request).response
        print(f"Envio {i+1}: Coordenadas enviadas via CoAP.")
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())