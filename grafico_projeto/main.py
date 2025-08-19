import matplotlib.pyplot as plt

def gerar_grafico(valores, rotulos):
    plt.figure(figsize=(8, 5))
    plt.bar(rotulos, valores, color="skyblue")  # Usa rótulos no eixo X
    plt.title("Gráfico de Barras - Valores Informados")
    plt.xlabel("Categorias")  # Altera o label do eixo X
    plt.ylabel("Valor")
    plt.savefig("grafico.png")
    plt.show()
    print("✅ Gráfico gerado e salvo como 'grafico.png'")

if __name__ == "__main__":
    print("Digite alguns números separados por espaço:")
    entrada_valores = input("➡ ").strip()
    valores = [int(x) for x in entrada_valores.split()]

    print("\nDigite os rótulos para cada número, separados por espaço:")
    entrada_rotulos = input("➡ ").strip()
    rotulos = entrada_rotulos.split()

    if len(valores) != len(rotulos):
        print("❌ O número de valores e rótulos deve ser o mesmo.")
    else:
        gerar_grafico(valores, rotulos)
