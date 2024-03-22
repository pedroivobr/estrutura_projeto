from pipeline.extract import ler_arquivos_excel
from pipeline.transform import concat_dataframes
from pipeline.load import load_excel

if __name__ == "__main__":
    listas_de_df = ler_arquivos_excel("data/input")

    df = concat_dataframes(listas_de_df)

    load_excel(df, 'data/output', 'output')