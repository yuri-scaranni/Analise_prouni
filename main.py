import extract
import transform
import visualize

extract.extract('files/prouni_2018.csv', 'http://dadosabertos.mec.gov.br/images/conteudo/prouni/2018/pda-prouni-2018.csv')
transform.clean_data('files/prouni_2018.csv', 'prouni_2018_rj', 'RJ')
df = visualize.instance_dataframe('files/prouni_2018_rj.csv')
visualize.grafico_idade(df)