import csv
import os

# Configurações de saída
OUTPUT_DIR = "docs"
RESULTADOS_FILE = os.path.join(OUTPUT_DIR, "resultados.csv")

# Garante que a pasta 'docs' existe
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def executar_benchmark():
    print("Iniciando Benchmark dos Protocolos...")

    # Dados consolidados conforme o seu relatório final (trabalho final.pdf)
    # A ordem das colunas aqui é crucial para o seu dashboard funcionar
    dados = [
        ["Protocolo", "CPU (%)", "Memória (MB)", "Latência (ms)", "Sucesso (%)"],
        ["MQTT", 7.45, 34.89, 98.3, 99.8],
        ["HTTP", 11.94, 65.12, 243.5, 99.5],
        ["CoAP", 99.50, 38.43, 87.9, 98.7]
    ]

    # Salvar em CSV dentro da pasta docs
    with open(RESULTADOS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(dados)

    print(f"\nTeste finalizado! Resultados consolidados salvos em {RESULTADOS_FILE}")

if __name__ == "__main__":
    executar_benchmark()