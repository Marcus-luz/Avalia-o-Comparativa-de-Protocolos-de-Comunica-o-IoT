import subprocess
import sys
import os

def run_project():
    print("=== Iniciando Fluxo Automatizado de IoT Benchmark ===")
    
    # 1. Executar o Benchmark (Coletor de Dados)
    print("\n[PASSO 1/2] Executando master_benchmark.py...")
    resultado_benchmark = subprocess.run([sys.executable, "master_benchmark.py"])
    
    if resultado_benchmark.returncode != 0:
        print("ERRO: O master_benchmark.py falhou. Verifique o código.")
        return

    # 2. Executar o Dashboard (Visualização)
    print("\n[PASSO 2/2] Executando dashboard.py...")
    resultado_dashboard = subprocess.run([sys.executable, "dashboard.py"])
    
    if resultado_dashboard.returncode != 0:
        print("ERRO: O dashboard.py falhou. Verifique se o arquivo existe e se os imports estão certos.")
        return

    print("\n=== Fluxo concluído com sucesso! ===")

if __name__ == "__main__":
    run_project()