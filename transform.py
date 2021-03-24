import pandas as pd
import datetime


def from_dob_to_age(born):
    # Função que realiza cálculo da idade do aluno
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def clean_data(file, save_name_file, filtro_sigla_estado=None):
    """

    :param file: Nome do arquivo CSV extraído
    :param save_name_file: Nome a ser dado ao arquivo final, sem extensão
    :param filtro_sigla_estado: Sigla do estado para ser filtrado
    :return: Arquivo CSV com os dados prontos para gerar gráficos
    """
    # Abre o CSV
    dataframe = pd.read_csv(file, sep=';')

    # Remove algumas colunas
    dataframe_v2 = dataframe.drop(["CODIGO_EMEC_IES_BOLSA",
                                   "CPF_BENEFICIARIO_BOLSA",
                                   "REGIAO_BENEFICIARIO_BOLSA"],
                                  axis=1)
    if filtro_sigla_estado is not None:
        # Filtra apenas o estado
        df_filtrado = dataframe_v2[dataframe_v2['SIGLA_UF_BENEFICIARIO_BOLSA'] == str(filtro_sigla_estado).upper()]
        # Faz uma cópia exata do dataframe
        df_filtrado_v2 = df_filtrado.copy()
    else:
        # Faz uma cópia exata do dataframe
        df_filtrado_v2 = dataframe_v2.copy()

    # Torna o campo data de nascimento um objeto datetime
    df_filtrado_v2['DT_NASCIMENTO_BENEFICIARIO'] = pd.to_datetime(df_filtrado_v2['DT_NASCIMENTO_BENEFICIARIO'])

    # Aplica função para capturar idade dos alunos
    df_filtrado_v2['IDADE'] = df_filtrado_v2['DT_NASCIMENTO_BENEFICIARIO'].apply(lambda x: from_dob_to_age(x))

    # Salva dataframe em um novo CSV
    df_filtrado_v2.to_csv(f'files/{save_name_file}.csv', sep=';', index=False)
    print(f'>> Arquivo [files/{save_name_file}.csv] foi gerado <<')

