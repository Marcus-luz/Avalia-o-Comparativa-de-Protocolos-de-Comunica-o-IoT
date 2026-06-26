# Avaliação Comparativa de Protocolos de Comunicação IoT

Repositório dedicado à análise de desempenho dos protocolos **MQTT, HTTP e CoAP** aplicada ao cenário de **rastreamento de entregas**.

Trabalho desenvolvido como parte da disciplina de Redes de Computadores no curso de Engenharia de Software da Universidade Federal do Pampa (UNIPAMPA).

## 📊 Cenário da Avaliação
O projeto simula um sistema de rastreio onde dispositivos móveis (entregadores) enviam coordenadas GPS para um servidor central. Foram avaliados três critérios principais:
* **Consumo de Recursos:** Impacto no processamento (CPU) e memória do dispositivo.
* **Latência:** Tempo de entrega efetiva da mensagem.
* **Confiabilidade:** Eficácia na entrega dos pacotes.



## 📈 Resultados Consolidados
Os testes foram realizados simulando o envio contínuo de coordenadas. Os dados obtidos estão resumidos abaixo:

| Protocolo | CPU (%) | Memória (MB) | Latência (ms) | Sucesso (%) |
| :--- | :--- | :--- | :--- | :--- |
| **MQTT** | 7.45 | 34.89 | 98.3 | 99.8 |
| **HTTP** | 11.94 | 65.12 | 243.5 | 99.5 |
| **COAP** | 99.50 | 38.43 | 87.9 | 98.7 |

## 🏆 Veredito: O Melhor Protocolo
Com base nos resultados, o **MQTT é o protocolo recomendado** para o cenário de rastreamento de entregas.

**Por que o MQTT venceu?**
1. **Equilíbrio:** Oferece o melhor balanço entre performance (baixa latência) e eficiência de recursos (baixo consumo de CPU/RAM).
2. **Robustez via TCP:** Diferente do CoAP (UDP), o MQTT utiliza TCP, o que garante a entrega das coordenadas de forma confiável — algo essencial para logística de entregas — sem a sobrecarga pesada do HTTP.
3. **Eficiência de Rede:** O cabeçalho leve do MQTT minimiza o consumo de banda, essencial para dispositivos móveis que alternam constantemente entre redes 4G/5G.

* **HTTP:** Desempenho inferior devido à sobrecarga (overhead) de cabeçalhos e alto consumo de recursos.
* **CoAP:** Embora possua a menor latência, demonstrou custo computacional elevado em nossos testes, sendo mais indicado para sensores estáticos ultra-restritos do que para rastreamento móvel.

## 🚀 Estrutura do Projeto
```text
/iot-protocol-benchmark
├── /src              # Scripts de simulação (Python)
├── /docs             # Relatório bruto (resultados.csv)
├── main.py           # Orquestrador de testes (Automated Benchmark)
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação completa

## 🏆 Conclusão e Veredito Técnico

Após a análise comparativa entre os protocolos **MQTT**, **HTTP** e **CoAP**, definimos que o **MQTT é o protocolo mais adequado** para o cenário de rastreamento de entregas.

### Por que o MQTT foi escolhido?
Com base nos testes realizados, o MQTT apresentou o melhor **equilíbrio entre desempenho e consumo de recursos**:

1.  **Eficiência de Recursos:** Consumindo apenas **7.45% de CPU** e **34.89 MB de RAM**, ele provou ser muito mais leve que o HTTP (que consumiu 11.94% de CPU e 65.12 MB de RAM), o que é vital para economizar bateria e processamento em dispositivos móveis.
2.  **Confiabilidade com TCP:** Diferente do CoAP (que roda sobre UDP e exige que o desenvolvedor implemente camadas extras de confiabilidade), o MQTT utiliza **TCP** nativamente. Isso garante que as coordenadas GPS dos entregadores cheguem ao servidor com segurança (99.8% de taxa de sucesso), sem a sobrecarga pesada do HTTP.
3.  **Latência Balanceada:** Embora o CoAP tenha apresentado latência ligeiramente menor (87.9ms vs 98.3ms), o custo de processamento observado no CoAP em nosso ambiente de teste (99.5% de CPU) o torna inviável para este cenário específico de rastreamento móvel.

### Resumo Comparativo
| Protocolo | Veredito | Principal Motivo |
| :--- | :--- | :--- |
| **MQTT** | ✅ **Melhor Escolha** | Equilíbrio ideal entre estabilidade (TCP) e baixo consumo. |
| **HTTP** | ❌ Ineficiente | "Pesado" demais; cabeçalhos grandes consomem banda e energia. |
| **CoAP** | ⚠️ Restrito | Rápido, mas alto consumo de CPU observado no cenário atual. |