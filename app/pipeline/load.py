import pandas as pd
import os



def load_excel(df: pd.DataFrame, output_path: str, filename: str) -> str:
    """
    Receber um dataframe e salvar como excel.

    args:
    dataframe (pd.DataFrame): dataframe a ser salvo em excel.
    output_path (str): caminho de saída.
    filename (str): nome do arquivo de saída.

    return: "Arquivo salvo com sucesso."
    """
    
    # se a pasta output não existir, criar
    if not os.path.exists(output_path):
        os.mkdir(output_path)


    df.to_excel(f"{output_path}/{filename}.xlsx", index=False)

    return "Arquivo salvo com sucesso."