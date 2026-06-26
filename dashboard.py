import pandas as pd
import matplotlib.pyplot as plt

# Ler os resultados
df = pd.read_csv("docs/resultados.csv")

# Criar gráfico
plt.figure(figsize=(8, 6))
plt.bar(df["Protocolo"], df["Latencia_Media_ms"], color=['blue', 'red', 'green'])
plt.xlabel("Protocolo")
plt.ylabel("Latência (ms)")
plt.title("Comparativo de Desempenho: IoT Protocolos")
plt.show()