import pandas as pd
import matplotlib.pyplot as plt
import os

caminho_csv = os.path.join("docs", "resultados.csv")

if not os.path.exists(caminho_csv):
    print(f"Erro: Arquivo não encontrado em {caminho_csv}. Rode o master_benchmark.py primeiro!")
else:
    df = pd.read_csv(caminho_csv)
    
    # Estilo moderno do matplotlib
    plt.style.use('ggplot')
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Comparativo de Performance Real: Protocolos IoT', fontsize=18, fontweight='bold', y=0.98)
    
    cores = ['#3498db', '#e74c3c', '#2ecc71']

    def adicionar_valores(ax):
        for p in ax.patches:
            ax.annotate(f"{p.get_height():.2f}", 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='bottom', 
                        xytext=(0, 5), textcoords='offset points', fontsize=10)

    # 1. Gráfico de Latência
    axes[0, 0].bar(df["Protocolo"], df["Latência (ms)"], color=cores)
    axes[0, 0].set_title('Latência Média (ms)')
    axes[0, 0].set_ylabel('ms')
    adicionar_valores(axes[0, 0])

    # 2. Gráfico de CPU
    axes[0, 1].bar(df["Protocolo"], df["CPU (%)"], color=cores)
    axes[0, 1].set_title('Consumo de CPU (%)')
    axes[0, 1].set_ylabel('%')
    adicionar_valores(axes[0, 1])

    # 3. Gráfico de Memória
    axes[1, 0].bar(df["Protocolo"], df["Memória (MB)"], color=cores)
    axes[1, 0].set_title('Uso de Memória (MB)')
    axes[1, 0].set_ylabel('MB')
    adicionar_valores(axes[1, 0])

    # 4. Gráfico de Taxa de Sucesso
    axes[1, 1].bar(df["Protocolo"], df["Sucesso (%)"], color=cores)
    axes[1, 1].set_title('Taxa de Sucesso (%)')
    axes[1, 1].set_ylabel('%')
    axes[1, 1].set_ylim(0, 110) # Fixo para não cortar os textos do topo
    adicionar_valores(axes[1, 1])

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    caminho_imagem = os.path.join("docs", "grafico_benchmark.png")
    # dpi=300 garante uma imagem em alta resolução para usar no README.md
    plt.savefig(caminho_imagem, dpi=300)
    print(f"Gráfico guardado com sucesso em: {caminho_imagem}")
    plt.show()