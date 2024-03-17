import os
import glob
import pandas as pd
from typing import List

def ler_arquivos_excel(input_path: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos .xlsx de uma pasta data/input e retornar uma lista de dataframes.

    Args:
        input_path (str): caminho da pasta com os arquivos de entrada.

    Returns:
        list: Lista de dataframes contendo os dados dos arquivos.
    """
    # Lista para armazenar os dataframes
    lista_dataframes = []

    # Verificar se o caminho da pasta existe
    if not os.path.exists(input_path):
        raise FileNotFoundError(f'O caminho {input_path} não existe.')
    
    # Lista de Arquivos
    all_files = glob.glob(os.path.join(input_path, '*.xlsx'))

    # Loop pelos arquivos na pasta
    for filepath in all_files:      
        # Verificar se o caminho é um arquivo
        if os.path.isfile(filepath):
            # Ler o arquivo como dataframe e adicioná-lo à lista
            df = pd.read_excel(filepath)  # Ou qualquer método de leitura adequado ao formato do arquivo
            lista_dataframes.append(df)

    return lista_dataframes

if __name__ == "__main__":
    path = 'data/input'
    
    df_list = ler_arquivos_excel(path)
    print(df_list)