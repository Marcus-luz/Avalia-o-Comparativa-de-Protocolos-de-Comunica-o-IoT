import os
import subprocess
import sys
import json

OUTPUT_DIR = "docs"
RESULTADOS_FILE = os.path.join(OUTPUT_DIR, "resultados.csv")

def executar_benchmark():
    print("=== Iniciando Benchmark Real dos Protocolos ===")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    # Prepara o CSV
    with open(RESULTADOS_FILE, "w", encoding="utf-8") as f:
        f.write("Protocolo,CPU (%),Memória (MB),Latência (ms),Sucesso (%)\n")
        
    repeticoes = 10
    intervalo = 1
    
    protocolos = [
        ("MQTT", "src/mqtt_client.py"),
        ("HTTP", "src/http_client.py"),
        ("CoAP", "src/coap_client.py")
    ]
    
    for nome, script in protocolos:
        print(f"\n--- A testar {nome} ---")
        try:
            # Captura as saídas do subprocesso
            resultado = subprocess.run(
                [sys.executable, script, "--repeticoes", str(repeticoes), "--intervalo", str(intervalo)],
                capture_output=True, text=True, check=True
            )
            
            # Imprime os logs progressivos gerados no stderr pelo cliente
            if resultado.stderr:
                print(resultado.stderr.strip())
                
            # Extrai os dados em formato JSON vindos do stdout
            dados = json.loads(resultado.stdout.strip())
            
            # Grava o resultado no CSV (Apenas o Master faz isso agora)
            with open(RESULTADOS_FILE, "a", encoding="utf-8") as f:
                f.write(f"{dados['protocolo']},{dados['cpu']},{dados['memoria']},{dados['latencia']},{dados['sucesso']}\n")
                
            print(f"✅ {nome} Registado -> Latência: {dados['latencia']}ms | Sucesso: {dados['sucesso']}% | CPU: {dados['cpu']}% | RAM: {dados['memoria']}MB")

        except subprocess.CalledProcessError as e:
            print(f"❌ Erro crítico ao executar {nome}. Código: {e.returncode}")
            print(f"Detalhes:\n{e.stderr}")
        except json.JSONDecodeError:
            print(f"❌ Erro ao processar os dados do {nome}. A saída foi:\n{resultado.stdout}")

    print(f"\n=== Benchmark concluído! Resultados guardados em {RESULTADOS_FILE} ===")

if __name__ == "__main__":
    executar_benchmark()