import pandas as pd

def gerar_relatorio():
    dados = pd.read_csv("usuarios.csv")
    print("Resumo dos usuários:")
    print(dados.describe())

if __name__ == "__main__":
    gerar_relatorio()
