import pandas as pd
from typing import List

"""
Função para transform uma lista de dataframes em um dataframe

args:

return:

"""

def concat_dataframes(df_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(df_list, ignore_index=True)
