import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminho do arquivo
caminho_csv = os.path.join("docs", "resultados.csv")

if not os.path.exists(caminho_csv):
    print(f"Erro: Arquivo não encontrado em {caminho_csv}. Rode o master_benchmark.py primeiro!")
else:
    df = pd.read_csv(caminho_csv)
    
    # Criar uma figura com 4 sub-gráficos (2x2)
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Comparativo de Performance: Protocolos IoT', fontsize=16)
    
    # Cores para cada protocolo
    cores = ['#3498db', '#e74c3c', '#2ecc71'] 

    # 1. Gráfico de Latência
    axes[0, 0].bar(df["Protocolo"], df["Latência (ms)"], color=cores)
    axes[0, 0].set_title('Latência Média (ms)')
    axes[0, 0].set_ylabel('ms')

    # 2. Gráfico de CPU
    axes[0, 1].bar(df["Protocolo"], df["CPU (%)"], color=cores)
    axes[0, 1].set_title('Consumo de CPU (%)')
    axes[0, 1].set_ylabel('%')

    # 3. Gráfico de Memória
    axes[1, 0].bar(df["Protocolo"], df["Memória (MB)"], color=cores)
    axes[1, 0].set_title('Uso de Memória (MB)')
    axes[1, 0].set_ylabel('MB')

    # 4. Gráfico de Taxa de Sucesso
    axes[1, 1].bar(df["Protocolo"], df["Sucesso (%)"], color=cores)
    axes[1, 1].set_title('Taxa de Sucesso (%)')
    axes[1, 1].set_ylabel('%')
    axes[1, 1].set_ylim(90, 100) # Focar entre 90 e 100% para melhor visualização

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar layout
    plt.show()