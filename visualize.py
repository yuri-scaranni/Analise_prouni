import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def instance_dataframe(csv_file):
    dataframe = pd.read_csv(csv_file, sep=';')
    return dataframe


def grafico_idade(dataframe):
    """
    GRÁFICO DE IDADE DOS ALUNOS DO RIO DE JANEIRO
    :return:
    """
    sns.set_style("darkgrid")
    sns.countplot(data=dataframe, x='IDADE', palette="Spectral")
    plt.xlabel("Idades")
    plt.ylabel("Quantitativo alunos")
    plt.title("Idade alunos ProUni - RJ - 2018")
    plt.show()


def grafico_raca(dataframe):
    """
    GRÁFICO DE RAÇA DOS ALUNOS DO RIO DE JANEIRO
    :return:
    """
    sns.set_style("darkgrid")
    ax = sns.countplot(data=dataframe, x='RACA_BENEFICIARIO_BOLSA')
    plt.xlabel("Cor")
    plt.ylabel("Quantitativo")
    plt.title("Alunos por raça ProUni - RJ - 2018")
    for p in ax.patches:
        ax.annotate('{}'.format(p.get_height()), (p.get_x() + 0.25, p.get_height() + 50))
    plt.show()
