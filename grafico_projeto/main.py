import matplotlib.pyplot as plt

def gerar_grafico(valores):
    plt.figure(figsize=(8,5))
    plt.bar(range(1, len(valores)+1), valores, color="skyblue")
    plt.title("Gráfico de Barras - Valores Informados")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.savefig("grafico.png")  # salva como imagem
    plt.show()
    print("✅ Gráfico gerado e salvo como 'grafico.png'")

if __name__ == "__main__":
    print("Digite alguns números separados por espaço:")
    entrada = input("➡ ").strip()
    valores = [int(x) for x in entrada.split()]
    gerar_grafico(valores)
