import pandas as pd
from app.pipeline.transform import concat_dataframes

df_1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
df_2 = pd.DataFrame({'col1': [5,6], 'col2': [7,8]})

def testar_a_concatenacao_da_lista_de_df_shape():
    lista = [df_1, df_2]

    df = concat_dataframes(lista)
    assert df.shape == (4,2)

def testar_a_concatenacao_da_lista_de_df_equals():
    lista = [df_1, df_2]
    arrange = pd.concat(lista, ignore_index=True)

    act = concat_dataframes(lista)
    assert arrange.equals(act)