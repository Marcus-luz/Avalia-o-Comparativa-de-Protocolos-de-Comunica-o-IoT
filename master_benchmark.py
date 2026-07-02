import os
import subprocess
import sys

OUTPUT_DIR = "docs"
RESULTADOS_FILE = os.path.join(OUTPUT_DIR, "resultados.csv")

def executar_benchmark():
    print("=== Iniciando Benchmark Real dos Protocolos ===")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    # 1. Preparar o ficheiro CSV limpando dados antigos e adicionando o cabeçalho
    with open(RESULTADOS_FILE, "w", encoding="utf-8") as f:
        f.write("Protocolo,CPU (%),Memória (MB),Latência (ms),Sucesso (%)\n")
        
    # 2. Configuração rápida para o teste (podes alterar depois)
    repeticoes = 10
    intervalo = 1
    
    protocolos = [
        ("MQTT", "src/mqtt_client.py"),
        ("HTTP", "src/http_client.py"),
        ("CoAP", "src/coap_client.py")
    ]
    
    # 3. Executar cada cliente. Eles mesmos vão gravar os resultados no CSV.
    for nome, script in protocolos:
        print(f"\n--- A testar {nome} ---")
        # Usamos o subprocess para correr o script como se fosse no terminal
        subprocess.run([
            sys.executable, script, 
            "--repeticoes", str(repeticoes), 
            "--intervalo", str(intervalo)
        ])
        
    print(f"\n=== Benchmark concluído! Resultados guardados em {RESULTADOS_FILE} ===")

if __name__ == "__main__":
    executar_benchmark()